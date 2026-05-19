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
<img src="https://cdn4.telesco.pe/file/f3VMPlIyDI8GrdF3Rvwk9HGa5EhoFl6HI6QF07wJIC3kj3Af7oHmQDFma6-5L6wXA_a_8FlRSzoARvgz7SVcKJXMFWwQUUUEbvh5cSyLfZW8QVJeRxKMcMEVd0oBxbmOu7zIir0GzofuXfmZdm46B3QHWmOiJV7ZyXOMTp9VYOAmJg6MkH4eqFcm0Q3XqliHbM_FGx0y2OlnlIKSYAV2-L1K3viuWesKc8rB5jKXjz-e4RfbslVlznrjhoeV3doxXJwH-BjX4EbKZH7oPtrbQdS4M-LtDgLar8ysQnvEOZfcoT0rLsrkzrEwRjBGeit8vld_rweloPr488nO6DQbiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-436545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV-htBxLnJNn5VRQwFJXxBLG6bm5nPXskT4wXbD_lvgp3yYVti6ZHyJYezAfpjQeCcDzmyydXXEHtYvQsklzgW7njPSc394Lrn7RjCFoTnfnn1_SIGu4wb31sjcJw6Y9GcDiv6ak4faLDYG4NLWnu-7wOFa8Q-QYKY3DLCxNlF1g3goat3thcxYpAfBU2esRC9MgYBRwTMVBM8Br57Uf-v5D6SwfYxwCn6VtE3rbaScpbvjq9oYSSR1z154AArjg_OBfv7zHJFbYHFulgrJZNMzszY1mlfonyujnq2EnYUSKWvOKYjoFmXQP3sYTIMuuCkuQ1XI9ZHvShzCNUrdaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhXnQqST7dbJ4a83u6lLAcOLE_TafwNKS1580JDzbbrbQ85goG3lpRnWYJ2sqgQb9WRbiV05CF56p9y344w9oPM50T99vGjuG3r9OrAYha8MQM68cMUmI7F7jJB6HmlkIPRXmdugHwqarCaxyrMknopZGYLmfpmFtIu7mdpsUr8sMk3-SD_W7GUhZGIoldTqt_aYeXI_oK_69xFwMKj-LSY9yflhKIRBgszOGZv0-7R4XkP6jWZiAroT051DZcv3gtHeS8HpBKV7VGh4xseDIR2c8Qapqifrc4i1evddRtN_amo2lXNB0MDUGdk5NB68d4lydwcRjGjDU8oV4ZF76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pECgPSQn7pKZChvYUgzW7TQ124MWsX5EoiBTJBKJPvCbJSeUTRQ30sy4-SiQmUumYFzPzPGkOyVLwVxxwMqcy0wJiCYbGEHZi-QtGsRgPHLXDpzurGC5udTSrLWPEI6NW5tr6DuZDd69zsuKhogTlBUniQJec2ixvLuY6PRAwzN8SQ_rWUdokz9-PZl75gF5X-EC44XQxiRga6KGjrJsLBrUUpjceNS7PlM8-zk8qoojEjuU1BMagmJh-YuQenil1RR5kS8w2IeH637ANH9JyCd_R03c1pTxKzYOghGcJShluYCU4Elaor7jnDMHQli0qdxpt-h2CLdbPrmzarhXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksn3bzGVwf6anGrU9btUzibLL1LjvcKZEJX07_tbiO7niyoBxkFRd98soy4_cN70xfTym-rBekbFXY89pvHLKnyqjq6KUfBK5-Pqgsm_8UugXkNW0uUO4RwNmc5wtkcI69QQhw-wNaBmE0HYzIDXq0bgX7KjO_7hJQxPwa_CUGtxIcy8eRjROmB_19f2azsPL58oxC-kFOzO9OO6Fk2gkZPxxcv7vjMnLM-9gKgT7Ug5s7QROsZTZE8J1sM1VYl47qyTNTxNJo0BiPkVytUYcKGzNRmiylHU13COPeQ22lJkZxu83Y1BY55xvN9o6KTmNO3CnrHRlB8YavB9CgNS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMYMSKGsBlTG51M3JCnTdRBmmoP5LGaZeL-xhnqoPsf_eC48ZiXXOsj5pqkk3Du7qOVtWhgwzmvxoVTUh02PVpvLu7BDS0wkZ-sSDgTr-gpipdiCa9FNCeNe8U_rgBaVEtKTTkuFLi-a1HVyo1vxXix1MXCKohveEZvDs5CwCkOOUKNHheSaMUzs-4OrLsVRTS_t9zmMHVJPf5qSwslAIsjicIwHWpMSXxubPfjnNejfpCrVPH_zH7tHMcqonyXEuUFJl8CWU6AKFIRYKIbkxCP0WnyhIJr1JjxxOObL8B0GeqDuUirJ0SK_oSTdxV0ml_hwcGNCmrA55yVZXSk67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXi7A0u0ORuNtJXz4rQaZsrh8C5YtlFj0VI_fJSSHWlsf38-kpou2yqQzCVT8WVQzVtGZogT2w3nTuBsClDVgZte-T0RnfIJyMOKFMBlTxDxfRdc__zILSTTOFxyWbubTcJxtEbxemSGVcjA7Kbn7cgI2G_zBoIRHUiwtJNYuP2BwWtfSjOXDUiju677DSkoDdvfZbclf0TOsmy1jglq4KpymL5GNWYqw5puMcuJXX8o10AwzkR0q0BiCvPNNTN9Abxa0vP0FjDdC7HnLWd_gqmtcyMZff38t2dvbZdr-lYveXki8SRGUYMPioUMpHxJGELjksoEu7w0E832LPLuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olQ26UGpN1tCfFd1UXcj1vHUL14qddpGfvCegBibRTSBTZVl_z470sf7WNvr-AZGxKeXUK3w-F-6ULDimfNoZXpR0Nldyr6peZmWXCiN7VFlLATCurYowjTWwBiGhB1_wOyX3r7Icc8Q_iRFMkGQLoGpuIWY25Z6xBfgyh5e9_4Hl_OW9GflvEM69qxuM-kYg63M0Ylq6npekYPpXcnTFD41WJMhCdAuD16UMzpQK3f3iJ1h7QdR712d5Yx5vMyfFoKDCayRYoFM_ZcjBF3ny-bxZrJIgf_3MN2BBqEig01NKaNLJtHrASZm75rXWMs-4SN7LykeQlUIqKVzJF1Y5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عروس‌ودامادهای جان‌فدای سمنانی هم مراسم عقدشان را در میدانِ خیابان گرفتند
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/farsna/436545" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy3vCaQkISy6GiBoXb1H2pqjEp_zwR6_F_0U9f_6M-T00gUjnYBwjuVxW2dY4QrDaiHI6ayX13ouC7i1n_QnaM-ItjFG_mpgNPjfe583HOxDxPJ1uT-GR5ASRY62ypYqewd4t2dqkGzKOs0uoviAhK40HCy3A2GBD5Bj-s2rsePgPFBoxM6liw3brbT2iBVU9arEpDzQgV3NO4kQgwkVeNKpYJ1x3bXrZLRaU0UrTLh4oJlBT-7mDeWRKTSFzR8xH7aJPtZeUJTnB00lyHCnR1vxPVWGRYA6qBHZgXBNAMMRXxaGhd_5NqQrTDQSqm-NuKT0OxY1IN0DclBZaLDmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر دست اسرائیل را از دریای سرخ کوتاه کرد
🔹
طرح اسرائیل برای تسلط بر دریای سرخ با کریدور زمینی مصر نقش بر آب شد. قاهره با همکاری اریتره، مسیر لجستیکی از مدیترانه به شرق آفریقا ایجاد کرد و نفوذ تل‌آویو در منطقه را شکست.
🔹
این پروژه که بنادر اسکندریه و سوئز را از طریق خاک سودان به بنادر اریتره متصل می‌سازد، عملاً حلقۀ محاصرۀ اقتصادی و لجستیکی اسرائیل در شرق آفریقا را تکمیل کرده و طرح‌های تل‌آویو برای تسلط بر کریدورهای تجاری دریای سرخ را برای همیشه خنثی می‌کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/436544" target="_blank">📅 05:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWhzVomEePCNSvqc5tbV2ZId3lgyGbwTAPa64uniwUu0iPhG1V9aOt1h53-BwQM5X4f_fWQSUZE2bpghfY44noXroah-oMc3rza-la04Fkux9GlKrcIOAFn48CBP8ukTJKXb8vZh3DcE2ATEkCj19EdXN-6bMN3ztzbUysliqh6HcKgMnIZmDydF2gBJkoxb9qUpvTrUS3gpOL0BtUs2kIW4sa8Gil9o-DhDHdQPWObTDHuTt72eKvd5cQDdiEnoDh10llwmRVqZ-_XcwfLj8EoqlEH7-hqjPekDfTB6RslNfPBWWVzOswjJsIhr99mayFa68tPd8L7uC4xk5W4tPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالتیکو: آمریکا برای اقدام نظامی علیه کوبا آماده می‌شود
🔹
منابع مطلع می‌گویند که آمریکا در حال آماده‌سازی اقدام نظامی علیه کوبا، بعد از ناموفق بودن سیاست تحریم‌ها است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/436543" target="_blank">📅 05:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از نحوۀ ازدواج‌‌شان
🔹
این خاطره پس از پیروزی انقلاب و در دوران ریاست‌جمهوری ایشان، در گنجینۀ تاریخ‌شفاهی مرکز اسناد انقلاب‌اسلامی به ثبت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/436542" target="_blank">📅 04:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676233c80a.mp4?token=HorGVAY3TgadeudnMsST4KSQTthHjlmO0VcBe8XQunx9iBucRPmubBCa_2WpRUT0znk3L87uEVGfCipQIv_W-4zyR01QWCaH_HTnc5Zkkt_oDrj9RUEWj80cLP9LhqQLg7VIxb9Oj0fsjaotVSK8OWpvmPKBnE-ry-pNkYaPl1bh4eASfVvpAHqQGEMWuefyLqpM7ZKmrfsRTltO39il6D3G7L2yv1-h9tKuwVppjhyxiMoQj31FKOZJg7AYa9NUQyHlyG_r7iOorytC9jL-9qDrsWUVKQ5TuhGMXJYIeTehBHccyDnCiU0BDwnszk33cqENf-IHq1bg1lz3YLnhAgegQePuNbF9HG8FFuXXOLXbta1w6QSQJRrem_CbTldvaJN2pE4Mftvpde6n7lKJTVHoYWaSAgxsDWQ1kY_xSxcJZoKGH86J2FBrBNAnlcYWvm-C1EdUlMM2gH7WOLBtMVKNF8dbIbl8AC9mNj2XKe3Le0mIHgpYlE4oXLM2QFMaDxUCIwTZ6CM7g1c9C2NDhIIdok0OEeWBXn-KZEze78qBStJB8XwXP-hjzwlzgVXsKBL5NkSeYLPHMNjSbaEtFQBsbY9OIYvhNRIjR0HqQhXpdnC-GZH9j8rH35uY3NA1xX_y8Af2GwPaO7UjFNj4-gapAvIad8_4_CNGRMVGgMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676233c80a.mp4?token=HorGVAY3TgadeudnMsST4KSQTthHjlmO0VcBe8XQunx9iBucRPmubBCa_2WpRUT0znk3L87uEVGfCipQIv_W-4zyR01QWCaH_HTnc5Zkkt_oDrj9RUEWj80cLP9LhqQLg7VIxb9Oj0fsjaotVSK8OWpvmPKBnE-ry-pNkYaPl1bh4eASfVvpAHqQGEMWuefyLqpM7ZKmrfsRTltO39il6D3G7L2yv1-h9tKuwVppjhyxiMoQj31FKOZJg7AYa9NUQyHlyG_r7iOorytC9jL-9qDrsWUVKQ5TuhGMXJYIeTehBHccyDnCiU0BDwnszk33cqENf-IHq1bg1lz3YLnhAgegQePuNbF9HG8FFuXXOLXbta1w6QSQJRrem_CbTldvaJN2pE4Mftvpde6n7lKJTVHoYWaSAgxsDWQ1kY_xSxcJZoKGH86J2FBrBNAnlcYWvm-C1EdUlMM2gH7WOLBtMVKNF8dbIbl8AC9mNj2XKe3Le0mIHgpYlE4oXLM2QFMaDxUCIwTZ6CM7g1c9C2NDhIIdok0OEeWBXn-KZEze78qBStJB8XwXP-hjzwlzgVXsKBL5NkSeYLPHMNjSbaEtFQBsbY9OIYvhNRIjR0HqQhXpdnC-GZH9j8rH35uY3NA1xX_y8Af2GwPaO7UjFNj4-gapAvIad8_4_CNGRMVGgMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هفتادونهم مردم توکهور و هشت‌بندی استان هرمزگان در دفاع از ایران
@Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/436541" target="_blank">📅 04:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkXjBclBsNUIggpgNrsW4K1xqOBbiyd-iWTocgDSW_o0AcjXZzwVlwzgsu6a0tRshKzOSa2lrDFjSpqa3gwiNSo3H151KFXxIcHTxY7VqqHBmh6D87NWuPGKItEjZugqNDYdIcfNTyaXMwkhA7ltgLJVgGxIdwdB2PfGW9X0ybgt3-Z4Yklqal2x73UvP-F2BVpUSD24alteu9EU631blgI_LknVd19xYc6fDrxzsFeur-POBUfTPTd-1X8wLyf5hR99WjYVY9VqPvl3SGwBG0a-J8i5MjD27YosQ7RZPSGB5vn9Wfc9HSmhK-_jNM1WdgLqBS6doA7aSibkTJLicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2viyfBO9zKq_LvBttuShkNsDiEtAxGBbTNWHRHFXB1OiTsmQ0lmKKpl7S1a-pDwTMetPg4OflYPrxyDSbaFrZtBMa6bI4O6r9RHJaAVLfI6Ga8MLqQg4kYoHKq6ZM_ZTAW86lkbGPMjQkTkkEHp0YcEbpiCPEJj7fiQEf0kzDn8bIPpfVsfIjCpjnE929kIgZJHP0KQWkJTPOB7BnmCxVB0jr3EBnOTghZ38ZIU-TD9g32HNMJQaFuvojOo5cxKAKcDr1YQJ5hPkHabRkxMnw3lTwnuMtEf0ShM0qmPIsCx8yOCxfmNgoj6S3wAm5c0IIXXGSdgpFaDjcUb6VchNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTMgSOEdqOu_4icdscE78EU9DDTyJ--wClJBw00BrY6zQr3OKz_YtL2ktQ7djlxEmpQXQSxddgv8_PuBDYZwWO4Q9nAjmciFHpWLuEM9MPoPBrE7bh8iynGaAir5wlsuGG9A2RZlcG77hbFnl2CcIvS3xALSQdoV48h8Nb5idRVRhX1E78k0xCurc7J1NsOWtOfBr7NXZUA5qOCHdIUxn_EFTM08GXFaGyFtO2vjJXQ2hNyb5TA4A_P1rvL86eAHRUfO_93NrC1eIHtETGCkSmecCMDC_Eq2x85gLDWedTwdh6weoRMGbm9CbHvBNlFmb7wC02JxEvFkG8WUTeT0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Izl1eVSDwi1UOZXjrktyo_Z2fweRpVQ7AJgfjoCOoJ5uLuqQ2-Y8FFXCfs3mf2cXA-Pas_VZ04TH6hIN_dT8Xw3byuz1WpcE1XQ-m-0YqstsnXJbPFrZl--5DZ_r5QQlDVPmRwfeBMK7CctxJ14VUDrDXJ9-bFT4u4HvVdIbkWR_xLhkmINuN04mxkGWePvbaWHtv3znEvhfb_A1bbq9FjpWiH_P9Gz7-hmzj0fu474U_F5wm9a_lXAETwrMNDPZg2zt_yINoBP3e0NXMWkACkKWL0u-jNt3E57d9vQlFgbMJwlvNjCmHwAhF3vho5HLtaCM3C1w_eQFSC5m-Mkq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmUMMPwVb6YQJxnGJmSsLLNtjzWnb4Hva5d5ZP4b6v2350O6hfdCM-Ny-ExkkuW4mE2J0lwd_KUQRZs6T49K1PV9WsruLYjsnYmmuL-PWPUj1Nu92ipi24he5q0VXE9ctEBeFw38WLoNs0KUl8LIpP_NURPFuvt6vFlhxVEnuDouIlp0kG0m0clZ27l6JzII72fQik4FuZdgLwyRCdMua6YM2YLAur5D8-0XZmmyvIoXiqtDV7s8w6fjPNV2YDjHUGb4ibJnmMRgP3ka3Dboe-gNG7YwMwcNPh5nNHqzyb6Nlq76RtfxA6AF7EexsXTBtu0iWqz_ufZ8Apg4r6s_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJZpzTsz2sq3hFzFMwT7fE90a4GQRhJf-iD9sLii7_i_pteGBHNviUkrFVXGIdmPo-kwk7pk455wcl91ZqvBHWMgHeuxtDBRNRVDyX4K4auYVTxpIrDNHLQIFKOtg1D6-YBY1nvqyR13BSoTcY57609rjjm-UUy7j4rZovkS8ICjhV4oz3z1ayIMGDmC4et9IxeSkTsnMYyydnMDMnLH-dJnRyW_gncZIPjliA72lFWPoiUjzNjNTMkwg4yfhVjDNk9AVC6mfRx0l_OCinmnMaf0Rd3f85QG0RblJE-_OS0PF_VILdnq0c0pXKxj1DwvuUaw6PuV6_oGYIC9BTEVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikmj2MgPomfP9T055IUicS3VLG1v6s8Gl9_EyvlLbc6N941w7XjkyKww_cYP6t5IHVbkKC9VWBaiGFed7h6XsQQNkdCufREGsNGh9rwfW0zDPBlZSFlmwCcQtfDi6pn4c-UbHjuw2BzWFxBsSN4nEARqwR0XjCTrb90NpFkZ1yPFlxwRb7XanG7VcQoj68ywbYR5WKAwx_VJvXUaxKPHMpbQaKnK2rVa-Mb58qF0VtT1EpbnKUc8jluVvkQ0msvYiJa1vOXrudoFyQyDQXBAbctLL8RZT8hqeuURbxw22y8E1ogBPSL_wbvMyofqc1vM3bgyPUkx2WxpB9s8EFGMug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آغاز زندگی زوج‌های ارومیه‌ای در آغوش ایران
عکاس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/436534" target="_blank">📅 03:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g182Kglx2ER4tvI-9d-oL7a2W5jt5bE_nruHiswdkMLOCVzmUU9MXDKVw4euQxZPhDkw7FEOwlTqUQhRmpz5OQl8zQFebYKFqSm3jRAdTeIqHO63heZBZY9606kMZqsvM29xP3wfNI7i-UtZtIK8aPlD5ri-Ks_jjNvV5dSqD_rGYiQztLq8N7Jp5Q8d2yuMxNOlsYbcAnT2lKB8_NW86Uta18froZmXMjshHExTelkpHYhrNaszguEQALN8gQuv9Lq-sPh7k6UZIoOnALaTwexxXGhxehb_zB4kRUsfry6Jud4juzkWgUR6CB_a-NB6EDzUeO9wzMqiKn_eCx95mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز دادگاه تاریخی ایلان ماسک علیه مالک چت‌جی‌پی‌تی
🔹
به گفته رویترز، دادگاه رسیدگی به شکایت ایلان ماسک از سم آلتمن، مدیر شرکت اوپن‌ای‌آی رسماً آغاز شده و توجهات گسترده‌ای را به خود جلب کرده است.
🔹
در این پرونده، ماسک گفته که اوپن‌ای‌آی (شرکت مادر چت‌جی‌پی‌تی)…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/436533" target="_blank">📅 03:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KamxeNMqfTGOfgPIN8sv79tbnfMhhVPxjaUug8wjJVrjqTLCYrCC0_qy5XZXf4k1t-pHgszz-kY5bsrKQKti--ugUNVfkFe8eRXrZIl9m74L8qc4XoDnJMgqqnXwfQAQvHSKg4hEg7w-71_DzU3M7NacvFAz5C2BFg0WJRIkBcIB4_3krxFP6h06YJRia-_hQT8jo3NbxxmZhFWwuoX_rFTjVoZJNDZYyhlDa1QZtnh_VdAYCsghv0XV8HjI7jeXCTgksHEbDZPy19b968p04-XuFQ5uBBEXTlXi8hS4ed8B7AIsKAMMa7VpAktjwUOvHPHqWEu9nYPDb8-2qT7GhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: ترامپ هیچ گزینۀ نظامی مؤثری برای پایان دادن به بحران جنگ با ایران ندارد
🔹
برای ترامپ عاقلانه خواهد بود که توصیه‌های جنگ‌طلبان را نادیده بگیرد و به‌دنبال توافق با ایران باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/436532" target="_blank">📅 03:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPN6pf3O8erOcrjHOp7f1vaft3qc_orTG5Wun4cQuJrjB5vHoOU83xo-8xti0fmH_fDIX3o3xPhBlLRphJHSE76ldN-qVcuCfEucZJ4p7UPOhkQQUZ-rJ4tKV5yvoDAye6wWrHAVj9I30Z6mCmjzArYRWkmPkJjCKBJzTS64MFuwCKU4ZPSOPjBZxproynIPuqIweG1dWzkVU326gQZzyLMER9vcRRiTnSRFac3Fnrfz3wwQGWd2LpDXQ7SlVzJT0fnipDSo1_LZ1cxdkQrRPM6UijSJ2CLHUMeDPyVzq0t7SUKxvZ6CSy2Ju-7EAJhkGW2HDJQ8Fjm_62N93hkn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IK0GoA7nV8vBQY_WBHd_CsYvSHVaZJ5N5OYAAbVDInl73STO7yQfOi_tBK87BPcOEroEvz0ATu21Bz84Ch4HsnEiw645cCXKL2Jtc6r9oS0_t0FbH5q2JiZ0kiPKOfpYe_OuszQGOpn2YVXmg2NglJ-N0gdM16eJ4zi6UW3Z_X_9T8uAmHUVuVAPiD-s752bUaECYVFaIS0OfXnU8_UWF09pxnZ_vMoII4puHSnBMDmqjLJ4zejhEqvfxT8bKAZGGh55TGLfBODbhlRH708D0uRxq0XCGvMASGfjN4LPvB0M92D7y9-4VO06JO-YYIRH9pHjcDe7rWbJCeTJiI7qCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlGyEMkSpYX6j7PDR35YxExeHv86-Wd5G_mbNsGWLRWQqBpd26RnV8k_WXQH0DmWjsFAugUgsyjXtDQrdmqgKqMdOVfLI5HsZFm5PQ8L9lpShB-BLeqUxZqcNnr34pzwE9tDhcNJSI_rWbZfXWh6nBVW-XXxlVhl9j76tyqdv5TiLCYbAy6SvAHymOY9Es6gNh1e3YxuzzZe8yCa_uh3FW8Dvqa9sWn_XFwe5YU0L1UQ4OEA8e2NJo72DMv644-dGoQsb2Gp9gjsWb1N7FB0mIWJbe6d4zt33lxZexvBl4CfCeGw9BFPbGfk1Pl8BiRZWRMNNOjUG6Wmu2YgGPxFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0vt8JBQ55xaYPdP6F54sABRNiww509m6d8hmWSG-o75FsFl73FkS9ooH8anHb0pc-_r1U4uiUf_e0LokHw4K1xM7T39srw5sqvy-OGR0yCZQzTC1Fm1QsJx5H7o34EpBjo_6CBQDLY9-EgRFFzqUx7p_-qevsoaYowTCKScv0JHZ61mPGjJc2_ol_dxu2UnnNHVcfOuu407wEOHJ7CBxcONQDPzwXnGZb6Bj8yGb2GzDvkfceKXquZxcmD-8N03AzsHxc4EKWq3v1getZejA7VGfJnz_9neHEs33tTnXT5EEs_Au259p46Am8FfZBI14YFL8koKpmCiXR8h5BiiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDLCF-4ljy-QoJsW8Med7dGTCIEnTU9F44vw0G82tQLpWFrEIYxjDaEBYz8pFSoV_MAIfU0D0rPIuTpQQsSQgVsad-F6wFqeS2NjtizEWvSInEHbE0F77wFpuneupPmJKuHBKodHWKIYLXwnP4i4S_tmh0mZJ_OpnX1NxUflYlRD3IwubIMhtbhKWm5VHcwRZ9fgo8uHv6X1dWX7HwyTdXQhX8oS57hHLDgYHQcZmnBrW0tK9zwaB_Bii5CQ4dUqqXl492myfj3ry75TnFgFQ56Ggi4_Z9sbp2pngtiTSejcScixZBVvw39T_c4520o8_srpgK_LeOu4rZIG28nppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBVyYQpwsxovwM1w7i5xjcIwldm_bPCvqhW-ZboRRZ9QB41q4-RdjFcYhxZXOZ2A4dkMdjAMX28CzT4MrJ2LNTcE8dsRl6v-JDNQZ49LlDe-dEHnwcaF2f-U1qVynIwssfViWsKwbA-w3YjQRTM9UgQcjbCHrbnEggPBN3H932ovPfUWfpVrrZwEIWP5Bl8FkGQ4SCexk4G5ajJZu7O8qBOeCnViUb3NaI6WplTvaGptQgQaFwKSjFoTGPiyrchihLJXGjUAkOWTp5vP-N81rftvSgasGYa0zLoLYCWFjYourMF-4aIQj25nqttErGvinuGMVVpgC84DssC33tJXaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیوند ۵۰ زوج جان‌فدای کرجی در هفتادونهمین شب دفاع ملی
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/436526" target="_blank">📅 02:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8OBbvTHmOZALM1hiosgF6ZTP6JfuJljTD4FJGowA9deCU5hFowI_x6OkZEf1OsCsaZZtl0ExjfcuSoVm-k9Eul1ZxKSoegKCehZ8CML8w-tt0TVsr4Evv64rPocHqRcPVgodXkzd9sHjphH18qXY1mTPODjlKxw21mupJH8cpzsNUZinqrelN7PxoH9lTsTBGRY-tQKz2YJNiT53usnqLPXkC2KtAvypjG6RyvvFGM1yh075yDAuVAg3bhdw2kjKy-3HZOZX4RnH1DhaJLs_mswbDwwhHD2F4iweaNnxn9h2W7SwX5fAZmplDw0Dd0AVedsteQizZf65bhdjMxjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به یک توافق هسته‌ای با ایران رضایت داد
🔹
رئیس جمهور آمریکا گفت: اگر بتوانیم به توافقی برسیم که مانع از دستیابی ایران به سلاح هسته‌ای شود، از آن راضی خواهیم بود.
🔹
ترامپ در این‌باره افزود: ما در گذشته به دستیابی به توافق نزدیک شده بودیم و سپس این اتفاق نیافتاد، اما این‌بار متفاوت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/436525" target="_blank">📅 02:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/forG8qhqK0RPO6zCdTDUzNyfyooLkLpjSK2I_3bPKBuyngP07t3eXXTGoNeLTTnGCwgaSsaul5qZ6h0I5_BrFLXSKK23Wuw4Dj-bMQdbf5wqTYcDW87305T7ibcagkbJrA14k1D4QY2MxhT17-WRXDIREwCxtVHdXTY8ZsiqOEkJcnnpfCvd3MXihVZuC-0qeaGZhkkPU5RkhBZoEhq7Hz5ZzQRC3eWXFEuA8AIk91eZnlOQvmYasH8arsBVP20BzVBCBsPv-WxxMbSg0WHuuO9rV_GQJHloI3WyT89Ny82QL3A21O6nP_NcDGtEb44_bl_2EBz0Um8ha5H2PfO-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس انرژی: ذخایر نفت جهان در حال اتمام است
🔹
رئیس آژانس بین‌المللی انرژی اعلام کرد که در سایۀ بسته‌ماندن تنگۀهرمز، ذخایر تجاری نفت در جهان بسیارسریع درحال کاهش است و تنها برای چند هفتۀ دیگر کفایت می‌کند.
🔹
فاتح بیرول گفت، قبل از اینکه آمریکا و اسرائیل حملات خود را علیه ایران آغاز کنند، مازاد بزرگی در بازار نفت وجود داشت و ذخایر تجاری بسیار بالا بود. اما جنگ به سرعت شرایط را تغییر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/436524" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a8949187.mp4?token=c-mGnvBAMP16I9WBsgEiFhUuvZLwQbTokxL7GhEIglzB0-Gy_6h7Y6j8iGdyxulELXRpGrCKQQ_W4vMrrP3Fved3LaMcsa_HWEWunQnrKPEsJJ0EZKYyvw39cYc9TqFif11mkh0CQMQDOgWKGNT-Dn9d8gkMaXRxfWpSY4TPHMBJHZbyeRBrGVB3gbPU1SnhD4Hu25AEY1VEJjL7ZZTwZz7zAtVpZu0QNSk9ijZQIth9m_wF8ZgjSMoiHP2KwLjqSg3qeXoUxku-_gslaF0E9QhCV3VEIVVlR-04f3zmmJfgHG7n--3I9HAQM0ojwRZJsjLTxipnvYXXGil7mTANPWkxxfnJEOYu6e_ekGs36ns4f4j6dGVR7B5rUA_4RqUte5R1GYFsJfMrGM5u2Bt4Zb8MS0_ApzSeWVeTNV9DJEMUVHRs_HYIKQK8FyZI5MnkYYVHCH9rFQ24xo_8NT9DrC8vFe8RiVdcZAnyqfS0T1JMq4IITauRALKdLLqjQ58fF9-d1BC35PgVd55E5m3LPQ3sPKG160Bdv4cfd3T4aiJFr9TIYviUbWEr7bX-lBT83ot8dAhl6siqAwMFtwXVGnVuydpHpp-y6yUfbo_6msXMklMDNolk6ThvvbspUYzponKtYw1DxqqyKV1Jgi0RbY83PDB-x5KsrzHrHMnQIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a8949187.mp4?token=c-mGnvBAMP16I9WBsgEiFhUuvZLwQbTokxL7GhEIglzB0-Gy_6h7Y6j8iGdyxulELXRpGrCKQQ_W4vMrrP3Fved3LaMcsa_HWEWunQnrKPEsJJ0EZKYyvw39cYc9TqFif11mkh0CQMQDOgWKGNT-Dn9d8gkMaXRxfWpSY4TPHMBJHZbyeRBrGVB3gbPU1SnhD4Hu25AEY1VEJjL7ZZTwZz7zAtVpZu0QNSk9ijZQIth9m_wF8ZgjSMoiHP2KwLjqSg3qeXoUxku-_gslaF0E9QhCV3VEIVVlR-04f3zmmJfgHG7n--3I9HAQM0ojwRZJsjLTxipnvYXXGil7mTANPWkxxfnJEOYu6e_ekGs36ns4f4j6dGVR7B5rUA_4RqUte5R1GYFsJfMrGM5u2Bt4Zb8MS0_ApzSeWVeTNV9DJEMUVHRs_HYIKQK8FyZI5MnkYYVHCH9rFQ24xo_8NT9DrC8vFe8RiVdcZAnyqfS0T1JMq4IITauRALKdLLqjQ58fF9-d1BC35PgVd55E5m3LPQ3sPKG160Bdv4cfd3T4aiJFr9TIYviUbWEr7bX-lBT83ot8dAhl6siqAwMFtwXVGnVuydpHpp-y6yUfbo_6msXMklMDNolk6ThvvbspUYzponKtYw1DxqqyKV1Jgi0RbY83PDB-x5KsrzHrHMnQIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن ازدواج زوج‌های جان‌فدای نطنزی در میدانِ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/436523" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=Xa4K4lzmOrL0w-Xpp4cysLsql9i9NZBu4tsMf6ozNYbaNAA0OL1yiBMZ5qw08AlkI6LTXCwVIZGmgsfECdWihAvhFrDi0WVI60kqNiXHz6IHQVikqWn_FglIuK_Xwa-y4yHT6AIvmhi09O9umUEvjNGOnYPuf26vX9FJBmYlRyevReqBGD6eYeOKFO4DXwfkEvoqsGd5rF8U1zvcs53qJUrr5tM4M2-LgfbqRFbizFNeYMOKUiVRxsKQAya8Sf7QM1oqYZtXdgEzc-23aQY8Ql0hiqJT7fbhiA8EKoj3M-E6zll2-XKKeD9lGfK5Rf26iX7O2ripfBSoNLQoHztKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=Xa4K4lzmOrL0w-Xpp4cysLsql9i9NZBu4tsMf6ozNYbaNAA0OL1yiBMZ5qw08AlkI6LTXCwVIZGmgsfECdWihAvhFrDi0WVI60kqNiXHz6IHQVikqWn_FglIuK_Xwa-y4yHT6AIvmhi09O9umUEvjNGOnYPuf26vX9FJBmYlRyevReqBGD6eYeOKFO4DXwfkEvoqsGd5rF8U1zvcs53qJUrr5tM4M2-LgfbqRFbizFNeYMOKUiVRxsKQAya8Sf7QM1oqYZtXdgEzc-23aQY8Ql0hiqJT7fbhiA8EKoj3M-E6zll2-XKKeD9lGfK5Rf26iX7O2ripfBSoNLQoHztKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
@Sportfars</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/436522" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
مردم کاشمر، ایستاده پای ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/436521" target="_blank">📅 01:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceQf9_V2tHmSt3VZwZa_UxZxFUbJzWBpnsE3KJjULn8QlULJmWxJMGZNu9qtjNokerWZms3Y2MnG0ft9LL0wJlt_QeK3xlo9S4daFdowW8lZ9tzRNinJ65N6ohi7_JvDazyDGm32DkWI5ev7m5pcrD5s8cSeHQSy4I-EccqZaRFcZYw1Y5WFAbvRvNnCkwWZPnEoZi4m6g1i5w93XGVkYZUDI25rCthj81HpKxJJfefQMlBD-RG-2RaJMgUoeO7n4P3TCjCBModNFqe3wgpLEZnTJkNysvr3pbe90Fv6vxrtid6G3W10pqfQj2rEQrXQO2QYL2DaS66Bt2LRqr5rDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vq3jWKbA8R4zUMqTumOdXQl7iBgWZqsQjHXFopR91fE7-X9sS8c9nFj9LlqvdqaCWQcJNP5gVa9oqnwJlVajIKSxstpp64fxv_knYWffMwtGyP8g2DxfwCgneRNAdgjCgzOBhvGx5_AmvOfB2Qbd_zvgndJeHM4Km2F56a2FxLJGTqEptcHPgQ3cs8vAktlGtOVgUg3bEN6BpEYovFum9dU-AlIvce2vqhNA71hEP3SGVRZf8sz-tRVWm35Z_cT6GCfKVLLXX-kUPpTVI4Q2qFQ3aK3Rbd0P7N3NDk370iRw8lwY0xQ-vmqnEBymNi_bUkKOC-O0SswPrhydNqlV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crGpxaLlzSMLH805HUgTXVpSEWEXpsmWP-F31TJtU2jGDv64yIFjNCW5-1kxFuZ1jWJf-Hm9Xu5QfrSsDbBJq39db47KRJg_lOKQSNqj5L4U9PiL11UiF0aYO1ylbK6PA9yGM6dgDqozIZ91734vjsxA_-CwAitrO91U1kS0BTcnJ8qXllb5vpduEuOgUAKTmBQD81M21AMHDCr2unHb1l92ovauwXIfW7RCRIyFc98vnojV21ehK8ACuJxOS3nDmiuHXp2wt6rJH2VLsXJv6t322S89Hn-w5wik9hmCojsWOyxbFO46DgJDc8FJSDSxcHCsdWfWLjT8nAqZYj46JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9ZXqLyR-edjxRWfJCtg9KuU5NpDwAeVdRNPBpFoJRKxrzT9DBuUL4sVkCG8mLI4L1kPL8cAzeMO4SM0uZz-ZHGY0QumIuRQRJJ_p0neknucmTzNrggFgTMbZvVD6IY6YNbv1b_jEmD4m-DOAem_vV3ZLjCJDloXLPSPjddXnTAFlKOq5QovXmV6VKsRdpkLdFnFSu8fkKGNdPwOsDYpGByQQ4ZUNDCxp_mWkfXLHzicJC8skfwVlNFK183p3eK0Zo5R4_ELMD26aOQMCdYR0BPygWlhTT-DaYsRqrwx1AaEm9H-hYPCGBKHKheTHlU_DVIeVRngyFspJCicSukcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwgn0-xSVS3SVYuvigHQdTKI7BqRooLIrLQcndQ1BHZiPRqv_OmSmMB0W30AVTgP3ymIXv04Ib3dHBp8eRtTwXEQ_wa-6Q06vQpIUiImJj2bY_-HXqj1fWwsK_u3IzCXfdOvwMU3FEfE9KQTRVJW_n38A3DNFPo6BYyngyZTZABly7Mpnp66a3won7YpMghmHg17WseP94LcjeAjO3pRGsFrDMl7MOu7zHvuoKYKt2X0Z1GGqzl24MnsDqv5CQ6QoplpGaTc5cyZ3mirSyrk_uAQHccTrFkVSVf37lwa6gSM2JuxHOpGcCysa6XMC6XDUeP_3pbtu1SNYPAhKczYLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/436516" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNnga1DirecvxXdNYauhxmmPNwOWwHgpdsjalECdKq0UClNPxk0_Hay4h1zP0rZP8TCcihPDD6O9aiGuMEgMIeJK8OUXnknOlU-M6PiQs0ZS2IZ88nBScJWyG3z7jnRIACYJrKlWpmgdHxtA4Yy1mxjwuIcO8LgvBxVmxSRJsNFmaAp8DyeFpv8uN4Ht3kT2ee41DPLtfZNtNFNLTE6_LGIM8okl-XhfsugE62nKP9OlPF6RRV0ayTDxE9euJXMw6K5Du9MP2RbYrWZgSYgOlppwCKFr7r5nZ_40OBA6zrPSbftSM2kZaKv3G5ncKSeXoSvgHhqKoXZMxdwPPFTrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW5bZbL5B1eLu--T8EL0dzZNQEXC6HKOqBW6xYcb7YXcgPQV5tGWD00ejJ3iYZl-FG7gBknuo2Q_15ms2eKZ1nvlpkzjkrp9SoI2ETFpp11yS2S103lyJUeH7mdGzedEP080jMfaWwSJIyDzjCIpKX_75BNbbAjHHH4EL3KYHs6ZIHLGcczWEPTTgPUQAXuhbFjpaBgacs7agKibyAlybHFllijOqZ4LQwuIMeZxVNiOSzd1WwLobKjJyf27jrTrmopSxiw7asRwIFd6oVJq0zsrr9KHBVZTiwaQti0J-PPcdGzm7ly_gMfrjaE_uIoW6v90Ji0hYmKknVVaplZ-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDf8-3s7BQ_gSeGnF2aAfvZPHpjORHW3qYODzZtwQCeDU6V5UCWUUKzA2H97PSOISoxNRSEzXSXxdDWduQO8QSGdk7fjw1UVbEUXBUCZCxm8EVwIZ3wP2zBX3Z-BK0J2JJ5dvzYIQLn6KiZc8o2OAR9sTUYMEYnZyoZIxgiVoMSg8QxZN5pW-6QmNhrT3hhT4hIpUPLEtMLgcg7L_T6Iew9s4aMQrOELdzREKYxN30SxXxE8FYp36n2oW3ktYFQFqL9a8qC_XaceQwTqs3d5Gae8v_f6WKZyBtqKQ_OsJoajRMWpxSzTt4YhAmZoX8f-HVShs4wHhBuKorMWAfUIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJKuKTrtMHYgUusDsvuJ-DtKACQ2N6QbsSfO-tOKfmAKP2nlzWVzfcwE7ubzMuNIP9czERwPJijRQ9XdnitwpjPKqo4_iB3hi8ASrSQ-k-pI1dWXKLzPbpG2uOTqmMPGhbyOW75KsFzRJfzXxDKrPE-wSiOrtHmKBuuqc7wA6hY3l4mUVAk40vgPLJWKFNKQQxe-mh_lfjNxzxoP_2Y0ooNzEZtDNvJLEGkviQFhxmT4Wzw8wmVWLkYaEn_RZw-cMgBOjXqCFSbyj8nWgSvId9rsb1kYUbXhd0DzsrFqtDLCSzYb76agfu2xYnyq_wMJnEYIBGeRUPOThqEWEKI6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTh4tlO1Gg3DOsaK3Hf4dTZDhA7nfOarPLidQDrrNQWOmHl_NT_zbxgW2veOw40l2UWH6hUzM-sknWEjP5xcjH3GJ92uLrdxoHZxD3_9fHY0R4W3xLG3cf6RnWaLJxiwJARgW7wsgX64O60res1WbGuineKEBH-FHDNPScKE551AeygYlIJhbgbs9iNwcU-o-YGi2zKE3Eh-75XP7gMAUnyao7eN2MsnQUVlHvpZXfK-SOa63xjZPk9yAQOIs9YiaKdOrX201JbaHY4wiPoSoi3jdtBojsNYD1S_6YcoyHaxFq5IY90Nity-XHpPc6t-Y3Mvw3uw2uiEABep1hnCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSpxwDU8d3qV1p0GHxk7FY-Xs2L3pcr0FaPiWr4Y_E7EOXfOulMTuKtQYsLkRh0MrVoHJydTW70Kkp5m6-u2UhFi6CRgJAOM8jWsAvAKQdC8u6JaAjWVQuW28voB7gQ-tVa49jbwcGOJAAU7Qv1csHPkEik5B_b99o8eleh70wGbDNC-Spz5SdOb7Iik145cwEPuA-hT809iQWio-W-nOtgrJBhuYs6fAdgjRKHKJDECa2EVN5RYv37H0-daTD3VNWzKWblXCDDf00690ogeEcHUhNBxirQTA3hQZ5g2G8ZcSu7COdMmLv_Q4giBwps4oV5s-ADEM4Zy5a2HBmNL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmxTVCAbjYE1fV-6zCZLAQPMK4Q4EG7MIEVmVK1hQpUl_a4ZbgctKGI2oc_NrTJ6H7WqI50ofX_ND9PQHFGXxzvQZFWeF97uVxhD0e_rAZ-w6tsvIjnvUAvIMx-FwR4hdho0cWnIbIcvBW5oRlKNVrY13iX6-B56GHGSnI-eWKRK0WeENC5_nPGBMFAHqAibe-3t_Ak01wRrIdWfu-qGqrSRjK6b6Tu225jcGxBkefUlf8a7l4VEY8sd-Hu8UHZPjqqvra8Gkls-kNBsADSQgMCbKHOT_csfv6QxZf19mYFm7yD5LFuXtExzmxqqfFgf_LHgNbPcaaYHm8GqBAyL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEHZHsjoiPNmi_Y34TOe2piV_mtU1U7vd63_mpHlsmL2hXyX_ipoz02FDMcmYgiv1noPDHsxNDPrVbgYkWx8nCOPjJqu6tj0QWTmq3RbFMvynLfM16BVg6O07HaUIS-55zeBjHWi9UEXK6i05GgYwqVSX79QknOgiWfsbmvwDdeJv0I8KtNUHJ3AWK-Sr8rhzMeDMgYyJY2wOZp-BV-PDOjtIAWrTwXpcaXWd2JCB6x9mSr_Ko4Pq6EuD_YyPn0LM_HaCwEaDDgKe0G0BuBUf31-sRIX9Hr1d7SG2s8sYu672561QRwzpP8sGfOZ0QhOdYZVdu0Obg1y2fwJHjlqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlcMIg2eIf7bHovXNLXoQXsw0WI6E_mjGUGRojJ7EgIBJnbtss1X-QgiKdMweH2lnaoZimZ7Dw41tHeGQc-eSX_qSjau0RfvuXretcSwZB5s4I6Lq_UovFaTbayOXMT0R1Y2AL_g71TAqOMxYUO15-sSuMXB03eFHfJt_wXYZxQaRbO9Fc8Lj8ri2ofDKbbLVc0HPj02vQCU_3yfz0JPJ3-3JLEPvKnaD720AfUwW-AtUC4cKVAjKFlSGWiPDYlJVmp6brN2aJ--fwnFaB0q-4S6Tv2O8L0E2IVjOnesT_dm7louek1yD9uQp5VVKbpHtKSfDqvJZvnIRDnW3QdUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z28k4nVd8nc8i1CMReupEBUxj7gIAxP2vg0tEcPv0qDkl00TFdOk5Bvj1ytTEEzCitl_rgJSA21x9EksmsaEhInHIz4zhP0Jq24tl4rkwX-B-BCU1BeibTyWhazW2S77oTxvmEK8lcgePggvamaPDfUzA9wiDAHZf3gcrmv1gLPh5zwLMXocxugOPTyihf1UT2bXyqcjaN-Iq3ZYdxCJEgsZJinyOrepTaKdKY_kLAi7FYXaXG_RWnI0rN-KPJfnB7aaFUcyhjc0BycArP77Y9r9J7dex-HPzTkB8MHq5WVP7uC8bWa7BeqObz2vCD8e5K55WH_bJn3vT9UezEE7wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/436506" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17fa4bf1.mp4?token=kTYSnICDB2rTsEZ6iGVbKM3o-NVOTuhGeyGtjqsqXa2yNB-8CVDP4L6hWx9swTmXwmkWr_u_xnBQFjoEfrdzApy-prnCgNGFB2y1WyJL2vlS4S02BS_k3Cokm_QhuPyC3YGlo8g-MmPIXYqrmuvvuzTZR1nIOvYKcmKwOXRrjjsKAHNVaLNjBsCoYfH9XRm7RkG7o08vh_NgTfroXdLZA1_P6d8N2f84BHMHWFpNYocOWZ84OhrtmiKLJ1Kmjd3LFUF8K8XLI2E9uL0NCjRzn0OHqWfr-UCxytLHPVHEoYbBC-Z2JXlAjrul03TnqnZeBxaN2U0p9SDdDQX26cVyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17fa4bf1.mp4?token=kTYSnICDB2rTsEZ6iGVbKM3o-NVOTuhGeyGtjqsqXa2yNB-8CVDP4L6hWx9swTmXwmkWr_u_xnBQFjoEfrdzApy-prnCgNGFB2y1WyJL2vlS4S02BS_k3Cokm_QhuPyC3YGlo8g-MmPIXYqrmuvvuzTZR1nIOvYKcmKwOXRrjjsKAHNVaLNjBsCoYfH9XRm7RkG7o08vh_NgTfroXdLZA1_P6d8N2f84BHMHWFpNYocOWZ84OhrtmiKLJ1Kmjd3LFUF8K8XLI2E9uL0NCjRzn0OHqWfr-UCxytLHPVHEoYbBC-Z2JXlAjrul03TnqnZeBxaN2U0p9SDdDQX26cVyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم. @Farsna</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/436505" target="_blank">📅 01:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436494">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8a7plaX0Mx_fERz8tDRkocZpNfbjjB3PCSh2cwINN6i0-JDYMiDasVg-HWbXNVPT2nHCX3EMRf6nrFyuy1gBi0CHN26Mhzo239X-MHBeCaVJJkqE07p_wjfi4w2OzveWFtkf6kDpjQDBVPPeM_e8sU_oHZWZZ0ogj4sGSyiZsWv95YWBYlG68yENRE55iycQQtCVreTfNQ6_xb0AuXdKo2HWMg-e_2JqHmVy4FibbgVk4llz_4mlXQlrxzOCgH2OVwkLiKgEL5qLRWszghEXWKL4dJRxGhV8zHMYUpiTehL9dxls4W_qSliuKQeNJQbT5ZzgdOpFDltj5n_QAlgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم بازداشت وزیر صهیونیست توسط دادگاه لاهه
🔹
دادگاه کیفری بین‌المللی شامگاه دوشنبه حکم بازداشت «بتزلل اسموتریچ» وزیر دارایی رژیم صهیونیستی را به دلیل جنایات علیه بشریت، جنایات جنگی و جنایت نژادپرستی صادر کرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/436494" target="_blank">📅 01:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436493">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نظرسنجی نیویورک‌تایمز: جنگ با ایران ارزش هزینه‌هایش را نداشت
🔹
در نظرسنجی جدید نیویورک‌تایمز، اکثریت قاطع شهروندان آمریکایی تأکید کرده‌اند که جنگ با ایران به هزینه‌هایش نمی‌ارزید. این نظرسنجی همچنین نشان‌دهنده شکل‌گیری دیدگاهی بشدت بدبینانه میان آمریکایی‌ها نسبت به آینده اقتصادی کشورشان است.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/436493" target="_blank">📅 00:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436492">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qAo2DepbTJvTI1GNbiQrHM9ZUQcZ4Y8LY1F3953PG3n52Q2jEbi1JqXshjekEfEJBFFNO3Rr9iUEO01TAvo6FY4b6R7rE45lXMocgCHp_-tj0cQ9kpjAYhrQDlScQV7dH7DqmUuoY5gONCaUsD_ZtZgetMq6o4wqe0emaI6g7Qzc7j1XO-E_MmJWsC5B1ra6_j0nYXFaVgfcG59mSr_jJvkldB6tGW_g8fWfDXmLNjK9g5uCIYPLBjz2VPDmemWYNm6EgD9FHjR0lT4McusiEwk2Oz5bjhdd3zNDvEeaPskPd83kSJNB_1taBEQIm0jlpOrYjuMVxiFXsYMs99kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش بقائی به اتهام‌زنی صدراعظم آلمان علیه ایران دربارۀ انفجار در نزدیکی نیروگاه‌ هسته‌ای امارات
🔹
سخنگوی وزارت خارجه در شبکۀ اجتماعی ایکس خطاب به صدراعظم آلمان نوشت: ریاکاری وقتی آشکار می‌شود که حملۀ آشکار آمریکا و رژیم‌صهیونیستی به تأسیسات هسته‌ای ایران که تحت نظارت آژانس بین‌المللی انرژی اتمی است نه‌تنها محکوم نمی‌شود، بلکه عملاً توجیه هم می‌شود؛ اما دربارۀ حادثه‌ای که عملیات پرچم دروغین دشمنان صلح و وفاق منطقه بوده و حتی امارات نیز رسماً ایران را مسئول آن معرفی نکرده، ناگهان زبان «حقوق بین‌الملل» و «امنیت منطقه» به کار می‌افتد.
🔹
اگر حمله به تأسیسات هسته‌ای تهدیدی برای مردم منطقه است، این اصل باید برای همۀ کشورها یکسان باشد، نه فقط زمانی‌که مصالح سیاسی غرب اقتضا کند.
🔹
در ادبیات آلمانی، چنین «داوری گزینشی» یادآور «قاضی آدام» در نمایشنامۀ «کوزه شکسته» است؛ او همان قاضی‌ای است که خلاف‌کاری‌هایش باید قضاوت شود، اما با ظاهرسازی ادای مدافع عدالت درمی‌آورد!
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/436492" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436491">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZxTYvYhgeVhiCDtdkqbCXfZPWsy2PCq_kNlEDNN6X1Sai1y7xOpDng0welU8fDfei8tzQMGP4WXgb96u8GXTcRp0ff4bim6At1nndxIu-mZEpX0_6g0lbhX-0SbPKWVzHX2z5CunxSlgcXNw37wt-0SjFXAL-joBDegAVQKI1J_8JL_0cUkWsklhBeBI-IJ0Q3XYBRf6BZY1IxT1sDvnsFrnf4L2rjmtXwrs82Tx0ZSKcOOybKVM9eaTcJYOXYXbUFTwUzSgS4n6o7rQYVeqOYCNz7e9Rk3B7d9p9h5gOCxPxZW3DNGFSsoHgNx-jna14UGCSdo7A8YYYAuKGeCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جای خالی این جدول را پر کنید
@Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/436491" target="_blank">📅 00:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436490">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فرمانده قرارگاه مرکزی خاتم‌الانبیاء: دست هر متجاوزی را قطع می‌کنیم
🔹
به آمریکا و هم‌پیمانان آن اعلام می‌کنیم دوباره مرتکب اشتباه راهبردی و خطای محاسباتی نشوند.
🔹
​آن‌ها باید بدانند ایران اسلامی و نیروهای مسلح آن نسبت به گذشته آماده‌تر و قوی‌تر، دست بر ماشه هستند و هرگونه تعرض و تجاوز مجددی از سوی دشمنان سرزمین و ملت سربلند را سریع، قاطع، پرقدرت و گسترده پاسخ خواهند داد.
🔹
​دشمنان آمریکایی-صهیونیستی بارها ملت شجاع ایران و نیروهای مسلح مقتدر آن را آزموده‌اند.
🔹
​ما با عزم و ارادهٔ الهی ثابت کرده‌ایم که اقتدار و توانایی خود را در میدان عمل به دشمنان نشان می‌دهیم.
🔹
چنانچه خطای دیگری از سوی دشمنانمان سر بزند با قدرت و توانایی به مراتب بالاتر از جنگ تحمیلی رمضان با آن برخورد خواهیم نمود و با تمام توان از حقوق ملت ایران دفاع می‌کنیم و دست هر متجاوزی را قطع می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436490" target="_blank">📅 00:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436489">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jha-wZJewL39XHx6cL6Q9MqNgJ5OONNdwhtJOCOv7Qhsn7Y0vAfBm__nD2Bsch313deOFuNxZVkpCJCzCHoL_l_CqMQ-CD4-fJR71EUAi1x9rWY1ERu_nYgjZmXuD7sUEUC5KXM1gtGaVksuszAabu6YSkoKeDaKC56AGGU7pTPF-rFCdRke5y1tOkKWWBh3D8WkITtuzidkXZ3rPPtTN4bQOzmqj-zi84RapetW5SDJ3UYaqlP4V0r4XfvURErK1gJlUKtnZa4U1RES0WNfEQKuQ701H2DK8wlNzf0AUHxdbU23xihA7M8aWje5i2ba46Ynw26abLgIghNJsVRT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۳۰ میلیونی ازدواج برای دانشجویان
🔹
مدیرعامل صندوق قرض‌الحسنۀ جهاددانشگاهی از ارائۀ تسهیلات ازدواج ۳۰ میلیون تومانی به دانشجویان خبر داد.
🔹
چنانچه زوجین هردو دانشجو باشند می‌توانند به‌صورت جداگانه آن‌را دریافت کنند، که مجموع مبلغ تسهیلات به ۶۰ میلیون تومان برای زوجین می‌رسد.
🔹
ثبت‌نام این طرح، از ۲۸ اردیبهشت آغاز و تا عید غدیر ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/436489" target="_blank">📅 00:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436488">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjjPu0xc74wKSZ0_oaPcbmw5KVsNI5jz7Kr0oEsy9tPXV7-FBlu_P-Idauxw2JgAoGNALRRqWrHjRJwXqZGC8xHbci6NU7BNKdKCFdeFv1IqRhu1kLC0rarkVGGKlpYqobdxje7stmivB3at8r6Mk2Dhac3mq6_y-TDAxuwT6Da2oTyqx3xmmU591N235vRGb7-JwO_9UuXaKv21QpBAm8Ghtf9ZluadtOavMC7Wv4RIEONneHcQpogB0-ufnw7CXap3ysQ1bg0vU-WDf-HZPb-XicJD8MPZHzUzIlp1ktRJDssaI5btxO2MgIm8HETzCmmOhZmegGb15pWV3TmfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش محسن رضایی به عقب‌نشینی ترامپ
🔹
‏ضرب‌الاجل حملۀ نظامی تعیین می‌کند و خودش هم آن را لغو می‌کند! با این امید واهی که ملت و مسئولان ایران را تسلیم کند!
🔹
مشت آهنین نیروهای‌مسلح قدرتمند و ملت بزرگ ایران آن‌ها را وادار به عقب‌نشینی و تسلیم خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/436488" target="_blank">📅 00:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436487">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7dakqG7IkXbTz4rP2bYvcA5KgT5t2vNxIHD5tAMitR8VjkPwh4xW6HRw4HFZfjpmvVtR9mSMcI2TyadSa6eSU30_CA6dyvCurHthGlsmroO9JRkgj5WXqOssEoGdzZigf5IjIfnqj-ZamP8-BNlhdoRi3pTf2ijYc48iM7VKECNDPOBBqalfLN6-unkT1adRWvZOtiZePddX7qhQi9tVJlbBIvWeUJkqXaXpCcRC72gg_sxv83ZB6MiG9jYB9lnoFpAuOt5-6EP1ZOu3WX4c2jf7zKkMjjTHEdODrIEQ1vgFxaE0nL6i3wG2171wz4YaYhGcR675J_97NA31j2KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشورت با ترس!
🔹
نقل است که یکی از ژنرال‌های برجستهٔ روم باستان، پیش از آغاز نبردی سرنوشت‌ساز، در چادر فرماندهی خود مشغول بررسی نقشه‌های جنگی بود.
🔹
یکی از افسران جوان و وفادار او، درحالی‌که آثار نگرانی در چهره‌اش هویدا بود، نزد او آمد و از خطراتِ احتمالی سخن گفت.
🔹
افسر جوان در نهایت گفت: «ژنرال من می‌ترسم که...»
🔹
ژنرال صحبت او را قطع کرد و با نگاهی نافذ گفت: «هرگز با ترس‌هایتان مشورت نکنید!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/436487" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
۷۹ شب ایستادگی برای وطن در دامغان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/436486" target="_blank">📅 23:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e40f06d8f.mp4?token=fdGoANOrpWV8dVx1Bk8BbUU9713H-7eEBsm5moQFoIlv2eKp9MsZo1gNBgkP6A-chj0cYKU9nfK8zw6ys_2aluRlDxxynasyAUZssqL8ghodn96bm7K7WPHAD9wAaphHMkgx6iRGAkddkS6ckuzE9kMoRo1MVKh83U6bVy6jC8pJE4-1-fG3qtY_-68OK0jYaL28YnVkWBEgG_I5XWNc_w0xWyV1nIyKiSauhmU0AlUyYgQD_GyIEjhw2Wo-F6Tt7oT79MMJi-GosQkHxx8JCzclYG4HAxsaNsPQWSMzZNyXoz5yiir8CpnSTTuvoYxkuWTA26BldiohrCXb5EvnpZ_ZBeObkCr5ojWsh0krtkrYP9O9O4B9AZojb6rNw1kCie2ojoUNr56stj-_QQeMtYvKMs1XMJAAaTzoQwVaThxpR7wEWFjnpW5l-zDbfw8nSYuuDwBksH12p1PX-cua4fANYD9Zjp7kfend615ul_oiOmzSiTTanu0uypTYn8_YyUENMqeTXQyFjrhA9Ja6mICw0PPQT2AcTw6DRBlazPEQEe5pxSuICPvdkMsbI1IZZ7SJgVTkSE_YbDXfQCc9nDXVUXN_SOko1MzFtFlA75AHQzpqvVEexhEw1-Zh12FLdvvT7mD2s47p4paHo2ltMfMbT_haBE5bUFpvl6nKI7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e40f06d8f.mp4?token=fdGoANOrpWV8dVx1Bk8BbUU9713H-7eEBsm5moQFoIlv2eKp9MsZo1gNBgkP6A-chj0cYKU9nfK8zw6ys_2aluRlDxxynasyAUZssqL8ghodn96bm7K7WPHAD9wAaphHMkgx6iRGAkddkS6ckuzE9kMoRo1MVKh83U6bVy6jC8pJE4-1-fG3qtY_-68OK0jYaL28YnVkWBEgG_I5XWNc_w0xWyV1nIyKiSauhmU0AlUyYgQD_GyIEjhw2Wo-F6Tt7oT79MMJi-GosQkHxx8JCzclYG4HAxsaNsPQWSMzZNyXoz5yiir8CpnSTTuvoYxkuWTA26BldiohrCXb5EvnpZ_ZBeObkCr5ojWsh0krtkrYP9O9O4B9AZojb6rNw1kCie2ojoUNr56stj-_QQeMtYvKMs1XMJAAaTzoQwVaThxpR7wEWFjnpW5l-zDbfw8nSYuuDwBksH12p1PX-cua4fANYD9Zjp7kfend615ul_oiOmzSiTTanu0uypTYn8_YyUENMqeTXQyFjrhA9Ja6mICw0PPQT2AcTw6DRBlazPEQEe5pxSuICPvdkMsbI1IZZ7SJgVTkSE_YbDXfQCc9nDXVUXN_SOko1MzFtFlA75AHQzpqvVEexhEw1-Zh12FLdvvT7mD2s47p4paHo2ltMfMbT_haBE5bUFpvl6nKI7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواسته نهایی آمریکایی‌ها از ایران چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/436485" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac42e5865.mp4?token=Krzk6USlqP5spmrWlucwoiiqJAW5eeiOkIzMwl7E56F6Mj0ObLba1QmlTlm84XIjfFzC2O2obe9wA4mHNX9xE2AtaD6jSuCYUYuoxPkKBEK64Zg4HWuhEnzKugKDXhgElfjRXSjPEhdtqRpsMu93YneBT9oSC-0udh2ZXoNTHZGgkiuiCqpIPIsaKNnREs2s-3dvhltI_Bw80qkyXusAKkDPCf1pZnCpfoWQoNuC0LfBShXwbxIcC2NutCZf7XbAVdDzbazrjYcyD5QAQipgvYYodcV-jq_fIWz-SeveMdxcKwiMfU6ZFjJxXLW2NgdscVwb67la7EYK54NTLpwkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac42e5865.mp4?token=Krzk6USlqP5spmrWlucwoiiqJAW5eeiOkIzMwl7E56F6Mj0ObLba1QmlTlm84XIjfFzC2O2obe9wA4mHNX9xE2AtaD6jSuCYUYuoxPkKBEK64Zg4HWuhEnzKugKDXhgElfjRXSjPEhdtqRpsMu93YneBT9oSC-0udh2ZXoNTHZGgkiuiCqpIPIsaKNnREs2s-3dvhltI_Bw80qkyXusAKkDPCf1pZnCpfoWQoNuC0LfBShXwbxIcC2NutCZf7XbAVdDzbazrjYcyD5QAQipgvYYodcV-jq_fIWz-SeveMdxcKwiMfU6ZFjJxXLW2NgdscVwb67la7EYK54NTLpwkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در یک مرکز اسلامی در آمریکا
🔹
رسانه‌ها از حضور یک فرد مسلح و تیراندازی در مرکز اسلامی سن دیگو خبر می‌دهند.
🔹
هنوز آماری از تعداد مظنون‌ها و تلفات منتشر نشده، اما رسانه‌ها از زخمی شدن چند نفر و مرگ دو تن از جمله یک نیروی پلیس خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/436484" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a055d3ef.mp4?token=BmOxkAfe0HkS9uLOlNfBScJLLJGGtGhwHZF_yNRzpbgfRfxwe61lPea5nQ3MRyVibT_FWVxgF5Z4Sx3z_G78ETksnCHr50Ex4uNomGWq9A6CyWSoOVMBsEM36R2vqVTtEDgAYVNpMI4y90-jHYjjTgw6dxijy9IoYt3oX3Hm-4b1oo7GlD6JgvvmVIBnIdKp7VuP352wQsQGF_sAytghn-tCr7NsmRzVgfb-A1e0wQgWQmrJ6TXSrkZzsLJbLB41cvNklDdhhr2qcnnuY01qCEwKnzl4_7uzv3Qfeq6J3l8qj8HEJwo18UWvpXIAS375YBpepBhyptsxLgfryDNHFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a055d3ef.mp4?token=BmOxkAfe0HkS9uLOlNfBScJLLJGGtGhwHZF_yNRzpbgfRfxwe61lPea5nQ3MRyVibT_FWVxgF5Z4Sx3z_G78ETksnCHr50Ex4uNomGWq9A6CyWSoOVMBsEM36R2vqVTtEDgAYVNpMI4y90-jHYjjTgw6dxijy9IoYt3oX3Hm-4b1oo7GlD6JgvvmVIBnIdKp7VuP352wQsQGF_sAytghn-tCr7NsmRzVgfb-A1e0wQgWQmrJ6TXSrkZzsLJbLB41cvNklDdhhr2qcnnuY01qCEwKnzl4_7uzv3Qfeq6J3l8qj8HEJwo18UWvpXIAS375YBpepBhyptsxLgfryDNHFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاش یک بار از نزدیک می‌دیدمش!
🔹
کرمانی‌ها از یک حسرت برای خود سخن می‌گویند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/436483" target="_blank">📅 23:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37df6fe12a.mp4?token=ZODvEHy-6ENERezR7QeGLHs3vcyJVW6tpmAMqFv95ew9cy3aRkzniSSvqHGLAa5JTIMWZsf3au6eTC-w1W0ElqIpQdpV6XfX9gHGmD2y--3yxHgwWJ1MzYwkuV5lGoDeRiNz5klqKwPLGtU6KDWSjkuAfz13OX40G4gHFbLXIrzTbhISIWpwo_e4wPAK4XH1dOAaRsRT5E_GDyq3dGw3WwNPZRTGfSkhQrHqQishejAQkoAFEQGwLgvYw5gmlBZ4-vrDjIXUg0UueLISfWinMH3wD8pPcL1VvMYZTk86MvAblKhV1Y1gkvdjBZKyZxQYPeRcV_UUoKTp1kyV3BNanlpJzoCHJyoWjFoACNPFsgYZtv6YUlL6DaLXhlerX-7eIJGdUJ3JGcvIUHdxj5o5xkRR98C9zj6Va5pMUn4N-t7vlsUaa2sLha2wL-lU1_0ICErwGbJpsjqm4S1-UqzwwLzVI5fwCn1jiM9a238kCKNgUyPwXeXQNTzIxCRUK79Y4M49Z0SJ2bWYpdVVszqiAD7n3vNVg92u0DRg3LsSxxyZ4AoGuMnrpFnf9dEi_8hmuk8Uw79sGh0M8fZUn_sHxo7-9Cl1Drj9rShXm44QDtCLd0hrr866ZScWLtM39-z5p5TtDV5o7DecZWEwYUD1YjBhZ1JMhIR3jVig38VLb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37df6fe12a.mp4?token=ZODvEHy-6ENERezR7QeGLHs3vcyJVW6tpmAMqFv95ew9cy3aRkzniSSvqHGLAa5JTIMWZsf3au6eTC-w1W0ElqIpQdpV6XfX9gHGmD2y--3yxHgwWJ1MzYwkuV5lGoDeRiNz5klqKwPLGtU6KDWSjkuAfz13OX40G4gHFbLXIrzTbhISIWpwo_e4wPAK4XH1dOAaRsRT5E_GDyq3dGw3WwNPZRTGfSkhQrHqQishejAQkoAFEQGwLgvYw5gmlBZ4-vrDjIXUg0UueLISfWinMH3wD8pPcL1VvMYZTk86MvAblKhV1Y1gkvdjBZKyZxQYPeRcV_UUoKTp1kyV3BNanlpJzoCHJyoWjFoACNPFsgYZtv6YUlL6DaLXhlerX-7eIJGdUJ3JGcvIUHdxj5o5xkRR98C9zj6Va5pMUn4N-t7vlsUaa2sLha2wL-lU1_0ICErwGbJpsjqm4S1-UqzwwLzVI5fwCn1jiM9a238kCKNgUyPwXeXQNTzIxCRUK79Y4M49Z0SJ2bWYpdVVszqiAD7n3vNVg92u0DRg3LsSxxyZ4AoGuMnrpFnf9dEi_8hmuk8Uw79sGh0M8fZUn_sHxo7-9Cl1Drj9rShXm44QDtCLd0hrr866ZScWLtM39-z5p5TtDV5o7DecZWEwYUD1YjBhZ1JMhIR3jVig38VLb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن‌ ازدواج ۵ زوج مشهدی در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/436482" target="_blank">📅 23:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b0db00c1.mp4?token=Acx8ygmhB-vpHyiZjE6SNV4byHH-DPR1kHhAEb3ltGMN_vSRvhMjyPnR2faC9Pud0CqJTzxCayQPl5T13U3J7G3IlxDChdj79EdUhE2MA4bKRao3TSBDntQQtEZMvbo_AVwXOs6r4HZnn8Y11C5N8-SZD-cCvGLY2z1bdq7oRg4nbfzjs2RlswWSbdM7nFUa_YSOB9fyj-_kDh2O0GBLUcuClU4bcS1XikTuklD_SmNQ3ZQrnsF5JQF4WW-negia7-O5XZ-uSAcL2Gw3jGCtCyI1EhdalixvJWRVf2SDy9fs8Sttll0R-7jIpolmXmrLiBwjR6DWwYBBbNmfUwCUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b0db00c1.mp4?token=Acx8ygmhB-vpHyiZjE6SNV4byHH-DPR1kHhAEb3ltGMN_vSRvhMjyPnR2faC9Pud0CqJTzxCayQPl5T13U3J7G3IlxDChdj79EdUhE2MA4bKRao3TSBDntQQtEZMvbo_AVwXOs6r4HZnn8Y11C5N8-SZD-cCvGLY2z1bdq7oRg4nbfzjs2RlswWSbdM7nFUa_YSOB9fyj-_kDh2O0GBLUcuClU4bcS1XikTuklD_SmNQ3ZQrnsF5JQF4WW-negia7-O5XZ-uSAcL2Gw3jGCtCyI1EhdalixvJWRVf2SDy9fs8Sttll0R-7jIpolmXmrLiBwjR6DWwYBBbNmfUwCUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان عالی‌رتبه معتقدند که باید در مقابل محاصره نظامی آمریکا، پاسخ نظامی بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/436481" target="_blank">📅 23:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
حمله پهپادی به تروریست‌ها در شمال عراق
🔹
رسانه‌های عراقی گزارش دادند مقر گروهک‌های ضدایرانی در استان سلیمانیه عراق با چندین فروند پهپاد مورد حمله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/436480" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb4adda89.mp4?token=qryLRBBeM1ZFA-fZR1HEeCcDqLy6L3-Y7GnxQP9SedXJ4bjEwGfGxUwHJStfGJHKPykVkwlwkX88nw5qxui9GoMnKO9i00JLSAQE6KS2AHwc7HZ7jvyuhWoytsADSml-_3tE8g-C0KehhSYEQIZZMbsWk7tNq5dys6CZ1bHehm6eTvH4xcVfSGWnjBQ-3j8_WAF_AuS1bN_MhQFsCjKagpmhIQICPni8ZC6d3RqjLOIsbrJfaJB9hcmEFQnhchLkDEBeSKin0jn5PMFFkln1sGco5iY07HtRSCNlooT_t9YsWJ1Y8SvKV9ddZbGxehDUh6G2IVJVo70GRDJMtiLuJzFHqZ_b3zaPH8QDqPu1OCN41FxW7--IiqBCocMboX2G7O9q3CJ4vCxyyO8KdYrDVuwYspQI7SD31yjEQ0h6mzF9XZSW6I4GuvP_P5kDLeL18E8jMzUUfYowfxlVwzRslBUt_mU6mwGQZQHhGYALf6zzkHbH_qKBukkgsCRJ3dvUTChVbWC91bWEupHevAnywqEOH48zJLMisF41rJtIITW89LTbsbLbYlanLsftq97F_YLFMFOjVYER8wYhBd10sUSrx8_Xl-rqVMSKDwPh2Y6zlVOE7woaQ27_k-u3HyJOhtUW2EqhizHqIw845FgE6aI8dGke_P9nDz3Z71nCwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb4adda89.mp4?token=qryLRBBeM1ZFA-fZR1HEeCcDqLy6L3-Y7GnxQP9SedXJ4bjEwGfGxUwHJStfGJHKPykVkwlwkX88nw5qxui9GoMnKO9i00JLSAQE6KS2AHwc7HZ7jvyuhWoytsADSml-_3tE8g-C0KehhSYEQIZZMbsWk7tNq5dys6CZ1bHehm6eTvH4xcVfSGWnjBQ-3j8_WAF_AuS1bN_MhQFsCjKagpmhIQICPni8ZC6d3RqjLOIsbrJfaJB9hcmEFQnhchLkDEBeSKin0jn5PMFFkln1sGco5iY07HtRSCNlooT_t9YsWJ1Y8SvKV9ddZbGxehDUh6G2IVJVo70GRDJMtiLuJzFHqZ_b3zaPH8QDqPu1OCN41FxW7--IiqBCocMboX2G7O9q3CJ4vCxyyO8KdYrDVuwYspQI7SD31yjEQ0h6mzF9XZSW6I4GuvP_P5kDLeL18E8jMzUUfYowfxlVwzRslBUt_mU6mwGQZQHhGYALf6zzkHbH_qKBukkgsCRJ3dvUTChVbWC91bWEupHevAnywqEOH48zJLMisF41rJtIITW89LTbsbLbYlanLsftq97F_YLFMFOjVYER8wYhBd10sUSrx8_Xl-rqVMSKDwPh2Y6zlVOE7woaQ27_k-u3HyJOhtUW2EqhizHqIw845FgE6aI8dGke_P9nDz3Z71nCwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور شیرازی‌ها در شب هفتادونهم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436479" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436472">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPfnjAQcSHXF13k-3XdAe0oKQ_ZatqhmXrM3qqAe1MiTJ74-vQQo2h-rDBZjTnwosPtH3gLzJRK2u-qOwsoWpy7t1KuRq1s0YtvI63XToAYO3Cg985o_JGYrfiS6Rc040ItGYdnL4fCLlR9kLjTOGlUIiUhMp8eedPsy0UTjXzRVTqzFoZEVf4hr86ei2rPvPRmNaw1ILWKBNZgOZwccbRwaFOUukAc55c5x23uJd_L-XvZ9GcDRERwn9GCl18ZR2oY3x2TmP4XbZvvz-SobXg9E2v7AWM3HJRa6kuI-TZMe4jncPUMiK3JgwjM_w1olsbZd-xn07JexZuw8dcBk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hloIZKz-4EqgL4NnV4pyAwmNwVWFOgn8hZeI39bcPH7fw8W5otUAD8RmGrOYmu5ThVOiFATYU4rsVbdqoV0NUpjbxVPxakQzpXEDcbuUv7QWHrcD1PQtklR13K-XXkjGQOdTqy15iUDxf8p0XidytbmjwZF_QK3AwJUuKeLryveWBPiuYLtNCDQdHn3UX7aamXwtJElgDDxdlOxVzo1AmsHO35bUU9zfKqMMh6vraDz2hMELCzkNlPYZR_nKA44L3UQSVBW4oacyxvFCXDwjGcmabO9TEJmHGTiQOCPpQwFAumyL0zs9Kiqhy-DzF1RGBedpTvSDmQFeT8f_QvkhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhDbEhI4u3gNKB1ltXc_tktd4BZcE1UA2BGBTcqrX_5vlFCQHXW9FPV4E3JIEyydbGPJCIbCGMOo3yRMkw3p9cZXRE8qzigJ9clgfBzoAeqjzwAblckVjoZ6vakZaaW9HBr9YGIhThG30PtKZaKOTKHgM6xfV3MzPcArgG3kx-kXZWGxTFcR9Iw4qEJqHAAt-i_uxNTZ91PhPTot_wP-DfDs9KyZAG6nneVVZiGUV5Krb9UQ1v0uKY91XOh1uQWeRlg8Mm1qJyHlVEJj-OMt5VOdTMlJ5CFdKsdTi51Y0FTJ9-DMhfyERpza4w7Bt9FEwJK5JujVYE_tC6lRFXdI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p06EeBQO1-DHq8OREw4viBZ_PZL9BPAZKTqt1Tnp1Z9xJ2wgk5TceyV-00kD3YqvAFmVi4mx79rds05OJi-UMl-PWinFX-H3fM1Glr5ELpvpRKRf4ykbJSPGIjmYHkJIv_Yvfrn0Dco8lOTLBsqeBasGoEsfzSSzMksRZt_wh1fbf5qGzJ53KBZrKKFYUS16QC9Z_zQvtLCjlRm9E1zOuOcGvLIG6sfDwY_CN5CT4pGmNDKf_YWmA4hJZaRTUxLo5kcPg5wu9HLwG1sF4_tniJIKEJn7soerOeDhjCxUlLSPwje2HzPO4BCpwwzmjz5-JsjX-o0LXfLTDrEFgV1SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAed2Ned5PPttg6Puqkjnwwxz2AcDtDBr27psI6XzfIcFKpzNu1jM_XgF0uteKmRszT63IgG9Xt4w1uGamxyvqo1uHuj_mCVPfAcr1fQq_g2_AsASeTDXwRUIB7ogxynY4BZXrp5BM4VQT9mIP8r6RGnEDaJcKUm0hiVrNldfL6GROjgRKsJBrPiQiays3OjHBm-olrYeye-zj4_vd72-GAKr5QiZENyMW_BfmMQ39mxwlNYbkLfJS2yd4xVj-ct6DclVjlBFaolt-dWh_Wo-Ju2rX3QpJR0k4HzLWPsBPL6TZsEkTEDDPjep3_4qesTz_hY4MMu6VRhFG8BA-Gbzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHv5sM36inekRjkQmEQsGQXeXoomCmopN54_NFt5d14GHVQ7YkwNtpkhIWlh0QbBGFEH68kXBnzEkhxaknCphtg7kuNh6CyDaSadJ1c4XKvZuyfi9g2pL89boVNn7ZNnPXnIIm594auCT8uf5kJ1_fa2Kl3b2BLUMAR2-A_S7XwLvFJy4bDEcbD7HDTX2TuYunqjWem8amBpv6AnR1A3HFfqG62RUBBgP4KngjcQpONdM0_WOJWf6ooYE4jl2x7Sv1HoTXq-oFv8vyAPPJXqKkZFfwP1wDCA2Ir9Q-DWZU5_iaevtHTZkw154fyOItkXUSCJPDaQ-fLKtpSHD8RplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCMSGIonoM9O23TDuGzjkARIILPNbay4_FvW1-XSYdu6MVbAxfPdOOoETCJWHPts2JlPFpyCZiyGAWk9L-kAGT89VEu3B7VyJ22ud_WrhJOFDe9Td8el_bnflmEIWACmRiAszxCQB7m52SE-QjMLAARGj6Q6hHqLsD-u_5_IBj6c3-35LRuNssrEpthWTC77AkHX8Yinp_DJFMoNrqEkkQxdJvqs810vTCetkgWZnK0BKybHMTqxs0ORUZruwsbgTGuThIGjpJ6JXeVZPlj-Z8tkRcdFYn-hICOfTfrKxgCg8S3gfY5c7G3Z9-K7d82conhEneuraWoZ1I0LmYWxmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کاروان ازدواج دانشجویی در خیابان‌های همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436472" target="_blank">📅 23:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRcpOs5p4QxaF43JLiAXSImPQeaejVhyvQ52w1yi_4v5IGydUmhf3W4OMcu2ay7-Gc-lQhM24YusOruCWLVVUzUGCLfSiszgVN0U50TdW3sdk-STCDU9ZIzdKXXeXawmTNtj8ndv87FzqoAmEGisxxMH6DDiH9wlfqqsKIgNUUFC4M6H11pgeuMBiPXo-FTezGjeKAUJLWM8tavn244G-yDmsuiA0ujpy5cgfd5Pk0z2U7YdAn0BX8NDr4OmJMS0qBsVqX-_uIaM2xTY-cIeU_HYoQ3te_Id8tgOgjfYLhctv1dci_vEG0z1_buyu-NkpjD2QxgiE-etOiKzhPhzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA5J3ljdPJrX98YZQu1Ekfc-HnGjLMNxK5b7qOihFS2fAHVmUC_ttbX3o1XFtTIR7uXu9DvNXENYTm-SBrjUJElbNJxRKZSMIuMZ9RNx1UVnDzSuuynnJpApBtchJSGJSVoX-6WeMXga0s0snM3-L5Zm57seUyWr-cP7dIZk3pA3Z_ABHL__s1zWvVn2n2ucrL5du6gFG5cv8xabtjJf7tHzY7FOAaStrZN5eQJIFLra8zYWjFpkik5rtmwT_rLEKItoDSFlcOgBUNqVc77fOKhk0eXSdOom2_f3BlUNJe0HQopEgRfiNmTJY4Pra9dWFbLHR1MYQEd5-zHr6Wz-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6Yb1-F5B5z89RI4iwUR9cXXW3b_REbf1WkSz3z4r89bXVsyW4UCtDbhZssv5kJuYQBGtIuJAa7Lkd1CUy_o5xRJrtDMSApyD3J4duxQ9VFTbea3e6apvF2zpUOFKPY0g_wTGKu0CSSKYJM0ylp1__yoTJtHR5geEDVq49NyU1mpV5BHYx6Yu3deLS7M3WVlLNOBwHHJIC_7dOk7LVX-XI8XTWQ_tykXMy9PHLGBt-EDXWQ--QNq75ZGJdRXJdu1xjzXKIARp2DbStWZHWU-0QgGqkKruGKI1FLapjRB67vtpmy6rt2yWfVb77G-wNpUhpKDwu8D3V7wllf8iFp96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXwRBNtTUaOegsxsJ0LwIgFIEEjQApTdo3ERCvpzOeYow6VBcb9a3aEtuhtnFyivTnx9Z3A6nLrgRp_0nkKoKg_-gZCP3iCGU-Xmh8eMmbqgjFzHI91l311QeHBSyl_FSwBtFhWdu_mBFQ5f6uCbugXSOOfY405zkyyBjKsxHGcPyTB4yF6vv2_qOQs4rRNQ3SapErosSE3HKjNjNZlX-922FmbfD0K8baIutYIVaOUwQGG5BgiyQ1g1JUCplTvyGqjLN0Dm3fuLyDYzqvgyaI45hSHxaOqrZX3m5_FwSLpM_RdPh1vwlnk0axeE6rVu0Bb81tPW7gsPVQ8HYItrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxE_2iVbO9TGgQs3iuaSWwzvsiR9VlT4vLdOt7noddL-B3y1wKX02zlIKqaFTvpgF2DHPScepfqP3kfAVvmcBfJjozBLitHVFMI34QmHW9zviec-U4zgdtMQm1sD1WTkBsdAMxcnKzKSa23Z1-4-LxI_EvoLiC5ZYhy-atoAVkcfjUBCq6r346V63IKBOHQafO412EbmAj0vTUHrqDXrxzacAM4pGVy6s5-ERWlf7Ur_9WpDdcF7kCpYcHja56-Pv4hqv5bKuctjV4XoiEKbw0gAqcT7U1UhhlsNGgC19pt73H7fEzzLNvNMmFIp2Xah1L2e8_jfalLDo9FfYVIZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5krU8nhyDpnP5Xuxqc8nJq1OUFIz_KflLuA3LsChn8MUmE06wjoNT1ZQwI2uIrjqhIdni-53BIEb1NJkn6ne-Hz7qZIpafUo5aoBcdrtE2gU7FQcvWMG0bWeUpdhmr8tXs0qLWOsvgY8hj-7t621KSFBXl8koSJFqvLbsIoFWP3OlK6-eHj396CCMe7uSzpc8Ke9RP1Wa7zD4V2iTnXklTnZQZAFp3ytWYg7e9pGe_YOcMlfdVgXQhSrb2Adhnum9kPKWramWoXqHC5p1gKSzdTsw6P-iuNMxTDN44WDm-LV34CdUOXMb4hdkqRgVB1cLO-mgkVS0emcurrNmKfdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از نخستین تمرین تیم ملی فوتبال در ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/436466" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436465">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">استانداری هرمزگان: پدافند قشم برای مقابله با ریزپرنده فعال شد
🔹
صدایی که ساعاتی پیش در جزیره قشم شنیده شده است، ناشی از فعال‌شدن سامانه‌های پدافندی و درگیری با ریزپرنده‌های دشمن بود.
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/436465" target="_blank">📅 22:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftkcwDt9Zl0H_AAk2Yf6mtOllUZbsvPO50rwOaE9h8fgDQIwxFDHwUeIwVJfxTClsGmwm8Hr7ks5Zzka-Gbnbz-EPhcrpjRd-F96LbqzjEmNBbHgy7BwODL3mWu1wUlWtn9dR6poE2WvnCT4ti_Wvqgtj46PvLk0P7El0bp1ytlAx-9_60adt87-sCpCdiJfulkQBdubAh7Ig9Pd11KpwS5SJ63qcYYmA8ImXwWvpVrRrwxECmspYcEwB9BKkh38c1KnYT2AGitA-SRnwVf627FdqmVATmQk19KL7mg51xboDQr1Bxe4T6i7QiGIXmnAWbUV43ZSbcLAPVAC-erPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/436457" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7abf04a1.mp4?token=C2RGbAnBbd9aC9BvZduUQ4GMVk52JgiJ_r2O5nmPrk6RUs-2DyihDG1n9L8mmcO6pXdTNCgiYndVnK6F_1cW854vZP_R1_pBY_UidJMNoafhfHtvjrUj-eQhDuN8aBdNraWP8jVpVDceI6ii03y56ATT8Qz_o7LQkmuegYArywfDNRnT579A2kqx8JIoVTsxNj6JrW4sLHrfgbL5fZrJPLNBZjLOwh87RlGZUSiuhHQRGuCC5mtX6CTqadJ3CZFF0i048EXwmN85qITLcOQNaK2eedauL9lDVUDhTw4A_LkFJHEsy_m6IFvIaTCZ-EWLhRQMlXtelWI8o5Wx9eXZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7abf04a1.mp4?token=C2RGbAnBbd9aC9BvZduUQ4GMVk52JgiJ_r2O5nmPrk6RUs-2DyihDG1n9L8mmcO6pXdTNCgiYndVnK6F_1cW854vZP_R1_pBY_UidJMNoafhfHtvjrUj-eQhDuN8aBdNraWP8jVpVDceI6ii03y56ATT8Qz_o7LQkmuegYArywfDNRnT579A2kqx8JIoVTsxNj6JrW4sLHrfgbL5fZrJPLNBZjLOwh87RlGZUSiuhHQRGuCC5mtX6CTqadJ3CZFF0i048EXwmN85qITLcOQNaK2eedauL9lDVUDhTw4A_LkFJHEsy_m6IFvIaTCZ-EWLhRQMlXtelWI8o5Wx9eXZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات حجت‌الاسلام رفیعی درباره صوت منتشر شده از او
🔹
رفیعی: صحبتی که بنده بیان کرده بودم صرفا یک نقل‌‌قول بود که می‌تواند درست یا نادرست باشد.
🔹
منظور از این صحبت نشان‌دادن خباثت دشمن بود که در آستانۀ به نتیجه رسیدن مذاکرات، حمله کردند نه این‌که بخواهیم به کسانی اتهام خیانت بزنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/436456" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📷
یادبود شهید علی لاریجانی در مسجد بلال صداوسیما  عکس: صادق نیک گستر @Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/436455" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d0fd3957.mp4?token=agCIdvyB4bnJjYcoZ7HCxxREJsPS9deIX5RqOX0UUW9zXvGddMAKdjE_fkre2RBuMdj9-JTzj_rl5ooN9YjiHlq7Y4wpMyF6NcRVZW7X5d9mGkLM10jRu8SSRDbAqHyaB17sAdw__WWD5fH5lB3Provy9x5kAefs1NFLSchC2O_oIAdy6G8K8aUkY3euvHCbvAkWHWHVI64OVPkDtnKLNrRqP8bzLqM9s7pR3XSv7CE-PFJneG3bibUh1-AdH2mo3ubGUDNnPtxHCFcwQPYxG5VktOrJrmLeHq6RlaYpYtQEm33WVslXL-L2kthYUaD4WqrTwcQfJ58Vy-W35L84ZyOyq1ubmFBv6JWlJj0WH4bwaVzhAM0FmTLYw4j2P_UMO6t4HsHyEz9UV5l2ufoTP5MGSfyv6eFdC_a9VprwdDSulPTwZz-0QKwUhfCud-FvLU_jjrC8g2GCkW4u4vgU7vb-O3rS-JBg8s6cWklIQnermBt_Fa7Ys-IlJ9XomjXu7xy70NYUG1ZeqJFOTOFDN0IFZQWrxSoY4gHG1hebIgDljpgQ1EET9NK23uB3TcXrqq5dUCcrE0wbvyzl43QIdSb-E9qlJbLjQAPtpUsshya1UjqQlVEkKAh0ru2n2gTLpBjLHY7kprB2sYYDcfyrlnpqU9YN-s5h3CsoBcoSu-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d0fd3957.mp4?token=agCIdvyB4bnJjYcoZ7HCxxREJsPS9deIX5RqOX0UUW9zXvGddMAKdjE_fkre2RBuMdj9-JTzj_rl5ooN9YjiHlq7Y4wpMyF6NcRVZW7X5d9mGkLM10jRu8SSRDbAqHyaB17sAdw__WWD5fH5lB3Provy9x5kAefs1NFLSchC2O_oIAdy6G8K8aUkY3euvHCbvAkWHWHVI64OVPkDtnKLNrRqP8bzLqM9s7pR3XSv7CE-PFJneG3bibUh1-AdH2mo3ubGUDNnPtxHCFcwQPYxG5VktOrJrmLeHq6RlaYpYtQEm33WVslXL-L2kthYUaD4WqrTwcQfJ58Vy-W35L84ZyOyq1ubmFBv6JWlJj0WH4bwaVzhAM0FmTLYw4j2P_UMO6t4HsHyEz9UV5l2ufoTP5MGSfyv6eFdC_a9VprwdDSulPTwZz-0QKwUhfCud-FvLU_jjrC8g2GCkW4u4vgU7vb-O3rS-JBg8s6cWklIQnermBt_Fa7Ys-IlJ9XomjXu7xy70NYUG1ZeqJFOTOFDN0IFZQWrxSoY4gHG1hebIgDljpgQ1EET9NK23uB3TcXrqq5dUCcrE0wbvyzl43QIdSb-E9qlJbLjQAPtpUsshya1UjqQlVEkKAh0ru2n2gTLpBjLHY7kprB2sYYDcfyrlnpqU9YN-s5h3CsoBcoSu-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش‌های نظامی به مردم در شهرک رجایی مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/436454" target="_blank">📅 22:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e295e864.mp4?token=tG3N7xtughk0iJFzm7nNA2nyufm9yLxr8vIZZCxOnUqJBwf7fHJuralhfu3oy6v1K92JiDEh5NWMVyBXqjZCxbbMhGMJDC-7MxqBhcbjnXaW__HZ-F54CVyakhCxDA0yyxJ3MqhdmF4DLP6VP8cXrlrephR697vOV7uiLHewRM-0d78Dl-EQx8vNwVAwlnOAD8vDtmfMlnXvIWug9LcwdAB3O2-tX7fpZDtjCHCM5xsKfXm_p0iE0PJtNjG_y1sCWKg4ueaLLCTHuQaTSyXMnE8qErvdvrZ2qq3HyC1XfVJOjoZ93_sXRvxcgB5JbmxaqbJYHV4jkr6GMayNvRFTqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e295e864.mp4?token=tG3N7xtughk0iJFzm7nNA2nyufm9yLxr8vIZZCxOnUqJBwf7fHJuralhfu3oy6v1K92JiDEh5NWMVyBXqjZCxbbMhGMJDC-7MxqBhcbjnXaW__HZ-F54CVyakhCxDA0yyxJ3MqhdmF4DLP6VP8cXrlrephR697vOV7uiLHewRM-0d78Dl-EQx8vNwVAwlnOAD8vDtmfMlnXvIWug9LcwdAB3O2-tX7fpZDtjCHCM5xsKfXm_p0iE0PJtNjG_y1sCWKg4ueaLLCTHuQaTSyXMnE8qErvdvrZ2qq3HyC1XfVJOjoZ93_sXRvxcgB5JbmxaqbJYHV4jkr6GMayNvRFTqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش پرشکوه مردم غیور تربت حیدریه برای بیعت با رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/436453" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgFknmp3lOKEvJx26_C_T5ShR3jWB6pvn8bZldVTelKt8OJU5rKv_PZlbQxjFuZq2aESOZa1AsyqVM5YxmvhRIz4J6o-tHy2HNWCTil1f3WnlgHuRChyV4vAwd5--OpFtBK8qtO6kR6rcw0IMHge52MgLMnYGG68jI3TzPGcJrstdAQCotXxk6mJFDYM9jKuiVBgx66IsNllPBuEHXMh_uCSCBrfwwlgj0p_gUdUWYwbqaf2zP1HFSEkLhnK85IffI9xzOAiwF8IZBXEmLcj74N-aPDHifSsCtJ7KF-d_VYXGPHAqVk09L-ny5TwDalOqqDsZHIpF0_MpaXi1USCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: گفت‌وگو به معنای تسلیم نیست
🔹
رئیس‌جمهور: گفت‌وگو به معنای تسلیم نیست. جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود و به هیچ عنوان از حقوق قانونی مردم و کشور عقب‌نشینی نمی‌کند. ما با منطق و با تمام توان، تا پای جان، در خدمت مردم و حافظ منافع و عزت ایران خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/436452" target="_blank">📅 22:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تاج: متفاوت‌ترین جام جهانی را در پیش داریم
🔹
رئیس فدراسیون فوتبال: متفاوت‌ترین جام جهانی را در پیش داریم. شرایط جام جهانی را همه می‌دانند؛ آمریکا دشمن است و دشمنی‌های خودش را دارد و از دشمن نیز جز دشمنی انتظار نمی‌رود.
🔹
ما باید تدبیر و برنامه‌ریزی کنیم تا مشکلی پیش نیاید. خوشبختانه تیم ملی شرایط بسیار خوبی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/436451" target="_blank">📅 22:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436450">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/436450" target="_blank">📅 22:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436449">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed04e9df61.mp4?token=NWM2VpZKL9HceLyixtjC2k7N0tGCiNbV8csmtn3Jx1VuoXoC_dSZf1NrFNShkttwjTIEVyza1txoZtKHugtOzED0xQRqYhf7YeOwG4VOvJX4IrmLRGSm1i6_dLf1CD8FpcNkot-bSqHQUjEUNonJT4TbH8AB7DqEiWZiQAiSYg6BK-WqI0t4F3eFKc1ldPALAn91WfQAV5vaD8OoRuNnlFrIkscM4SC9Z-DSWHorXZldwi_9QZ1V0pvOpVI2x1WUqt7-9M9k2R6u2i4-rmZsbcNf8zHBAsbRJJDzytbYi05CjFBkf-DXNzc6b1p7r4847YVIS_-VKrWNSm7d4uremh7fPTjKVMMomlntLNKjUNraM5ueb5Ru4lu4pui_lMDD04LHndMamX3t7-MC9p_zkJIkjzbePfHkIX9YCmpgr4xghuSxTIW-jbqccc5a79lJQM_wkoxVdySQU8IunyTDyB3sNXGGm2JdFkuU1gmJ5EDl7_-ED_uxRqJr1DkrppJvqjqjFQuQjbViNbMHfs4XotN0DQVAFQbyZOk8AUB8jVnOmhwacmd4Z9Ym0Upah9-6xny04dW7SixlgRsmmyAKolSn-CAfY00jN9kluR31jo9rEjVS58iIz-7GZ8LWh7mRTMGDA3IeQQBOzIgkX_vDATV6So7Ip-Wa7ogaQ2M5M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed04e9df61.mp4?token=NWM2VpZKL9HceLyixtjC2k7N0tGCiNbV8csmtn3Jx1VuoXoC_dSZf1NrFNShkttwjTIEVyza1txoZtKHugtOzED0xQRqYhf7YeOwG4VOvJX4IrmLRGSm1i6_dLf1CD8FpcNkot-bSqHQUjEUNonJT4TbH8AB7DqEiWZiQAiSYg6BK-WqI0t4F3eFKc1ldPALAn91WfQAV5vaD8OoRuNnlFrIkscM4SC9Z-DSWHorXZldwi_9QZ1V0pvOpVI2x1WUqt7-9M9k2R6u2i4-rmZsbcNf8zHBAsbRJJDzytbYi05CjFBkf-DXNzc6b1p7r4847YVIS_-VKrWNSm7d4uremh7fPTjKVMMomlntLNKjUNraM5ueb5Ru4lu4pui_lMDD04LHndMamX3t7-MC9p_zkJIkjzbePfHkIX9YCmpgr4xghuSxTIW-jbqccc5a79lJQM_wkoxVdySQU8IunyTDyB3sNXGGm2JdFkuU1gmJ5EDl7_-ED_uxRqJr1DkrppJvqjqjFQuQjbViNbMHfs4XotN0DQVAFQbyZOk8AUB8jVnOmhwacmd4Z9Ym0Upah9-6xny04dW7SixlgRsmmyAKolSn-CAfY00jN9kluR31jo9rEjVS58iIz-7GZ8LWh7mRTMGDA3IeQQBOzIgkX_vDATV6So7Ip-Wa7ogaQ2M5M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا می‌شود با انفجار یک موشک در مدار لئو، ماهواره‌های پیشرفته آمریکایی، اسرائیلی و اینترنت استارلینک را از کار انداخت؟  @Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/436449" target="_blank">📅 22:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
خیابان‌های خرم‌دره زنجان، میدان نبرد اراده‌ها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/436448" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خطر بزرگ در کمین افتتاحیهٔ جام جهانی
🔹
درحالی‌که کمتر از یک ماه به شروع جام جهانی باقیمانده، نگرانی هواداران از حضور در مکزیک به‌عنوان یکی از میزبانان این رویداد بزرگ بیشتر شده است.
🔹
تیراندازی جمعی که روز یکشنبه در ایالت پوئبلا مکزیک منجر به کشته‌شدن ۱۰ نفر شد، نگرانی‌های امنیتی را تشدید کرده است.
🔹
۶ مرد، ۳ زن و یک خردسال قربانی حملهٔ مسلحانه در خانه‌ای در فاصلهٔ ۲۰۰ کیلومتری مکزیکوسیتی جایی که قرار است بازی افتتاحیهٔ مسابقات در آن برگزار شود، شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436447" target="_blank">📅 21:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436446">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce5ec67af.mp4?token=AsLWLXOT_uB1EonoPo6RNwQKRmQJPpS9OjAuySAkVUyImCASUnqL0k1U0f_zqvZ4NO5YH02uPfgRtdhu4UT7XzlbPc6_kTczF5V3HBSkM9vqIaktNBjL00ihTjRQ_J07pBt5y3FH4OWghN0DLKJK5thfup5fF7DGHRJ0vchlDxaAPa29rLEvxuFpmE3D9rmgQH0sXkpLW--qvDysStmNBH6xGiMwDs7KwwOQZplYhwqmVnX5JRH9msKucpdfIkquNkMnCSeSRXWH7AoGIWevXWms2nwQ01XDI6Lw3GEDwrVoOu54IovnB4dgG4ccyv7DM7cumhUgwf5c40ibk2ejYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce5ec67af.mp4?token=AsLWLXOT_uB1EonoPo6RNwQKRmQJPpS9OjAuySAkVUyImCASUnqL0k1U0f_zqvZ4NO5YH02uPfgRtdhu4UT7XzlbPc6_kTczF5V3HBSkM9vqIaktNBjL00ihTjRQ_J07pBt5y3FH4OWghN0DLKJK5thfup5fF7DGHRJ0vchlDxaAPa29rLEvxuFpmE3D9rmgQH0sXkpLW--qvDysStmNBH6xGiMwDs7KwwOQZplYhwqmVnX5JRH9msKucpdfIkquNkMnCSeSRXWH7AoGIWevXWms2nwQ01XDI6Lw3GEDwrVoOu54IovnB4dgG4ccyv7DM7cumhUgwf5c40ibk2ejYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بات‌های تلگرام از امروز باهم حرف می‌زنند
🔹
تلگرام قابلیت جدیدی اضافه کرده که بات‌ها می‌توانند مستقیم با یکدیگر صحبت کنند.
🔹
این ویژگی به بات‌ها اجازه می‌دهد کارها را به‌صورت خودکار و زنجیره‌ای انجام دهند، مثلاً یک ربات اطلاعات را جمع کند، ربات دوم آن را تحلیل کند و ربات سوم نتیجه را بدهد.
🔹
توسعه‌دهندگان حالا می‌توانند شبکه‌ای از بات‌ها بسازند که مثل یک تیم با هم همکاری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436446" target="_blank">📅 21:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436445">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e688626c28.mp4?token=F0HT77rOfQsQHlsjXNA_Q82wXvzt62RZbHkzl3vAwjND0h4VuXbLi_81l0DGyjBbj01b8IQ4pYKAE-ZuQBk4lehpFoRZO_kYtSt9jDZbQJyxr_kbfBX03ANb2bfT_DXK5B_kKVlUGutBcCvteUR2gebcXCujpMYMJ80Y13g10SeijbgoYjdkefSZpvsrOU5NGJERu5vuWWiyj9TYgwvvHZnMFP2y2wjthglUrMB-ZPXbxT8s33nDXtE8pxhUZzMZiYIAiJe8IbA9-GY0wwIknlapJz0AUJNrPpseKcBMlSUpa_qWbpbqKDCLiY71Rj7Vd45Y3wyLn1rhySXPuu5htA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e688626c28.mp4?token=F0HT77rOfQsQHlsjXNA_Q82wXvzt62RZbHkzl3vAwjND0h4VuXbLi_81l0DGyjBbj01b8IQ4pYKAE-ZuQBk4lehpFoRZO_kYtSt9jDZbQJyxr_kbfBX03ANb2bfT_DXK5B_kKVlUGutBcCvteUR2gebcXCujpMYMJ80Y13g10SeijbgoYjdkefSZpvsrOU5NGJERu5vuWWiyj9TYgwvvHZnMFP2y2wjthglUrMB-ZPXbxT8s33nDXtE8pxhUZzMZiYIAiJe8IbA9-GY0wwIknlapJz0AUJNrPpseKcBMlSUpa_qWbpbqKDCLiY71Rj7Vd45Y3wyLn1rhySXPuu5htA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«قلب اینترنت جهان» در دست ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436445" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd3296632.mp4?token=IVwEZe9K7cPj8vEEgxRErm8Ct08-H_BGYVEe7eC9c1cf6kv3hUbzCvzuq0qiIg-uGwoJVDi091Yfybn-UQ9BekEbE3kJQwnjRqRZUcFjE70z_aBRfSk21nA3dOEy7dJ05E_qw7ERbq6Lwm6i-PG2mOr-uR_Y032tNrJFfXmv-0J8G7pgv8Pvmx3QayO-39zUcPR62Q2oKBJn_D41v3R9_IRaF3ExPjgh-FiYW8E7FN3ACX8UxRNVrWYWBVTsL5UvJA5vAZUmASZ4A0ruOy3LF3KTWnSoXZr-c4QYRBCdjH3DvBZ_iCVPgCTjFmZjkosizbZWhcsPAfk5F57iBAA3kEWRIMUx5VfvnQ3CUnHL_AfSUIdfmA1-ZqJTiAUMnwA1TQDHSQjQ8fAlQekSZHsum0QQxUjGW7QjZqi5MrA8aEZQIhiBtT65_MMskYGI52eqQecV9OEsZ6gbtkxeHID-QWU3jlUIIrc-Jt7-Z401hAATWnBmalRM96LGFSYlKPo7U783EzrJ1daediY6M1LqgD4x22PEPa-DB32qBTYYFL0qCI6h68UY60ZpP3f27JHgtDhODrFbuN4OU6LHu4dCgXKt9P9PmvHMA-2LtUkxLdKMw9zPHz04UdF5Df3QZDtOjMEUoJeACcsX-bchIz1l2H_kTqGNjcD22-Vba33EyVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd3296632.mp4?token=IVwEZe9K7cPj8vEEgxRErm8Ct08-H_BGYVEe7eC9c1cf6kv3hUbzCvzuq0qiIg-uGwoJVDi091Yfybn-UQ9BekEbE3kJQwnjRqRZUcFjE70z_aBRfSk21nA3dOEy7dJ05E_qw7ERbq6Lwm6i-PG2mOr-uR_Y032tNrJFfXmv-0J8G7pgv8Pvmx3QayO-39zUcPR62Q2oKBJn_D41v3R9_IRaF3ExPjgh-FiYW8E7FN3ACX8UxRNVrWYWBVTsL5UvJA5vAZUmASZ4A0ruOy3LF3KTWnSoXZr-c4QYRBCdjH3DvBZ_iCVPgCTjFmZjkosizbZWhcsPAfk5F57iBAA3kEWRIMUx5VfvnQ3CUnHL_AfSUIdfmA1-ZqJTiAUMnwA1TQDHSQjQ8fAlQekSZHsum0QQxUjGW7QjZqi5MrA8aEZQIhiBtT65_MMskYGI52eqQecV9OEsZ6gbtkxeHID-QWU3jlUIIrc-Jt7-Z401hAATWnBmalRM96LGFSYlKPo7U783EzrJ1daediY6M1LqgD4x22PEPa-DB32qBTYYFL0qCI6h68UY60ZpP3f27JHgtDhODrFbuN4OU6LHu4dCgXKt9P9PmvHMA-2LtUkxLdKMw9zPHz04UdF5Df3QZDtOjMEUoJeACcsX-bchIz1l2H_kTqGNjcD22-Vba33EyVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتاق اصناف: پاک‌کردن قیمت کالاها ممنوع است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/436444" target="_blank">📅 21:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8f95cc9c.mp4?token=DHkaoiF9J90gtpvKwiCPWnijpb7CkM0T-YRLcAJ8zG_p-2WBugqurFuXwYfdeO81Ox6wvI_Px5ZsbAKUIt91wUQgIZUU5rLuWPygAg5blgiLis1uwSPAaY3km8d4gmnCRtooAeWvDs_ZfbcPZZ1Lcg_W_zrfRBDW1ae_IsHtTyYeLUA27mDD9eClFVoeOqH66j_59SFdxZO-4us_aU9xGlmU8QooVb89cwQFz6mmkhJBBMyDsr0FZW4aDtBlTXGJvU5cUQkd8bwFSxRgmto4uQvRt0TwgO9gpKYf63kunF8KKUWNO5dLqGznVFGaHGaCNvn1jePEp7ALHn1WNzLvBEvPH1vEj9BrQodM3hPHEsrZK8CDahF1QgB8_nvLGK3OA929qlPgXlDR4GN6zo17OzRDLEI2CiZocU5xI5xbX_dPpeCwm0yMeDwKlvSApolsdUGe0QZS1AU35dEoY_3OhS8xyA3bG_del7pCtHdGjMzaOuvMTj3Q-Z1ClZwLMAQsOtrtqSgdMYC4qAktsM4dWKga8BbDGSDBAf70Ym2ENsyNASRQM8k9Dlmjwa075J8wc67pH-Ml0Mm41kkUVP4rSeFRVwKdSA6EEEtn0gW4Gaq8CgoTUSQeCv6HUwlASgSZ0DI13AuNxI4mTbs-LHaDNrA0HEJddSlOZbYAQFuszUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8f95cc9c.mp4?token=DHkaoiF9J90gtpvKwiCPWnijpb7CkM0T-YRLcAJ8zG_p-2WBugqurFuXwYfdeO81Ox6wvI_Px5ZsbAKUIt91wUQgIZUU5rLuWPygAg5blgiLis1uwSPAaY3km8d4gmnCRtooAeWvDs_ZfbcPZZ1Lcg_W_zrfRBDW1ae_IsHtTyYeLUA27mDD9eClFVoeOqH66j_59SFdxZO-4us_aU9xGlmU8QooVb89cwQFz6mmkhJBBMyDsr0FZW4aDtBlTXGJvU5cUQkd8bwFSxRgmto4uQvRt0TwgO9gpKYf63kunF8KKUWNO5dLqGznVFGaHGaCNvn1jePEp7ALHn1WNzLvBEvPH1vEj9BrQodM3hPHEsrZK8CDahF1QgB8_nvLGK3OA929qlPgXlDR4GN6zo17OzRDLEI2CiZocU5xI5xbX_dPpeCwm0yMeDwKlvSApolsdUGe0QZS1AU35dEoY_3OhS8xyA3bG_del7pCtHdGjMzaOuvMTj3Q-Z1ClZwLMAQsOtrtqSgdMYC4qAktsM4dWKga8BbDGSDBAf70Ym2ENsyNASRQM8k9Dlmjwa075J8wc67pH-Ml0Mm41kkUVP4rSeFRVwKdSA6EEEtn0gW4Gaq8CgoTUSQeCv6HUwlASgSZ0DI13AuNxI4mTbs-LHaDNrA0HEJddSlOZbYAQFuszUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروسی‌های جنگی زوج‌های جان‌فدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/436443" target="_blank">📅 21:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تامین‌اجتماعی: واریز حقوق بازنشستگان از سه‌شنبه آغاز می‌شود
🔹
پرداخت حقوق اردیبهشت‌ماه بازنشستگان و کلیه مستمری‌بگیران تامین‌اجتماعی از ظهر ۲۹ اردیبهشت آغاز و به‌تدریج طی ۷۲ ساعت به ترتیب حروف الفبا انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/436442" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b01e76f2.mp4?token=euRDPBxPswaVWk7R8bR9ZvHVm6m3MrHuJUiIfFgCSuzwWzmgao2MPT57-yjTwhQwxvAU6OTzG92XI3SxeQRFFvBtqkZbADVQ2rVIquGtFqPKUA61ACPMBgjvmBJtR2clegGNc7U1QBmBjWAq80g0-B9tC4c1ZuNaRdPgXUMODcRf2lBseQOZZQpEprJzFRXROy-PM4fs8RrNyOWeFA4Iy-DtATY52kJl-MtgpAev9oYJKihUrnOAKYTd_lqtuuvM1inBV2thnXvBshGJYuySMIb8nns24P2A5IkT622sczB1X3A_7I3Gqpi_ol-71BTczFCoYiuxqnKRmn3SfYhKejBazwKyYzPWnkeMheWakvxO2Y3G0mlJO3VtdynwNkqNEseyI-5EMTI22VhjS_KzmfzHfNKQHEsUn5HQGbvgzdw1b9OWMTzNspBuNObHBEhs2SG57FprWjDf__HeWZbFdpkHTdirFxaKXBSgeAc9BWjT7sEeWF9g9IcCMh-Mwg2VODPCfgsB3OQFVrbX8OJF_2i8UtXdeRV43g7-hvYLirhiCerHkScm-NNjOo6gOv1WG9A89O3Tzy7Y1BtVwl6MT9WW7OMDrwsfM0IvAcEzCXPSmNxsceVxYu5C-u5PGis8gOrndG7p-kDG4iQbEIoSGP4Ob7ZLlC6w2OqKIIp0Kao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b01e76f2.mp4?token=euRDPBxPswaVWk7R8bR9ZvHVm6m3MrHuJUiIfFgCSuzwWzmgao2MPT57-yjTwhQwxvAU6OTzG92XI3SxeQRFFvBtqkZbADVQ2rVIquGtFqPKUA61ACPMBgjvmBJtR2clegGNc7U1QBmBjWAq80g0-B9tC4c1ZuNaRdPgXUMODcRf2lBseQOZZQpEprJzFRXROy-PM4fs8RrNyOWeFA4Iy-DtATY52kJl-MtgpAev9oYJKihUrnOAKYTd_lqtuuvM1inBV2thnXvBshGJYuySMIb8nns24P2A5IkT622sczB1X3A_7I3Gqpi_ol-71BTczFCoYiuxqnKRmn3SfYhKejBazwKyYzPWnkeMheWakvxO2Y3G0mlJO3VtdynwNkqNEseyI-5EMTI22VhjS_KzmfzHfNKQHEsUn5HQGbvgzdw1b9OWMTzNspBuNObHBEhs2SG57FprWjDf__HeWZbFdpkHTdirFxaKXBSgeAc9BWjT7sEeWF9g9IcCMh-Mwg2VODPCfgsB3OQFVrbX8OJF_2i8UtXdeRV43g7-hvYLirhiCerHkScm-NNjOo6gOv1WG9A89O3Tzy7Y1BtVwl6MT9WW7OMDrwsfM0IvAcEzCXPSmNxsceVxYu5C-u5PGis8gOrndG7p-kDG4iQbEIoSGP4Ob7ZLlC6w2OqKIIp0Kao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر یکی از دانش‌آموزان شهید مینابی: دخترم روزه‌اولی بود و با زبان روزه شهید شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/436441" target="_blank">📅 21:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تامین‌اجتماعی: واریز حقوق بازنشستگان از سه‌شنبه آغاز می‌شود
🔹
پرداخت حقوق اردیبهشت‌ماه بازنشستگان و کلیه مستمری‌بگیران تامین‌اجتماعی از ظهر ۲۹ اردیبهشت آغاز و به‌تدریج طی ۷۲ ساعت به ترتیب حروف الفبا انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436440" target="_blank">📅 21:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1ea73aef.mp4?token=MnzEqRf02qtDYfCsQscNcduNfGXCzM1uqATjHDeRFebtPvDhFXOtbVB25ZNuGgaIefgnyclGu_60F6Mbr1UXvcrxCdS6K4eq8KGaWCKMCL_0XYB6x3MRxjW0F4_cq4zTYVXTj9n5t1N79E3bGaD0OPG1Bzr3nCNhXCbxe4OHZuVx03zwLLnjBgrO4lsZotLlTF2jDAf0hGfW8IuMr_r6yCID90xwTUtNtbOQrn-5Ci1rkU_uCALDPKlth8H0uCzqRPJS3TqDPHpw5vMKed9MmpmRsplwY2Ji62o_9raybBZxngjnFOezONkN5CewNEtgJtwphzgeBvujltJmWoAPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1ea73aef.mp4?token=MnzEqRf02qtDYfCsQscNcduNfGXCzM1uqATjHDeRFebtPvDhFXOtbVB25ZNuGgaIefgnyclGu_60F6Mbr1UXvcrxCdS6K4eq8KGaWCKMCL_0XYB6x3MRxjW0F4_cq4zTYVXTj9n5t1N79E3bGaD0OPG1Bzr3nCNhXCbxe4OHZuVx03zwLLnjBgrO4lsZotLlTF2jDAf0hGfW8IuMr_r6yCID90xwTUtNtbOQrn-5Ci1rkU_uCALDPKlth8H0uCzqRPJS3TqDPHpw5vMKed9MmpmRsplwY2Ji62o_9raybBZxngjnFOezONkN5CewNEtgJtwphzgeBvujltJmWoAPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از سردار شهید محمدصالح اسدی، معاون اطلاعات ستاد کل نیروهای مسلح
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436439" target="_blank">📅 21:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حزب‌الله: محل تجمع خودروها و سربازان ارتش دشمن اسرائیلی در بندرگاه شهر «الناقوره» را با پهپاد انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/436438" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f395efd8.mp4?token=Qz-lwk2uQeXvIetheLoGdH612qBeyABDLpQGCpt_UqQNAomYtJ3mWJ8x3rKUXfFaRbY43sCDG1bGcStLBNGh2oy2K9LaM6vek18KBEy3oCs3y68HnwGIABqs6o1Dmn6t8_VCNbnBU8BoyLn7DNuS5PxryrTSshphgTxbQGqQDMF7QmW-iKqMLXgVc99VvDcpBi7ayCKG49FAF9iTcDFd0IgikuWDzuePEaSdn0DP70wASCJgjCL_zCJ-3fr8K_vXQdLe4zXboTqE16Bo2wxjt15oMeNi4VN4LYr4_2fClZqvuPK9K6Rs383MqPHrrKQ7FrXQHXyyyRoEKeGgc3j_HDHaj25addbe5DG9O50PtuZaok-vMhfJAf1opYBE1NMt_pNnUp3n5TFs27dRa8RTdhalSCjX6Wr-6mtcI6IDSu-GSLqGrU0-n-qIfJA6IczRchB5JR8IgclQmUuqRqyaUK6v3EPY5vDdN6RASe4zEC-P0DXdY0zgwnOW9e_lSvIoKdFjmyaIy6p-ZB-EUFpqB2F6YRQ4BZ7tEfjj2yExcKtZ4bimY3X4i0dK-peyRvEvJpYirGbjNHVeVE8nf6JuyVuHX20dnJtxTILFB-o295XqWwZWiHGa48tP_12pqB4ewcRPhQhDM_sBkc9bEvYAfjC0_704o0J4tCEAeji5ZTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f395efd8.mp4?token=Qz-lwk2uQeXvIetheLoGdH612qBeyABDLpQGCpt_UqQNAomYtJ3mWJ8x3rKUXfFaRbY43sCDG1bGcStLBNGh2oy2K9LaM6vek18KBEy3oCs3y68HnwGIABqs6o1Dmn6t8_VCNbnBU8BoyLn7DNuS5PxryrTSshphgTxbQGqQDMF7QmW-iKqMLXgVc99VvDcpBi7ayCKG49FAF9iTcDFd0IgikuWDzuePEaSdn0DP70wASCJgjCL_zCJ-3fr8K_vXQdLe4zXboTqE16Bo2wxjt15oMeNi4VN4LYr4_2fClZqvuPK9K6Rs383MqPHrrKQ7FrXQHXyyyRoEKeGgc3j_HDHaj25addbe5DG9O50PtuZaok-vMhfJAf1opYBE1NMt_pNnUp3n5TFs27dRa8RTdhalSCjX6Wr-6mtcI6IDSu-GSLqGrU0-n-qIfJA6IczRchB5JR8IgclQmUuqRqyaUK6v3EPY5vDdN6RASe4zEC-P0DXdY0zgwnOW9e_lSvIoKdFjmyaIy6p-ZB-EUFpqB2F6YRQ4BZ7tEfjj2yExcKtZ4bimY3X4i0dK-peyRvEvJpYirGbjNHVeVE8nf6JuyVuHX20dnJtxTILFB-o295XqWwZWiHGa48tP_12pqB4ewcRPhQhDM_sBkc9bEvYAfjC0_704o0J4tCEAeji5ZTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چهارمحال‌وبختیاری با برنوهای خود به تهران آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436437" target="_blank">📅 21:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
حزب‌الله: محل تجمع خودروها و سربازان ارتش دشمن اسرائیلی در بندرگاه شهر «الناقوره» را با پهپاد انتحاری هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436436" target="_blank">📅 21:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65ee77392.mp4?token=iElKSMOclewUTQjuyoL3Nc1bbzB6BKfJBc87ZaDTp8fK6MszHvTlpmzKq8GBFoawFUajxbwGXfd6D2HW8Bhbo34pcCe_lE0Kgrmr5MU2PZ5wcdPj9m4pkUMFPRNvKFXB3ElUBW2AsKJORF_CvoHlXzIoFNRJlGIry17tzd9omLuTT57k9oW-Ht8La8wYYZWGM02BKIzqZLzHM8lnc7FXODXidl0LV2yy-OgJVsR7V4DdRVYX6mA5QGrSB2xz3UEBfsmKCmbE7iogzMmIGsZ-BGKYHsy5fCmV26sHxF5VeHbZK5zOLq4y1DKO4ifoo-X1UQSOZ8HiAg5NmkLbmVkrY4xbB2rYgBsEqFi6JbF_WoC1bd0uBuBFAY-ZiTPpBBca0MPKS-3nsQ9SEXprxHg4EwpAbYpIQ32ycb4zZxy06FlForXn4zD-CbKpG1lKNKBEXtF94WB6GupYrIfi5MMeH1cW3m6yNmPhdJssfceSnEOgnIWAqnYpRHFTBZ2sP_OK8R3mFEtSNMaFY4jt0lw0yJiX0QHRZf0HKqA2cMmCOa0y4q7PqhPkch0lQBssi4RroKWlIRWqCuDvzK7KK59DAEEC2C2aniXQE9uBrV_OrwP-wPs3DJG9WGDZTqpuocWxnDgWQSjcvXBMaTDVXwatcemYCMRaZ_9DF1hDo98D3is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65ee77392.mp4?token=iElKSMOclewUTQjuyoL3Nc1bbzB6BKfJBc87ZaDTp8fK6MszHvTlpmzKq8GBFoawFUajxbwGXfd6D2HW8Bhbo34pcCe_lE0Kgrmr5MU2PZ5wcdPj9m4pkUMFPRNvKFXB3ElUBW2AsKJORF_CvoHlXzIoFNRJlGIry17tzd9omLuTT57k9oW-Ht8La8wYYZWGM02BKIzqZLzHM8lnc7FXODXidl0LV2yy-OgJVsR7V4DdRVYX6mA5QGrSB2xz3UEBfsmKCmbE7iogzMmIGsZ-BGKYHsy5fCmV26sHxF5VeHbZK5zOLq4y1DKO4ifoo-X1UQSOZ8HiAg5NmkLbmVkrY4xbB2rYgBsEqFi6JbF_WoC1bd0uBuBFAY-ZiTPpBBca0MPKS-3nsQ9SEXprxHg4EwpAbYpIQ32ycb4zZxy06FlForXn4zD-CbKpG1lKNKBEXtF94WB6GupYrIfi5MMeH1cW3m6yNmPhdJssfceSnEOgnIWAqnYpRHFTBZ2sP_OK8R3mFEtSNMaFY4jt0lw0yJiX0QHRZf0HKqA2cMmCOa0y4q7PqhPkch0lQBssi4RroKWlIRWqCuDvzK7KK59DAEEC2C2aniXQE9uBrV_OrwP-wPs3DJG9WGDZTqpuocWxnDgWQSjcvXBMaTDVXwatcemYCMRaZ_9DF1hDo98D3is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگی‌ترین غرفهٔ مردمی محلهٔ فلاح تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436435" target="_blank">📅 21:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436434">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3fecf0229.mp4?token=YEVcMf8Mi8_8sJ8Teo4e5Mey9CHIxEKUdyErp4nZX9pMW4FCfx-zRBUbug3XA1YZ_j5pkyQe1ZGZIB7NucSbVCXEbQgWP0i6LU9c7Lyny6UwQI-zzqtd4SrrDgl7XPraxTYOh5KuLoHj-OxyfC4CpX_UTamliPlDcIm2Pupy0vcl9NExT1T8v9S-QculNVA5Mh9QOheJlWGE36EoWKNegM2ep_q23NkJXmNYKsr_hS7OTOH-hQNvPxg8mqY2-QuhkRF7oj0rjkxWl1auray0NTDb5htFUHlJebCOPBTDcAbD5uyvWYc2rffg1xpguOT2Z9v1AvoVFh8n8i16m7iK9qE1EmeDXi7tOG_qgbXy8EUusKwYBddhK7DxqDhz-527djEXZhmDTlcu0fYdbpCSAu9QR_n7IlQI8lmQQ6LHOv6cKve9uV4RNS3KXNlkIYmppsq4-WZ6rwfOqzsWuiB2QD8Jr5dLOgRitKaiqGR3MjpwJhJoo8FSUAhnk8paD0tjpOLel7Ia1lZboB_11n3ozw8CHZt7LDvb20b2rslovtm7kFZMyEGuJvxbV0Gm0lFWaybhFi-sHMcPg6JwVrcpcK4Qr2aQ_w7JGakz9TUdBtsBArgY5BJ0jQggc3Eg-4B-l3PTphn48nWSG0oo2K7UuPd-lPFQrJB3SYG3BYXHBDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3fecf0229.mp4?token=YEVcMf8Mi8_8sJ8Teo4e5Mey9CHIxEKUdyErp4nZX9pMW4FCfx-zRBUbug3XA1YZ_j5pkyQe1ZGZIB7NucSbVCXEbQgWP0i6LU9c7Lyny6UwQI-zzqtd4SrrDgl7XPraxTYOh5KuLoHj-OxyfC4CpX_UTamliPlDcIm2Pupy0vcl9NExT1T8v9S-QculNVA5Mh9QOheJlWGE36EoWKNegM2ep_q23NkJXmNYKsr_hS7OTOH-hQNvPxg8mqY2-QuhkRF7oj0rjkxWl1auray0NTDb5htFUHlJebCOPBTDcAbD5uyvWYc2rffg1xpguOT2Z9v1AvoVFh8n8i16m7iK9qE1EmeDXi7tOG_qgbXy8EUusKwYBddhK7DxqDhz-527djEXZhmDTlcu0fYdbpCSAu9QR_n7IlQI8lmQQ6LHOv6cKve9uV4RNS3KXNlkIYmppsq4-WZ6rwfOqzsWuiB2QD8Jr5dLOgRitKaiqGR3MjpwJhJoo8FSUAhnk8paD0tjpOLel7Ia1lZboB_11n3ozw8CHZt7LDvb20b2rslovtm7kFZMyEGuJvxbV0Gm0lFWaybhFi-sHMcPg6JwVrcpcK4Qr2aQ_w7JGakz9TUdBtsBArgY5BJ0jQggc3Eg-4B-l3PTphn48nWSG0oo2K7UuPd-lPFQrJB3SYG3BYXHBDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان متفاوت عروس‌ و دامادها در تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436434" target="_blank">📅 21:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خسارت خوردروهای آسیب‌دیده در جنگ‌های ۱۲ و ۴۰ روزه تعیین‌تکلیف شد
🔹
یزدی‌خواه، نمایندهٔ‌ تهران در مجلس: خوشبختانه با تلاش‌های صورت‌گرفته، خسارت خودروهای آسیب‌دیده در جنگ ۱۲ روزه و بخش عمده‌ای از موارد مربوط به جنگ ۴۰ روزه رمضان تعیین‌تکلیف شده است.
🔹
خسارت‌های خرد و مبالغ زیر ۳۰ میلیون تومان عمدتاً پرداخت شده است. ارزیابی موارد بین ۳۰ میلیون تا یک میلیارد تومان به پایان رسیده، منابع مالی آن تأمین شده و هم‌اکنون در مرحلهٔ شروع پرداخت قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436433" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436432">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC1fSJCZQOjgzDl-nJCaSCohdDOh_ID-tcKMikuxlm2-380e6qHsXh8fHG4mzkA9j4mSADo1VLFMrx1d_otaThz1Vtp_M5NdkQVCKDUa0gvlf-aMDQ3tXUnURSX2bSVx78PuIGgJoeLOaDR8myPIqaosQkCSylNQ9bcBwvOa6j-m-rddsJG5xYFcGcKIX3T9G92prD96CkHpTIodYyb8TZK5b1BqZz2SptD-EDNwRa10DorzrKrOsXeOroiqZfHhGuHWls3lDsdBwLkBvkKqNtd2Cf9uqSuDGYr_Hz8ElG5Aj9kkKC9vsrDK5Vb9JUpAYm06f2FYnjGbgFxdB7ZsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حاضر به دادن هیچ امتیازی به ایران نیستم!
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/436432" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436431">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261e4d84af.mp4?token=lsi7mfMzTJeTWfxf5YlWdbwbOzLVcLRZp8mB_6d0fD5d_dNEtD3nNGXcRFabXUDa08NKhQtdEbBt9F-JHwMZlMXMUwW97q4c0yO3zJtEGi49VNhdTevFU-jQdSyIPZmhW8eacJ2r6oFv504HV0EhcMSTPAHK593weMRU-Jes8r7-XyT5bK8LU9MKPaoraKg4CnYdTni86t5vZzGcNOCMWFGRNTIAU73_MyUJKM0zBgSTUJQeWWq8Mo0V8YIW6SiaQHC_elPI3cVYxxuxNUgPL6VGAg0w-o58HBt_bYmvS8jDMW4A7vTXQI9ngHlhnuRMDiSZ9-StZmAxREYqyEk6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261e4d84af.mp4?token=lsi7mfMzTJeTWfxf5YlWdbwbOzLVcLRZp8mB_6d0fD5d_dNEtD3nNGXcRFabXUDa08NKhQtdEbBt9F-JHwMZlMXMUwW97q4c0yO3zJtEGi49VNhdTevFU-jQdSyIPZmhW8eacJ2r6oFv504HV0EhcMSTPAHK593weMRU-Jes8r7-XyT5bK8LU9MKPaoraKg4CnYdTni86t5vZzGcNOCMWFGRNTIAU73_MyUJKM0zBgSTUJQeWWq8Mo0V8YIW6SiaQHC_elPI3cVYxxuxNUgPL6VGAg0w-o58HBt_bYmvS8jDMW4A7vTXQI9ngHlhnuRMDiSZ9-StZmAxREYqyEk6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که از رهبر شهیدمان گرفته‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436431" target="_blank">📅 20:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
دانشجویان همدانی برای عروسی هم خیابان را ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436430" target="_blank">📅 20:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEoDs3gsCUuLgvPzh-26xX0-0x2yr7ypwRDhXBTIcTGMD3VlZPNvLZ3E4rch4Nm030vFF-5nhfPJUxLFMfV2I3OK6x1S37JfsFlhOXh6eEQM4f66gwMkWBOiGicF6sLD9XMlRpJD0kN2oRHq58-xsNbFg9FmQ-0MvbHQDN8sLo0B0GOpMGP5lNqD_WbVz9OZ2lvlTnEYyzy8CWmmiBNz7yYoBtMEUJ7q5YyV-6zJ5cXFHi0XdbvPiWvGR98240bjG7b37FEiyw0N8zMvChZxJGynlCQJ1VqFcIUNi7qBlZHgokVDZ-b2_2mu5WdO19Ee1ZP17eCDsETCG36EdFcZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار حزب‌الله عراق به دولت اردن
🔹
حزب‌الله عراق: بخش اعظم عملیات شناسایی آمریکا و رژیم صهیونیستی از مبدا اردن انجام می‌شود و این مقدمه‌ای برای انجام اقدامات خصمانه در داخل عراق است لذا دولت امّان باید از اتفاقات جنگ اخیر درس بگیرد چرا که کاسه صبر درحال لبریزشدن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436429" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzz1DOPn9Ng6-viL5aQCpR2NPKb-Zuexh_0mBTZ-LnsSDh4D8BUZ8XkRFfDGLnNGAavv_3f1UsHUrjrmJuQ45JJ_h8BwA9xdSQc1_kWWr-nw9GgN0kf2WLAN59ETvCBJVLeNHzAXp5Pr6W82ehPV1V6oCtQKlmE3DGveGQsKR0DQKAMFilx7c8Sh5PLTUz_Wf2vbyXeNydR-P4rp6evSkm_VJNYsGZAesf-VJf__FmYjVxV9vKKPjkPgTlxZil_3Cb_htK7_L52in48H2U3xqQ61Hr1hfjayUEqkjbAnMAPSB-OoA90mtZy7bqL_iIYDZT3FJeNaD4GWIloqL9o3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام اروپایی: به‌خاطر جنگ ایران، با شوک تورمی مواجهیم
🔹
کمیسر اقتصادی اتحادیه اروپا:  در پیش‌بینی‌های اقتصادی ارقام رشد اقتصادی اروپا به سمت پایین و آمار تورم به سمت بالا تغییر خواهند کرد.
🔹
ما با یک شوک رکود تورمی روبرو هستیم و آزادسازی ذخایر استراتژیک نفت توسط اتحادیه اروپا درحال وقوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/436428" target="_blank">📅 20:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvflkDpuv_6Hh3_-xNyovJ4zsB3p2bGvSOnY3dhRqDjwvA95y9pvZg82LBAbn3KTfSwhIrCxSF77eSuLC4rhKmAzisxr4CtfRkrdWuytaV1QeGLiNxzTb0092mLsoLtLCM8mFHo5mhaPLbPkJMlghte54czN5DwU1iR1XQt_59BNRJ4c-jZBJoRe_YZVMKExv84lSR-MhG72vYvsJXbEHtkcj6SYhmhNTeNhz2JgWMvLlSw_Xz6LScR-eSfx0u1AXGbzpYbJIIco5B6ZRz32QRx1drbcnCfPJ95OGNsyVVMoiisjqMzEHfzSneGdXsAZfO4SJG1336KqlsPScPWgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYmTK3ndKoyRwKBh8KmezExdxgFtUvJ5zSKQfNuPYmMdSVtpYha05YZhmzJ25QTw1vL2Q5aOXKzshuPWSRMZSuaZ4l7voXb1d98m0luIuODNTliGWGWtgagDnvYPgz-0hN5zXiqmSuzZ1NLH-U65EprFIKRNaNMysa_jWy6YO0o_IPGXF3j75CIm0TbX-DvsfftRhtvsFNkK0Y4EFCniUG1iEof5LB2FHQ0BG6nMf0ojnxbVREswmOeryOKIOJJVSH4fx0MCcgu6nfOzbb8aRZkg7pHObElzXgaOs6ndKfnsqA_ScPpAF7M9WX1S33JVjo6bylS2qOKGNp_mBdZM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNcBnb_oE7YTmuD6vrhIZeQWtrDVk1waWhqfzhicBNflK_gVTu8ESxMSt1KrXmuBscPlbUm3iLnkR9ceoIMV9KsVth5LXps0pUx6Clq5OvihlwdggCm9DPmtNB54Rt2tQrGCD8o6oXnP71ZpP_qjh7jF5HevJ77nZ00g1gyaBitylBs1Qs8xTUnBMFHlZ_znmr9CA9-jOAvCqx-9SrNJA_XXgLJos60sik9Gqz19IuWFtIyN3ikD8MTQgKZ1t5G6g6EfTaLx7RR8RbsbbVtmVzG18JNfNjRW4C9M0mqs8KQdBJKzpbSryxF-x8yehwelAQvTtVp6kYayo8ZdAlFEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D83YRfzJUtKfEA3Sk5GdoW9xSPlkmlqMKjgNQF2gGBcZ8Ad31s88CZNpsYQiICK0q7UMCzaT03cknjtd00r0E29sUr-nYWR3bIMulyisq843ladEqpn41dgecCu5fGFRwqYmWDGRlKxmXSE9KsgXl2u5HPHOmBU3kKmxcdYNhTSawShdwriFhmnjIuLJAu3-Xk62BUfscSiyUrccggucPnhHMFHEXEeqz4QOj3bz92ujcW-kVzYmtH8IZzQb38jL7UeTDJo2FCDXxLZ-1xiPfE-ccOjhAUmndNZNzFjW2Q21xZiLoRlqzNz7oGx80rFTdhsfb6HTVy8EiOanRygfUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گردوخاک آسمان بغداد و کربلا را نارنجی کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436424" target="_blank">📅 20:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dd64fcd8.mp4?token=l9mwtd-AQGXNH52ClWALMgFvO4hAYnOIt-QPML8okfxxCPrIZwGlemvmnSc_CHlX3MbNpoat7MjBpJTBQ27a_p7WX9jEeMjfpbFlOxuZhh2L9DnKqKlU905ONA5Su9rIIbtwpioP4TFKiwaD5NqboX2k4D23_exJews9xUvKVvqb5H4ganrVoEIVoFR5_nHoj86Vm4PS65sgMG4SHCEVKhfddKDMc-6GbEbPrwH56wfQwvqApHzLEz_17Scjail5f-MN5LgI14DopCeo2o-OOZZQnoROQlMPjV5_XY7XXyKByvlCDqf_k-Gnr2jNonq8V8AoKDgYB4r4SbSa_X7PFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dd64fcd8.mp4?token=l9mwtd-AQGXNH52ClWALMgFvO4hAYnOIt-QPML8okfxxCPrIZwGlemvmnSc_CHlX3MbNpoat7MjBpJTBQ27a_p7WX9jEeMjfpbFlOxuZhh2L9DnKqKlU905ONA5Su9rIIbtwpioP4TFKiwaD5NqboX2k4D23_exJews9xUvKVvqb5H4ganrVoEIVoFR5_nHoj86Vm4PS65sgMG4SHCEVKhfddKDMc-6GbEbPrwH56wfQwvqApHzLEz_17Scjail5f-MN5LgI14DopCeo2o-OOZZQnoROQlMPjV5_XY7XXyKByvlCDqf_k-Gnr2jNonq8V8AoKDgYB4r4SbSa_X7PFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/436423" target="_blank">📅 20:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
حزب‌الله: تمامی مواضع و محل‌های استقرار ارتش دشمن اسرائیلی در شهرک‌های «الخیام»، «الطیبه»، «دیر میماس» و در مناطق «خله راج»، «تله الحمامص» و «تله العویضه» با گلوله‌های توپخانه و شلیک موشک‌های سنگین هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/436422" target="_blank">📅 20:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436414">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a35eed28d.mp4?token=Yn5Oen-bujDbQyQfenKSZhQJga4lIRxH3ee0-wz3U5zjtWkwvI6bPEpzGLI5I4h7nPRzFr85Ad0UWJjTLsZOKa3FL89tX5kLIy5I3B_3H-aWXE1vXAPnZz2Ao4F2xeCP9Vjf3j0XCavp3zOIGG1fwVz3Psm2ggLCxVSHeAo009vI_jhOJvx7BqdhRa-8WiiXnp-ENkBpd-R3cWbV5Fi8xN6jd2LxtjIKkLFmj_-Ps0NRFsNbxt7q_3Vvyx59i8JeqXahdBBlH4ivuCHVzqmEZgGq3O6VS-nFBhs9EiGokL4IOawclygxsykPFJelA8eHZa4jtwtMlqn1ICM1LEazkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a35eed28d.mp4?token=Yn5Oen-bujDbQyQfenKSZhQJga4lIRxH3ee0-wz3U5zjtWkwvI6bPEpzGLI5I4h7nPRzFr85Ad0UWJjTLsZOKa3FL89tX5kLIy5I3B_3H-aWXE1vXAPnZz2Ao4F2xeCP9Vjf3j0XCavp3zOIGG1fwVz3Psm2ggLCxVSHeAo009vI_jhOJvx7BqdhRa-8WiiXnp-ENkBpd-R3cWbV5Fi8xN6jd2LxtjIKkLFmj_-Ps0NRFsNbxt7q_3Vvyx59i8JeqXahdBBlH4ivuCHVzqmEZgGq3O6VS-nFBhs9EiGokL4IOawclygxsykPFJelA8eHZa4jtwtMlqn1ICM1LEazkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار شهید امیرعبداللهیان در دومین سالگرد شهادتش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/436414" target="_blank">📅 19:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436413">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2a92833e.mp4?token=Kjzx5kXl1_9vumlXvHGZJZxynwibyXYq6yXCzoCi2Yw2rcckPqXlMDoC8IavsHgsIcZ9r3RLBaGbQxhwxtjSJ7YdLreF5ZC2fp8YxcLut13CdE6kwgooxVJ-eG9AABBwFLB6y19EbkwRbXB9C2WKHkh_vSolvwRkRxei5WoOQCZDOxrY02yH4iN3y271c3n3j5a0yPq40zihf3lQ-6gHLVh-tqygNMTzkMaqaWtKqqdfrEyZKFGoxMiYqU0OUf-upj3NicUW-eHGjISI873VHWIjNSznnVrOyjgcar5THGQ3fd6wfpcw1PfNe7B7tu7mnaaNiJbVUl7Fcj2dJCS83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2a92833e.mp4?token=Kjzx5kXl1_9vumlXvHGZJZxynwibyXYq6yXCzoCi2Yw2rcckPqXlMDoC8IavsHgsIcZ9r3RLBaGbQxhwxtjSJ7YdLreF5ZC2fp8YxcLut13CdE6kwgooxVJ-eG9AABBwFLB6y19EbkwRbXB9C2WKHkh_vSolvwRkRxei5WoOQCZDOxrY02yH4iN3y271c3n3j5a0yPq40zihf3lQ-6gHLVh-tqygNMTzkMaqaWtKqqdfrEyZKFGoxMiYqU0OUf-upj3NicUW-eHGjISI873VHWIjNSznnVrOyjgcar5THGQ3fd6wfpcw1PfNe7B7tu7mnaaNiJbVUl7Fcj2dJCS83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آلمان: اقداماتی نظیر اعزام «ناوگروه کمک‌رسانی به غزه» را تأیید نمی‌کنیم
🔹
این کار خطرناک است. در گذشته نیز چنین ناوگروه‌های کمک‌رسانی حرکت کردند اما هیچ‌کدام نتوانستند به نوار غزه برسند.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/436413" target="_blank">📅 19:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کشف ۵۳ سلاح غیرمجاز در اهواز
🔹
معاون دادستان اهواز: درپی اجرای طرح کشف سلاح از ابتدای اردیبهشت، ۵۳ سلاح غیرمجاز به‌همراه ۵۶۵ فشنگ کشف شده و در این رابطه افرادی دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/436412" target="_blank">📅 19:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
حزب‌الله: مقر تازه‌ایجادشدهٔ ارتش صهیونیستی را در شهرک «مارون‌الراس» با ۲ پهپاد انتحاری هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436411" target="_blank">📅 19:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ATKYHGbUg5G_-4IXQ2c2Pm6KjkgdyHku5qeZGM79xqG4LtbYof_aOpTmWkvDPhp3pQEeQM2V-TQFhPesXjBg75fx7MKB1Uc6RHa4jOCpVcfZ4e95J7QZ7uv9HA_UPcth6uDsChiNZORj1KnNWDIpYDz-g0SjYSUCerx0yfGnmVXC1p2BttzLOqDrWXJPsbeDAhOW6mZ3ussFYlT38iH9DAKO-wFXSjRcVlKE7vmqibUxVQ2UGqPWN7Gc7ASToJgS01eKkB4Er4TS4KuDH-z7s9Hm9IeY05jgVqNg1PFYCSlm6590TF3YUGBhrKxl8L_PCmgsgK5srqJ5hHtVzg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کتاب یک» از امشب روی آنتن شبکه یک
🔹
برنامۀ تلویزیونی «کتاب یک» با محوریت معرفی و بررسی آثار مکتوب رهبر شهید انقلاب، حضرت آیت‌الله‌العظمی شهید خامنه‌ای (رضوان‌الله‌تعالی‌علیه)، از دوشنبه هرشب ساعت ۲۳ روی آنتن شبکه یک سیما می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436410" target="_blank">📅 19:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436409">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee3bbf1fd.mp4?token=jUNn4EXKckEGe2xvluZNRuWjwYa8-DocWTFi6SoEIvme2gErxPFgewTQ93N5vpZAXRcOWLGZGo8pqNEXDYD9aCi91KTMasuxCFarXDFcFNN05WwzdSuoq8-Q2J1qh5aDqje625YadisEaXqnW_sZ1yKEoQbxMYvKsaIPDhqol261KQkIukMon9rFRJ23jqGKOk2jV_cX6Pl5iunOvBFNBqO2y4Z_YnvaZixPzvp82VWkzbRL8y8MZ13xy_v2QjePyLeC3yrhXJLBDNaYoKYtNF8RO77w9D_NUFQnhp1K7_j43Dw3hndqsZcI90R9JWZrybNgHDwehh_QFASX9eHrOi1gFVcdi0SCZGnb9k8RcdyB5WaDdYKCNSEoOJmyNC3v8F6HvqV-urk6hMA4P3xL5KBTNITqBG_DIIRiPLofbMJ0Y5_v7dEMlnrOLz3br2MWzIoFV_NDucTpokFAnOEEU0IPTkHLZpYPTzopNHKi3MZH_3YFdh8fekc0uU161oMQXFbj-tTB0D_uqLqwzXWdow4pn0MtDF5EIAyNib3a7wRacbw-5kmhw-rzutzMOn-4OoP-WbUYaFOxFK61SoigU9U1d9BlcJX7-QERevO8K2Fctzlg8b_o95Tjfkpa1CsrODqhTmSwaOx1VWIXXeiEuM-MoY_tElR3O_G-hHF56cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee3bbf1fd.mp4?token=jUNn4EXKckEGe2xvluZNRuWjwYa8-DocWTFi6SoEIvme2gErxPFgewTQ93N5vpZAXRcOWLGZGo8pqNEXDYD9aCi91KTMasuxCFarXDFcFNN05WwzdSuoq8-Q2J1qh5aDqje625YadisEaXqnW_sZ1yKEoQbxMYvKsaIPDhqol261KQkIukMon9rFRJ23jqGKOk2jV_cX6Pl5iunOvBFNBqO2y4Z_YnvaZixPzvp82VWkzbRL8y8MZ13xy_v2QjePyLeC3yrhXJLBDNaYoKYtNF8RO77w9D_NUFQnhp1K7_j43Dw3hndqsZcI90R9JWZrybNgHDwehh_QFASX9eHrOi1gFVcdi0SCZGnb9k8RcdyB5WaDdYKCNSEoOJmyNC3v8F6HvqV-urk6hMA4P3xL5KBTNITqBG_DIIRiPLofbMJ0Y5_v7dEMlnrOLz3br2MWzIoFV_NDucTpokFAnOEEU0IPTkHLZpYPTzopNHKi3MZH_3YFdh8fekc0uU161oMQXFbj-tTB0D_uqLqwzXWdow4pn0MtDF5EIAyNib3a7wRacbw-5kmhw-rzutzMOn-4OoP-WbUYaFOxFK61SoigU9U1d9BlcJX7-QERevO8K2Fctzlg8b_o95Tjfkpa1CsrODqhTmSwaOx1VWIXXeiEuM-MoY_tElR3O_G-hHF56cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این زوج‌ها زندگی مشترکشان را در میدان آغاز کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/436409" target="_blank">📅 19:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436408">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/436408" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436407">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/436407" target="_blank">📅 19:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436406">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIW613Jv-XBvDGea8RPtb3quSSdcWktHpe4yQzd-NsOwr3d79DY6UrmjTPYFpRvNmfHuO53CbisGDB7eb6pxIBEXGWC_arjqkT2RR3J270Cbf4oUyaEyGujabee9QDPLRDgfF5lmGCy8arrtPMtNhQfECO107beboHY_zhl1UAXNLwp0OPUPQlQqJkswhVvvpWNW4y7dwS0nZDs-xoeWWQyINYHySIpuKpJrdVcKAEcdfVy2CxnbSGw978fHOTnXGFtkJXrfRnFHE91DJK6vWkoZaz96uRzV9oMgG0NW-KugxjDb7VBcfN6mJnps3uCZC0Wl3xGRjPvta-YKC71XrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند به بالاترین تعداد از زمان محاصرهٔ آمریکا علیه بنادر ایران رسیده است.
🔹
این شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران می‌گوید: این نادرست است، تعداد زیادی نفتکش در محدودهٔ محاصره وجود دارد اما تولید نفت خود را مدیریت کرده و ذخیره‌سازی‌هایی هم در خشکی انجام داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436406" target="_blank">📅 19:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMemzuQXOLmeqaWOQIgS45Kl0-pL04KdSRz9JMwW8HN6k6H5KuIAJmxYzLf3LVSS1rCjjzyvsFTwYpfNZC3eDzrm-lUmzJ16d7RbdgD3aH7LJ5BqUffi--9gbCP9sJTTQ3ni0qzp5SH3ydP8VsewLktp1H3WlUbiHFNunhor4loPNFYRZBurvzhGCx5bPAF9YHG_HkKMM77jNl8u3k-wK9Z-H-hH-fqzXfuXvdvx5ns_eWEaRT-l88nIsa0QYfsCkfUMdkvO8b-rHU6a5oP3nqo1o0BV6IuRiaUDLj3sxizzzBDzQ7ZrMEk7apjHV0LPziIGZUMz-7Rn3o3qnQeUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBHdyrCfct0ypLVslWmDgU1inh96ka0ATd9_rwFUhg7nETq8t6RafroIZieWYi2un-oXhYC3OzJ1IpxUjScZK54OBrRxQQaWR2i45V8H5pOAWvfBIK7E6nPzkk4BfIOYiI8LZJ3JrdRFdXyRSc1sBuVC7VUPMWYQAgawWFz3fbSNglZSMBL9xgUkmeyCpUUbQe-gATgizv0QeKsBUZHka4ThIkrySMjp2ujMlSRQ6_hxqbLNrFXhopWwWxWxS-JIRzRX9ZVH5Uhrl_TU-SxPq5932LdqhmTI7Aelx3P8U45Jq2MeBcvKJujqN34BONqlYNXcl2p8QsuRt6XpIrvdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htK-oDcZ-joFvBfpp5pzy_SeYtD8PDPAC5hHjX6bZsxywkWKhNVvdyeWw69mazq6jgu1Li1r4SPWRMII5pDiSaKYgRjtIFGb2V8kAwSrlTG2NWyoPKfjoC9dMWEGZrevG8RCm52kMPvkDPs_VuRX83QLbCbFALd-WaOhkeM86Acx_pSQ2U_FXyKsRzdoHY5RVDK6OuAb2KuhjGNEaJI0UvzmpKpONknc_34bIPUShxi9XpU45eYN0AGgejsEifMt_jl5cua_74EAsK4IFw5s6h54oBNXJQWaYDO5mPQSslJozT-99BVzvBHHP83r6jcyC_x4pF6kSYNP1CnUPDq2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-BZQrS4Gjl5dFMZD1rCJdc6wQPwk8AXdql2g7zJe8y429DMf4GaTfheAswaUq_S-RLLC8pYZ4YDyYkqgKvln9t1Mk6CDI20qcngVDioO1eC5oj4-soOLFFaZ9Le1ktodoCmzeYge9JXT7Zqoyazenm_Fl3zFxP9xGTupwjLlKJabTB2KMFUHDSclemNnMGWV4sRJd1BB3F6_YTnEbUPmG4XZq5hq8SDjK6juTzgEo-o6lsojWcd_6s2jSqnbAyr-42SvsyUe-iTtSwCn5AmMJ_VY3DPuuo0WDYg9rGgx-Jkz3tlXnpYNFqO0TAtD23QjmTdKYDc4XIEPp8OaUuNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgDqPH8Mwl4im0vjrMUWLZqB-hsC6KSPaQAqYUfOjJCj3fC8TBgSTHsr7wHnVllQPPoxm2QiIQQmPADGcEmCb7GhdmQjUUK4KD9o4fTIcJmqA1KLJ-Bkt4W2ulFuJ_ynt17gBrRoFDs77ccnlRyTnUbaEBsBKbDDgap-dvvcF4ed4zPT6Qdi0X280tDAx1GvBztfO2G8QRWXY1vAIYKLlYJWpJsgr7WhkPDQyMyhtFErjit7OA8k7-ARCqyJruvITE1eX3RKvGrGkL3vnzrNYisZIf1MCXtEPOjR8q3PrtApVdQV1kLztJJZPzOhmy7dyYxiGRvpWPH8LbWyytYx9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادبود شهید علی لاریجانی در مسجد بلال صداوسیما
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436401" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1301cf2b27.mp4?token=R1paWqNpES2kighGd9hCDbHZfwF1UvdY43SAuwMK1RtSATbrZB8BY3HLc3Km5NU5yl9Fn66FA_hQPQlVRlIR-bU27YHuYgnM2mbBuQqjrJXnQfvMAUsbX8hM76cF5Ql6SC-v_s9GKmun9PBDNGUPChq-48YNjoeFM5uxlUAQ2wu0KIfkypr8Qa475l9jeQpZCBjvhZHmKHwIhSCVOS-xL1Wl2bBDw41FN6sOKZfv9tx9wMV88ZlsB8xxxz2R_J0Vac_3KM_VxcMeh4zNYu6KFWfuXQ0iX9KaP5xQqo1eUps5uwTtyl5kBd3hEAuS5_y8QDJTcuCTqfKb4641s8uPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1301cf2b27.mp4?token=R1paWqNpES2kighGd9hCDbHZfwF1UvdY43SAuwMK1RtSATbrZB8BY3HLc3Km5NU5yl9Fn66FA_hQPQlVRlIR-bU27YHuYgnM2mbBuQqjrJXnQfvMAUsbX8hM76cF5Ql6SC-v_s9GKmun9PBDNGUPChq-48YNjoeFM5uxlUAQ2wu0KIfkypr8Qa475l9jeQpZCBjvhZHmKHwIhSCVOS-xL1Wl2bBDw41FN6sOKZfv9tx9wMV88ZlsB8xxxz2R_J0Vac_3KM_VxcMeh4zNYu6KFWfuXQ0iX9KaP5xQqo1eUps5uwTtyl5kBd3hEAuS5_y8QDJTcuCTqfKb4641s8uPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار وزیر کشور پاکستان با عراقچی
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436400" target="_blank">📅 19:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مخالفت AFC با درخواست فدراسیون فوتبال
🔹
کنفدراسیون فوتبال آسیا با درخواست فدراسیون فوتبال ایران برای تغییر مهلت معرفی ۳ نماینده ایران در آسیا مخالفت کرد.
🔹
ای‌اف‌سی هفته گذشته به فدراسیون فوتبال ایران اطلاع داده که تا ۱۰ خرداد فرصت دارد تا نمایندگان خود در…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/436398" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYmgZux_kTxWTQTY73Q9X-FuADu8dl9Oadtv5qZ2V06sAD3QMoDohRckaonSy_a7HQbzOhPBZ6ZSsS0VY5nvw1kp4ddW9s4Bk4VvHR1MGOdzHw5nEnYLKUbrENA4dDxhZQFqR4AH0z4ksCuDbEetVyppNCxTi-OBsXY6l5r0rUeZAQ-FgRRrqiGcnU4G9qLi-BEPillPfuCL_g8W6lp7dQ4IucfQykiCEJORH80g3kaT0x4LfXH46w_OjKTpNdMhmhvixGjDJzIiLrwGbT03vn75qPYqTn_5-ob_BHQdVWWU-H1gfMAqmgNaOduRjUw4LeucVbkDv41R1elHLN7m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: ادعای باقی‌ماندن قدرت موشکی ایران، خبر جعلی نیویورک‌تایمز است
🔸
خبرنگار: شما گزارش‌های مربوط به توانمندی موشکی و سکوهای پرتاب موشکی که باقی مانده‌اند را دیده‌اید؟
🔹
ترامپ: بله. فکر می‌کنم این‌ها اخبار جعلی نیویورک‌تایمز است. احتمالا ۸۰ درصد لانچرهای…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436396" target="_blank">📅 18:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfgJvP7I6co12n1arYNJzKv2w0LmwFI2dMXzuWMWyJFnYp-CuzGdpi87xeO7crKV1QOEznog1JWDVH2TwjGsSCQOl_L6qfH22av5X2D8rZ7esQRo3PYHHiBEBjAi9fG8ODzLetvL4mvx_SdC46uGIZtMeNnYj2omK0Qtbq-laa6Qdhgg5AWZodc2Qu7J8Onkyhzjm5wnBiIno7QUoQz6QS4LS2xrFyhDyo7X43BrWbI-N_9dNJyHKGnhbh6PBMphguwod5hnzUNzE9twyL-H48-bj35InDYslDbCP9a2L90xc1eHvRhqDwalMwM765DYZ21DAE6Ar3iwdiLuT1sPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ باشگاه ایران در آستانهٔ کسب مجوز آسیایی
🔹
طبق اطلاع خبرنگار فارس، برای فصل آینده ۶ باشگاه لیگ برتری مجوز حرفه‌ای از کنفدراسیون فوتبال آسیا دریافت خواهند کرد.
🔹
به‌نظر می‌رسد استقلال، تراکتور، گل‌گهر سیرجان، چادرملوی اردکان و پرسپولیس از جمله باشگاه‌هایی هستند که مجوز حرفه‌ای دریافت می‌کنند؛ سپاهان نیز امکان دارد با تک‌ماده مجوز حرفه‌ای بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436395" target="_blank">📅 18:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436388">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Df9svj10_LAsHGFwDOmWrXcjvEEgsyOZSBFngxe5ehXKjsOMQ0MWrYos-Gvwpdjn9hc4_hW1QnnYO62ODUEgJ8mdj9cQU2teQHgkhdN-cIdizj72xp6kqraqf1CitW7iP26xm09be5Yjt56R-dXBaM2izdgyTz6YntRQqn5vGko2RYdtzkofkFNk3hrObG0V75fxhVWrJ_0It2w-C5smHQRkabxjoJbJ4uHSGYmWgKwKW0G8TzKY5JNxwSqlD2tfVYFuBkCf01ZobyLWFR5ENzmYAtZ1wnEs1kq9-u5X-t9gFUOeX6IDKLaiKHTh_KAo6OoCf0arS0KeCceWsVcXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTNB6HY2I_BPxVBIr3S-Tv2_9-q7_Eqw_Ss1rbiM5HJ7sY_uH7w8bvkw1Y9_KRArykkxds7w38Q7t2Dl5_HBevjKyeJcFXM2r_48VXNIBqel0TRZl5i4bZpwjpKkgYevXbhaopHBSP91gFtXN3XQxHP4r62UFbPz9UWAKH96IrIOV22UWbRgLnNkOVf64TJe2pVXkyUMQRdBs7FgI632A9v9G-haEabSb_0NCbiwA88ppQ9cke6IpeLe8WM_-HQHHBL8UTkiejHpgs6rnDb5MPdcvJbbp9tGu-vOuLK6xDbU6yxnMxQuyaCg5VMkqE20H7g64u0REqqzbBaHNa0Qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rngslu2O9vgjXmwBO9haB66bbewtTGZigPLkDdX50-Jcv2Zm0HgaBADIZr81tqTF2iaL9-jg_pSA3tLRjetF6Bm8GQKBjJcTc90Y8w6rg7rsUDtlL7ybIRUxqIeA-tUur6Mf_dZkxgUteBx3lbyFpYI7GEtu0DHabY6yaZ2xXJ02l9a_2tdGbPTWqv_BTOpOkiPbomCsVOrf4BVFbAJ6O9ZGCVtPg7owvc4fiy07Kx7gz4V0aXt_gn2jfcOtu-sXeKmFxiZ7ZYXeFf9KHB86VdMF0SBZq5O_h1YHHv3XX0iE6T1DvT1MeabH91NMGV9-zZWAxR8oa22oOIJvQoKo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTWRcDjUSSTI15rmHT0fr3M5E4VroUsB4mh8d6y_oPFLjHXxpPiwDOAL_Ulvq7N1kFEEOHz17D1WIPvFTbyFqD9YNxu-kGzjUFmDtZjth4Ko92xtgToMsStv0OXeoen8QtoDHF4aV4STXjoluin1gLWMpDQxyOlgZHIwyBxvM--mxtv1D9pRB5-XbiABj96aDIEhubTpd2Civ6vfNBkUXNZKuqvyAvPVBZzJNWavfQXJKTWpCUwV-pEtpAUozn7OkfanuGpLPV4ZCQq0BNUYliJ70i6jI3gjy4rOOH-7NubW6ua1VDetKF6tQX3TEBxF5u98919XKPKJDckLIKV5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGIDxLrxAMlawFEMyZTwZ8Qkcrai-Cj5Y-Zb6CF4o9eF2wWE-Fu-uVeFb7fXme2oP2y5LVESb2Dg1B5RH_UYhtxB4t3tuWbo9ewiSlMpOAGT9Ri2ljazrTupk2QfqESYABdaq71tSe2QuUwCk6Lgh44ZnlHPpEmP12O_p9v2Fof6fsFV-bxpFwoa-u_Oas82tAW8Xkatv28IQj1_KOD_rZfW2T40PmhT1mx4uasM8B-YjK2gvrOIUXw6HUSh4QKteAaNSiD9bEGpkH_PCqfnX7XSeE2kyTFt-caJySftsP648pwDfbG0bPS8vKyB3laC_1IMPKuX_K4ZxYZPJakotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WApYYnrsFJXRBjklOBP5MD3H73ktBLJlS3LlOaq2F3gdN7kadWqL2gB4CkfxN2G-RmP9EsphjhC0LZBJqE6WGW-ZNkDvj2gXFVGpGnfxDuvznZ85LNJVWFVTGHte1XT5xqmeCY0FP5Oe-TW0WTWA7iZeufSshP8fw50MgQV-d1UTz2f96PyByZ_ribrejatnHA4Mj3gb9fw9Qp5b5zKQLzdHhFWq67dx3CH-t72-DUsekjX9KnvDYIv9-egmNvFzJ2tWuV0ngelh_OKHm7ieryhCcnU3ac0rKTAa2Iwt3kgBLBMLlYrzNMtobjSCgjzdSC7DJCbJqLxLTueVassRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSk5zAj1P6Yh16xkspQ68VhaYO6tOWi0uKoyVCPGVUedhMx8cC2iTgQRmCD2LDIJ_YloKH7TRGMx0n6yhCByX0GRPYAPNwmwjbd4t7ViTlEkXpZoyV0-CtIVj7Em6eCHtAkg-wqeT0znr6exqAM-H0i2h9aOyMIQC40lhUYrRyOcGhLFVM6phUOWUa4FRDxjpjKD7G1f0ddht6hT8Yt2D9sblsZFTxaTUesl9dvHjwSeyEX5r6GSL1A-8sarZzBUf6aKypfuqBY4UnADMzIs7z2SmP7xnwV7upPHMTmt4DpMPanqlr47fp1zcFTB-YYjAK1hcD9MU5l-ka7Qt_7gSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: در مقابل دشمن سرخم نخواهیم کرد
🔹
من به‌عنوان یک انسان به‌عنوان یک مسئول به هیچ وجه در مقابل هیچ قدرتی سر هم نخواهد کرد و عزت و سربلندی کشورمان را قربانی راحت طلبی و دنیای خودمان نخواهیم کرد.
🔹
کسی که جلودار است باید صادقانه با جامعه‌اش، با مردمش…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/436388" target="_blank">📅 18:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ادعای عربستان دربارهٔ حمله پهپادی از عراق
🔹
وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شدند.
🔹
عربستان گفته حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند.  @Farsna …</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/436387" target="_blank">📅 18:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8I-beKAXwOv42BgmQVYxzxC4e1WxbuovwOlFcgBfKibON0PANrxyV1po-mtJLj60UWFMAkDKAwGC5tQSBx_OC9LNXLxRyU3Nf4B9wGjoeqpb4KzeaCWLAeMmkXah-kJMAlz4GgY9jmVWHEK5xl470fwi2wJ17k6pjyXEQs6T3G-GqMQOWG09SHF7cKPuky-_lY40b_fYNhPGEUcK6o7b8WoIClfGSXU2mDATfAvvQ_nUCJc6-xSCBnQOyp-8DTYEr_jjGoqEataLz1NvN-eK0wUGMwOXsUs067le8dX6fvcOpyIem1EvN72njtynSv3PKZbUTpa0D-vLLs82soCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علنی پرسپولیس سر سهیمه آسیایی
🔹
‼️
شایعات از احتمال لغو ادامه لیگ برتر و معرفی مستقیم نمایندگان ایران به آسیا حکایت دارد. باشگاه پرسپولیس با این اقدام مخالفت کرده و آن را غیرمنصفانه و غیرفوتبالی خوانده است.
🎙
یکی از مسئولان ارشد باشگاه پرسپولیس گفت:
🗣
ما به‌هیچ‌عنوان این وضعیت را قبول نداریم، چرا که هنوز حتی ۷۵ درصد مسابقات هم برگزار نشده و جدول فعلی نمی‌تواند ملاک نهایی برای معرفی نمایندگان ایران باشد.
🗣️
ما هنوز ۸ بازی دیگر پیش رو داریم که فقط دو مسابقه آن مقابل استقلال و تراکتور است و سایر بازی‌ها مقابل تیم‌های پایین جدول برگزار می‌شود. طبیعتاً این شانس را داریم که با کسب نتایج مناسب، جایگاهمان را در جدول تغییر بدهیم و حتی به صدر برسیم.
🗣️
از طرف دیگر تیمی مثل استقلال چند مسابقه سخت با تیم‌های بالای جدول دارد و طبیعی است اگر لیگ ادامه پیدا کند، احتمال لغزش این تیم‌ در امتیازگیری وجود دارد و شرایط جدول قطعاً تغییر خواهد کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/436383" target="_blank">📅 17:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je3Nz3WV3I7bYzpbLOyqnJ8GL9Jl2sJuhSzC_Ql85P4W5lxmHNpGd3Ym2r25_1BvGcz9heddWjuTbnS2z8V0gNE2865ueJHXEWe_5bRu4y27zmUFHoPFVUfg9H86QffO83zD3Jv_6M8qJSOAQe1UspzsfgVovlwRHeN4irCOtKWzeM2iV03sBXpf1LzWvdl3-v1V72-8iXrwJl3NxficyhACUi6pqOcqJLp-XG9C3BZNzdZj-AATWITtiH9KVsxrF2upAk_nKxsNqdLDRCtOWqyerdHfIm1wx0xHsHXgWBfUA73Br243ObsLJ4qqRiwxQ9SvAvAUpKmR4TusAvYS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoXPn-KbtSHCeOAAD5H1hXj2N7uFEUurrnD901aFme8E8HuEjtVvhq4E74eonkkXwxXEKvv5iTrVjaLgoHq5rUc0IfZUPLzPOPlno7zC3EBvIkiNHp9NRo-2LAU8JxDV-jhwALTrUgy1PBxxhv0lPnV-Op8jRKty0vfTBaQ9AUsCVJrF9M034cZcuD1Pus3o_849JYEuynf-l7ErwAmWEi5ElAuqNRFlq_tnJswoxof2BQLvmb1LMrEEkhDIjaV7X6EKzR9TQG3fqC8YYTQyXwmSNJK8rSejtPI2hBJSlySqINGWWqtVbMlMyJmy2R6SQmsM0yF9JBL0U4-lfGGieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEeoRcL-AXnAdwu9y1sossY2mHE3_8fDfpFDIS3-J9Of6TL80z43YnzqcwwECseDCtLVIjstkLi5EXmhbKsRGHTwxD0Ybt2IdtZvJODkxNOgHn0efozPC7cnzOBZh_zkNtSQ6_I2mDe_IaxD72TVeykCYl88LLy1-vjlfA_U64a8aqDrn5Zvkw-djulknnKQ82qj29HoOiX5LBZ1zoXPE3wNlObjhfqfUtgNfkVt_7mxjElyWeB8FziNmhd1vm822xFpoNbt5DBUFQiVGNssZ2lzHMfdwl0iMKchNrHKVEKkcoTzKmEoGCUjv9AVE1LpjLpJJOgSHI3IOCTMyyApXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI8D9YA1C7W3oij-7qr7JyrXlbI-9bAO4FYM9yGqi73Iqh_YN7s8yNolyI7r8WG8FPySYoK2SB0mz9IPZ4rKj6FgJrtm00LzgeOtSMbP2k1QoVJrcPy1CM1oqxmllSKwD45t1H0LQ_RRJErhgcrArdpn5pjv12JGzCqjW_pKb0PclEqefNvWsH99lQevj5ywK0anmzMaxamsgh0QU5wB2HqLtUJbQ5Rv-sR1IBgac1P1Ptt3f5yeP9ag9adN4iDUDw58wx9gRPJLhfXHGAMINxPGufMFZdoFxDUJEByjYf9sZ0KC91NaVrdd8NVxSCVFzoDSlfxazBxWxq0T3nEJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0Zl4-EVSD5W3iKRLFZV74wmxIRzMCfRvvs5hfK1IiVQWErm_g_VEgywXhy2QD32PrE47CZWQz7yaZ0ax1cBo9ertvg0ob9cdDdhFKrDL1BQJ8jXF592OZtXwxEwtIPZzIEwYWTOLzw6oARVStFUDqSLCsbnvSMXl6nN7EzVkzL0o02ZFCt_au02Sx71zk-diavC2NMfzbTH4Lxn7aEuGvlBXK2PbIfvXaqdN4vwHZVkvaAb3wVF6cnZy3x2eZJpRV1x-yNDLF2zhSnoPX7SxW4M_8t7CC0B3J3QG6RcArSZOa8GlFmo3OIcbxUlplM6RaFIvJTdVAM5QymsYpgDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMGjg8WhZoZhdip2NFoKssbtENXOj1yD9SWD_13No-YfxhkUN66v0mIBl6Uc1PN6uY2thOp5tHzWjD04RiOsGAYCoqRagqkVd_Qx4bwPRT8qZyz7PFe4o4DxL0wyNInGphZhnDfBrPgvm3BuZ2DUz7bCknDwwRU7Z_tCc6Lju6PW5fmoTQdd0nDSa-P04tPW3hkz1p9jxzvDQknpoe3Y48RqsN32o6ahxf7T7L4J-chwQFwh-pb9JkLrEVWb0emCVythl82MWNGtZIZ61LryVTZS4VON2d5kPBf-OE78L7DgCumGl8P3fXlzvG3I_dtk0HPK9MxROFePq-90exQUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQYWU6xURfelnc2XYnvyV6ld2JwbKbgrjxLgPEDXehZeT1sSDDUfH6b5TmC87dwHu01dkprUDB9U63PMcYI6oACVKPGZtnD3rV-MA_lkrh2PdZnXnkSTdC72rCQkr0rYgMmDR-qrhkcagRQHVFOqTXYwXNpezOdp7TfMkXUxf6r5v4OqNYVdxejpkH77uHb5YeDs7mBempDgP89d1O-xfEPjUB9Ylt_L12DIti-1bmi0XZaEInOH8gqc1F_QohbRAMtiyCK95nu-AwARhy9oZQH8Nm6Dow3oZIwjiR3UO3NcPO0b1RofyaYiQSCy5cvLQfmoToZBgGle-_dLISeVzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمدن ۶۳ هزار ساله خرم‌آباد در قاب موزه
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/436376" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb138f5f9.mp4?token=I6hvMOORls_pFRM5Gg3NyjiVdaK5-CPSr3rBtm64kS-dYNbHB1EwKqnUGaVoFkOqV1KfhSg1HZyt0nChszDfxPTk6gwobvWBawe7tQuEMiLjivTZ597xdwWHEM357XSbCZ1SDFkCKN16wzfW_D-5SAli9Q90sSLdfxjAVoTXAbS5W1Ph-YbpFwSzvldHNIHhIX_zo3-DoY-3Tn81bYEy-Qf1qlsNkwJymRmgO3BmwK78NesO5OmuUCc4ItGn8qwkwNJmJfB8rxB8h3dPgP4KvIDRT2s6Sl8GP_f3H2DNHM2RbCyrHQh3ba4qVVAvWcKhihrnxshUXMNSRYvqvT-PEkAJ8JPQLjYJrfT8b5uww5DQ5KHYbwkOk_zrDZIlN7e_OWxffu7nxsJItyIeu0z9nk5P5hsZmN7ncyXtpKEreKaQr5J89mI_loGy4bCO8g8rGkz3R08XJe9k_toR9cjm2krKRu498Ckz9gDtiM8RyaXFZMZNPa1DYP3o33yUfxzmoINdGOe9S-3av6bvQsnQTdGHTRNW66js3NHPxMonLGbBWKqQN0sxORuBhl4_OsqgrfWi3USX4zEiKRLR0UhrF9paMNKO_c7OICvkhF_FG52ATJ0rZp-bJqr8OprvAP-QMJuiJG5CTG7oMwnEkDB9Umef3DqQdqUjdjYwHKhmNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb138f5f9.mp4?token=I6hvMOORls_pFRM5Gg3NyjiVdaK5-CPSr3rBtm64kS-dYNbHB1EwKqnUGaVoFkOqV1KfhSg1HZyt0nChszDfxPTk6gwobvWBawe7tQuEMiLjivTZ597xdwWHEM357XSbCZ1SDFkCKN16wzfW_D-5SAli9Q90sSLdfxjAVoTXAbS5W1Ph-YbpFwSzvldHNIHhIX_zo3-DoY-3Tn81bYEy-Qf1qlsNkwJymRmgO3BmwK78NesO5OmuUCc4ItGn8qwkwNJmJfB8rxB8h3dPgP4KvIDRT2s6Sl8GP_f3H2DNHM2RbCyrHQh3ba4qVVAvWcKhihrnxshUXMNSRYvqvT-PEkAJ8JPQLjYJrfT8b5uww5DQ5KHYbwkOk_zrDZIlN7e_OWxffu7nxsJItyIeu0z9nk5P5hsZmN7ncyXtpKEreKaQr5J89mI_loGy4bCO8g8rGkz3R08XJe9k_toR9cjm2krKRu498Ckz9gDtiM8RyaXFZMZNPa1DYP3o33yUfxzmoINdGOe9S-3av6bvQsnQTdGHTRNW66js3NHPxMonLGbBWKqQN0sxORuBhl4_OsqgrfWi3USX4zEiKRLR0UhrF9paMNKO_c7OICvkhF_FG52ATJ0rZp-bJqr8OprvAP-QMJuiJG5CTG7oMwnEkDB9Umef3DqQdqUjdjYwHKhmNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ بیهودۀ ترامپ با ایران به روایت رئیس سابق سیا
@Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/436375" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک کشتی ایرانی دیگر خط محاصرهٔ آمریکا را شکست
🔹
یک نفتکش ایرانی تحت تحریم‌های آمریکا که ۲ هفتهٔ پیش در سواحل هند بود حالا در جزیرهٔ خارگ پهلو گرفته است.
🔹
این نفتکش حامل ال‌پی‌جی بدون اینکه شناسایی شود از خط محاصرهٔ آمریکا گذشته و وارد آب‌های ایران شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/436374" target="_blank">📅 17:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPfluk8emtv_fVsJXjAzIqay9NFXRjMstH7Zkm69x0rD_CkooZ-IonFLKVa80RVmKikamSdBqwmjKyBlFp4eEhW339-aysfWWhxN6V5UdmOLSrn1b4DZWAuT8Wa3RsjdOk5YgX90_VRUzU52vq6TZdULBNNjadibhOeG3_XongVsb5GN321ZTs23W3xsYlGlSeW-0R__FbnjhBRDyk5XOB6ICYawM4pRz7mGIaBTzJRVxVEP364WcWvVvoQaS-RVRwWoDgEIeJoSoIaC5uU4NCiUYY1xTFyxHhPzOh5N_z1J0zKad5too2MVeTbd3fyPpqRaVO1XyF0EQDJl1VZaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانات رهبر شهید انقلاب در مراسم قرائت خطبه عقد
🔸
ازدواج و تشکیل خانواده یک نعمت الهی است و باید شکر آن را به‌جا آورد.
🔸
توصیۀ من به همه عروس‌ها و دامادها این است که با یکدیگر با صمیمیت رفتار کنند.
🔸
محبت، وفاداری و همکاری زن و شوهر شکر نعمت ازدواج است.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/436373" target="_blank">📅 17:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfaqjZYZWvF8qqO2aVvLkdasSbjw3gkrbAUAcPBZR_p-WxHPDmL-qW4GHD1QyF8z0b8UDLhJfbSJKzdnq_pNzthjrm1TytVUlVaFnuX4IZn9yKPVbaxQ-cm6xYpiWdCaQmffJiJXQWlQufGS7tR-drllZOMGdRBuQ8ExsjeX7G86w0OSm8S55mJvL1U7EY3VAsL8GIitk0SpozVuGeBnaJQfoL7jMkz3gGr86V1mahi_qGWopJ3C9CnsGHU1i68sYGe6EC6uOo7XwgrEeNunBX_HciWoPEfLFpQ5xhlHuCiqt2BuS9ULYcYeXvXtwYNe9z5Btb-tfEi5WfVGulo3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حساب رسمی مدیریت آبراههٔ خلیج فارس در شبکهٔ ایکس راه‌اندازی شد
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/436372" target="_blank">📅 16:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری دانشمند فیزیک هسته‌ای: از تسلط رهبر شهید انقلاب به مسائل هسته‌ای خشکم زد!
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/436371" target="_blank">📅 16:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ جنگ رمضان در قم
🔹
سپاه قم: تا ساعت ۱۷:۳۰ امروز عملیات انهدام مهمات جنگ رمضان اجرا می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/436370" target="_blank">📅 16:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436369">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqivJiDts25ROqqX_u3-eMVAvUPUXOvYgHOouOHOyHEJYk8Vkf6J1UvU_swJHurqC2IU2rcofawo17NoiX0bPvz4Cm8o21BOwU8-3WZpMKJybViIjnTNjwBFi8bMf9YwqeWF5WTQPt_17jEbdV2-4GJqGeLqGK107zAtzSOC4Gs0wd_c92MLlVm_TW-UmdvIikcQWm3Gj9GHbPZeZAjeValVEZ1NmQtWff2jvtB_zrW9HK6szd_l-H6cE_4_PATPVGPHI6_WVBANSfSiGuZqawm1bz_X75Tsosv-G4abNL9LTYOC2YzYBlo-K-VlZOW-2LVL-XiDop_ppkKmp2BFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای هفتمین بار از آغاز آتش‌بس با همتای عربستانی گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/436369" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436368">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBEFQN6_lrbY6T6gKh4nzULTxShEfQEDRyVnw03Vfnz50F4tPe_2wFYcm2JSitTQed0Bse_5lbfkJnEcs0Q2VEPK8itlwR5XkQ00r3i-ry6LlXxrfnAzG4MRXJEWM6plfmio5dLwnSjDbh-BaLHep6A2poLdFKla1nOxfrtQjIY0WDNPDxTFf2F-Ox_dxLN3HYH__kKiK1XrFmEQd7rJIymt7edlKpySSqjf5g69w6Ng63K51PkUQbeertkYolAJyusu2LL52AYCsyCuYgsIYoc6eLFcaHjEfVVHE3zw6tHFT_yaKGkr2W1agh_nKjVcji6j2Zk_B2fSzlyMk7VTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نماز را در ۱۰ روز اول ذی‌الحجه یعنی از امشب بخوانید تا در ثواب حاجیان شریک شوید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/436368" target="_blank">📅 16:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436367">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌ ۴۲ نماد بورسی فردا بسته خواهند ماند
🔹
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔹
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/436367" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436364">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
رئیس بورس: بازار سهام با دامنۀ نوسان ۳ درصدی بازگشایی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/436364" target="_blank">📅 16:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436363">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjXQcT6FuiXU0UXweDSpWYjqxUiSZlPSD1CBogh_pZyfeVNcT-mFk-jhUJf8lrhVgX04nuSDLxcogCcoEZDA5awKajFVaQTo1LskoJ8nC6qTqU1BM64WvoqbrTjNDMz4c_QBHw1EiXc-d2sq5gOV2P5DwJ16eKi6yHLoj6z3sHFDOoJmaKLHvhYUHMWFSHz05TmGggRyVbel4yjFwFUfX53cxqe6Mtd_K3EVJo8Jztx7uBEjv-YxBP-4xRohWivDg-JHxbMQS0_F3ur2WUjX6y5VrpkYEKu0m-NrBCXMcQ9lyUcdu3eWDPhbIQR65ti2i7d_xxTnlzJd9oYTCtegcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان هنوز به ۱۱۵ زائر ایرانی روادید نداده است
🔹
یک هفته دیگر مناسک حج آغاز می‌شود اما رئیس سازمان حج می‌گوید: هنوز ۱۱۵ نفر از زائران حج کشورمان اعزام نشده‌اند.
🔹
باوجود گذشت ۲ روز از پایان عملیات انتقال زائران، سازمان حج می‌گوید «طرف سعودی قول مساعد داده است، اما تا صدور روادید باید صبر کرد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/436363" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مدیری که می‌ترسد نباید مدیریت کند
🔹
کسانی که تنها در زمان امن و امان حضور دارند، بود و نبودشان دیگر فرقی نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/436362" target="_blank">📅 16:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436361">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
گوشه‌هایی از زندگی شهید علی لاریجانی
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/436361" target="_blank">📅 16:02 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
