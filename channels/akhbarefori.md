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
<img src="https://cdn4.telesco.pe/file/AfcILezzwYHZNbc0Dx8ZI4rh_G7jP7EZhqh2YyOliUjfgbcxjyJMKypq7wSKu4pSd-wrF4rtE_deyZJ6ctpkShhv0gmna9R2gJ0VAC7_qJgHwC08KcIhl8-8J3cMb8q2XhR3I8SXzVA90HaDHfRrGL-tEaD3PmjttuiPF7AWGsr8P3FadUyhsfo2VcCje4MmdnsPuw2mBcMPx7Ppm7Hy7OOBZZ4nJgj1i0u3D72tABB2DLJgnHbnnBbqcjjXNZYiagMlhg1Jpf1tv_0BEdG1FaUcvr1gdsURiJ-HbUojLzcCBBFmcPSKERcshazC4hgVaxMrpMDDnGHtxd74vBHF8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 16:02:47</div>
<hr>

<div class="tg-post" id="msg-677723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خبرگزاری عراق: بیش از ۱.۳ میلیون زائر ایرانی از مرز مهران وارد عراق شدند.
🔹
نظرسنجی سی‌ان‌ان: ۶۷ درصد آمریکایی‌ها می‌گویند تصمیمات نظامی ترامپ در جنگ با ایران به آمریکا ضربه زده است.
🔹
گرما اداره‌های خوزستان را در روز چهارشنبه دورکار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/akhbarefori/677723" target="_blank">📅 15:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677721">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: نباید دور کشور سیم خاردار بکشیم و بگوییم در همه حوزه‌های اقتصادی می‌خواهیم مستقل شویم/ در بسیاری از حوزه‌های اقتصادی نباید خودکفا شد و باید تکلیف خود را روشن کنیم
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
بالغ بر ۹۰ درصد مردم بر روی تمامیت ارضی و استقلال سیاسی کشور تعصب دارند. دشمن‌ترین دشمنانمان هم ما را متهم نکرد که تحت تاثیر فلان حکومت خارجی است.
🔹
می‌خواهیم کشور نفتی باشیم یا خودروساز، فولادی و یا معدنی. اصلا نباید خودکفا شد؛ خودکفایی با خوداتکایی تفاوت دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/677721" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677720">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
توقف کشتی حامل گاز قطر در جنوب تنگه هرمز
منچ‌اوسینت:
🔹
کشتی حامل گاز قطر که تحت اسکورت آمریکا حرکت می‌کرد، در جنوب تنگه هرمز لنگر انداخته و متوقف شده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677720" target="_blank">📅 15:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677719" target="_blank">📅 15:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای آژیر خطر در اردن به گوش می‌رسد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/677718" target="_blank">📅 15:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqKYMJULmBwAAz1Za5G8HBQXrhjXWQHR7fy9JRMyNeTapc22yZ_est8pDK3_H4HZu1qRvrIAFuySjTpxJzKuEgr6TRT5dmwn0mUQju76z3UdIexWbWg6ZNNaZlQ7JWW2LqfrEvpzjbUzhlpw8DGRFefIS0XpvYIp7VGGAKkFLb5ESHG9FySWn2tjB1QrWU8zSApPl-qQUOextwrWUMIerSoS-aEMQ1iMoHVOPAYBL2jNTwynR8AXPU1mL-erfq7-mugQj62v3zOJFYJOphdcW2KM2njxQjf_O7efHKIgk9OE15lH8ZAUy8WlsUBOQcxIqt0--kxQFfclitzh-PTCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکرار ادعای جنجالی اسموتریچ درباره تحقق «اسرائیل بزرگ»
🔹
بزالل اسموتریچ، وزیر دارایی اسرائیل، با استناد به متون دینی ادعایی، بار دیگر آرزوی خود برای تشکیل قلمرو این رژیم از «نیل تا فرات» را علنی کرد و گفت امیدوار است این رؤیا روزی محقق شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677717" target="_blank">📅 15:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نماینده مجلس: ۲ تا ۳ هفته آینده قطعی‌های برق تمام می‌شود
سنگدوینی، عضو کمیسیون انرژی مجلس:
🔹
تاکنون ۵۸۰۰ مگاوات برق خورشیدی به شبکه اضافه شده و تا پایان سال این ظرفیت به ۱۲ هزار مگاوات خواهد رسید. قطعی برق شهرک‌های صنعتی به یک روز در هفته محدود شده و تغییر ساعت کاری ادارات نیز حدود ۲ هزار مگاوات صرفه‌جویی در مصرف برق ایجاد کرده است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677716" target="_blank">📅 15:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحول دیجیتال در قلب شهر مشهد
🔹
شهرداری مشهد با اجرای پروژه هوشمندسازی کیوسک‌های شهری، گامی بلند برای تبدیل شدن به یک «شهر هوشمند»  برداشت تا دسترسی شهروندان به خدمات شهری سریع‌تر، راحت‌تر و جذاب‌تر شود.
🔹
تلفیقی از تکنولوژی و زیبایی شهری
https://samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677715" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترجم کوچولوی موکب اربعین!
🔹
این پسر، مترجم فارسی یک پزشک عراقی در مسیر پیاده‌روی اربعین است و با ترجمه‌های بامزه‌اش توجه‌ها را جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677714" target="_blank">📅 15:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCRI5jrNYkBQrPWY-myyBT90gKo01EzAdwBIouQSRLHZEyFg6yP4x--CoGP5RQ32RA_5JmamTWoXuy1LnOjDlvpTUGwtj70o2O4j3lFV7CzuPYkgiJQTXWe6A1J3p3_tGkM5Qz8KLGVKcTxwgm1S7ackdHczt8TToK7z9SWdmhe3kUd8tSQ_tykeUiUtC6ZHtHv_hW9lfEU0PYl7RJ2VLFVakPEhKJAj3Ek6My5o3ykPrHOWB0eGTZhHXnWIerCo9Pqdd6cL2XG6bABpho19BTKfD3Wqtw1-LdRa5nqQR0zToktEMAvCOt3055rrK9MF2446eV60bloikR2xed1ajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
من حاضرم همینجا بمیرم  ولی با جنازم یک متر از این جزیره رو حفظ کنم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677713" target="_blank">📅 15:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ستاد مرکزی اربعین: زائران برای کاهش ازدحام، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.
🔹
۵۵۶ هزار نفر در صف وام ازدواج؛ بانک‌های متخلف به دستگاه قضا معرفی شدند.
🔹
محیط‌زیست: آتش‌سوزی جنگل‌های باگ و چناربرم پس از ۴ ساعت مهار شد؛ تعدادی از درختان ارزشمند سوختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677712" target="_blank">📅 14:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
جهش قیمت مواد غذایی؛ روغن جامد با ۴۰۰ درصد رکورد زد
گزارش مرکز آمار از افزایش قیمت اقلام غذایی نسبت به تیر ماه سال گذشته:
🔹
مرغ ۱۹۰ درصد، شیر ۱۵۰ درصد، ماست ۱۳۰ درصد، روغن مایع ۳۴۴ درصد، روغن جامد ۴۰۰ درصد و سیب و موز ۱۰۰ درصد افزایش قیمت داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/677711" target="_blank">📅 14:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcAwtxDyoLI9cRXl5QtRrdHJnivjK2JgxShj4FOqqBJebHFRbh7jDZ13nrZdsLCMaYdqiQh2sJ8IyIKLpvHWe_d6hiNiJv5Ic4WLJb95hJgjlNjFS_ikkAF8HwqFr6ytOGfbg1sgftOeb5p5bkQozHAbHozN0ZmMjvgDYksIjvNDQV_4OEXMthBAVM_FZ11e9zZdNky4rTUPJ-H3VrY5ELxnoiSVasE95kXY5QG4YxLEsLNIGnzWqD_iIBu5R2u-ysKvP149wJpgg7EaMcDZ1NDyJ_IoxmJS1P0yahROVcq60pLWsOaP2pj7uFaVL3XLYTO1CAcq7FrUZb8SDXBM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورتی رو با کدوم رنگ استایل کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/677710" target="_blank">📅 14:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیافت هوشمند پسماند غذا در مدارس چین
🔹
مدارس چین با سیستم‌های هوشمند، باقی‌مانده غذا را به کود تبدیل می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/677709" target="_blank">📅 14:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📱
اینستاگرام تمام پست‌های عمومی را با هوش مصنوعی تحلیل می‌کند
مارک زاکربرگ:
🔹
متا با استفاده از هوش مصنوعی، تمام پست‌ها و ریلزهای عمومی اینستاگرام را از نظر محتوا و لحن بررسی می‌کند.
🔹
هدف از این اقدام، شناخت دقیق‌تر علایق کاربران و ارائه پیشنهادهای شخصی‌سازی‌شده‌تر در بخش فید و ریلز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677708" target="_blank">📅 14:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی در دریا؛ آتش‌سوزی کشتی مسافربری در اندونزی/ ۵ کشته و ۴۱ مفقود
🔹
از میان ۲۷۱ سرنشین این کشتی، ۲۲۵ نفر نجات یافتند و عملیات جست‌وجو برای مفقودان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677706" target="_blank">📅 14:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از حمله آمریکا به یکی از زیباترین سواحل خلیج فارس در روستای بنود عسلویه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677705" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5TztulqKy8fytx3dU7ZdMUIExeZh1EHp0aqQWHuvp6vyHK5uRll5edBr-7qGrDvMqODXE4LDTJVejHFlJUGG_BhNYDZcID8jS27sBC0dOCHnb46h2Glh4gcN6Lwm_SetzGyQUzfaOvsrelLrBJVGJuDpFjbD8sOQ0hb3KmlNPu7mKo9xmTqOpaQQ1-OcjjaYLTFkzCr_x-eH-pT7adlQCO2-94rtUKukuFwNt1YZSN0fXOGbFzbIUXdIIt1y78ypR63FPKXth95tRWmkX8tLtpf86KidR12wvN5Lt5Rkirjzh5PpkHMO_w6WNUU9V0sZkEOhyO3h9CVB44M1vkA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲۸ هزار تولد تا ثبت جمعیت ۸۷.۱ میلیونی ایران
🔹
بر اساس برآوردهای مرکز آمار ایران، جمعیت کشور تا پایان سال به ۸۷ میلیون و ۱۳۴ هزار نفر خواهد رسید؛ برای تحقق این برآورد، ثبت حدود ۱۲۸ هزار تولد دیگر تا پایان سال ضروری است.
🔹
بیش از ۶۷ میلیون نفر آن جمعیت شهری و حدود ۲۰ میلیون نفر هم جمعیت روستایی خواهند بود.
@amarfact</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677704" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnNQL5nQDlR_lMtbEE5XrgiGM2ySQhZsnmmOU5sxd46VAhWwmlP-7ZOB2c_m6N6f-ZSlce4SX4W4nIbSwSzmM1NPk4roYP4ynWeCzvymKP0Z3HWN7X5u0wxjSq1BBebJ6bmTDnfnU2UFwW8JkhDUrZ1J4_qzRInyP6VPO6xXfibzOXWWGKIKq-y3xo98hw7a-KYOGkIgKGCGffN5w6cfIDWnbiqbjNdW8vIIlphkMLGfH0fqp-kfkbWupS82agJ9KEjFlV6ggN7z7-86RFTs6JvZaEQFDFtEV2SQfURpm2X8GxHj9HQmMhSdiGA0Xmyy3NYyLGajD2hxGXhv_PhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاشینیان به عنوان نخست‌وزیر ارمنستان منصوب شد
🔹
به گزارش دفتر ریاست جمهوری ارمنستان، واهاگن خاچاتوریان، رئیس‌جمهور این کشور با صدور فرمانی، نیکول پاشینیان را مجدداً به عنوان نخست‌وزیر ارمنستان منصوب کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/677703" target="_blank">📅 14:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای بهنام راعی که با داشتن غرور جوانی روزی به سینه پدر لگد زده و چند روز بعد بر اثر تصادف روح از جسم جدا و در برزخ شاهد عذاب و شرمندگی به خاطر گناهان دنیوی می‌شود ولی در نهایت با دعای مادر و عشق به اهل بیت در کودکی و شرکت در مراسم عزاداری، مورد شفاعت قرار گرفته و فرصت جبران و زندگی دوباره به ایشان داده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: بهنام راعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/677702" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVvz2QPkRmjm3Fs8pbtvC94ttrFgzQVIWc9sEkbL3L1oGa7DIoh42zqRALWxrmVnoN3_42FGL2bAlDWwJ3cgXNpU-4K-0cGgGfcGMS3bPwA75KSYuH-eqkEBuxn1JH0hoUo7PjYVLgM7daAOIHWnDfmLziPrQrDHOWG-WLyNWyP8f0mGcMMXxn-dBS2dQ_9tBqjgMaK16s8Ou7lfHxJs97qy7q83hqRiEUe-NC7HUEpDu7_0pSBbgk21R2kH1yqD1WQLnbWiYI0W8iOo2rYWZ_53oSm9l0oyhLIeLXOqXiC7-hc5PI7zc5IPtfOB3Blqtn2khzP9H5lzhjnxYEW7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی با انتشار تصویری طنزآمیز، نوسان در مواضع و اظهارات ترامپ را دستمایه تمسخر قرار دادند :)
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/677701" target="_blank">📅 14:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677700">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: عده‌ای در کشور می‌خواهند مذاکره را ممنوع کنند/ دشمن‌ترین کشورهای دنیا هم در طول تاریخ با هم مذاکره کرده‌اند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
پاسخ‌های ما به آمریکا باید پشیمان‌کننده باشد، اما هیچوقت در مذاکره را نبستیم. تجربه گذشته نشان داده به حرف‌های رقیب نمی‌شود اعتماد کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677700" target="_blank">📅 14:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای رسانه‌های امریکایی: در پی درخواست‌های وزرای امور خارجه ترکیه، قطر و پاکستان مبنی بر آمادگی ایران برای برگزاری جلسه‌ای در ژنو، سوئیس، به منظور ادامه مذاکرات، فرماندهی مرکزی ایالات متحده به طور موقت به مدت ۴۸ ساعت، عملیات شبانه خود را متوقف کرد
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677699" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677698" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «دقت» به اجبار تبدیل می‌شود؛ OCD چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677697" target="_blank">📅 13:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5GrWY_fnHdrYV1ga5VXVto3_fyBAfyY_eUzVLncOYqLyHtxPoeVWCMO80w0k8d37hjsIvEcmwdg-gNUfmTJQKpxFpWVbIiq6Z0ZaGqEJotxa4w-Pqqyl1aZF6pSSsRaS72rEQelANGPoApmxOs7di1MgRkjjp5GTQXrLS-IHdD3ao4BASslPWwJWM110FPtrVfAORPSNEOIBnftVBNyKMWYqGssVLCzgJWdk1bhI5QzKtUYGSLG9s3NqjRToCzbSwdWjMi9zZRJCu6vuvvy2i2z_xfKkQ1zV-f6n1RJYgySsAf7baQeBTYadc_aPRZyqBVpaaH8Nfux8Xw2fDstrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
شاید چیزی که اضافه برمیدارید سهم کسی در انتهای مسیر باشد
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/677696" target="_blank">📅 13:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s42DuIKmwa82Fjnbbf2mPji5r7i_ZMiWFK1JKg-foq04IxAD7rz0suLAFloy2AumMawBhDXtZE0ke4FtWJ3o9m-L1H_nR1w_qhQn83FxnuH8a6jsnIIliDxSNvW3FWmLH074oe81cG4_IrOm8btzofK7sRbTrevqiHMn0yo-1k3S4x7elbsTc43_U3jn7VfxRXtO3nYs7eZ0fsvB2DFFokTiIJOWA9bcRG_bjPkzvYFSLdvc6UPLGZnrOH5Thtd3R6b_pg5J6tyC03dZXVrGcLCdOzCfk9TYXvvKTi3iy4MRwUMEYphKsrWfvZqb_5ofnFzRfJ3h242fdd65AX3RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر اقتصادی: هدف ترامپ از اینکه این همه تهدید می کند و حمله نمیکنه اینه که حمله به ایران عادی بشه و دیگه قیمت نفت و بورس رو تغییر نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/677695" target="_blank">📅 13:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/677694" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBS63rHMtYv1iC2oT2es9cN6FRlFMOgX0eqBD01WMvm1cxoBntxLS2jPGlY4khxDYYj0WfIi3vCP2zcW3fA2rkH1JGbfGd0arv4yic2s1Zvw25axyH1J4k8w-UEPtT8Sh3svzHZ5PrjEVYvJ5Sa29Z5CR1GH3AOMew7VTqG4IZK0ftmqvdVcISNhZOuLOgEH8sG3uJmENlNAYkkA4VZtbvmKJuXrKzDToXHXgkZJvBtiHj4ByOG-i6PxChK5BUMJO1I2PxyHYz7wZU_lCcfEdo1AagRzmMoq8JIWrjALTpp0CJkZU5RcVL8lFctrPvjLaP2wycXMy3CS2dMEOR6ZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای در شرایط جنگی (۲)
🔹
اطلاعات نادرست در زمان جنگ می‌تواند به ایجاد ترس و اضطراب در جامعه منجر شود. تکنیک‌های سواد رسانه‌ای به افراد کمک می‌کند تا منابع معتبر را از منابع جعلی تشخیص دهند و اهداف پنهان و سوگیری‌های پشت پیام‌های رسانه‌ای را شناسایی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/677692" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677690">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmRh1j-YdGleYNJTgXESE9AhJETR3zF5kBiZyKjY-aPGjTL929xbaurHWNjJxd2IPU48bGW11sfOb0KOTZOz3EZpguS-XUVRSE7U9yiAxKbexILGQuAMb0eKXkksbHrVl53Yohyuankh4HK_hcv5tdjqtxwNMKXEp2P8HEmTjQSLZ-0YwEIWCw7TK0QMTKSqskW2c3T2tscO8QnJhZHWPVOWvY6dsaixPOktf2Cp6ale9OmRNvBBNzIYDhCX1G0VmoygomE8Q1bEWrPHNDFzYcZnM2I39DGrc5YqpcuwR1-m8et-DWSUBLRSOQAW4YKEvH3vsWipY6acst5lV7T44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTcGCunXKQyUh4Aab6HjpGuJnh5kReRccof0M5YJ5kKi907qrBk5NmEDqbN-3cIh1hAkVffnYV5jFekZc8N0cF_H08q_-7S9FJF7BGOrCzydzVK9GxUIZbePQzjUviGa5d0eWaMoTCN2QOu7HCuxN_hOLxVFDWtlNxaxCilkF11t-8bWS3I6MWkXlVgtwpP5y7qUSKBYAOQgVLo2kK6YhA1Sni3cBB0cBSSYlCKO5kcBkCgeJiRw9I2xCQdQLce-e6weP2ZZuQguy_uguLAgzngpwro3wVtPWQbWqa5nXgoqDUV93PuMEj1WgokaarPWnPEKC80r0Z1D_HYXyRXRwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب دکتر محمدطاهر ابوغریف را در موکب نداء الاقصی دیدم. همان پزشک محبوب کودکان که با نام "پزشک معجزه‌گر غزه"در جهان نام‌آور شد. محمدطاهر عراقی‌الاصل و ساکن لندن است اما خانواده خود را رها کرد و داوطلبانه ماه‌ها زیر بمباران وحشیانه‌ی رژیم صهیونیستی در غزه ماند و آخرین جراحی بود که آنجا را ترک کرد. او بیش از 300 عمل جراحی پیچیده انجام داد و بیش از 1200 مجروح را درمان کرد.
با او درباره خاطرات و مشاهداتش در غزه حرف زدم. هنوز عمیقاً متاثر بود. احساس کردم آنچه بر او گذشته دورانی از سلوک معنوی شخصی را برایش ایجاد کرده. او به آیات قرآن پناه می‌برد و از "صبر" سخن می‌گفت.
گفت حالا دیگر سخن از دوگانه‌ی شیعه-سنی یا دوگانه‌های دیگر حرف زدن جایی ندارد؛ دوگانه‌ی اصلی "مقاومت-تسلیم" است.
[ان شاءالله گپ و گفت من با دکتر محمدطاهر در تلویزیون پخش خواهد شد.]
✒️
#روایت_اربعین
۹
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/677690" target="_blank">📅 13:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677689">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1d20dfca.mp4?token=QH6RHmrBt7lN-aypqTh6KgV561gmFFV8Gm_4HNx228GIO4cQWnyD_RbNXNCFexX0bIHck6ZZ-vYvome5-w0Q2PFLElSIN5OZWwwxfKa0OV9Ydtpgwm2U6l5g2kqrFkxew49jSJgH5LmH6_KJEsWwMVfb7AXDo46YyHUyl5_cTN50rs49ZiZLZfJQ09-4EzIgyXnA-a-p5d19kFDxixyVZQU3bIWFRENnJ8R_zbHsvvDpYlK32qyxCzholbofjIMNtNaOD7jniocQulYeCcoK_uBT3p6eyRTeF9HKSq6ZuidfuRhLZpc6RfYnlMjkdIldbABdzau75NY-XZHluNMgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1d20dfca.mp4?token=QH6RHmrBt7lN-aypqTh6KgV561gmFFV8Gm_4HNx228GIO4cQWnyD_RbNXNCFexX0bIHck6ZZ-vYvome5-w0Q2PFLElSIN5OZWwwxfKa0OV9Ydtpgwm2U6l5g2kqrFkxew49jSJgH5LmH6_KJEsWwMVfb7AXDo46YyHUyl5_cTN50rs49ZiZLZfJQ09-4EzIgyXnA-a-p5d19kFDxixyVZQU3bIWFRENnJ8R_zbHsvvDpYlK32qyxCzholbofjIMNtNaOD7jniocQulYeCcoK_uBT3p6eyRTeF9HKSq6ZuidfuRhLZpc6RfYnlMjkdIldbABdzau75NY-XZHluNMgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لجستیکِ غول‌آسا: هنرنمایی تریلی‌ها در مسیرهای باریک
🔹
پره‌های غول‌آسای توربین بادی با طولی تا ۸۰ متر، به‌دلیل ابعادشان نیازمند تریلی‌های هوشمند، برنامه‌ریزی مسیر و گاهی بستن جاده‌ها برای عبور ایمن هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677689" target="_blank">📅 13:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677688">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwDMaeUIQYY6As0-6sckc3S_bS2H8mzdKclSj5Yau-4g2GR_eYDTbreWx7QLqgVsh7QLdIFKFe_MK9ovDEjBN_3dBUYM_h68mY8XsX6w1MEaLJm5NPNuZJ1mNpPr6aoDFqLHs-FcwT27JenT2yq1QpPEGMWS_QyYV-sHt5cEao3Px994ybZW917Hjm31EEfBiUxj7SJuNs9vQKSgwjYcF_Z9Ifu0L0evzSuQaX5KP1KtnvWXzubxgj21B1OkoJlqxRWy3L85s28fA-3ay0zDN-W0rgqx2WBtI8Ew07M-sGA1f54SeaR3hBFOj5Tm7w2PpawnISTN5A0z165F1GJWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌اندازی رشته «تولید محتوا» در دانشگاه‌های آمریکا
🔹
دانشگاه ایالتی آریزونا رشته کارشناسی «تولید محتوا» را راه‌اندازی کرد.
🔹
دانشجویان در این رشته تولید محتوای دیجیتال، برندسازی شخصی و مدیریت شبکه‌های اجتماعی را می‌آموزند و برای فعالیت در حوزه‌های بازاریابی، برند و روابط عمومی نیز آماده می‌شوند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677688" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677687">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5RHUv-pKMEu2bdEg6HeUhB9ReOWPcO1QC7QoPOwLScCCAoQTPJsLj3JhvlPtabWl6yvs41Yx8fGkkY6KADTp9F1ytI6ZWdUZ60JarJYvS4-UilWWtAmxkCxIOsYa7QtDtlt9JnVK_CI_rXJ5FJs9tb9j6-lmmbtbxD6YIQHMrd9AvaVlOgw9jvdtYhgFhnTXYAUqfuWJv79kL_CBei1z9l3xuUf-hQTzFt_uisyxWoV3KZ_sVa1Rj_lfWRup1-YelksYUTEcez_moWd-Fb2yg0I2YVRyXR4kzy3H0b4GpmzpvVJwmkufHaTpc6DzwOG_9Ni5Ur1jJqrmqZZ-PfCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه استقلال: همه اقدامات برای بازگشت نازون انجام شد/ ادعاهای مطرح‌شده خلاف واقع است
🔹
باشگاه استقلال، ادعاهای اخیر داکنز نازون مبنی بر پیگیری نکردن این باشگاه برای بازگشت او را رد و اعلام کرد که تمامی اقدامات اداری و هماهنگی‌های لازم از جمله اخذ روادید، ارسال مدارک و پیگیری‌های مستمر برای بازگشت این بازیکن در زمان مقرر انجام شده و مستندات آن موجود است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677687" target="_blank">📅 13:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5VVE6NXKsI9ZHcmwya34hue9HkE_JCxQ7QN-BhjRodVbqw2pkNjhc6HXlRyb4c6j-kcG9afq1NLXk4x3G-nFG5ew6RM16CkCtblNF18Qdi-Lc_3wpVBfoOnd_foyVVD9c64MHjr0GjrKqeS6puBzRPW-DkQnAGrkDMAkB2Kpsc9jCx4EejiQdynrS0X_LEgBlp8ZT2BUixwKBPl7xEbsAATcJyZXgnlH7prju5pgVZ5pj5qE2QztglBCGDxyzD1BK96T1u9WyxzHrYLQ-uo8oApnuDPd2--0SwvGp27u4qsatQnJPxIwiJ9ZB8Mnw0Eb4PKGQ46IcdFOSZlx1faNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSPAHmdBMPxd8lgtCopwLQB83ND3PJoFpyTlZ1043UAHjg7t8ahgExG8d3_TyJew5WPTckYoDlw31ydxahScZSqRhOmIgwZISXBvj5HZ0VsXBEqXy7-RSvEWXCnhFcBa6QNvQOt9dqdUiZQddoVFGCJ8bDvYdxZ4s0hMY-zexkYMV5yuQjpeowuxJYFjRJeLaJNr1ePBCBkfP8kQeRa2zjjZ1i4ydxc4tcImgGpMPB7uAhQUgG661jsmcb7F_xMrZEHLWeM5BztJ3Tf84l4tIkPpdblbfiq9sjYjKqpRj0Zz7OZ2Td-c7m2Jzw8qC5UTt84Uy37MogQCF8nElCy4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qertR3RR6YZ9cJCKs6iwshF7Hlq75EFTjwonwt-NaXwLGXhBNeXIXPPcBkPYkibJZryzXahHMewFyD1q5Y8S6wCf5oAFt3McinPcoD6dDKdXnD4u_5WtLYlLzJQHAmRQT0Zj0-AFKjgnn5hPiC18j_2LeaGRqf3kM4KELtAU24s-yYgk8FkYYb8XbQLx-KJ_tWOzR8Toeyx_S6khQDSVich5aObcMAT6_CbNscPq6_AWaWoYpQ5j2tf7XLVbceDr71_cvSO9hJDq-ZDWn9ToJLu5GMX_sfF9H7X7JHH9Ekg_G-_cRB2yJoj_rQF_k8d7UjM0sPXV-HjRIv00c5zNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIkar2NwcdSL3sGmw7lkA9ToJ11-WHkHIdJUB9jrwS_ujxW76V8LICnSkQiHSdLf2iOeHAxgqz2xfoW14vFaZhekOvqa1sSloucS48bYPAmETM5Nc2u0eFuYvhfc2YE20D06ZUdn5vipHjZJB-Mwu1QaIxj5N3ZpaMM0K7HqjVx9_Q9nplvLZihqdEyFPoZ3pe_UUI-ZyGXiC7lLyOlfybwFCcLcR0oZzRXbf9B_ufDjO3wnepzoV9mrJPVp-GrqY5MYL80BTyTOfInBsbTrY7_tjTTcofBL7sTlZl_csVrnL-IBq4aOAbDV8i3PDiSMGkGT-63g2vs8f3eAGGh2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwcGerT56m9NGLnePFYzMQjIVCZ0XXV7fzrufuehk-z6o6O8a8NSr3Iv5ly1ep3ScUbMOvzrfc3HqS_B9zEiQbjDBQoNiX0w7aAXyfm6mt7jyxi0bP198TlAYn3V-3LNNc5k72t2cQU9aFsZNvF5r9M3UmCHjknUxFf7TDrIQe8-5WXbcKnSYNLVE2oSxQLY_Y-kib6jmJn7Hf2ycWswnU8Xz0ZBxNON9TMUzm6QSijC6J5Y1fhacN9Up7nalWZ32gyLFiym6NnZJE5yZpntQZn9Lh54ITe02Hr8PV7Vy8Jw38_vyhASZf-tVSKPhSXl764rO4Tf3-VXSkJxgK_2Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">؛
ارتش حرام‌زاده‌ی آمریکا به دستور ترامپ برای به شهادت رسوندن این خانواده از یک بمب ۲۰۰۰ پوندی «مارک-۸۴» استفاده کردند؛
بمبی که طبق ادعای رسانه‌های غربی توسط رژیم صهیونیستی در حمله به مقر شهید سیدحسن نصرالله و ترور ایشون ازش استفاده شده..
این جنایت همون «اقدام بشردوستانه‌ایه» که پهلوی از اون حمایت می‌کرد و خواستار تداومش بود؛ حمله‌ای که نتیجه‌اش چیزی جز به خاک و خون کشیده شدن غیرنظامیان و خانواده‌های ایرانی نبوده و نیست..
و نکته قابل توجه اینجاست که خود آمریکایی‌ها بارها ادعا کردن، بمب مارک-۸۴ بدلیل داشتن سامانه‌های هدایت دقیق، از دقت بسیار بالایی برخورداره که احتمال اصابت به هدفی غیر از نقطه تعیین‌شده رو غیرممکن میکنه.. به همین دلیل یک بار دیگه اثبات شد، جنایت مدرسه‌ی میناب توسط ترامپ و ارتش آمریکا اتفاق افتاده..</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677682" target="_blank">📅 13:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
مژده لواسانی: کوچکترین مزارهای دنیا رو در گلزار شهدای میناب میبینید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677680" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیدی که بجای سردار رادان در جلسه شورای دفاع شرکت کرد
🔹
سرلشگر شهید «غلامرضا رضاییان» رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» که به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و به شهادت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/677679" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اربعین، سفر همدلی و همراهی است
🔹
با رعایت نوبت، صبوری و همکاری با نیروهای خدمت‌رسان، می‌توانیم بازگشت زائران را سریع‌تر، منظم‌تر و ایمن‌تر کنیم.
🔹
چند دقیقه صبر، سهم شما در خدمت‌رسانی به میلیون‌ها زائر است.
↗️
ما را در
cheshmberahim.ir
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/677678" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677676">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از شاهکار به یاد ماندنی اکبر عبدی در فیلم مادر
🔹
همه در پشت صحنه گریه کردند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/677676" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فارس: طرح بازگشایی تنگه هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای، ادعاهای مطرح‌شده درباره موافقت ایران با بازگشایی تنگه هرمز را تکذیب کرد و گفت: «جمهوری اسلامی ایران هیچ توافقی درباره بازگشایی تنگه هرمز نداشته و اخبار منتشرشده در این باره کذب است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/677675" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/677672" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تخلف در تصحیح اوراق امتحانات نهایی تکذیب شد
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
هیچ تخلفی در روند تصحیح اوراق امتحانات نهایی صورت نگرفته و گزارش نشده است. بعضی تخلفات که در فضای مجازی اعلام شده شایعه است و صحت ندارد و اگر کسی مدعی چنین موضوعی است سند ارائه کند تا پیگیری کنیم.
🔹
سطح سوالات امتحان نهایی دانش‌آموزان استان‌های جنوبی هم‌سطح سایر دانش آموزان بود و تفاوتی وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677671" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh_OVCDlTuxRpUSslM9Gl9SwTIXPLEtiYf77EnQIwszT0Z_SALI77K5g6VlGFbSy7fMXar2q4fzuA0oQhDxQS5WyAn6qwkWp2KaEyc_1iSGKbQC4YDJ7pYl9w_dbGa1oTJt_aWCLVamaTgxCduoGUlZC3m9EYbnm9MOeDtzcatBo0GxETyuH3zuSqZDr6R43v1KefkfyDtM2_87sc1ubnzEKBJDMuPzLT3HVRx_G5AmbU9iRgjf4I_m7WovfUyJixppZNY91GEjLh6oheIhF8Gk5jXUewGJOemoP8_iA10IYLrbChvb4w2BrkgehuYbGxcp2j_n82eNAGPB1T6bibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQe9eBW0UNpK9Yip9HlezMwrnmGSOJIZCFVidh-kLA_V4ZmIb7RxqJFnN9oSYX5JfVwashOef84sa4kqRzJs9INYZhX-GmFjxQ3ulRclnUm-zuc5Ew1tKp1O2In-LJEvqEMZfSpmqLPkLRdLxxVuJy-Ys9agKO-G3d9rcOxEjIhvV37e4DR3Vzzx4n0hn97d5mNxYijQbih6CqJrdmu7eXVZauPEbJr6PT1_xjgFR-XhpphfpIJQNRmM56sWZ6278hE0ewNqnPXqQXyXJZXsIzovZJ1keTtDZngwWLGftC7aRUAw2PHdVHoBPiSROgWKBdZf6jkArmWJ9bPLQvU1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuFidJq4bYRveP0vJN8Tkomy-i97A-uLmp7CXvJ9vCSWLSrlkpp2VuWlARuML_sjF7xFK4E0EzsH10c0x2y_WTjMcIMZEjuMmzdxmy2Q-Mc0dI1_iunM8v4rAqqYhvgBQ4h9qaSMyIQxxyVpLDKbDGBw8Ab9U507JDQreWjQIXmn8BLgCfwSqQ_IPubm3ntdJZlG64t7BpUnyp7dOmZYCZIaLLUsEg11zOFjcTXtu-7-nOf-qO_6NY_8Nxy-XaXVPkH1d4qKzHJgDenOpY-IdRO0g_-Mognj5K_MzKckaH6vM5DTkx4RbT-l9H4PAuUbdy_l6hOjdtOwGAOy3vN0Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استایل خیابانی نوید محمدزاده خارج از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677668" target="_blank">📅 12:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نیکزاد: افزایش قیمت بنزین منتفی است  نایب رئیس مجلس:
🔹
رئیس سازمان برنامه و بودجه درباره بنزین گفت که ۲ راه بیشتر وجود ندارد؛ یا سهمیه بنزین جابجا شود یا اینکه قیمت افزایش پیدا کند.
🔹
طبق توضیحات آقای پورمحمدی افزایش قیمت بنزین منتفی است و جابجایی سهمیه انجام…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677667" target="_blank">📅 12:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgeNEhmMlDli--H1rr2mYyIBA3HDIQAdU-qViGYWKSSIQgNqpHR9l9tAQgbolL2OQf34g8hhDgbzMpsNfDJE2e_AM7V_Z9t5IDb4tgQqzj_Ue_LaLqIjZKkW3ErW8iRYp4k2dV1ser39YO_5YbTXvuM93xXVWMjjaKZOpG1WLybytI-lVAHEfi35tS6lPfd0c3Z_TnGhhIyGBJ9AF2Wg9ZIBMTTVvKgXjCY_S59nwm3IdyfXLFwjbHrtthbFV43oktodks6T0OtIAbQvzFr3QhTjDifi4Z1IlM5Aj5jV6Ma-NckaEhe4XFzcAw99Y6EIH7lbNotzad0X2ElpXFgeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه چرا مرکز آمازون در بحرین را هدف قرار داد؟
تسنیم:
این مرکز بخشی از زیرساخت رایانش ابری و پردازش داده‌های ارتش آمریکا بود که در تحلیل اطلاعات و پشتیبانی از فرماندهی و کنترل عملیات نقشداشت که هدف قرار دادن آن با هدف کاهش توان اطلاعاتی و عملیاتی آمریکا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/677663" target="_blank">📅 12:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f578919b3a.mp4?token=Ow5QmyGijImp_hP0oq9UjXMkdHYwxBhEaknMQKmjmK7wuObSZKJdr3_WqAsBnw8Ug1QcgZu9fNHcHyLtT1x9wRs1SGak71nMan-Zjg5NXyW2kuyeieIpoaaOM5V9bvsFewQpZYwE-u73A2PR5dwrhvUcf_GPgKLzZUHFiRFNl_G_WVxaG75CZYm9r5zyYEvO3YixAdH9i3wOhF9tmu_egjTstzOQbxoxZKC_Zc7U1hYdu8NbObP2QWYSSeuOv_2JJ2Rv1bTfwRzQs-temEEdgX0wb8Di1k06DxnJousCSyBFmRxpMcDfbOvLce1Kpsat9cJk4blqVR9BIFYWEbms-IhlO15l53u-GB0YrTqv7lRhc_3pxPVoF61hOzuRQ14L9jds76L9DsHBj24GEhdqTWB9ckkBKj-NxScwXod5ArKF8L0j87eJN8nUrEDt8OCMLgmKEKSgU1yVslj68dgEI5ktsBF_P_14cSpjUGh25mw2CLTFUpm5yeDf_TFdiZQ7SpyWGywtxLEEJ2Dd0CqD3nkml8eGUN2aFZPoclkmUHBOklFS6qhg_kpr1hSPXhSKCgMVtWl1K3PwsONONjDIyRFCutf_wvCTJqaAVmJeDb2nUbGCJP4t9FmsBRh7iyDgMqseez3X_t5JiU2pw-qQ3aW5yTT-AeSdM_uPNVfOAIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f578919b3a.mp4?token=Ow5QmyGijImp_hP0oq9UjXMkdHYwxBhEaknMQKmjmK7wuObSZKJdr3_WqAsBnw8Ug1QcgZu9fNHcHyLtT1x9wRs1SGak71nMan-Zjg5NXyW2kuyeieIpoaaOM5V9bvsFewQpZYwE-u73A2PR5dwrhvUcf_GPgKLzZUHFiRFNl_G_WVxaG75CZYm9r5zyYEvO3YixAdH9i3wOhF9tmu_egjTstzOQbxoxZKC_Zc7U1hYdu8NbObP2QWYSSeuOv_2JJ2Rv1bTfwRzQs-temEEdgX0wb8Di1k06DxnJousCSyBFmRxpMcDfbOvLce1Kpsat9cJk4blqVR9BIFYWEbms-IhlO15l53u-GB0YrTqv7lRhc_3pxPVoF61hOzuRQ14L9jds76L9DsHBj24GEhdqTWB9ckkBKj-NxScwXod5ArKF8L0j87eJN8nUrEDt8OCMLgmKEKSgU1yVslj68dgEI5ktsBF_P_14cSpjUGh25mw2CLTFUpm5yeDf_TFdiZQ7SpyWGywtxLEEJ2Dd0CqD3nkml8eGUN2aFZPoclkmUHBOklFS6qhg_kpr1hSPXhSKCgMVtWl1K3PwsONONjDIyRFCutf_wvCTJqaAVmJeDb2nUbGCJP4t9FmsBRh7iyDgMqseez3X_t5JiU2pw-qQ3aW5yTT-AeSdM_uPNVfOAIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/677662" target="_blank">📅 12:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30df4735aa.mp4?token=oiES3Ac7uu46jewMBvaM_sBOajmTYuNHDXrw6xSZpCQoTAm2q3WxmirwJBWk2LiNNps670FyXBQ8i3QqcBNRgYeto6DQ8bUd0bBF2wv-Qj-2xT-aw9QrWZpUCapC_U0y4LSmBKMgPd0cU2EssVPRGSzKto3ggA6J3TNCwf6xLfCD-faJ2oQnaxY4Qx2k5LtcPqfulv2G-aMHzfk38MhzscZDTzefvzkH2TFl-ONYhqvOOYS5JkqhhiczMOJZ8ApLEMj6VYLBmTIjFGaX62Z4qpuCXMpuanVVWpNXZaBUigAnspmjCEhFSG9YpUr2cH4ZZCuwlpmn3ssqtokA0bhDAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30df4735aa.mp4?token=oiES3Ac7uu46jewMBvaM_sBOajmTYuNHDXrw6xSZpCQoTAm2q3WxmirwJBWk2LiNNps670FyXBQ8i3QqcBNRgYeto6DQ8bUd0bBF2wv-Qj-2xT-aw9QrWZpUCapC_U0y4LSmBKMgPd0cU2EssVPRGSzKto3ggA6J3TNCwf6xLfCD-faJ2oQnaxY4Qx2k5LtcPqfulv2G-aMHzfk38MhzscZDTzefvzkH2TFl-ONYhqvOOYS5JkqhhiczMOJZ8ApLEMj6VYLBmTIjFGaX62Z4qpuCXMpuanVVWpNXZaBUigAnspmjCEhFSG9YpUr2cH4ZZCuwlpmn3ssqtokA0bhDAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677659" target="_blank">📅 12:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقاب آسیا هنوز آماده است؛ نمایش آمادگی بدنی عابدزاده در ۶۰ سالگی
🔹
احمدرضا عابدزاده، دروازه‌بان سابق و محبوب تیم ملی ایران، همچنان و در ۶۰ سالگی نیز از آمادگی بدنی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/677658" target="_blank">📅 12:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX6G1eqQ_nGut_hWrwqGH_OoMQymOQBMVLAPgjtCYb0RswBVsF0TM_P0Fulud-bVrF1PiGchn-gF_VdS4vI7MpoTqVw8WotwpK-fKxsXr7kle3a9vphtQJsGEmwO8FqPW3GpmYCkEd2uaIFfmI24chfAVwyt4p6iqjNd9_BCpuPN-xRrB0yqB0PdKgib7WnCmge1f-pQAhRYoaYTjERi-GBDRMvvjYB5jaLM6IZ1cNfpPpbLrUUdZofSScp3CGxDBIK18PgfyGyTW_rFbBijKv22Lm-Bnm6mMJAnA-3k--8Cu_B7q1SF8Up9A8FQ4ZnIQOLiko4SpVWF3LF-JwRHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور روانشناس زرد رو از روانشناس حرفه‌ای تشخیص بدیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677657" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677655">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: همه ۸۰ میلیون ایرانی حزب‌اللهی نیستند/ خانمی در صداوسیما گفت مملکت متعلق به حزب‌اللهی‌هاست و هر کس ناراحت است برود، در پاسخ به او گفتم شاه هم همین حرف‌ها را زد
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در مصاحبه‌ای گفتم گروهی در کشور حزب‌اللهی هستند و ایثارگر هم هستند طوری‌که به حال برخی از اینها غبطه می‌خورم.
🔹
در حال حاضر دشمن وظیفه خودش می‌داند که جمعیت منسجم ایران را به تکه‌های متعدد تبدیل کند؛ حزب‌اللهی، نیمه حزب‌اللهی، بی تفاوت و....
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677655" target="_blank">📅 11:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDZ6-PQnU-iACsSh9CauTbFCyrweIA46JWqY9Cc7NcdyP0BjtxFvkZobZPDO2fZQhH0B5sV8aZWu7uJ6Obm0zw6KOmxsSxpmgEKdefT7GPAHhjdDMZ3i_VbKxp29_4K9rz8SMySlhwFBs1dF9dkNEcpYeq8F_pdE7ZMjm7JuaYbqH6hzpmC5onVxcQh7t7HU_-7d7hJdMLE1rWRGDCoPYvGXGiL1LVNfCZwYf5JA-wIf6JKECpfDRzVFKLaiUnwQbybNJ0NhbUdq7f1voXumyrB3nHRXCe71ryiHzUcOhM0V4KTeLwdufjJnt3A_V6_-MCsZYcuHSpBGRCjDmybTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArXwAYkMwtEV2x6sbTdMjmySEXkIyoHBA4WcZ_h9hWpwrfObYiGELJIaLfsOGegruE3o9Ipxh-G0nMh5lpoRiIOLK-Hgzln7RMlDLsyHCQXCMTQMEXAf3Z2X28AUMqs9Is3ROFBUuCaoMOEyfY5m3Hh_zKAEEglCFfHxDC6MhiuuBLokmCSo293vq2VA_UZ2Ip3Y3bw_nlB5zob6hhEItd5xg3NGsMw7x59yfMx8_N1CylFK5uHJr4w-EZlfJ-Tg3CizVBI9dlmg24udEmSqiCsU3PnzwbaEgluPynL2dWR73F1gMXFmhDAXvecQRJHnNR8USIeO8RnJve__UKtQDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امیر جدیدی، بازیگر سینما عضو تیم ملی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677652" target="_blank">📅 11:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4c2PYLge7xxLrAIsPz6i004ykNF_mgGJOSz4dp-3W-pZfCCTBJtGm8AvKAkwAe86fpz4MEfWKhML4mKRO5jJsP6X8i6905eVGEOzjYJBtp7IHspUxF1Bg4Kji2E14Xh9-Fw37T47Qy3td28RGz_UNngOTJnFHfVqcxTVUfHXOVJkTclmG_G4MBEdrAwukXQ6NW1YzLYrqmt5NuIhU-acj4mqPrfDmL--HC_2a_J-EpR5hYqqxSJlesNS7POc_7oLoOf2nRP4iCjP_HNHTBVXY3490OOpeyrCAxeMYQOajjN_VLxNIIVCvTo82DXr84hZMIFmLp9veoHaBGFPZRDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۱ مرداد ماه
🔹
در بازار طلای امروز با کاهش قیمتی نامحسوس روبه‌رو بودیم.
🔹
قیمت‌های اعلام‌ شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677651" target="_blank">📅 11:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
خودروی همیشه تمیز، بدون ذره ای گرد و غبار!
جارو شارژی خودرو  با مکش قدرتمند ۴۵۰۰Pa و ۲۰–۲۵ دقیقه کارکرد مداوم
کم‌حجم، سبک و قابل شارژ با USB — همیشه همراهت، همیشه آماده!
⚡️
🧼
از صندلی تا کنسول، از زیر پا تا گوشه‌های دست‌نیافتنی…
همه‌جا رو در چند دقیقه برق بنداز!
🤩
🌟
قیمت اصلی: 1,598,000 تومان
🔥
قیمت ویژه فقط برای امروز: فقط 1,089,000 تومان
🔥
🏠
پرداخت درب منزل
خرید
👇
memarket24.ir/dirmob/180124/g-en26903</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/677648" target="_blank">📅 11:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677647">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2vG27lZoel2nfZLdoTcZtcGfkyYxIUnN7p-e4AI7KT0vo1ItJeid5wxtpamg2q1lUZ3W7O25d7CddgXI4leFiAtSJgDHl6N0oW8u6i1bx4UEBPBp0MjayoOFSGnEBvy_xco8qf2VnNl8RLn2B2X6wL1icI6cepFqOmMS91vbBxGEryBqV_TxtaC0gjI2OzpV-IbJAywF5R3WhVk9AlSSHaFy0Po9MYHPaM5ZXgcqgrUjk29gz2YEa7_ET8BmUHNek166nALFoSibBlCaOkeSkJ6KKXgi8L8Dwgva-nBP1WSuc9dV9BRjIpZveDfSzLKNipaK7XVhnS1XhMsOOgAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باراک راوید: اعلام لغو حمله توسط ترامپ بار دیگر نشان داد توانایی نتانیاهو برای نفوذ بر رئیس جمهور آمریکا خیلی کاهش یافته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677647" target="_blank">📅 11:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/677646" target="_blank">📅 11:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگوها در خلیج گرگان
🦩
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/677643" target="_blank">📅 11:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAQPHwSnFftNbVl-Q0CA2oEpse_Pn6__ae4gfYCiGTvcgFXIfQZ05jvLcJ1KHl3fWxbW98H3_Z1Z8RRDHMEzvBRGjEeBgcvXrRXw7uGzlImAXp-vlqUhv17nc_n8sVgYD--LJPXM9T6GIV1rQmvvN1aY3U-T2jPtsOMmAci8WcLVpCy5Y-xhUX66FSXGGy4Tk4sv1GhJ9HpH5zOvdDAFluA3lu8cBUPhx-uJWAFhJ2qXDxMFpCrxtLFE-V7S0cRfKLJTbwM4I-3ZuE15FjApGg-APacH6CLDUk3q1nsp9BBYnjOgJMXurb1HfY7TP_YW1ZLitj5J1hG_Bj8Ld1VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشرا شیخ: برای واشنگتن در ایران کار تمام شده است
🔹
آمریکا به موشک‌های پاتریوت و تاد نیاز دارد.
🔹
اوکراین به پاتریوت‌ و تادهای آمریکا نیاز دارد.
🔹
اسرائیل به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
عربستان به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
قطر، کویت، بحرین و امارات…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/677642" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره رسیدهای جعلی در معاملات آنلاین
پلیس فتا فراجا:
🔹
فروشندگان در معاملات آنلاین، صرفاً به تصویر رسید بانکی اعتماد نکنند؛ ملاک، واریز قطعی وجه به حساب است.
🔹
به ادعای انتقال وجه از طریق شبا و واریز در ساعات آینده نیز اعتماد نکنید و تا دریافت وجه، کالا را تحویل ندهید.
🔹
موارد مشکوک  را به شماره ۰۹۶۳۸۰ گزارش دهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677640" target="_blank">📅 11:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_3B8jorWHIyqxuTK3ycg9dkLIXK91vALS0GK2v7umxaw4DKUQYtJ1l9H4iNvXgrGzw1MIsW-ggPz_WLVadlWUlXVTrCxQ_80FL3SDFCzmLFBsbJyifk43-BFJt8fzUJKYYqZ9MvUuzx41g6own_TXne2hHdNnR5a7GoPDMMG7qb3sC0OwgREhWgH0C_H_sMNj3o0ZwtfSGgk9eIAHw07GgTlWARKq47PIVLHxgUCWwdrm5usJH4augTdT4ygs0_bCo-OWsILJ97qtyaEGDA_vZMOXmmKcwqWWYOuCT3804o4wb53ZoZKyA6R0plWwjQvYyDYStsJx_hQdTV_HORiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر مسائل دفاعی و امنیت ملی آمریکایی: واضح است که در ظاهر، این ادعا که ایران با رئیس‌جمهور ترامپ تماس گرفته، از او خواسته حمله نکند خنده‌دار است
🔹
سرانجام بخش کافی از هشدارهای نظامیان به رئیس‌جمهور منتقل شد که اگر این حمله را انجام می‌داد، برای آمریکا…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/677637" target="_blank">📅 11:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ابهت و زیبایی حیرت‌انگیز در خودروهای BMW موج می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677636" target="_blank">📅 11:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdFPPJH9edNsXXsnHIA2avF-pF4B8hLgU54ACrgOqykrIV5K7UWW4grPdRXXMOsM7nbwLei7Gx202P33vJZ7frMSa2whzMhnsbaKzE6jD-q0D37sq0TMyl_pzou77C5m0NcLrdhN78iT-30vY4RgGhabo4JAYusIq_mrDk4j4H0iXx1WhLL4IgHJV-aOWm7oiwVQId6-4udt1FP9Fcijt0jlF-Mj5ggDryVoRcFEoIoKYq1CBg4oa09MJbeivFhkpP2V2vQez2dKy3HSEqcjDGs4bXIE5SwXX0zW4QWlKqqc176mUp1tBEh80ytYTPfKAX1fHjKZduQI1W3gG851wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر مسائل دفاعی و امنیت ملی آمریکایی: واضح است که در ظاهر، این ادعا که ایران با رئیس‌جمهور ترامپ تماس گرفته، از او خواسته حمله نکند خنده‌دار است
🔹
سرانجام بخش کافی از هشدارهای نظامیان به رئیس‌جمهور منتقل شد که اگر این حمله را انجام می‌داد، برای آمریکا یک فاجعه تمام‌عیار به بار می‌آورد
🔹
او کار عاقلانه و درست را انجام داد و دستور حمله را لغو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677635" target="_blank">📅 11:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8752ae23.mp4?token=vdry_W_bFcjoUlJe4xOLWk-9Ia-dQD0wGoQbpP9mNiCCoCr15B1vD29YTWKdCHcas6qRmyWUcq_ymlNyjOmoJCgzKl5K5_EioWkdrEknyFrBnGgDSNj9LehTRJ2MwXLDrTVbaF7ohUt_CeYRJ_oUPAhvwL2tMTZLKWSL66OAGhU1WO_I020gmf8sI30J4STJXjpTm4zBJ8vWITpnzP1sO0iHYzZf38KGmt_PrvYPQAhcaUJBpK472jS9etXMwvryq-jbn5Vt7lrgZD8qehxMF3kKQpY_bpne1snVxce3Ms_7wg1HkkLx-Peb-lDWLH39Hhwo_QezOTnbNmp2f1xHgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8752ae23.mp4?token=vdry_W_bFcjoUlJe4xOLWk-9Ia-dQD0wGoQbpP9mNiCCoCr15B1vD29YTWKdCHcas6qRmyWUcq_ymlNyjOmoJCgzKl5K5_EioWkdrEknyFrBnGgDSNj9LehTRJ2MwXLDrTVbaF7ohUt_CeYRJ_oUPAhvwL2tMTZLKWSL66OAGhU1WO_I020gmf8sI30J4STJXjpTm4zBJ8vWITpnzP1sO0iHYzZf38KGmt_PrvYPQAhcaUJBpK472jS9etXMwvryq-jbn5Vt7lrgZD8qehxMF3kKQpY_bpne1snVxce3Ms_7wg1HkkLx-Peb-lDWLH39Hhwo_QezOTnbNmp2f1xHgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رد طرح آتش‌بس ترامپ در غزه توسط شیخ زکزاکی: درخواست خلع سلاح حماس «بزدلی» است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/677634" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677630">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوقلوهای تازه متولد شده همدیگر را در آغوش گرفتن و می‌بوسن
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677630" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqR4NxGG7VW3ig8QoFfuGWenwUV_hcrqWBvKVwI7LC6azEipuseqNEpt25jravMhLbvkayFFvIO7LA5arUewdICleL3EPf7yDIEe2dOeGmVMQ-EyBrKglmP3vzhq4MJ_gfuBhsb_KU_T3cp5ViGn07veoCwp4lYJIIlhUgWD3F_7G_XrGGJ3dPTeO2bSBOtfzccs3Bk-i_5YoFtnAWZN3LmxXzXFAfbVC1hzDr1gC0JwM6N1MD1jtkuNpYGFXsLpCZsK8QpsbIDEvW3oQnfKRfcn6IfstriTZDX57ZzyRi7eCn9Vq69ot8RQQRPJq-8FGcVlX_9tXWdduCrcEnVGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های افرادی که از لحاظ عاطفی برای شما مناسب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677622" target="_blank">📅 10:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
چرا از رهبر سوم هیچ صدایی در رسانه منتشر نمی‌شود؟
همشهری:
🔹
هر فایل صوتی لایه‌های پنهانی دارد که سرویس‌های اطلاعاتی می‌توانند از آن ابعاد فیزیکی، جغرافیایی، زمانی، سخت افزاری و زیستی گوینده را استخراج کنند.
🔹
آکوستیک محیطی و هندسه اتاق:
هر فضای بسته امضای صوتی منحصربه‌فردی دارد. با محاسبه زمانی که انرژی صدا پس از قطع منبع ۶۰ دسی‌بل افت می‌کند، حجم تقریبی اتاق تخمین زده می‌شود.
🔹
تحلیل فرکانس شبکه برق
: سرویس‌های اطلاعاتی با تطبیق نوسان‌ها با پایگاه داده لحظه‌ای کشورها، تاریخ، دقیق ساعت و حتی بخش خاصی از شبکه برق محل ضبط را ردیابی می‌کنند.
🔹
طیف‌نگاری و امضای سخت‌افزاری دستگاه
: میکروفون گوشی‌های همراه فرکانس‌های بم را تضعیف می‌کنند و قطعات ارزان‌قیمت اعوجاج هارمونیک خاصی ایجاد می‌کنند که مثل اثر انگشت دستگاه عمل می‌کند.
🔹
نویزهای پس‌زمینه:
صدای سیستم‌های تهویه، ژنراتورها یا تجهیزات خنک‌کننده مشخصات فنی محل را فاش می‌کنند.
🔹
زیست‌سنجی صوتی:
رزونانس‌های مجرای صوتی یا فرکانس‌های فورمانت ابعاد فیزیکی نای، دهان و بینی را نشان می‌دهند. الگوی تنفس و وقفه‌های میان کلام هم وضعیت جسمانی، ضربان قلب و میزان استرس گوینده را مشخص می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/677621" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677618">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjOYVfuGT5Uu6P4Lu7az-ZzOwKt2mIqFhFONA1Ilnm_XJwXMyzV7dCWderhN1ysTAAJ10rD0wonkZl0j9TKMuBs1eQPM39vQXHB-n-U6mwQcr5QmnjlQOGU25K_N1RQ3i_ChZz0nv1i5ofgKrJKdvsCevZ5uNMoK_7hNQbMRjCANAe264qk9loacx4I1mlLNvYxwic6Y2nGE4ynvphjb4m8yxJVOKvvnFlVWpSkxLIV865gHrZMciGvBbQc5olEsyFcrQne38Y1rXE-gPLm0_qs5EAjkAxJDcjXJADePle2W1616oPFcSc47XTFaUpaSJqvg-SW1ZdmPu036euMUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا با بمب ۲ هزار پوندی خانه‌ای در قشم را هدف قرار داد
🔹
نیویورک‌تایمز با استناد به تصاویر، ویدئوها و بررسی کارشناسان مدعی شد آمریکا در حمله به جزیره قشم از بمب ۲ هزار پوندی «مارک-۸۴» استفاده کرده است؛ حمله‌ای که به گفته مقام‌های ایرانی،…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/677618" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecSn1HbBS5Tz1YPer59PvFykwBcdj2-HvvHNE_LVXw1w9tPBHLdakcbh_p-UvrehhBXDfVdgAkhrAdC5HWjSFFTI__aT_emPbQuPk48C2FarbxiRJcx6PUtQr9-hYValExhh3J-Ii7CC5So3Xo3ywsVXZ1Ysk_0jZa2luygR9Og1J1_IT0La8bDa6qkusQ1PHzatzreXOVreCbkVR1h3Tnz3tYfpg-xHSpHYt-OrN1yL8b0lz4YgSxWxvbrYhj7fabefnBZOMaqbaCx82Wc0RCmyN37YInEWNBruSoQKAdSd-hD8C3QWRYaYNYKHswrdm3kGcoc9AGqLKurTYPeKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امور داخلی کشور: مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام خوبی برداشت
رئیس کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
در طول سال های اخیر اقدامات خوبی برای بهره گیری از ظرفیت های مردمی در برگزاری این مراسم انجام شده است. مدیریت شهری نیز گام های خوبی در فعال سازی و به کار گیری از این ظرفیت ها داشته است.
🔹
همچنین درباره اقدامات فرهنگی انجام‌ شده از سوی شهرداری تهران با طراحی شعار « یا لثارات الحسین» و نهادهای مختلف برای خنثی‌سازی فضاسازی دشمن علیه مراسم اربعین گفت: تبلیغات امروز اهمیت زیادی دارد. دشمن به دنبال عملیات روانی، شکستن روحیه مردم، ایجاد دوقطبی در جامعه، بر هم زدن وحدت و یکپارچگی جامعه است. رهبر معظم انقلاب اسلامی نیز همواره بر حفظ وحدت و هوشیاری در برابر جنگ روانی، جنگ شناختی و جنگ ادراکی دشمن تاکید کرده‌اند. از طرف دیگر اقدام مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام بسیار مهم و تاثیر گذاری است/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/677617" target="_blank">📅 10:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677613">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/677613" target="_blank">📅 10:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به سبک انیمشین درون و بیرون، برای بچه‌ها غلات صبحانه شیر و میوه آماده کنید  مواد لازم:
🔹
یک پیمانه غلات صبحانه دلخواه
🔹
یک پیمانه شیر
🔹
نصف پیمانه میوه تازه
🔹
یک قاشق عسل
🔹
یک قاشق غذاخوری مغز #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/677612" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: امام‌حسین(ع) خودش دست ما را می‌گیرد
وحید شمسایی سرمربی تیم ملی فوتسال درباره حضورش در کاروان اربعین حسینی:
🔹
این حضور به این دلیل است که خود آقا دست ما را گرفته و امضا کرده است. اولین بار است که با کاروان و به شکل گروهی در این مسیر حضور پیدا می‌کنم.
🔹
زیبایی اربعین همین است که هرکس با هر توان و شرایطی، به عشق امام حسین (ع) قدمی برمی‌دارد. فرقی نمی‌کند عراقی باشد، ایرانی، بحرینی، یمنی یا از هر جای دیگری؛ همه کنار هم هستند و از این سفر معنوی بهره می‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677611" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی  بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677609" target="_blank">📅 10:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlldt23hzkbfY9ABBK1mdEwhiLfDX9kJ_YyM_eZ7U2c9ElJAD5bY7toE3RTA9vYsaBKD54KKvfbbV5nyGjSkOvP-ML57OIoifqKA1KZveGqKxkj3B9OsxrYnrKoUehOENWblc9hcj0Pq916nF9J-a-nsDQxeiSJlv_IksQ41l-i-mgBik2W8LYbdtusyT52J0EAkFibzglgaENj599qxcWYqoEh5FJGzMiEg8qLqNAgdgu-dktKniaoboclz-t5c4HopL0I_GxZh6IA2tHp0Mp60O1IeD2FntOkDCRug81ciSIXJTfN4w1Y508BpO7rdmZSU18BX65UwtQcWqmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر روز ناسا؛ رنگین‌کمان آتشی در آسمان ویرجینیای غربی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/677603" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فرصت دوباره انتخاب رشته برای نهمی‌ها و امکان تغییر رشته در پایه‌های دهم و یازدهم
مدیر کمیسیون مقررات تحصیلی شورای عالی آموزش و پرورش:
🔹
نهمی‌ها می‌توانند در آزمون تعیین رشته مجدد شرکت کنند.
🔹
تغییر رشته در پایان پایه دهم و در پایه یازدهم (فقط درون شاخه نظری) امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/677601" target="_blank">📅 09:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677599">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی
بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید در این باره پاسخگو باشد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/677599" target="_blank">📅 09:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677598">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad4M5qDHRfo1QyIcpS1LILAkdHyR21BRT_OhMqWqQOiIZUM8v_DwmFWmykX1awfnQJnSXzbGBjVHMBx-lWlJ4ps_faK88iXuxomopYc0a7uWmBqAtOPWrp7GqlqvbF3v7b0SXDb6C6WtCVMwZzkzYK39NHc7NfDvFDirQU9K-BQeM0rziR9p9HR8C5YI20eVW6LTEQzdCwIG7LWvdvq-rp_YCDPgbVTvwH2cEwKXn8vO6CbvlnApaWqhbHK8rjk8jl-WiiFpgk_QYq9l4aCfW3mb2qxRRWrkA6dpt5VzNgo4XHioWF1a8Bnf0KPCnYhcMDBY1s63oV3_-GbdUWttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
📅
شروع ثبت‌نام:
یکشنبه 11 مرداد 1405
🕚
ساعت 11:00 صبح
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود
👇
🔗
سامانه فروش:
https://sale.kooshakhodro.com/
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود است و ثبت‌نام تا تکمیل ظرفیت ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/677598" target="_blank">📅 09:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677596">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی برای نگهداری مواد غذایی در یخچال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/677596" target="_blank">📅 08:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677595">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رئیس سازمان امور مالیاتی کشور: مهلت ارائه اظهارنامه مالیات بر درآمد املاک اجاری عملکرد ۱۴۰۴ تا پایان شهریور تمدید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/677595" target="_blank">📅 08:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای نظافتچی با کنترل مشترک انسان و هوش مصنوعی با دستمزد ساعتی ۳۰ دلار وارد خانه‌ها شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/677588" target="_blank">📅 08:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه اجباری شهروندان به دليل اتش سوزی گسترده در ايالت واشنگتن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/677585" target="_blank">📅 08:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یه صندلی و چند دقیقه وقت، بالاتنه‌ات رو قوی‌تر و خوش‌فرم‌تر کن
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/677584" target="_blank">📅 08:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0xrgMdPCFfXuwCUUmjCgvEwk-ufVDDybDuSPFoYGysHCKJYm3nN0G5VctndL-V70tyY7oB5j9qUOictUSUhsWp96IP7B-HVW3b2EsQwL5t2RpaDUB6yr2GULIlmLzX9x8tb9hCwv8kO56enD3krcxxGqjnUgNcaDvwssRRDQEBKJqgQqK5oKFV9Z_8NJMt8r76O8TjNWFxUGmma4Klia6rird1gTIhPFxf9OiGaO10cNjwYcW6Tj8aMANR8yrUZGyTpGgvHGbJUfObTyZNBKoI3iE32Tv0NQoJfMcfioUL0S1MYGkulg1bQLvhswJJAD3AlrzR00_809PuG84xMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8hlhdIUHOdDxIR-bsATfHAzlaVtKdp7k0ZjLJ1zm4xnQ5kXgDT1D9ymfUzyFpO-aRiwj-Z21xhxUCtUCO7G55diviAMMP8Z7Od4v-I7vH_ILJu3dPy-5qOyD80ZiADsCZPmiVONl1DBKrROEbKaRxQmEiy2KMkGdIAg0FRHc3MaPCHwKy3Ef0JPwebr05IagsxS4Nik7mvrBap92ryE-EI4LceWB_NadvEl3k0NEIyX9PJk99fgDlf_TkAfXxIo7Vf9pokt_umisB7zIrmSJe2wU4GMWcOlHNH-c_-iUdxskb_nK3AiLkY-Iu_rkR6IGTgmALNUgWh6pUZbcxEa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIQI88XNBf0mt5Rm269pIrALENXg2TaTqj4Bq3Z9qZ4NdyKcP4KMYUnENgDxnVF7m8SJh_vJsHKBMCLgJW6vyA3UNR7rxlUMNlQJaJrdkVlK76iHf10-lhO_WI3RHCBm0_Rpo5fudy3Dz_pnxYySztx4GjbnVDXLWskKOSczzrM9uVM17CjssaxtOEp18c5DZ_VFf8IJcaP20w1vUiWNd1K7BqiAC_28VAqs7NaZBmIqk7cvWF2usQAfQO107HNCW4V1-z6VT5cwkzl2gkbTi6xEXxpIXCDmlUB7-ewH1UvB9K2Otf4rrZuWVJH_uqzq16zw48LdnuLVnPxi8zbNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qS5mgFD9qSQAgibhozzn1MWO4EfV-vZxgAPWfFSaGD5ELrB_q0auU7WW-x5IS3Q86hNswpnL1KDiRaDmOsee7MFkpSOC0qD4CXkKdWrskEHsvPuaVNOGkuIHMk3YX77BXFZkPPW7t34RqWIeNBlO6a5uImp5RJd-TFjF3pjM7utjGaUEc0m2meT51uGe6LGdjFsNomN71-8jpQKESmInTiIlNrG-qs7OLVJEha5NWI8rMAkZRtKvh8u4wld6F3129QKs0_UolWeGciBiIZYP1LZ55KRRRk_auwjhyIG7E04hSn42he35fkK3CpVVtxYHBQcAgbL7r71zezWbexoP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCNTVAJxDH2s1MLl0uc9mrOZbEH0vVnoDnFEKERJ6UjNi2F93dh_i7vVGR-rPG5rvKjhDOnjjzG2Lk_aYCoRQR9z0nWSJ2ZP_FagbDnx9AkLlA3mQ9L01ZpPw1Liep6uCAdXgBu_PR5hwgO_HYdbexrVPPkQXj3ROz4tX6GltO-6f9Wl65Nq9uxFOYcaXoaW4skXDlIzR9YMJe_XPgpNALzpG98cwRuezntctki7NID5j7cMmKZ0F6Dbpg739KyD12ebvrFcXMlcryAvgFBMDn4WFUOFw3L4WDjQ_E4vpH38hL8SZCxbdDMh4-gRxNNpd2h6PQ7nEByjQBB4-w72DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS8OIuxiypYDq-ah91Ab4sKhOluAw0H6I2h4ybW8pB--hpsF3HbrTIkFF89aGgA4cQz92yr3_pxHOBxkydTL3BiHB_0bH1ABPhrdXIyYz4aUmUusKrH3ab1C3fxGUY5S_mry8vAjjfBjwLZVoPMWHy8vUKIcKmccHmHzC542Ih4pLPhOfL9FhuP4THA11-FC0VUW3eI1xdrqoR_TL2uQti4OlJ0q7mAVlOoVNg45gXHmP-rNCaWrZdHh9ftpA-BL_sUIjZbNbzMOyyCWSJTRxJkkyLgZiVBeIY6wZ310y1U6aZFJ3YD0TkYr1Rv5R0NFK_ZrMUZlB7o-VNnQmyDoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1ag60hqz3kED4F6bMDjuUxR4aqYIk_A_nSjbnfb6Sgk3Wjd4ACE4UFqKcEVTHMaUnipWEQ8CVJMW3364hDU824qp-VC06WYAB4oyhEgj9MiGnaNemMF1vNLqoZiSrEbJa0Y5AYNWnhNUN1EZJdZH9COz9wqIpyHOdXX-0V1v9CXDwsityqELr1MYTlUvtxqLh4fRGvE-aRdD0rUQR-IfJqqXpeU1wfW1WB6zoEdAMxp5Vcx7N-uRLuPSEuwx5IvK7GAxBF8rSWFNFnLGAvlg4cyQ57P07G6C_I0IL8vYOsCjvDquqAkuYEXp47z2tpH2nloCGLkpFrlga4iLmkddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYWE-gIeqGwkdXHzBi8X-L1m07-Qiv_r2FZMduQJWuplBDYwAM19_tCpCZKCK71G3YO9K-zR7G7W1pcMV2XhgGeF5aykNY2C5QfwNM1EFycOpsaBqVKaPETvqZgBpczWupIa8VF4dhlGtSLOtATllULSuVLpdY9FGttZtHEYwc6dk1fglKO_YYUU3dCZZGpPLHzjIVN0JtAM0jdptYMHZjfeRur9xQqAh6LDGLIVqzcu6zny4DALq84Pa_gPNl0U6OzU_x3l0Cvfiovf3luoQu4fa4KitJMYENT4Py9Wjm-PwdqCuvXCTHvmanULaFNmT2-FbMis6FUuJ0QMNi1vAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XM777ldiUmIWIH30Y2emgqgHCjQQVMLW9dlMpZuAHaUab4Z6A6Q_XbZ73wBYymACm3FdlkCWan27ZwImU3qFUQkUWBCyKlXLZSh7Gsdy9fQA0YvT8iLeEFb_xY5ofc3126BcGkyHsag_mIxRkEgQPTck6Qm6kCGZOQDQFwElUjsPuZuZC4wnjNHlMDAQ3wm79t8r5kXohjteS_Vxt-MQOOp9t_QsUkI2D2mpnUGhYcQApUqJQi6VZPDYjdxKKxrnwCOEfLL0yivnZeeXMk4HzHDql8_FWSPigahmmILQQAfxKb1N8GK7zXje9Rtk1FZjmLANxy33_NYPwYCcZJQMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1997XKkmBsOp9D-5yIBFqW5ol6kCFk3HDXLGLouF9RronSlq7-ma0t_nKec_M3wF76wBG0V60ANyL4YGJ6Dj1OC116VZ3lu_n1E4BFjs9KZ8_70sQUKWRK__UiUR7Ev1m2DRx_tCDx6D67ERgFn-U4K80aPmoe_nwsiaEoGeFC0DBMb4An_EDaOG4csU3NgYDU1k-YQwqNL2Qc0cV1CksOYutxsJ6bUCDBoVGR0libOFIB76YRYpZ8uxHkPAtYpRPq4LSdUhYb2OXhHjCxvazuZy85Lj1woCgV3tnVDBlf-L9nthUiiK3SpyeUJrQkN_b4aRnt9ggWQfV6YgYvO3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دانستن چند ترفند ساده، می‌توانید هنگام خرید میوه؛ شیرین‌ترین، رسیده‌ترین و خوشمزه‌ترین‌ها را انتخاب کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/677574" target="_blank">📅 07:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677566" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggyaFHQzrp9gzTTXTTHX9xulpd6vqA_hxr6SA1w81G3rw__sDeKlzSyVx_DH5J5yrI7oyVyNSI2H1sa8FZqysNQTX8jZa4YTzCWRGckxldPuh5L0hDCBKdaXPAcQK7Y_k3H0tEcAgPpZazs7gr6KjVdGlatBIZGVgMBC3phntJtjiV_0zL1TOllPoT91fha-AnjIy-OX4iAkX9KmT5njyvgAaZmy_6mFZKuEOiamhx6XHaMUgjipxhwzvbyweoSAHidfOrB_KCwB50NwuV0axMzpiho55P0Sqs3Nhxa4mars0dMzIoZPMy3Uz_TK9877ala7qPQoeoZ_eJWloQ5tHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران، مظنون اصلی حملات سایبری به تأسیسات آب ۷ ایالت آمریکا
🔹
ایالت میشیگان روز شنبه اعلام کرد که ۹ سیستم آبی این ایالت هدف حملات سایبری قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/677565" target="_blank">📅 07:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌ده</div>
  <div class="tg-doc-extra">عین القضات همدانی</div>
</div>
<a href="https://t.me/akhbarefori/677564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
عین‌القضات همدانی
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «پرداختِ هزینه‌ی صراحت کلام»، «شکستنِ تابوهای ساختاری در اوج جوانی» و «حفظ اصالتِ درونی در برابر سیستم‌های مسموم» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/677564" target="_blank">📅 07:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عین‌القضات همدانی و جسارت بیان حقیقت
#پادکست_کافئین
| فصل‌دو،قسمت‌ده
☕️
🔹
اعجوبه‌ ۳۳ ساله‌ای که نشان داد وقتی یک مغزِ مستقل و جسور، خط‌ قرمزهایِ منجمدِ سیستم‌های متعصب را به چالش می‌کشد، چگونه می‌تواند با طغیانِ فکری‌اش خواب را از چشمِ حاکمانِ زمانه برباید؛ حتی اگر بهای آن شمع‌آجین شدن و مسلخِ جوانمرگی باشد.
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/hwciVLCsnpI?si=Sn7kIHdYXQ8FWRVS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677563" target="_blank">📅 07:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHvn1hoy1_qI04jev1SUQrv_uRu6-V3TD_Zlar1x_h2MWMDjhRnRQkUvBata08qgMXpJwCG2DQzZ5E4YNnbrOOCS7sFBv82FFfymiAJ9JksxirEkCoQvRHPv5QPE3ZnHfBGpRAAuyxnBN8Ufm_TFHo3HjqhKsKq_j3OxWBcsQwcv0WfArtZs_lr3GSt30vPotldbYfycJOoDTxLNtEWMup0w4YakG2R9n9HOMPLbVhK9IVBfogK8xdalp-nPkVZbeqfcGx063dwAllHHTqmS21E5cdoUA4dBuC93r1GIh068y0o0chtVml67CQfLx1hmPl_nWAMsczM-0rY0JJijPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۱ مرداد ماه
۱۸ صفر ۱۴۴۸
۲ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/677562" target="_blank">📅 07:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای
منابع خبری به نقل از مسئولین نظامی: ادعاهای تروریستی رئیس‌جمهور آمریکا مبنی بر اینکه ایران خواسته است حملات را متوقف کند، صرفاً یک دروغ جدید و یک تلاش مذبوحانه برای باج‌گیری از حاکمان خلیج فارس و تحت فشار قرار دادن آن‌ها با تهدید است
🔹
چه او به تجاوز خود ادامه دهد و چه از آن عقب نشینی کند، نیروهای ما در بالاترین سطح آمادگی قرار دارند و برای هر احتمالی آماده شده‌اند. اگر مواجهه اجتناب‌ناپذیر شود، میدان نبرد تعیین‌کننده خواهد بود و در آن زمان، همه خواهند فهمید که چه کسی قدرت را در دست دارد و چه کسی کلام نهایی را خواهد گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/677561" target="_blank">📅 06:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
/
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/677560" target="_blank">📅 06:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flb3iM0STzAChgJJLrdcwCa7J8AS_i5wtrrpi3bGfGLKaUeEbkQ69R56yqjbVREAcoBSTnDjG1M_cbHhZVcKcEtz0B4BNLKA9PO-wadv9VEIVJrTtgGQ4MlZag62httEfCMQ7BX08tSs4uJ-Sp0MNNrcpA6HMhk5GmkcCGwtJ86AYks77iNyfZp89HvQVh9rQlzZDPrSFXnlT6daaWAFbkPdubqTh5hp74aLPQlzneUPyQaEt2txCnUKfPcfa3oIL-orbavaiG-dgiv4aK96NtKz1od-qs3egB7lI9JwhTYxAE1dLSHg9UlONkS8_ap0zaBNkG8swgQbIcXmhPuvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک هار: من با لغو حمله به ایران موافقت کردم
ترامپ:
🔹
ایران و دیگر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر چارچوب‌های یک توافق، هرگونه حمله را به تعویق بیندازیم.
🔹
این توافق شامل بازگشایی فوری، کامل و همه‌جانبه تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
🔹
با توجه به این درخواست، من موافقت کردم، به نفع همه جهان و همچنین برای اطمینان از اینکه ایران موفق و مرفه باقی می‌ماند، حمله را متوقف کنم، مشروط بر اینکه توافق به‌سرعت حاصل شود.
🔹
ایالات متحده در آمادگی کامل رزمی قرار دارد و برای اقدام علیه ایران آماده است.
🔹
اسرائیل به شرط دستیابی سریع به توافق، در پایبندی به لغو حمله به ایران با ما همراه می‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/677559" target="_blank">📅 05:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRBwzgwXzY7nQyxv4nD9Ggja7izOt4NXSj-kvQ5B8vkGyfc3pwsn05iloVo9X-XBrPrJ_oYl35sjAXboaR7gp5tZZDbhW3hcxhMIn8F1dPvYxyGmQI_1b_Ykz3p_AKAFl8PljR9sBcO5QNm2dYFWj1hL85o3CidzTi0k3wgqO-J_CldczigUUOodyh2uNPXrmcyLMUXy-kXcuRVIQdZnh2XVTC9QMw9d7vvJYTJOh7mwW4C0-oE6fx6R1H5X4ctQ_cohFkm_hEnkvOFtmXoP8h5Q20maQfFoV_gLJbXOO0d_CbOLMdXOLoowmvK30mrLp9Ed7zJaqmQCfCnjAHnhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیست و نهمین پست سگ زرد در ۲۴ ساعت گذشته
🔹
دونالد ترامپ در ادامه پست‌های رگباری خود، تصویری از جلد مجله نیوزویک درباره ونزوئلا را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/akhbarefori/677555" target="_blank">📅 04:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای اکسیوس: میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی جهت بازگشایی تنگه هرمز، به‌طور جداگانه با عراقچی و ویتکاف، فرستاده ویژه کاخ سفید، و مقام‌های عمانی گفت‌وگو کردند
🔹
به گفته یک منبع آگاه از این مذاکرات، این گفت‌وگوها پیشرفت‌هایی داشته است، اما هنوز مشخص نیست که این پیشرفت‌ها برای کاهش تنش و مهار بحران کافی باشد یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/677554" target="_blank">📅 03:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای آکسیوس: بن سلمان، ولیعهد عربستان سعودی در گفتگو با ترامپ نسبت به طرح آمریکا برای حمله گسترده به ایران ابراز نگرانی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/akhbarefori/677553" target="_blank">📅 03:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای رسانه‌های امریکایی: در پی درخواست‌های وزرای امور خارجه ترکیه، قطر و پاکستان مبنی بر آمادگی ایران برای برگزاری جلسه‌ای در ژنو، سوئیس، به منظور ادامه مذاکرات، فرماندهی مرکزی ایالات متحده به طور موقت به مدت ۴۸ ساعت، عملیات شبانه خود را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/akhbarefori/677551" target="_blank">📅 03:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/akhbarefori/677548" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/677544" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgS7JgROEyJ3UxTlziKDA4m7fKwHK_GMxh4nYD6A8BFbwpw5-_A14CzqiIvkt6SxC-TYp8l9jEuo6UH6STa5BEXg5m9fXNRWTCYm14ypa2AXyQtrYYOMZoOjLtEvLhOwf7ORT68lDCOhvU9CJlQPSWlNOkNCDFjUA1rCFTZKMfdhXmHxJ7ZlHxdH-S5JBdXK-LTRWBmzjmfN0x9kgeRNJMnK2JlXcsc1C1af6S1-1W_SsIkb5AQkaDfn_0ADElD6asv3vMjyAKOTBPs5iYvS1BeEW9BHuyIGxj68lKf_XTB43h98tX6L8g6YWWzL59wedQmeAotK8vuqTZrT7bbIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/677543" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
هشدار رئیس کل دادگستری گیلان در خصوص کشت مواد مخدر در روستاها
🔹
رئیس‌کل دادگستری استان گیلان با تأکید بر برخورد قاطع و هوشمندانه با جرائم مواد مخدر، نقش دهیاران را در پیشگیری از کشت مواد مخدر کلیدی دانست و هشدار داد در صورت اطلاع از کشت این گیاهان و عدم گزارش آن، با متخلفان برخورد جدی و قانونی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/akhbarefori/677540" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/677537" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
۴۰ روز
🎼
چاوشی
🔹
موزیک جدید چاوشی به مناسبت اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/akhbarefori/677537" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDRA1vdwii2NE4Egh4LI4G-tKc2ZLajNeZTPR_lDMgzBiGpmzTTyFRSD1xyHuVnOCGd2fRTxFw0nKXBPKsXyPXITiVJE8mPUjq_xzZJUtDg9_J2NgPq4ho6tsxOpoaJe59tfUNavFWl5DM3u3eiNhfUFJGh18FmQ-AOq4voEZkaN4JjyhIvkCQotkjfL769jk666IFYKs0FUTMt-oua-CUU1kxdtOWYuU98r-St4PXIi7p5IM8O955lbJQeljW-40etB-oIrLlgfmK52W40WOs4HYmTKtrqVhbsUhOMo3NyxQNQC9mm2VWVaq8XFAtZ1QOaMnre12-XNY4FJwvewFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/akhbarefori/677536" target="_blank">📅 00:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtVXEL0pDbX6YM5B5JM0ryxA6zrBXA34OCVP9vqfWrYIB00iAvha-7K4-Ru0Ba_jv9qLQvdlDu-tSbdSjpVXCU_iX_lBCDEbFEkstJqZ-D2fvUGPlZt9i1bfTbdG80ZrD3fKXaSyXFFmvLSiKkTHGCSQ_JfGyw6PikobN2FzElaWIaVSaKTKnRoNLAmUeFe4cNz9NovS1KP3BWYDtAllFK12apqqp-Dq2Dw32c2dH2D47tHz7rp1UmrFCzi4CWs-GwoThGUsGk7s9Tn0hC5h-junnx30luXE9B8qXRgZDAuP-JcmPDW2llFb3KB3e9mHS9cU9WmckcRsNk_XfB44bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوزکار می‌بایست با تابوت برگردد
🔹
طی روزهای اخیر تب جنگ در منطقه بالا گرفته است و به نظر می‌رسد آمریکا قصد دارد بار دیگر دست به حماقت بزند. آمریکا اخیرا برای شهروندان خود در منطقه هشدار امنیتی صادر کرده است اما با این حال به نظر می‌رسد این هشدار صرفاً محدود به شهروندان آمریکایی نخواهد بود و در صورت تکرار خطای این کشور فراتر از شهروندان تمامی نظامیان و منافع آمریکا در منطقه و حتی سراسر جهان نیز در معرض هدف موشک‌های ایرانی قرار خواهند گرفت
🔹
هشتصدوبیست‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/akhbarefori/677535" target="_blank">📅 00:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf3TMCj2DuLiu1YuqWHMyB5XKAveI19nbSDStKmmd-h1lYL_Q6ASeBzpGn77uCtRUTBjt7bdceXi40T9InCNkpaCNHdc1fxQCQBnYc_t6jPbAAwzvMrRu5-gbwOFI0yUhh0sSDmuO0bImK0Cr989sQ_IfaExq82xL1HjyIAWVUos5zm-uioMS65gAlcWammf8AIi0thLYKDsucjdPKkZwcMUvYPifFqBHBTEiV3KHKwEXNLTzqTEF1ZTuyNF4lg7Hv-oTi8U6ZUd3GroL4q2BmqH6E6vlgUqsvEPJajGAaNbUAa71--Xa2MIsGxLBnXoJjY0avCMFys041YupEL4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد هواپیماهای سوخت‌رسان آمریکایی در رژیم صهیونیستی همچنان در حال افزایش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/akhbarefori/677534" target="_blank">📅 00:41 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
