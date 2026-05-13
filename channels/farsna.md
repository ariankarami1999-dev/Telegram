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
<img src="https://cdn4.telesco.pe/file/EU0qUAghnO4Nz-5Bwf5oc6xFADnAG4o0k5BqW9-n-DUKMU7oYf8y_rbC0uH7okxaUCkKGgfbkOF5h6WBXCcanQRUXstxcc9OXFyxer2KegUlMcRcvYGUoH43KjNp8a5kY8xQ1ULpvP0m2TbWHA7cRcIRoWbS4rXF4ymE-5odQHLKz96J06n6lGb3G2uyvbOE4QX7MYppOsFCA-IS0_gfEqv6tvHA8cUaSAwQKbnY9BC8LgX_n1Omw2YZeTtTb9e7ZrC2gl2SUvCj88cNj6V136eXdgm8OEql3ZItgmwFU081C-mt7PNDQbB-oQ50_J59SCB4qopMYxvBFXMoefjKJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 22:22:59</div>
<hr>

<div class="tg-post" id="msg-435449">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چی این چمدون رو سنگین کرده؟
@Farsna</div>
<div class="tg-footer">👁️ 218 · <a href="https://t.me/farsna/435449" target="_blank">📅 22:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9r0S-bDq1w29IHKK5Hcb-SsaLf7DBos42-h0CZqGelhR-IP3ow8KiG2cdSsxr4VV41n-GRUidzXxkKepexzwqFbBJ1wvXcfhxdnDxaQGTi2NKf8x2o1uyZgHqe7WkEfUYy2A0Gj-z0cyJvIFeQBT5VyqxzLxclBNu8cWKGazUqoiVI3eQ7dGuOXN8qY12FKfbaHm80vWHxyO-aIrA7-91oEPW5m5IrIHiT2YcUud_eof58398VRFXAweABHN12IDEl3RA8YO6WP08m4IxrsNC6V3FvR9FRty_rIZDfaVU-wmXBgc01wyME7g_7qgaf8YcxLxPGGqjmXMczXsr3tmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عباسی، قاتل شهید سرهنگ دهقانی که در اغتشاشات ۱۷ دی ماه با ضربات متعدد سلاح سرد به شهادت رسید، قصاص شد.
@Farsna</div>
<div class="tg-footer">👁️ 253 · <a href="https://t.me/farsna/435448" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
۷۴ شب همدلی و عشق به ایران در خیابان‌های گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/farsna/435447" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435446">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USy_SOHMr0bohkhah-8Qv1y35OGAwnX4RnJl5EbnFXVobLnMRQYLiy8QBk1H4krZ8owHCy5c22-OoqRiIkM7P5B_yRMc7uGDnRACucQ7LfSk7stwK-ay7IO2H6YyiB638UkB7hGoaaE7LqZ8OCN3zrJ4BK0vejiC0dJXHAF8cMYrDo_37axQmfhqN_arx_No_DjGm3dzQ4YjNC9ajiHjZ34PMPJre9yl5mOsSt9VkMbIn8cnUMX-GHME5_v2bruFlkEvgXAJK0AePorrAv_PHnuVAI0PrYvAfsPjoCrgD-4XB9rgviZdZTJd_6Y-Wgjl8sQSqbkfyjMUNqHZo7zFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر شهید دهقانی: منتظر مجازات قاتلان فرزندم هستم
🔹
جلسه نخست رسیدگی به پرونده متهمان شهادت سرهنگ شاهین دهقانی‌نیا در شهرستان ملارد برگزار شد.
🔸
سرهنگ دهقانی‌نیا ۱۷ دی در شهرستان ملارد و درحالی‌که هیچ سلاحی همراه نداشت هدف حمله اغتشاشگران تروریست قرار گرفت…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/farsna/435446" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شکوهمند امشب بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/farsna/435445" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVV3WWeLcemOR6oJVbQWeSu1b2TGWgRkgVL3ljlNOyhqFBYWzZhwq1YQHPGwJ-upWCSMLN6V1Obl3m1V7gFIT50GLJVT7B24miEW9fpWJyJstDs1e7uw-OWnqrhucVZh_SaCqqTzF88JwuzjQ8rAMGPxejUDCM7thKC9xsUegmp1vAGM6zhGhSt2kw47yxyDbIoUmiKqji70ygAqDE60mSs4DKkPaUxkzvkmKO4OVy-ewWC93eDaI4T2i5YrqVin1XxIhOuJu6Rk1NdEY9fvkwAicDzEWEG_Sy7O-Ym5OD0W-jxm70VJBoYjgHiOMDsSSGGHeFRuONwtZno1m5MFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش‌چهره، اقتصاددان: در کشور و جامعه در قبال جنگ جدید دشمن آرایش جنگی ایجاد نشده است
🔹
درک درستی از تهدیدات وجود ندارد و بعضا شاهد ساده‌انگاری هستیم.
🔹
نابرابری میان تهدیدها و مدیریت تهدیدات در کشور وجود دارد.
🔹
باید قرارگاه جنگ اقتصادی با افراد امین، علیم و دلسوز تشکیل شود.
🔹
در درجهٔ نخست، نیازمند اقدامات آنی و کوتاه‌مدت برای کم‌اثرسازی برنامهٔ تورمی دشمن هستیم.
🔹
مقابله با لیدرهای تورم، ضرورتی اجتناب‌ناپذیر است.
🔹
در تاریخ جنگ‌های جهان، دولت‌های موفق در شرایط جنگی بیشترین سطح  مداخلات را در بازارها داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/435444" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHnwPLJU9eT_FEpksX6ymigD1Wy4jo7czfL4pWPGUeBxopVCDcpUqHHZJSySqyabgGCoIHIt-hixTgRYrDRxxvU4X1jq2LyOBVPxFgJxf9lC62sUjX4G-9OZyuBtiJU-a8FjujIZUahe_oehw5fkNLsWLpGZIO_VpHouuRho1hWVjz7-zVnP2wFzXBCE10J9IAUzt1XUgEHAzCGab03SyryKPoQUfEL41TivceR-ipuqoy9afyX1wBKiH1Ew6ZGk4qUQzjpmKenK6BTOosBhn1sCLfIMuuWbJOvSgTBmPvf_ta9rUQCSKlATbaPN2NvKKnpXESO7gJ3nS1m_pwV-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردهای تهران با شروط ۵گانه ایران برای پایان جنگ بروز شد
🔹
شروط ایران شامل رفع تمامی تحریم‌ها، پرداخت غرامت جنگ توسط دشمن، تثبیت حکمرانی ایران بر تنگه هرمز، آزادسازی پول‌های بلوکه شده و پایان جنگ در تمام جبهه‌ها اعلام شده است‌.
@Farsna</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/435443" target="_blank">📅 22:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435442">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkzNv1ZV7SryiF4QgKQ0Z4jWgfVoUejsyleu7frrcga-eOnpP77a_WJGkqQ7KntWqm8F0dfGQ2v1FGxIADOsY27b7dAjIFEJ3u6AcqkQTV0Le9gqTGA-GAiZKt0BIg1IODBTOYtA4-EyaG6UpxbDLG_RHPpOdArrs_iH0h9qzPn3yTNGpufhQ19kRb_evL8yt9lhkd9I2sjjKWUo1vCtHKMXY7Bu2qBPsdWXCB8jtCiJbpirMkA_vdV7looJN6a4e6Ue5yeXVvji9smo5d-XsQe0GH3iLpMLlxd8cLgfuF6f2gXbqAcCX4LyKacTEw1UPg1xurpzy7bZuNQT26Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/435442" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/farsna/435441" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435440">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مارکو روبیو: واشنگتن پیش‌نویس قطعنامه‌ای را در شورای امنیت برای دفاع از آزادی ناوبری در تنگه هرمز پیشنهاد خواهد داد
🔹
پیش‌نویس قطعنامه در شورای امنیت با همکاری عربستان سعودی، قطر، امارات متحده عربی، کویت و بحرین تهیه شده است.
🔹
پیش‌نویس قطعنامه خواستار توقف…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/farsna/435440" target="_blank">📅 22:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد  @Farsna</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/farsna/435439" target="_blank">📅 21:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435438">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/435438" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">«پرواز همای» خوانندهٔ رسمی ترانه‌های تیم ملی فوتبال در جام جهانی ۲۰۲۶ شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/435438" target="_blank">📅 21:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/435436" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IingY6SMc2ZtUlavvxS3CluvVY5FERA2z72EdspZ3KSxAu6T6r0Tj3uRsiZq18N7OCYU1iwrddX9dmoghxtmkFPAr7DZ67NrvbZLFvuG7SpFzYVCIfj-P4YWdsGWJki4011UHM8JlfQLBqkwlnVmfcbBWUPXA8hlShPaazJ4RHbluo79LoKPOQ1npoZlo0axuJ6plspypIRwZtfCJKH3MCD3YjrMk4KVTRIcvEJkQMO7AYAAiCSaoGzf60pOcY_DFW2y43JW9atiS0VLqoCtj-8dZNmrKkElj-tgMdKSyKelInlL6l_0l8HegawqCU9leLYZYatG7WuRRyYWWbIZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقی‌ها به کنسولگری کویت در بصره حمله کردند
🔹
به‌تازگی از خاک کویت به سمت عراق موشک شلیک شده و عراقی‌ها به‌شدت از این موضوع عصبانی هستند. @Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/435434" target="_blank">📅 21:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0ZMK1mwRVEae3K_3cGKO86Pmje5NNf7pPe4ssr-IJFWTDuotpHwwRTSH2MSKdSx6RR3r2ErR9Nab_kCuTHkoPDLAegJXk_4RS8AWAZOJWSc_3ECn8-WW3zQ5SshIBqyAcE2elhERuvsWt8fHIoVu3X3fmIRGptpTrWxOTaDY_cjAIqzJffeRaLhgqXOLj-0l55-NePQud1Oe7pe-M_q2B9kgjFk_DLYYiwABZknJaHzYfFbIjY_oP44K1LJtSefZKXAJufxQlz4j5jXn0VdQz9nVBwLXykVx6EW5Bg6x5EMvJxFDaeCUG5d6hEwV4mb8JtyeCUErSMvdnE-RvSR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awY9Xq7eaXVdM1BcLpiTKvDTTZRLRH_sQFC3cTIrApHHJWMwrgzYKdwjP3Uv6mcJf-ZlsJUOFZay5BnQxnd0hsUdnexB9Wp-wbaBBeMbpPhkM_hhDFfx2I4v5kDNG-uPfMlrByMq5_jN9ZD-P8XCNm3goqS4acq2kXqect0F10Z3GZ8jNCmq21ci_ZzPzN0ltoGtrAyeugpop878CjXr8Q5JkfWSylbeQI_8NArynqh-vHHe84FYb7ew8MyU8wbdevOIpwftgjHqRVwIAKuwq-66zSvsVtE2SrFHsAfJg3AJ7_1pSY7f88NBlSYViSnQ6vXJmfnYcoAlyIUhLl1nUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcSdMQsktH_dJUCKXYN4x3iOt9buipS4iw9wrOQjGAZi9m-FV0lV_q_Jyq9ZC2-16GjwarrXkywpIPGl7N5yyvzmDun0D6yRCMKI9PEZ7JwsEW8zz3cJBHaEkgUX0aoDGg69yIqkyf0mJN09fiReF-wUvwRcj4dGwt9HQMglK58eDlUmVnaboO7GlSv3JvHD_b6F4gMWUsowSbhci2lQ7It9JfRMrX82mySwxOtbZPIoIYhHnpKAz81HqzHPqKshI1Hu-mIxE56fkJ8jVKp1D8p8_9GxxufBdezzjzIbwPH6tqgLWGQuAbXO-eiwqt8UBgfBgmX-8X2fKNsEvcd3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v39GHaQyDcf-Ar-zKD1Xa0b6oAZ-o_hdvTn4JTwaqGCTP3ch21Rb11PRSCa0bx55Lr-FH1l0FzgLQs0jRtTxewCCwz5G3LMYtZ2jiaB-47mwrN2O8myQ0oylYzYgAaDYQ_ia4UqEBp5F9y81RTQo4bjTHfaKaz6GWwMJyoH2AtBrs3448OeaXcfp-juf_u59vp2KtNHY2SL48kAdzgPitwHmWmdWw-Qq1V3phobewjgpNZLFmNv5N4dXT6fjkFIooLnx8qIsEK24dpxIUrNzweOt1A3jHcvuuV0gu9Dg4Kf0AtSJ-WIrhS1RaUIauShiopgRH3ZET1FgX3wTLsxeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Jpl3SP3QDX7f0p_D3UbGBIJASfOWFfAKjhYSCUQE4ErFjRVTyJJmFxyHJ8E3tQVfjMvP1RHCYNAESn8j1DP2owUDHqTSeYul4Hm9jhJ3nW_ca842t7tjyjVl6Id1XyHw-nrx_TIxihsG4QIP_9CgtVt0tKIWYwSDO6wLUjkU_7_-5iQA9PPAyDM7UmZUBoQNEovZhw0awITdUpnR0QHEHMd2kXpyjT9838xLRsDCtUxn9u_ugQjAnWS1UFeYTTtf5rjsUJyBtnPCQOSbzhYGyTkCfNAb3FXV3z2E5NGqU_x0vyKisfeGVtX3lAIRlvp4B7IGAXT3taSNSMdCPxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGrOcPx0TQC8_emWEyaSGond4BcoRsiyodIIgq2iM6zaXvwsUsIoPxCNQykzBHAxwtyma2o5zYDk1BovLv84Dk8HH_Lf9D691Om-bnZoOrwgrHKviC8QPK5mOkTIcKvwzCBeJwe7wP2HmJo8F1hFljvVhosqrCKQHrS8eKscc5ZL-0bFYiJtvOPhPPT6YIBOQ0B-h17A-eMJr9i8ewlYE-HbNTc3IaugnAHX2feGRFY2muUIEwrsJLqGq0iwH3sJf0x6Jg1iFqlr_UaPKLRx2qj2zQg2F5_j-qPy9WAWwisPsj4h080rKVYepgtkYTkNT1GXRjr5D6TH8tKAoU7QFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jezo6aEYZAp5AYIpPIbyszF3xb_44QWePSYDKC-53O7iAZQl8or4iUtg1i8QXEV_Ntt5Wg1Qk-7LKF7-BG8I9Dky3spe1L3QzcmQMOfo241Snc1H-3r_bwX2f64LVNHlWWqBavHeayDA5Sn-ihYNu1aQ_f5YhvMUCyXQPX6aWZVM3-pLs-xLIwXpVcJP_fJlQgGVE2Jpgh4orKckKCKCg4BGSxLTALF5KR0IMZk9QErjAqk4RlB3HHlz84_3e3Kci702S_Q5y2JIlxPaZEwCNqg2T2NYaa_KDfRuhHc50uC_ZbwnPRCzBoN-C7pNcpAAFicaf8M-nZ6PYAeIQ1lErg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهلمین روز شهادت امیر سپهبد شهید سیدعبدالرحیم موسوی در آستان شاهچراغ(ع)
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/435427" target="_blank">📅 21:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی فوتبال از میدان انقلاب به جام جهانی بدرقه می‌شود
🔹
معاون امنیتی استانداری تهران: در حمایت از تیم ملی فوتبال کشورمان برای حضور در بازی‌های جام جهانی، آیین بدرقه چهارشنبه‌شب ۲۳ اردیبهشت همزمان با اجتماع ملت غیور ایران در میدان انقلاب اسلامی برگزار خواهد…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/435426" target="_blank">📅 21:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjryeLcJmlsC8CxUuNEgK6VTm8UmXA_KqRW6fjSws_9746Fv_AG9VSpi1t4Vh_tcq8wL0g2DyuZO-I4zwA_g2_ffT3N9sRHmht511aaWecY5vHDU2LQBf1Qw1SUX2Gvm9wh7XQDC8ZjDGrhfAdtojW34PxlSuIPFq56nnhAGl6uusvyJEaV1WC-ARCy-IXhdY5i1v2zh5sdor-xaHiMGY1CUCu5MOzJ3wgFpo-Uf3opm51Y4jzytYZ-LU5AVwSW_9oaj6d5PrkD-EwQSdFt-cxtD9JG_nme-o-JCLm4xHMCnbll4xzWLbXqWbu54Q0HeQos6Zi5KzWZ5EfZVdz2u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیق روابط ایران و چین در سایه بحران‌ها
🔹
روابط ایران و چین در بحران‌های متعدد غرب‌ساخته سال‌های اخیر از جنگ اقتصادی و نیابتی تا تقابل مستقیم، همواره تعمیق شده و کارشناسان چشم‌انداز آن را مثبت ارزیابی می‌کنند.
🔸
«به چین اعتماد داریم»؛ این اظهارنظر وزیر امور خارجه ایران در سفر هفته پیش به پکن، پس از دیدار با همتای چینی است. سید عباس عراقچی در این دیدار ابراز امیدواری کرد که چین بر نقش فعال خود در پیشبرد صلح و پایان دادن به درگیری‌ها ادامه دهد و از شکل‌گیری چارچوبی جدید برای دوران پس از جنگ در منطقه حمایت کند.
🔸
در مقابل، وزیر خارجه چین ضمن نامشروع خواندن جنگ آمریکا و رژیم صهیونیستی علیه ایران، برقراری آتش‌بس کامل را امری ضروری و اجتناب‌ناپذیر خواند و بر تماس‌های مستقیم بین دو کشور در مقطع حساس کنونی تأکید کرد. به گفته وانگ یی، منطقه در حال عبور از یک پیچ سرنوشت‌ساز است و هماهنگی تهران و پکن می‌تواند نقشی تعیین‌کننده ایفا کند.
🔹
گزارش کامل در این‌باره را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/435425" target="_blank">📅 21:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی شرکت‌ها دوباره فروش اجباری کالاها را راه انداخته‌اند
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/435424" target="_blank">📅 21:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام این جاسوس موساد اعدام بود
@Farsna</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/435423" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر ورزش شمارهٔ ۱۲ تیم ملی فوتبال را به پزشکیان اهدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/435422" target="_blank">📅 21:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Mdyvmjq5RzzuYocUH_Zu-X3bvlxj6_KDm2h_OU8WnJ_QXpa1rgHXtvDkjAov9XpTMpflSsyd8f4ToKhmPIkgxv5QeYF5qtjSwTaQmeTEUTqnes4KTqf3DrDyEL9YDIYO6M42Z5hHiGhDl4f-G5iER6K-PpLsj1JFgLmGCcPC1vsf44Cgs-yep1CH_CQdrT9HgnIoDaoFg_tssnZSTGS0yQrRlMQxpwxCUJy74C22tO_FPNY4v2hvk6tZ9NbFcUpTk7rJtRvnPaBpOcPn9eey8L172Nu67-EF7I_rX2oSNmID8UxW2szdcKrbZEafzaMs-sjXR0VQq5zi7zJiYEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای احتمال مرگ یا کشته‌شدنش نامه نوشته است
🔹
درحالی‌که ترامپ، در بحبوحهٔ تهدیدات امنیتی فزاینده سفر دیپلماتیک خود به چین را آغاز کرده است، افشای وجود یک نامهٔ محرمانه در کاخ سفید توجه رسانه‌ها را به خود جلب کرد.
🔹
سباستین گورکا، از مقامات ارشد ضدتروریسم کاخ سفید، فاش کرد که ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه‌داشته می‌شود تا در صورت مرگ یا ترور احتمالی او، استفاده شود.
🔹
این افشاگری در زمانی صورت می‌گیرد که ترامپ در آستانهٔ ۸۰ سالگی قرار دارد و موضوع سن و سلامت جسمانی او به یکی از مباحث داغ سیاسی تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/435413" target="_blank">📅 20:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435411">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkiagilIhCnq6FR2jc5FgfySS9TuCYj01Fj0_-it48afqraF4RfuxMVTnv1x7bemqX--z69eiN3sTpDZhR749UIcSqSb3y4-NzmU6yU4z2mygTwc_QuUvAmjUuAYcJMbjgT-NrGOw1rxaueOLajPvu3xowgd0RqcAjzXJEa_t6hZ862ZFbvTdPhuES0-Me5O7hD632aY6HcKB9sRikpKomOuROBRpCQnWYiWX61UQvsJ00eQns-jmpvKCnYoTZAD32xvyM_V9Dly18Ct-mQbb-uWbUL90j9PaEE6qSS4RjhgbsFYHhW4bOIRzeoYK19Q5GpJiTWlbwtrz15oHsxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: اسرائیل علاوه بر گنبد آهنین، پدافندهای دیگری هم به امارات ارسال کرده است
🔹
فایننشال‌تایمز نوشت: «اسرائیل سامانه‌های تسلیحاتی دفاعی از جمله یک لیزر پیشرفته را به امارات ارسال کرده است تا به پادشاهی امارات در برابر هجوم سهمگین موشک‌ها و پهپادهای…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/435411" target="_blank">📅 20:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435410">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ea55cf4.mp4?token=CTAfR8xRENrHk-6zIIgAMKRwQXt5BdkTHIFeCqKiNHu5KEUDryB11Ci1dZ2_Ey54XykqfmucfAn0APS1XLyVjD0hCQocRenLWwykXptyshFxAHK1XgxlJsjXWrhwQm0ZyEwVFMWvYII8jN_Z8f2GGsRFAnQqf9xmqtvbLRTtIEtVZPf75tfk8lNURQCOmDRzAyF6FS981cCwLvGy11hUpVN0lQrbdqTtsVqhdB6OiZa5kHxacqDlt9mh1ans_mRVFGgJDSNylrKZYlXnirpR6U0QgXPgA1wgaDjTyxht1mDKJhAIhbEmWY4_xPnlyfnsssKmykYQ7XInILuegd_qmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ea55cf4.mp4?token=CTAfR8xRENrHk-6zIIgAMKRwQXt5BdkTHIFeCqKiNHu5KEUDryB11Ci1dZ2_Ey54XykqfmucfAn0APS1XLyVjD0hCQocRenLWwykXptyshFxAHK1XgxlJsjXWrhwQm0ZyEwVFMWvYII8jN_Z8f2GGsRFAnQqf9xmqtvbLRTtIEtVZPf75tfk8lNURQCOmDRzAyF6FS981cCwLvGy11hUpVN0lQrbdqTtsVqhdB6OiZa5kHxacqDlt9mh1ans_mRVFGgJDSNylrKZYlXnirpR6U0QgXPgA1wgaDjTyxht1mDKJhAIhbEmWY4_xPnlyfnsssKmykYQ7XInILuegd_qmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: تیم ملی فوتبال ایرانِ در حال جنگ است و باید این وقار را حفظ کرد
🔹
صحبت‌های امروز رئیس‌جمهور به دل همه بچه‌ها نشست.
@Sportfars</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/435410" target="_blank">📅 20:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ4WYeOvJzTh2vdLO-a0Hg5sRXZN7R1X7lUpDZiMGExS86Anixj3JSQ_6wK94c99vYmFPySEEtdACq-4WmVkAifxjP_SJVgUZ6D-dpt3tYArdyj1KWcrCuvSlc5a71D1PW25xt9xZQ_LyQZ4_z7Lxk8SYalttB14lli8dmJwM-YaV3bYRhl553_3xCwr2G91vCUOl_fZruTCJ-F1qQCwr1mNamLhc-cxDBJIuoydqCu3mVvgLPNkqyzpWuXki9_A8ooUDwcKrD8b-fQfxQ7KNVbljQ-hvzyzUlbGBBLD5t2FRilOKL0vEBOYddFFFJ4i1JOvOKP0hC9fuSMdNf32Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام سردار سید مجید موسوی در بدرقه تیم ملی فوتبال ایران به جام جهانی
@Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/435408" target="_blank">📅 20:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مجلس سنا در توقف ماشین جنگی آمریکا علیه ایران ناکام ماند
🔹
مجلس سنای آمریکا برای ششمین‌بار قطعنامه‌ای که خواستار توقف جنگ علیه ایران است را ناکام گذاشت.
🔹
این قطعنامه اختیارات جنگی که قصد داشت درگیری را تا زمان تأیید اقدامات نظامی بیشتر توسط کنگره محدود کند،…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/435407" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc555bbe09.mp4?token=WS5dzyqW5nRayjUFCs9e8jVoYm30ZPTisAigPqHwq9e7zhoJuy5qNGfO16gzbFx8tGlqF7lnzDV8igLkraGDZWnVHnWoEws9G-PLxme5bs6tcDp27uq5tMuuGuYxGMvmOjn7s0h0ne30CSYTbqJSn5l4z__vf9fsgx2MftzhDgSWJwRwY3TWqxPLV3KOWreRwOl0XhyaNRaQ1lqDWranbGLttu8LsqWdBRNu8EPjy09yNcljAteCuOpk4GG6hOekiNdUa-wnCX7bdtNcOYGmoj-IwsMgS9XJi-_sRmgJJDmZfIxUdIOJt7Fwe6VFtgwhgk7ljnqPy184h6yvwZ6rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc555bbe09.mp4?token=WS5dzyqW5nRayjUFCs9e8jVoYm30ZPTisAigPqHwq9e7zhoJuy5qNGfO16gzbFx8tGlqF7lnzDV8igLkraGDZWnVHnWoEws9G-PLxme5bs6tcDp27uq5tMuuGuYxGMvmOjn7s0h0ne30CSYTbqJSn5l4z__vf9fsgx2MftzhDgSWJwRwY3TWqxPLV3KOWreRwOl0XhyaNRaQ1lqDWranbGLttu8LsqWdBRNu8EPjy09yNcljAteCuOpk4GG6hOekiNdUa-wnCX7bdtNcOYGmoj-IwsMgS9XJi-_sRmgJJDmZfIxUdIOJt7Fwe6VFtgwhgk7ljnqPy184h6yvwZ6rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت موشک حزب‌الله به محل حضور سربازان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/435406" target="_blank">📅 20:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p573izjdRFOzhClmXQiYsv-0DGw4MYG-Xljm5Oph1cbXlMlXzpxvbTX41YOBx0NnftddZUlFNrdvm_W7j5Fb1sHs_eqsRW17J5V8QAo6XcA5t7n1s6wU9HN8-uHjVuP-TRAwzUFzTSCSHEPuMLrbp3lvY2L-0p0TBJ1JDILlgWiKzhV3obw25io5CU6TkxEi9lUWu5hrdi6s4ERT2pzPNGvFC5ZkTGZUzst3L5UWG69POdrMAaVRl4nlgv2Se5WlmsJqCNGg01q5Nk252a9Ox7e7kD4xn4m5IVux_Sy7e0wup61RJxdWf2KK_M5hGkfBnO_afSKHdCNP5yTRbVCVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزارت خارجه ادعای کویت دربارۀ ۴ شهروند ایرانی را رد کرد
🔹
وزارت امورخارجه: اقدام ناشایست دولت کویت در بازداشت ۴ مامور ایرانی که براساس اختلال در ناوبری وارد آب‌های سرزمینی کویت شده بودند را محکوم می‌کنیم.
🔹
اتباع ایرانی بازداشت‌شده باید مطابق قوانین بین‌المللی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/435405" target="_blank">📅 20:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی  عکس: زینب حمزه لویی @Farsna</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/435403" target="_blank">📅 20:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435402">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
امتحانات حضوری دبستان‌های استان تهران لغو شد
🔹
مدیرکل آموزش‌وپرورش شهرستان‌های تهران: ارزشیابی نهایی حضوری برای دانش‌آموزان دبستانی منتفی است و نمرۀ نهایی براساس عملکرد مستمر کلاسی توسط معلم و تأیید مدیر مدرسه اعلام می‌‎شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/435402" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435401">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن تکلیف فرشته‌های کوار فارس در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/435401" target="_blank">📅 19:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435400">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حزب‌الله: سربازان صهیونیست‌ را در کمین گرفتار کردیم
🔹
رزمندگان مقاومت موفق شدند با استفاده از تسلیحات مناسب، خودروی زرهی دشمن را به‌صورت مستقیم مورد اصابت قرار دهند و آن را منهدم کنند.
🔹
پس از انهدام خودروی پیش‌رو، یک لودر نظامی که درحال بازگشایی مسیر بود، هدف قرار گرفت که منجر به توقف کامل تحرکات دشمن در این محور شد.
🔹
درپی این درگیری، نیروی هوایی دشمن تلاش کرد با اعزام بالگردهای امدادی و پهپادهای مسلح، مجروحان خود را تخلیه و از عقب‌نشینی نیروهای تحت محاصره پشتیبانی کند، اما با آتش پدافندی مقاومت مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/435400" target="_blank">📅 19:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در مخازن نفت شهر «مرسین» ترکیه
🔹
این آتش‌سوزی تاکنون یک کشته داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/435399" target="_blank">📅 19:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی برای شرکت در نشست وزرای خارجهٔ کشورهای بریکس راهی هند شد.  @Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/435398" target="_blank">📅 19:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
آشنا: سوییس که به ظاهر آرام‌ترین کشور جهان است، قوی‌ترین پناهگاه‌های اتمی را دارد
🔹
ما بعد از جنگ ۸ساله نباید پناهگاه‌ها را از دست می‌دادیم و باید آن‌ها را توسعه می‌دادیم. @Farsna</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/435397" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435390">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVSR9xcokH8XtIHWVu3ROWG6J7Er1h0x2yRfhYtTinz5_R31j4qaEo6SUWsRuydXevkYG21rQH75faNGoEoxHcWB4qs41Nc0jlFSMPm0fqSNsK4CjtsNEZuGWE-7ORUplF5YPE6ng7quA7EvkJGJ3842Ln3umbZose_tr0UVxhlcGjSi6HAA9LmGYlZ7Q86tShyN9k8hArlJZNNWDNlEnKuRaf4GUfr4JzbkudWQ_Xv9s8cnPkJCvNFNqFyqJ-KDADsq0QigM8hDrGtyxh08z5NIfX3R3ECvrWH8DMht0mfryD5x9YSJFp4LjZaSOmPxjkSn101rYgdaWtoCLODLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzF2_cPGIC79LcehKDQrvaugF-urgy5oJ9Fr3w6J1i0826GOvEV6mV-ITpW6WG44-uYWcSSU7aox0IK8cG5ItVs_iqNhkxY0sNrbRwaXofuBsbjz0jAeu0-E9fXn69_kM2HYD2aCH8tUvwQ2pY3RE_HI69UR35TTE4RRcIvokr0fQOtOqZBgfgn4FXkQMks8sVdnVM0ZZM0uu4_R9kWtRDos0RZSs5g00K5CRHfdt3oiFeXXvJlnzr95t9XXCsrLX_g_-YSHuwG2tHfAS-l6PKHF5arqAmsQN0h24liUqZusCkoOlA-MDnqCiv9MYoy6fVNiT500Q1l8GGLAWCuZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4fDYPvWd52bJE3NdVEqWz1ZC5dwgZZJCJ0T6_oJ8pa-NfyXj80JrEptO7F2QHPX9IGSE2G_rANf1HyIiRQshEjqzX5Dn8xIbodxvyFa60HhEviZz7sQqaM2_ewu1wwgNSpUtfp8f1I3mdGFUbii5Cn9hPrLED8RBJafZq8yNYvHcN0hnMjBYMqE12A5FMtCDr5qkiyrFzeZDO9zgV8a6jzJSXFdvJT81lPct7YVciXy9ZgbmKtN72U0Z_PoDUD0Qh9DPQ4psmjlIMFRQ3VLZ2FiJXP06EtSeuz4npMfNLlBBKJ0eL6UEXUL4fdJGFfCY7vIh3IFBbN35zmRl0236w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDtl-maz2WOXxj5yFLIhN2OwwVyQZlznR1E8T-Ol_IZVgEbw72VA2o_XpmWL7hcTtedlkXrIRzJ1roWZnD_qUrIlJWmPotytMDwPEIdDieU961_B1lHpmSpYeq1vOo6QaSDgKLrC6qBxNEpoTlL_cO0HRmT83QXrXEMkI5cybicKzFFdyZ5KQIhFEo9T62qhV7uG85RqRT3udzxppEIffwcGOV0TeC07I1KOBY_7Gp5f6Hveb72_GQBL-rlThX50FJfwk5qViIEgCSKSiixSzTLBmf0T2NcwvzTwgxAAo9zWrZAWrmAwkMgTDIx09AvKBoCNIUqlG14iJBooWhzqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOjx-NW5S6aoZvW5htelhk4edIKNWZA32Ilj2IJhyR4iKPmaTanFeBj7WXSuOQFSfUz9lEBs4tOOwCWdB1JSGaSOyMNUxoPXKrMnBWTeqftPOLFJkUQgfxaym2Ak7AbVOLnmEdXPACa3FDYsS83asPJiM_H48rlR6wchmmdusKskNmfA1DJrx_qcuxJ_taen5pJUONr0zfaQTKekbXK3n9Qiy_Ya1xxgle_kLE0u9s9ACfyLr64TtxzpfOLnsen1mBaTkyQdk_xJamxZ18cXkRjAMKjTxcosKP9qMpUSjOHvUx3rHmf6upYyfH58zWht3LdGEPf2_wQ5a1izF5yKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVjfAtBMajmHvh0zyMMV2Yl7DePJ-vi5ndo_yXibJXEio1Oz73HcSsDZbMa-A3F2j0DOTzz5jMMNRhMES9Y9PELIgefCU1Cpgq8ZxAa3Nnsf1kViguIR8b0jrU3-w7cUz5Rv46qPRyEp_hQ-9jOR0XH3hEZolTvl7Qfvf_6K8ho3vt1v-pJvgp354m2TDLXr_A9P08pqbC1KVdykQPCpEjfC5tS2Jz4fEOVMY2rhGbtEznZDiswbB4569D414SvbDYfgI3n3wwRn2BAlky1-u0__o3SibGV5G3VQiwFV3TM33n51aLBvd0XZ2YSgPtRn-lu7MmiWJHwUMElMWOX-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUw4FU6iVQmwQBEBEEnT9O62wCwgi8fYz2n8H5Y6E0JsSmcb_gsGrzd029_EVyLY8Pqliqu6ch6IQv2AwxJ-y0Er4fb5WpcX247C8JDPIoAkdSssX2MFndZLwKg8uDFcbfpK1tmSVVeOE8OSS0ANhx-9yX1yaXx8kQrxgcQiKL_sRT8-Nd90Grb2zJfn5DbPKZSLn1XL_ndxxXQ8RiwNcGk7saIUxUa-ibf2rv6uFPAzSLYpFur7-1RK-mZ42bSR7p3V-1_5dIR2ocQMVvlBXDLHp5hUVw-2c2szjjGgI4TIli6ccmJPfS4fC4iSZeHNIwXA81zJJ5DuLhEwaEzFNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/435390" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435389">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwN5xsPt-OKyO0mfx5QldbtS0wI7581ODZuQVfaXpagFX9GcBAR3RXo2zPUH_yaDXddSwGM1NXeWEqtzd9hKODWkA4pD0iDYUG5Dsc9uysoGw3VaMmzpWD-F3wDhZL8-5gsevluOHiPDWfxzM1vTZilNTt8-h40BKrCR3tki9417iRg8kP6bn0dIvR4oEt2quIA5UMG2xlGEfk4Qf3p9A5qy5yOB2gvUBjuWKEPYsY1bA-1dOaB-Wf6DJ5wNnDfepokqmySgpoHQSTH-rQ88BD8jxSpYg33q5qU0OTPAbki1qxQ14_3tREUcqSuUuViFm9l5mAsgkrS_jvj-h76zYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات آمریکایی: اعراب بین ایران و اسرائیل یکی را انتخاب کنند
🔹
سفیر آمریکا در اراضی اشغالی خطاب به کشورهای عربی حاشیه خلیج فارس گفته میان اسرائیل و ایران «یک طرف را انتخاب کنید. کدام طرف را انتخاب می‌کنید؟»
🔹
مایک هاکبی ادعا کرده که اسرائیل «دشمن طبیعی» آن‌ها نیست و حتی مدعی شد که اسرائیل قصد نابودی آن‌ها را ندارد و «نمی‌خواهد سرزمینشان» را تصاحب کند.
🔹
این در حالی است که بسیاری از سیاستمداران صهیونیستی به طرح رژیم برای اشغالگری‌های بیشتر و پیگیری پروژه «اسرائیل بزرگ» اذعان کرده‌اند،‌ طرحی که شامل چندین کشور عربی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/435389" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دنیا به ترامپ می‌خندد
🔸
وقتی ترامپ می‌گوید «ایرانی‌ها دیگر نمی‌خندند»؛ اصفهانی‌ها جواب او را این چنین می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/435388" target="_blank">📅 19:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: در جنگ ایرانی‌ها فهمیدند عجب چیزهایی دارند
🔹
وقتی پل B1 را زدند ناگهان ایرانی‌ها توجه کردند که ما چه پُلی داریم.
🔹
وقتی مدرسۀ میناب را زدند متوجه می‌شوید که در مینابی که ته ایران است هم مدرسۀ کپری نداریم.
🔹
در جنگ است که شما می‌بینید شبکۀ برق‌تان را…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/435387" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگترین اتاق فرار دنیا کجاست؟
@Farsna</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/435386" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیوارنگاره میدان انقلاب با تصویری از ملی‌پوشان فوتبال
@Sportfars</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/435385" target="_blank">📅 19:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: الگوی توسعۀ ایران کاملا نشان می‌دهد دولت همواره نسبت به گسترش خدمات عمومی به دورترین و محروم‌ترین نقاط توجه ویژه داشته است
🔹
ایران تقریبا به تعداد تمام استان‌هایش فرودگاه دارد. اگر الگوی توسعۀ ایران چیز دیگر بود می‌گفت تمام پول این فرودگاه‌ها را در…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/435384" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBwS9sXbCuTvH4KGR8yE7PHOYVvnFq8Pt08k6RiTngZvQzxWG7sSYc-0je7DAPwS1zNWcIsYxq2mYKKO42jc_cdbXbyU_Po-igAX_O3r9Rh4g1oxqFbgHNQ2-5Pwe-JrhkkbHfKpGL2gAtG1r32Ee2w0M--7Ts8kYHN7-OHgXbTp_zF9xqqnzprT1wKAACAFxkQDMyGVR3r2G3WDQ7zTGFmdiUgJYjkiwYxD6SBjjmTZr4Z5ltIVFeS6ByI7RSXqMLu9xdI4j1InVIWijoBOeTQZey5RNnmSL35ipT6Pf1O1u11XguDviZTq1e3wmBjoXZGPEm4vKX7F6g7hfykew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/435383" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: ایران هنوز شگفتی‌هایی برای دشمن دارد
🔹
ایران ظرفیت عبور از چالش فعلی را دارد. برای توان نظامی ایران، ۴۷ سال زحمت کشیده شده است. به‌نظر من هیچ‌کس نمی‌داند ایران چقدر قدرت دارد.
🔹
اگر قرار است مستقل باشیم آخرش اسلحه‌ها حرف می‌زنند. @Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435382" target="_blank">📅 19:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا  گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/435381" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Live stream finished (4 seconds)</div>
<div class="tg-footer"><a href="https://t.me/farsna/435380" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOI-R_HJfqXW2SZysTCHfqs-QIUQpRrsZfKWrkffuOX_bbouyXtbemEVT_rYOBuh_IPt1xMzGKfAC7JXI0nzqAFR3LnrLD_NBXg74HkOI1rfbbcWhyAl1qtAyaBRSl0LGkQjLK9a6jq1u7V6VyKNI6paH-tjIm-Qjbx7cYf_C-b1BzStUG1gKHVPZjZkex_nCMFeUbGUPyKrMKjgNy7_O3ranA6bYwxoEQTOKMewRHi7BBbWJ30f26hWUEV7jvHSYgTgbmM3ztOHVV2Qilj0gCjsVxszbpPGxXJXVRacVSLap8mZKWsNk_TR8ba-3u0K9QjoHoj61GpVUzujCdKPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/435377" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4NV2ABFagMJbnt06TsibSJtJz2M2_UtqNKn71-nbvOuWsD_YI6EtFIsyXLsB2maO3Esgh7tqLkJVYnBKvzJZW30EB8oPMfIT6MOmf8zVf0Z7wKxHDBud17Kl9eqH40zIqT8vwbKmVXbpnzvhkUS-IMxvp_6mo4942BLOkIKgDTPvNMrTZP1cybEnvDvB8e_jLqbza6wIjnVfGCHL6QCEtnD5GtkbpS0x6ram-swtCzxbcJMnBQRr00Ghx6GFfBiR_s7E-CuIAQDBKfGoPq_WQfSSSVIOJwp4f5aMEdVq8FpE3Tf9pBHj-Z4R9XzfRqeVa-rRVq3_GWZGQDR7nq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد بود؛ اما آنچه ملت ایران از فرزندان خود انتظار دارد، ایستادن شرافتمندانه و جنگیدن با همه توان در میدان رقابت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/435376" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv3kZBASh6Ppz_c7kyG6Vi1he58Bflrkd82Ip71SSJqxxZrGAf8m59DhC-k4t-Ab7DcnAvt_Qm3IF7nGveTAMPoLlO39MTxKow-zWqCfwnylerF6PuMTncA-1xYLkQpiSwsYwtkUJ_TPMerPG644k3mgUJ-N4DBL4-xaS4Ak-w3-hIqxHEpvWQVi0GcVuxJc5w6MEe256J_y9Ojz-w0FmwNUbizd4l2gt51Cl1QZ_VGcIyufK7AKK9NdpKtZXmmkmb52Texp5Sq98jfBf1-lbHfChtlaQDf98vBGoJGdViXKmeO4jlfR-UhZHrqdA5ghirY0IXm5QmGVGX2u1MSaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا
گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در
سایت
،
ایتا
،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/435375" target="_blank">📅 18:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-34.pdf</div>
  <div class="tg-doc-extra">2.3 MB</div>
</div>
<a href="https://t.me/farsna/435374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۳۳.pdf</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/435374" target="_blank">📅 18:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JftG4Z9lf5WPnCr7ZUyWkk-9KiyTpdjYfoQJoNQxzhmfHwUTxewg8wXohfGQXDAZmdBdwMIVydTE9iCPwDqHIuVoWS2IrcbL_XZE8DPzsV7WCuDBlClY-UQfvWO5DsxyoYhnyPMpYtVG76mxHnvY2sGiNWFjY3SC6A5Dn1moAd20szTcTU3hirEJ_CGJ2Det9exwmpVncbpsJl0MVKdd-5Y7xkxiM5qnMW1ddunG32TJ2F7xOwaIsnRuTsouzUUaukvbw6RAf2XsPkbB8RUWQl-igEMfCfE2pXfgm4o4imJQT-r6CYSVK-7TWpT1_AGtxrfdd_zC4ayZDf0xvoCW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/435373" target="_blank">📅 18:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/435372" target="_blank">📅 18:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Zl-zm9Z2jcXY_P1YSpNS53zcVOEn-FmHl59D6Ki2jY88m_d4E2HaG_1dg5TDs1bv-Jj7dqGT7tX8EL2Sn1DylS4v9z0XR0QzJFFRUQgnJzqLGqDVFuDc7dbbJlo-t-0pWRC2RH-dYr7Ap-WtL4DQrISurSMxjfCx8nVXrvbmcFpb-1ybR1dbP3bOME0mi3vcUbZ_o7klMxgHuyshvU0Sz8ztJP4xDroVJM0M9296ic9YBEtmcGw_zxu6YE_-c0u5dWuQcSy8QpTJjzymE-UZJsPYNk5trSks2krF-wZDxiNsxX32QdB_gb2RIk-TMcRjGl_Nstfze-EPC02yQZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: تأثیر جنگ ایران، برای صنعت هوایی در ابعاد بحران کروناست
🔹
اندرو لوبنبرگ، تحلیلگر خطوط هوایی در بارکلیز، می‌گوید: گرانی سرسام‌آور سوخت جت فشار زیادی به شرکت‌های هواپیمایی وارد کرده است. بحران فعلی مانند «کوویدِ بعدی» است. ورشکستگی‌ها، ادغام‌ شرکت‌‌ها و بازنشستگی سریع‌ هواپیماهای قدیمی در راه است.
🔹
احتمالاً دوران سفرهای هوایی ارزان‌قیمت درحال نزدیک‌شدن به پایان خود است. بسیاری در این صنعت اکنون در این فکر هستند که پس از تعطیلی شرکت هواپیمایی «اسپیریت» آمریکا، کدام شرکت ممکن است بعدی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435369" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIKVEVScLBb3IFaGiGLmZ3n2arovLfhsyi-WXA2MCEHMTBQptUfkc0yrBWpcMJ4aoeZ56L_nDbOo6djvXFdeMQEApki2iead5wCsmsR6jkYNbFVuJHIL6GfBkb7A7ZJXdMMpnO98jEeGawPRXOMhS-zY20eKUoFP8CPwaYBleVHtUVk43XAyE-7BwZUHNi7QEU7qqDfhcW_AryKx2GVvSFNiriWFMzzoTjujj0VmCMJTt6rIPzPNnare11gGxBEYxFCRD8FSWzy-NwBgpxcAqPhcMdQMgkrGy18Yhg_8HBskNO-nWknTwj5qHTMLpn88sn_zzQ_q5Bxr5QG4ajlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت خود را از بازار برق بیرون می‌کشد
🔹
سندی به رویت خبرنگار فارس رسیده که مشخص می‌کند، مشترکان برق با مصرف بالای ۱۵۰ کیلووات شامل بخش‌های خانگی، صنعتی و کشاورزی از تاریخ ۲۲ تیر باید برق خود را به جای دولت از بورس انرژی خریداری کنند.
🔹
پیشتر برنامه هفتم توسعه دولت را مکلف به خروج از بازار برق کرده بود؛ از سال آینده دامنه خرید و فروش برق در بورس برای مشترکان بالای ۳۰ کیلووات نیز برقرار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/435368" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامه سمت خدا:  آمریکایی‌ها می‌گویند ما می‌دانیم ایرانی‌ها چه تجهیزاتی دارند و راه مقابله با آن را هم می‌دانیم اما بازهم نمی‌توانیم در مقابل ایران مقاومت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/435366" target="_blank">📅 17:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/435365" target="_blank">📅 17:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهرهٔ رسانه‌ای پرنفوذ اروپا: با افتخار صهیونیست‌ غیریهودی هستم
🔹
ماتیاس دوپنر، مالک پایگاه‌های خبری پولیتیکو و بیزنس اینسایدر، عضو هیئت‌مدیره نتفلیکس و عضو کمیتهٔ اجرایی کنفرانس بیلدربرگ: صهیونیسم نژادپرستی نیست، بلکه ضدیت با صهیونیسم نژادپرستی است.
🔹
من با تمام وجود، از روی اعتقاد و با اشتیاق، یک صهیونیست غیریهودی هستم. اسرائیل تنها دموکراسی منطقه و سرپل ارزش‌های غربی است.
🔹
اسرائیل با وجود همه مسائل، سرزمین آزادی و مدارا، و سرزمین دفاع مقتدرانه و موفقیت‌آمیز از ارزش‌های ماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/435364" target="_blank">📅 17:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435363">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره همرزم فرمانده شهید یگان فاتحین از آخرین دیدار با شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/435363" target="_blank">📅 17:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnsfQ-21nQGx4oVqdRRAgtfbKdt-wJRkYXNOkvUyGHfVQpxWqnR7p8IeinHqDYn4vkoKQnXfQMhfTsNA2Jv0Jk4ivBBqWlLbIk6_c_LxPSZa-ehK2R264Q5trnjOVypLmWeqi7O2b4cn9KfdxWFKxT-WVEPBR4TSOZJKEZAUgzlP772hzS2UJ-A_jPtAlTtoDCq2R-EQHn05W0-f55TPS6SbKSQhfalLQhrSMzuAP_8cgpM3AtUaHICoOXaqR2Ejt8g7Z7vAP1JxAgaFpVUisCvRXPzBoReFHmvk_o_WcgEX9JkZQf4kRSEdBDwkMtvCB5xrUVDcJpgmKgaBfJ5fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO3IRCWe0mpl_7-M-UfmPL0F_6ccfAOVTligy1cEamW_-RyX59Vf0ZLG55-zXpqniySbD8RKm5nqR76BwJ7fw-WjB4s7_2VZ0N3WkSXw-p2w6WxcFB6RcumXOz1-QQ_yhfu764BF3PiYN4A_AL6a4tfg5bZC0SE1mdcSjMMa9nnTGHemNAFRsF0cTnrwjlnfLXqfH3pSa1Ot01_mM7Ig2YkwZCWam0P_PmDpfok-A1WqiEJwrm-j1Qhzdh3lIlIQOhjNE0wVu2UPzt1WNVDOx4sHgkckxdQoR4v7-LiPSCDimgHToXeZ3NB6HGE53agNXXsyIrmx-b8ijrKoIOtong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQe3xul7Vk87gXQtjxbX4UJsiU--IizsTRwfmnSLW7C-8BX1Z5pYR3B6y7abajYo0KD8hyHdO1BOUfy5R-MQiTCHl2Lijb3RR2pAc7W7Jv0tz35Thxa2q3OhNRK8xncWpsbWYu3SazTFkNbABUXWSOeplHuXE8lYSwvzbwVtNsWKslpaqP3EKHCx1L5Mea7X-Weru_CsSMSOgQqSFSYNAYufOZIt-76mq1HcZ__4IxO6H7GV0fSW1dhP_M31zxCF6m7k1-bZcN1rvx8lSuJgIj-C-w7z-bLi6e4Ivw_zJsIWJjrMi28u1DvwYw_kfCfG_Z0CyRBYWRIArcVxeo9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AelfQai14Ze5c9lZCBDY5p6p0OSgLyvTtsiWI-ceq5cLg1Se4YaiTkre52n1HhUTtHgoF9oIC6UN_CeTN5I5Nz0d76gwYJ5f7ewSNg6g6hD26I6hxjQFnlWJFN2nsPjJ8oxQX3GuNg3LLSDIuU5vEbzJH6Hm3bpUnmNGIrEAMmyqEnuCu4Lad3h_91u00Vc4x-mIe6ElUK_b9QST91vCWJaXt6bMZr_MDIoo1mdccoEgM1e-DZyG7mej_b89f86HNWXrm4pWqtbBOpPK-KfZu2Mcjp71bneUuUficYJ2DYSIHmFgXPoaNxYLzLvp8KcPgR32wUWO3UqLjOn0CyY-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9lt9lzDCZizHgrcpLOJPp9-qlCP5YcFNwSTEHkmBWJuLXTQyxR5KkAklBz03xJVwj2H7YH8EWSuf37CB3xKKd-3VA1rwXuXrcJPGWagdIdDf-oQtlkiepkSrEI5y1xceaposRj1M2U--4hpnm2C-x9DX-_3RKuedSob8SzvoTqAb2pd-pXud_UWvILTaJ16FjmlHIjC_B8oCpUVnOSvDyKhlWDKZTrEMeD3u7Idb-LAOUb_bmx02NZJUIjnj1GfLn5w6C7JRjIxRPV0eHd8iz7bV6Xo6cboDsN-e1IOdkDwZb24ll2P6rLO0l1NVgakawvd4btd5Dvg7sLWTyOx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvrKA4vxYoZfz-ArRrsGsXYu3KmXWKPzDQJBN23MS0JMVBZWrwd8bUpETJbRVKbs5nAtZkHZHvCJYdQAimiPwhtuzoTEEeh8pV_KNQ9H6JYPH4XVjfSYDemmalNAX5dXqh_H9--AIze13AtAgMd8KANfLQDaaqUp-xpy_O7mjUWmbFal3MzRKh9WOOGUIj-lYai5x7NALArkeAztb8ZO4_a4EJsaHqk0_FrQpBy7ii6rQsQsA4k24z3TBfGXY9lu06EBRhxD1DLgqXoFGfG5mVMv9lQUWwWFS7c-X_lbg9-2N_oDdAJrv6Jj6sv29Nw5b8r2TWgFhz77Tkm0UMPHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk9nS7-f1HKkQjR7f5re_i5GNiBEzwqixnmMt_BnVbe47kqeZMTygwaUI_B88Cyy5OZ-U2u-dC53D_bme2hIoPqnivUmpy9iqni8UA_cch2tcUrDrrBebprR_9hJSkCxqI30DSFfkQ7mbcBR9FUhx0VW8hgxh3lsNBwPvouougc-bjQ49PJNLUl0yl05xrjY7-iIatzDsdgCSIa0iHOjg6hEuEx5yna0jdykQHJH4I0WUCsdDSVh28Izct0BpweDFUBdy5QpimY8PbCtN-HT0mWDzmR9u3ug6L3X3b6YmrH6R9P7fq2QmZiLXsoOtu8IwERJ5dzN0yF24o-_QCQM6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سلام شهید؛ آئین گرامیداشت شهدای جنگ رمضان
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/435356" target="_blank">📅 17:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYJSudKGM_psCpMmW9308MDIqOgkLeC1JR_eAu9AmdQe_wHsmVVws18_XieJUsWbchNGW1CSIuW50nI6Slva4QhoDLa3ZuqmcOcNtbIwSrtZ6niQd3PS5EJNZ9ML4YHA5Sk-nZps_YJSYE6YXtdrYd4frWLIYx740YbzSBic5RmynDNCIbqpqvX1UBVdKjITuzQy4GdKNJDiyTY4W3A29Sw7ZCk-pFd0Fa2NTXv_I5QVFzl9olCDiLBnJ9IHSjg80J8rcyxEDAm1253pJ4yr5dLS4PGv9ONQuwaoSmV5DiK3-i3NYX6XQV82Ok_7uN9nmvsHxW5O4ZBqpwSa-3QUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر آب سدهای کشور به ۶۵ درصد رسید
🔹
طبق جدیدترین آمارهای وزارت نیرو، میزان پر شدگی سدهای کشور در حال حاضر به ۶۵ درصد رسیده و حجم آب موجود سدها نسبت به سال گذشته ۲۴ درصد افزایش دارد.
🔹
با این حال در مناطق پرجمعیت مانند تهران، البرز، مشهد، خراسان‌شمالی و مرکزی همچنان باید رعایت مدیریت آب و صرفه‌جویی در دستور کار قرار گیرد تا از شرایط کم‌آبی در تابستان بتوانیم به سلامت عبور کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/435355" target="_blank">📅 17:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7JwZTSRdVxAhsImnB8UPyPdASfnu2i7EHB03FNkbjEm7qQcCU3OsS8E8Hf7szbkYB-HbqtpLCfQfi69-I7ZGxz9fIeUv8Tx2h7raLuSarW95n3uP-AARVtA_DQm8XiG1vaOtlFAD5YBPGadYwwxkTYq11qb5N4i0TXISivLwGZgRMRl4i-IN-kKHJoJYvaRjUtNufXLlclxZU-ag6WP6n54FvPeJIQCMNQZHpBNsIOffyGaIDSmWBMirL40jk5ZXuYGmXuH-nh4cWz4hxetVfrbxwsMvS30Hs-_s_beMuRbG_LjLIgPORZ40zM5igMO1Schq0k41tqPwhzJtMo2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمزگانی‌ها روزانه به ۱۵ کشتی در تنگهٔ هرمز خدمات می‌دهند
🔹
به گفتهٔ مسئولان بنادر و دریانوردی هرمزگان با همکاری مردم محلی روزانه به ۱۰ تا ۱۵ کشتی معطل‌مانده در تنگهٔ هرمز خدمات‌رسانی متنوع می‌شود.
🔹
این خدمات شامل تامین آب، سوخت، نیازهای درمانی و دارویی، نیازهای فنی و تعمیراتی سیار و... است.
🔹
۴ لنگرگاه در منطقهٔ پیرامونی بندرعباس و قشم وجود دارد که زیر نظر سازمان بنادر و دریانوردی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/435354" target="_blank">📅 17:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تشخیص پیکرهای تکه‌تکه‌شدهٔ کودکان میناب توسط مادرانشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/435353" target="_blank">📅 16:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJOYjoN48jZWtyS0qJ4cCQCvlzGS71E1zgwMDtF1zRxMHpnWZT8_mtsS2wBwzZOnkMcoQNmH_ZSnzZT74PzSc8DwxvZ7ayknwYv6UDmtl6O5CGQ7K5pBjWIlcTekfwC6sm9bAjFR9uFMDSjiWiqOdogIT8iovieytwZVxdPvPJoweJTo4gYuM5GJpP8Ra3nInL_QLGoYOU9F97MGVoWvi2b5lRqcD1AOvysAdIB7RCYKX3EjCmeY4c34uSKfNaOPZ0Qn3fXGEHqmlZKmfo6az-IOmQNhIzsNS6blaMV-MX5-KD7gqLOiWXkowfVQ7GxFxs4eRpdvMzftCMKj_sB9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgBdRXFc_UebOQS6nC0sVRPN54Yq0STNTeNKA1r5CDqHjKQFRDjot5KetIQFqTrLboXS7js0qFLWugvI6ENMSdMWzx-A7Br_Q1DeIfkIB5PVgz6K5ZyEAxgVrlVm_tM8HsBzC69m8Rk1nIxE21JiTqehllawlCEgF0VYjq_4k3i7l-Deow67Kom0ZLTfbSTTqBESZMFKgeKyBUCnr8vD2MRciyRjEseIjlBy8XET6rOjN3FXDmqWK1baLmHTTRlv9Q8ng7Pa8VO40hc6uHzUckLTBdeiWid9LLfKduruOfgty2j2wSjiJoihdJzZI4BM5iOmP-oj3w4kVZ4oadEgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9r9oPNCIbt2PXeDB1c7-MvHO7eOnf-67UZhJY6FCo2rF9eTzSwf4Y_4OfRs7jKN9IJPv_5Ne9pbb3u9qBGIHWmCar1Fvqdg56bQjlS4Tzf9axQIM7TAm4c1TFQOyuRAXYxrjjvxg21I7c05Puu7gH0C2DKF6Sr3SAH2dUzoMRPKVNVXNkFA8AWlQdiY-qMtCzQkHfgAv6SL_KH_1LdGJv0hp0R683Va6CfYu1VC3F65nEVTzGT3guKp_hGOtDs9bXznYl5tUgiukia83ra-OFd0me8Izlj6cVhedy5Xobpc0zIEICwUb-4RzQAZ02qkG0QL1XZDiolJ2OQbU5AzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqk_0Lmzs-J1PunKEqzySKGZdvoBFFexOkwdNTBglhhixg6AtdTwxB7HfPOwjgjCvNxrJmeNvHqge8QZ7CFOzpAHIyZ7aFBC4ProP1E1XoJJP-euwx5iSyobxiVIGCjvfvnh2kzQsiSexJf1T79izKluLVdKoz_utmW-87vZdoCQhrlyHKAqt4XlQTrmY5EsAnR9Z5GKpo1_zw--FHum6V-a7wo8WUmsjvYHzIE5zSvpVjUlgL0mn45WbPDbNvwkjjTc0rXAD4Fr0bTtllgbFcic-KC6-1BUllQiBPq9y5xb-XWVf83kSR3PuwgafThw2Mr0ddIX90Glj1EKpFn-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDhomIRnu3ovdOeQPs60TEfgQyPctlVsg6rJsPlUzS2895wFZcWPVS8c6c9pY81npIbQW16E-Y1CVWwqI9JrEM5MzeVgjOXix4VosCmxQPyTiSiQHuI_q8YevIXzGMkAunP82DqsZbGMB85j4DvBOm79dB3XpAGBknjOYLopzL3bI0dJal60GBDJSZoQgwkp8RSJkvFLKzvuiOK2kEXo6ib1gHnUZp09JB-4AtcoXY80X506-lND19tFzkxY7Vx0eqA0d9RTMCeDuKEU8tsQYRGxFnUNl6b-_0pPgm0QVoT_P9hUCRkN4uH5GJ2PV75QVAExrP-atFCm-DD06oiV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/subLx05rcjrmASf-WWDj4EWg9ufpQusnkyXUniLdgs5bLOQRmpr8AfB6wD1XD_WwnFsBxxWFvgi9uB4G8CQjJboGz3iHXoiBgkC_TDu7iTAxUpcZseDEJ-bT43zE-usy-5vnjK_etNwrnTJ6Zz3UEqWC_hi-816FIstzO23W4MoaydvpQTrxGc0WFGk0ckBz2D8ZG1vXg-FMZSCdtPrXap2w60DMg-zwv6WPvTfwonlPekMFKeTirVv-9kpZxeBJELcDbBryb6_Y0xV_vc8dNCPLYI-Hxy6IZ-Cm1RHDg5Zy2_pfGFAjtqO9o2-Fu3n1b5yqMLCHGFPIu6opypFEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r23x5l8GWwVjM22moy-I-tRMgcUGKjVz4_43HGXjdxoU5_jKK6jxcY-lHZArXiUUgdBD8d80INOOlEubF_bp7V7m-1enJtsJzrwLnXPQ1Yre5MPvhNzbxfz0M1GbvyT7Nzr3dagqPTK8BWKbmTZJpW6b5SBztlDrNmI1wPDGpGCqZGtgm1y9xkv7B3Eb4c6Iaf-1vkXLJU4mIRnlOhgNpBHWH-4faADjIghBeGQhGI9svua-acdhOtzywmlDXkkTp_7Vt-lRzOe-rW0LoJlfiKOkpKuOgRyRKaxYImLffn-MxNQPmgF1bPeMRXhCAkVL-aijGZ6BnlyYr2qClbb2NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری هفتمین نمایشگاه مجازی کتاب تهران
🔹
نشست خبری هفتمین دوره نمایشگاه مجازی کتاب تهران امروز با حضور قائم‌مقام نمایشگاه کتاب تهران در خانه کتاب برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435346" target="_blank">📅 16:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ سلاح مهم شیطان که با آن بر مردم مسلط می‌شود
صحبت‌های شنیدنی حجت‌الاسلام رفیعی در برنامه سمت خدا
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/435345" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV3rEMz4P8eZTf0Qzp84oOjecNJeAHLGZMF9nNn_JX2C_xgGKtfdnEOFCsCYIZa8UQJ5ET_dznPZnVgOyl4azX3JFH2cq-4OPivK_i3n_0uPEE8X-W4qFzGuNVLskytNkm3fwrNDSYl-wcP1YUZOsII-PrgTApL_AHynAgRxoctI-r8xTK3_iIFcS_Qz7cZl0wslSTFHoIKZphGCO_q6QnEkljnfVtxKBRX__lNmRvKF_T0Gk3flryY38b6PpXFhxa5KD4OywX_tM9ej-HSARQFPvhCE3GAfW4UIsIU8yAEe24MBMg3Wgo3rCwgJRvAhBxEaap4uFA2XcqyPnFrpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر نقشه انتخاباتی؛ حربه جمهوری‌خواهان برای فرار از شکست
🔹
جنگ ایران، جمهوری‌خواهان را در شرایط بسیار دشواری قرار داده و احتمال پیروزی آن‌ها در انتخابات میان‌دوره کنگره را کاهش داده است. اکنون آن‌ها در صدد هستند تا با «بازطراحی نقشه انتخاباتی»، ضعف کاهش محبوبیت در میان مردم آمریکا را پوشش دهند و بر دموکرات‌ها پیروز شوند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/435344" target="_blank">📅 16:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما از ایران سپاسگزاریم که به‌خاطر حمایت از حقوق ما در خاک، عزت و کرامت، سختی‌های بسیاری را به جان خریده است. @Farsna</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/435343" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435342" target="_blank">📅 16:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در سنای فیلیپین
🔹
همزمان با تشدید تنش‌ها بر سر دستگیری یک سناتور ارشد، صدای تیراندازی در داخل سنای فیلیپین شنیده شد.
🔹
شاهدان عینی از شنیده شدن صدای تیراندازی‌های متعدد خبر دادند که باعث شد روزنامه‌نگاران و دیگران به دنبال پناهگاه بگردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/435340" target="_blank">📅 16:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/435339" target="_blank">📅 16:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_zHvZrm_WrYTYkPwFLsWgjWWMK75kWH0Ib1oNNKWEci54lbqC_W8K1uI4z-RV7IhCJqyLtaokZABSUgeDr_JHsnxeCD84Y7_vU_Ddhk6D6cYc27q2r2qRjDAeuERPTzV3Oaubj6-XlSPyqWpGy2IV1hRqG99txBIyaZ-zKnsJ4-WtSuRrINnSYyfhmiVLwWFHbcoqVfS1wfqS6aZvBsu86EVf5zS5_vI5kC8OjL8u-k7LbNb8ya5Yt5Eo0OTV3K-_yrNQg6LVScK86VTLXLbyWHnvUGBRsFp2YwAmao4jkt-CNAmmsrok6XzVsgzfqEW1z-MG2qLsLiesED6X5BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم توقیف اموال باشگاه استقلال
🔹
ساعدی‌فر، مالک برند پوشاک ورزشی «مجید» به‌دلیل دریافت‌نکردن مطالبات خود از استقلال در زمان تولید لباس‌های این باشگاه، از آبی‌ها شکایت کرده و علاوه‌بر دریافت حکم دادگاه، دستور توقیف اموال را هم گرفته است.
🔹
همچنین طبق شنیده‌ها دسترسی به حساب‌های رسمی باشگاه با مشکل مواجه شده و مشخص نیست تراکنش مالی استقلال دقیقا از چه مسیری انجام می‌شود.
🔹
آخرین پیگیری‌ها نشان می‌دهد که باشگاه استقلال هنوز اقدامی برای پرداخت بدهی خود انجام نداده و همین موضوع باعث شده تا هر ماه حدود ۷۰۰ میلیون تومان جریمه به مطالبات ساعدی‌فر اضافه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/435338" target="_blank">📅 16:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB_Cgiz-6f4qk9qZvhYgXUGpuu1uFAfy4zjQlvjxSxwdwv8xWQM9VGUB9Hh3mLwN7RlQBBOZu3JhAJqDOiXgzLqN7jmkYmBZS6N9D9p-7Fqxe2WqO9Ab1YnAtrPeLEygaX4TOMnYakc9t1jSpkgRJ-fOQwabtQCKOYFdaqQ_pAnqT_bFmDx788aakZRe4KBjIpqliwp7a56uqRqDEp4rI6bZOUa9XFaUDNA2uuN1FZFHuGPwKgiG-KvFkjK2EhMdX1ue33AYKbyduWqhDRjGsc09xYBOomWsNsyJDLK_CxuY3VTxfx1hH8hIrsK61cGDGDhqUc2ZOtmySLM0qam4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: عراقچی برای شرکت در نشست وزرای خارجهٔ بریکس به هند سفر می‌کند.
🔸
نشست وزرای خارجهٔ کشورهای عضو بریکس پنجشنبه و جمعه در دهلی‌نو برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/435337" target="_blank">📅 16:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=kwVlSXKoGlC3DPHEF5V8KvVck7Gjr2-JPcm5muXi7bRR7eCmWpC733iXwpevfQWC07QWGE6seVph-G0encJpvXSzY2EM_8bwHCIzWnX05_GkKk6v8bbVPO6t5ihakSi7M_xvn0b6dxdrvmq_OlOnjVdXLwdL82CD6k8Dc4OOnCIkbor8WSQ7H9vxJdPVIl-IBc0KUkhPfq8_fuiZ1VK8nRgkmjioZM3_RrVXJcHqQ-2fpTtNp4wFXXmJ1_Q78BAFvzvQcuzm-SILV_HLjDIeWKZXkNK1qVWv30sC1L8S-TFAqmzRiZ_fufMsaMgcfMHKF9rtkaR0GMevklPL7zentw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=kwVlSXKoGlC3DPHEF5V8KvVck7Gjr2-JPcm5muXi7bRR7eCmWpC733iXwpevfQWC07QWGE6seVph-G0encJpvXSzY2EM_8bwHCIzWnX05_GkKk6v8bbVPO6t5ihakSi7M_xvn0b6dxdrvmq_OlOnjVdXLwdL82CD6k8Dc4OOnCIkbor8WSQ7H9vxJdPVIl-IBc0KUkhPfq8_fuiZ1VK8nRgkmjioZM3_RrVXJcHqQ-2fpTtNp4wFXXmJ1_Q78BAFvzvQcuzm-SILV_HLjDIeWKZXkNK1qVWv30sC1L8S-TFAqmzRiZ_fufMsaMgcfMHKF9rtkaR0GMevklPL7zentw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: امیدواریم ترامپ در چین موضوع پایان‌دادن به جنگ اوکراین را مطرح کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/435336" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a66b75.mp4?token=cUi8eskNfSH0zrZnUqmUeNVkOo5XH3bdALZb896_vfkk99vcLkJy66Zd06CULRnUUIBh7P9SYgJS0Mbm4ACB1ow7POLcQHeilcVcNT0TErymCATs3X7mmKJzwbtF7SEqA31dXt4VG9C9yJxozSpyQ1vGP7NaKbmoj_g2xHUuieDLkeGp-fFOmQE-Co_yLpHHEqZvHSFFNjYeyjVwoa-JNoe2JoytQqBDilcS0dhy7uXn7v1RKRueZFyx9aLM181BTaccn9UA2t_t65KxgjfVGnCyUFh2XjPNXsBLwVamY52XEX4VN_ND5dR1Bi1fhziHfe7uUmHV6iqwwb_g-40yiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a66b75.mp4?token=cUi8eskNfSH0zrZnUqmUeNVkOo5XH3bdALZb896_vfkk99vcLkJy66Zd06CULRnUUIBh7P9SYgJS0Mbm4ACB1ow7POLcQHeilcVcNT0TErymCATs3X7mmKJzwbtF7SEqA31dXt4VG9C9yJxozSpyQ1vGP7NaKbmoj_g2xHUuieDLkeGp-fFOmQE-Co_yLpHHEqZvHSFFNjYeyjVwoa-JNoe2JoytQqBDilcS0dhy7uXn7v1RKRueZFyx9aLM181BTaccn9UA2t_t65KxgjfVGnCyUFh2XjPNXsBLwVamY52XEX4VN_ND5dR1Bi1fhziHfe7uUmHV6iqwwb_g-40yiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ روش درآمدزایی از کابل‌های کف تنگهٔ هرمز
🔹
رئیس اندیشکده اقتصاد دانش‌بنیان در گفت‌وگو با فارس: کابل‌های فیبر نوری به‌عنوان کالایی ارزشمند از آب‌های ایران و عمان عبور می‌کنند.
🔹
تجربهٔ جهانی نشان می‌دهد کشورهای ساحلی از طریق شرکت‌های عبوردهنده، منابع درآمدی متنوعی از جمله مالیات، هزینه حفاظت از محیط زیست، گارد ساحلی، تعمیر و نگهداری کابل‌ها دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/435335" target="_blank">📅 16:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD2CQQgcAZ-rHFJza4AaezmmDa9xU5VVKzSFUgMwKACwClzyXgjG3F38XlifX-Cc5gySkZGgJBVZOXMXWM3P8dyGRQjfOlYuYU39QyIaEQMYTfvr94Wt0hSKNFXSRz0SkbawrCtbonHTLHdikZdJfvvP1dKyq2NVX6E-87ChVe0k_V3_zSv02-_V4DhYjrORpqvjGhH9rlA7YkqOIVuTrklm8yZ7ZR0GqWYNxhRHVNWSDhE7aw2v5tYXErRqz8x83V99q49N0CMU7h0EeHSX2sO2rP7aLR6D-FDhPYjrzI3qy-82mcC0RUxBf5VheAH6P1qQ-tjRCjtB7C5p7duJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیست و دومین نشست شورای عالی مدیران با حضور سرپرست و اعضای هیئت‌مدیره برگزار شد/تاکيد اسکندری بر توسعه بانکداری هوشمند و حمایت از تولید ملی در بانک صادرات ایران
بیست و دومین نشست شورای عالی مدیران بانک صادرات ایران با هدف بررسی شاخص‌های عملکردی سال ۱۴۰۴ و تشریح مهم‌ترین اهداف و راهکارها در مسیر توسعه خدمات مالی و بانکی برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/435334" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUVnlpRsEnAwRJ-0q13brkvVj67N3SR7ioUMjohiFxwRJ8bh9WW2io7vAt-jOg1-zQJYR95rw-BedH0fzPNvohollxYoJ7ndh0rge79a-PnypplR2VirUs54kde0BZlrkyMh-7yY6l2O0ze0ZIQhnK894EiWnDXLvvUveJ8sIPx6TknHdZ0LWHkFCM_2ECzki17Ae8V3Mn_yAwhQkk_tfoOnPIhaJwi3hy354JxejDLL7VoYCi9R-wgA25rkwGlL_38q5N2xP6eWTp6ESR2cbI4k6kmzvzglIZXVBZWYHjsZVyvxKFogA3cqgkIK_I14iDvbO58vgN0zenG2_mHdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIclVuG8Tgz49SnDQOtFVH72POFmZkycgMXu4qxTklgKSsX5civhvyDU7jC4NBOZ2VtJlLyBbDOs0F2Hly410fa9CW0PPBhLKsuhcyVoRaIcWLRazYj48fjtqMZIFznGr00BSho-BMr53F6BA2AuL8W3CfWZ2qeM89PHNrEu4je-Y5vvD4OV5C3zRMacVFHD5pduSmn6qinSQqAEtrnIm7IBtCg8jVbArQvXdjlLyCKMlaVBtiF1y6f4sn2xOiQCt2dSGxbPEcM3CRCYGhpzV074q_-TpW5yfBzFBgKL73Hi_ihOl-fzbFhvyVrVLLCR9uN8p9a_Ceadf4nqdujXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTbFP46ozcNqMKW8IQdi_R96FwSFjnFGSyPjSag-iCgGH9-ZBr9eoMc-EvkNfp5UET2PAM_UBLexw_EThxQ3fN_DLcPQA5C7VGud4kDzh5C8b4i-AiSnGnB2xTwWabeXm_NJ1wxb8SoeJdboMMToniAvribgvhg0RxEW6WjIwYPka5ELRNx6OeDsfclOOyTZpaDB3cX2qF_6x8gtpOB983Wc2llvZbiriOyspeJfdrV-VqudL68sE5GtFIkBr6iyPFPwwxnCvR57RtMMX_rmiqo1Tzi1RGUUA54YvDwaFOzuAEJmF2WkysT4DshWI9rk2LbJPJ8Iyb3Xl6DwfRjU2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
رونمایی رسانه مس ایران با حضور وزیر صمت؛
🔰
«عصر مس»؛ روایت آغاز شد
🔻
شماره نخستِ دوره تازه مجله الکترونیک «عصر مس» با حضور وزیر صنعت، معدن و تجارت، مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مسئولان کشور، رونمایی شد؛ رسانه‌ای روایی و چندرسانه‌ای که با نگاهی تازه، روایت صنعت مس ایران را بازخوانی می‌کند.
🔹
آیین رونماییِ نخستین شماره دوره تازه مجله الکترونیک «عصر مس»، امروز ۲۱اردیبهشت‌ماه در حاشیه افتتاح نمایشگاه «معدن و معنا» و با حضور سیدمحمد اتابک وزیر صنعت، معدن و تجارت، دکتر سیدمصطفی فیض مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مدیران و مسئولان برگزار شد.
🔹
«عصر مس» در دوره تازه خود با رویکردی نو در روایت‌گری رسانه‌ای، می‌کوشد تصویری زنده‌تر و عمیق‌تر از صنعت مس ایران ارائه دهد.
ادامه خبر در مس‌پرس
👇
👇
👇
https://mespress.ir/x6QG
◀️
شماره نخست دوره تازه مجله الکترونیک «عصر مس» را ازطریق لینک زیر دریافت کنید:
https://media.mespress.ir/d/2026/05/11/0/15374.pdf?ts=1778489262000
@mespress_ir</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/435331" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/435330" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdsSYVogPPVTF2Ro57rTOSTgVwB0vj4IvHSLz6mBa_RUHfrYWOgtM5oxiIzBh_ZGjLggLfMCt4o-MzE8blBHKc0XC83RAsCt45qY9EDhYLbmFDvyJhLFMYz-rdDDDjsvbd9o7HW-jyAdcCRGUvR05xS8ogolQrFGg3lQsTpDf8h3w5BvALGNwxxO8BicwysMavIkIJDIWC3BajAiy_pJQKXwIbfGGB_I_k1McQ-pMypbDi0wGFhNEE7raOnltT-rJUCZ_90zXFTfr5WjvALtZJ1QmziqwjvZtuxHLNwqgXbj4vEKEyALDnIHXiJWpDGyntQ8HAmsLw1TCq_rZkm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش از ۴۰۰ تن برنج احتکارشده در مازندران
🔹
فرمانده انتظامی مازندران: درپی بازرسی از یک انبار در بابل، بیش از ۴۰۸ تُن برنج احتکارشده به ارزش تقریبی ۱۴۷ میلیارد تومان کشف و یک متهم دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/435329" target="_blank">📅 15:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoTdt1rbOqwbIBIiqlRnjs9FDxsxSwgIDeNBFmBS1839ubaLeIElmD6mHheaxaw_XL-kko1fFwNdVAhwvFJ6FX1BKMssE6kllqbsB7mzompySLvvwaTcXz_7T2AGMmo2ovFxSEQQoiBuY00UVfVYrhZ3rQ877Th2iqHE7haxUB7V5OyjHaK4OkNB9h1iVlfnjDWXyvLuGRguPFgDjGzn1vBzIgSUoH6ELs4NQ8wqohO8FFEuFrersOWhmKEPF4BahohrEvANJs2dZsGWDkCSIg5i3sl-RmRB-mMTQ8NrNYYRudA0apvluDEsvet3ZCS4_FrP7fezHqNeGPQes0rQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حبس پول توسط بانک‌ها صدای وزارت صمت را هم درآورد
🔹
با وجود اینکه بانک‌ها بزرگترین دارندگان پول و دارایی در ایران هستند، اما عمکلرد سلیقه‌ای در تخصیص منابع و استفاده برای خرید ملک و تامین مالی شرکت‌های زیرمجموعهٔ خود، بسیاری از مردم را شاکی کرده است.
🔹
کسب اطلاع فارس نشان می‌دهد، حتی بانک‌ها برای بازسازی خسارات جنگ نیز ورود جدی نخواهند داشت. یک مقام در وزارت صمت می‌گوید که «امیدی به بانک‌ها برای تامین مالی بازسازی‌ها نداریم.»
🔹
بانک‌ها در شرایط جنگی هیچ وامی حتی وام‌های خرد ازدواج و فرزندآوری را پرداخت نمی‌کردند؛ با این حال در همان زمان برای عدم بازپرداخت اقساط جریمه هم گرفته بودند که با پیگیری‌ نهادهای بالادستی قرار است به حساب مشتریان بازگردانند.
🔹
ضعف نظارت بانک مرکزی و غلبهٔ نگاه بنگاه‌داری به بانکداری در بانک‌ها منابع بانک‌ها را به‌سمت فعالیت‌های غیرمولد سوق داده است.
🔹
تخصصی‌کردن بانک‌ها و تقسیم‌بندی آن‌ها به توسعه‌ای، تجاری، تخصصی، جامع، قرض‌الحسنه و پس‌انداز مسکن و نیز کاهش محدودیت در کنترل ترازنامه برای بانک‌هایی که در پروژه‌های تولیدی مشارکت کنند، از جمله راهکارهای بانک مرکزی برای خروج بانک‌ها از بنگاه‌داری و هدایت منابع به‌سمت تولید است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435328" target="_blank">📅 15:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کشف ۳ بمب انفجاری از یک تیم تروریستی
🔹
فرمانده مرزبانی فراجا: با هوشیاری مرزبانان در کنترل و مراقبت از مرزهای کشور، ۶۶۷ کیلوگرم انواع مواد مخدر به همراه ۴ قبضه سلاح و ۳ بمب انفجاری از قاچاقچیان قبل از ورود به کشور کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435327" target="_blank">📅 15:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa69c5177b.mp4?token=srq8EdBMOVRLiLKBJ271O3ucbEz4aZTFsV1FZK5ebo0R9aNPE1j2qdH_amiQI20lP6iLM8wWbZcSEuJcguDaXDDu3kUnVTjPT2L5tkogcgrFbL98MBEg2Fua0P-OLLlB6gYbWj393D-R-LZ56vBuB5guBCtSl7CkEBeXHfp-L59CtUGw7u9wgxzQK7uLFhQ7MZEq4xaiajoerwjCRX3EW6Ej47pSYmLas8uxqnAaSKJ5l9t3uB2Mep06uL7gHHsR3hgVQfPy293MWiEMWapbCWNCZtEKc_tuVIQE32M-TAvAHA9dIU9RJ9pHW8VLHB9QpkiL1k9hMt2oI_m3OgIGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa69c5177b.mp4?token=srq8EdBMOVRLiLKBJ271O3ucbEz4aZTFsV1FZK5ebo0R9aNPE1j2qdH_amiQI20lP6iLM8wWbZcSEuJcguDaXDDu3kUnVTjPT2L5tkogcgrFbL98MBEg2Fua0P-OLLlB6gYbWj393D-R-LZ56vBuB5guBCtSl7CkEBeXHfp-L59CtUGw7u9wgxzQK7uLFhQ7MZEq4xaiajoerwjCRX3EW6Ej47pSYmLas8uxqnAaSKJ5l9t3uB2Mep06uL7gHHsR3hgVQfPy293MWiEMWapbCWNCZtEKc_tuVIQE32M-TAvAHA9dIU9RJ9pHW8VLHB9QpkiL1k9hMt2oI_m3OgIGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستور کار ترامپ در سفر به چین؛ ایران محور اصلی
🔹
بلومبرگ گزارش داد که ترامپ قصد دارد در سفر به چین، شی جین‌پینگ را در ارتباط با فروش تسلیحات و خرید نفت از ایران تحت فشار قرار دهد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/435326" target="_blank">📅 15:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0EMtyDDNqm5aDAh8Xys5MUAhr1u0XGndPIP9ABhNdMXrkxzZ7VKwx6il4FzgQfgN0o7US1h8DJEfVDPCxXBoWwz4DMbi6iLnFoJEspneRCLq67dY9uJJBrRYeLJ3uYqA_doRvtBcmfUQz10vIJpLbxtzolIO9eqMS5BB1NWlW6wg_QDm24K4J3yo4SNAiF2RhgpfmuS0eCCYV5B7D5pJQ1eieS9iSi6CkqNnNM3nCIfQTHhgTVT4wKEJgKSftecCCvF0eZkQ224kdekNX0C34kk8aCNBJ_bTrNCoxYYgyScf4_7sewkSae61tJ9vAIYIsmyY1e59sFNBxEd02Vchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها معادل ۲ سد لتیان آب پس‌انداز کردند
🔹
کاهش ۲۵ لیتری سرانه مصرف روزانه آب توسط ۱۵ میلیون شهروند تهرانی در سال گذشته، به صرفه‌جویی ۱۳۶ میلیون مترمکعبی در پایتخت منجر شد؛ این رقم معادل ۲ برابر ظرفیت مخزن ۷۰ میلیون مترمکعبی سد لتیان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/435325" target="_blank">📅 15:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzgh8DHLI9kwJ1Jy4Ilm0WEdFgP02S-OfDxvXvrAf6S6uSLo9HtIz2UTyymaZO8A_crrOBGvNaLHW8KS94qlk1F33grOSJOwkFIWiy35n4MdLrFeFnCxktCGBxxgeff2ZXKCoIUm3pxEJauNDdOnETm1fcN6ijHeix7lcGLIE1BKZvWD4aFSikYteXW2ZlEzxbidciIvRblqqXiwfYhqbi_itSo-v6XouhyRcLWhBDUemmTt-p0SrxhmNdHtoMfj9p9ODcXpzoHNgZVe7f9_M6DUkYFimJ7S0r5-jUbRuKQRV-qwGT-pJaLLScrjmiHxhhKlRIS9D4icEm_TAmIuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اپوزیسیون اسرائیل: روند انحلال کنست را آغاز می‌کنیم
🔹
یائیر لاپید در شبکه ایکس نوشت: «با همکاری سایر جناح‌های اپوزیسیون، اخیراً تمام لوایح پیشنهادی را از دستورکار کنست (پارلمان رژیم اشغالگر) خارج کرده‌ایم. در غیاب اکثریت، ائتلاف قادر به تصویب حتی قوانین خود نیست. این وضعیت کنستِ در حال فروپاشی است.
🔹
همانطور که این هفته ذکر کردم، کنست از کار افتاده است و ما از هفته آینده روند انحلال آن را آغاز خواهیم کرد و در مسیر اصلاح اسرائیل گام برخواهیم داشت.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435324" target="_blank">📅 15:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsxR7Dv_QdIX4Lj0i2fxHd_nZRWKiVeRXz3LiuT1ndSWwwY3e4C5CX9OV9xPpSNrl_b1V6yZBpHEgvukr6cDh_x1_0ED_5pYwLYBg0g863L_dwmhU1qz1SOnaax9NlSha9O5m_L1RhIK2cbapamYeDIN_oF_1F7XvEwi_3hiHe_R9C7EEboX8f8KSEAnD3miS-jVhwnMkn1vUiTmJgNIvEZoXQ_pb0CthkUlmGByouGyV2L0hdEJYl7_VxEXeGaGtvbFx-bIQnX_JxaDCuTBSIGEaG7ax9qXF-2gJfKUOOb2sep2YOQ8d8dY1o5jJpVVv_oAlF-GtBXpnWZr0KcP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ بسته‌های چیپس ژاپنی از بسته‌بودن تنگهٔ هرمز پرید
🔹
شرکت Calbee ژاپن که تولیدکنندهٔ چیپس سیب‌زمینی و غلات است، اعلام کرد که به‌دلیل کاهش موجودی جوهرهای رنگی که پس‌از جنگ ایران ایجاد شده، بسته‌بندی محصولاتش را به سیاه و سفید تغییر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435323" target="_blank">📅 15:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBcoMw3kRtirfledOj-woaFErvrpLSl3Cl-3SprfV6n9RRjmJ04g3C-Pa0dy1A1FEegeg2U6x7Q8ZjBLzDVvhDrqzFxTboyWEnl7TgNamIVReclzB3JZ6vpVI-KWelhzqCIn71EjLV4rgp9btuzGUTZ9YuoCQ3AeMJCE8Kpc0qaLmJcXf1ZYNq--YpKP6x_LdOE93EZsxXWRg90-2hF-PLyUfbwTRfIwWdqUz_x71uzcrP3afynvY6jGtgUS4w2jB489KwqQXDXAzLOSP4ubOd2oQuCiNAPUk9MgkLumddegN4cZdNdYaT-ouJaZbbh4e7vz23IjcG4v9R8yJfgbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز روزانه ۱۵ میلیون بشکه نفت جهان را کم کرد
🔹
جدیدترین داده‌های بین‌المللی نشان می‌دهد حجم تولید ناخواسته متوقف‌شده نفت جهان با جهشی چشمگیر از ۱۲.۹ میلیون بشکه در روز در ماه مارس به ۱۵.۸ میلیون بشکه در آوریل افزایش یافته است.
🔸
این آمار که از پایگاه‌های معتبر انرژی گردآوری شده، بیانگر تأثیر عمیق درگیری‌های اخیر در منطقهٔ خلیج فارس بر بازارهای جهانی انرژی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435322" target="_blank">📅 15:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN0f51ETNAqu145wUoaNpPPSgO7F0xfZXOzrp6JKMgZs5Lfy_SMAtROpV-HGxL-K41ZdMnR1zm30f5ZtWxrWxZLLe3zqD4HhsPX1Inixqc-iVff-H-5-YsM4fLHPDx-TMe6OztHvfFN0uwVHV5bPywsQpG838y4aYQ4xAmAf88bdjyyZlskadqqJaZwtLF8NRnvmY10BViNl4225YLgORHou0_jd8leDDpwgDfQiBdfRycpxg_ZmY8y1sUBZ4wrZTK7uwOc5IIpszMO9KLqHQGFidiLYn3godyeCvch6-FRz7v17jPVeWzgOUEJwALXz4_WbsCTtIlcTL4xvaCHpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بازروایی انیمیشنی از رسوایی پدافند آمریکا در مقابل جنگنده ایرانی و طرح یک پرسش؛ چه رسوایی‌های دیگری همچنان افشا نشده‌اند؟
🔹
ویدئوی منتشر شده توسط شبکه راشا تودی داستان تحقیر پدافند چندلایه پایگاه آمریکا در کویت در مقابل جنگنده اف-۵ ایرانی را که روز شنبه…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435321" target="_blank">📅 14:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852c5d7e70.mp4?token=jmlI-9lzbqq6lifI86S7nxQA_b1LruVKDilR-DRm4b10XGfnfZeIgls6gGRZ-dgff-_N6CVCEt4tJpckgI7XuT6ZJiH-rL2ONT542a6FDw0PpT7LFj-sDRFWJa5-l4fnk_6sYeDGAnVmZ5buCHuOVIFec2-LLyiLypBNTM9OlBcEePlPFqTGU-AYHBwCQHbgolOgTBDP13rLkX_U5eEuiyiD5loQ9HSsFq_NewrAHPAm9C4e5tJNvkrvSguJnjkLSZ2j6WJR2HlEwR96K6jgmt2BDFfPBDnYy6Oiu8Xk2p6eK5nvnmQ7Z7Ko3Mclzv_yTfkQnGhwWOqYrfg4WFuAvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852c5d7e70.mp4?token=jmlI-9lzbqq6lifI86S7nxQA_b1LruVKDilR-DRm4b10XGfnfZeIgls6gGRZ-dgff-_N6CVCEt4tJpckgI7XuT6ZJiH-rL2ONT542a6FDw0PpT7LFj-sDRFWJa5-l4fnk_6sYeDGAnVmZ5buCHuOVIFec2-LLyiLypBNTM9OlBcEePlPFqTGU-AYHBwCQHbgolOgTBDP13rLkX_U5eEuiyiD5loQ9HSsFq_NewrAHPAm9C4e5tJNvkrvSguJnjkLSZ2j6WJR2HlEwR96K6jgmt2BDFfPBDnYy6Oiu8Xk2p6eK5nvnmQ7Z7Ko3Mclzv_yTfkQnGhwWOqYrfg4WFuAvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش سپاه تهران بزرگ با رمز «لبیک یا خامنه‌ای» برگزار شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435320" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3hP3dpNgqn1402_TMuY41pLbk7WxevDVEtZiK8YMBtbcb7G5UxRlFYJYwUq9MOND1tT9pGm8uKyQRfPA23BkB6ClHCjGTT2pBMFOWK4zSxul4HuwMDpTLG4O5wzLKJYILDhx_4OoeaSjwnHDhPz8fpb7UZ6qr_3oWDyXxgz8LfuMBHnfqBghCzMo01CywoXwp0j36Kx1cQC55WsA3dJQIQuT4xe6RpzvT6F7yvTlwxOmBT57GoULVQCLcyB1ZRbeRFpsQxRYHHgZNJz2feBRXLUAX5hBsAf6OfJloslpTBhLSI6BdFmHAwM6ziQ6XZ5e779FA7dNzNjrRTrhlyuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای سفر مخفیانهٔ رئیس موساد به امارات
🔹
وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش کرد که بارنیا، رئیس موساد، در زمان جنگ علیه ایران، دست‌کم دو بار برای هماهنگی عملیات‌ها علیه ایران به امارات سفر کرده است.
🔹
براساس این گزارش، هدف از دیدارهای بارنیا، همگام‌سازی تبادل اطلاعات و برنامه‌ریزی تهاجم علیه ایران بوده است.
🔹
وال‌استریت‌ژرونال همچنین گزارش کرده که «نقش ابوظبی در جنگ با ایران فراتر از هماهنگی اطلاعاتی بود» و فاش کرد که «امارات به‌طور مخفیانه حملات نظامی مستقلی را علیه ایران انجام داده و تنها کشوری به‌جز آمریکا و اسرائیل است که دست به چنین اقدامی زده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435319" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جادهٔ چالوس یک‌طرفه شد
🔹
پلیس‌راه البرز: به دلیل ایجاد ترافیک سنگین در جادهٔ چالوس و آزادراه تهران–شمال، تردد تمامی وسایل نقلیه از سمت چالوس به تهران (شمال به جنوب) به‌صورت مقطعی ممنوع خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/435318" target="_blank">📅 14:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isyZxBWAe0sTFclGRmQFAUQ2BgwxWT11pOlDPw8rxe2nBSExazTbO31IxDL-SlTeboW9DuijLLsAotI8OOlfckQ34-8dOhOlWHTRVFINarRkT93305LuGdg8KTQT6iSFmFzpHD6cNd1jucbQmSQILc6pasSc-Yfuv2ZxVGSier-ucZrL3nu1Or3UdJO5ssi64trWLYboVk0rN_MMm7Lt2Y8eygeiCRKHd5L9aMQ3SWKLx5_Ag9N_dcjLmu__SXg7hMgxM4dFdCELbFkQ2ybyaX924X-LHQ-b7CvRxngAVie-ghZKaoSIS55KGQOeuOUewpwWpWRqBVXho_w2dwLpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۰۰ تُن روغن احتکاری در بروجن
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: درپی بازرسی از یک انبار در بروجن، ۷۰۰ تُن روغن خوراکی احتکاری به ارزش تقریبی ۹۹۳ میلیارد تومان کشف و یک متهم دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/435317" target="_blank">📅 14:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV5smzqZcbvfcc1vfGgDRZNP0_peNSGy9RLL8VQbwMOfuBhY5vyqZXjOJ79KfX9allDCf9XRecdK7e6k_LXFaPPZWrnPlC_9O60CSkdAZp3vJHnhCmmcKaoIXzf179py87cKij229Iv8WKbg4nFqMFH0PNJc82DHOxhBaDWOwfsJfUWJeF2RJXgplKJBHjxDFdgcp8DaBhlEKp-2E9QN0RWolsKv8n2DEw9rT9XMzJNWRqdz9eUa7UslWldRKq8AgdL-ZT6ZCBJrEgvb0gYfvFOVHkCzUGFkcLE4K6Ddh2P_AzGj2LpKBeygyUAwZPD0pQaVUKFfCsPmy8Muy5Nhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: وظیفهٔ ما این است که با همه وجود در کنار مردم باشیم
🔹
با قدردانی از نیروهای جانفدای وزارت جهادکشاورزی از دورترین روستاهای مرزی تا پایتخت و وزیر محترم که از ابتدای جنگ رمضان پای کار معیشت مردم عزیز ایران بوده‌اند، می‌خواهم تمام توانشان را برای کنترل قیمت‌ها به‌کار ببندند.
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435315" target="_blank">📅 14:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AliVFXyBcLophbejZqE57Ym6aA2A0lqDE_zhP1g384B0DrzICvQ4eAFxmAQ-bxedhqQQKN08TxMV4yd4NbFSV8hd0AYHjAAWExbGRK028pTchuWV5JgOzMPipvS_CAqTNKpq-hHkzWqsPY-2eLzOTVuUz8piw81BjIp8dag8Cz7Nhg58lDELXlN7qFzw24IcrPIxfzWnFXD3tx6gcIDactkcXpc1J_yHq0jElXFBubFkFb25D_wq2g45QWNWJD3IAs3KzuMk1dpcT71ri7s8flOF7zzK9heEFu92l-UcYQnZZoaSFV_JWSqQmgCb4WhRdOL2cg4ak-es-FhesAlH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم که با تلاش پزشکان بهتر شود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/435314" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توقیف اموال ۲۴ فرد مرتبط با دشمن
🔹
رئیس دادگستری هرمزگان: اموال ۲۴ نفر از عناصر خارج از کشور که با شبکه‌های معاند دشمن همکاری داشته‌اند، شناسایی و طبق روال قانونی توقیف شده‌است.‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435313" target="_blank">📅 14:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnKGi1nKSBfsdfJSKF8qDtrCvkvugXbJcVYUd-8wLRVVxi2-O_RTL83pSSFxxXbx9egqumgTVRp-jiE7NuaccYyOneETSQQ0odGGs2BOetimT_kV2sgkLmXbvbTw9FvKnG_-g4l6SNof2FaMd62jmH1Ou3CKEanm0lEWRWcURLwY_VJctYT0_nC3KvAu2JUnHK6Yun09O28__0CHqTIyzODjdbBvdmP-m4XyGZmC2upRD7d8fNbHAJUGDb2qTmxtbg8Pn5GL5jhrB_QmliOmU_0BERyHmMdBfgKqGcfqtjVaTf0UxuRBt3SQvmmUZsrCiIXD2COesi0TIB6suD2wGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wuf2Jfca8pORNtQ7XRXHiCvU0Wzd3Ai2uWB3NEWH4pE52LK-N7GyZeAwFNhKL3CViNNrAuUP6rRJveU96HjQnVEzimsLIHL3njsiYdWp3qrbDD6PFrA9ularANP00lwagdoscEfYgMo20Nk4cx_bcwsMCG68SN4ySGqE9BLagrRTyGmJ2btwKqBmR9VRPUpGW2b0RTn5Kva1Kel-43R2dTfPi09JYWDoeOw13IFcpJ40dk7bV7JkWhoBnXRn4WuIwZXSQ5qc4d0FDDz3FUuJlCgZDfpVEiOMVj1-vDd0w4ed-V_ro9xdlhiXp45Kfcn1BvhknBWJbKs3g4cf7HgvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laG_DbSSYUvMExeSHeOeyXgtFc2eEX-iEM5fJmpVnCszhN05S2XklOQGckuoO3SDdyPOtSLL_cIENUAhMDUex9SeiT6DH_p905akC1CL10b3hKkP1gF73sTzqeqxn_r67QOFFqpPGzt7_XiPkUGk87G3nyqpG64PGWuvNir0Gq13VnSl3OmtGm64EB8XYwDOyNVjWSWMhzchLXDh9Gqxer7CM-5k9J-6r0emMaRlJHOxSaxPL0-hL00IhHAZzk3TwI8o6MTbGteNI06mxA8NyLfyK8VqKOinEFPOlH5IqZKCx5xW8NqEOtZqDCTTqH7dl7XUiH-d2ROqGdCGhBZ7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDOyuCXF-eWUxIS1eCC2veXFn-sLW49xBdWLAsK9PMqMM5QJjjQyWvKy9hjGqbUTcp9AGboaDBUnJCGY3zzmeePowI7kigK1UHyIVb-1A_kK8xe0ASQ0PNjPR89z1Q65z5RilAoi8P3_Hf04aBhflNMsJg1McoFca18jXZzYObaUQ4HaLugp9W4u-H5NJkQ15L_wRbgjdytH8HBuDIGCCzYg7caVU81kGuDaDl4Y7PfeZRYlWRJAJNkyck6qP9yXPowkjqt-FoqC3WLppILi7s7EXWOXLrjhZY2MLkl5PHIhhbo-4zN5krTT_CztaS-USwnq_K2r2lpF9CRMNwWk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ED-wxZDG5aUuU4drYsHEuo6FdZMzUQLX3dEZmhObxLawl2iKGMvwuqBrPNyDttcFOcwG-DtKCDU0GKMCY98VesY1_HhU68pDMT4vIO4nJ80ONdiJ3Fopq9u9htomtDpxqLChrE1u_O2mTIyGP2fj6g0LYzXtM5effSJko9GJ6PZgxeOng1hy1Cy8dF_cZJGmeYZwxEN53_eqkmsSuMfpg-qGMo3cFS55DbqkzD92YWblg-GfqVUmAkc38UBHJT0vjhu1Tqp_uBjCxfb-t78qdBwrlnbdAeHNDNIGVkFjJECE83D3nP3kcKDEzQwLLJ6T4YEORAd8o4sviM08ZU6QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgGwFPdCiLOeFT9sJc_Xj5bGf6nwPT1cURnI-d8Zpbw40KZlu0Rv2qk0xWQBxDwpim4O5v-hazhdWGn8b8dlJw8ZfJb1Kj4F1fK2WxbPOqNReufPnOb6YsD-OGYW2fYnHVGnMCZGpGyuJ1epG3kUlewn1bMvExOFwOo-nu4s9mrjrTCOl58-ui4FByZsP8O8oNXbtbSmBzXbdK2MeKwynQTrJ5hSmvAImuL7sZ1TFZa-jn901hrukN80xaxqtPfa_ZRyFSn1s9WYWqVDmAM4o_lShQoJgGtvrNAgyrxACmBvnNotPEDDpPMhSuQumd22sxRyO906-ZAqf4Fkl5JC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/havT2bM7H_SMo7lhOctfJNmd6tamyLVTcDQHsIm3Rk_o6AmwJgNzY1a4gpB9sx8YIoTAJFi5ryeq0peLC1vLPdkudwuBwqRfyUsGQ4hww4M4VSMKUQFF-U0sHeV6dSjLIfHk5hRBPdrk0EqXP1AmayJlSTvkLiJZqINZvx0vTXAodA_G33vBtlgLUV-GP_FygoHQCSa2s-bWPGoTHyuGUCwr-9xrRw_uFJqw2pcLoX2OrKIJix5SfBf6R3nA_XD-y0qWezPxT_lN_L1BE-TT19dfL7xVAJ5jNjBjXn04MtonX1IxCjYbKiDqcJp2Rg8rpY0JNdKfd-L0ditEZXySSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzdSDaldtV9Gj0qgcrYt7GH2f2SEW83koqiz4bMvNIrT7Q7mxbQUQlgVAy8TrCKbtiBCj6tkgpjblNof6OkwnU8y_mN1dl1zCLYQJ_39dxal2hpm3J2qFN1rw6GbvLQs596scuoJOQFYWYuVWJg7g2pLcnLjp8zzB0e6aSTnZbz0dtHBhlAEe7YXINORtVAC2bxe4XfTKMlZ4aynUgWWTrlOcIVK6LV7gzjA67jLYlW1S4GBjzy8fDbqRA6vF4Z_YFU7CEoKLXZ-KR0AQy49g93k_4n5zuee6U3Mpex1NIOBdpjFZzKHoXH4uXl3ATH1JzXBY2WQSESgiPx2Krnstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgUMbEI7UHXUBnadUtCntQwujnHZV10fsPNXzl9vRdsvrqk_DbDzblZSlOnAX58hMjNurO720-8KEafqD7pg8aPtDRKRCafhYAyqZzFmQpwUtgFRwNwmQvZMfok6bAKUIZelVr6yoGIUKK9Wd55td2f64bwPA9O2LobT0JapotTh2Ejzk6nYplM7GqgZ-HG5u0qVJaMD-3FDrS7ZfVmjmyxkUKwha5hThtaI2vc3ClmO_C5EB5-j3kBt6BZvSsMV2DokdHGUBVN9fDnzOGnEi8fFLZIcuUMiu6qOSjGXg5ka-6zBvzY_3GOih6qyLK0sRRz4mD6FY-gwqP64LgXRpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از تنگهٔ همیشه هرمز
🔹
بیش از ۱۵۰۰ کشتی خارجی در دو سوی تنگهٔ هرمز منتظر دریافت مجوز از سوی جمهوری اسلامی ایران برای عبور هستند.
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435304" target="_blank">📅 13:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbvmy9A-6TmMQhwmvxhY-T9WcEfRvFB4U_Sw2Ol-LlVWZh9l9QKQfpXPYA2tlaMt0RJDJ7K4zB79SPIAio47xW-T9vLGrXo171UIZl07yAh1T6KPxVFK0mPma8HJCzodWM1jrW1vSSO06lDcjp2MfCs3uSXCH4D_4X7jZoJM7f2EUDUgoHnXcvzWM-JLGSh6bDzcZ_umSdF1N63Mvi0_0TanxzJHJ_kjDOCT61pGCUb8lVMrJc-uQoCnEaK7pVBW20gm8Q8xPDfW8NIsr4Phmx9EnJqG1UAYSdwJNWHSJpP5cShHgPDWYODHtvJAmsD7HDwa025DVoZz07DU8jrfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کارگروه آرد و نان اتاق اصناف: نان گران نشده است
🔹
قیمت‌های جدید نرخ نان که در فضای مجازی دست به دست می‌شود اشتباه است و نرخ جدیدی برای نان تصویب نشده است.
🔹
از دیروز فهرست قیمت‌های جدید نان در فضای مجازی می‌چرخد و حتی در خیابان‌ها مردم از افزایش قیمت از امروز خبر می‌دادند.
🔹
هفتهٔ گذشته بررسی هزینه‌ها طبق روال سالانه به سازمان حمایت از مصرف‌کنندگان و تولیدکنندگان ارسال شده و آنها هنوز تصمیم جدیدی ابلاغ نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/435303" target="_blank">📅 13:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b50a2f5c5.mp4?token=sUanGdkpCoTCi3z0_dDyKSSJ4DBqVXirwe-FnTzb-2Cx1StgCep8ut7I1TByr383w8_2T-8LlPMDUVN1AsgjVg3RMMGS8XtJyI2TMcxPLgybd41GeiM4KbCLD9NREsgPI94U2q6pqPhYNrCh316GtF_ZvkiiaSyE2Vdf0q-eJsu5W75P74kQ7RKbmqUQ86cRMCgpWvxqTSw9BQZaqEoyd84SG31e8PKGoQQAmQIC5uxIhUxk6CF3zD3qyXMl0TWxNvQsFDxR0rUdp4fC0rpEFpYaHieSjkdUT1HH0p2Mi_JuxfnI-3gVcWlFPgQD5rBLnrr8Gd10GmJ9f4HJ9FVnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b50a2f5c5.mp4?token=sUanGdkpCoTCi3z0_dDyKSSJ4DBqVXirwe-FnTzb-2Cx1StgCep8ut7I1TByr383w8_2T-8LlPMDUVN1AsgjVg3RMMGS8XtJyI2TMcxPLgybd41GeiM4KbCLD9NREsgPI94U2q6pqPhYNrCh316GtF_ZvkiiaSyE2Vdf0q-eJsu5W75P74kQ7RKbmqUQ86cRMCgpWvxqTSw9BQZaqEoyd84SG31e8PKGoQQAmQIC5uxIhUxk6CF3zD3qyXMl0TWxNvQsFDxR0rUdp4fC0rpEFpYaHieSjkdUT1HH0p2Mi_JuxfnI-3gVcWlFPgQD5rBLnrr8Gd10GmJ9f4HJ9FVnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از انهدام تانک مرکاوای ارتش صهیونیستی را منتشر کرد
🔹
مقاومت اسلامی لبنان همچنین از انجام ۷ عملیات موشکی و پهپادی علیه مواضع ارتش صهیونیستی تا ظهر امروز خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435302" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXp-6zI5Y3t7qvuZyjsz5AjO9VT1Gns62XroUAykXUhOk0lZ4NXnaH5gbAyIEImsq4Fd2VlIzXCrwrD4Z4MD5_IKTPG46dHy7ApwwoO5OG1MuGl9sqVEy1pORldzEHsKIkS9C1mri3zOY_KxQ5fAOkEagiMXBZhT27wpSPqnA1CJC5yNYBbowk5pBkK6l_P3kcRgOnRWAoC9PSBhwzeesMdH9mn4Hh1URVrxzyML0MXjnQdo_dp8vGb90AskGhSRXzweGBbemg0Plf5QrdT_gx9gPZxxZ4Sv457nqO2MHIBFwLZ0GdOl56TpEiiGcYHoGrmeYJ55F2HIeGYfMYxmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدوین ۶ بستهٔ حمایتی برای بازسازی فولاد و پتروشیمی
🔹
وزیر اقتصاد: دولت پس از جنگ ۱۲ روزه و پیش از جنگ ۴۰ روزه، برنامهٔ جامع حکمرانی اقتصادی در بحران را تدوین و اختیارات را به وزرا و استانداران تفویض کرد.
🔹
با شروع جنگ، اتاق عملیات ویژه تشکیل شد و خدمات بانکی، بیمه، گمرک و ترخیص کالا بدون وقفه ادامه یافت.
🔹
همچنین حقوق کارکنان و بازنشستگان ۱۰ روز پیش‌ازموعد پرداخت شد و وصول مالیات‌ها با استمهال و بخشودگی همراه گشت.
🔹
بیمهٔ جنگ برای کامیون‌داران در نظر گرفته شد و با تأمین کالا، از التهاب بازار جلوگیری گردید. ستاد بازسازی فعال شده و خسارت‌های زیرساخت‌های اقتصادی مستندسازی شد.
🔹
در نهایت ۶ بستهٔ حمایتی شامل تسهیلات ترجیحی، اعتبار مالیاتی و انتشار اوراق برای بازسازی صنایع بزرگ و کوچک، مشروط به حفظ اشتغال طراحی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/435301" target="_blank">📅 13:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c9b569181.mp4?token=QJA_vfmVElubfzLTjElvt7_6_iCphnvDb_Wm5nWi3uBFR95Y9vWCLtISz6Ik8fmeiVRrqc88nvthpC8rhWZWO10nhEhV7ZK9b4EGzSQNMWHDkAj0UUs-ZNcYWGxYXLKb-4W-C8t7yndx4HFn_89qTMtR5kFTr8lz58LSZNRW91FiNiuA6RAw9q3-Sq2m_diLiJoS7FL2_LeqVwfnuiS5G7DXh91jcyE6dkrnljF-mK0_-32xk1RGdFjMGuZBW5ulG-ZBsux0Hsmma2Y86gLRFDPHJX7z3_P2X_43U3OsXiWr2cGOIm31gbulvCxBhlUFzY3MrZDhDyS0JiAhDXjNCywrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c9b569181.mp4?token=QJA_vfmVElubfzLTjElvt7_6_iCphnvDb_Wm5nWi3uBFR95Y9vWCLtISz6Ik8fmeiVRrqc88nvthpC8rhWZWO10nhEhV7ZK9b4EGzSQNMWHDkAj0UUs-ZNcYWGxYXLKb-4W-C8t7yndx4HFn_89qTMtR5kFTr8lz58LSZNRW91FiNiuA6RAw9q3-Sq2m_diLiJoS7FL2_LeqVwfnuiS5G7DXh91jcyE6dkrnljF-mK0_-32xk1RGdFjMGuZBW5ulG-ZBsux0Hsmma2Y86gLRFDPHJX7z3_P2X_43U3OsXiWr2cGOIm31gbulvCxBhlUFzY3MrZDhDyS0JiAhDXjNCywrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اجتماع دوقلوهای شیرازی در هفتادوسومین شب اقتدار  عکس: احمدرضا مداح @Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/435300" target="_blank">📅 13:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907dfc0cea.mp4?token=oPDJi_LSw8pNwLNqgoWwKexEMyk7qCF-hpB6rOjNqGwglh1Pm0enlBJEY6DAs125sajwJAji2ueSiWzmrPOdXUeCxoo29NAVbrJvB8sRMRIVYqUCiZBlPOhJLlnH7eEdUs-aHcbYp90cZc3OEgrmCq1DcrjbHZcwYEFwVDuEj-KTcmuydWkGrUYfIbZWQptXuZICxZ15Mr0tWNQFDeVVesTgTUockgmm3YDpRnP16mKRkvq3Rf5HSIbU_HSUOiA0NM0rzSBEOEZhSQ8PoZpUssTKHQ533tFsK2U7FC3YOfy2IDkCYR7g_c21VvI26axr20d_mWgJ3pds3sW46ePl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907dfc0cea.mp4?token=oPDJi_LSw8pNwLNqgoWwKexEMyk7qCF-hpB6rOjNqGwglh1Pm0enlBJEY6DAs125sajwJAji2ueSiWzmrPOdXUeCxoo29NAVbrJvB8sRMRIVYqUCiZBlPOhJLlnH7eEdUs-aHcbYp90cZc3OEgrmCq1DcrjbHZcwYEFwVDuEj-KTcmuydWkGrUYfIbZWQptXuZICxZ15Mr0tWNQFDeVVesTgTUockgmm3YDpRnP16mKRkvq3Rf5HSIbU_HSUOiA0NM0rzSBEOEZhSQ8PoZpUssTKHQ533tFsK2U7FC3YOfy2IDkCYR7g_c21VvI26axr20d_mWgJ3pds3sW46ePl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار ابن‌الرضا سرپرست وزارت دفاع شد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: ‏با حکم پزشکیان، سردار پاسدار سیدمجید ابن‌الرضا به عنوان سرپرست وزارت دفاع منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435299" target="_blank">📅 13:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435298">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه آیت‌الله بهجت ۳۰ سال پیش دربارۀ رهبر شهید انقلاب پیش‌بینی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/435298" target="_blank">📅 12:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435297">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsld1YkgTx8jspM5HbBbefUHv-vVOwpi0IIJJRfbquGdEiBpGYgXxqIVHlieHUoVydAEq7DoAmzxmFf-zx_pilgjEZr5ZE-2Xsx7iO1BxPOWCmC89bt4OSOpmxiWXeMa-vHZBBSxXOUVWBf7NeIKpQcM7MxvqAcfGSIPueHul1dJ6DGN7uUnPoH4-r9jf-CYdyGJD3Qyzib7rcDsXJVGsLmHYUsvvr6WzBoh4CPzNn8a6AwX57sJRqolYWhFEXyWKvVlrmft0-xyGTdwO9W3iJ6I4I6CD2i2P6KBHhqA11GOm0gIkDIeVe53g9Nh18eX784n-3uW0h9RtUyxIkLaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت اربعین شهادت سردار سیدیزدان میر
🔹
مراسم پاسداشت چهلمین روز شهادت فرماندهٔ گمنام جبههٔ مقاومت اسلامی سردار سرتيپ پاسدار شهید سیدیزدان میر (حاج اصغر باقری) و شهیده دکتر فاطمه‌سادات میر، جمعه از ساعت ۱۷ تا ۱۸:۳۰ در مسجد شهید بهشتی تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/435297" target="_blank">📅 12:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435296">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9v4bG0UF93QRNqbRzNVIsqn6eDgdqmLjk1P4cqkd7pxRmKxBOIjUVxJJr1cjizoTVslLFEkg2SSKa5Q0ctkujOqUY1L0S1cZDQypWDVqLC94uRT3PiNuTzUAv3Kf8uFDuXW8BVNAySD7TPvviCYLML89rU2EXXg5tmY-fq5puUns6whLi5fJHrbtKXsDa2ofsJkKBorejFxr-QUeiocWpH2Oba7kTC6d3pKHx_0m4mPBXGzmhTMiHjCMC_caqPKmRQEQYjJ-yEhbJQFB1Zy76cIEocWxrtuNPNX7h1xqSOYv5aDgPkb4iDOfXgb16M-0uo3og2cbqUbO3M-wA8iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای مجلس و مرغداران بر سر مقصر گرانی
🔹
نایب رئیس کمیسیون اصل ۹۰ مجلس، وزارت جهاد کشاورزی را دربارهٔ گرانی مرغ مقصر دانست که با وجود نهادهٔ کافی، جوجه‌ریزی کمتری در فروردین انجام شد و تولید را کم کرد و قیمت‌ها تا ۳۹۰ هزار تومان در هر کیلو بالا رفت.
🔹
این درحالی‌ست که اتحادیهٔ مرغداران، کمبود و گرانی ۵ برابری نهاده‌ها، خوراک،‌ واکسن و دارو را مانع جوجه‌ریزی اعلام کرده که تولید با هزینهٔ گران برای آنها صرفی نداشت.
🔹
بر اساس آمار اتحادیهٔ مرغداران، جوجه‌ریزی مرغداری‌های کشور در فروردین ۱۰۶ و در اردیبهشت ۱۲۶ میلیون قطعه است که این میزان افزایش جوجه‌ریزی ۴۲ هزار تن تولید مرغ را بیشتر می‌کند و نیاز ۱۷ میلیون نفر را در ماه بیشتر از ماه قبل تامین خواهد کرد.
عکس: علی‌حامد حق‌دوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/435296" target="_blank">📅 12:13 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
