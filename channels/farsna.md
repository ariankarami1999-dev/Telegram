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
<img src="https://cdn4.telesco.pe/file/feQ5gweKXRTTLlIkPy4OJYukUkRBlwVkBjaHl9NTXXWDzucmx5enJqo4lVGKBAkfCLhyn9yQljcK4SuF88Z2qJqRlJ_1uVQJB3YOGVrkgAhRDMdYV6bhdd7wZRGG28tmkIhERAsLtnaT3YHI90d6XHdmODYBpSe28SYXQQnOTD0DZ-oPSM_mWqAp-oTHhdsjAHUoGAl0_81he7aTZZPOfzXIZZxU7X7ucDH1WNsF8IWRwmR7cuuGN_o-gmN32yRe8dSALQd6IJsKnOWm1KUVf6weQMIRvtyFrgUPD75utZUclJW6kz5iDqyIBiShV_PoOyxO-UhPIyarD3qShxxdBQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-450680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۶.pdf</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/farsna/450680" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/450680" target="_blank">📅 20:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV_veFJJl9vVaQZ6GmazzO96r7zP04finUWlrE8fHtlQ0Me1XkHu2EDqy4KYRgLRuriNT4Yne0x0xA5oGlWe91HiKyzv4cqQ_TZx2ipLzsxuhm4KUYOhig0uH0gktfCYLd1J_WWhyVMGv-kHc9dJMV4HMdgwQpOJWiykq_QanlCqBaVMpTLeNWq_uOn76uQ6veSY8XwjCiwizjl2ZQkO2iAAHF2kTTLwTHSLsvTYTxxug_0Yl-Sr9juC7mwDxoCT94CpSt-9KBwIHuPiuGE4kltuOYtoMA6_4pcKP2CU3kqIdKHSPFhkwTo6tNAn85Lj4ZzP4tmKdTXa8TQ1m5Wmhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxhPv1-7u9mVFH3Ixzq1b-V186tjszSF--0YfFaeJkG1rrqWoF0oZXvtcy2hoZxAfoKCZLqGjhU0a-3uBBq7t37C60W7NYZKBDhWWTZA0hm-Y2i3MNm96wIW3PC2ku-1yQTqdnAyxjFSSwQYvKJihUYiBPIVtrHxqGZVH9MaqDvJv1BHVKwQhVsKrdEO3q5iqqQeZ4q5dBtB5hcjE2Tr00lj1O_J0ZpmFnIkFM70JC7yTPPpY7Oo56y4n2mACojDUtbKR5rtv30c7GwSx7g6Dkpeva1Dz_pY-dRauWRDVOxEGf7Pz2Jeb5_crYUz1xiEs6yCvjlESMmE7EfFOnVfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fVMvDLp0bjrc8IsytOrRNlf6sXXi1CZ3Tp2FV0ILz7UMZGvQZCbtLANwYUgOOr0qmZxkFKKYEGdB_m9XzN1xxbRz6krUADvCUDoyzyNwz22YTH3pD1jWW42CM6es8M-VwlSju8vXzsIcm-A02vz6S9VKlOy8J_SO1Fhi6ztPwpKZkUH7wnePWe2UZszNMU1Q_gG2VQ3BAzNY0hngEWjheupfO6RulOHKN9GOMdXsh9XCuwVZtuwa_w4t6xT0FAQhKVcJD7_IMFwN8zM5WS--YAlsrRvO9QSPvaGzIP1Gas94Bip7Bi_JTaOCFJXueez6oDdslLQFB5qynoz4AP95Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1SL37wqtWp9LnLD4kgAP13_7MwIlfp5ylcdN6gNJhpG5R5ux8URrGPGIRreyCBqMKssigGJBXSIAkHoDdX29Bon19oFOBsVVVjFtw42pfX--eol51IXi9iyJjgklBXnd08BEf3n7GYxqIOmPJA87BOnnLnC0l8DpL4stqiPrZbKpl-tW9F2XJVkuW1z_xA74NgPHpMhZlAiZBmSNML1JQruTlMrg_DTagde8HYZpVj4CXT3L-Ht5hO2NSyHDbc7gZinDd2PN3zC4ze0tcfmAoB0b99Z3mEHZPb9nP_NTVfgp59cbGE_Ugvpt7dQIERoXWkxZFKe6EVsFxs_znVD6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از جنایت آمریکا‌ در حمله به پل‌‌های مسیر بندرعباس-لار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/450676" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملۀ آمریکا به نفتکش ایرانی در جزیره خارک
🔹
معاون استاندار بوشهر:  نفتکش «بلما ان‌آی۲۲» که ۲ روز پیش هم مورداصابت قرار گرفته بود، امروز هم موردحملۀ ۲ موشک آمریکایی قرار گرفت.
🔹
این نفتکش که تانکر آن خالی بود در جزیره خارک پهلو گرفته بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/450675" target="_blank">📅 20:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMTKZ6d7ovNs2cLeTE3Wltxsmz0FoMzvfVbQbLC00m6BtivrqEjC0DXDEt_TE6iBb38kwGqwOoHvpJ8O4vpLlVyjrDtKzRnN8k-nM-ZbFZ7UIq4X0cfz5CCzYqByy7nQF--JDaqk-HUKSpAo7CEvLyglRHnoasl1IUiCs-CmfZhPcOYuB0nkpSpFBcYNmRAdyCHM-469HIxJSGAV9dm3Q_fLL3ss9vFZieMW-MQBSDirIlso75ej7usJfsrhAl5wjWbh-J27aweSAhfRMsIwOs0qvNNbm52CiepJaivTL5I98trWU2CLFSz6PtLDSWCPUegjZpQpvoK99kD4m8qtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی تا جام ملت‌ها ماندنی شد
⚽️
تاج، رئیس فدراسیون فوتبال: آقای قلعه‌نویی باتوجه به مشکلات و محدودیت‌ها نتایج قابل‌قبولی کسب کرده و همکاری با ایشان فعلا ادامه پیدا خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/450674" target="_blank">📅 19:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acEOoh2ssohWRaNy6IxubDeYgWoyWddrjcjPzGez3PX6P8QI4lZXONJwQzwnl8SQ3onZMCYT4Imgwa0A1z1usZ0gDi2cQfHbX34kY30byYyzcUDrd5U62Xm7DzgKabBgb29fFbs0j5-yXHYyWg3s-1dKNNhqNFlOOVBFMqkjYlM5JVDIZ7MsGt5v5rRw-HCqGhHIdMvEwNAyMx6iUvTrDZBpYrbG2WmJ8WfDTe7XGM5FnPUosrqu9U0IXKocWYPM5oP95vCs72YfNiF6xojTfGb4_vDBzB7E-lT7eJkJX5WSm0Uq3OAsE5VO-ZltJ3kG2tFiMFRPA0bkV6CcNVsasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
انهدام پهپاد آمریکایی آرکیو۱۱ در رامشیر
🔹
یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ ریون توسط آتش سبک سامانه پدافند هوایی سپاه در رامشیر رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/450673" target="_blank">📅 19:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n85UUlLosIOkuNGKn2mFMIe2O1ZGwctmK2qshTvfxBaCJttgzEziUoUMn7sU8rjmRnyTDv8DErXBJjRbRlmouD-eMXh6KkS_8z4q6AC73acSPsULYgnvyd97T_Hf-umkg8GfpVvKQOrgoytzRlpcKdRZu5LMOVk3FoUKI1T1V6_Ui1dql0QvlTGsRJT2am5E4KVon1FvmElQVnwn1H5oEchehQx28G8cENFklGqhItXOIIzrgsvn7Kvz6kaSgk01cETB8Bh0cC2MSnyfz2ieI6YxfEPB_9FTraQzrfMI_Dzo2u4A8HfN9eCqcZHmwj0rr6w8669PBBsLdP4o92NmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماهواره‌ای دیگری از آثار حملۀ ایران به انبار آمریکایی در مینا عبدالله کویت
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/450672" target="_blank">📅 19:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">وقتی تئوری انفعال با نقاب عقلانیت بازمی‌گردد
🔹
هر زمان که کشور در بزنگاه‌های حساس به اقتدار و همبستگی ملی نیاز دارد، بار دیگر همان روایت قدیمیِ عقب‌نشینی و انفعال با ادبیاتی آراسته و ظاهری مصلحانه مطرح می‌شود؛ روایتی که مقاومت را تندروی و امتیازدهی را عقلانیت معرفی می‌کند.
🔹
آیا آقای خاتمی نمی‌داند صلح زمانی معنا دارد که هر دو طرف اراده‌ای برای پایان دادن به درگیری داشته باشند و در برابر طرفی که فشار، تهدید و مطالبه‌های حداکثری را ادامه می‌دهد، عقب‌نشینی یک‌جانبه نه صلح، بلکه از دست دادن قدرت بازدارندگی است.
🔹
استناد به صلح امام حسن(ع) یا سیره امام سجاد(ع) برای توجیه انفعال سیاسی، بدون توجه به شرایط تاریخی آن دوران، برداشتی ناقص از تاریخ اسلام است.
🔹
اقتدار، وحدت ملی و حفظ بازدارندگی، لازمه عبور از بحران‌هاست. روایت‌هایی که انفعال را راه‌حل معرفی می‌کنند، با نقد و گفت‌وگوی جدی روبه‌رو هستند؛ چرا که تجربه نشان داده حفظ قدرت، شرط اصلی هر مذاکره یا صلح پایدار است.
🔸
متن کامل این مطلب را
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/450671" target="_blank">📅 19:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSXky0h4ebaGKh9L8DWRUawyfxLCRnB40iW_VcaBmYcXDSO8SboUIzupmUKFZw8BRZReQ4CjXDJlVKOiGeGdvXpmyQDx6suby9xhR-QNoGc9Py22sxlCADjLeQRFXfTklrzxmlVfIWzxxuFgXX6oWDeU8hn28ly7D3NoZ5192DsSbtliMMM-ma7h0pnhk6IZDzTNwX1mG9awxclUIO_jCFIkOOpuw4Xq9dcshr-CDv17TxSwpS01qZ5z4jtVYeHoJF9PrVMNnT-UC1XZVLNvjObvpD6UHsr_NM80-p12b9b91-jdhQq1A489y6dVSl4MXYV-ePZAo8J4TZ6NnmjcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Prb8hMvoO14LKSnCDcC0D6fMupyEs7ErQ0GIJcphvIXodp9NpeJUFDiUBfWbtN4bXp8WJgZKguKbRrCSdi7cgUp73SLLcsyhONke5qVtTzDBkhMFKPDRlp4sZUy7LRHtzilakKjAuAgr3Xosf8JeuhJ4fEecsnMaRvnsirr_IszAMN2nGf156o96fuv8n7XTkV7QmEqfM6EF5PRam_JiaWUtiK74NFNtzhIlDjr_m7q4cUZiomDXsVnoxALGZHspxHJdLW97kFUULPzRh4q0pialaG4kwvBzqDLJxlOcrH-SdR_l427s0GOyt9kwdoH8PSk2CzFlbxKv1sIp0CKIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIWtBexkFoqqgK9lO_ZGEZHqWMudgSPd0QHY-pt6ZU9_W6N5SzU7VxzgXK-AZdDrOr1qu-IPE1qD6Q2igrjK4Du6H-Sw0peJ-nRk4vPG2kVyWIRy0HJPHPSQIeZTRjkvPdnZMeka1BS-wPoj4R2MFlahKWAupMzA151UHuG4_8QrcN_owcnSQhS3ECEZ5isFplk5AgaRMYb5NLjL9Fgrhq_z4F_IzP_zt-X5uQFIMpIF36t_dS0CgoHhaiJp-7tMYDak758vgSysKqPX3rQNJey9B7PbW03Krw1rt2mIisHORS_RcUJpaSKn6gDsqZRwqUvVOw9b5q_rNqsVKJKDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COAwxR3E078P0wxsgESfD9I-OrFauOi7ibGYBFr0chmMloa9tO4udaO6uB3s2JKumQ6RzuTbMKVZ0vy15niIeLMJyp_dL0xvydEyOxO_TAgQYG7cgoZOmcnnWz6kKMtE2QvU1F07qmgQ63I6F80tbmG6HDwBq-uh_EhCjhXbT5tIUrStmfVjBrI08WYJgbyW9UBYp6DIcnUUeqtw-mAA7KF-1F23BPSpXfsZYQPbCs58_OzGyYn3b6F91Zzb3gNf7kOD1nhin0Cc2g-AD94aRESrh1YlWFxyHX4zY8cJ7uR8BmkGDzohciMy23KeG5YSSIweif_SOVBcbcdgI-VIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fh5vxedETtrhx5W9U0erHK8K65RETI0xiJ08WTPHg9IbfF0Z2VukrjRmIv3tnPOI0c3m9wQqV8p8BZM0YHsvEqNDzB8aprw9UTSHVRkujFqk_90MWNFtQSmtuLiqewgK7BfqVuns_gK_D21Z5UT6uXASFNx4IgkPybt9aDL-Sb2m9RExlHvfKENEjq9vcTJqHPDF7yJVXOWJINKiFXuTf34GAs8IghtRapRAyr6Dlr6x5QqkN8deW1yzDGD8QLtTkEwJncXIg4tXRYaCgsh0oJxf_AS_Sf3uVUWbfTln9m-KsGCBU2ZmZhB9GuACYndkqi1L6kVPdvQGim6e86rPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST0g1D1ByS2RY9eUGT8jLHvk6BgH8CmctuUIJtNB8dr8wnPLsb3csjUS2ytL-NTxsORfPYK7wduJfiikVnJqrwbCHpAgi_3DpOIZRtDrHiI42tWXim5dpfv4Vmaazt4kdTa7Q9kukiDcXrDZ__LWzOpc5KGGOzWsC7XN7ZBrI6_XrncyPF2Or9GKkfcaaOF7U1qezq3T6803fv34oYK4mPGaBgoyWUZMMLA7SoIQhV_v4GpbTUl9gErWGj-uJhvjWyjS94dCRfE4wQ4utH6PRElVgHS1JFsZJYPu751TloXQbZIDvJGRofP4kz8_IRUBW1UBWnh3BYxqKcVvG6am8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
به یاد بابا
🔹
مراسم یادبود رهبر شهید انقلاب در شیرخوارگاه حضرت آمنه(س).
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/450665" target="_blank">📅 19:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwjMDmJTSWnR-evwNVWh7o4O2rsRifQ85yvz8RDc0P86m0yRjKhTVEGpbdl2oBYeySr7ZcFE4VEfn-pZ9Fuo336akFq1KnCOLe6NRGfKazMYx2l9hstjDi2dZX08tUTO1lrUt00qQvKHipSJTigW4HFQs6E1F6_Q1VldkXobyAZ-hLh1fnlac_9rhxmxJa6nkczB7Tw2ousNH-cVFODRY4sDxhbGOGgdeYMOPr4ZGKJxEB4VXoQYkg5VonMulEwKD0vF4GNkTmK1IGqEonwAIR_2Q1d6iEM2lm_UUyUwI1HF8twq4fl4M6YxGE_yy8OeAvJs20x6a8wQBNOroI_8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KENKZHu9AaPIqFfo5KDJ_bUPJ_gjYkInx3Yx-9K4g8YdlyopuvMH9uNicy2nGKsAUSPBxuLqez1nXGbibTN8xRfp-eBbEIqvw728k7zJOreTkeZPuCiVa0wAIJMjDKxbwSbgM8V3o2R0f81SXgFNWdJo25zcK0_dQkmt5U6RJuaXyxc0HaW9TKAC2rwqbifJ2BUiSFoJR1Wb_StqWVAirfoj09uq0p6TcZWLkY2XjsH0KOGNYBSwy1wjb3IHrFbZbZpfIXtqPhf0Q2YBLptxDbE05C4npMTiJ4l5tZg1fqvjGmtFrgK31aJ664_Mje6LPnsUtS79-cLhFQ5zhXnQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcdUH7sM60IH8OQKBEquZx5ky7BEEg5N1et__Uqkz_OHjVPm8f86o-Vp1DXNtUy6FdFb2iTM2HvLLfXPqbcdhYgUspZ5zdnN4lXdwsu2mjCeBwbqWvN9nA0sz3rGgDzJAph0RMs0L37unliYADcdio-XpHp_HXO20F78ymh_Wd_OQnOi0O15GUcU9iPoBD1PpV0r6t9eNtBu3jpqnLhCCrpB5lTAH-M44SewLCBmQCo5pMOUxn2Q49vDaInRT4WtbZ604eSvzPJXJACH6KW-fyyXVAGU46vq_-r8ofp5gCyX1UCPHMF2hfbSujU9gDVjYle-FX8GQbmKjIoox2JiIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خروش میلیونی مردم یمن برای اعلام آمادگی برای جنگ با سعودی‌ها و حمایت از ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/450662" target="_blank">📅 19:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=nTdvvt5ggfsv5EYWIHIVvdDo9ky09sHd6HnP1kTHc7XYwNaTfZcAxJr2-3AdxYKpfquP61iMvYYj0Jf8noqMiu3GFsyr4MeemZgCq_WMbmHXjq-czGEEpRmBhOTqlpTs6g0luTXseRNxMWWpNuRd5pqphdxwX_WTCIwUCF5ATVKGwsrvVVbXbxvqXgsaqSgZgOw4zqYhc0uIr5-o19nexIaEiesmlKldBWmEFPwNANf-X97FClclYtKEipq8SB60YOPU3tnWPDK752fFdHmHHTcxYF9CEd_UkEMwaAj_nbxk9povMKYHIaQqEHE-_cHHt5bLkssBgEBvdSqU7ajVOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=nTdvvt5ggfsv5EYWIHIVvdDo9ky09sHd6HnP1kTHc7XYwNaTfZcAxJr2-3AdxYKpfquP61iMvYYj0Jf8noqMiu3GFsyr4MeemZgCq_WMbmHXjq-czGEEpRmBhOTqlpTs6g0luTXseRNxMWWpNuRd5pqphdxwX_WTCIwUCF5ATVKGwsrvVVbXbxvqXgsaqSgZgOw4zqYhc0uIr5-o19nexIaEiesmlKldBWmEFPwNANf-X97FClclYtKEipq8SB60YOPU3tnWPDK752fFdHmHHTcxYF9CEd_UkEMwaAj_nbxk9povMKYHIaQqEHE-_cHHt5bLkssBgEBvdSqU7ajVOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاهش تردد در تنگه هرمز به پایین‌ترین میزان در ۳ هفته گذشته
🔹
امروز تنها هشت عبور تاییدشده از آب‌‌راه استراژیک تنگه هرمز به ثبت رسیده است.
🔹
اکثر این شناورها از مسیر تعیین‌شده توسط ایران عبور کردند و هیچ شناوری از مسیر آب‌های عمان استفاده نکرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/450661" target="_blank">📅 19:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b870df4585.mp4?token=Pq8xO-wsQk-a4AyBjNmEXJRGWYnYNXM2T7oWQP_qzqW-v8cpxYhmEIcmbber3dr0Yoy_vX-XUjwCPdISwROjgJuZau9EmTaVl1vKBAleGH97AkF-RrwNjxwRrpYdz53QoCkXb1v2wfR-RessDfH99QXL4gdUULbxw5QUGzzddICjAKPbSp8Z6SI996Ksq8KgGetIapr4M7lMNmJeZWq787n9Z4bObY2nl4_GL9abrwtH0wVsmQHJXNRilp6B-dB6jXvNdv649H-Rz1cmkwbPbIKkpXiRKrCr30Zo25o9RysCbYxLmrMlp8QEW0sueu0Lz4Y_SBsd6Hv92JXYdogYM3z2CCD1zrS9JdBMOpkWJ48Extsjq7HDM9_b7gfSY0-ZSAEHeKzWQHVU9HMpf7cdi_lJGt9QzNXBIhBvNsTrrAnTdPb-qbXrC-c93YCvPSOENQhehrDiGJaEbJL-GyRRQFVnmm_NJIjpwvsqlUGN7kD7BqRMDoDNw5-8HC_vsa2YGx3MPVWAhQkkZ1yC5BLV4DEitBzDY9ta7VKlYNVKz3HzbCi-imkWOD9q35YQeilrJcnbGeBtOFaZdFANR42F1MH_A9UwAOJpuk2dhrKi7oS5CM6b9Odt2U8o98bYB4WhVNFvuHa4k3zdbQNhrWBGzwz4TX9TXLUyGJd7rTmuxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b870df4585.mp4?token=Pq8xO-wsQk-a4AyBjNmEXJRGWYnYNXM2T7oWQP_qzqW-v8cpxYhmEIcmbber3dr0Yoy_vX-XUjwCPdISwROjgJuZau9EmTaVl1vKBAleGH97AkF-RrwNjxwRrpYdz53QoCkXb1v2wfR-RessDfH99QXL4gdUULbxw5QUGzzddICjAKPbSp8Z6SI996Ksq8KgGetIapr4M7lMNmJeZWq787n9Z4bObY2nl4_GL9abrwtH0wVsmQHJXNRilp6B-dB6jXvNdv649H-Rz1cmkwbPbIKkpXiRKrCr30Zo25o9RysCbYxLmrMlp8QEW0sueu0Lz4Y_SBsd6Hv92JXYdogYM3z2CCD1zrS9JdBMOpkWJ48Extsjq7HDM9_b7gfSY0-ZSAEHeKzWQHVU9HMpf7cdi_lJGt9QzNXBIhBvNsTrrAnTdPb-qbXrC-c93YCvPSOENQhehrDiGJaEbJL-GyRRQFVnmm_NJIjpwvsqlUGN7kD7BqRMDoDNw5-8HC_vsa2YGx3MPVWAhQkkZ1yC5BLV4DEitBzDY9ta7VKlYNVKz3HzbCi-imkWOD9q35YQeilrJcnbGeBtOFaZdFANR42F1MH_A9UwAOJpuk2dhrKi7oS5CM6b9Odt2U8o98bYB4WhVNFvuHa4k3zdbQNhrWBGzwz4TX9TXLUyGJd7rTmuxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش میلیونی مردم یمن برای اعلام آمادگی برای جنگ با سعودی‌ها و حمایت از ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/450660" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مرشایمر: مقابله موفق ایران با آمریکا قابل پیش‌بینی نبود
نظریه‌پرداز و پرفسور آمریکایی:
🔹
به وضوح مشخص است که ایرانی‌ها پیروز این میدان خواهند بود. اما کاری که ترامپ انجام خواهد داد این است که اعلام پیروزی کند و تمام مریدان و پیروانش نیز خواهند گفت که این یک پیروزی بزرگ است.
🔹
مسئله این است: آیا او می‌تواند اکثریت مردم آمریکا را متقاعد کند؟ من فکر می‌کنم نخواهد توانست.
🔹
باید از خودتان بپرسید: آیا آنچه را که با چشمان خودمان می‌بینیم باور می‌کنید، یا حرف‌های رئیس‌جمهور ترامپ را؟
🔹
پیش از این جنگ، کمتر کسی فکر می‌کرد که ایرانی‌ها تا این حد عملکرد خوبی از خود نشان دهند.
فکر نمی‌کنم هیچ‌کس — از جمله خود ایرانی‌ها — به طور کامل درک کرده بود که ایران دقیقاً تا چه حد در برابر ایالات متحده عملکرد موفقی خواهد داشت.
@FarsNewsIny</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450659" target="_blank">📅 18:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbr2yIFlW0Yznuayczelx0DnNaNh6zbLhLKGzA9VMy3j5M_B3P-C6uMn2MsdJfm9v-q9ArRkGh8zjqwUKaprNkOoy-um6mzoITD2z7_2pRoH3LFJpz-1j_LBB55Cvw_VhRFtnhwW0tmXmddEMd7DIICnXVL_7v0HTu138_I3JhBusdh5oww64ki0fcXObUb9zexl_3ZTSkX2lESUIw1FlgBfqM9qaBAxlJmnKB8Orja7B8j7SUHyRTUh69-2fBtvHpg8cp0yR69AO-M3Zh3vMUih4kuTUHfXhhFJCLKsg-kTkBX92VZFm1WyxDS86X-dHbY-UU7YnF0qYgeSOZk8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: آمریکایی‌ها به لحظۀ عملیات علیه یگان‌های دریایی خود نزدیک می‌شوند
🔹
تحرکات و تجهیزات ارتش تروریستی آمریکایی، تحت اشراف یگان های دریایی جمهوری اسلامی است.
🔹
آمریکایی‌ها هر لحظه خود را به ساعت صفر عملیات علیه یگان‌های دریایی سنتکام در آب‌های منطقه، نزدیک‌تر می‌کنند؛ انتظار بکشید...
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450658" target="_blank">📅 18:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn_JPwJ_AhmEkPBP3CIFLQEU2J6GEoBeTSxfq6tFvIc-IIyQSIWN3QXBOUZZYdpzI-EnhfPnJ_LCk1jvvBcLMQlQXHE7j85dJXfTrvAUFpdeQS5YjAjPebU-7Is-_2ybw86vjuenxTGnEwpqSpn6RynPM2jqxEghwelduxjg65qgSOVBs_QRPkenIWgZ7akvrJgqX-nLJk04UkxabZzGCLq8v8tnuh5M7ZsewDJpj_1lGO7YeeCouRPXDBpqdOkHNPJeevnHoirVkiXEVwEFyt6ZgwlXbPA-0TdkGhkYr8Aow5aoNhUKR9hS2LUXRYPRFdKGZvihdMDLakxnNLmAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: دیدار نخست‌وزیر عراق با رئیس جمهور امریکا در کاخ سفید بی‌موقع و تخریب مجاهدت‌های ملت عراق بود
🔹
مشاور رهبر انقلاب در امور بین‌الملل: طی روزهای گذشته سفری توسط نخست‌وزیر عراق به آمریکا انجام شد که ضربۀ آن به مجاهدت‌ها و زحمات ملت عراق وصف‌ناپذیر است.
🔹
واقعاً نمی‌دانم آقای زیدی پیش‌بینی و هدفش از این سفر چه بود؛ یعنی اگر دراین‌باره با کسی مشورت نکرده باشد، وا اسفا!
🔹
نکته عجیب این است که در‌حالی که هنوز مراسمات سوگواری آن قائد شهید به اتمام نرسیده، اقای نخست وزیر به کاخ سفید سفر کرده و هیچ نشانه‌ای از اندوه و تأثر در آن دیدار ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/450657" target="_blank">📅 18:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrGJ9X17DDbtHfaGgFoMeaAvNEZsyqSDlvYiOgnR9vMkvKOTYWpBA5AsrgstPwTRjr1HR5YP0satG8rnPnB01BHxcOglHR5bYozl0GmXFh2gqhoyCAupUnnkshQbC_n9HvmjCZsgwV8mIRa39nYM-P19Hk68mRMeJgnFb6y_IVv_T6UakEb3B_xY2xzPOIxMPFPpt4JZzniRxkTolfnIa2dF8WB5w-CewUpjF33rfg2iFQhei9Lhqe0EZsGQC_YGJNnchCaod_zex5jNsIpdkVTdAQPg_z2ODdBN9cfWPCYHlcdLuEef5azi9l0N_B_ifh7yK15ki2e49y4_041KPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی تشییع رهبر شهید هر شب در یکی از میادین تهران
🔹
معاون سپاه تهران: خودرویی که برای حمل پیکر رهبر شهید در مراسم تشییع استفاده شد، تا پایان ماه صفر هر شب در یکی از تجمعات شبانه مردم در تهران حضور خواهد یافت تا یاد حماسه تشییع میلیونی رهبر شهید زنده بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/450655" target="_blank">📅 18:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6414d63b.mp4?token=jLGMkxOZQWVpuTazlyFIMnTc37uynXlmA00XNPCwBzpam1oRSVcQggi3MuDRBOxF_KBCuWv4LmZUypB4WXNZah_TUswR8Fl9MUgG315vyeVO4eAKC96lZDfvc10_LbZKZ7aWKtnjH8W5YVgu2Dw-K1qoWwwWQ8syVViM7is_CYokECzZNeV_DHPGA5nLB_WZtRYddpGELxTTwMvsoyQn_Vyy9wwoIb_wOfBojRFxB1yY8Fgt_6VxuJfVI7KnHDCuEZl7u_H2Jv_h21e9K93d_TX8NlQOvOmFTVp04I3Sbfq8jffmMFfPI7ZaM1bl9sBYhMt2ker9j5W7Rt0a0ysKuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6414d63b.mp4?token=jLGMkxOZQWVpuTazlyFIMnTc37uynXlmA00XNPCwBzpam1oRSVcQggi3MuDRBOxF_KBCuWv4LmZUypB4WXNZah_TUswR8Fl9MUgG315vyeVO4eAKC96lZDfvc10_LbZKZ7aWKtnjH8W5YVgu2Dw-K1qoWwwWQ8syVViM7is_CYokECzZNeV_DHPGA5nLB_WZtRYddpGELxTTwMvsoyQn_Vyy9wwoIb_wOfBojRFxB1yY8Fgt_6VxuJfVI7KnHDCuEZl7u_H2Jv_h21e9K93d_TX8NlQOvOmFTVp04I3Sbfq8jffmMFfPI7ZaM1bl9sBYhMt2ker9j5W7Rt0a0ysKuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450654" target="_blank">📅 17:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f8239385.mp4?token=EaYfr3UveMmBowK0Csqbr1KwAujwE_Y37VL-xQEBCb77eL9cvbCYFOrklrzK77e6wg9eSBoBpm6c94ndZCS90Uk5VG03-_RYEoZsQan_hGY75V3O-_wBO4hrJYmu6vXPncmx7vhkVNE5ppCSF0VI16HR_efER7h4QaufQCV46AbbYxz7stAMDFp1Yv3x-WYaC5u1Ph1_p_Ozu9maUxVKkZ2F0OLcUPaOIcBojtuP4GimhzF-Af6bra5iqu0vLeufmhsQKjz8HDtqQhJpwQiM8A1gIXm-Q0OcoJNfqzdfIhUkKeqGyfEaLIhr4k84qTf18kkS4wazqOHAj-WrwHV7CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f8239385.mp4?token=EaYfr3UveMmBowK0Csqbr1KwAujwE_Y37VL-xQEBCb77eL9cvbCYFOrklrzK77e6wg9eSBoBpm6c94ndZCS90Uk5VG03-_RYEoZsQan_hGY75V3O-_wBO4hrJYmu6vXPncmx7vhkVNE5ppCSF0VI16HR_efER7h4QaufQCV46AbbYxz7stAMDFp1Yv3x-WYaC5u1Ph1_p_Ozu9maUxVKkZ2F0OLcUPaOIcBojtuP4GimhzF-Af6bra5iqu0vLeufmhsQKjz8HDtqQhJpwQiM8A1gIXm-Q0OcoJNfqzdfIhUkKeqGyfEaLIhr4k84qTf18kkS4wazqOHAj-WrwHV7CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های جالب اردشیر زاهدی در‌ مورد شهید حاج‌قاسم سلیمانی و دفاع از ایران
🔹
وزیر خارجۀ پهلوی: ایرانیانی که خارج از کشور می‌گویند در ایران بمب بریزید ایرانی نیستند و شرافت خود را فروخته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450653" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffe488a34.mp4?token=e4hPVyZOQOpTmdExoIJw4VVxapRDz6yC7e6x8wEPNisu-tkZvRJzqX4NsB_qhQgqUyIzND0qZzNvHMV80ElUs21GXRB4LeempJWfk5lpBVUQIHboq_TlGsOKC2ZpKvS62b_rMEZlWcZPFY1kzY1jkDGEAvkqN47KkJqPVmHDWyg7ZGduur1XjbSbf7lvyFx813BWBdTVykavX2g00dp5kn_rYKwVfFKXV72wikbuCh9jLOm_n292TSvbTxN5I7C6dMZKNhvrDUY90a4ZCy9NCdvJyPYvuxcplndruOgcwxVsYkcbohZ4V7MwBXpKOgbPflDQQqt7TwoAKh6mT2jkDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffe488a34.mp4?token=e4hPVyZOQOpTmdExoIJw4VVxapRDz6yC7e6x8wEPNisu-tkZvRJzqX4NsB_qhQgqUyIzND0qZzNvHMV80ElUs21GXRB4LeempJWfk5lpBVUQIHboq_TlGsOKC2ZpKvS62b_rMEZlWcZPFY1kzY1jkDGEAvkqN47KkJqPVmHDWyg7ZGduur1XjbSbf7lvyFx813BWBdTVykavX2g00dp5kn_rYKwVfFKXV72wikbuCh9jLOm_n292TSvbTxN5I7C6dMZKNhvrDUY90a4ZCy9NCdvJyPYvuxcplndruOgcwxVsYkcbohZ4V7MwBXpKOgbPflDQQqt7TwoAKh6mT2jkDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد لوکاس آمریکایی شکار ماهیگیران ایرانی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450652" target="_blank">📅 16:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
رسانه‌های عربی از حملۀ ۸ پهپاد به پایگاه‌های تروریست‌های ضدایرانی در شمال غربی اربیل خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/450651" target="_blank">📅 16:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7ycgm7LZELY9PB6lo5pASCs5xXmB0zXRK1GP9pLbYh3e0Ifu9tWqpcwQc_HwnnE5atPlQ378HSkTjGsbwwtqw0MUi8gUjvBcVVnAfXD1IBLSJPqfmjJ4Yy4bShNYEX44rI8WgjQfo14dk3ePnRa8Zt1ExO6uYwoySHG9sP7dtP4kr5yGVcrFjS0y0v6S7Szg9cQePCknmq6idwmJP76jpzzC9CulRRNDxagMuszkT2CULhkKgW3a3_W6UETT87Qe8EG-J5eTBDJ1abVqLTdND6R_onvY4lxxhtYHExY_7EN21Ut0RIAXwUWJBty-iPYaxrAOyqvk6voN6Z4X5Zq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر جدیدی از مزار آقای شهید ایران در رواق دارالذکر حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450650" target="_blank">📅 16:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450648">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecXecL21ucXXvSO-uUJEeL0jZo9e53ZwED2Bady8Cv81P1Gc7Pc53w_XTVNXVfAHickg2WuJf7DfnsYDVRJ7Z1NtoE805atfqFencaeW56N14fbc9K4kP59AM5NlkLzV0w-C-joz72_3aSgaIh2w29qF_lS3yncNLib38PxwXtrRXWYNcW0I5KV0KBjfQcFSUhUoh1w-BkoxTnGbVSjArF-Dl34pqRmhNv9PKTjEgWzgfnf_XiV_0ZJJoTfCDCs19IwJQGkF7YTpNlZb7dqbqSCH0SYUKevl6vV2_2q-_VUy1opEVYzfSsy2VBRp7zD8XdNKXoF1V-xiEf7tHJDzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=k_P5MHkX1XXB0MGjxmZ6p39tXxk7_iK_OYb1fBxcKqivLbxQefbuc9BLu_VUI0lCsigL8HI1R9MR04ADxT0UGO8q5MKXtP4opJKiXd4T3N4cuifM7KeYg59kN0W0VfiWwCui4xLzh-HfMl8ev3SDV4ZZn0jhoMh0tnaI6KiZtAnftck-TL5tUtjc_CVV0X-_8avN0bFOe0vuXc-CV5_k2eON4Cwq3lSm80tZL64ezNLFoHZ6FVDHuKxqTnHxluPsu-i1MWo0WV1fhq5BO0gzz7rw52PytdK8W0OIBdSNqjQaH8KZRVC4riYBLsqAU6-6nLThJGVqaWNoxwZRswuq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=k_P5MHkX1XXB0MGjxmZ6p39tXxk7_iK_OYb1fBxcKqivLbxQefbuc9BLu_VUI0lCsigL8HI1R9MR04ADxT0UGO8q5MKXtP4opJKiXd4T3N4cuifM7KeYg59kN0W0VfiWwCui4xLzh-HfMl8ev3SDV4ZZn0jhoMh0tnaI6KiZtAnftck-TL5tUtjc_CVV0X-_8avN0bFOe0vuXc-CV5_k2eON4Cwq3lSm80tZL64ezNLFoHZ6FVDHuKxqTnHxluPsu-i1MWo0WV1fhq5BO0gzz7rw52PytdK8W0OIBdSNqjQaH8KZRVC4riYBLsqAU6-6nLThJGVqaWNoxwZRswuq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام یک انبار لجستیکی آمریکا در کویت پس از اصابت پهپادهای ایران
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450648" target="_blank">📅 16:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450647">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیام تبریک رئیس‌جمهور درپی کسب عنوان قهرمانی جهان توسط تیم‌ملی والیبال نشسته
🔹
کسب عنوان قهرمانی جهان توسط تیم ملی والیبال نشسته مردان کشورمان برای نهمین بار، افتخاری بزرگ برای ملت ایران و نشانه‌ای روشن از اراده، پشتکار، خودباوری و توانمندی فرزندان این سرزمین است.
🔹
برای این عزیزان که با اتکا به اراده و تلاش، محدودیت‌ها را به فرصت و دشواری‌ها را به موفقیت تبدیل می‌کنند، آرزوی سلامت، سربلندی و موفقیت دارم و امیدوارم با حفظ همین روحیه و انسجام، در بازی‌های پارالمپیک ۲۰۲۸ نیز پرچم پرافتخار ایران را بر فراز جهان به اهتزاز درآورند و یک بار دیگر موجبات غرور و شادی ملت بزرگ ایران را فراهم سازند.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450647" target="_blank">📅 15:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJF9tfJpWyaaBwzFF-EX1VkLn6-GV5etFHMTXi7zj8AfH4pR_SJFAYy_77GXpF_9_tjVbDMmlILnOI193GDcu0paY2ER8jh2XF2979Or6Yv37S3RllyVO_9Ozfh6zcKwtZxJnfIC-r1s-MqtfyfDWwHeFcuM8gB8hnocd_wrol65IaqxhsxZ1kcKkZjHjKJsElKqdr6ABDof5EPrRunziOu2rEe7IKy2UbZBTL_Dr4Yloh4hB_HoxSxFjtOm8xS0Cil2Vo49atfeR4hoMRISUKG6PZ9y3qFfw0ON44m7WMJojsZCvjfUnOckBk1VCNI2vrcZJPjtFKuetjGlAGg34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHKwCvi-x-RUJeGQOnmcT_7F2OQ7EYHvokUd7puW5HsQODsdvQV6_EPu3HCDh17FcYe6qHvpB63YuSdbSq9u5mLjg8fxwKGzIBN7bjxMLZHx2ztR7r_apK96OGI7vI35pgXYsmtCTxMCkr0rYtza7ldRneUrJYVYDlpEFtYEoPYO66B0G1va5wwp51MBnPH3bigkmQHHXT1mF4QcU-6HdNuV5ylU-yn2sg6ZE6o4Rp19uyaYTrL5tPi0p8vHwcXb8uIpMX8do2o3wkkQxnfLTsghL2mftgQnH0U31WQ8xIlr7-ggNBkv_Xo-Ci7uW-N_R9ynp6zTFD-kW1QUGEK5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWEv9pJvDd0uaM9xZKz5bhFASvHKlKO5mRK6rU1wAMZ66e_pZoNl5eElFnG9Zq2bqE1fKr44pNS0IHCL6xTq-R5R_bNWYwW11ODrZLmBiZG4GIWqZxILwzveqtKMpVuJ6MUqfDHfevok6xdg7agY9_zpHZji3lVJiBbLcPWZ2Oym2s6naI9F0ZrcdCj2SnLt1V2REP0qTRElynk_MI8kIQp6sS_u5pW9q6xPR1E9XWtrKow16ISqXF1tXmJWd0WdLdqfHgwIJHHoJxDBIc55c02Qike5Ikabw9YhVp90gaayNG8IBg0ljfez5R5M9YhZiUWPerDGw-nYggYT7dGRHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  @Farsna - Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450644" target="_blank">📅 15:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در سلیمانیه و اربیل در منطقۀ کردستان عراق خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450643" target="_blank">📅 15:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5gNabQA6TNGIk_X8SqeCeAmORk-wVPVfhYrO2k8p1nVmT1bfdLhU90QFLn5z4lWDQKD_zUSY2osphRo2BkGTJx8_qxUrKrQdtexA1a4uU59Me4pOFD2g-en5V1tmurmnhhWEOhpgCkSB-HoGnLG51otLI275GNAzCCRgS3Rgw7ZUFjBRLgH8heWGU0sP7R0o9x0qnk1gmGAFrlQ6Gx4P6WAcoGOIgZkWZj-S1ZESh0cjIazthEjb4XfcRxxl2kCAfU_9PIHjTLTqj8jLC9sJxGUIqQ0cPWDtwp6pzThittHH6HTPoxxswyM0w57XruwYPdi4RGwrotZIqh4Y-Bouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضای سپاه: شلیک‌های موثر و هدفمند ما تا برگشتن آرامش ادامه خواهد داشت
🔹
سردار سید مجید موسوی: در نظام محاسباتی ما خاک، خاک است؛ تهران تا جنوب یکپارچه برای ایران هستند.
🔹
شلیک‌های موثر و هدفمند ما از سراسر ایران بر سر دشمن تا برگشتن آرامش به خط ساحلی جنوب و تنگۀ هرمز ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450642" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFmM6eaSrYvsmgEG7P7pXuV1iS5Xt9bwiXyXloI9HppT4uI_VAbYD_LWGNt13dGShNyo3hOxc-X3xgZjBY2CTxZCNqgfbsRIExNQNdj_uQoLPDy6ydlFJSqUTX8ASE8S42wIZg7jDpgyFSnvzJEqHQXPkHhMVCAUgGukRcu9vDn97f8Gy5YDlbKIc-IumuXzJBEyjU7LEZEft6F1uSxUl0O_OYJmOrsI7NYQv6Qruc8fpGOLH8ommlymmd_AS6LMNh8Baf55Jqk1DxFoGfK8NemEpuOqPpnj0I9xOjOcn0woShCLB4LTYCith2VJYWcapZZ6i03FURKRvoYcCSsFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMzXBrhNKQGAE3ghAxxIXY1zQcKMF0KXTbDMUJQg5pKpE_gW_C1ieVKjsSmRKjtX3oMnSk5iPJUyUrQZb3POwzuM1_TVRDNDJOMG3OuRdGubXQOppws4AOYPWetxSgz2NUW07_cLJZsPteS1Y9xvfwY3E5xgYlsYVR-9PlX-GM41nxVOpyl1-fstPdFF9BlFtr1JZP9p5gJlKqmb4J3MXZzVYf4gpLC2KA8quVLEVqD1GjbYqvThl-OKIi6CXbEHj2umj5esGVvFCgnbuh1JgrIcX61pzh3QMpxh_s4Qgmgy6qx_XENK5Nf5X2nAthwh1ncNDV8ANKKWvoB2LMQRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmyPrdFAcsSHQQUUB8_y6iu0XbLhyh-_jgBcu5yBGMRkB5iC7J6KMhoRO_h6HUeiMaYO7KHesx2hFjfNtAOiD8coufBv4_dyQYStjoCHfRIqZjQDShdDWTyQzOVzJbTdvmqbxULPtghgjH2lF0x9AN41kdJaUNT9XfgL58vMJ2fpvUcotlaGaerQhgf-naEJ_Nq3GeYqJPCBVpECByur0rqKXvg_RMNvtQ5-9WtMtLR3mnYqGkEe1mNeHz4wgobAjq_Eo3gyhUY0R-Gy3-46i9O-GrEE_DvCXS_0Gq7o2QxQor_WcsY4TjiuoA8ZrklM0wDEJLIVh6gTfVvaE5qgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlycUacx1d0wgQiAzXOGgcWkEC0oGsLrz8YIaBS8KS7gLAO83GCdX8EcbSrzkPrbBr9reQlyVezd1Vg6-2JY8ZOcUMsHCI5nulSLUALQFlYxgNJuN-IHgY97cTP3bUYmup7ijqNARHizd7lGTL7wAF-CT0QVvFMaZbzJJTgwIX2dUNGjAmJ7ndaXvpZ1P8ZB56kupkeBUAVuGfS7zvEXQwVFu3SfaxQJtdN0Jjmg6CtfXOmKNQxmiPihBmMvkh8ZVoLF9RItQ9VSsLWS1YYpQIpIITv6mdYIYFtAzF5h8vVSnyPgU6YzHyyJq83cj-6UrqGgOFaqbBftIQsHdmBqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJBOPxusm0LWLLbOUo0FsxUVLC7jmZgnw_kLNr5YhEEhY_jXktHob5cvbwtDKz-Kd5Y1yEl4N5CGTDAqHOntEjVmXEaQ81dJXqjSRabH1NEVDeDcW0Y0Gi6S0ZQPcS_Lhj2qNM5kTLdu_7cVKj-XoOS54oEX3yMNkkVr_Z5RihD-8loPs5aqlBmKyUTH0fzSx4nXPCfcMbE4bVEkV48v7i8Iw9mbDLe3vr0KOumUGFAE7DDRH3BLYtW40HbAdZn2snlHAGsyXxY-4-U_1LjTM9-fRA7dckCOinYaOnhYC8h2BafFvWgcrSlVPNT2rjFUnsh1PT5r7FI2YwCnqWcK7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب در دفتر آیت‌الله نوری همدانی
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450637" target="_blank">📅 15:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در سلیمانیه و اربیل در منطقۀ کردستان عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450636" target="_blank">📅 15:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۳ شهید و ۱۷ زخمی در حملات هوایی امروز اسرائیل به غزه
🔹
منابع پزشکی در غزه از شهادت ۳ فلسطینی و زخمی شدن ۱۷ نفر در حملات هوایی دشمن اسرائیلی به مناطق مختلف این منطقه از بامداد امروز خبر می‌دهند.
@farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450635" target="_blank">📅 15:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7EXxHV29Gg7078ADbAITKGh1Y5JDLmv8_fOdq6V0KgSDduD27GZ7OsU5yzW5hK_UCxTR2bweG1aU0zV4Ar949u7LrQ-rbBjF-oETNJXYedDFz8Lc9D0r6WukMwsgmH3HdcsUMFryEqtt1wtZ1zfebRPU1842Kg8gci0z1Oe5tLT0etVZ86V2hPEaukVM2TQSHCCliBtz9N3hYMNsqBIt3whEjD6M4hEtDHH0eIjhu_FhtAfMxcK6GLnOnBl2ftFfwbz98Hg3XRE3VDJvCICeYEBWN2NczdSd-tgQKJDtGRQ2yw8gvFQI2zfDKQBgPZhVn6zXANvtCulY97uzDUQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnT0iIIpyqcCrhFW52D3FTiIj7NPgNVCiXdYhbp9jdD8zCF9yh1lBHh3BHwsxOOY1CV8EEUu9JVcPlKoGeucdIW-Tjj79iqE03sm-372Z2xwriMVlDvVRhiNshguq8n52pNXa6L5DuXQXasaDqV927whMKsj5t8xa9bnRsWoVzMNVOVryQ2D0SUlgN8RE4rhV4FPCw6kIN7Sjc_Lwx21s9fGDno1JmbGCh2GfNB6FxvlL90-wI-aatsqbbdjMhezVeUc2JGi1zqOExCSUrsTQ7TzWkg6_eK5BfpupSwcCt0Ndeqi2Bkb0K7Oz13vQ1ERMleg38glXoV_J8z04I5nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JP7jeH6yQ0HzxVkNQWrRaxR0qn6qNdbUbeVAI-txJH3qN2YSth-oCp7iMGMGlSUhKGM8ut8IF50Ma2fEL2rOiZaq6Tg-EOy7tuKPBUXuX2TSaLw7fSG7GYyIMAiOxQzAQlXlE5vU3gacQtFl_Adu8lPkUkwqIM1LMRulsq7QFCrIF4uhrTfWZqf6a5J7eCvcR0uCQ1ta1qHwXrgyW-rnrILOgPFf1j-V9dEvefCAWL5N0UhQn8AsDTiO9WoVFPvCDJV9-AjvQHlEX4eMcJJ3MNQZ-qYPcoDUBFKh4soIlQ4liH63sZgUEYXo_tszd4KNRNjJhAcwmpcU8POL2g9Cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EufknEB90JZFwd7JeqOmnLCmJ0DS4WP4mpsVUgXpFAe5iQUA2Yl4appxsBGq0jcfD1wx3GenRA8HRDWdw2QSk2bg0eUKrVZEcfWA-fYkslyA__TQ7Ny4JHXwmbnWHeY8MpsFbCdzM0V90XTtB-reYnzUZpFFuxGnxE34OfwxvXkXaUCLZAR7qydiSA-bvYBhFOkfKQy975Iq-rHv08aRdbH-3UsD9FXbvBRMyfu1CsTj0sxDU1fvq2IBtqbI2_YxWhEC7gG8HCWYcSq2chbCAxe-cgPPfyu7Ng9vik43vzSpJi6Pbhx8oSekzgdK21vzKsrs6y8pmQlz92WiQkX-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FeBCEUF7LalN5VXo3HzBI60GDDAbCjV9XXeUlPg9o2xpDmJ-6IqbC62w0j80_IRweUULsCM7kcg8xc-Tje7_VnVtHHY6XJSie855yNgfpCE6fH7BOtg3kKuWLoo39U2qv26ETC2rPRyNWU-xIbIa-0AWWjYEbkPm4zDxKQXzW4oYSJbdkyFRnSyw0QuGC17PrIefyqu6hERMmB1-0irdq0hckVm-1XngNd6mPBH2XUcHZMDNoyJuzIQWVSzX8PeLFMZTiBcx7ijPY6g6EvWVDSjytGhohC_bmpx_EjBCuvOAS4qxg1SLfMDPQsg182LoSdaZcYmfhkjcuPQhjiX2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrBY2iyQIFpuM4l6jO42flfKFcShydCu81qT-VgvkJF-yxIa1pus_nAgF88NDtOuyzm0bgbGNd3uatX_ZHZRdBxxMJUSvAns62sFLJIiHBtImu1kS3u0XaAmwEfII9cYceiy7MI5p9FwdosviH81h83j2zXI3LQvYh19dGR1j8NFaBSJiQrhbyS0dJaoQnfN4lfEx6q4bMHBXZORO5dReHflFhpb3KYyr98La4k6hyvZJwRrUR3krKb-JQs2T4D5d0sslLX7OYgJipQMirXfHR8_vOl5bzg__HwgI01n2lMMy8jKNf_9lD1qpXwbP8fmPYgDzAoJTz3BYa8wXq7LTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p66PDyxFrB9JIT8tjG2tAZ1omKqREKjbTOJgoc2Ezmv34E04QC9wjc0VMXD1fN8WE_gwBDSf2SML5nxkBGi9QBl00Njz0fgZGB_9HlNjW3xArHmjGL7Wm2UXh4VX3CmMpMj9YMC21IAM9Ni2bgiurrzwLeqKD06XZ27n9IUI5Qde8e9ck2-5ITPoc6vInIFxoUBjf77ICzQ00zZPRypbRxmaYtwzMXY6SRG2aL7SmU0P3fgIgzwVYLw3mEEbg9xppHQNT_hA1YevSBK0XCCHPEx84AuFk6kTnnqz6-tgPvQTKhRcx8pCod6tyjasWW6Jt1IlA71aeC5vSMNsq1pRug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450628" target="_blank">📅 15:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYcHR6Agcqn_2XHLd8JjLQ3pc1CcStZlmQANBQV7vjb9lHlwxYQhjtP4zJkCMppzCZAKhRvFIU18cNsHQcIs1vO8OIVVyacssOOuYwdh9I6bc5-lcDw4mKmnc-WznysEJhYUjgkpa9xA9sNROczw--ra26r9fj4ioM9bQrz_LMBXRJ5z1nb43fyvjdxOssk5wK7_W3nS2dO342hJKY7poUHqMFOn10RJEnkAslUwnDsrxdsRoBuutNS50UyCvNm1gNMMsSYA66wI41RByCCPGrML4Lkl7svb1JWAsLXUsJWkAHAALXvxeDU1fy13TSZkMNSJkN6k29PBQhIB5cBUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر انگلیس استعفا کرد
🔹
پس‌از ماه‌ها فشار برای کناره‌گیری، استارمر بالاخره با سخنرانی مقابل دفتر نخست‌وزیری انگلیس اعلام استعفا کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450627" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌ شمار شهدای حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔹
دانشگاه علوم پزشکی هرمزگان: براساس آخرین اطلاعات دریافتی، شمار شهدای حمله به پل‌های بندر خمیر به هفت نفر افزایش یافته است.
🔹
همچنین در این حمله ۹ نفر مجروح شدند که روند رسیدگی درمانی به مصدومان…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450626" target="_blank">📅 15:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXxsRgLPivCqKL4InKPBhb87DHQHHppddpg1XgLHExlmfqNxN6LH4YDEtXkU0qRi1YGb-FFqDvUFI3PyzHvyyWFISbnSQD0qP2_zgd30laaCt1ale5ih_GSyHwe9NZDZslNoPUnvsR_Dh8QWQXKXJJGhBmio204_poaC1PcE7KDChyHkPPIrQIVdqAcOpCP5TW-PeTrc6rCv7Rc8fk6GQDg79BTJLZaltb3VFnNcn8Q72kWoU-6wBC-pT0TC01HLGxL3nOUX3ovkXMIbLXVEo1Sp40l7F_QvGARuyaNazyEX82D67-8VBcKXXYzrN8in6wILnACBkuWEDAl40tkBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه امنیتی جدید برای نفت‌کش‌ها این‌بار در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا از وقوع حادثه‌ای دیگر برای یک کشتی تجاری در نزدیکی بندر دقم عمان خبر داد و اعلام کرد این نفتکش در جریان فعالیت‌های نظامی جاری در منطقه با نیروهای نظامی مواجه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450625" target="_blank">📅 14:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4e23VLOwNsxCTyrFikHnHaisqu7JwmmZSbsFBMmDEXNxtTtpSJBV9QjWZCSNOxx2S_cgL-zIublJNnzZXFCoos6WU4mXfQ6v79EiWb4WxV01PIxkBKWENnE1jXcdtVtuHYzebhKfpaigN3sROcOiTr110A3kELke-elRAY0un8XwGB7D9iRlk196NNkSqaU4OT00eD9FfHLEusgACN6DVLL3ICFVy1v-MIMtYeCAEn41OS9H_BOrVaXuHf5ZNP0R3XJL3fJUUMrTnYjJvhdAST_79p_e0lKsy6fPnmRHDzN5YBZfXUl1zDQUaft6DH-ZcLRt6w8GTdWBEogLfo0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام پایگاه‌های آمریکا در منطقه طی شبانه‌روز گذشته مورد اصابت موشک‌های ایران قرار گرفته‌اند؟
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450624" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450623">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161ea20539.mp4?token=v9GtoGK6qFLcmduL9qSm6wNy4N243eYe5kmyLxUw40JLis5JMnTqnSsQB1aSw26WNxlskQiZDOaVgE0LglPm5IqF4M6n-4u_wHtdz9v4W0k6bfUnM9_b_iFhmzIzcpp5E9IP6vFGEle_JQvloS_JD7eaTbmk7KdnFpWWZfOtO_M1t25hxCeOtwnNyOjxg-nmoPxFzQk2WbKQLJsa6Upr-3WWKyLmnviaOt3tCIcobY0LUbr1SF3zk_va6_RVK9MB1oHdbWbIChY7Bd_4S6xaCnYavGgcgjcSZ48f1BY8EwXfkUUm_Zg7nlekKtcCJfgbAQwnVroeQp4sl8ZvRmdnlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161ea20539.mp4?token=v9GtoGK6qFLcmduL9qSm6wNy4N243eYe5kmyLxUw40JLis5JMnTqnSsQB1aSw26WNxlskQiZDOaVgE0LglPm5IqF4M6n-4u_wHtdz9v4W0k6bfUnM9_b_iFhmzIzcpp5E9IP6vFGEle_JQvloS_JD7eaTbmk7KdnFpWWZfOtO_M1t25hxCeOtwnNyOjxg-nmoPxFzQk2WbKQLJsa6Upr-3WWKyLmnviaOt3tCIcobY0LUbr1SF3zk_va6_RVK9MB1oHdbWbIChY7Bd_4S6xaCnYavGgcgjcSZ48f1BY8EwXfkUUm_Zg7nlekKtcCJfgbAQwnVroeQp4sl8ZvRmdnlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سومین حملۀ موشکی آمریکا به برج مراقبت دریایی چابهار
🔹
دقایقی پیش مردم چابهار صدای چند انفجار از این شهر شنیدند.
🔹
بر اساس اخبار اولیه این‌بار نیز دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفتۀ گذشته مورد حملۀ موشکی خود قرار داده است.…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450623" target="_blank">📅 14:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=Qv8Q-cNK5c0-5ft4bMbEWk_GMOcGA6L23l_9IwDlE7JQjMnEKdo7a7zCAfKgGa1mhOxxjarWo_S0nnHvXYlhDUIcHdb4mvUz-gyZeKWg4UnAHp_9FFD4bcu_iM0JZw-QHnJ0IhDIPlXmHRvmoV_67TicbfNXDaeDaeV2daouqU3rq2M8dUWtVMpO4YtUYGBYJouIDOMPpG9VpMOjP3CWluUdHolU4ONqE67bEcr1m2U1mBogecgxtIFYAvEDteGY1yJ0vVQ0aZJ4qCnDxsLESbWVfoawl4JSX8Oeb09R9eeDkYui8DwYXqvAx5tFveWAFt9bo9vPgCWK_pSjAdgr8pX0_ntJ8ObndWuPRd6J20I3XD1PYqEl2aKELOWGbIPuGOq0r5bk7g9W1Jq_gWTK3kyN3daoztlzM2cU07jF79yYWUmB1wXjmv4NluPF_FLOZHgPjtOH6rR_Uf3IJQZu6fcg3c7zzR4YLaV0G-Z0GBKPrKfzqFirpy40ClF7KiLBqshG5v6Mu7SXLij4cIw8zEajhCVtmWXJyMWCFoygz06vSVPVqinKd9hZo4JaSHwhBH9_RSVbOE9sjco9ED9Qd7wwOPhDvof04qtGBt81BxPpnR4w9cIhNsc1Cd0L3WFGhCz5xeTKyU83mX4j9LIoqgtowFDsNR-yl6LhJb4odIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=Qv8Q-cNK5c0-5ft4bMbEWk_GMOcGA6L23l_9IwDlE7JQjMnEKdo7a7zCAfKgGa1mhOxxjarWo_S0nnHvXYlhDUIcHdb4mvUz-gyZeKWg4UnAHp_9FFD4bcu_iM0JZw-QHnJ0IhDIPlXmHRvmoV_67TicbfNXDaeDaeV2daouqU3rq2M8dUWtVMpO4YtUYGBYJouIDOMPpG9VpMOjP3CWluUdHolU4ONqE67bEcr1m2U1mBogecgxtIFYAvEDteGY1yJ0vVQ0aZJ4qCnDxsLESbWVfoawl4JSX8Oeb09R9eeDkYui8DwYXqvAx5tFveWAFt9bo9vPgCWK_pSjAdgr8pX0_ntJ8ObndWuPRd6J20I3XD1PYqEl2aKELOWGbIPuGOq0r5bk7g9W1Jq_gWTK3kyN3daoztlzM2cU07jF79yYWUmB1wXjmv4NluPF_FLOZHgPjtOH6rR_Uf3IJQZu6fcg3c7zzR4YLaV0G-Z0GBKPrKfzqFirpy40ClF7KiLBqshG5v6Mu7SXLij4cIw8zEajhCVtmWXJyMWCFoygz06vSVPVqinKd9hZo4JaSHwhBH9_RSVbOE9sjco9ED9Qd7wwOPhDvof04qtGBt81BxPpnR4w9cIhNsc1Cd0L3WFGhCz5xeTKyU83mX4j9LIoqgtowFDsNR-yl6LhJb4odIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450622" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brt340jGShGq26tFEVhEyO8Ig7PJg7vYasSLPXdJI1FX4gSzGsb9Fi2EBhf1SS449VI5js2P3ApZPSLX7gU9DGLknIrYN9OfCXxWRjUxIA8f8neQ328KOcIsqhBJentPBDAJVNdklaLm9NMovu3xlGVSR8I3rorAEE3_SPQWsmi_18Kk9pnEp7OC15fAJaUrvN80viMR5r2_b-xk7TsIiSW_cCtMiMS4YuOhjDWvXYPSWZ4BOvKZ6h7r_Zzv-GoL3TRgolBP-NVGLWuNzt_Hcb8j-gFKFz_cZrN2a6QTtHKkZzvJJp2AIWZFcHAzYYA5G_4TzkzHalXHUAwtxH_Ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پایگاه‌های آمریکایی‌ها در منطقه باید تعطیل شوند
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450621" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450620">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیام تبریک قالیباف درپی قهرمانی تیم ملی والیبال نشسته
در مسابقات جهانی
🔹
رئیس مجلس: این قهرمانی، تنها فتح یک میدان ورزشی نیست؛ تجلی روحیه‌ای است که در سخت‌ترین شرایط نیز از پای نمی‌نشیند، فرصت می‌آفریند و با توکل، همدلی و استقامت، پرچم مقدس جمهوری اسلامی ایران را بر بلندای جهان به اهتزاز درمی‌آورد.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450620" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHqNZfKLufqiNluTITcSqgTaPpqw8f88AohmSzj1HlVMfg1l6Z3SUIuSw5hztgkYUMzhIXFwvRj6Ku2RcHqcJpxmPI6_P-v0Hq1r-5w_6VTup5LyHp9JQSe-t0m1FuofyxoKdjii-FTkSBCJo6G665u9uA3MKng-7WlB3FWoGbq-Eo1Xi1k_bibEsnNXOygY92NbUvKgGHK_IVbpYo7SqLPvdyHR39Qb_naiZxRhvuX6x7f0Lev7d9_Zt8b76Z2ZbrNo5Olsp8t9cahnkSBj--qJ9a-ndWQ4S7_1_Ry7ujCosABTkgsOQmK-e9y_gaV1TRw8foi6die8Vip3wmrOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضه ورق گرم فولادمبارکه در بورس کالا
در روز شنبه ۲۷ تیرماه صورت میگیرد؛
▫️
شرکت فولادمبارکه در روز شنبه مورخ ۱۴۰۵/۴/۲۷ عرضه ورق گرم تیرماه خود را در بورس کالا انجام خواهد داد، این عرضه همانند ماه‌های پیشین با استفاده از ظرفیت های موجود و فعال سازی ظرفیت های بازرگانی گروه صورت می‌گیرد.
▫️
لازم است به اطلاع همه مشتریان عزیز برساند در این ماه نیز شرکت فولادمبارکه در جهت جلوگیری از التهاب در بازار و همچنین حمایت از مصرف کنندگان نهایی با کاهش قیمت پایه، ورق گرم را با قیمت پایه ۸۵۰/۰۰۰ ریال عرضه خواهد نمود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450619" target="_blank">📅 14:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450618">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ0RKCj2-WT-SBUWl2GZiRthHag_LZQhPXuLIBFbasPWfOklHHNJDVplaAPRjD3gNJVvACEUoolCaFM5PPgFtjxdSaIqkQlH0HKUouy4Ts69uQdhNk_IaoDKdAzi-yHfms3C1PhOaLhMg3rwIME_R3nu07RgnwlMlgUpNlBh2SFdOIkia7KlUExe6576rJJ8NRg4LwV2lT4jMHeXwlsx8Ni16zP8ioh3BORQfxAAK1B7rfQGWP8SQrqcCZVRRmeQbFYI9eDL0fQPbTaTJCXtuoWLcuRoMwDLKAnG2hIL-xf7165kxG7gQvxuCCXtygeJX30ty9OPxV2Zv4AE1TT-gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450618" target="_blank">📅 14:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450617" target="_blank">📅 14:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18e745a1d.mp4?token=kYuei2_QEjT38pAj-hzJRsVUiZI3yHvFc4Pg7qhTTaK-JvBWkuTZQXqwbDOXrqRnO2SPpLwdoHdr6NDYuHyyAgHsCxCYwHMdXHXro6tS69a39FD3cxI9K25rH6CzKWQTtHaJ0kvFiVodYqmq_IH7PdinPhjSgvwqgYsLXAaUwSy1Bge8b6i7uWk2drsZy1yk42Kb-zTlP3qQ8SxASOSndhxL2Tjrm94Oh9ZN48WwggxCfwny-3q0Wueke9sIn8tfMIbMyh9V2yV4GBtVzYepC3j9Hea7NTLmK446duWbo12Rr8zLyl_EqvE2HoLwCt1dUvCPCS3qaH-LtbtXkxRO_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18e745a1d.mp4?token=kYuei2_QEjT38pAj-hzJRsVUiZI3yHvFc4Pg7qhTTaK-JvBWkuTZQXqwbDOXrqRnO2SPpLwdoHdr6NDYuHyyAgHsCxCYwHMdXHXro6tS69a39FD3cxI9K25rH6CzKWQTtHaJ0kvFiVodYqmq_IH7PdinPhjSgvwqgYsLXAaUwSy1Bge8b6i7uWk2drsZy1yk42Kb-zTlP3qQ8SxASOSndhxL2Tjrm94Oh9ZN48WwggxCfwny-3q0Wueke9sIn8tfMIbMyh9V2yV4GBtVzYepC3j9Hea7NTLmK446duWbo12Rr8zLyl_EqvE2HoLwCt1dUvCPCS3qaH-LtbtXkxRO_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت بیمارستان بقایی ۲ اهواز به مدار خدمت
🔹
رئیس دانشگاه علوم پزشکی جندی‌شاپور اهواز: پس‌از وقفه‌ای کمتر از ۶ ساعت، بیمارستان بقایی ۲ اهواز از صبح امروز با بازگشت تعدادی از بیماران، فعالیت خود را از سر گرفت و روند پذیرش و ارائهٔ خدمات درمانی در آن هم‌اکنون…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450616" target="_blank">📅 14:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1c5e5344.mp4?token=SNY8PKOTg1RnoTmKOF1I0loOo_PqvT8H9d2sOtBCKmPdjJIKLJFLaZNmYQQpM7q2bRsANyzZ0oVG-B72pg2zyboQ5W4HLx_aNn1LFCzzwC1iTcTsZp8Xx8b9_QKArICFnk99B9WWm5bqukk-_7GnW4xWTyl3Z2F5V-_wSgExHTWKsv1pbHtVsgqEgkjtv8dJ3aPK8PP7WN8hhUXGyzp8A-eF6aCBzsOiQtWBOCbJ_syZXi27qzntYGQq0U4oUBFvpp4m5q6goIbEdCX5rTT9LsMHTMt4rWGgyakRSiGctbPcQ1TLWFYLPx8U99M5P3xDw2Q2_OlNCAmSin_aTpdz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1c5e5344.mp4?token=SNY8PKOTg1RnoTmKOF1I0loOo_PqvT8H9d2sOtBCKmPdjJIKLJFLaZNmYQQpM7q2bRsANyzZ0oVG-B72pg2zyboQ5W4HLx_aNn1LFCzzwC1iTcTsZp8Xx8b9_QKArICFnk99B9WWm5bqukk-_7GnW4xWTyl3Z2F5V-_wSgExHTWKsv1pbHtVsgqEgkjtv8dJ3aPK8PP7WN8hhUXGyzp8A-eF6aCBzsOiQtWBOCbJ_syZXi27qzntYGQq0U4oUBFvpp4m5q6goIbEdCX5rTT9LsMHTMt4rWGgyakRSiGctbPcQ1TLWFYLPx8U99M5P3xDw2Q2_OlNCAmSin_aTpdz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض گل‌های مزار رهبر‌ شهید در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450615" target="_blank">📅 14:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d37350701.mp4?token=V2Z28PjgRUini68YQK7mUIWq-yfqijWFHGQ18GLEs9ODEKsnUKUXH7UIcjUtN7xzmZ2LRR5VUV-RPkPFF_IAyqr6Yv3uYT6dRapbUxvbo7dWYmNbTbxOwMLJgcrdvHXthAAMuyM6lsjcsRM8rR0ZBZcarwmM3Bu3DDDpCIZnrEIq-Ebwp-Z7ae3a_I5zFW0ziv5fn0_fToC9nOsyQco72ojaJiuDRPnI6nUnBzlDamXPZ9SepC0jrwv5Omg0o0uQNPQEfT2-IZM1xUwL790oPcngLe5BVIQzVXdxkGK6pY6fjowL_f7AWLWBugeGZpeItyeySI8BIcRj2l1z7UD5VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d37350701.mp4?token=V2Z28PjgRUini68YQK7mUIWq-yfqijWFHGQ18GLEs9ODEKsnUKUXH7UIcjUtN7xzmZ2LRR5VUV-RPkPFF_IAyqr6Yv3uYT6dRapbUxvbo7dWYmNbTbxOwMLJgcrdvHXthAAMuyM6lsjcsRM8rR0ZBZcarwmM3Bu3DDDpCIZnrEIq-Ebwp-Z7ae3a_I5zFW0ziv5fn0_fToC9nOsyQco72ojaJiuDRPnI6nUnBzlDamXPZ9SepC0jrwv5Omg0o0uQNPQEfT2-IZM1xUwL790oPcngLe5BVIQzVXdxkGK6pY6fjowL_f7AWLWBugeGZpeItyeySI8BIcRj2l1z7UD5VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌   سپاه: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
🔹
سپاه پاسداران: در تکمیل عملیات مقابله به مثل شب گذشته رزمندگان غیور نیروی پرافتخار هوافضای سپاه، در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" و…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450614" target="_blank">📅 14:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leBYjDpaayvhzDSXFVyWU5mgbTgHhMYDwLrmE3AX42UtuZP9E7JS4kbi51b_YWaqQpA0F71Bi51diHDxfjTxrOhvYXCqqJ7BhUN2W3xMBXV-Ha64pjbZ3TyOd25JSNNqsNLYAf2t_E7UjvbmEFonpUq3Em340PHoQ5zNT49RV0MjPQbAPV6mjbicgyRhHhl2e9nWV6dbXtUfuoD8BZMOwYc7N4bBqEvnNsgSx9RfTtqxFV-dcaI5TROr4P0hiOxcnxM4aeCNaqmJwj_xRqD6i7LV63ezrSBGYwxgzFfvOleiyHS9B70MhKr0kBeT6kE_LHtvPJyqAvRbDYwxkzzUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام‎جمعه میناب از امامت جمعۀ این شهر خداحافظی کرد
🔹
حجت‌الاسلام والمسلمین محسن ابراهیمی در پایان خطبه‌های نماز جمعۀ امروز میناب گفت: این آخرین خطبۀ من در نماز جمعۀ میناب است.
🔸
حجت‌الاسلام والمسلمین ابراهیمی از آذرماه ۱۳۹۹ امامت جمعه میناب را بر عهده داشت و هم‌اکنون نیز به عنوان نماینده مردم هرمزگان در مجلس خبرگان رهبری فعالیت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450613" target="_blank">📅 13:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سازمان راهداری: تمام محورهای مواصلاتی کشور باز است
‌
🔹
در پی حملات دشمن به زیرساخت‌های حمل‌ونقل و آسیب به پل‌های ارتباطی در جنوب کشور در شب گذشته، با تلاش شبانه‌روزی راهداران در کمتر از ۱۲ ساعت با استفاده از کنارگذر ایجاد شده، تردد در محورهای آسیب‌دیده برقرار می‌باشد.
‌
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450612" target="_blank">📅 13:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddwuDPzq8vfNx_S7VSkYrGlNsjUXllTQjyuVRK16RmLYPVdiu9Kc_Oqs4VjBzeT7LJ3oI1yffpKlr4nefC76npPcxitEyjHQmqXfltzTndJXcRj_ZdbHz0eF18vlsRY8apD1yuvn3CVHFFT-RFtyDW9_AicZf5GAO7cn2KY8Pf1jFaRO7SRZ_ZeFX4UerPX6K93ZnunKdG3mUj2eGFez6IVJvjiTez0v63KibgRmGW1KL93Biwh471Xiz2QgiUyxRGTQnonNPPFrsOoPo1oGPd9QZ-THGu1ZvXhoWd5VYtqRrqVfrIWJhL_LnqSySUAvJJ4LOP4Ed6ZCGWOz1-IHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ مرحلۀ خونخواهی امام شهید از زبان خطیب جمعۀ این هفتۀ تهران
🔹
حجت‌الاسلام والمسلمین حاج‌علی‌اکبری: نخستین گام خون‌خواهی، مجازات آمران، عاملان و مرتبطان با این جنایت است؛ پس از آن، پیگیری خروج آمریکا از منطقه، حذف رژیم صهیونیستی از نقشۀ غرب آسیا و پایان یافتن جایگاه سلطه‌گری آمریکا در جهان، به‌عنوان مراحل دیگر این مسیر دنبال خواهد شد.
🔹
مطالبه انتقام، صرفاً یک احساس نیست، بلکه خواسته‌ای مبتنی بر عقلانیت، شرع و حقوق است و بر اساس آموزه‌های قرآن، خون‌خواهی مظلوم حقی مشروع به شمار می‌رود؛ رهبر معظم انقلاب در پیام خود این مطالبه عمومی ملت را تأیید کردند و اکنون این خواست به یکی از مطالبات اصلی امت اسلامی تبدیل شده است.
عکس: میثم علاقه‌مندان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450611" target="_blank">📅 13:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌  سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450610" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=Wxtzuxqo52B-ko2PKMHIwvO0vJDgcSKMrTrLwacvWbxlU0ZMqeJNhyHE1EhICQPR_f6UeKMVKXZPgynI1b2UxyQ9SfCBOvRFcp9VeZC1RQQ5jmqSZzsjdyRf4NkSO3s61MxFp3dR5-3cv2wYteJu0l-pXmSmxE0z0s5PvLKq1nFmdVUAbK-XN7DgbWd1DWo_eKM7M43-xcFd_tMqK90MPv3m6uJcMKane4Q3T7OfLmsMCh0AYnQcX8MV425Kf4I15ohl0-k2pSLAf1t81MH6hfMVqWDmHlrhvB-2N8BKtSPuoA5IKVCuGauTBV5QXHsQz2Nag8Ub0OkzQvReJxrkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=Wxtzuxqo52B-ko2PKMHIwvO0vJDgcSKMrTrLwacvWbxlU0ZMqeJNhyHE1EhICQPR_f6UeKMVKXZPgynI1b2UxyQ9SfCBOvRFcp9VeZC1RQQ5jmqSZzsjdyRf4NkSO3s61MxFp3dR5-3cv2wYteJu0l-pXmSmxE0z0s5PvLKq1nFmdVUAbK-XN7DgbWd1DWo_eKM7M43-xcFd_tMqK90MPv3m6uJcMKane4Q3T7OfLmsMCh0AYnQcX8MV425Kf4I15ohl0-k2pSLAf1t81MH6hfMVqWDmHlrhvB-2N8BKtSPuoA5IKVCuGauTBV5QXHsQz2Nag8Ub0OkzQvReJxrkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دعای سلامتی امام زمان(عج) توسط رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450609" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6150d53023.mp4?token=unp-Mn9ld2Q1DS_VfbibAU1XVdk4Z9SCgOA52CvFAQGTlWs-XbeFgW_ccpqs-AYNWbXxawYGPwZ4mykN_-kpraBgyWu-DP_9RN3gmDueM8cG857Jg3yquFd42GZ_DDlCvhAlTvzMFoHyGQlQfX6j3xp0hkopaw6spHGmMujKqCtJ7140YNP2p7M2wRsCHEp0pLpHGLMVlHPrClj0Bfgp2EGBWXXVuH75xrT9CScpbR3juTRqg2Jr_TYWuXJhoJ-J3ft6zkNH5XGFDoKY588xL6vjWz1SkFeZFTFiSl1EZVgsPp7xCLaij9Xdo9YDfbGbvs8nO8VH9hY6G_lwMOER1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6150d53023.mp4?token=unp-Mn9ld2Q1DS_VfbibAU1XVdk4Z9SCgOA52CvFAQGTlWs-XbeFgW_ccpqs-AYNWbXxawYGPwZ4mykN_-kpraBgyWu-DP_9RN3gmDueM8cG857Jg3yquFd42GZ_DDlCvhAlTvzMFoHyGQlQfX6j3xp0hkopaw6spHGmMujKqCtJ7140YNP2p7M2wRsCHEp0pLpHGLMVlHPrClj0Bfgp2EGBWXXVuH75xrT9CScpbR3juTRqg2Jr_TYWuXJhoJ-J3ft6zkNH5XGFDoKY588xL6vjWz1SkFeZFTFiSl1EZVgsPp7xCLaij9Xdo9YDfbGbvs8nO8VH9hY6G_lwMOER1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال نشسته ایران برای نهمین‌بار قهرمان جهان شد
🔹
تیم ملی والیبال نشسته کشورمان با شکست ۳ بر ۱ بوسنی در چهاردهمین دوره والیبال نشسته جهان برای نهمین بار قهرمان شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450608" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmgtXMM6CSv5FWTsOISWAHSKEg8QLGuvzTGA4YSCiEq38U_EZqWCaWjbKUt16lJpJRPqYyWuotNuZWznMJX7Hry9vjwAxDUuMw0ZqzhrlwH98kQ1scqqAG2mU7S7qmt2y3SayfgukspdUg0vtZnfK-020oVTFNCglnI9eCsCBVjalLcXpOsjgQFMMQzOszN9C_Mvl9_dPDS4iEczjjqEUY_iZ7WM1BmksicOHpWwE_RGdNyz01qX0C2EyZD97-IFkTAUYTI03baLV378GnlkN-jGHy6ApvCq0T8Ys7LId6Pv7sCUpSW2L41izQUOW--t6a_VD5pVi0JDPfyEeAHAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والیبال نشسته ایران برای نهمین‌بار قهرمان جهان شد
🔹
تیم ملی والیبال نشسته کشورمان با شکست ۳ بر ۱ بوسنی در چهاردهمین دوره والیبال نشسته جهان برای نهمین بار قهرمان شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450607" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450600">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV4VKIT2E_du7kwrHh7ktOHD2JKgVNNyxx-TtDfoPRm0aDhTrjEInWT9uAA4fIvHAgHQk2sCX7amZJSKpNv-Mw8TngPlsyTYHSk8CDy4oWGKxXW_0lFi1zC_bNdgERQhihbHMnK5snFERXsXY_cITsW4DNKEjag62DEDCbH4Y2u-qV8oH6X5F9_2FLMRwPkdZGsma-sl3ckrfnp3ZbFi1REYkD40bbZr1M2_qRiD2CRyoO5JLQCD_u4AzyO9yh5ZLUhY_rn06sr3YXgq-gIRHiI1v3amsyhmFXfZMi0tTTgFUihWRCqnOeuXi9jIWePbVZLgxBOV4dBb2C6fr4vsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKLc15SRBYxgbR_mRRfimjHPErKPoNMjBs4Y7Lvs64ZtqZ2k_bYMnhS3PX8Ccuh9st1rnI7XyuMg8L_goKj-r8Fs1R-IrEPA29NUdQ338hoJ9OaX3JBo9FBi5Y9N4pWyeaF-RSyrJ327EpjdmgyfAeqkAZCe2Ap_vDt8zuOKbf5Zh6sKWa-ZjuDVnqlzzFUKfttF_-09el2JitDEGfGZf0h6ieyR7V5IbOtaP0ZC5xJqSC7RHv47LGYqR1SF-2vzIGSPV3Dj3CrbReQ0ZH_0RG3mUZCXr8QBq5LKfgJBF-9axTecB0s5z8NfBEFryGSt_Mk3HHpRibQndZXoJrvRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMLWeNsT07esARpy7sY9sw0ARygECporPCHglRIlN1vA5l3_pjIddtDfZPsNb2XHEQPl6XsmvUoAG96tbHpa-Xquyx6BFiDGuJfsvSdSROz2Sj-OHoe__ZPZd9vKd0MBGbLq7KPvrxjahfrlQ1xKxLkHByBRaNY3icPukaNYz-3y9QWC35583bzIL2VizanopXgB2tZ-cO88v6Gxnqj0l9Nr87eNVG2YHqBC5KV0arvOEM_6JpdlN9acH99s0lOfBOyhBCDpHsTnNjgXAWgOn91u911WlHnAIHK3z9qq3IHga8RYs1rZNpehjyNfPvULE98ZKbYvQuodHfOBin-lLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450600" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450599">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادعای کویت درباره حملۀ ایران به نیروگاه و تأسیسات آب شیرین‌کن
🔹
وزارت برق و آب کویت مدعی شد در حملات ایران، یکی از نیروگاه‌های تولید برق و شیرین‌سازی آب کویت هدف حمله قرار گرفته و شمار زیادی از واحدهای تولید برق آسیب دیده‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450599" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuTvmcpCBsZisYVFyhfzRKhVSvkyt8hGdQT1CKMbeRA8HEMwDIUo0i3Wf4MoDVQwOfkLX6KhQzrLXmPRF-PZpcOq0upJKNnbvhRopsUo42BmZt5YZfe0peWuzFcsY8fafwZWKFD3_Qo2IIn2uCh6PPAS7Mj4ZPngHcI4zy52F4utNEx9v0U7G3Dx5H1mnrR-y9tZgaDMcBer-u7sfE0_gb8gyZ-utYUHEjWf6uyJpXL6QH6mDuughFkcSPQ0zOGZ5BzhNCBi9mJ8KijzUYiq6nuHbgYShbdHvVBR-8S-9T_ENvw_KA7_cibfBR440cCGOIJHqgnunn-JOH9w1weZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوی خارجی پرسپولیس لغو شد
🔹
شورای برون مرزی وزارت ورزش مجوز لازم برای برگزاری اردوی خارجی پرسپولیس که قرار بود در ترکیه برگزار شود را صادر نکرد و برنامه سفر سرخ‌پوشان در شرایط فعلی لغو شد.
🔹
کادر فنی پرسپولیس تصمیم گرفته تمرینات این تیم را فعلاً در تهران ادامه دهد و اردو نیز در پایتخت برگزار خواهد شد تا برنامه‌های آماده‌سازی تیم دچار وقفه نشود.
🔸
باتوجه‌به شرایط فعلی کشور، احتمالاً مجوز برگزاری اردوی خارجی برای هیچ‌یک از تیم‌های ورزشی صادر نخواهد شد و باشگاه‌ها باید برنامه‌های آماده‌سازی خود را در داخل ایران دنبال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450597" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILxPMqpEfJD6ZZyMtU3LfLNCcOqiebaQsig5Sv6Dj0-BEz2GhQ4Hvc0LfCJoIU0DNIzThhQuSOpN-ixDoQKdlSMgG0gli0k-YznTeIf8jJGpvYwhfG9AlLe7Zzs4NiEJy9GS67PUQFBtxTewevXXo0ze3GAx6LR6JteYvF4PdllPqDfo9f5OVtQW1SBx6I9bs_guvMoawBZD1PcCRw10WAe5xyGfSyjOrqenIQXoY9Qc4e76210GNoMeKFa1X59FgDhro4A7MPgXQ1hIiRPo-f6kCdFHb8d1XIBWdn2V0rk7E_ZqsF32886VEOInsNpsU0r0MBKiSGuWHiYxkS8V9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع حادثه دریایی برای یک کشتی در جنوب یمن
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه دریایی در فاصله ۶۵ مایل دریایی جنوب شهر المکلا در یمن دریافت کرده است.
🔹
بر اساس این گزارش، مقام‌های نظامی اعلام کرده‌اند که در جریان حرکت یک کشتی به سمت شرق در خلیج عدن، افرادی بدون مجوز سوار این کشتی شده‌اند.
🔹
این نهاد همچنین به تمامی کشتی‌ها توصیه کرد که با احتیاط از منطقه عبور کرده و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450596" target="_blank">📅 12:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترکش حملۀ آمریکا در قلب کودک یک‌ساله بندرعباسی؛ مادر شهید شد
🔹
دانشگاه علوم پزشکی هرمزگان: در جریان حملۀ بامداد امروز ارتش آمریکا به دکل مخابراتی در محله تپه‌الله‌اکبر بندرعباس، یک زن بر اثر شدت جراحات به شهادت رسید.
🔹
در این حمله، فرزند یک‌ساله این مادر شهید نیز به شدت مجروح شده و بر اثر انفجار یکی از دستان این کودک قطع و یک ترکش نیز به قفسۀ سینۀ وی اصابت کرده است.
🔸
نیروهای مسلح کشورمان شب گذشته در پاسخ به حملات شرورانه آمریکا، پایگاه‌ها و منافع ارتش تروریستی این کشور را هدف حملات متعدد موشکی و پهپادی خود قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450595" target="_blank">📅 12:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfZX4Od9xa9RjsTtjWIoWXpdpb9YN2rBdjvbmoeVxZ-0ab7DKaHMRY4i1y5Ke_agRs6KIncsJ9KYrqwrHLAjzrhj0TcNEzcYWF4ebcFgm7_P-LMgJuPQt-u4V1DcWvptLeSHz_PF9AF1nJDuJM0mAqcCUv3xkLijEX0N-r2t_WxVxdeyLZs29VgrsOTG8u5TDJs07KDDcEYaEk30SJQdk-qTPgem5K0eEDQMRTU0BCyPDZdb6FgcwO8nuTP0u045kCgqaxIcp-kJWaN6OsKXOv1TEsXe8dQ4WWj7zW1JyWLkY42ooys-BztVnzG8Wmf92H6un7kpzbvzLlZ9v0Aflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو مجلس خبرگان: قدرت، تنها تضمین احقاق حقوق ملت ایران است
🔹
حجت‌الاسلام صلح‌میرزایی در سخنرانی پیش از خطبه‌های نماز جمعه تهران: تجربۀ شکست‌خورده برجام، مذاکرات عمان و همچنین تجربۀ مذاکرات و تفاهم‌نامه‌های اخیر نشان داد آنچه می‌تواند حقوق ملت ایران را محقق کند، تنها قدرت است. اگر به دنبال امنیت هستیم، این امنیت فقط از مسیر قدرت به دست می‌آید و هیچ امضایی تضمین‌کننده آن نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450594" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
تصاویری از ستون دود برخاسته از مقر تروریست‌های تجزیه‌طلب در شمال عراق  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450593" target="_blank">📅 12:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شهادت ۳۸ هم‌وطن در اثر حملات آمریکا از آغاز تیرماه
🔹
وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن شهید شدند؛ در میان آنان ۲۲ زن مصدوم،۳ زن شهید،۹ مصدوم زیر ۱۸ سال و یک شهید زیر ۱۸ سال دیده می‌شود.۴۷ نفر نیز بستری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450592" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj3Za9UYCBEOl7oH3tpnrw0yC5YUGBpnvimuqiE1hSGBqao6rIwX-5cRmcLyiwWJRRR8q3SLYG35qlL67BFfdpLMrxIF6AgWn_yu5IuGgc0WKIfdiCzkpjf22ue2htAmhl7dZf3tj8n713KaD0IR7pHIG4QbJ4nDTt7p6eR47a1-MIv2BvC6QLRECLEZlezzz-aUTWTArYepVqYe0WNSORymDu5qd9XP-8IHAbuNbTGPPweHv5PnfwQrw1W8X22XbVnZTWxOpScLGQZGN3qZvPp3WZ8ETczJMwuDP0uNDFdRdp5PATY7MVaefXd6lSvRxNPBPipj_3dMlgc8wAC3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله به چابهار ۵ بندر کلیدی منطقه در تیررس پاسخ هستند
🔹
حمله به زیرساخت غیرنظامی چابهار به اعتقاد تحلیلگران یک اشتباه راهبردی از سوی آمریکا بود؛ چراکه فهرستی از بنادر تجاری حیاتی میزبان منافع آمریکا در منطقه را در اختیار تهران قرار داد و در پاسخ، نیروهای مسلح ایران می‌توانند شبکه‌ای از بنادر کلیدی را هدف قرار دهند:
🔸
بندر جبل‌علی (امارات):
بزرگ‌ترین هاب کانتینری غرب آسیا با ظرفیت ۱۹ میلیون TEU و پرترددترین بندر خارجی برای نیروی دریایی آمریکا که سالانه میزبان بیش از ۲۰۰ بازدید ناوهای جنگی است.
🔸
بندر مینا سلمان (بحرین):
مقر اصلی ناوگان پنجم نیروی دریایی آمریکا و مرکز فرماندهی، کنترل و هماهنگی با متحدان منطقه‌ای.
🔸
بندر الشعیبه و کمپ عریفجان (کویت):
ستاد پیشروی ارتش مرکزی آمریکا و گره لجستیکی زمینی با انبارهای تجهیزات زرهی پیش‌موضع‌گیری شده.
🔸
بندر حمد (قطر):
دروازه دریایی بزرگترین پایگاه هوایی آمریکا در غرب آسیا (العدید) و مرکز پشتیبانی لجستیکی.
🔸
بندر صنعتی ملک فهد در ینبع (عربستان):
یکی از سایت‌های لجستیکی کلیدی برای انتقال نیرو و تجهیزات توسط فرماندهی مرکزی آمریکا.
🔹
پاسخ ایران، نه در شعار، که در ترازوی «موازنه آسیب‌پذیری‌ها» رقم خواهد خورد؛ جایی که برتری با کشوری است که شریان‌های حیاتی دشمن را بهتر می‌شناسد و اراده‌ای آهنین برای فروپاشی آن‌ها دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450591" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کویت: در حال مقابله با حملات پهپادی و موشکی هستیم
🔹
ارتش کویت اعلام کرده پدافند هوایی این کشور در حال تلاش برای مقابله با حملات موشکی و پهپادی از سوی ایران است.   @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450590" target="_blank">📅 11:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivufCdSHjJby58BL1QpIY5LP_NWeMotp0pK_23a-_226mtppFuqPpk1fGpmZMKtWCKaDPsmr3i-DheOVcGe9GwUZo8JDxHEh412isnW0YPPG-nHG3eKuLTZPdcF6DKr_hQoDmfW2BPbO17UzbOPBPATLRJkEJm1fjd2nDjuFaW-BMpl56Lq4eR4gdR5ygwyNLbgc3hFqTFCsWcPlNXjLf3lC3RhYXRJxwAH1uSY_1YMRKjDrFfwwfNweMJqnVf1vUIZsHIOZZqehe0eZITxYIHf3H2UdnKmG2rpWXVBqrAMN8urnz3QZTaR-n5pT7kuuYUI4-KznMAKr_uIKoZyqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه خاص فیفا به قهرمانان جام جهانی
🔹
برای نخستین‌بار در تاریخ، قهرمان جام جهانی «انگشتر قهرمانی» هدیه می‌گیرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود و انگشترهایی با تعداد محدود هم برای هواداران در سراسر جهان عرضه خواهد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450589" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
راهپیمایی عظیم مردم یمن در صنعا در جمعۀ موسوم به هشدار و بیدارباش
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450588" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انهدام چند فروند سوخت‌رسان و جنگندۀ آمریکایی با موشک بالستیک و پهپادهای متعدد
در موج۱۴ عملیات نصر۲
🔹
سپاه پاسداران: مردم شریف اردن؛ مردمان نجیب سرزمین قدمگاه انبیا الهی، ای مردمی که بیش از همه‌ی مردم جهان با فلسطین قرابت دارید و با دردهای مظلومان غزه و کرانه از همه آشناترید، بعد از حمله سال گذشته ما به پایگاه العدید قطر، ارتش کودک‌کش آمریکا برای دور کردن مرکز فرماندهی خود از حجم بالای آتش رزمندگان اسلام، مرکز فرماندهی نیروهای آمریکا در منطقه (سنتکام) را از قطر به الازرق در خاک شما منتقل کرد و از آن موقع تاکنون مرکز فرماندهی شرارت علیه مردم فلسطین و سایر کشورهای اسلامی در خاک شما و دردسترس شماست.
🔹
علاوه بر سنتکام پایگاه هوایی و دهها فروند سوخت‌رسان، اف۳۵، اف۱۵، و اف۱۶ آمریکایی در خاک شما مستقر هستند و از آنجا به مردم مظلوم فلسطین، ایران و لبنان حمله هوایی می‌کنند.
🔹
شب گذشته ارتش کودک‌کش آمریکا بازهم شرارت کرد و از پایگاه‌های خود در اردن برای ارتکاب جنایت جنگی بزرگ و زدن اهداف غیر نظامی از جمله چند پل، محلات مسکونی و یک مرکز پمپاژ آب در بندرعباس در جنوب ایران استفاده کرد.
🔹
در پاسخ به این شرارت، رزمندگان اسلام در موج ۱۴ عملیات نصر ۲ با رمز مبارک یا صاحب‌الزمان(عج) ادرکنی جنگنده‌ها و سوخت‌رسان‌های آمریکایی مستقر در اردن را در دو مرحله حمله با چندین فروند موشک بالستیک و پهپادهای متعدد مورد هدف قرار دادند که منجر به انهدام چند فروند سوخت‌رسان و جنگنده آمریکایی و آسیب جدی به تعداد بیشتری از آنها شد.
🔹
اینک نوبت شما مردم شریف و ارتش غیور و با شرف اردن است که به تکلیف الهی خود عمل کنند و با ضربه به منافع آمریکایی متجاوز و ضداسلام، لکۀ ننگ آمریکاییهای اشغالگر را از دامان اردن عزیز پاک کنید.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450587" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdgCCnwzjBKU3rO3BE11ryGHCdoosZQUPXvMA8IjxSDUm8Mp_vvVbZCnL6AXKtVd2EYWZtQgDdZiwy7ZVfq6p2Qt66ad7BZOe6xuPf8CLUUn838VdqzYLzbGNPAUck99_mUyHde0X2EKKoFSXszcclLWqA6Po5I2j-wolNpF9AtRHzvmstEzF-B539IDGNYzOSnvs5D_mviXa0s1MukBYTCN04OFN_AdjjsrfNn70wb2_aqXgMaMmY1TQNKXzCjik4FOS9X4K4gz7Gmt8RgbH55ZdwE5C0kE3YwG7TLB67is5YPVAaCuuNTtdOwXJ9aJVMh0aJuqhTn-3dVJUY9UwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بلیت اتوبوس‌های اربعین اعلام شد
مسیر تهران ـ مهران
🔹
اتوبوس ۴۴ نفره؛ ۱۲۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۷۰۰هزارتومان
🔹
۲۵ تا ۲۷ نفره؛ ۲۲۰۰ هزارتومان
مسیر تهران ـ شلمچه
🔸
اتوبوس ۴۴ نفره؛ ۱۳۵۰ هزارتومان
🔸
۳۲ نفره؛ ۱۸۵۰ هزارتومان
🔸
۲۵ تا ۲۷ نفره؛  ۲۳۵۰ هزارتومان
مسیر تهران ـ خسروی
🔹
اتوبوس ۴۴ نفره؛ ۱۱۰۰ هزارتومان
🔹
۳۲ نفره؛ ۱۵۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۱۹۵۰ هزارتومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450586" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th8dipdI-Itv3IXhWmWV_VZFYtG1q3kzDZ26Gpp9l2hVady67L5hSRVop1EBj_X2pKSporyff4XMBsoUvVN1PlHp5LsM0BBKz4NKQSE5vT1johJW_Je1_2mKj-yr_G0eHlh9Aifm7JDp8U2hBmt4x8DfE7w2VRW9k5azgfpd5SaW92GcmGVUW3qsP3AjVhE1vamdgmkKaTGADA9MwokJCBOi3VpMluv_Hi3korcH4NVaanFP1FtazJ-hdTVL1fuHSo4_d7DKRkK7I7TAxlUCif1h7qgja-EKIucBgxdq1-ehKLmwkMadqIdxgDzd_tkMjWBjbkNSdzlemCbtoGDWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین اقدام خصمانۀ آمریکا علیه خبرگزاری فارس
🔹
در تازه‌ترین اقدام خصمانه علیه رسانه‌های ایرانی، آمریکا با اعمال تحریم جدید، صدور گواهی امنیتی (SSL) برای وب‌سایت خبرگزاری فارس را مسدود کرده است. این اقدام که به اختلال در دسترسی کاربران و حذف تدریجی اخبار از نتایج جستجوی گوگل منجر شده، در ادامه سلسله‌فعالیت‌های هدفمند واشنگتن علیه خبرگزاری فارس ارزیابی می‌شود.
🔹
بررسی‌های فنی انجام‌شده توسط تیم فناوری اطلاعات فارس نشان می‌دهد که درخواست صدور یا تمدید گواهی امنیتی این رسانه نزد تمامی مراکز معتبر بین‌المللی صدور گواهی عمومی (Public CA) که مورد اعتماد مرورگرهای اینترنتی هستند، با رد درخواست یا عدم ارائه خدمت مواجه شده است.
🔹
در میان این مراکز می‌توان به Let's Encrypt، Actalis، Certum، GlobalSign، DigiCert، Sectigo، HARICA و سایر ارائه‌دهندگان معتبر اشاره کرد که به دلایل ناشی از سیاست‌های تحریمی یا محدودیت‌های داخلی خود، از صدور گواهی برای دامنه‌های متعلق به خبرگزاری فارس خودداری کرده‌اند.
🔹
در نتیجه این محدودیت، امکان استفاده از گواهی‌های امنیتی مورد اعتماد مرورگرهای اینترنتی برای وب‌سایت خبرگزاری فارس از بین رفته و علاوه بر اختلال در دسترسی کاربران، این موضوع می‌تواند باعث نمایش هشدارهای امنیتی برای کاربران، کاهش اعتماد مرورگرها و تأثیر منفی بر ایندکس شدن صفحات در موتورهای جستجو از جمله گوگل شود.
🔹
خبرگزاری فارس همواره در خط مقدم تحریم‌های غرب قرار داشته است. پیش از این و در بهمن‌ماه ۱۳۹۸، دامنه دات‌کام این خبرگزاری به دستور دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) مسدود شد. در شهریورماه ۱۴۰۲ نیز نام این رسانه و مدیرعامل آن در فهرست تحریم‌های SDN قرار گرفت. این تحریم‌ها اما به آمریکا محدود نشد و در گام‌های بعدی، اتحادیه اروپا و کانادا نیز همسو با سیاست‌های واشنگتن، تحریم‌هایی را علیه خبرگزاری فارس و مسئولین آن اعمال کردند تا بدین ترتیب فشار بر این رسانه از ابعاد بین‌المللی تشدید شود.
🔹
محدودیت‌های اعمال‌شده علیه فارس صرفاً به حوزه وب‌سایت محدود نشده و در ابعاد مختلف رسانه‌ای نیز جریان داشته است. در همین راستا، صفحه اینستاگرام خبرگزاری فارس با نزدیک به ۳ میلیون دنبال‌کننده، چند ماه پیش بدون اخطار قبلی از دسترس خارج شد.
🔸
با این حال مخاطبان می‌توانند با نصب اپلیکیشن فارس دسترسی بهتری به خبرگزاری داشته باشند و مطمئناً این محدودیت‌ها نمی‌تواند خللی در انعکاس اخبار و پوشش رویدادها ایجاد کند.
🔗
اپلیکیشن فارس را از
اینجا
دانلود کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450585" target="_blank">📅 10:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4VSWfbNGYTD5of0SdZzjHlAXD90Q8H8RGQAsoQDBVOyWCQhFZDnmiDGLK2w22pUcaAXtiz2aG2Tob5nANjJX6zlC58tCb4siPKc5AS52sIuiqhxW7sqD98oxkXr6AODiI47wCpyNhHRo0ss5U5m_SS0rR1r_MGbGFK7lhRn6WdLRXDptl8RO4YfiaZlNWBsLuyP2y95dW74lJiqgULM2NSAWwHluL2Yy2l00J4-DLWVbdxiq3NH6lh23XiK1UEO6TjUpE9QXIZ2ICo_2Dp1R64cNSZGXcwDii2SL6H-lEQTRulP8tKv29kJo6g-VTPiwx7E2iBLBuRCP6cLDga8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عزیزی: جنوب سرافراز همیشه سنگر دفاع از ایران بوده و قلب تمامی هموطنانمان آنجاست
🔹
رئیس کمیسیون امنیت ملی: جنایات آمریکا در جنوب کشور مانند مدرسه میناب، بیمارستان کودکان سرطانی اهواز، سالن ورزشی لامرد، حملات مکرر به مناطق مسکونی و غیرنظامی و... نشان دهنده‌ی ناتوانی و استیصال ارتش مدعی حقوق بشر در رویارویی با ایرانِ فاتحِ جنگ ۱۲ روزه و نبرد رمضان است.
🔹
دشمنان ملت رشید ایران باید بدانند که نیروهای مسلح از خون ریخته شده افراد بی‌گناه گذر نخواهند کرد و روزگارشان را سیاه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450584" target="_blank">📅 10:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به انشعاب راه‌آهن بندرعباس
🔹
استانداری هرمزگان: حوالی ساعت ۲۴ ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی مورد هدف قرار گرفته است که متأسفانه در این حادثه ۲ نفر از هموطنانمان مصدوم و به مراکز درمانی اعزام شده‌اند.
🔹
این ایستگاه…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450583" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرا امروز برای جنوب گریه می‌کنند؟
🔹
چطور ممکن است کسانی که تا دیروز در برابر جنایت‌های دشمن در شمال و جنوب سکوت کردند، امروز مهربان‌ترین چهره‌ها شوند؟جریان‌های ضدانقلاب و سلبریتی‌های همسو، که حتی یک استوری برای مدرسه میناب و جنایت لامرد نگذاشتند، ناگهان از «جنوب مظلوم» با اشک می‌گویند.
🔹
این دگرگونی، نه تصادف که قطعه‌ای از پازل دشمن است؛ تکه‌های پازل را کنار هم بچینیم:
🔸
تکه اول: مهربانی‌های تصنعی
کسانی که ماه‌ها دلواپس ایران نبودند، پرچمدار دفاع از مردم جنوب شده‌اند.
هدف: جا انداختن این باور که «دولت جنوب را فراموش کرده» و کشیدن مرز بیگانگی میان مردم این خطه و سایر نقاط ایران.
🔸
تکه دوم: ایست‌های بازرسی، هدف حملات رسانه‌ای
رسانه‌های صهیونیستی (مثل اینترنشنال) بی‌سابقه‌ترین هجمه را علیه ایست‌های بازرسی ایران آغاز کرده‌اند.
هدف: القای «مزاحمت غیرضروری» بودن ایست‌ها؛ در حالی که این سنگر اصلی مقابله با نفوذ ضدانقلاب در کشور است.
🔸
تکه سوم: پل‌ها و اسکله‌های جنوب زیر آتش
حملات نظامی به زیرساخت‌های جنوب تشدید شده تا مسیرهای تدارکاتی قطع و انتقال نیرو و تجهیزات مختل شود.
🔸
تکه چهارم: القای «بقیه به فکر نیستند»
بی‌آنکه مستقیم از آمریکا نام ببرند، ذهن را به این سمت می‌برند که «اگر حمله‌ای شود، تقصیر دولت و غافلگیری است»؛ یعنی از حالا جبهه داخلی را برای پذیرش شکست آماده می‌کنند.
⚠️
آیا این چهار رخداد، تصادفی‌اند یا زمینه‌چینی گام‌به‌گام برای حمله زمینی؟
🔹
۱. می‌خواهند بگویند «دولت توان دفاع از جنوب را ندارد» ← تنهایی جنوب
🔹
۲. می‌خواهند بگویند «ایست‌ها سد راهند» ← قطع همکاری با نیروهای امنیتی
🔹
۳. پل‌ها و اسکله‌ها را می‌زنند ← بستن راه اعزام نیرو و تجهیزات
🔹
۴. شکاف شمال-جنوب را دامن می‌زنند ← تضعیف دفاع همگانی
حاصل در یک جمله: «راه را برای حمله زمینی هموار کنید.»
چرا این دلسوزی امروز، نقابی برای خیانت فرداست؟
🔹
این «مهربانی» نیست؛ مقدمه‌چینی است؛ دشمن می‌داند ایران نیرومند، مرهون مردم است؛ مردمی که پشت ایست‌های بازرسی ایستاده‌اند، جنوبی‌هایی که مقاومت کردند و همه ایرانیانی که در برابر تفرقه قد برافراشتند.
🔹
پیش از هر اقدام نظامی، باید این سه ستون فرو بریزد:
🔸
مقاومت مردمی را با تخریب ذهنی ایست‌های بازرسی خنثی کند
🔸
همبستگی ملی را با القای شکاف شمال-جنوب از بین ببرد
🔸
امید به دفاع را با القای ناتوانی دولت ناامید کند
🔹
دلسوزی‌های امروز، دقیقاً همین را دنبال می‌کند؛ نه نجات جنوب، که بی‌پناه کردن جنوب؛ جنوب تنها نیست؛ پشت آن، ایران ایستاده است.
🔹
همبستگی، هوشیاری و ایستادگی، پاسخ روشن به این سناریوی شوم است.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450582" target="_blank">📅 10:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQdH5g5modxyj7MwyUJuq8Zv9t-8vu7VbBdDoN-xIjGhiApxinPGjZkhRuBp_qlVLZbr8XC07CTncsMULVFSVZzv5ErK4uNI0E8MWxodAjXIJsEbCHu5IhErog6jYCiC2f66WHZEgBq8GpvmL13aEKWKn1Tj9Q2l-WA559jZbS6mCCFd5rD8p3mjetWtob85DsSj3E248x2UzVn2Bk0SSvT0o_mu60t9Fd_HuZkc_QZGqoN345qPZrtDi5SAyjhHArnZ6wnMOOXSuIIN9cbce8azdJ0VNqYS3LjChc_PX6IbzOzDu1tz6FlYdyVeV981QpMxnUWvWWSfXZMlIsZ-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
🔹
سازمان تجاری دریایی بریتانیا: یک نفتکش در شرق خصب در نزدیکی سواحل عمان مورد اصابت پرتابه‌ای ناشناخته قرار گرفت؛ این نفتکش گزارش داده این برخورد موجب آسیب به بدنه در سمت چپ (پاشنه) کشتی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450581" target="_blank">📅 10:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJA-gzW2hZTYcHaMrIAhUmrplBXrboQaSCkkr-2xv4z679bwZRfoXVvPUZZ16BLruqxYdsIK4rk2_tle8BdoihzZ8udaGrOKzUypr2rs3yPcS99bbYDEAIfJ9FYLsEt1abEMrTAOX7DFM8QEUXjAqANy1Z9IRZSonUVKVcSmsO7hwkbdqyAC4EDWKwnV3-Psnn_Y_x4ZXElJ8mdZpB871bjEBEo64YbKWXq-1JnLYrU7vuStbdIpkktng6tKXbyZGKite7dpzrBrXd4CNdsjbxzWXZqTFAHpjQHFNUq4gtFr1lE6DjyjFXKY1-xarTkDl7vsKoyZR0Zw2uy-Use8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب‌نشینی ماه و زهره در آسمان امشب ایران
🔹
ماه امشب در کنار پرنورترین سیارۀ آسمان یعنی زهره، مقارنه‌ای را با یکدیگر خواهند داشت که در آن تقریباً ۲.۶ درجه از هم فاصله دارند.
🔹
این مقارنه از حدود ۱۵ تا ۲۰ دقیقه پس‌از غروب خورشید تا ساعت ۲۱ در قابل دیدن است و ستاره قلب‌الاسد را نیز می‌توان درست کمی پایین‌تر از ماه و زهره دید.
🔸
این پدیده معمولاً با چشم غیرمسلح قابل مشاهده است و نیازی به ابزارهای حرفه‌ای نجومی نیست؛ کافی است در زمان مناسب، آسمانی نسبتاً صاف و دور از نور شدید شهر حضور داشته باشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450580" target="_blank">📅 09:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIgjKH4DmM97vDUNMMFjTY5-TMktQSaX8fuWakNgA5rG076JI509f2AHB7dsSpZVU_2QSNJ05nyDV4clpoVgOjodrO7mYkQ0H9Yq5ddD6pVhMrVq3zoijWDnU3LaHvY-EJUeuFf2rK7p0UxAeQcNh-2E1HjuqYOiIdiPPGX9WWjfK79DcAUW2DeDnxKd74oTVWXHapuokcWjTdV27xfLq3tAfc73hbwhS2GAto1grTZWl3DJMoX13TmFZFSdq9chL338-aspvRv8hzMahAzQXh3NbQtT9Gm6vQPVfvhk8228J-W8BHkFwAYXKvDRrgviso6NDoNgjHRIznZFa9Ncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۵ دستگاه ماینر قاچاق در قشم
🔹
فرمانده انتظامی قشم از کشف و توقیف ۱۵ دستگاه استخراج غیرمجاز رمزارز دیجیتال در یکی از مناطق روستایی جزیره قشم خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450579" target="_blank">📅 09:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLpbWP5M-BwXTOXz1-Yb4f35-fBXf3qqh1C48sWLGppv20FeF9OW7k8IZfEVeQzxfpGb9FIVrp424borRqAD_nI_XnxRkNGpjcKOsnkal-bGP_0nxopDxPvpXhq8HiAlDi9H3vqs_flkEPvfLfQ8E45_tSfv-kwvGXq6Rrigw2MfyK_Im1e6HUeg0uNzKoG539hvbfNmztB7nt2q_1ZragrWI1t3oQ6sFi5N8By7T5KJM5NJ_eIC8Yzw-aXx6sCpLlEeS4HFL6_DKJofSJCA-1xyZivP-HyRA40mClWqFHF03UL1n3UGwG1P5FshcoC0RTy-JE80WM8CUbbyFO9Zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcUI09Ib8nrsfpLfVAi8SYCM5XXYOUMr5JIhE1CCOb28XXVin-kaJDK-I3xzXhmOa2HO1y5xzjzGPmlHqGz0p8_lOsEchjqClLC-evzmH6eGqTqdyPub9sXDNfGhVRW1lfrAs4P6CcDW5LnWqjDR_ihkXnFvXA-fRkpqDHOBBD08SPpNrQdXjFPLE5IKVk3c_hcK2-1FG1NMSg3fxx-SafZZcu7hsWXjPSIQSRTCH5DzN1YXwRdK63fXWdLts4dk3Sgy0s0jn9CMR45AoOhVfxFf5dssfozptM6t1S64lGYW3fYD97GErTPOr_xURqdG4EFhLzObcuePbFdtCX1BRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvsMLxZLJuufmVPwJPO903esBkyjDavwAjH8fWLC-RjMWu28QQXYk_fXWdMRUTzHNYHBdb99M8K4xcTqyjvXNesgg5esc6Rubde2vKy6g0fvjUh0dQUTiS8Ga_sjH1_tzDkLRFhgV8XI6j53R28TjzwFZkLvT3TrYNzInJH3n2SdDONlnDJ5FLj9m3YDpE8zx8YzwHJ4DVYxDmznWh8LhHU7AyogDznEX-8AKi9enHVWt79_yGlX-hSeuasu7ExREUBIHb3ZNr4GWH43d37BD5hex3WxxnRI9dyHEV3uoy1tPzX-A2xm4MagARRm6Ct5xMGw7sBCqhwMtKtWCBZ7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmazH7V1kqof_52de4YyhMIvc3Jrw8cV9IrlpLqZ8OvtUxGtHI3-D8z26dtkS564W3X3SuOeciHiNqwwfLZKZgRpK58OCjynwJt4AjGKshNEVnvyLvD45dc5jgiyyX7Fmqd9aLFKkXEqU3kESSTIyEv2K24pZb-Q04MqSJvtGPlx5qCTN22lqpuZFj4ClJn9Mk7qSbda1MSckNRgg6J-MXfHf9fpAr0Cg-q-3RY3Fq9pH9wrVJ5eJ4QtQyguuS4JTgJEBTrr9eRg83NPHcFga00SeuL7Stn_BP3t9OGGQQfWgyQW97TL7Y8bXB_LREkcWubyJ_SleJAu3yFx7sFo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/To_I86ZV1E1Ala5x19TtSpzlLtKakKAh6ITIeWEctIjH-i6fBcP5JnKidw4kk5DEONQx3WRkw3e1B_EzSFa8StOZ4S90Ta1nLY5npeu1zzI-4_S2KBh1s6NNekf2-yaodkaVHxNG9BHUgp-q2x3lqnrvbLxj-VlYEhM0ZNlHrmhWp8vDamRzQTJBuqWhquVlQplNsGE2giGzm9Yv9ldGr-w2YMgiube-C00wiLcAyr4ll9vXUG8EivSfPyYNVu-9gfJ7EUk02VcMAVu-xphCQI6kEVCZXHDGqQvoxntbhSfcHfxNAzUbYTGS4OuWYHljtlDgSP9JQObB-O6gapfiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKRljNHSNe9x0VGSsdFVK83Gf9gvDXNlKlGMUKKWKcRwhX-D5zVjsCKiNImfA9WiMd6YUrMwLD-2rsMi289iSVcP4C1m_Ptzsc-Qzp8WGbqjgOxa9xv6JdfAHVOoTi4Q-__VdV3xcSS7M9JeV_JXWZbsGLBcsIMtgZSYdx8TbcG3NUM1dDm5uhp4fOi3TJJHUFs-cPECMVxTCJoKtCphmZ0Gcpg4c3pK5QKyL5NmDI_WI-dTDccqc7uLR41tLSyBj0M1zdVoW7rX9iAsXYbF4BlZDHEc4eNkoWcdAlxSTyOZz_ak5_UQ0A-UEGyBa3qHwaihZU_5wepcKLZ7-pGkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7ANzObCLmtO99BSLVZekuJAmC_YtS83MCFhK8mLKGDzdDUHEtdLyUU5Ax68_8TJ_-45KqGz8_wy3-1j7EZThTQzthp_cDp5P7Dxm-r1m65CnxhK2upaSdDC2DNKEEj_sjAG_WR_fpTnXQ-lJZBKFe4kKn19IPLkHNZffTLECgW78MgIOiFoOmpSr8lB8EQ-Nn2aJMhvb6w9W9QjNS8XgmR5i6JWHg6nxofe4ngbp8LmCRyCyaBx5HdsXoBP0kBhljpb7L_PddUuhTOTftjwYzFW9mzHGlg8SHhKmWGCTpBAS6iNIWFVohv4Vhp1L8re9wdEXSY_WPfRYWoyfgVTMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رویداد هنری «مشق ناتمام» بر فراز پل طبیعت
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/450572" target="_blank">📅 09:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/169d29cc88.mp4?token=cJATQmHAwzsJyLOxVAcqx5KG0CGCSaJgi-CfyxmLzTEbvn3-rrkS9_H2G2fOG3z7_7OwH5SCQo8Yjcmq_WfUCjoQgRplMykIwCtdTEaB9HWx4ba-cByn3g2fA79pOkUePEWjo0BryfmvqZWAErG35IlecqUC9a5-xtSHBsKe483Ea0u-OJuPMQUUpRfgF5X4L-nB-mG0z7IB000becWNY-DnhMdOX38Sf-nlgE03eBVXqtyq_9sZAxMLiVxJwW4fdGtqoUgd61qUGizaiVlUGr1JjQZZWoTngJp_PUoqYad8MgavN4S_KmStMzRUP68qxWMUi5DnOyHzVEyTIi5Mgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/169d29cc88.mp4?token=cJATQmHAwzsJyLOxVAcqx5KG0CGCSaJgi-CfyxmLzTEbvn3-rrkS9_H2G2fOG3z7_7OwH5SCQo8Yjcmq_WfUCjoQgRplMykIwCtdTEaB9HWx4ba-cByn3g2fA79pOkUePEWjo0BryfmvqZWAErG35IlecqUC9a5-xtSHBsKe483Ea0u-OJuPMQUUpRfgF5X4L-nB-mG0z7IB000becWNY-DnhMdOX38Sf-nlgE03eBVXqtyq_9sZAxMLiVxJwW4fdGtqoUgd61qUGizaiVlUGr1JjQZZWoTngJp_PUoqYad8MgavN4S_KmStMzRUP68qxWMUi5DnOyHzVEyTIi5Mgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450571" target="_blank">📅 09:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه پاسداران: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم شد
🔹
در ادامه عملیات مقابله‌به‌مثل، سحرگاه امروز رزمندگان نیروی دریایی سپاه در موج ۱۳ عملیات نصر ۲ با رمز مبارک یا اباعبدالله الحسین(ع) و تقدیم به تمامی مردم‌خون‌گرم استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان، رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان را هدف قرار دادند و منهدم کردند.
🔹
عملیات مقابله‌به‌مثل با قاطعیت ادامه دارد، همان‌گونه که بعثت جانانه شما مردم؛ و تنگه هرمز هم به فضل الهی کماکان در قبضه قدرت دریادلان نیروی دریایی سپاه است.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450570" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwgGzZbou3522f743ZveivHCfPuYWuBq72w-sa7yw9TeMm7O4S8XEZgTaTFSbhsXVQZjGwX_8_Y-T8arra5Ms0jQQV-mPfbYiP6aCEYBP782myhQ9k658kg0pdz2rdUnK3Vd12NLgEYzs3CD8d2zryP4zb0KCodFmin_1BynMHJg33SS_6fd8SY9bKk_HTUCOpJ0-08pyp-GND7HRgazPWkF9n45FrNYf6uRsMJXPUo5NKLfq1soOzT57IRYBuZDGTyqiXJKHHcwUry1oJLogjh8ej17uvMlkgz9ZGxiWnLh4wZMy2xSt83oVnxY9aN29siW3AfiGaGX_hLeUASpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اعضای کنست به انحلال آن رأی دادند
🔹
۱۱۰ عضو کنست با انحلال پارلمان صهیونیستی در قرائت مقدماتی موافقت کردند؛ پس از تصویب اولیه، طرح انحلال کنست برای بررسی بیشتر به کمیسیون‌های مربوطه ارجاع داده خواهد شد تا مراحل قانونی قرائت‌های اول، دوم و سوم را طی کند.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450569" target="_blank">📅 08:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913d736794.mp4?token=dTPm_YpQRUkMbTwS7mH_GPovoB_e56jskGtt-qSy4TCkSq7oozKqqezNjrtAHrwqFWePbDtXZ6JpH6XgqxADAQy4ITu7ypHWEjI25iGanmER4CZRp5-sDB56h_oCgfNdoQXZwxRnwA9xVA_7fQeLSn4sgDXNU1XXyjoFfb3ooMmASX7_LkJrZKkiOzgF_ovg0J8u8WTVIsNHP-0olIwSPiqiXSxoXC7CEHH_XPExpP8fFWBQkf50rbvaiTqfhCSd-6D_IMjs5KlHhAS8mmyPSQ_-Mu54uLdt8BrF1XKFKJIvbBNYIbVbPv9M5cMMVMgj5LodNnLKYFzAcHSLweVKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913d736794.mp4?token=dTPm_YpQRUkMbTwS7mH_GPovoB_e56jskGtt-qSy4TCkSq7oozKqqezNjrtAHrwqFWePbDtXZ6JpH6XgqxADAQy4ITu7ypHWEjI25iGanmER4CZRp5-sDB56h_oCgfNdoQXZwxRnwA9xVA_7fQeLSn4sgDXNU1XXyjoFfb3ooMmASX7_LkJrZKkiOzgF_ovg0J8u8WTVIsNHP-0olIwSPiqiXSxoXC7CEHH_XPExpP8fFWBQkf50rbvaiTqfhCSd-6D_IMjs5KlHhAS8mmyPSQ_-Mu54uLdt8BrF1XKFKJIvbBNYIbVbPv9M5cMMVMgj5LodNnLKYFzAcHSLweVKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
درپی حمله به مقرهای تروریست‌ها، ستون‌های دود در سلیمانیه عراق به هوا برخاسته است. @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450568" target="_blank">📅 08:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسداران: مردم حماسه آفرین و شجاع و بصیر ایران اسلامی! در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/450567" target="_blank">📅 08:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=Ml7aGmcpzeyMCM9P2RdnpDOp-NBhYIvYt4bsKR1cn-D-kg2b9pOsWzA8YO4_A3Gmnjf6sH4AEKhdK-ZvZlN0Sg-udkWzO8oSk-BNwU4hVZeYOORTuVryMBN1q1puUPat4vNyYHMtbG1RvWLXPG-_mpaP2AG8ubFGoKvq9PGruedsxLo8mnoVCEBaqb67M-eXUUUGoxuCx2jGZmJWOad7FHoIMxOt9L41GKrgcfvpx7DFzDynXy1SvTGCnGuD0ottsB2ljnIi6r9FkanVG8IqJVLGUrPGIDTi8NTga6Qo_6vV8pT9I_L4Q-fOVTq1zyeje0ibP7KV2fCgVR-jsvih5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=Ml7aGmcpzeyMCM9P2RdnpDOp-NBhYIvYt4bsKR1cn-D-kg2b9pOsWzA8YO4_A3Gmnjf6sH4AEKhdK-ZvZlN0Sg-udkWzO8oSk-BNwU4hVZeYOORTuVryMBN1q1puUPat4vNyYHMtbG1RvWLXPG-_mpaP2AG8ubFGoKvq9PGruedsxLo8mnoVCEBaqb67M-eXUUUGoxuCx2jGZmJWOad7FHoIMxOt9L41GKrgcfvpx7DFzDynXy1SvTGCnGuD0ottsB2ljnIi6r9FkanVG8IqJVLGUrPGIDTi8NTga6Qo_6vV8pT9I_L4Q-fOVTq1zyeje0ibP7KV2fCgVR-jsvih5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
درپی حمله به مقرهای تروریست‌ها، ستون‌های دود در سلیمانیه عراق به هوا برخاسته است.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450565" target="_blank">📅 08:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسداران: مردم حماسه آفرین و شجاع و بصیر ایران اسلامی! در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات نصر ۲، با رمز مبارک یا اباعبد الله الحسین (ع) و تقدیم به سربازان مظلوم شهید بمپور ایرانشهر، با حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه تنف سوریه، علاوه بر انهدام یک سامانه راداری، چند فروند بالگرد خاص عملیات ویژه، در قصاص خون سربازان شهید شب قبل در ایرانشهر، تعداد زیادی از نیروهای جنایتکار آمریکایی را به درک واصل کردند.
🔹
کنترل کامل تنگه هرمز کماکان در اختیار رزمندگان شجاع ماست و تا زمانی که شرارت‌های آمریکا ادامه داشته باشد، یک قطره نفت و گاز از این منطقه صادر نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/450564" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-2EXnSDLz_95Tx6rNurzfRnPWx2tOAcprMzcl1O3kZGk79UI-pCefkc6xVvhQ9uQIE6Obp4WgvbVbS5jhEi8Xa8lwLE0Rf0FD-GK74_WIEGFJHyoqt0VDI6-lb4SRka9M0_KceMbJPlo8djS4KkQNfH9bMv6IlNMUxLLeKipOTZz7DWhu5Q9n9jSTso9jeeA3U5wo7X7p8gaLEvTkT_cQyaroACdW_KpSU2r-igBOPX0h7bewdl013_nX6xV1yRLvt-voGnpdFPW465BBduKk0lqBuGZQzLiFfapD7S9bl7S0Z4NEsowK96JAx--zH63STajwpzgaeDSrcKwDtY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور فینال جام‌جهانی مشخص شد
🔹
فیفا به صورت رسمی اعلام کرد که اسلاوکو وینچیچ، داور سرشناس اهل اسلوونی، قضاوت دیدار فینال جام‌جهانی ۲۰۲۶ را بر عهده خواهد داشت.
🔸
این مسابقه یکشنبه ۲۸ تیر از ساعت ۲۲:۳۰ به وقت ایران در ورزشگاه مت‌لایف نیوجرسی و بین تیم‌های ملی اسپانیا و آرژانتین برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450563" target="_blank">📅 08:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
منابع محلی: پایگاه آمریکایی العدید در قطر مورد حملۀ موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/450562" target="_blank">📅 06:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/450561" target="_blank">📅 06:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZSPfMZk-hS-sneHocA9EaPIhDEo-ECfGBfa8azvkvH9w68nWfaUBhZnb6XfcP5wT3Oz0FXEAgE5nMZqRiYM9guRl-vCnnnwFoXshI8i2wHupe0a3Asr67MXwLHt-36z6AryaTPWd7k2pM5clZ06EAULnppGRRkFYau3j2mgExJG-o7HKKPklEYsJbs1IgHInvUjRtfoMUgE1LeEi50J6_9v5fjrSe3x5JA_RwiJZQShYzXAbgpyvFIB7niNC0DKMdByY7VYbzfS7gx3MbUO1ncKNhr1rCjlTTQKxXKNAxqDSVQJSKD8lWo82Fn9Hdsufc5SViI6lHdntOgKG0Ekvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بالگردهای نظامی آمریکایی، برای رهگیری پهپادهای ایرانی در آسمان بحرین به پرواز درآمدند.  @Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/450560" target="_blank">📅 06:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce75853d5.mp4?token=S13IlpLSHPdqSUhBaSbY3jAwxjNFgzgHqHP8aBvrr2eVZq1MIO-t5BykhUwV1jczp2Y9_j4HoozhQ9Z4h9TV4lGXwcxV0hzrxFsyApYv1w-Ux5OaC8hnrEeLnjo3HBdo_w4Qh_kXr7GwFgbeSGm1r91O2g1GQA64E-bXiKlDymzEGiawdK3VeQ-dDT_8h76vDcBfezyT5Iakgka9-VD0chGTzueSMBpX0YYX1GmhnXlIDPKXay37mZOnoJSkmrdfblxh0jrSEDeq5TbpxTsmdPZNgEvEFbRF_v9ySg6UO8mCVBGcN32-8KZptpVpDFmReYx74w9trcbVXlXHP8_wvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce75853d5.mp4?token=S13IlpLSHPdqSUhBaSbY3jAwxjNFgzgHqHP8aBvrr2eVZq1MIO-t5BykhUwV1jczp2Y9_j4HoozhQ9Z4h9TV4lGXwcxV0hzrxFsyApYv1w-Ux5OaC8hnrEeLnjo3HBdo_w4Qh_kXr7GwFgbeSGm1r91O2g1GQA64E-bXiKlDymzEGiawdK3VeQ-dDT_8h76vDcBfezyT5Iakgka9-VD0chGTzueSMBpX0YYX1GmhnXlIDPKXay37mZOnoJSkmrdfblxh0jrSEDeq5TbpxTsmdPZNgEvEFbRF_v9ySg6UO8mCVBGcN32-8KZptpVpDFmReYx74w9trcbVXlXHP8_wvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/450559" target="_blank">📅 06:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=p_aM1hcoHHUjF0A4km4PbsCdzSXLns4vfA-wqM_VLumlHGYEpZwj5tc1YLESjKjp1sGX_vv7LAjqL-jyYX5jKLhUcAAkOZPMS8oAQUWOESPTURun-4Zi85k7RqJd-Ru5uQMcDxl3hZw2zNlE_GBK-lWFBXtBy9BvByoihwHhnknLQxiYcSuk5CybhuPWcReuulaUQDUIPJ4EGHHc5vt67V9y54Lp2hXKLt1mLtV2BaVjRz5RpSkmGPFCZKg4lwTSIij6BYYQPtGGGy1ymnInOb2CSNcqhp_zJYveHbblhEq5R32qRyL4zGNrJnRGlqwuZAvdOLshqmPaX4dvco7zkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=p_aM1hcoHHUjF0A4km4PbsCdzSXLns4vfA-wqM_VLumlHGYEpZwj5tc1YLESjKjp1sGX_vv7LAjqL-jyYX5jKLhUcAAkOZPMS8oAQUWOESPTURun-4Zi85k7RqJd-Ru5uQMcDxl3hZw2zNlE_GBK-lWFBXtBy9BvByoihwHhnknLQxiYcSuk5CybhuPWcReuulaUQDUIPJ4EGHHc5vt67V9y54Lp2hXKLt1mLtV2BaVjRz5RpSkmGPFCZKg4lwTSIij6BYYQPtGGGy1ymnInOb2CSNcqhp_zJYveHbblhEq5R32qRyL4zGNrJnRGlqwuZAvdOLshqmPaX4dvco7zkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرحلهٔ یازدهم عملیات صاعقهٔ ارتش؛ مراکز و پایگاه‌های آمریکا در بحرین آماج حملات پهپادی
🔹
​در پاسخ به اقدام خصمانهٔ دشمن در هدف‌قراردادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحلهٔ یازدهم عملیات صاعقه، محل استقرار بالگردها…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/450558" target="_blank">📅 06:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/450557" target="_blank">📅 06:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
حملۀ پهپادی به پایگاه آمریکایی در اربیل عراق
🔹
رسانه‌های عراقی از هدف قرارگرفتن مقر نیروهای آمریکایی در نزدیکی فرودگاه اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450556" target="_blank">📅 06:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ شمار شهدای حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔹
دانشگاه علوم پزشکی هرمزگان: براساس آخرین اطلاعات دریافتی، شمار شهدای حمله به پل‌های بندر خمیر به هفت نفر افزایش یافته است.
🔹
همچنین در این حمله ۹ نفر مجروح شدند که روند رسیدگی درمانی به مصدومان…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/450555" target="_blank">📅 05:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
سومین حملۀ موشکی آمریکا به برج مراقبت دریایی چابهار
🔹
دقایقی پیش مردم چابهار صدای چند انفجار از این شهر شنیدند.
🔹
بر اساس اخبار اولیه این‌بار نیز دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفتۀ گذشته مورد حملۀ موشکی خود قرار داده است.
🔸
برج مراقبت دریایی چابهار از جمله زیرساخت‌های غیرنظامی حوزه دریایی به شمار می‌رود و نقش مهمی در هدایت ایمن ترددهای دریایی، پایش محدوده بندری و هماهنگی عملیات امداد و نجات ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/450552" target="_blank">📅 05:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در بحرین
🔹
منابع خبری از فعال شدن آژیرهای هشدار در بحرین خبر می‌دهند.   @Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/450551" target="_blank">📅 04:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌ شمار شهدای حمله به پل‌های بندر خمیر به ۳ نفر افزایش یافت
🔹
استانداری هرمزگان: شمار شهدای حمله به پل‌های بندر خمیر به سه نفر افزایش یافته است.
🔹
همچنین در این حمله ۹ نفر مجروح شدند که روند رسیدگی درمانی به مصدومان از سوی نیروهای امدادی و کادر درمان در حال…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farsna/450550" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجار در پایگاه آمریکایی العدید قطر گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farsna/450549" target="_blank">📅 04:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
گزارش حادثه در پل بحرین-عربستان
🔹
صابرین‌نیوز: صدای آژیر آمبولانس‌ها و ماشین‌های آتش‌نشانی که به‌سمت پل متصل‌کنندۀ بحرین و عربستان سعودی در حرکت هستند، به گوش می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farsna/450548" target="_blank">📅 03:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/450547" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کویت: در حال مقابله با حملات پهپادی و موشکی هستیم
🔹
ارتش کویت اعلام کرده پدافند هوایی این کشور در حال تلاش برای مقابله با حملات موشکی و پهپادی از سوی ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farsna/450546" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ادعای مقام آمریکایی دربارۀ هدف از حمله به پل‌ها در ایران
🔹
یک مقام آمریکایی در گفت‌وگو با روزنامه وال‌استریت‌ژورنال گفت، حمله به پل‌ها با هدف قطع تدارکات به بندرعباس انجام شده است که ایران از آن برای حمله به کشتی‌ها استفاده می‌کند.
🔸
بسیاری از کاربران در فضای مجازی اقدام آمریکا در حمله به زیرساخت‌های ایران را مصداق جنایت جنگی توصیف کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/450545" target="_blank">📅 03:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450544">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در بحرین
🔹
منابع خبری از فعال شدن آژیرهای هشدار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/450544" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
جزئیات حملۀ دشمن آمریکایی به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل گریوه نیز در محورهای ارتباطی استان، مورد اصابت قرار گرفته است.…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/450543" target="_blank">📅 02:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
رادارها و سکوهای پرتاب موشک آمریکا در کویت به آتش کشیده شدند  @Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450542" target="_blank">📅 02:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61309d075.mp4?token=gO_bFqT4JjisiqgtI3p38WlWvNza6h6YSzj0Nmqo691qU2l5gGjEbeAKGQvvoKVlLlFz_a56zltcoNUxtPdrR2YVPm5Gk8dIuJhVfVCX8zNP8AMaULsEEO-tMQqhdV16Eo8BF6K0hX2L6AZRqkZ1FcVL052WpT3HbwRWu2EgEOV-rnSzaE-MnnzOAFmNZAQ3RzLIDcn1qjHaCvfsQEc_qrtKHcd8uZra_UC_3S0kmNwQZs2iQE0FaqWdHnEC5ZgVtKatwmBA3E1kwLXZ9-3qJcCOq_2y4m6v1DDGhFJ7_VeMEQey0PeTbar3ReRVBny4QBpsWgmMDwbOJ_t9nYGPUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61309d075.mp4?token=gO_bFqT4JjisiqgtI3p38WlWvNza6h6YSzj0Nmqo691qU2l5gGjEbeAKGQvvoKVlLlFz_a56zltcoNUxtPdrR2YVPm5Gk8dIuJhVfVCX8zNP8AMaULsEEO-tMQqhdV16Eo8BF6K0hX2L6AZRqkZ1FcVL052WpT3HbwRWu2EgEOV-rnSzaE-MnnzOAFmNZAQ3RzLIDcn1qjHaCvfsQEc_qrtKHcd8uZra_UC_3S0kmNwQZs2iQE0FaqWdHnEC5ZgVtKatwmBA3E1kwLXZ9-3qJcCOq_2y4m6v1DDGhFJ7_VeMEQey0PeTbar3ReRVBny4QBpsWgmMDwbOJ_t9nYGPUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرحلهٔ یازدهم عملیات صاعقهٔ ارتش؛ مراکز و پایگاه‌های آمریکا در بحرین آماج حملات پهپادی
🔹
​در پاسخ به اقدام خصمانهٔ دشمن در هدف‌قراردادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحلهٔ یازدهم عملیات صاعقه، محل استقرار بالگردها و هواپیماهای شناسایی P8 ارتش تروریستی آمریکا در پایگاه الصخیر بحرین را هدف حملات پهپادهای انهدامی آرش قرار داد.
🔹
​ارتش با تأکید بر اینکه امنیت و استقلال این میهن خدایی خط قرمز ماست و متناسب با شرارت‌های دشمن خبیث، سریع و قاطع پاسخ خواهیم داد، خاطرنشان کرد: هرگونه خطای محاسباتی در برآورد اراده و استقامت ملت و توان رزم ارتش و سپاه ایران، هزینه‌ای سنگین برای دشمن مستکبر خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/450541" target="_blank">📅 02:34 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
