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
<img src="https://cdn4.telesco.pe/file/edHwB3Tg161wjMCQG7ePdnsXc2Z6NyfSrKNlpYg-SzjP0Cgot7dwF4Yij4Tv6P-9fLaXrVgRhVLvqTOWS2V2oOv0uVHRPMF-jT2c_o2zPhhYg3gfAANjNfTdwiIOdBTCSr5QWfK3TAyYUIRkhSgg9aCCnVrXhIIuvBc8BM_0lYxxW1BXs1RUucr7bJCJve7aqktPaveTkNY3lFBWTiQE_U08iZ0R5UzF_MbOpKPLNLmL1uolgpNECjbEKB5wznPDf5sXJoVh-qdWWLYNJTeuMHqzKlxevTdUXYHGBo7Z4bS6BX7_kLjFmtsrJ2OOUXdURgNyVuC1uQlNVyJAGrf4wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-670467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب بقایی به اظهارات وزیر امور خارجه فرانسه درباره ایران
🔹
وزیر امور خارجه فرانسه دوست دارند هر از چندگاهی صبحتش در نشست سخنگویی انجام شود.
🔹
فرانسوی ها باید یاد بگیرند درباره مسائلی که به آنها مربوط نمی شود انتظار نقش آفرینی نداشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/670467" target="_blank">📅 11:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امورخارجه به ادعای ترامپ درباره درخواست ایران برای مذاکرات؛ طرف آمریکایی صادق نیست و یک بازی روانی است
بقایی:
🔹
ایران با میانجی‌ها در تماس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/670466" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نیوزویک: ایران ترور ترامپ را برون‌سپاری می‌کند!
ادعای نیوزویک:
🔹
تلاش‌های ایران برای ترور در خاک ایالات متحده معمولاً شامل برون‌سپاری واسطه‌ها می‌شود.
🔹
تهران به جای استفاده از عوامل آموزش‌دیده خود برای حمله، از منابع خارجی استفاده می‌کند و واسطه‌هایی را برای استخدام شبکه‌های جنایی محلی یا افراد مسلح اجیر شده می‌فرستد که امکان انکار را فراهم می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/670465" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پاریس: تحریم‌های ایران لغو نمی‌شوند
وزیر امور خارجه فرانسه:
🔹
تا زمانی که ایران برنامه هسته‌ای خود را کنار نگذارد، هیچکدام از تحریم‌ها لغو نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/670464" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63119fd6fe.mp4?token=bIHn42vqQ35n5BGmoxsPVuhRuIHdaUeXUXG6ReDO6tXYazBAI0qJEKEeOns_h06r__XggHtRj2DSbgSirhIw5daRPCHW24lhLb2Vn9HEhvcq2xnc-LhACHWcCb7MW1mPspwHj50mL7q-yF2RKVnHqxgis3FOEGNcyFoIYVoi72imJ5lkk6TRcXAhrnV6iXCpJrJhnnBgvb0wLatUSOELUdxwuHXv6Gx8LGPXLHYbd3q0G9N-qNBhiY4VCCn5su2ENkl2CxpyVCK-46u6UzwN9NJ9U-typXw7aWqkYv33ee_43q8SptB9pO4MoB20PHZPUJg0dgPswQfk80LYp1gsCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63119fd6fe.mp4?token=bIHn42vqQ35n5BGmoxsPVuhRuIHdaUeXUXG6ReDO6tXYazBAI0qJEKEeOns_h06r__XggHtRj2DSbgSirhIw5daRPCHW24lhLb2Vn9HEhvcq2xnc-LhACHWcCb7MW1mPspwHj50mL7q-yF2RKVnHqxgis3FOEGNcyFoIYVoi72imJ5lkk6TRcXAhrnV6iXCpJrJhnnBgvb0wLatUSOELUdxwuHXv6Gx8LGPXLHYbd3q0G9N-qNBhiY4VCCn5su2ENkl2CxpyVCK-46u6UzwN9NJ9U-typXw7aWqkYv33ee_43q8SptB9pO4MoB20PHZPUJg0dgPswQfk80LYp1gsCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: مردم ایران تجربه تلخی از پیمان شکنی آمریکا دارند و برای ما دیپلماسی یک ابزار است و مردم ایران حامی تصمیم گیرانشان هستند؛ شیوه و کیفیت مذاکرات دیدگاه طبیعتا متفاوت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/670463" target="_blank">📅 11:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a156e3c05e.mp4?token=H62ll9GY8YMkZuZ1Drbo5OhRE1bgwb38b-4bEuqUmAfqrQsZ6Ih2Fan8rCAMyICkDvw0yrHKZmeC1wSK9uHhDEPdyimVx263SBjUeZZU-wM3du20HpT5kiMQn94KE8rHtcAxv42vY845-byNU2Le70BntqreZmqV27NIyIyVBubUbl5mXwGwLLZ07m9QZ0NgJ-aPC4jmWpsfLyKdwilXstZ0MMmJhYz9A_7Kw5ySpcWZbJJQxkDX5uWqRDCk1qNfUZzojyyKeLQs0FQkOhNn-y6WN67M7R71kP8hgFx2UwZ4L3XxOCUJl8rcxV3lrw-ze4Jn9UruFEC6kveGYeTfzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a156e3c05e.mp4?token=H62ll9GY8YMkZuZ1Drbo5OhRE1bgwb38b-4bEuqUmAfqrQsZ6Ih2Fan8rCAMyICkDvw0yrHKZmeC1wSK9uHhDEPdyimVx263SBjUeZZU-wM3du20HpT5kiMQn94KE8rHtcAxv42vY845-byNU2Le70BntqreZmqV27NIyIyVBubUbl5mXwGwLLZ07m9QZ0NgJ-aPC4jmWpsfLyKdwilXstZ0MMmJhYz9A_7Kw5ySpcWZbJJQxkDX5uWqRDCk1qNfUZzojyyKeLQs0FQkOhNn-y6WN67M7R71kP8hgFx2UwZ4L3XxOCUJl8rcxV3lrw-ze4Jn9UruFEC6kveGYeTfzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: اروپایی‌ها نباید رویکرد مهدکودکی خودشان را به دیگران تسری بدهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/670462" target="_blank">📅 11:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◼️
بدرقه یار
◾️
پیام‌های صوتی مخاطبان خبرفوری در پویش «بدرقه یار»، آخرین جمله به رهبر شهید؛ بازتابی از ارادت، دلتنگی و وفاداری مردمی است که حرف دل خود را با رهبر شهید در میان گذاشته‌اند.
◾️
این صداها، بخشی از بدرقه ماندگار ملتی است که در سوگ، همدل و در وفاداری، هم‌پیمان مانده‌اند.
◾️
کانال رسمی سوگواره «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/670461" target="_blank">📅 11:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ منفی سخنگوی وزارت امورخارجه به ادعای گروسی مبنی اجازه ایران به آژانس برای دسترسی به تاسیسات هسته‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/670460" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20484bc0ab.mp4?token=FjlTwPADFDu34BPCcZbP6-EqT6ygIdYGkkcnMGL-OKgLfh3dnHHL4LWfMYspnzETYMk6UOWBvBNXeDuPNbZsWsbrcUCvwan4Jp10fAdrOABLK1wFgWV3kJmAopjMSHwu2jilT9NfHpGhXCsRYyZ5lSOj1lrVUtTcnR3xJ1tyd4dCsf2LmoFuOawBtuQGdSdYBLEAKDAGcdxov74mKgsyuIA2qAT0U7FATLroasoebmqj0A9KaWUyNKaG2vJIOcRf5AKDH5oyMGoBdUg2Oa9I9Us_K6BUt-RK-3Mc7f-JnJl4vORz-XylFk12oSlF6qbmvuDdvyMZLUKU4l5AFOrGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20484bc0ab.mp4?token=FjlTwPADFDu34BPCcZbP6-EqT6ygIdYGkkcnMGL-OKgLfh3dnHHL4LWfMYspnzETYMk6UOWBvBNXeDuPNbZsWsbrcUCvwan4Jp10fAdrOABLK1wFgWV3kJmAopjMSHwu2jilT9NfHpGhXCsRYyZ5lSOj1lrVUtTcnR3xJ1tyd4dCsf2LmoFuOawBtuQGdSdYBLEAKDAGcdxov74mKgsyuIA2qAT0U7FATLroasoebmqj0A9KaWUyNKaG2vJIOcRf5AKDH5oyMGoBdUg2Oa9I9Us_K6BUt-RK-3Mc7f-JnJl4vORz-XylFk12oSlF6qbmvuDdvyMZLUKU4l5AFOrGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بقایی به مرگ لیندسی گراهام سناتور ضد ایرانی
سخنگوی وزارت خارجه:
🔹
خوشبختانه حضرت عزرائیل عادل است قرار نیست مردم برای لیندسی گراهام نماز وحشت بخوانند؛ مردن این سناتور تندخو و جنگ دل هیچ آزاده ای را آزرده نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/670459" target="_blank">📅 11:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7c0e8dc3.mp4?token=MZgR6VhijeyWKLN_bNYOB7bVJjc2cZkaxvXCPSEiqgMchaOxh-3p8Rec9uLeMRt0YxKTmBohtOKGerXt0IfzBb5yHyUHPlzKy_rXPAHjFwIU_0xwfcwbsjaKT21F4Cz9faxfMAqpT_5DbcBLHiqQs5dBwkdnc-SdRNETTSqoZ59nL2v5BnbKZcdeXLQDPMn0sANNFG5J1ZmPaNURuS5YFEZoOJCaoGzHH4a-MrXWzpqIx2SbmO6TLJSPVmNc-WFw1AyJIAwIJOS9SE2d9hkfZZXtDFK_2N2R8qu8O1BCTyAVAkVjCM1_hgn9vKPzc1kof0yVTzClQrIUp6Ap5R8mTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7c0e8dc3.mp4?token=MZgR6VhijeyWKLN_bNYOB7bVJjc2cZkaxvXCPSEiqgMchaOxh-3p8Rec9uLeMRt0YxKTmBohtOKGerXt0IfzBb5yHyUHPlzKy_rXPAHjFwIU_0xwfcwbsjaKT21F4Cz9faxfMAqpT_5DbcBLHiqQs5dBwkdnc-SdRNETTSqoZ59nL2v5BnbKZcdeXLQDPMn0sANNFG5J1ZmPaNURuS5YFEZoOJCaoGzHH4a-MrXWzpqIx2SbmO6TLJSPVmNc-WFw1AyJIAwIJOS9SE2d9hkfZZXtDFK_2N2R8qu8O1BCTyAVAkVjCM1_hgn9vKPzc1kof0yVTzClQrIUp6Ap5R8mTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: کشورهای منطقه از وضعیت ۴ ماه گذشته که به‌دلیل حضور آمریکا به چالش کشیده شده، درس بگیرند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/670458" target="_blank">📅 11:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران دولت فعلی افغانستان را به رسمیت شناخته است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/670457" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هیچکدام از پایگاه‌های آمریکا در هیچ کشوری از منطقه از بانک اهداف ما خارج نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670456" target="_blank">📅 11:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6accc4e75b.mp4?token=kk5zFK1CGZGyz1pC-5y7PFreSLhz8t9bOw5WaFGonTmeRemiqdNwJ4fXCwnFjYmjDKvQhBtiDbUJLI4a_FKdvrEc2BYWW4KTDk33svQg9h9ooa-7TEp9SvqEsmz3jc2RRgFDwJ9cxN_lOWC_F8ztCEFMCDhoDvhYSQ3arlLdU3lP8QIDXmGcfmK2QagJ5VcTwKmibNzjJU10I9xW9X5tU1YivYETrr8vjukqEwNNNsv67vLyeWGnMbgM7nJChhzsrqc9iTBhU7wc2WICqiIUfwEr93I_1RxkqocEtQ_JkVI2rq-R0KfgwbY1_UEFmicXINYhew5eB4GbFIodrsxaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6accc4e75b.mp4?token=kk5zFK1CGZGyz1pC-5y7PFreSLhz8t9bOw5WaFGonTmeRemiqdNwJ4fXCwnFjYmjDKvQhBtiDbUJLI4a_FKdvrEc2BYWW4KTDk33svQg9h9ooa-7TEp9SvqEsmz3jc2RRgFDwJ9cxN_lOWC_F8ztCEFMCDhoDvhYSQ3arlLdU3lP8QIDXmGcfmK2QagJ5VcTwKmibNzjJU10I9xW9X5tU1YivYETrr8vjukqEwNNNsv67vLyeWGnMbgM7nJChhzsrqc9iTBhU7wc2WICqiIUfwEr93I_1RxkqocEtQ_JkVI2rq-R0KfgwbY1_UEFmicXINYhew5eB4GbFIodrsxaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مقایسهٔ ایران و رژیم صهیونیستی توسط وزیر خارجهٔ ترکیه حیرت‌آور است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670455" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: آمریکایی‌ها از روز اول تقلب کردند
سخنگوی وزارت امور خارجه:
🔹
آمریکا با تحریک کشورهای منطقه سعی کردند مسیر امن تنگه هرمز را دور بزنند و بند ۵ یادداشت تفاهم را نقض کردند و امنیت کشتیرانی را در منطقه به خطر انداختند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670454" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4f1fe902.mp4?token=I9S-u8hGaQNfCvv5JhLA17QPSsw1NSDfl7odTK2ptsDzpwlVH4MZIBQwaLKF8dKxidUq3BVTF2ZnjKiBKGomElEb6PnIccSX7egOX0rNrcXLpwL5DdOeMW9LRoDssMDns5RKAh2xyyEaaFNVecGmhGVVVRt89xNWCwqslOMjAfKXZwgoucP60xqhSRBuvbdVwTpOkxJIWtA19LUeluLZNBvqfgQx5BZRRWeCx6c66SSrnw238yWLMp8mDe_c4Rda1qDjbAzHe9WJEYTFj5DcnBQ7pVOipBGRvUGFI0rkPycZ42aRYhU9KxbxSUtw4yKK8p5yttQZpz1t2Y0-eGEucA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4f1fe902.mp4?token=I9S-u8hGaQNfCvv5JhLA17QPSsw1NSDfl7odTK2ptsDzpwlVH4MZIBQwaLKF8dKxidUq3BVTF2ZnjKiBKGomElEb6PnIccSX7egOX0rNrcXLpwL5DdOeMW9LRoDssMDns5RKAh2xyyEaaFNVecGmhGVVVRt89xNWCwqslOMjAfKXZwgoucP60xqhSRBuvbdVwTpOkxJIWtA19LUeluLZNBvqfgQx5BZRRWeCx6c66SSrnw238yWLMp8mDe_c4Rda1qDjbAzHe9WJEYTFj5DcnBQ7pVOipBGRvUGFI0rkPycZ42aRYhU9KxbxSUtw4yKK8p5yttQZpz1t2Y0-eGEucA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امور خارجه به بیانیه کشورهای اروپایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/670452" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4852a538d3.mp4?token=HOjsbTc4bYjohD-QMhG-q6h9TtYr4Nyhh21EgvdiYeBU7ctiF6rjr2JTa3Wo0CSYK2M9BQDQTvKgKV9E0vNJY_8Qa2QMg46JLDXBR5MxqBHUKtq16B60UkCXstWWIOJU7s3zg68f8YcJKHScprvks2YGE5KSuIvts_NmRot1yVY7q-U9osJ5bh6fdkCQ9-zpLsZY57v4Vk15A0rZjw1tHclMOMj9XUpt5n-KLPZ8cgzY3FdnyXRjg8Ju2p9OXIfCyOKyrsl5EZSRjAuKVvQl_pOlLqzKHqkTuQJgzw0maIsNfNvK7pTCdm4Tkg9LMikcbfhQfGEAN9uaJmUcJcafTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4852a538d3.mp4?token=HOjsbTc4bYjohD-QMhG-q6h9TtYr4Nyhh21EgvdiYeBU7ctiF6rjr2JTa3Wo0CSYK2M9BQDQTvKgKV9E0vNJY_8Qa2QMg46JLDXBR5MxqBHUKtq16B60UkCXstWWIOJU7s3zg68f8YcJKHScprvks2YGE5KSuIvts_NmRot1yVY7q-U9osJ5bh6fdkCQ9-zpLsZY57v4Vk15A0rZjw1tHclMOMj9XUpt5n-KLPZ8cgzY3FdnyXRjg8Ju2p9OXIfCyOKyrsl5EZSRjAuKVvQl_pOlLqzKHqkTuQJgzw0maIsNfNvK7pTCdm4Tkg9LMikcbfhQfGEAN9uaJmUcJcafTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/670451" target="_blank">📅 11:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده تفاهم صلح اسلام آباد چه خواهد شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/670450" target="_blank">📅 11:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: بی‌تردید تفاهم‌نامه وارد مرحلهٔ بحران شده
🔹
آمریکایی‌ها در پیمان‌شکنی این‌قدر کم‌صبر بودند که حتی اجازه ندادند بازهٔ یک‌ماههٔ تعهدات ایران دربارهٔ تنگهٔ هرمز تمام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/670449" target="_blank">📅 10:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: خون‌خواهی رهبر شهید ایران یک مطالبه است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/670448" target="_blank">📅 10:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0592b8dd56.mp4?token=PAL5C8rJ-oncD21EV0fxb-WHbPB4z9VXM1FzIFuLLv872x2r45rl9nanJcZcOtycBXqv144ojSacbkP2CLqoIKEqYDj6hqrhoUIBhSr1HW_jCYMTPHEy3LXgxgAmanvv3xzD6X7IrVHRGfiSkvWi_dZuTCcn0A6cA4ywxMWJla1DZAq6w7-aSky2e3LaZHBrlFqlB8yNuDSuPPUCKtfOoJQRZ_EFumqEttDig9PRWJqBXkAmWsmjVQAHPG8TAbOvbnVV-RwfXXIOT7tK9aWMOyN_IkWTQ4EPS2yiw4hiDzOd7EhhBhg4TkYSEAk9VD8PhEP4FDyDlGspOZEoMfHrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0592b8dd56.mp4?token=PAL5C8rJ-oncD21EV0fxb-WHbPB4z9VXM1FzIFuLLv872x2r45rl9nanJcZcOtycBXqv144ojSacbkP2CLqoIKEqYDj6hqrhoUIBhSr1HW_jCYMTPHEy3LXgxgAmanvv3xzD6X7IrVHRGfiSkvWi_dZuTCcn0A6cA4ywxMWJla1DZAq6w7-aSky2e3LaZHBrlFqlB8yNuDSuPPUCKtfOoJQRZ_EFumqEttDig9PRWJqBXkAmWsmjVQAHPG8TAbOvbnVV-RwfXXIOT7tK9aWMOyN_IkWTQ4EPS2yiw4hiDzOd7EhhBhg4TkYSEAk9VD8PhEP4FDyDlGspOZEoMfHrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: ایران جهانی را به تماشای وفاداری ملتی نشاند که داغ‌ترین داغ نیز زانوانش را خم نمی‌کند
🔹
آنچه جهان دید خروش نوری بود که از دل میلیون ها انسان برخاست و از تهران تا قم از مشهد تا نجف و کربلا امتداد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670447" target="_blank">📅 10:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
هیچ تغییری در نحوه برگزاری آزمون‌های دانشگاهی ایجاد نشده است
سیمایی صراف وزیر علوم:
🔹
آزمون‌های تحصیلات تکمیلی حضوری، کارشناسی غیرحضوری و کنکور سراسری اواخر مرداد برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/670446" target="_blank">📅 10:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌ان‌ان: هزینه هر واحد از پهپادهای انتحاری دریایی که آمریکا در حملات اخیر خود به ایران برای نخستین‌بار استفاده کرد بیش از ۲ میلیون دلار برآورد می‌شود
‏
🔹
سنتکام همچنین از پهپادهای هوایی «لوکاس» استفاده کرده که نسخه‌ای الگوبرداری‌شده از پهپادهای شاهد ۱۳۶ ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/670445" target="_blank">📅 10:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت رژیم صهیونیستی پس از به درک واصل شدن لیندسی گراهام
باید بسیار نگران بود، ایران از اجرای سیاست «چشم در برابر چشم» سخن می‌گوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/670444" target="_blank">📅 10:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تروئیکای اروپا باز هم طلبکار ایران شد
🔹
به رغم نقض مکرر تعهدات آمریکا در تفاهم‌نامه اسلام‌آباد، وزرای خارجه انگلیس، فرانسه و آلمان با انتشار بیانیه مشترک «حملات بی‌ملاحظه ایران» در تنگه هرمز را محکوم کردند. در بیانیه تروئیکای اروپایی آمده است:
🔹
«ما حملات…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/670443" target="_blank">📅 10:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تروئیکای اروپا باز هم طلبکار ایران شد
🔹
به رغم نقض مکرر تعهدات آمریکا در تفاهم‌نامه اسلام‌آباد، وزرای خارجه انگلیس، فرانسه و آلمان با انتشار بیانیه مشترک «حملات بی‌ملاحظه ایران» در تنگه هرمز را محکوم کردند.
در بیانیه تروئیکای اروپایی آمده است:
🔹
«ما حملات بی‌ملاحظه ایران به کشتی‌های تجاری در تنگه هرمز و کشورهای منطقه از جمله قطر، کویت، بحرین، عمان و اردن را محکوم می‌کنیم.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/670442" target="_blank">📅 10:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرغ رو به این روش درست کن
😁
مواد لازم:
🔹
ران مرغ: ۴عدد
🔹
رب گوجه: ۲قاشق غذاخوری
🔹
فلفل دلمه ای: ۱عدد
🔹
پیاز: ۱ عدد
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/670441" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارهای مهیب اردن را لرزاند
🔹
منابع نظامی اردن امروز دوشنبه از وقوع چند انفجار مهیب در مناطق مختلف این کشور خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670440" target="_blank">📅 10:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دولت مرز ایران-ترکیه را برای واردات خودرو باز کرد
🔹
احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
الزیدی، نخست وزیر عراق طی سفری رسمی و در راس یک هیئت بلندپایه عازم آمریکا شد.
🔹
تعداد قربانیان زمین‌لرزه‌های ونزوئلا به ۴۴۹۰ نفر افزایش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/670439" target="_blank">📅 10:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV7xK79ZQ6Ggh7j1IkBadzVY8xzYiiXXA9uNBfi6rUHlsfkO_5rzZoYJ8waGjXKH1y5EOdcLKJySVgd-JWmBWtceGNhik0htBsTPBn3r8H8yOwSZtQSz22KdEm3i8oe8UxYblHsLwWkk02UIocVS2SoKRG5CJ_AgDeMJrvm5N5W-wmDfOhBwO3e2LwDx2S5ADoptbu0fGq1YtPzGzh85c7PcO9KbONn3rBSwt3h7M21I7Z7zKGdlHCS8fIrLE_5yQQNHWydDKgCn_4izgSqp839-MwRzhLExaseQCX0OaLzMWoLc6TtMoG4NZMi3-b9SbEXm4NN8OwUgePoMhSI-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارت عملیات موشکی سپاه در پایگاه آمریکایی العدید قطر
🔹
در تصویر فوق اصابت دقیق به یک سوله تعمیرات تجهیزات آمریکایی در این پایگاه بخوبی قابل مشاهده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/670438" target="_blank">📅 10:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erLJIi7Icin3goC9Bp7SV3UZCYeEveklJFV27KpVde7z5w_L9jCGW6V_2NQkDAGV5UqS5rMym6rATc24r-QqLzioG4hIC8IYiMrINIPLlZmopkFlw-t-eq6UNYut7-Sd7g8IUBgKMHa0qMrWsdZ4kyTfWmFO9pL_MNGzk7l2cczEEM1UByAp40gsTT7F-fSnKIg438F-hkC2fP8_N0n9hO3Dui9IcaraNfECcGPscJCaNevDQPs44sS3sVFyi9zThd_34gJHZikvL39aDaXzwGcX8IonRICVTMtlEGLC4OahkSH9ZEmG7AS0jqU0iOojGy9M7j_i6SG-_BSmIEK20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس کانال ۵ میلیون واحد را از دست داد
🔹
شاخص کل بورس تهران ۱۱۴ هزار واحد منفی شد و به تراز ۴ میلیون و ۹۴۰ هزار واحد برگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/670437" target="_blank">📅 09:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYvXyhQSO4inE2duA1Xf_hyzXQXlBhPJNgLknXWV9s1P-WyL-H-VGUyZH4PL0b1dyNx22hW0Tblin5aLjpQsh5v1U2cAs3rzvcm6wZmz0Fvp461-8mZ9KUPz5-RXo-Rp-pmga7WcpsTrtatJFKeqgPh4rxw2LQl4tsteDMxEbQL8la7-KcGchVT-Hy2y4NnKpEQC7RoPW6B4UU_g7euCOA6e_Xwdx-K6HpdjFDOp-AC3y-L8wxgc2Qb8nTwMx3MZdBds8c5ZOrCvIOuszS1rLmmWBYNPV-UAAzXOx4VWBDwLCuDj7TifBREBKu7gW7f56eYixfAxyBhtQ2PsvtSE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه‌های رنگی در مسیر زنجان_ میانه معروف به آلاداغلار
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/670436" target="_blank">📅 09:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
معاریو: آمریکا نگران واکنش شدید ایران است
روزنامه صهیونیستی «معاریو»:
🔹
آمریکا در عملیات‌های اخیر خود، از هدف قرار دادن مراکزی که ممکن است ایران را به واکنشی شدید و خارج از چارچوب درگیری‌های کنونی وادار کند، خودداری کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/670435" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز خاموشی‌های برنامه‌ریزی شده در کشور/ نیروگاه‌ها و شبکه برق با حداکثر ظرفیت در حال فعالیت هستند
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
🔹
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/670434" target="_blank">📅 09:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11a1b382df.mp4?token=el9a-G1Km33JidiBLPXo_YpQEyFdZaAVFWjyQZbLWOkW5HUbun5W9OFo_fKkNQzNb96soMGCE4jqJDKvtl5Zz5jRa3t0sDsMJc6lGT-RHxxhX9mbvf2GgdfsajMgt9KLMlTF3ixvOJZM3ZtRamxubprLTLPlUvr5a-NmwLey-mFMWLjbNR_OBBX8Tm18NOr2J6tt7EO9K1HOgxIBQKikSgcgQZimM6SWs0boAaTLrBbA9NASy74HoVuZGypjLMMu_8OAVxxtqd836VNQZkFZRerQv0L1Of4EM3poMCR5Q4QESDCBeA_ZFztkTx7xOdMY3HkreJu5QreDKFko5UFIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11a1b382df.mp4?token=el9a-G1Km33JidiBLPXo_YpQEyFdZaAVFWjyQZbLWOkW5HUbun5W9OFo_fKkNQzNb96soMGCE4jqJDKvtl5Zz5jRa3t0sDsMJc6lGT-RHxxhX9mbvf2GgdfsajMgt9KLMlTF3ixvOJZM3ZtRamxubprLTLPlUvr5a-NmwLey-mFMWLjbNR_OBBX8Tm18NOr2J6tt7EO9K1HOgxIBQKikSgcgQZimM6SWs0boAaTLrBbA9NASy74HoVuZGypjLMMu_8OAVxxtqd836VNQZkFZRerQv0L1Of4EM3poMCR5Q4QESDCBeA_ZFztkTx7xOdMY3HkreJu5QreDKFko5UFIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای شاهد در حال حرکت به سمت منافع و پایگاه‌های آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/670431" target="_blank">📅 09:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
‌ وزارت کشور بحرین از به‌‌صدادرآمدن آژیرهای خطر در این کشور خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/670430" target="_blank">📅 09:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
داده‌های شرکت کپلر: روز یکشنبه تنها ۶ کشتی از تنگه هرمز عبور کردند
🔹
الزام بیمه و ثبت‌نام در سامانه «سماح» برای حضور در مراسم اربعین
🔹
اولیانوف: هرگونه حمله به نیروگاه بوشهر باید متوقف شود
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/670429" target="_blank">📅 09:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ7WrVruh94rHH-XBaGCo4VSlju2zDkXJYeT4ggsKAi8i8vv1dl82jpv93_ZpWHbfj_VWst_YQm4XQ0BkcUySf06fywIqTBnW0zdii7luSQYvpJAT3qxbBS4yqejUN9boEHA0a4cpVnyOO2Hbl2qMg_d33bT8Ebm4hQRXK4rv5r9eW3tW7Scf0muU4GdaPRc5lvtM7vFAjPCX6O7T0u1Bw4phK_cJbAO6Ha-qHJbcr3gXurGm6vYXVhcCJOdL_4fxmGpTX6841IkX12etAC_0LOaqYlyKxWXRBWiTML1jgqGXFD5B3m03giXbq0GaHwdpbKEWBrJsldQVRIZBJ9Y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقال سهمیهٔ سوخت به کارت بانکی کلید خورد
🔹
براساس مصوبهٔ جدید هیئت وزیران، وزارت نفت و بانک مرکزی و وزارت ارتباطات مکلف شده‌اند که زیرساخت‌های لازم برای انتقال سهمیهٔ سوخت از کارت هوشمند سوخت به کارت بانکی را ایجاد و بهره‌برداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/670428" target="_blank">📅 09:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حمله به ۸ نقطه خوزستان؛ شهادت یک نگهبان
🔹
معاون استاندار خوزستان اعلام کرد بامداد دوشنبه، نقاطی در اهواز، بهبهان، دزفول، امیدیه، ماهشهر، اندیمشک، آبادان و شادگان هدف اصابت پرتابه قرار گرفتند.
🔹
در حمله به ایستگاه پمپاژ آب کشاورزی ماهشهر، یک نگهبان شهید و ۴ نفر مجروح شدند.
🔹
اصابت به شلمچه و فرودگاه اهواز تکذیب شد. /مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/670427" target="_blank">📅 09:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگردانی خودروها در سیل ویرانگر شمال شرقی چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/670426" target="_blank">📅 09:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وقوع انفجارهای شدید در بحرین
🔹
منابع خبری از شنیده شدن صدای مجدد انفجار در بحرین خبر دادند.
🔹
وزارت کشور بحرین با صدور بیانیه‌ای فوری از شهروندان خواست ضمن حفظ خونسردی، به نزدیک‌ترین مکان‌های امن پناه ببرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/670425" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
♦️
سپاه: تاسیسات و زیرساخت‌های ارتش متجاوز آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
روابط عمومی سپاه:
🔹
تنها راه باز شدن تنگۀ هرمز برای تردد شناورها، پایان یافتن مداخلات ارتش متجاوز آمریکا در این تنگه و احترام به حاکمیت کشورها بر آب‌های ساحلی خودشان است.
🔹
ادامۀ این مداخلات حوادث بزرگ‌تری را در حوزۀ نفت و گاز جهان به‌دنبال خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/670424" target="_blank">📅 08:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M093X7DA885alfnZcfW7gK0wlA5wcDalP_1AjYnF6Gbs5TLXahDkE0GUVhdSXlEJ2Hek9Ur7fF6bJc-w219KXuoyekATQvr-q-M2j22BCFZOBkoe32WaI5uUHNaeNd93W7MGxSlzQRApr_GPA7K5kgyB38HjJEEriMsHGR0OmbcB3eqPKRanj2Z9v0eDrnpzsB8OuQggjOg4W008sxpXBdM-59H4xC1rREzmu1a5PcizKcVyWPPcZ_FyCQNcdl45hgGN1831Ioo705KuuiSt0eCwKs1_KKwgYZoGfTxGaZBlrNcA_4va_ZbAad14WY5aKJiYt7iVkW3Hp0PVEnwSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برترین گلزنان جام
جهانی ۲۰۲۶ تا پیش از مرحله نیمه‌نهایی
🔹
از این جمع فقط هالند امکان افزایش گل‌هایش را ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/670423" target="_blank">📅 08:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRHaU6L0qRUNg7MpqVhDP-mJMErNR4PLKdJw4uHa5MES9ObeTy_xWgmJK_moEbaAWhZ5VVLVm0unakKvdTknBzt1GviQaGTyYJMnYSPcM_86YBIry7Hge3HteXK28CNxIJimkVDviVBAvdPVtewL_pypRYb_qc8SgdjwyhnHxYE0k-XWLbwr1mB4ldq_rgAEf7w_UzsF36TAdqEEd_WS9dQqaOliaDXA-HfsGKeWbchcEgBOT4prcV3o2740KAUMvYVTnJmaqFZuguIB5gxwD623uTunzcfVE8sePtvlUQdW9c0YIl1Q0dRdRgWDjvCyClSscwZ3eMLtDYJ6M7Yq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به مرز ۸۰ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/670422" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbrMKxc4sZt77BZ7VpfxCU786b26aDHod0h8UQjTUoswx72D33Q4iBUsuVM_UWY8MNvZ-JZZh1HinxLZv_wvCr8QfuyZD-dy5f2MGs6TuK2sYqsQNy4B9y8tp9mpMeCrssEWi_Yko_GCELNj2YI-YvEkvjw086kxS_jX86RTyF_HwunvQBA1x3-t-zcpUwCnJNj0PajB99nUZhDMTUUU7ez7WYJbkR4qMotlUsAp9fvLS66sL9GydAgZQgUMrPrUkOQ9UIRMe_4YSGbNNms_7M6ZW73NRRkUoTLEveRhGLIeYwYRx-wpgQxi70kvASvLYakxOH5eVAWicFazl17kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucui_BrfF19ziKP_EqEhveq1quIIZlc8cZX97xmXINrSneb0LD_Ar95YW0ig_QYzONMni0_34YQsLrsO1bV-8Aopn2Q5ak1YIOqgznuIxZ25A9VEMPDljr-oulKtx95yhjg6sjnxM0YeY405IjPbzBW0Iqype3geOE-P5jfkHrtMj6F8i7tZk4UbqxKyRYhakrD-sES_6w_PNiZkrgDgh_RB7j-NiJuIcRQqtIZohHAlGR949mZ3nrqVGRd_NHI8qf-SdpB3WV3UbKuy-LPNtCFKNP6P_ZnP4sSWlVeKggPxkvfjzK8Y3tlsSe0OLZvkW3My-z8hEziN9eJ3f8ULEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7ok2aRAmkCh_fPJ4Ni4EVY7m6qI3_I4rDSJIVFqJAcIKQ-vD0-FHfSE3E7dGIc5PFzfcgfdxdfgPmBllq2ts_hWdbE9BGuYt3dlD3lQuZAVeWhf8d4n9DFvCgDRN9KxmflXeM89isz39FcTUfZGDggBA1K9dUrtB4IyAQHJzU83HRyfEH37IRGHp5ZE2p8FB1dh6bOuQfo5pUW8ciqFA0RuKzhqbFvef8c_Jp1DChShI8MnKjI-2f-6WTEnxGVCWv6Ytj60g7r4RqD47-bYzrQ8rl8uE89p5dRd8SlfEE44nMWI0RNKmYDQXi3m8E1QX8kyC60hNgdrXTOnQ8Yspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwdUkprefC81zm5bEhIAtGkYtWYWNafwmByp1rbeToaDaQfLy5j1HHqFbe7ujNej38JpN5OtDjiLhGF_NfKyYjAVZuhGQEdkUVY4lPySKafXq3Ws1fImhqfQzkazWhSXs16qRGivNldv7kALCbD-7zSgggdHe3ktcerXSPKmkkJ5vEhlDWeIhhh7pKxzcEcbIPtJZIUc0hNV4DLU7lMAln4z0U9R_prKXA5UAEWaq1Af6t66M4zwtUQKa87IGb2ImpCLjlVbXhVk-YwfzQFUbxs4TzZALFwZ-bIieMO9FCvX805YtfwbmgArCTvGEsc09VyZCAT2QOsqlWCriydQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjCXlN9qH_5ldGA7JwDGzxSBBi-0-hqsrwbdF3l4FxryWFcm2bwHG_pWkKvUAWoe8qPR-LXCyNSnBCCvkAPwoRa1kr8Z00FqSl1DwBbUuFnZHEyUhwSPGAmTB6hXF9dGuhqnp17dRemQC4K_esb_mX-9GmLwoUcqmrZJH5rnOvx2x--_9vtpSDtSCeoTIbCj1cXmrMFwCITqzAeCapucaSjCMjxi4ZF2GNdtkjapL125RC52NkWLNgD8yPcT1dlCdBI4vu2RSCl4AUNnLqWmdrzVw6wNwXmHCVVNr8hFa001k8jaejk40I4T-Ge1TTEnMz8PC0tTIjiuB6F1q9SfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0ngLBh-7u3ujxq3MNSAaI9xnqLwO4eKoAKWyt5U7LnY4nHnb0R1TK4hKtHkDcZ_5K5qr7FpEXsW8sXvI4ldPI5VBkO9vqi5O3eGyZvLC7WbYv47holPO8gWzADl6MMLPlABh30eDyL3WJYhuT20kdkLUgME_Q9ILAmgA0Czv2d19wtrYS2PGv7JHzOIag6k3unw7FDDW8I0G-9nxGfWmR4_XDDFPI9r5m4FY3cgh6h1WKTqkyDGHtimhYoemvhrGyPcuaXI1b2C3KIqMWIbWkjqCrYmTE28F_geVf2esc46djjQxx9OZPzwKV5QFqj5FMuOe-yLsAffXUdsnqc2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khaAqP229j0wNsB-OnDjQxFi8YBEsBMOtbk6r1n15AmMa_ZJDmBIMAejjVW4GkZ9z-y815TXBqfAhOyYRzpXhZZxaRZZh859Cb2tI4t94B4J_58TtlO6HgNhroUk9IANW8U8HTD-sm9ET2yxJ3YJiYxajUBgg5_nEY6sDFFQFFiKiHKoVIYy__R-9h7EQjQ8wDAvRCIXrpL4CEL59_mTvQ-NuvPe5UH_brX3ApeLYl0wfFgXsfoRGODkCaL6nXtr5yjhpk5amejtc_xKV3bt9MVx0faJD0bY-aPMkto2u1zORxkjHX6kc6zw7T4YXWNRl6k_2ARtqitrbqGaXXu9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s120GK3KjmeQvJVt2og7hVqyUL-v1IBlH8T2C7wH8rkooffBri7AMnovJvs7DqcYgJlTZ0C133YUFM4JkuRAa674rt3zPQAtmpqVL5-vavkipRH2qsrkFyfOis9un1yEmk7B99Bdsy5ZqKUiiD6lz0Akf2bsNPDBmcXumLWkIVlsaU9O2EPCKwQwOCXciEcvZROy8LnM5rOn-Y7z6orQVNQKJumHBWVJoCK3N-rYbIbaEDSL32AvPKHpQ1uTxCtFH_x3lpxbusnxolsjQ4HV2KbptzQlfKB_pf03y0oRIfi4Mcllbh9tbx2T6U66H0awLM1FtDHpjcabCeiL0d0dVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7gOFvKocDulgcWaQzFipkEl0-cqv1C6Db_b4mN878OCCjUp_W9woFBKwrTjNCmo-88P0AATwW21sUGFFztRvXRJlprfhiwlaPuEXWHEOU0i-UU9x2pAJ6irB81IKjEVo6fwjCsc9TxJx6o7B5cmhZLcvqwTAwLcBbmnzZmsM84dUQHfrNC0FpJusc0HxjwswNqew0AAmP8HJrIckC1mYjs1rEy4CX6nXwOnkgwK8yDp_ucKSxeF0baUmynak7z8dLgHH9_WRRp-_7EiJoTxBNAnXSJu8Ai9bfwBKKC8Dqma-r1gGB2SZ6JYUDJwKwaM0Fhd3-0JHZBPf0jnTA74xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/670413" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GofTDhNtjums00DKxaM-Iwt98hi7uc8m9m8Fkym8QqyQfyygZplRXjNKiXwb_PQvT43OrB-K6ftbxwOH_jgUhtCgLJdm8klqkNMGM14SUg4dEsVwujv06PsA3_3DaTPwJLyXa3I07dzwzd6n19FPaNxu6pJt9hBExp8MUsI31p6LEN4S6h1zdk2UfobzIaBv-Eah83wqnJ2ZcAOZUMcVpOIxdeA02X1SOisPp7WSvS0noEMS565YJ4TSK80n-k1AzpWfjyl16RdU3FekfTjx_2LJHE2I7B90r_zZS9Q8bOwnvMZe4qD8ipXRXXRyE76xevK9s5g6MaxGHS3YoZGfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الاخبار: مرگ گراهام، جای تأسف ندارد!
🔹
واکنش‌ها به مرگ لیندسی گراهام سناتور جنگ طلب جمهوری‌خواه آمریکا در جهان عرب همچنان ادامه دارد؛ رسانه‌های منطقه ضمن بازخوانی مواضع جانب‌دارانه‌ی او در حمایت از تجاوزات صهیونیست‌ها به غزه، بر کارنامه‌ی جنگ‌طلبانه‌ی وی در منطقه تأکید می‌کنند.
🔹
در همین راستا، روزنامه لبنانی «الاخبار» با تیتری متفاوت نوشت: خاموشیِ بوقِ نسل‌کشی؛ لیندسی گراهام... هیچ تأسفی برای (مرگ) تو نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/670412" target="_blank">📅 08:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
انهدام پهپاد متخاصم دشمن در بندرعباس
🔹
پدافند هوایی جنوب شرق ارتش یک پهپاد متخاصم دشمن را در شهرستان بندرعباس رهگیری کرده و منهدم کردند.
🔹
این هوابرد از نوع پهپاد انتحاری لوکاس بوده که مورد اصابت دقیق قرار گرفته و ساقط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/670411" target="_blank">📅 08:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای جدید در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/670410" target="_blank">📅 08:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات مفید برای تقویت زانو
🦵
🔹
زانو همیشه مقصر نیست؛ گاهی فقط اولین جاییه که دردش رو احساس می‌کنی. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670409" target="_blank">📅 08:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سپاه: پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت به دست رزمندگان نیروی زمینی سپاه منهدم شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار ملت شریف ایران می‌رسانیم؛
در چهارمین مرحله از عملیات مقابله به مثل، رزمندگان نیروی زمینی قهرمان سپاه، پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت را هدف قرار دادند و دو سکوی موشکی "های مارس" و زاغه‌های مملو از موشک را به آتش کشیده و به طور کامل منهدم کردند.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/670408" target="_blank">📅 07:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هرمز؛ جایی که باید برای ایران ایستاد
🔹
بی‌تردید هیچ انسان خردمندی دل در گرو جنگ ندارد. جنگ، هر اندازه هم که در ظاهر با پیروزی همراه باشد، در عمق خود زخم‌هایی بر جای می‌گذارد که سال‌ها بر پیکر ملت‌ها باقی می‌ماند.
🔹
از همین رو، صلح همواره مطلوب‌ترین مسیر برای ملت‌هاست. صلحی پایدار و محترمانه، نه صلحی که بر پایه فشار، تحمیل و توافقات یک‌طرفه شکل گیرد.
🔹
حالا سوال اینجاست؛ وقتی آمریکا به تعهدات خود پایبند نیست و خواهان توافقی نابرابر است، آیا باید از حقوق و منافع ملی خود چشم‌پوشی کنیم؟
🔹
واقعیت آن است که یکی از اهداف راهبردی آمریکا، کاهش اهمیت ژئوپلیتیکی تنگه هرمز برای ایران است. تنگه‌ای که نه‌تنها یک گذرگاه دریایی، بلکه بخشی از هویت راهبردی و قدرت ملی ایران به شمار می‌رود.
🔹
تنگه هرمز امروز یکی از مهم‌ترین ابزارهای قدرت‌نمایی ژئوپلیتیکی ایران در منطقه است. اگر این جایگاه تضعیف شود، مسیر فشار بر ایران و محدود کردن توان چانه‌زنی کشور هموارتر خواهد شد.
🔹
از این رو، دفاع از جایگاه راهبردی تنگه هرمز صرفاً یک مسئله نظامی نیست، بلکه دفاع از امنیت، استقلال، عزت ملی و آینده ایران است.
🔹
ما مردمی هستیم که تاریخ‌مان با مقاومت، غیرت و پاسداری از سرزمین گره خورده است.
🔹
حفظ تنگه هرمز، حفظ بخشی از اقتدار ایران است، اقتداری که باید با عقلانیت، تدبیر و وحدت ملی از آن صیانت شود.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670407" target="_blank">📅 07:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOPdDKUYqjWVYUk_WPgqBQ4ZceaH3l2QKu3Yx4r4rOXaB_SVdZ6ElC0beS2rf8eU77oqrSubbge94BMMlukNu2eGVOwM2jQBCdgP67EJtXNDxh0YDmjKdY6I4OR-eqW4qgf5qVUYsUmHJqidBefcaDRwg4iqYc_FFIVW5YXi3WIllqC15kSYADN-KwcwfaFRfLzMcsJKWpB64AwIgX1aBT6Xio59dHv3c126lWnqARzEiDs5i8EHN1vaKT51oHMxCvexOoclO6LbyLQddLp1ZuMHTAx4eLh5NCEcCMYuR4is8d-ShL8eX2Z_79ZXKIOh10eeDm4whhfHaJQiSH2lyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفتار آمریکا در برابر ایران چطور تغییر می‌کند؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670406" target="_blank">📅 07:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گرما فعلا ماندگار است
هواشناسی:
🔹
از امروز دوشنبه تا چهارشنبه در اکثر نقاط کشور جوی آرام پیش‌بینی می‌شود و تا پایان هفته ماندگاری هوای گرم ادامه داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/670405" target="_blank">📅 07:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
توزیع کارت آزمون کارشناسی ارشد ۱۴۰۵ از امروز آغاز شد
🔹
داوطلبان در صورت مشاهده مغایرت در کارت ورود به جلسه خود می توانند از امروز تا ۲۶ تیر از طریق درگاه اطلاع‌رسانی سازمان سنجش ویرایش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670404" target="_blank">📅 07:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670403">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIIZMoeG-RqQTONPy8ZyC1htiJA3KmbVnPEF9SVm9108u_aCcmgKcbovn1PIdeSezwBfhTV9mLYVe9kPmenAmUXcrboHuCH5JGqEhBInY19Lkh2e486vXIDyu0MTQ8dH3LeTQdpO_WpoEYtICi36ZvTWysLoPv9C5WwqJHveegeRzgddwhz8y1etk1x-80KSTY_SLPEy7ArZv7lSZdYRiBBGW4dVWRA7Gw32T6_krZyCHT0rk5nERDLC16C-GcbUsDkmrDNHtS3diBjKmKxlnGZfnJUVDFh0WkEAFLLnYxG1qKwUBPiGKBD25Mtjqb1NbWGc9X7OfYGiZk606Uxfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۲ تیر ماه
۲۸ محرم ‌‌۱۴۴۸
۱۳ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/670403" target="_blank">📅 07:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670402">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
صدای مجدد انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجارهای شدید در پایگاه نظامیان ارتش تروریستی آمریکا در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/670402" target="_blank">📅 07:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670401">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c79f83d14.mp4?token=UJcwRJvd1PS0mdqbQBlv7TJ1g5XXyqrvAMHpYZnppqUJWpehKy-nZz4cE2NnGMkhtX1GVoXcim6Wdm_kJCeq6JgMsPh21qji3struvN1TGzEueLkQznbvyUCCQEey2nXEiMzKr18a1fpDwhNmJpB6JH9gGRFaDbOAtxT0D3C0WNgUA-Er7MZ3Lt7kC6YWnRUODg09FqYPbNYpDulYpFAkl24BfqbY4SjYCi2FiAbmvoOiErEIzKrzWS9VH4cpULOMA917XvbJM7Zjm1_MnedEG_Z5gZ1tgDK8LILaTOXfFfWYAvYEae2vHmidlqU0EP7FLp1UgUvNaTfH5NQyixWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c79f83d14.mp4?token=UJcwRJvd1PS0mdqbQBlv7TJ1g5XXyqrvAMHpYZnppqUJWpehKy-nZz4cE2NnGMkhtX1GVoXcim6Wdm_kJCeq6JgMsPh21qji3struvN1TGzEueLkQznbvyUCCQEey2nXEiMzKr18a1fpDwhNmJpB6JH9gGRFaDbOAtxT0D3C0WNgUA-Er7MZ3Lt7kC6YWnRUODg09FqYPbNYpDulYpFAkl24BfqbY4SjYCi2FiAbmvoOiErEIzKrzWS9VH4cpULOMA917XvbJM7Zjm1_MnedEG_Z5gZ1tgDK8LILaTOXfFfWYAvYEae2vHmidlqU0EP7FLp1UgUvNaTfH5NQyixWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو مربوط به آتش‌سوزی در پایگاه دریایی امریکا در بحرین پس از حمله موشکی پهپادی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/670401" target="_blank">📅 07:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670400">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
گزارش‌های رسانه‌ای حاکی است که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین هدف قرار گرفت و در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/670400" target="_blank">📅 07:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
صدای مجدد انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجارهای شدید در پایگاه نظامیان ارتش تروریستی آمریکا در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/670399" target="_blank">📅 07:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایۀ خبرنگار آمریکایی به وداع با سناتور جنگ‌طلب فقط با یک گل!
🔹
یک خبرنگار آمریکایی در مقایسه مراسم باشکوه تشییع پیکر مطهر رهبر شهید با مرگ سناتور جنگ‌طلب آمریکایی، با انتشار فیلمی از خانۀ او نوشت: آمریکا ۳۵۰ میلیون نفر جمعیت دارد، اما تنها چیزی که نصیب این فرد شد یک دسته گل کوچک مقابل خانه‌اش بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/670398" target="_blank">📅 07:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات جدید به ایران تکمیل شد
ادعای سنتکام یکشنبه شب به وقت محلی برابر با صبح دوشنبه به وقت تهران: نیروهای
🔹
آمریکایی با استفاده از مهمات دقیق، ده‌ها هدف را در چندین نقطه هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های بین‌المللی در حال عبور از تنگه هرمز را کاهش دهند.
🔹
در این حملات، سامانه‌های پدافند هوایی، سایت‌های راداری ساحلی، توانایی‌های موشکی و پهپادی و همچنین شناورهای کوچک نظامی ایران با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای یک‌طرفه هوایی هدف قرار گرفتند.
🔹
نیروهای آمریکایی برای نخستین بار از شناورهای بدون سرنشین یک‌طرفه دریایی استفاده کردند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/670397" target="_blank">📅 07:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e107caf93.mp4?token=mOxB_sjit0fbIsyyZmCQdWAYdIKp53jc0Vml4Ml3Sy5yvAN5bivassKDdnkpilQ1i0fOeWToq7EkByhDDrWTOQruDqoTA3jXLb8yP1gX3IXwNSR9yEW36FKcC1Ejao4S3hHv8p6qfCgB8O88jYLVRlDKGX7c_MVZLnVJrhvU89Y_EG7eV3AGRzq628Vccj8Kgu6rlc0FoB5iKJN_K98PpkdPOJVV6BsL1e7bDYbqu-nXswv1IyHKjZfov7PMHk6WDthM3jym1goxgtmc0OJJ2xsZtNGFxsH50CNHVQkN-0AwKhp24NJ_XDi2bDKQ7EbVj4FHrezasDGiOvRt4y-e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e107caf93.mp4?token=mOxB_sjit0fbIsyyZmCQdWAYdIKp53jc0Vml4Ml3Sy5yvAN5bivassKDdnkpilQ1i0fOeWToq7EkByhDDrWTOQruDqoTA3jXLb8yP1gX3IXwNSR9yEW36FKcC1Ejao4S3hHv8p6qfCgB8O88jYLVRlDKGX7c_MVZLnVJrhvU89Y_EG7eV3AGRzq628Vccj8Kgu6rlc0FoB5iKJN_K98PpkdPOJVV6BsL1e7bDYbqu-nXswv1IyHKjZfov7PMHk6WDthM3jym1goxgtmc0OJJ2xsZtNGFxsH50CNHVQkN-0AwKhp24NJ_XDi2bDKQ7EbVj4FHrezasDGiOvRt4y-e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود و آتش در پایگاه‌های آمریکایی در بحرین
🔹
در پی حمله به اهداف نظامی آمریکا در بحرین دود آسمان مناطق این کشور فرا گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670396" target="_blank">📅 07:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر برای دومین بار در کشور به صدا درآمدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/670395" target="_blank">📅 07:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/670394" target="_blank">📅 06:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670393">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
صدای دوباره آژير خطر و انفجار در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/670393" target="_blank">📅 06:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997573ae21.mp4?token=ZgVlfS5QVGIusFyhbFXKcgKoWW5f9_s5bVg8Hx7LQ_jlWJMnTqwFeN5h2ExnL1KkQJWlnMgEUqpelSxWa_zsYXJvtgXcTCG6T-LYIzlietxwh6LDD7DzLi8LPE8b_M5yK4qcAS5c5FKRhwUQDYun6OGQR3oxcLX1UYrq_VYgzf9bYwQGqrQCzQ-1MPUOR1piNN94_iHiUUHlnrlrXZL3Yz6LnMbTbIT9JcSefKfVGpkfB3dSbxKxBKIl5pIrvj1y5dsrsHMt3DyZH53VXVSEDEs_pmqzWMe4fDJ6jzkcBFxHHlc_DU8V-DIhP_RhhCVoZJuYyKFvfFB4EGnQEohKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997573ae21.mp4?token=ZgVlfS5QVGIusFyhbFXKcgKoWW5f9_s5bVg8Hx7LQ_jlWJMnTqwFeN5h2ExnL1KkQJWlnMgEUqpelSxWa_zsYXJvtgXcTCG6T-LYIzlietxwh6LDD7DzLi8LPE8b_M5yK4qcAS5c5FKRhwUQDYun6OGQR3oxcLX1UYrq_VYgzf9bYwQGqrQCzQ-1MPUOR1piNN94_iHiUUHlnrlrXZL3Yz6LnMbTbIT9JcSefKfVGpkfB3dSbxKxBKIl5pIrvj1y5dsrsHMt3DyZH53VXVSEDEs_pmqzWMe4fDJ6jzkcBFxHHlc_DU8V-DIhP_RhhCVoZJuYyKFvfFB4EGnQEohKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
روابط عمومی ارتش:
🔹
در پاسخ به تکرار حملات غیرقانونی آمریکا علیه کشورمان، ساعاتی قبل و در دور جدید حملات پهپادی ارتش جمهوری اسلامی ایران، محل استقرار نیروهای آمریکایی، سامانه های پدافندی و موشکی، جان پناه و سوله‌های پشتیبانی ارتش تروریستی آمریکا  در کویت هدف حملات پهپادهای انهدامی ارتش قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/670392" target="_blank">📅 06:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سپاه: مخازن سوخت و زاغه مهمات پایگاه هوایی پرنس حسن در اردن به آتش کشیده شد
🔹
شب گذشته به‌دنبال عملیات نیروی دریایی سپاه در متوقف کردن دو کشتی متخلف که با خاموش کردن سامانه‌ها و حرکت در مسیر غیرقانونی، کشتیرانی در تنگۀ هرمز را به مخاطره انداخته بودند، ارتش کودک‌کش آمریکا که خود محرک این حرکات غیرقانونی و خطرناک بود، بار دیگر با تجاوز به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران خوی وحشی‌گری خود را آشکار ساخت.
🔹
رزمندگان غیرتمند اسلام در اولین مرحله از پاسخ به این تجاوزات، چندین زاغۀ بزرگ موشکی و مخازن سوخت پایگاه هوایی پرنس حسن در اردن را با شلیک موشک و پهپاد به آتش کشیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/670391" target="_blank">📅 06:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
صدای دوباره آژير خطر و انفجار در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/670390" target="_blank">📅 06:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS در کویت به‌طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند هوایی پاتریوت در پایگاه آمریکایی در علی السالم کویت و همچنین یک سامانۀ راداری راهبردی FPS در پایگاه احمد الجابر را به‌طور کامل منهدم کردند.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
🔹
عملیات مقابله به‌مثل فرزندان غیور شما ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670389" target="_blank">📅 06:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
برخی منابع از وقوع انفجارها در پایگاه هوایی «موفق السلطی» در اردن گزارش می‌دهند
/ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/670388" target="_blank">📅 04:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
یک شهید و چهار مجروح در پی حمله دشمن به ماهشهر
🔹
ولی‌الله حیاتی، معاون امنیتی و انتظامی استاندار خوزستان گفت: در پی تهاجم بامداد دوشنبه دشمن آمریکایی و اصابت یک پرتابه به ایستگاه پمپاژ آب کشاورزی در شهرستان ماهشهر، یک نفر به شهادت رسید و چهار نفر دیگر مجروح شدند.
🔹
فردی که در این حمله شهید شده نگهبان این مجموعه بوده است.
🔹
وضعیت مجروحان توسط دستگاه‌های امدادی و درمانی در حال پیگیری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/670387" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای قطع برق در سراسر اهواز صحت ندارد
🔹
بررسی‌ها نشان می‌دهد ادعای منتشرشده در فضای مجازی مبنی بر «قطع برق در سراسر شهر اهواز» صحت ندارد و شهر در وضعیت عادی قرار دارد..
🔹
از شهروندان درخواست می‌شود اخبار مربوط به وضعیت شبکه برق را تنها از منابع رسمی دنبال و از بازنشر شایعات و اخبار تاییدنشده در فضای مجازی خودداری کنند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/670386" target="_blank">📅 03:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رسانه های عربی خبر حمله به گذرگاه مرزی چذابه را تأیید نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/670385" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امشب، یک پهپاد اوکراینی به یک انبار نفت در شهر میخایلوفسک روسیه حمله کرد...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/670384" target="_blank">📅 03:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارالذکر در نیمه‌شب‌های حرم امام رضا(ع)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/670383" target="_blank">📅 03:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQgXO9juC0oeQUG4J4HVMeYdAh1-665K-rUcfW2Yf5-QB3SpabaMvlsLi0lYd_yeTyrUUfgXcD81oF0mJy_ENP1BIgNi58dJpG6h4P7Kwsp4PMAKtBTYqiP6iCFyBa3xN4-tZg-1r8RYutj1MASVHXLnqD3WdZWhp3If1pMdRILut1DZfPKRP2O8MMI78SMe8ldgKUJxINwkCaSpdcnJa17hQT_lTL6yHh1ZmRb_Ex0ZYfsf-ZSKswMFWS6QegM5I-d7-8RC0iX5OAYbs2PP2HCGzytjO0ZaQTweciaONr_EJk4R1YJWcWrUush6Lhf-hSn87QS3JkEmli5SbSuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرهایی که مورد حمله آمریکا قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/670382" target="_blank">📅 02:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
الجزیره: حرف‌های ترامپ درباره تنگه هرمز با واقعیت زمینی تفاوت زیادی دارد
🔹
تناقض در این است: رئیس‌جمهور آمریکا مدام از چیزی می‌گوید که آرزویش را دارد، اما واقعیت در میدان کاملاً فرق می‌کند.
🔹
واقعیت این است که ترامپ گرفتار شده است. او سعی دارد القا کند که تنگه باز است و این موضوع بر بازارهای مالی جهانی تأثیری ندارد، اما ایران به‌وضوح بر موضع خود پافشاری می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/670381" target="_blank">📅 02:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
استانداری هرمزگان: تاکنون اصابتی در بندر خمیر گزارش نشده و صداهای شنیده‌شدۀ احتمالی ممکن است از سمت دریا باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/670379" target="_blank">📅 02:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: یک مقام آمریکایی گفت انتظار می‌رود موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در شامگاه یکشنبه انجام شود؛ حملاتی که از نظر گستردگی بیشتر از حملات اوایل همان روز خواهد بود./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/670378" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfJdy6UBlC2p880OTPKSNLGlT5rpH2uzipif3k_ShMiwKP-dGDLHI0QVi2kQ_XWrYAye_diwHOrQ_MoviO2h9AgvHRWM0EEN15AcEMSIgkE7C7lmTbNZxXBFEAk7g-rtGavdrm9R5sLJ3pn-w9bLMvP_63lGGxb8r263GGExNqgI5Kq-0hwShi9RqfItJwHY-c8v_E5WwTWUlDO8NxK-b2myiJBFKL8xt26jrNKdE6ETFTXftNS7OcVlOEPNBKB0e8XtRLumyahgX4kSwULcpFle_5UTc-Bxt-aXuYhyBxaB8K-MT_rhtUArPwLU-Cb2swtQfX3Qlkjk1Jlh0xWb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با شدت‌گرفتن درگیری‌ها، قیمت نفت برنت به ۷۳.۶۹ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/670377" target="_blank">📅 02:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
نقاطی در آبادان و اطراف شادگان مورد اصابت پرتابۀ دشمن قرار گرفت
معاون استانداری خوزستان:
🔹
در ساعت ۲ و ۲۰ دقیقه بامداد امروز نقاطی در شهرستان‌های آبادان و شادگان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/670376" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
معاون استاندار خوزستان هرگونه اصابت به فرودگاه اهواز را رد کرد
حیاتی:
🔹
دو نطقه مورد اصابت اطراف محدوده شهر بوده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/670375" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت  حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/670374" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند، برخی از موشک‌های آمریکایی از کویت به سمت ایران شلیک شدند
🔹
طبق این گزارشها، موشک‌های آمریکایی از کویت شلیک می‌شوند، وارد حریم هوایی عراق می‌شوند و به سمت ایران حرکت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/670373" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن چندین صدای انفجار در قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/670372" target="_blank">📅 02:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت
حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در حال ارزیابی خسارات احتمالی هستند که گزارش های تکمیلی متعاقبا اعلام خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/670371" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/670370" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مهر: معاون استاندار مرکزی حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/670369" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/670368" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فاجعه در بانکوک؛ ۲۷ کشته در آتش‌سوزی یک رستوران
🔹
شعله‌های آتش نیمه‌شب، یک رستوران شلوغ در بانکوک را به صحنه‌ای از وحشت تبدیل کرد. در حالی که مردم برای نجات جان خود فرار می‌کردند، آمار قربانیان لحظه‌به‌لحظه افزایش یافت و علت این حادثه همچنان در هاله‌ای از ابهام قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/670367" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مهر: ساعت ۱:۳۰ بامداد امروز دوشنبه صدای دو انفجار شدید در اهواز و ماهشهر به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/670366" target="_blank">📅 01:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله دوباره آمریکا به دکل مخابرات اطراف روستای طاهرویی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/670365" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670363">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCRrqA5XMyexG-7G4AEK4J4gJ3yNasWXkGIKNS18HODwrCiylegrb4BtPfmEoR_BcW28IAEO4qHJ84P7ywn_LP2qVZCp7JlASUWIQonxoWHalyNv8Ez1UNgZll-Pddfged4ZBbd1ROVZd5aLE5JQuws__EU43o-RklrvGnjAjXJxYrIp1BlcJMMeriisaawavVvD8Tv0izhxE8pR1-CMOWvY6u70nDRa2IhYmcwP-vDRq-rXt_frot9HMv_Qk6hmmI9ayJa1HfMSS8QSfvFbYmrcAKA0FHbFlY0leNcUt8oNgl7pPxYPkEI60gs4E0LbZgTnRvZviU_27T1-bEv03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz4X81mvX7gNB43Y0zJ_eUUEO0cxfAkHxFjMBU35IZIjPy-UCJ_Sicbo3mSiJ7kYcou4tsjh5oPMjc3cW8cdKYkvxqLwNfpxa7FbyqYcC4h7E_xZnfhNoLtBmCS4uI_9MAyPGnhVIYacPzbrxrAgVZ6VR4QP8_EqjAQW4xtpt3V0mZKhYBgRCg--UG0GgRaIyDT9GstBB6y57N-f8M2FjISn0KyTEwyd0_pvOoFXQpR3wXx2CWvGR_9ZwQ8LcGYM661IVdVp9xPH_GhJbB0eKRtMscEfdOM5jxyFGT63QoX-jR33LsTunSREHTwmEaXM7Q-DVWGQZQuHQSQZPotoJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری
کم‌تر دیده‌شده از لحظه ورود پیکر رهبر شهید انقلاب به کنار ضریح مطهر حرم مطهر سیدالشهدا علیه‌السلام در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/670363" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670362">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-3wxMDooGvLRi12ZLIkCGz5zuvwGMkHtN2bVuzLYUQdGK5vI_1hAEcJqqqYf86HgaCSqizPJ-ktxke1oQO7pGZe6FdTz21jucT4L-M-bPLrnTT2mUlAhMC3gTLNjqlcUR-LpDXQZFg1UfmxOZsiofPsm4xj5iavRm3Tl_iAxwd7qXMulgE7YCUX09HdpisYdKJTSrU19cJlt7u-LeUUKkdECDcjBPe16tQ9-btBJ6bzNsjmDySoPoHdaTUwxJy5L67hUMqz7GJATRbbpcStMWENXyRPFRd2awVZNuxAP4Z7qZrUhS1F7DO0uKt6c9YguhDNcj_AXwRh3ZbEcUMcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اراکی: ریختن خون ترامپ و نتانیاهو و شرکای آن‌ها «واجب» است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/670362" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670361">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah3hfvglhfzYNW4RrpZdNjV8CzHrJE5PAneXhU4-yHK3hOtzFvZ8dmTHvbucp0GmIy4phuM2Qn_5lao7MtBfelj3bPREAXCd61Cj2IGGLA0He1BDHu-SS2yxiWuqQY2QqJ8KYtUjI2qInWBrBuKtk21kjx0c3vmL7H7i0ZPfMepj_QaN8SX8npi_uj87dMk0y9e4yIwzKr0e1SEbUv60Yx1baCU7LptV_GF0v2qT8r9e1mANbWgSYhC3sFFDSCItrQw41qAKNfxKewNO-OPZC3N2pLlEcZsStWV8V6AwGcnHW3VBDJHYWL1faevs5LLd57kkm2ehDg2xDpcnkFIHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار نفت با افزایش قیمت شروع کرد
🔹
نفت با ۷۸ دلار بازگشایی شد که رشد ۲.۵ درصدی را نشان می‌دهد و در ادامه رشد آن به ۳.۵ درصد هم رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/670361" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670360">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سخنگوی فرماندهی مرکزی ایالات متحده در گفتگو با سی ان ان مدعی شده که سپاه پاسداران انقلاب اسلامی ایران به تازگی به سوی شناورهای در حال عبور از تنگه هرمز آتش گشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/670360" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670359">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
برخلاف ادعاهای مطرح شده در فضای مجازی مبنی بر تهاجم دشمن به اهدافی در این استان، تا این لحظه اصابت در مرکز استان از سوی فرماندار شهرستان بوشهر و نیز در کنگان توسط منابع محلی تایید نشده است
./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/670359" target="_blank">📅 01:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پرس‌تی‌وی: صدای انفجار در کنگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/670358" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در جنوب شرق کشور؛ جزئیات رسمی در انتظار اعلام مراجع مسئول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/670357" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/670356" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رسانه‌های پاکستانی از چند انفجار در چابهار نوشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/670355" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
