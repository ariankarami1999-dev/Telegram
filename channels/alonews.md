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
<img src="https://cdn4.telesco.pe/file/D8SVRKDX2tCCo42UXZo82YZccSi1ZnzwhQC-jwFr-aYitVhesNp5M0ZartY1hZcWbUA8A3LFprTU__cLwPM7hJM_AHcIPwRdRuLRlTQguqdMjNylyvahdq9RCT1PEBk_XY-j3gxFcMio_FBRuJf8t0PQHa1qG1hGWq6CXL5u6oM685Xn0L5kveYom6t2Fu3IWffjcBqASEdc3nsxDeD2LsuaWgXqSXrGv8VOr-GkYejwt2B-n0m6YvWBBpGEaN43yVmJbE8ZHksyE9u2EoRNOLF_lZoJwOIvIL8EkUKdsP9qRAHl2meVUdall0vWMdIWM1994hpkXMy083AL4do06w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 03:42:57</div>
<hr>

<div class="tg-post" id="msg-145496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/145496" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=NPGe19OTyoiR4Uxmxu0rwmD_WRiRUTEL3OijH8Y6d8X9AJAHM84rnyA8ZnVdsTIWSzSDT6fQ6TMbc1a1WwV7OSlcwzNOMfHVFa4vBQQPrDmlDEXiIOpuozKq-mdRN0XCPSRHKZ23Sw3WK3XT9_s3iqTJ7Aa_Kly9fvBT12-qlywjGFZKQCuS8YkeJV5OFxWaDV6sCJBIVFc1QjnBCTTBhRNJtoFnEvMP97VDyAVQE1k2H04ST2fi5xAlFleec2oU3jSdjCpzx8jpHSy9UYblyhzWQEXQW-UaYyJEmyqYBuvRyvR_T6oYDe-1PkzMk1hfZSS-8pVfFGdcemMBbXcOgA-Vj0UcWEN2BAl9RKaLEEBGVajg-qnq_d09hcm9ZCLLCsp_BZSI3hcvJ2mSZKZ65b0iFkTuUX9l6jNxRTqE-1KyxJunushGhD6MucFZ3IBOpee8FoscDgyUW_LhrZgp3NPaLc0djj8ZdG9lkn3keCQXDiV63Ntfq_-zwOLTATDIDoaKM1SijbLR3BnvMUapEDXVl4QdSLETxGknTj24fQmuWPIu18t_PoDJrj07-tcQGZoK_NfttFq6Lzp_jJUHPjXz2-w5Qe74BNAZLdnZCTs8s4OYBrfsDlKZfwsSINW9DRl9V3QfCjsMAj1L_S05wR8wk06VIjkwWDXqFo8WvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=NPGe19OTyoiR4Uxmxu0rwmD_WRiRUTEL3OijH8Y6d8X9AJAHM84rnyA8ZnVdsTIWSzSDT6fQ6TMbc1a1WwV7OSlcwzNOMfHVFa4vBQQPrDmlDEXiIOpuozKq-mdRN0XCPSRHKZ23Sw3WK3XT9_s3iqTJ7Aa_Kly9fvBT12-qlywjGFZKQCuS8YkeJV5OFxWaDV6sCJBIVFc1QjnBCTTBhRNJtoFnEvMP97VDyAVQE1k2H04ST2fi5xAlFleec2oU3jSdjCpzx8jpHSy9UYblyhzWQEXQW-UaYyJEmyqYBuvRyvR_T6oYDe-1PkzMk1hfZSS-8pVfFGdcemMBbXcOgA-Vj0UcWEN2BAl9RKaLEEBGVajg-qnq_d09hcm9ZCLLCsp_BZSI3hcvJ2mSZKZ65b0iFkTuUX9l6jNxRTqE-1KyxJunushGhD6MucFZ3IBOpee8FoscDgyUW_LhrZgp3NPaLc0djj8ZdG9lkn3keCQXDiV63Ntfq_-zwOLTATDIDoaKM1SijbLR3BnvMUapEDXVl4QdSLETxGknTj24fQmuWPIu18t_PoDJrj07-tcQGZoK_NfttFq6Lzp_jJUHPjXz2-w5Qe74BNAZLdnZCTs8s4OYBrfsDlKZfwsSINW9DRl9V3QfCjsMAj1L_S05wR8wk06VIjkwWDXqFo8WvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/145495" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUPpmwJsteVggI7jJiEC1832-oem7VZReZHKt_DRp35TEBMJvzLX3ADl39GkK0MD40u5vy1XPA4_uuYunI70hOVg3EwSIc_TLt6ByXUm0o7T68poHc9H5Bbj2PsKYc03hDMKvoxm-F6rJRGh6GqGJ53HtK0xhs0sD2K6AY8bAFwUmEJIbOBA4dalAzLELKJC1RppxS_Lb_7SL5xug9OgUNOhZqqOFlDHm_Zr5Hu3DgowRYn1rwzPcGsRGQbq_moQugDDbcWLBnzwBeq3sN940_69fyC6ZRGGesXpMNEv-M6MfKhLnsrk7tBHOd0lvPppgEfS1bLCGouyli2x0jzE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تکرار مجدد داستانی مشابه داستان الهه حسین نژاد :
ملیکا ۲۲ سابه دانشجوی ترم آخر گرافیک بود و بعد از پایان کارش داشته برمیگشته خونه که متوجه رفتار عجیب راننده میشه .
همون لحظه لایو روکیشن برای دوستاش میفرسته ،
اما بلافاصله بعد از فرستادن لایو لوکیشن با راننده درگیر میشه و راننده اونو به قتل میرسونه و دو روز بعد جسدش توی یه کانال آب پیدانیشه
و طبق آخرین اخبار ، قاتلش هنوز دستگیر نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/145494" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قوه قضاییه: حکم اعدام رضا پهلوی صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/145493" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: اگه ایالات متحده همین امروز از جنگ علیه ایران خارج بشه بازسازی این کشور ۴۵ سال طول میکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/145492" target="_blank">📅 00:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=DEAffNQ0X9Rf9dM_yjb-_P3k4fK_Pi1Ebv9Uc8PxI_6SjcuWn2um9xryuUexzFBlc9srW7WfaPIL2esuQKfgtOeQaa4Bk7e_hQZVyMX9wJLIE0GuZUhoqedFUPGX0jcfi6TCCRuHHKRdnMZ_5JZ7MVq1Cor3CPdON7PHYvaANAqrwmB7-hDoG2613HSoGbHdfX9jD_uJTGBrmOo5-NysWvqSMTOUq23hIXmnTYssbSXLz7rTdNcZ3RUc2fKhbhznFsSbsfDBxWwMIwgkFgo_X4xtr8_i890gtE5OuZcqB5YhnViYQI-dhwVwmSTwVKsAiijzemRKrAGjgP4JYKdQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=DEAffNQ0X9Rf9dM_yjb-_P3k4fK_Pi1Ebv9Uc8PxI_6SjcuWn2um9xryuUexzFBlc9srW7WfaPIL2esuQKfgtOeQaa4Bk7e_hQZVyMX9wJLIE0GuZUhoqedFUPGX0jcfi6TCCRuHHKRdnMZ_5JZ7MVq1Cor3CPdON7PHYvaANAqrwmB7-hDoG2613HSoGbHdfX9jD_uJTGBrmOo5-NysWvqSMTOUq23hIXmnTYssbSXLz7rTdNcZ3RUc2fKhbhznFsSbsfDBxWwMIwgkFgo_X4xtr8_i890gtE5OuZcqB5YhnViYQI-dhwVwmSTwVKsAiijzemRKrAGjgP4JYKdQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من انگلیس را از تهدید ایران نجات می‌دهم. اگر ایران سلاح هسته‌ای داشته باشد، احتمال استفاده از آن در اروپا بیشتر از آمریکا خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/145491" target="_blank">📅 00:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp3GxK4GvXpqaRZ9M1QxKtnQZOVyQM3AgqWL8Qm-Y5eZS72MnP7sgIMNt7gZPDyZPIGlerR327DqCPAYCP5q0Jy2QTjYeDQtLycMDGdzX307jrOzMIIQVfRyK_UiH0E4756DIi0BMdhaGQPrGEiS7h9muZy0o1dRwbZC02iI3JhcgQB6zchyuBge2hRUJ1Ug7k31iHt1In0EaeEFyucYsHn4UdN6m4mEydEkeMu5CGUlISWT9-OVkhuQFEPY6mwqeQIzQ5cEsJdMet3JGeJcCsaSvoDkgsSFHemFiTeQYFfW2-Ck7HeyXea9BIPYBnUd8VVG2JN6-p2s6VF6kqaejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiAK013DRm39xMmt-U_VQoy3IJfsdvs5HgSUvTW6LbcysOmoGOq7Pftqzpu1_fPycI2kk20_2e4cHMLtQK0w5RoQu7h6Yn1sszr1Wd2o_U6hwSm7Y2wwuGh3n3Gxc1phWAUSs26Amt0lM6YWkvHBGjYsJy1dFcSkAG6Duk5iO2dnFjNP9OFJR5VuyomCREEIe-PRTOboi2LxS2-RRXPc5g_3c1lbEwtvL8YsE857Kvt5MIy9XbLuYHR92o98BtCp0l-YtjYWshbqPXLfRxfHXhbzOqPWBthlRO_OynMczXHGc-3GbuDLtxI-Jj6K9y_b0jw9De6TGTL6wxEELnKIsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی نفت‌کش "میرکان" متعلق به ترکیه، از تنگه هرمز عبور کرد و از مسیری استفاده نمود که توسط ایران تعیین شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/145489" target="_blank">📅 00:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhaZAPoa50VF2dju7grgxYheXmg1N1w0auqJqNhlYqAlcADMBu4JuvCmYUuNhYnOEfxAX5gM5y-Y_HtBobcrCu-tx77TAiveDkpuhauHV-QRTSXAR2LWRSW6_N4_pB4mQ9Eg3w2YxXXxnmwg6LLpHj-crMlLtLN_XdfWK9AxWI9LJ2mkkZOCURtmKHJUtNcNtFUIsTRXyEvX4j0Gl82v2Eq15_2KxvLnSb-FZ5YYY1wOd9znbgwfyRbCoGZrKhC3PJIkuc2lj1u0tYNSb0ULdhHkVrZq_r37BbBgoTDGLHmtoQWS7BWQ8L0BhBGxZJEr6tYot1ILU4kjoBXiWCMARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی:  احتمالا هماهنگی جدیدی میان نتانیاهو و ترامپ شکل گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/145488" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOScdEGG5yaaTevkMcUMJlSMWZVhcrAvIKks6xB-xe6UsRJjurHWvxB_AY_Z3hOeElOv8LbgqtlPe6G2fAb5zXGvoMEgzlZllG2aU5oJYr0IO4-MURWShjb_Z3UPv7kwWuNcScq9WfTiJpT2hhMynSCsVlbjxsBkQGkeL88YnciFPFvF2YAvFiFpAVaLnEwH0FlX-A09lpX1iLiIYTTbAi-HxbtAzqqsHsF5MbDLoijMMWFVh3JyFQvELIuzy9JudyMy-i3HK9onjIBGQfJJksvTXFSra19u8mHP1NhUr934OfN0w07qxZfrYJAtBncY1sQcfeGx-NwI4WLkD8vH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دادگستری ایالات متحده آمریکا پاداشی تا سقف ۱۰ میلیون دلار برای اطلاعات مربوط به امیر یاریاب، رئیس فرماندهی سایبری نیروی دریایی سپاه ، تعیین کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/145487" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
متکی: آمریکا طرح چهارده بندی را پذیرفت برای این که بنا نداشت بهش عمل کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/145486" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itYGGw3EZmTlYPnel9gG_U31BuIyArJ_PaQPwlBKBjHcud5903KLOa4JuYtR8LXKAWAXIoVZAKMkuJwuJkM5PP5CyVScHYDt_soG8uz8bfvGntJKmtqGg5mWFlzCAXht6xFvpdXUC3vqnPXMZPtC_NQQngGv3iejc_Lt_RJFTZ1m9D9o8LvAJ1U1e9WwyDLUXsx78jkzPL4pvT0NAcoNa9XwUxKQMULFPwL3UKwWb_WMfH3y4K7JjJsJM2LE8h0wMwuS6T3y7wXE0edKCKGvukHaQvuMK91FKg0SSBhFGoLcyhboCuph_aaeuqnhwVC1OSykbCuxGvpVJGK-YJCXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی، سخنگوی وزارت امور خارجه ایران: دولت قطر، در یک سند رسمی که به اتحادیه بین‌المللی مخابرات (ITU) ارائه شده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر، "به تأسیسات نظامی آمریکا وارد شده است [...]. هیچ منطقه‌ای مسکونی هدف قرار نگرفته است."
🔴
تنها استثنایی که قطر مطرح کرده، حمله به یک تأسیسات گازی در تاریخ ۱۸ مارس است. با این حال، باید به یاد داشت که تأسیساتی که در آن روز مورد حمله قرار گرفتند، در خدمت تهاجم نظامی آمریکا علیه ایران بودند.
🔴
این موضوع، تضادی آشکار با سابقه طولانی ایالات متحده در حملات عمدی به اهداف غیرنظامی - مانند مدارس، بیمارستان‌ها، محله‌های مسکونی، مراسم عروسی، پل‌ها و غیره - دارد.
🔴
تفاوت بزرگی بین یک ملت متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی را حتی در شرایط دشوارترین شرایط آموخته است، و حاکمان جنگ‌طلب که هیچ قانون یا اخلاقی را در اعمال قدرت خود رعایت نمی‌کنند، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145485" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=h-FZrszrhHacws92A2is4bzbhlBEAo5NFUONaf8T2LrQm8juDbzKKBOfdRusxFVXCrFYbTG56bFL4i4BWjKmGjLacnv1gXixIp2Phe56TzHcRDHB0auZt9HcGN5NcPPTkIf4w9FFaCvwfVRp0Vrr3r7D8cxHu1r-GLi_dED9QgWs76EI8W1noXXGPV_7X4hGWzto5QCYMW6n8iyvEANMHAygf-Pn3OElXagQb716IR4sY_yQbuM9QsIp8Ha7zU0ZdSM9ZGpUc7BN9efbEQEqdfMhEp1RXZwDtFC7HQZZevX67nJxVK1JDUZEQjW1_EleNkDn5Lf6sOyP8lkANGsQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=h-FZrszrhHacws92A2is4bzbhlBEAo5NFUONaf8T2LrQm8juDbzKKBOfdRusxFVXCrFYbTG56bFL4i4BWjKmGjLacnv1gXixIp2Phe56TzHcRDHB0auZt9HcGN5NcPPTkIf4w9FFaCvwfVRp0Vrr3r7D8cxHu1r-GLi_dED9QgWs76EI8W1noXXGPV_7X4hGWzto5QCYMW6n8iyvEANMHAygf-Pn3OElXagQb716IR4sY_yQbuM9QsIp8Ha7zU0ZdSM9ZGpUc7BN9efbEQEqdfMhEp1RXZwDtFC7HQZZevX67nJxVK1JDUZEQjW1_EleNkDn5Lf6sOyP8lkANGsQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه رستوران اومده قیمت هارو به خاطر نوسانات قیمت به صورت لحظه ای تغییر میده و‌ تابلوی صرافی طور گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145484" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تحلیل الجزیره: آمریکا نتوانسته توانمندی‌های نظامی ایران را از بین ببرد
🔴
در حال حاضر، هیچ‌ یک از دو طرف قصد تشدید تنش را ندارند
🔴
این خوش‌بینی وجود دارد که در آینده نزدیک شاهد تشدید عمده تنش‌ها نباشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/145483" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ارتش اسرائیل: عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145482" target="_blank">📅 23:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
🔴
این تعداد شامل یک کشتی بیشتر است که از روز چهارشنبه تغییر مسیر داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/145481" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گاردین: رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145480" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
‏ کانال ۱۴ اسرائیل مدعی شد
🔴
پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145479" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L30w30cPBR-l224taXYouXbYjhRp-a3x_33bMcPkg0XC24WUamadIEXsN6-VFXdTIECkuJ-4P5377nbiD40vFid1ZZGcTI3u5HBVXAaU10w-Nt4N9OrUxN0bKe1oi-H0BFt_274FDJNb0Kl4BF0cGLqwHxQt_NujzkNZ-PO33ByVT2x_G2jI-od_7bV-vRrRCgPYieO4luGZyHUfx8PIo0GaK6e26HsyjDyyxAw2YJdNgLTyuPD08pAQOGUug-1fx45vSAKJIza8HEiQuAE6SHdVSEyPAZ_gAbs9F2krpfebxdW9LQiJ4Fgqe9tLkKq5mip6mbts_4YwcA1J8YY7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت نتانیاهو پس از خبر تسلط بر ارتفاعات علی‌الطاهر: با ما درگیر نشوید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/145478" target="_blank">📅 22:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH7rjFgM3YNVPGiG4KVG2ofZXctb3l_2Lu45oDEDgzKG1l-NnrM8mUrGXDYnNgyl8AiRwj3UW7J-tWnNPrLAAEsDyUJkB24bt8CBUAbOAqGx4BJEzslWyDcPBle_WeV3HK_aVq-UB1pvEsr9p572np6BIBhwCdE-uE0exzT8avnzuZF0rKzIcgXXTQSJ0Qh2AVPI81QTL09g02UTdJqdGcuNfNSJJjXlP3q1M3rvAb8-zu2lacDjYis-G-HmwZ5ei96Cs--65VTI3BPVQcs3I2_VjPeA5ZEp03_RZG-oOeypER5LduQJiuJOQs8qYZKTbf3gGOR2NgQdeoLSx1W7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به روستای المنصوری جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145477" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOtRTrRxftFW_wCAWH-u49d99ZQV0lw-wckn37A67pt4p8L3bixiBEOTjAVIu6spTSdPIlA5U48yrPNUK7OAdzIFluOsjSkxTwrcn4J8L7tq5L-I-3QGGz-eK1LZfKmPy8bUGwvxU-hjz3QOYax3Nxzf9sEGIFIpTxAqEixeJ00tvgFexDfAYwhVPE5zlENoyaYKf4EO2hYPQ0ymAGomjEuN5DenJNSvRwhoIepUmFGmFRJGvOKbPLj1P-usf9t9GX4W1M_rsZZ8hJ12Yb6SmRjMZurc_nKELPzqR-d0XyqJBZftm7mD4t81nck-wGgnXpThYka0aUK4ahVNtfWY0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: امروز من نوه‌ای از راوول کاسترو به نام فیدل ارنستو کاسترو کالیس، بانک بیرونی کوبا (Banco Exterior de Cuba) و چهار نهاد دیگر را که بخشی از شبکه فاسد مالی و اطلاعاتی کاسترو هستند، مشخص کردم.
🔴
دونالد ترامپ و من در تعهد خود مبنی بر اینکه کوبا آزاد خواهد بود، سست‌ناپذیر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/145476" target="_blank">📅 22:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,600,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145475" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz2oyxHank9SufFrf7umgsHh5BVZVJvzpbtSTNabVThqdh68Lt_hsxcBs3y2_U_AoB4mpbj0W-jwSfZMO6oWCM3CZsCLna0AvKZjcH43qL5LmASVgt3vScRFzfRSx42lreLNIhIp9_fSEeQYCy5sZWKlUfDnjIaBol9GyLoFwBlWlWlQ_gQPo5dJ-ViD2rurZZ2RmXZVKrhUA5T3fYM3s8JMPzCQBhZXfJndpT8MwepwbT8VbtQLVx3188fad-VMjA8w3ggS7MCY7m9S8L1wdm-J32vMoPbi54Bgrjte4vFt691-oIQkJbXu0_1dBd9Yq6jiEf8e4nFArR20MDcLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایمز اسرائیل
:
گزارش قبلی رویترز مبنی بر اینکه ایران به آمریکا هشدار داده است که به هرگونه عملیات تهاجمی اسرائیل علیه علی طاهر واکنش نشان خواهد داد، کاملاً بی‌اساس است.
🔴
نیروهای دفاعی اسرائیل (IDF) از چند هفته پیش در تونل‌ها حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/145474" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۱۸ نظامی امریکایی کشته شدن!   رویترز گزارش داد وزیر بازرگانی آمریکا سخن قبلی خود مبنی بر کشته‌نشدن هیچ آمریکایی در جنگ با ایران را پس گرفت و تأیید کرد که ۱۸ نظامی آمریکایی در جریان جنگ با ایران کشته شده‌اند. این رقم مربوط به کل درگیری است و رویترز آن را مشخصاً…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/145473" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ونس : اگر به ترکیه، آذربایجان، قطر، امارات متحده عربی و عربستان سعودی نگاه کنید و به طور کلی به سراسر جهان بنگرید، در واقع شاهد تعداد زیادی از کشورها هستیم که گاهی اوقات حاضر به بیان علنی این موضوع نیستند، اما در پشت پرده کارهای بسیار خوبی انجام می‌دهند تا به ما کمک کنند تا اطمینان حاصل کنیم که ایرانیان به دلیل شلیک به کشتی‌های تجاری، مجازات شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/145472" target="_blank">📅 22:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ونس : هرچه بخواهید درباره چین بگویید، آن‌ها از آن دسته کشورها نیستند که به دلیل نپذیرفتن خواسته‌هایشان در یک اختلاف‌نظر بین‌المللی، به کشتی‌های تجاری شلیک کنند.
🔴
آن‌ها قطعاً مسئولیت‌پذیرتر بوده‌اند، هم از ایرانیان و هم از چند کشور دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145471" target="_blank">📅 22:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ونس: ما می‌توانیم منطقه را ترک کنیم، اما کشورهای عربی حاشیه خلیج‌فارس به ما می‌گویند این بدترین اتفاق ممکن است
🔴
با وجود اختلافات سیاسی ما با چین، آنها مایل به همکاری با ما برای اعمال فشار بر ایرانی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/145470" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ماریا بارتیرومو از فاکس نیوز رفت. آیا او قرار است سخنگوی بعدی کاخ سفید شود؟
🔴
جی‌دی ونس: نمی‌دانم، رفیق. نه، فکر نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/145469" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : ما با اطمینان کامل احساس می‌کنیم که سرزمین مادری در امان است. همچنین با اطمینان کامل احساس می‌کنیم که مقامات جمهوری اسلامی قصد انجام کارهایی را دارند که توانایی انجام آن‌ها را ندارند.
🔴
مردم آمریکا باید بدانند که دولت آن‌ها با تمرکز وسواسی، هم بر پیش‌بینی هرگونه تهدید سایبری بالقوه و هم بر پاسخ مناسب به آن‌ها و اطمینان از عدم وقوع آن‌ها متمرکز است.
🔴
اگر به توانایی ایران در اختلال‌آفرینی در زندگی عادی آمریکاییان نگاه کنید، فکر می‌کنم این توانایی بسیار محدود است. صفر نیست، اما بسیار محدود است. من بیشتر نگران حملات سایبری از سوی بازیگران دیگر هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145468" target="_blank">📅 22:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145466">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ونس : وقتی می‌پرسید «این جنگ تا کی تمام می‌شود؟»، در واقع دارید از من سوالی مثل «ایرانی‌ها تا کی به کشتی‌ها شلیک می‌کنند؟» می‌پرسید.
🔴
من پاسخ این سوال را نمی‌دانم. باید از ایرانی‌ها بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/145466" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145465">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
در مورد جمهوری اسلامی آیا جنگ تا انتخابات میانه‌ای تمام خواهد شد؟
🔴
جی‌دی ونس
:
من آن را جنگ نمی‌نامم. در حال حاضر شلیک فعالی وجود ندارد. من می‌پذیرم که در برخی مکان‌ها این تنش‌ها تشدید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/145465" target="_blank">📅 22:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145464">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس : دیروز شب، ۱۵ میلیون بشکه از تنگه خارج شد. این به دلیل ایالات متحده است.
🔴
اگر ما این کار را انجام نمی‌دادیم، هیچ‌کس دیگری آن را انجام نمی‌داد و اگر هیچ‌کس دیگری آن را انجام نمی‌داد، با یک بحران انرژی جهانی فاجعه‌بار مواجه می‌شدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/145464" target="_blank">📅 22:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145463">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ونس : ابزارهای اضافی زیادی در اختیار داریم.
🔴
برخی از این ابزارها توسط رئیس‌جمهور استفاده خواهد شد و برخی دیگر نه، اما من قصد ندارم دقیقاً تبلیغ کنم که چگونه در ماه‌ها و سال‌های آینده با ایرانیان تعامل خواهیم داشت، زیرا صادقانه بگویم، این کار فضای تصمیم‌گیری رئیس‌جمهور را از بین می‌برد.
🔴
اما هر آنچه ممکن است رخ دهد، روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/145463" target="_blank">📅 22:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد ایران، آیا این درگیری تا زمان انتخابات میان‌دوره‌ای به پایان خواهد رسید؟
🔴
جی‌دی‌ونس: من این رو یک جنگ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/145462" target="_blank">📅 22:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس:  اگر به توانایی ایران در مختل کردن زندگی عادی آمریکایی‌ها نگاه کنید، به نظر من این توانایی بسیار محدود است.
🔴
این توانایی صفر نیست، اما بسیار محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/145461" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : همه می‌دانند که تاکر کارلسون و من دوست هستیم.
🔴
بسیار واضح است که تاکر برخی چیزهایی را گفته که من با آن‌ها موافق نیستم
🔴
او برخی چیزهایی درباره رئیس‌جمهور ترامپ گفت که به نظر من کاملاً نادرست هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/145460" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145459" target="_blank">📅 22:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ونس: آمریکا از زمانی که من زنده‌ام، جنگ‌های زیادی را تجربه کرده است. ۴۲ سال.
🔴
و تا زمانی که دونالد ترامپ رئیس‌جمهور ایالات متحده نشد، تقریباً هیچ‌کدام از آن‌ها را برنده نشده بودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145458" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ونس،: توصیه من به مقامات جمهوری اسلامی این است: از رفتار مانند افراد دیوانه دست بردارید و از شلیک به کشتی‌های تجاری بپرهیزید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/145457" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره ایران:
رئیس‌جمهور ترامپ گفته است که ما واقعاً دو گزینه در اینجا داریم:
🔴
می‌توانیم منطقه را ترک کنیم و کل جهان بسیار بدتر خواهد شد، زیرا دسترسی تضمین‌شده به نفت و گاز وجود نخواهد داشت. کشورهای عربی خلیج فارس به ما می‌گویند که این بدترین اتفاق در جهان خواهد بود.
🔴
یا می‌توانیم بپذیریم که ایرانی‌ها مانند افراد دیوانه به کشتی‌ها شلیک خواهند کرد و ما کاری که باید انجام دهیم را خواهیم کرد تا اطمینان حاصل کنیم که تلاش‌های آن‌ها منجر به بحران انرژی جهانی نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/145456" target="_blank">📅 22:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جی‌دی ونس: تا اینجا عملکرد بسیار موفقی داشته‌ایم.
صادقانه بگویم، اگر تلاش‌های ما نبود، قیمت بنزین می‌توانست بسیار بسیار بالاتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/145455" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=rAaKtpvF_1Vxc_t2XfbUAR0YeD94SMxqajaIlBCCpnJl_leY8wHDq5amNfV8Q3AZg9rGKyY-A2DoD-56k6RFBZB02TBMGJJ6OlAmRMJKhahshyrHU-jBDNVg4VYhvDbfAbeFPde61e68YTCBE2FxaciAs2dtM9WXPiQaHkENTHz4ua4tmI5o_C913Tgh0IIfBbeHysRNMiD0rvw99rjT8Bmxv0PnAbEu0bsGfQhvAnBSxPBhq5quAsQawJ6CbXx_Wu4_AFUSWtX0O3W9U04vbCFu7uV7vu-sNWdmvkUcpYN-UAoKKqt-O-Q6yPBn1X_lEqtmGTpVwi8h7P3H0U6SWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=rAaKtpvF_1Vxc_t2XfbUAR0YeD94SMxqajaIlBCCpnJl_leY8wHDq5amNfV8Q3AZg9rGKyY-A2DoD-56k6RFBZB02TBMGJJ6OlAmRMJKhahshyrHU-jBDNVg4VYhvDbfAbeFPde61e68YTCBE2FxaciAs2dtM9WXPiQaHkENTHz4ua4tmI5o_C913Tgh0IIfBbeHysRNMiD0rvw99rjT8Bmxv0PnAbEu0bsGfQhvAnBSxPBhq5quAsQawJ6CbXx_Wu4_AFUSWtX0O3W9U04vbCFu7uV7vu-sNWdmvkUcpYN-UAoKKqt-O-Q6yPBn1X_lEqtmGTpVwi8h7P3H0U6SWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
:
برای مدت بسیار طولانی، دولت بایدن ذخیره استراتژیک نفت را صرفاً با هدف کاهش هزینه‌های بنزین و نفت تخلیه کرد.
🔴
هیچ بحران بین‌المللی وجود نداشت. هیچ کشوری خارجی تلاش نمی‌کرد تا بازارهای جهانی انرژی را مختل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145454" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/145453" target="_blank">📅 21:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/145452" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اسلام آباد: نیروهای امنیتی ما ۱۵ شبه نظامی را که قصد داشتند از افغانستان وارد خاک پاکستان شوند، کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145451" target="_blank">📅 21:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مقام ایرانی به رویترز: در نهایت افزایش نرخ تورم و سوخت در آمریکا، ترامپ را به ‌عقب‌نشینی وادار میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/145450" target="_blank">📅 21:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rhd-uw1mdGo916hqwqydfBUVLAIfe2IGKDWuvuql3dhgtCU7nRk5Go8gaDWApf_5h57Nu1F6yOAhJTSYuaikE-6wIqaCYnw9GPzbqRRo-UuIbcxRxFFif-Bxy3-R1dHIE3QzrjqF9_x8zN608tzXiR1Er02NZBbI9W9mpQeu40ntcFoO598GTswu-7NdnZmmmdx60L2aoxH92C7hWY7zTuvthK9CKQAm9JXO1ijB_CRl-EDvqYO2XOa66-g7_12bqocBJqmrJ2tFe3XXvuMhk9ABo0ekIOHGiJ1S0yuUVUgrTi7F99rujGps9ROhAt68HDP_EfrKUwU0crwg55Cqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7SqrvyQ3ON9X9fXpCqpqybGPyfVc71lLGnt3QsMX9BB_zybvKgnVWonpTEGI4sfTMb44VKnvUjuEr9PgfJgC-ZrnHaRtgwQcWb6bGCE7Vzt3kAS0_n1E6KBKKi0uPCEcUfOWrV9ypC5aVbq3oYEBFseQgaOpX_psL9UrN8QseokjRp5bm3Bmwm-ogwT_FV4fgGJhur6G6kULGZFKCHPxlpiEoWgAUqu5U2XYayEZFBkJoYUl8Yboy3pJG4G9t9QhaCqyXKYL3nyTtCSKKVey6_F84NcFLg1DLVmsDPLizfnqSi_qo62gT-Odfdp5aqdc4YgG3ypWrAyfM2tEZR2hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات سنگین شبانه اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/145448" target="_blank">📅 21:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر نفت: در جنگ ۱۲ روزه انبار نفت و پالایشگاه‌های فجر جم و پارس جنوبی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/145447" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145446">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نیروهای اسرائیلی با چهار راکت، اطراف تپه «باط الورده» در نزدیکی شهرک «بیت جن» در ریف دمشق را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/145446" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145445">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhSGEPov9Ad6TJsGt9u1MX9URjTNHJxZbR7dPybjE1bsEu73JG3d0Ecm-G1h7xeCIhMkFozFriwwakirpT0iE_PiFl9sPy0iKqiKOU0UUqjSesqC60250wkbt0cTU3MJeMMPP4ZB8Adw1RZL08HtzjG_k_th8l7qh0RUqDGCuerLv8cEP-XG7NZ9lgk0cW9en2xtuPg3Pa9FBh3Z4msa8Yu4qo1qnchpmzDfykPElwqnIGQNH7hLHV_v3RXV3Rlb2s_kFfCqPTDXdfCrhjyVbI19qzeY1orsghzGdh_RnZ9cOgmf3jk5indX764PAQyED33HCck3WhW9Hq1i9Hzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری های جدید علی کریمی که بازخورد های زیادی داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/145445" target="_blank">📅 20:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به بریتانیا: کشور شما خوب پیش نمی‌رود.
🔴
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
🔴
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/145444" target="_blank">📅 20:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB74ON7LzHx9-kgrQGTVdBlEaf3pAw-AfYNqRMi0rrBmEe3TCMcA2hOhvRmfZcoUyqYYaMVWKtRNqJ75L2z6DgUn6iG1RFSlPk5uDUc7H3E1W_irA4jcnQPDgQNS30OQmOpZ5cnckxtfcY4TKvxt8QIn3liQ1TzYidhaMrfmltNpUtITs4p8HbCiHbdjHqPJPTAmGFzJ3pW7luPi2VmxEz2nx8pQ6xQhQ9-dz5LneDbeRcKEmSbwYivllZgfbLs-8TpVJ_PNQQmiMnqoA-nHRVxbvDDrVf8KXi_AhD_rWCfBFF7Oh9aWcQDY3bfmpTI40i_2tiZQNM_xYR_SSQfsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به وزیر خزانه‌داری آمریکا: «قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
🔴
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/145443" target="_blank">📅 20:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کانال ۱۴ عبری مدعی شده سطح آمادگی و هوشیاری در داخل اسرائیل به‌طور محسوسی افزایش یافته است.
🔴
به گفته این رسانه، این وضعیت در پی نگرانی‌ها از احتمال ازسرگیری درگیری نظامی مستقیم با ایران ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/145442" target="_blank">📅 20:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سپاه اعلام کرد که هفت نفر را که ارتباط با گروه‌های کرد در استان ایلام در شمال غربی کشور داشتند، دستگیر کرده است؛ این افراد در حال برنامه‌ریزی برای عملیات‌های مسلحانه و حمل مهمات بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/145441" target="_blank">📅 20:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک پست: عمان به طور پنهانی پیشنهاد ایران برای دریافت هزینه از تنگه هرمز را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/145440" target="_blank">📅 20:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هم اکنون حمله اسرائیل به حومه دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/145439" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به گزارش بی‌بی‌سی، دونالد ترامپ تلویحاً اعلام کرده است که آمریکا ممکن است در مناقشه بر سر جزایر فالکلند از بریتانیا حمایت نکند.
🔴
ترامپ این موضع را به عدم حمایت لندن از آمریکا در جنگ با ایران مرتبط دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/145438" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد، «اسرائیل کاتس» وزیر جنگ این اسرائیل، با حضور «ایال زمیر» رئیس ستاد کل ارتش و شماری از مقام‌های ارشد نظامی، نشستی امنیتی برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/145437" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه فایننشال‌تایمز گزارش داد بازار بیمه لویدز لندن انتظار دارد خسارت‌های ناشی از جنگ آمریکا و ایران در کشورهای خلیج فارس به حدود ۱.۴ میلیارد پوند برسد.
🔴
مدیرعامل لویدز گفت برخلاف حملات به کشتی‌ها در تنگه هرمز، بخش عمده این خسارت‌ها ناشی از آسیب به زیرساخت‌های زمینی است. از جمله، شرکت سعودی سابک در پی آسیب یک مجتمع پتروشیمی در حمله موشکی، در آستانه ثبت مطالبه‌ای حدود ۸۰۰ میلیون دلاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/145436" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نتانیاهو بار دیگر تاکید کرد : "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/145435" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145434">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، مارک کارنی
:
ما از آنچه پیشنهاد شد یا از دوام آنچه ارائه گردید راضی نبودیم.
🔴
ما نمی‌خواهیم در کوتاه‌مدت به دستاوردهایی برسیم که چند ماه یا یک سال بعد از ما گرفته شوند.
🔴
این امر برای کارگران ما، شرکت‌های ما و جوامع ما منصفانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/145434" target="_blank">📅 19:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
برنامه های هوش مصنوعی ChatGPT و Claude و Grok‌ و Gemini به دلایل نامعلومی از کار افتاده است.
🔴
تمام هوش مصنوعی های آمریکایی از کار افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/145433" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145432">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مدیرکل فرودگاه بین‌المللی قشم از برقراری دوباره پروازهای مسیر دبی ـ قشم ـ دبی پس از ۶ ماه توقف خبر داد و گفت: نخستین پرواز این مسیر با یک فروند هواپیمای ایرباس A320 روز سه‌شنبه ۱۷ شهریورماه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/145432" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145431">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، چند مقام ارشد آمریکایی گفته‌اند پیت هگست، وزیر دفاع آمریکا، در گفت‌وگو با افراد نزدیک به خود از شان پارنل به‌عنوان گزینه اصلی‌اش برای تصدی سمت وزیر ارتش یاد کرده است.
🔴
بر اساس این گزارش، پارنل در حال حاضر انتخاب مورد ترجیح هگست برای این سمت به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/145431" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / پرتاب موشک کروز ضدکشتی توسط نیروی دریایی سپاه از منطقه سیریک، ایران، به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/145430" target="_blank">📅 19:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2894def8.mp4?token=J2r_Vr3RfKQji-ANv_sm4mhIkjJ25r6xA0z4DLPgXiR7rpdw9sgS4iAQ1rieFsX4j1X3Qqxc3kEYDaLSEgmGmc26Fx4XmblnW5wYmkgEq_Gbz0Qax1bIq_tLi_K4mggE8QMQsAQvFMN8TeFkzNRhe7QqDSIc3KLVlkuRr6KwuDkVfJVPbFeW9LkeqLbPZF3E5tDZzjE47qVtF9oeeMo864Vt8GxuUfvPnxTN92m7lIPuUPKK0Fqtfvaev0-inLIBmO0Cd8v07eyf8-x4BOS_FJeHcXvKJ6ZN3MsT6ak6TMOR5KPrLb6KbFXLK8NArN_Zb3aj0Icf4TWP4mo4jXcg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2894def8.mp4?token=J2r_Vr3RfKQji-ANv_sm4mhIkjJ25r6xA0z4DLPgXiR7rpdw9sgS4iAQ1rieFsX4j1X3Qqxc3kEYDaLSEgmGmc26Fx4XmblnW5wYmkgEq_Gbz0Qax1bIq_tLi_K4mggE8QMQsAQvFMN8TeFkzNRhe7QqDSIc3KLVlkuRr6KwuDkVfJVPbFeW9LkeqLbPZF3E5tDZzjE47qVtF9oeeMo864Vt8GxuUfvPnxTN92m7lIPuUPKK0Fqtfvaev0-inLIBmO0Cd8v07eyf8-x4BOS_FJeHcXvKJ6ZN3MsT6ak6TMOR5KPrLb6KbFXLK8NArN_Zb3aj0Icf4TWP4mo4jXcg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای مهیب در پی آتش‌سوزی گسترده در افغانستان
🔴
وقوع یک حریق بزرگ در یک فروشگاه عرضه گاز و سوخت در شهر جاغوری افغانستان، منجر به سلسله انفجارهای پیاپی و هولناک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/145429" target="_blank">📅 19:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
طالبان: تظاهرات نکنید، این در اسلام معنا ندارد و اتلاف وقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/145428" target="_blank">📅 19:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145427">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3352446383.mp4?token=PxksajZtkxoL3vzLH-0QjBbSebdEijBQbCqZ671ZpsL6gwlZiwXiBQjYRHlngkO4BX0MG2QoUj3pQvzloQ1wBkz5uEgjwRdiYox-RuXlaVTEMOBNfs87KN-mfhVzTIvUhmbyG_SC5d4-FvPdvu1-SNzr35Z20eRbIEEMG1fNfLrZA_x--wVz4KOiN60l1X_Fzrr3TtHJas4xRCEBhhBRv_mM0PvRSeSi5w7zTqXFRpekXWsEubfo3WgzO-61AF95ZmdJLoUD4JSey76-JTCB-uKHKpBentPfZ9Hp5AaNwD2dNxg0oO-7wNfLQnQv27hLv4dQIOF_1JWGq8ErPv52Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3352446383.mp4?token=PxksajZtkxoL3vzLH-0QjBbSebdEijBQbCqZ671ZpsL6gwlZiwXiBQjYRHlngkO4BX0MG2QoUj3pQvzloQ1wBkz5uEgjwRdiYox-RuXlaVTEMOBNfs87KN-mfhVzTIvUhmbyG_SC5d4-FvPdvu1-SNzr35Z20eRbIEEMG1fNfLrZA_x--wVz4KOiN60l1X_Fzrr3TtHJas4xRCEBhhBRv_mM0PvRSeSi5w7zTqXFRpekXWsEubfo3WgzO-61AF95ZmdJLoUD4JSey76-JTCB-uKHKpBentPfZ9Hp5AaNwD2dNxg0oO-7wNfLQnQv27hLv4dQIOF_1JWGq8ErPv52Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه رویایی را هنوز در سر دارید؟
🔴
وزیر امنیت ملی، بن گویر: امیدوارم بتوانیم مردم را تشویق کنیم تا غزه را ترک کنند، چه با اتوبوس، هواپیما یا کاروان. فکر می‌کنم این کار مشکل را حل خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/145427" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145426">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=dbet3mpfYTHGArGkJdu2EB-xiKPnwEQ_Pa-zZK-XEgfq_x_7z8FcV543Gui5OnDz12wQJEDOwDO62zQEesKLY4Q7TzpcY4W3arx9WucrZLoh1Ya6A_E80Y71GFvhtPJHVREH31-rIqVLYEEmfXw7TiOPKvbxXGSRYrrS0kLragAdWUCKyYbdud5u2FueRajrQ67vmQFArZL77F_PlMwVCtKp--dXuyNvwTwhDIyAJkV3R4n02-ijjKF7fITIVU_i64NAePQqGr-hE5ue3C3AgJWLCQyzbwodDUSd6aH4DE4LNzgD7JIH7URwgu6ykH8rdRf_Xcdwy55nH11uC_R42w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=dbet3mpfYTHGArGkJdu2EB-xiKPnwEQ_Pa-zZK-XEgfq_x_7z8FcV543Gui5OnDz12wQJEDOwDO62zQEesKLY4Q7TzpcY4W3arx9WucrZLoh1Ya6A_E80Y71GFvhtPJHVREH31-rIqVLYEEmfXw7TiOPKvbxXGSRYrrS0kLragAdWUCKyYbdud5u2FueRajrQ67vmQFArZL77F_PlMwVCtKp--dXuyNvwTwhDIyAJkV3R4n02-ijjKF7fITIVU_i64NAePQqGr-hE5ue3C3AgJWLCQyzbwodDUSd6aH4DE4LNzgD7JIH7URwgu6ykH8rdRf_Xcdwy55nH11uC_R42w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
آنها واقعاً ده بار تلاش کردند تا من را ترور کنند.
🔴
من بیشترین محافظت را در بین تمام وزیران اسرائیل دارم و وزیر مورد تهدیدترین در اسرائیل هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/145426" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=GD5UbN7FyFWxtFQ_TAJ3BR4bBh3-HyJ3rVY6SsLbT0KYSj3z2FDwqZtbgVheTfP_rN210-h88OQT-ozzwwku5Cceb7VFXhjH4TCYM9FrHcSwooDkxKGqrYMnvp_JZTMzhMeCGmLTbfkgVtNVI3dmh8AXUySdlH1BIzeUondWHfzhKLkN3F9aSGTs8LGNzPeVb7EOCamS6o1D-2pmP0pbiXZeRPaMIzr6Iu1B_x0XcO8wMha9dNDhNqX3SU7oupXwvuf30C9bspjnyaIxyWPrjE-4O2cr_0IjQci-MxJd4nXRh2KV_8NJhUxjHO1xb8jTQJbaaRxejTDmYLYUexRCbprfP5JcOqPBGIs2bYWXyHUdmiYaQLZvc1ySffKqaLxipFn4MnuQk0duD2UwetT9ZuD-gpZdLfjFy8NPQF43aUArcWenq7IBFXGJoyB-3WkUPEPI7wGL7N2XE11stuezetR72W9n8vGEkNAZU3giBaeubH5CtIt-Ghu2TtV4lWelrusd17trn77nHwii3F8L-hVn5LRIMNEPRTvMatMU0YLnaLW2KLNrE1-RKrXaCjsAh7gMF2cz6zLmSQQAuCIpxcCwcR9TqAN6RO2CgnT-FPxgBmahnkzBEIkG6ZVZqdk5u2QTxVgbd7ov-Vs5QJSBhsQVmUYaZkqjLyGpNVTbzMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=GD5UbN7FyFWxtFQ_TAJ3BR4bBh3-HyJ3rVY6SsLbT0KYSj3z2FDwqZtbgVheTfP_rN210-h88OQT-ozzwwku5Cceb7VFXhjH4TCYM9FrHcSwooDkxKGqrYMnvp_JZTMzhMeCGmLTbfkgVtNVI3dmh8AXUySdlH1BIzeUondWHfzhKLkN3F9aSGTs8LGNzPeVb7EOCamS6o1D-2pmP0pbiXZeRPaMIzr6Iu1B_x0XcO8wMha9dNDhNqX3SU7oupXwvuf30C9bspjnyaIxyWPrjE-4O2cr_0IjQci-MxJd4nXRh2KV_8NJhUxjHO1xb8jTQJbaaRxejTDmYLYUexRCbprfP5JcOqPBGIs2bYWXyHUdmiYaQLZvc1ySffKqaLxipFn4MnuQk0duD2UwetT9ZuD-gpZdLfjFy8NPQF43aUArcWenq7IBFXGJoyB-3WkUPEPI7wGL7N2XE11stuezetR72W9n8vGEkNAZU3giBaeubH5CtIt-Ghu2TtV4lWelrusd17trn77nHwii3F8L-hVn5LRIMNEPRTvMatMU0YLnaLW2KLNrE1-RKrXaCjsAh7gMF2cz6zLmSQQAuCIpxcCwcR9TqAN6RO2CgnT-FPxgBmahnkzBEIkG6ZVZqdk5u2QTxVgbd7ov-Vs5QJSBhsQVmUYaZkqjLyGpNVTbzMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
زندانیان تروریست از تمساح‌ها می‌ترسند. آن‌ها می‌ترسند.
🔴
من می‌خواهم آن‌ها بترسند. من این‌گونه می‌خواهم. این همان حکومت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145425" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به گزارش اکونومیست، دونالد ترامپ توافق نفتی با ونزوئلا را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده و مدعی شده این توافق به آمریکا «سلطه انرژی» خواهد داد.
🔴
اکونومیست این توافق را جسورانه توصیف کرده، اما هم‌زمان نسبت به ابعاد و پیامدهای آن انتقادهایی مطرح کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/145424" target="_blank">📅 19:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
معاون امور زنان رئیس‌جمهور: مصوبه صدور گواهینامه موتور برای بانوان نهایی شد؛ پلیس راهور مکلف به اجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/145423" target="_blank">📅 18:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsnbdXRV0uNjQuIyMhKyyFmF7S2FqCS8Ag1D2bgFNCKFN4tAncD7LjL1NpHZ8R59SPXLTaiGOxTnhagn9wWgQ0DI7R0xrw01tWZvghDpswcjypKTorLDum9RFSYfPHbI0gJcgpPWbPnmILY_QghGy26GXfQGew4GBiMw_a66_yEyi-nlnC6u7gCbCvOTqQ4laSrzsEtEznzSlou0uBDhVU52MZ4MRtb3URJWfreHQyfwe4FERoTfX-xZjgNg2cI4_CZqST89pfm_3B4C95a3R0j-7rmHam2HacRaIxWyrx1Ms0J8Su8rJ_92S66m7PaLJEpHhdedQmjC8kEoMHruaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «برای سیاستمداران کانادایی، مثل نخست‌وزیر کارنی، خیلی راحت است که دونالد ترامپ را «دشمن» معرفی کنند؛ اما وقتی اقتصادشان فروبپاشد، این کار از نظر سیاسی به‌شدت به ضررشان تمام خواهد شد؛ بدتر از هر اتفاقی که تاکنون برای یک سیاستمدار کانادایی رخ داده است
🔴
فقط تماشا کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145422" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVB_GMdKwkDT6LY2mqEAyvJSJ7YKIAdB7pmX2ciNQJmy2F_crxPVZJeGIUaAMbNqjIK2o6A8uSpsjqjPbGljupffBsCkbd-UfygkovwqiAZrQvKOSkZTZW0pcYtRfJSDmy5us4x3CmGQKaU1l3jlCpciRt6ENt_yoz5qscmsfdbY68KWnnBOXLYco0sV4dVbi2mBo0GOLH3A-pexT-j0sDfc6rpRoFRkH0P-mKiX8V4zgIhDwbOul8aMJWToY_T4t0WngA315MW-0FFglGnV0xCmMH_a0_3kKpsmoVjgq_1ixBWG98Di2q5koA67C7b_dZt9UV6u7pvXEZUIpSn3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
افراد و رسانه‌هایی که مدام بر این موضوع تاکید می‌کنند که ما هیچ مهماتی نداریم (و آن‌ها ۱۰۰٪ اشتباه می‌کنند!)، در واقع خائن هستند.
🔴
آن‌ها این کار را انجام می‌دهند زیرا ترجیح می‌دهند ایالات متحده یک جنگ را ببازد، در حالی که ما به راحتی می‌توانیم آن را ببریم، تا اینکه من پیروز شوم
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145421" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/145420" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AChqmfafpmW9IWIeeuOjww6LQZ9YolDh4_3oisKMot3dRwBvpRd-s028_7MpuzhxLuhiDQthHg5ra4VbkdJnQ0u-arKOdF5oh5jatd8985_x_k1HNLPHtt3DVPmJaB6irzD9vi7ZGxwp5_2GJ8kkRD1dXDdffTiQRf6Dgfb1eDPGyrKVx2uk0gl8a4YHesh0IKuWtptRTX4FJ6QQOY2hSKffqKH2egyu9shfNlQcBE1-INhvQuOQTZTZ0PuTDzK0vMZhFu_dxm77WEEXIAVdWHN8fWSdH3FOTH6ifOLFByFoH39KVOdLoe2toNjjQV3i5vN-SKfKnXC-ZcYlScd91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145419" target="_blank">📅 18:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Noh3OoTitIzt1snPAgoWG4hVwqIzh_bBFvNkKBoMtrH6CGKICreUHHrf1oOqxokhYoeav-RoFSDFdruUnau8pTnFcqtFC7xw2n51ECB80b9NeA0QQQ-mj7Z3LyNVOPDvYDvLFJTD0FXJL7Zpy8t2ZOZIUPebX65SN5tBKDirxJo7k1exz8yYWMv9_3Wgbbv6SyP7zoMMOZa97QABXJ9qgcVaCR8swpl0lrd3JRZ2ahmDiqOtsbSAZ1VWLEaS-0isCbUD5MWIojpo_U9sX93LrInp4rt-6AINgFTIv8YWD1I1rjtjJEmLXbqBNfPRC86IckLO-kN5p6EVL1M4Z01kSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در هفته‌های اخیر، ارتش روسیه به‌طور بیشتری به داخل روستای کوزاچا لوپان پیش رفته و همچنین به گسترش منطقه بافر خود در استان خارکوف در امتداد مرز بین‌المللی ادامه داده است
🔴
رسانه‌ها تصاویری از نیروهای روسی منتشر کرده‌اند که در بخش‌های جنوبی، شرقی و غربی کوزاچا لوپان پرچم‌های خود را تکان می‌دهند؛ همچنین ویدیوهایی از نفوذ پرسنل روسی به روستای کودیووکا نیز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/145418" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رسانه اسرائیلی: موشک‌های ایران به هتل نیروهای آمریکا در اردن اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/145417" target="_blank">📅 18:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=FI95dRb2aMRvmDWbs7wF_koiliOnXDtvSmb6odr_Mu_2eD1gp2hnRZtITRLalEIqwnnNNfMP4cFh_lAUm4pldDdW66DvLcXe_C2DfOmYAxKZmR0w7heeRFQsZgGOyeD-8vCqOVm2WNIlp80t9hDlKHvvufMHBPTLaSaHr8m7gXJGvV9UVc60AYP3VvFzDWK-jR-Ms2ddoA2ym7cmypub2FUD1toHMs0qcF3h7Rr0mcHK5XLHCnvmOairMyJ5K7i9lEAWPbmyWKNNa9hNlwvy6oGpYp2NQk5jTaDqH3E3DNdqZVM2rBZq9TZRxSTI1UVgEzYJxjDH1kpPiOyWcPkt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=FI95dRb2aMRvmDWbs7wF_koiliOnXDtvSmb6odr_Mu_2eD1gp2hnRZtITRLalEIqwnnNNfMP4cFh_lAUm4pldDdW66DvLcXe_C2DfOmYAxKZmR0w7heeRFQsZgGOyeD-8vCqOVm2WNIlp80t9hDlKHvvufMHBPTLaSaHr8m7gXJGvV9UVc60AYP3VvFzDWK-jR-Ms2ddoA2ym7cmypub2FUD1toHMs0qcF3h7Rr0mcHK5XLHCnvmOairMyJ5K7i9lEAWPbmyWKNNa9hNlwvy6oGpYp2NQk5jTaDqH3E3DNdqZVM2rBZq9TZRxSTI1UVgEzYJxjDH1kpPiOyWcPkt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری مهم از آخرین ویدئوی منتشر شده توسط انصارالله که نشان‌دهنده اصابت یک بمب خمپاره‌ای پرتاب شده از راکت "روجوم" به یک وانت در حال حرکت است که متعلق به نیروهای حامی دولت قانونی یمن (PLC) می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/145416" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=J10_6hXJhFWhcd9Cm1Zvlwg5mTxw89L0WQfVz_LzOal2Zhv05Vjhu12Bnyy7oBe4pFP0AS25r8-RMl2rqiLUt632DWms-O7bQ4oZSMxwRqNLDaRm9sTSb57s0wcx9S3h3w-UCTyr-sH0DGZYTx03Np3tASCy0DcG81sTufGdjOg7dTOyFO2fa9r4u31VX0AlobWvXYdM2fNHNtgygio8QRsWWi8m4v3n4wex0Xy-q1Uipb8In_3GEuC5gaNfrcWl6sqQqBVE0yf7iLpBrqfY_IaL3E0G-dJpWDt7i7GrwFGoo_E3PxVD28CD9p8YKVIARqsYY5_DagPqvUCEKf3H8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=J10_6hXJhFWhcd9Cm1Zvlwg5mTxw89L0WQfVz_LzOal2Zhv05Vjhu12Bnyy7oBe4pFP0AS25r8-RMl2rqiLUt632DWms-O7bQ4oZSMxwRqNLDaRm9sTSb57s0wcx9S3h3w-UCTyr-sH0DGZYTx03Np3tASCy0DcG81sTufGdjOg7dTOyFO2fa9r4u31VX0AlobWvXYdM2fNHNtgygio8QRsWWi8m4v3n4wex0Xy-q1Uipb8In_3GEuC5gaNfrcWl6sqQqBVE0yf7iLpBrqfY_IaL3E0G-dJpWDt7i7GrwFGoo_E3PxVD28CD9p8YKVIARqsYY5_DagPqvUCEKf3H8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گوشی اقتصادی a17 سامسونگ از ۱۵ میلیون پارسال، شد ۹۷ میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/145415" target="_blank">📅 18:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان مدیریت بحران کشور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhQGjc9pmgC9yTI2LeQhoN1y698uhqEIUCO3l0GtcSIvxLmg2AAfqOeVaAD2cuVsTL1GRL85t5cL1IkgLJFqadyFJjq5pWLExgXKzhPQ0CG_KbIqjmgPrfneZzfSYXl7hdzfk4DyTEjDHMBCeT3Sci4tviEwrpD8aN-LHpnbOVb5DtcGwyS-t9XwtS5_eifACKk6QJgCBW_nfZE0JMt8rQMwQuqUSNcaL_OrC30THE0Qn3Azgd8uGJ4gY32Mi6_p4HLiWsQZX4FfvuhxWhUyONAwtafOxHyb3t7WJmUpqyU4ExsL687THkAygH6AI0Tc-X6ddllJyGQQ7eKYimuO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه بانک مرکزی</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145414" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جنبش انصارالله تصاویری را منتشر کرده است که نشان می‌دهد نارنجک‌های خمپاره‌ای از پهپادهای "روجوم" به سمت نیروها، وانت‌ها و خودروهای زرهی طرفدار شورای انتقالی جنوب یمن (PLC) در نقاط مختلف خط مقدم درگیری بین انصارالله و PLC پرتاب شده‌اند.
🔴
خودروهای زرهی مورد اصابت شامل یک تانک اصلی مدل T-62، یک نفربر زرهی مدل BTR-40 و یک خودروی گشت زرهی مدل BDRM-2 هستند که همگی از نوع خودروهای زرهی طراحی‌شده توسط اتحاد جماهیر شوروی سابق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/145413" target="_blank">📅 18:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145410">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daad725d95.mp4?token=RBXl3iD7li7VlBFrAk_xtfi6Zm_OC_KU2tsWVBFLyjvnLkMqOtNKDuCNrlgYk85wknhvbfixkMkUWN2okxVDm_PRoDOZXzJNQBwj0tY4Z4iYfLpfbpnt-wHLSk-LOX9j1HsCbvYYIuQ_0krt5b6GzpvOKsahTcQ0BeMBtDbz2Te-6QugFiqr2HzOpSg6r4bWGTSClK4wW0w9RVJab944EJQp24MGoHImGmjP1HfKZa3nlk5u9iH1WYapiLGVvdL5Hfvj1WrEh_UKcCkRSFoFkkWBR5j9dmo3UXD5jjG0MC263vPVHs_-QnUG6K8XZQYNHcB0FX8L22ct1gLhfpG78g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daad725d95.mp4?token=RBXl3iD7li7VlBFrAk_xtfi6Zm_OC_KU2tsWVBFLyjvnLkMqOtNKDuCNrlgYk85wknhvbfixkMkUWN2okxVDm_PRoDOZXzJNQBwj0tY4Z4iYfLpfbpnt-wHLSk-LOX9j1HsCbvYYIuQ_0krt5b6GzpvOKsahTcQ0BeMBtDbz2Te-6QugFiqr2HzOpSg6r4bWGTSClK4wW0w9RVJab944EJQp24MGoHImGmjP1HfKZa3nlk5u9iH1WYapiLGVvdL5Hfvj1WrEh_UKcCkRSFoFkkWBR5j9dmo3UXD5jjG0MC263vPVHs_-QnUG6K8XZQYNHcB0FX8L22ct1gLhfpG78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی اوکراین امروز، یک عملیات تهاجمی با استفاده از پهپادهای دریایی علیه کشتی باری روسی به نام "نفریت" در شهر بندری سوچی انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/145410" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145409">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یه قاتل فراری تو بیمارستان شناسایی میشه و اینجوری با چاقو چندتا مامور رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/145409" target="_blank">📅 17:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روبیو: یه زمانی واقعاً این تصور وجود داشت که کل دنیا تبدیل به دموکراسی‌های مبتنی بر اقتصاد آزاد می‌شه و همه کشورها شبیه ما خواهند شد.
🔴
اما واقعیت چیز دیگه‌ای رو نشون داد.
🔴
کشورها و دولت‌های ملی هنوز اهمیت دارن. ملی‌گرایی هنوز واقعیه.
🔴
مرزهای کشورها هم همچنان اهمیت دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145408" target="_blank">📅 17:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=cdgXCSfiXizfPdcLQZFAVZFtdy-mXuwBFVanu0ss9Lh4J1PmrYPyLCAO4uwUctdCnr1mTZCzhRs9c7UnA6f5UgKtSM3rPDv35xXdCuR_5oAAyuSIzAGMUHQhJ7Ef4Khas9ax-c_Koy4leYqXoJVuJhTDqiGkwxd0UOqpFqSeQLAVWnnPorw2ihdphfwkBw36n6gupq8xUT_aWrnRTlnJAc_Ocqq5cOtY9wpWRi5YGRdi0SONALNys20VVvbc3BAnRl5xxzn-QMY7zlA7zXANlef1vShIWvp06g7VXXCISFVRewD57IpUQQ7jFQQGpOnjw2MHcWsCaj0emx5GAyOu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=cdgXCSfiXizfPdcLQZFAVZFtdy-mXuwBFVanu0ss9Lh4J1PmrYPyLCAO4uwUctdCnr1mTZCzhRs9c7UnA6f5UgKtSM3rPDv35xXdCuR_5oAAyuSIzAGMUHQhJ7Ef4Khas9ax-c_Koy4leYqXoJVuJhTDqiGkwxd0UOqpFqSeQLAVWnnPorw2ihdphfwkBw36n6gupq8xUT_aWrnRTlnJAc_Ocqq5cOtY9wpWRi5YGRdi0SONALNys20VVvbc3BAnRl5xxzn-QMY7zlA7zXANlef1vShIWvp06g7VXXCISFVRewD57IpUQQ7jFQQGpOnjw2MHcWsCaj0emx5GAyOu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: نمی‌شه یک اقتصاد رو کاملاً بر پایه خدمات اداره کرد.
🔴
باید یک پایه و اساس از تولید و ساخت کالا هم داشته باشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/145407" target="_blank">📅 17:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
چین: به شدت از تحریم‌های مرتبط با ایران که علیه ما اعمال شده، ابراز تاسف می‌کنیم و قاطعانه با آن‌ها مخالف هستیم
🔴
از آمریکا می‌خواهیم فوراً رویه‌های نادرست خود را اصلاح و تحریم‌ها علیه شرکت‌ها و افراد چینی مربوطه را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/145406" target="_blank">📅 17:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه الجزیره گفت که پایگاه‌های نظامی آمریکا در این منطقه، از جمله پایگاه‌های مستقر در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران، "تحت هیچ‌گونه حمله‌ای قرار نگرفتند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/145405" target="_blank">📅 17:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F7887ibbS0NnlYvl93PC4o5n3Qq2oyeUj5AsP9BATs_KN0b7gN7PAoD0fHbvLDypF-h0XjKAgYeN_XvAhO2LxHFMHYIjtOktvDrsCDFOu9kv8XHQo1cHxmn5w6Hg88ih4fbnLbaZgbRlDwX5gFmszYtLDmqWKhjzQB2uPmyldnHMqTSLiTkQYM435D4tpSo8KPyPIZy0ECtSGlKm7mDE3g6HBKy2Ch269uJal7BOjqnV8dop3LCrikVRrGmF0D6_PB8wviW_zSJyHxfQtgEB56unln7TOALCRgngEMJ4Zh3RDaQAdfQPL8g1aT22ylDjNhXyLdnlsDP1GtOHqQKqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان حمایت مالی جدیدی از بانک مرکزی یمن متعهد شده که هدفش تثبیت اقتصاد یمن، افزایش شفافیت دولت و حمایت از توسعه اقتصادی و اجتماعی این کشوره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145404" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145403" target="_blank">📅 17:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز درباره ۳ گزینه ایران در صورت ازسرگیری جنگ
🔴
از حمله به تأسیسات نفت و گاز، نیروگاه‌ها و آب‌شیرین‌کن‌ها تا تهاجم مستقیم یا غیر مستقیم در کشور‌های غربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/145402" target="_blank">📅 17:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145401" target="_blank">📅 17:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145399">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIEINDQ_-JxUX6ipLUhhf-VX-kJMOqTA5PDT1VZJzND428J1wDpdRY_u39pakz4hly0R0d6-3WlfBhAhfb5dgbfFmnkJU6Xi_BdI_XoaYoDCNdUbJCkiuGo-xJSFJct1nZX6pLtSHq8eIK0d9GSiO6I8W9uWPRA16zvj0xmm0nSxQ0_vCM-7FiMPfNNI8cZsXex8xnoDCjnwrajGW3ZYm4oISJG2uj6yoWFgPZ6Sbz4xWjsL4NYeRIHP4F5q9RKi_0AtxTuxDfMA_Jj2PhjYO0E01gEIfUFJ6EFxAgL_tfZ0hc83W__DFxPSvwxc4qQKlpKOB_RXeBT0bY2e0L3q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCLMS7O2xY48y2V99EvMuYnyhtlbEuC56MX94FQR0n_KoQvmAb3u5ZMQC7_9gdHbjn7AnwM68hHLfBEhfJ9sGcgCNmN983k2t0UBv6EbR8fcZq5DQWyZn1y_PczZhRhXa91MtxbljmLv0qPp-gvYtjHUp88mdt1zKdr3zQG1YYWcvTgqbpNmEwqFC34BVdSn85MzHD9CrhjZTje2tNKv8VZUp7DY_SF0-kFdsP5sPBeW6Q79_DxOH0mjOQC-0O508ALp64P6yqK3jEDZiKBI9Hhk8Lz0vneGkU71SN1G_EI9D_W4Fr0OmY0J-LTWOZ0y3eFj2KPZLMndT7qQwunfsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری هدف قرار دادن یک مخزن نفت در پایتخت لیبی، طرابلس، در نزدیکی فرودگاه شهر را بر عهده داشت، اما نتوانست به هدف خود برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/145399" target="_blank">📅 17:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145398">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=JL1AIUtDNjPVzNafAd2bZb9tOeg-M9T57KydDq69F65kePu0gL3uFhQEzJ8vvM1MNXGFdRvYa2nTHtliPz6Gl_YclVXmvGOrEv7EQC9XW__XOXqYFLe7X05LwVYeTqjfEgiTOeMgaBpQyL-rVG3QFRyzmq01jXGblwvOcPXAFkadxvCxwFymydvxKIy1_rc3PPIPaoqQ5Uk8BB5xgEg9eRLknSfHvM-HioHRMe2Kk0jBfIr_d-GiGcKKPs4eFqRBRaGm3b-nMbh6V0Sk-7hTLjatVC17Bj71CwXnWW6QDERO3W0APSmZGHc5LyCsLxaTct4mwj0722SxlQG29ZrsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=JL1AIUtDNjPVzNafAd2bZb9tOeg-M9T57KydDq69F65kePu0gL3uFhQEzJ8vvM1MNXGFdRvYa2nTHtliPz6Gl_YclVXmvGOrEv7EQC9XW__XOXqYFLe7X05LwVYeTqjfEgiTOeMgaBpQyL-rVG3QFRyzmq01jXGblwvOcPXAFkadxvCxwFymydvxKIy1_rc3PPIPaoqQ5Uk8BB5xgEg9eRLknSfHvM-HioHRMe2Kk0jBfIr_d-GiGcKKPs4eFqRBRaGm3b-nMbh6V0Sk-7hTLjatVC17Bj71CwXnWW6QDERO3W0APSmZGHc5LyCsLxaTct4mwj0722SxlQG29ZrsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: ما تا یک سال دیگه بیشتر زجر نداریم؛ یا در این یک سال از نظر معیشتی نابود می‌شویم، یا قدرتمند می‌ایستیم و از این یک سال عبور می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/145398" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145397">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد؛ مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/145397" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=sMtT42qMFek9sUcbR9cl7dLL1wGQI7dWnKWTwzS3wcC-DaU682YyCsDBsI8RqAxtpeRf8-5skjqGLzQgsxvnwW6GGd8ou6mwqkhVG16QkyXgFPJaS2ElpiYf53M9UltGu9ypOzim2IOVUO8_7wiMId_voaKSub0DstGVIFOX8FTeO4K1S_xYzA4st9UFMIg247x2bwKGOJpWAbqb-JpFdPtRdGHIL1Pkgo-88ZKbrDgf19CEL9NbNQ38098hRI3v-0j8Wf2-tz_W2nGmR1mxVRnrPA3U_kJud-7tvMqgIm69xDr0mXvuPQNosB2qehVKS0DsHYOFUjULzCruThheOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=sMtT42qMFek9sUcbR9cl7dLL1wGQI7dWnKWTwzS3wcC-DaU682YyCsDBsI8RqAxtpeRf8-5skjqGLzQgsxvnwW6GGd8ou6mwqkhVG16QkyXgFPJaS2ElpiYf53M9UltGu9ypOzim2IOVUO8_7wiMId_voaKSub0DstGVIFOX8FTeO4K1S_xYzA4st9UFMIg247x2bwKGOJpWAbqb-JpFdPtRdGHIL1Pkgo-88ZKbrDgf19CEL9NbNQ38098hRI3v-0j8Wf2-tz_W2nGmR1mxVRnrPA3U_kJud-7tvMqgIm69xDr0mXvuPQNosB2qehVKS0DsHYOFUjULzCruThheOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خدمه‌ ناو هواپیمابر آبراهام لینکلن که چندین ماه در خلیج فارس و چندین ماه در ونزوئلا حضور داشتن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن چند روزی رو در خشکی عشقو حال کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/145396" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
معاون ارتش: توانمندی حملۀ پیش‌دستانه را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/145395" target="_blank">📅 16:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک مقام آمریکایی: پایگاه‌های ما در هیچ کجا، از جمله کویت، در حملات دیشب ایران مورد اصابت قرار نگرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/145394" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بلومبرگ: اگر قیمت‌های بالای نفت تا تابستان ۲۰۲۷ ادامه پیدا کند، بهای بلیت‌های پروازی در اروپا به طور محسوسی افزایش خواهد یافت و برخی شرکت‌های هواپیمایی ورشکست می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/145393" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نتانیاهو اعلام کرد که ۵ غیرنظامی لبنانی در ازای آزادی اجساد یهودیان در لبنان، آزاد خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/145392" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/145391" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
