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
<img src="https://cdn4.telesco.pe/file/mM_iCbSU3kev9xxpdCLSqktQrqH9MEaHz1s5fnTiewCoZ5v2ixrFWsS1bvaTI-_th3tQVtI12svRScHzpUyko1O2Jv36sgtZeS0-nWqOHVrkXQmug37LVc9DfHYBPoIWjFejhKVTu4nGpQbb8MY9Q8LtMyIrc8jAUZHGeosWqeOpDBGDS7EIK__qc7wKNGnCHos2vkYohaYshZ0ssJ6pxXD1-sTgqu-fjYYJGMU0jVQdghHq1aEpioRbw2CgqLJiaLhwE2tE1Pfh_4YSK_ttvw8nH_BPhkuUg-SkWUu3mjednWPmUpRaVp9L5n3GCA5ghGoHZfieeUrSpd04x9Kncw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-694671">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هم اکنون| عربستان اعلام کرد که خمیس مشیط و جازان هدف موشک‌های یمنی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/694671" target="_blank">📅 22:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج ماده غذایی که کمک بسیاری به مغز خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/694670" target="_blank">📅 22:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694669">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/694669" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694668">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/694668" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694667">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-hAMpsUkbiKqysMGTa2PWE12LlOBpW71-oev6KOXckfFaBfsJ7e_lTbrq-dn_giiEXBrYu7yrlBHFpwjx5tqRbCY84uuoz-i8Gi9tDacDuTeq__0QEIsisrB1pFP_GCePlg4F8mqCjkzwd4othspB6Px0lsOmpdG07sllLUsy2B-w0u40XSNyP3ggKgc_pPIiRxZ88UtEZMX1Uh6XUrGfJI1YVUc0aYu24e80jl3oyKujiWmo8N0XB2OpxQj0Il-jmiQKbWomwttr71M2PcauGpC2LT8JU7hqON-z0f-fYJO2Ywdxu6MGGVOPNFsHEN3ToGSes1hiX9ia-8-b6SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/694667" target="_blank">📅 22:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694666">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo72IsLZ4lwQbtLGi-voysbC4eTjemCT5jE_Spr8QGcoT4bq0mm4Z0vprXqvs0FPu66aqH88maSCXbSbvUlHq4F4TH7kqlpMQpRrZZZd1uxp6EV7a2vmaWoh2YyeqZhtYx_p7PoVvHzlTIMueaCcUa3K9bszveJuMEhxOmp6-4LlVSlUMsoOOyWqM9I1NOdKCog95BQK7RCjINDlm0v0WLAt2qpOv1EEtywlHWYjDNxvo5r2_8y-wyuf5kUmKMrLOot7wl6FKEhjtPPQN-ZFbwhNuZtcPhT-W3FN84ItWXrTjVT4sxUtEqdkgppYo2q1voSl0IacYjhNzITGmLXIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی یک باشگاه دیگر هم خرید؛
باشگاه الدنسه اسپانیا اعلام کرد که لیونل مسی، مالک جدید این باشگاه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/694666" target="_blank">📅 22:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtm0AgHYdkJti6FgN_PAGhM_TJUHytCdeeVaFxqa2Jr1He8WY7s0tlaQcKAro3hDkSoxVw2JkVOS9waDIFpq13xxrrj9_jmzDekXJrmy5iYsnsffYxxiySzAWqDBbhdQvjg3d4rqlstZgl9f6DK3eIXvbMAwDdwgiBmfBICFx_ALRx3JLzhnqd1yH5x4yi_qrw4WJc5dGyvmM5L08hCty6oyyJIFntNfgY7TLbb_b6-5Y0HpLVtvyEHLf-SYKcYXWR8TETWH_qLh9rOpGpfjnD8yZgxQUF0vrPcjOJ1ZXGevra0wdO1VgRtu_ITKjdic7zqW_yQO1rwVtDyQ2Huu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: جرد کوشنر در حالی مذاکره‌کننده کلیدی صلح خاورمیانه بود، شرکت سرمایه‌گذاری او بزرگ‌ترین سهم را در یکی از بزرگ‌ترین تولیدکنندگان تسلیحات اسرائیل داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/694665" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXaTCe10FGi5BGz1BkawHSsB0hWDWZqQkP4kmEm4WrvngTr5pOJypRuielZc1wlwCIn8y9j2E3kUSQMZIrmbPMBZ3LxXBRRnAT3xg23Zq_7HqQhUjjaeAx5zgSWooxz-6_lcPGKw8Udd0_DnTcWgZ2Kf03FPOezpCDvG0a4j268o3xDGs1R6En9k0OxdI80vS6oip8fHzlYmQO_8TgiCX_zkFbewny1JUTTm3eMorPRfdQN3KRWZWHzqqdbWJzYnECCZhape-qgJzQlwe_U-IaoxkyYk0p-N4KQvOT1Cf5tlaarPCID0_XbiW1tLqmpwLg8scfd7e1VqePWikDzk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDJD4GpFjHtMPkX798GD0N7FHAjWL-foEMa1Gamb4VWV21HVBaGekcTH2nR7S0A6or7xfJ_jLtKq1Mg3Zxg7mNSNGl7fg9aE02yKP9U2d3Bx3yNknkfCyO_nW3G3sGMRZuxA0FaZZ9GAXtxVk9Aq-rgn5RiJnWb4jMx1QsmpETe3V1diTBLAOxCfqnBtXzSEl8x_6qPOOhu2wob4cMwnq5aBpQ_uBrBAkMfqtIjY__EMEOZyLzQ_vK1sO431E9EFlqp7MDZYP-J0ZV2bChG8gc6CBrL3l3gDTmVCk3netKOd2t81OsGjU-j0P66FAgoNWAbAdKdE2nK32F3S7thQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند سبک برای طراحی پوستر با هوش مصنوعی
🎨
🔥
با اضافه‌کردن نام سبک‌های بصری به پرامپت، می‌توان ظاهر و حال‌وهوای پوستر را تغییر داد؛ از جمله: • Skeuomorphism: شبیه‌سازی ظاهر اشیای واقعی • Neumorphism: نرم، برجسته و سایه‌محور • Glassmorphism: شیشه‌ای و شفاف…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/694663" target="_blank">📅 22:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvT-Fmf0Qa5Vg1M6Z9Iy3yix7L-mkdPWEz9ywOoCuF4euKM97d4D9vwoAhiqupbCmjFgHLTVv1Stu8mF-0YlCxh7I3OgtMmWXpspudQe8Gh2TPw7tRCXaeVXydSvpZOwlXzDEEkCcfBqToElSIWnh2n2uEXxfa_oHUB1qn8njuffWjUINt2B9-dTJKtlNE33h3NZL_QnztkPAPyLP5j5E-aR4C_Wve9PPzJURzsInO4i2gjmvC9Sv9OA9N90r3GGXUX3yQ1D2hCWguXFFvboNFQOanIKUquN-2h7lY2i2TAchtXP3_GYJBNlyr7hI3bxr8z_Q9Txr1Q6dkszltCokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/694662" target="_blank">📅 22:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ترامپ اخیراً به دستیاران خود گفته انتظار دارد بمباران ایران در ماه نوامبر از سر گرفته شود
وال استریت ژورنال مدعی شد:
🔹
ترامپ در حال بررسی ازسرگیری حملات هوایی علیه ایران پس از انتخابات میان‌دوره‌ای است و اخیراً به دستیارانش گفته انتظار دارد بمباران ایران در ماه نوامبر از سر گرفته شود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/694661" target="_blank">📅 22:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290673400.mp4?token=VtKnn137WaAxrT5Ypb0HdYNIkDsCMTS26bPHi92fVzqqm2pLutrT1kECJQf8SM_Kd7f5l33-ECtDnRm_tjzCdr7yROTw3Zep--oomRApoV44VzpnKQbtgnUWFYQYVTDS0-bR3gyQLN9yz1tdgVDnH600UbqXEVbx4K6EeMbzgZ_9FPX4nMfIZfbQYxMpZ9TAKBRpZcgoWlFxGk0kSD1agExMXrjVPoHFFOH3FkwUObU8druDKQd9v3vdzizFL0STfyiKHmIaaLA9obfjB98UU0CQjnOPmKiQtFtEoes9G8rGwKjRy_UKKEPmLMU_MGdOoEPx1950-yVjDdSA7CgFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290673400.mp4?token=VtKnn137WaAxrT5Ypb0HdYNIkDsCMTS26bPHi92fVzqqm2pLutrT1kECJQf8SM_Kd7f5l33-ECtDnRm_tjzCdr7yROTw3Zep--oomRApoV44VzpnKQbtgnUWFYQYVTDS0-bR3gyQLN9yz1tdgVDnH600UbqXEVbx4K6EeMbzgZ_9FPX4nMfIZfbQYxMpZ9TAKBRpZcgoWlFxGk0kSD1agExMXrjVPoHFFOH3FkwUObU8druDKQd9v3vdzizFL0STfyiKHmIaaLA9obfjB98UU0CQjnOPmKiQtFtEoes9G8rGwKjRy_UKKEPmLMU_MGdOoEPx1950-yVjDdSA7CgFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با پیشرفت هوش‌‌مصنوعی، حضور و غیاب در مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/694660" target="_blank">📅 21:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573d27db24.mp4?token=lHQ9CFtPgvV8Zlf5_piXLHa9-vcVTTuIjqeeE7xGuSyFR7TqLyJrExn2hbgUGWVEez-cKnc9Mi6tm4DA-Hjm6pC19RaCrwNRAjptDyHxDleggsf7KAqdxqU9stLygiJPmRjfLPQQkpuIiRrzMW5Njtf6qeb4vrdSM3pnpfV0wGhfMxFrw6FK4IeYqrUBq6d-HzpS8wL45j5R91hdy2Nx0vQj4JpyOLgeH3VE1vQOky8OLyDjnp45Ucbm9Sr7xpJ5UwmjFOeTCL7poCgCHQvRPcy8467MyQB9Ve06WL10wv9tNiPiHLg3AotRush00B8jxfCCxHrEh-gprJ0dZmaDFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573d27db24.mp4?token=lHQ9CFtPgvV8Zlf5_piXLHa9-vcVTTuIjqeeE7xGuSyFR7TqLyJrExn2hbgUGWVEez-cKnc9Mi6tm4DA-Hjm6pC19RaCrwNRAjptDyHxDleggsf7KAqdxqU9stLygiJPmRjfLPQQkpuIiRrzMW5Njtf6qeb4vrdSM3pnpfV0wGhfMxFrw6FK4IeYqrUBq6d-HzpS8wL45j5R91hdy2Nx0vQj4JpyOLgeH3VE1vQOky8OLyDjnp45Ucbm9Sr7xpJ5UwmjFOeTCL7poCgCHQvRPcy8467MyQB9Ve06WL10wv9tNiPiHLg3AotRush00B8jxfCCxHrEh-gprJ0dZmaDFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمرت درد می‌کنه؟ چند حرکت ساده‌ای که فشار روی عصب‌ها رو کم می‌کنه و کمک می‌کنه راحت‌تر راه بری  فقط روزی ۱۰ دقیقه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/694659" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_6sIUFxQfGYKMGw1c9ywuadDpPQ1lDuzyGuYZqc-TTuwWr-if4FEuJ5Kd9zZsux8y6QMaBuUC74z9jGvY2KacWMXyMRgpiuWKp7wOOAkVwHT9q3JI4Vv6PEvqKvYYC_4ZvkYW73i3Fx_rVmPQAx_ex29BNYqWMTAOffZfDWwOSFG963JC8twjVvRbK0v2LDXI9qkrBFvg_1_3byqy9_mah4y_kKR7mJWAcCST8fKBxr0UVRf7_X3TIh8P4fkOPuTPsDBqKEjqlUTnKZZCBVdguE4_TU5zgC8TVluHn6xPonWwi4cKAmtFGFV5WjPXsyj1Z9FtEsG6x9rmvzd6Ecvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نحوه دریافت فیزیکی طلا از طلاین
🔹
طلای خریداری‌شده در طلاین، علاوه بر نگهداری در حساب کاربری، امکان دریافت به‌صورت فیزیکی را نیز دارد.
🔹
برای دریافت فیزیکی، درخواست از طریق اپلیکیشن ثبت می‌شود و پس از آن هماهنگی‌های لازم با پشتیبانی طلاین انجام خواهد شد.
🔹
تحویل طلا در مراکز طلاین در ۱۸ استان و پس از احراز هویت و ارائه مدرک شناسایی انجام می‌شود.
🔹
جزئیات مراحل و مراکز تحویل را در اینفوگرافی ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694658" target="_blank">📅 21:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f9fe8f16.mp4?token=ZMD1SHa2UfWJQTSePWQCjhFdR7YRDUbnch31-VIdlgYeZtv3N_roeoOLPYtzl4BdF0Whvf5jcZ_gqmjoTxApkxqcWY2N1rzoltTjJ0ocwTcRrr1q7exxeiR1EV5q_Uh3Ohl0l1OJkyTLWteJaoF0j9rjECwl3Zvh1M5PGYNdn1Oj9xGjt4P_JlISWv6jFvYLewO5MHzTO5SqcB1QHcXnsA0iX-tTZwtDNeSpGS_KHIqSv6SDk6XVy5cuqL5Gor67pU27rmEq_4mpskA4TvAoT9NbWUGcWaPIxJIK-JkzpIHKzUpaRtZp1QbuCOV47jz82Xsqp-c8mlqSkwZ3FEJJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f9fe8f16.mp4?token=ZMD1SHa2UfWJQTSePWQCjhFdR7YRDUbnch31-VIdlgYeZtv3N_roeoOLPYtzl4BdF0Whvf5jcZ_gqmjoTxApkxqcWY2N1rzoltTjJ0ocwTcRrr1q7exxeiR1EV5q_Uh3Ohl0l1OJkyTLWteJaoF0j9rjECwl3Zvh1M5PGYNdn1Oj9xGjt4P_JlISWv6jFvYLewO5MHzTO5SqcB1QHcXnsA0iX-tTZwtDNeSpGS_KHIqSv6SDk6XVy5cuqL5Gor67pU27rmEq_4mpskA4TvAoT9NbWUGcWaPIxJIK-JkzpIHKzUpaRtZp1QbuCOV47jz82Xsqp-c8mlqSkwZ3FEJJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسر شریعتمداری خواننده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/694657" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OZnHcPhE0bd2e4-6UHhTvp_VnV1H6Zd6t9c-E1DJ1QFiHBudX8j2IcB66Vh1yi1iim6IHqREubPGxY1MNXCr3qoszoOwSz9N-kwVoo30oCE239q6J1iKKDluF8w28QcZfqW2DODBuJCNiEB_YL4_kGAbwP1iyM1fOwV_r2mFAftEw0ZYdd8jQ8RXUZhFuS8SgoCmK1HhlKejrOtnNMh-hVNzqcrOf-BV6QAB6jPTHl3dguXZM7ubSX4PnXXDUDcfOOHq4Hz2vWyLnU1L9kmiPY2DFQnOBiy4gMHRjfOeseH_sNMpOD-UDWY14EjNN15Uq2wg9YDbMAu7ZxdNg-Si2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: تهدید هسته‌ای ایران را در یک شب از بین بردم!
پست جدید ترامپ:
🔹
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/694656" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=rYdspV7qe12HotknqS8MAEJBqZiJKwcfCDDDEWnIKgEGsagR1UYoAr8Er8drBidIGLuf4Qn0oYT-bnfeYFhMXXqOD8ZXF0pMhAQYXNOAM2VpsqA8xy5QK-pYT-NdwkM3Njcs4rs8wsEFS9UonWmXKg1sLMdY2PIi8UaZaDTAKvp3BekthgGckDBuITU3pMMdhuPfSEHUe-pHSU9vM8pVrmgNCE-kMImt3tSSUQw24nW0f5_LypeHpR0p2ce5U1AIC0p7aqcoQ2SNNGjaeiqul_Zlu-bnS8gHeDe93k7xR05j0X8MhxYInzN7IgUU0rGvTZJCst_FCtgTINpaxGRaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=rYdspV7qe12HotknqS8MAEJBqZiJKwcfCDDDEWnIKgEGsagR1UYoAr8Er8drBidIGLuf4Qn0oYT-bnfeYFhMXXqOD8ZXF0pMhAQYXNOAM2VpsqA8xy5QK-pYT-NdwkM3Njcs4rs8wsEFS9UonWmXKg1sLMdY2PIi8UaZaDTAKvp3BekthgGckDBuITU3pMMdhuPfSEHUe-pHSU9vM8pVrmgNCE-kMImt3tSSUQw24nW0f5_LypeHpR0p2ce5U1AIC0p7aqcoQ2SNNGjaeiqul_Zlu-bnS8gHeDe93k7xR05j0X8MhxYInzN7IgUU0rGvTZJCst_FCtgTINpaxGRaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما خواستار محاکمه محسن نامجو و بیژن مرتضوی شد که به کشور برگشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/694655" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e05ef7c7fa.mp4?token=XoL2YtOG6r6dtbBbabDPFCQw-HZQO-Fdn7xHxWanY3-dsW_fPM_RqHUIBUZgbCVbA8KaCci7VLRKXlu30eEv6vuEILpYbu4r5cPraJgcnymx6SokDZ7hshTN-baVioHMfG8KywQWWTZX1BVUTc5aZBDTjz8IvYu7pxxZyMQrqpt3YARhdYBxcpaWR8C9qmNej55psG7HulBHJf5fC2ETKUQ9PBGJ0VN5im3Wdze3gC3f6PAQQZJ-u3R-m1HkudJjiqcatxSpMs1LsCt4b0qc2VSM6fvM7rQntFx1LIK2g-IiY_Qdru_8tkQxRmwRzcgYIsvKhsSt6WSm-TmTN3txfE9n1eC94UPQotljYc0RU9w1WqvJFv-WiWTsUQA4SFxUVstMXcKgoBUQQm-kBvm6yTuNpEbS53LRcl8h4UKXsywoIcWLfKZs69zrDskv888NqLv8e5ZbIz0hjd5zFXnS1vCMbBmdjSTgFbAI_WAWiaoPH7lkPYWo7hDK2TCx9UKaTCR0D8cKuC8x4qpQGStGHX0tB3yMMAH1lSDAZ4u_WtDP15qylaVCHY_4sXt1i-Nh8LQHBHk-Qw__kySFEcI_HcYiC735wCBfMRuloxI8-a2gc3RV2JhHBh6mM_Flb-ao_w2uqzt6HGyK8hASFGymiSsuhjih62DtlMqoCocKpdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e05ef7c7fa.mp4?token=XoL2YtOG6r6dtbBbabDPFCQw-HZQO-Fdn7xHxWanY3-dsW_fPM_RqHUIBUZgbCVbA8KaCci7VLRKXlu30eEv6vuEILpYbu4r5cPraJgcnymx6SokDZ7hshTN-baVioHMfG8KywQWWTZX1BVUTc5aZBDTjz8IvYu7pxxZyMQrqpt3YARhdYBxcpaWR8C9qmNej55psG7HulBHJf5fC2ETKUQ9PBGJ0VN5im3Wdze3gC3f6PAQQZJ-u3R-m1HkudJjiqcatxSpMs1LsCt4b0qc2VSM6fvM7rQntFx1LIK2g-IiY_Qdru_8tkQxRmwRzcgYIsvKhsSt6WSm-TmTN3txfE9n1eC94UPQotljYc0RU9w1WqvJFv-WiWTsUQA4SFxUVstMXcKgoBUQQm-kBvm6yTuNpEbS53LRcl8h4UKXsywoIcWLfKZs69zrDskv888NqLv8e5ZbIz0hjd5zFXnS1vCMbBmdjSTgFbAI_WAWiaoPH7lkPYWo7hDK2TCx9UKaTCR0D8cKuC8x4qpQGStGHX0tB3yMMAH1lSDAZ4u_WtDP15qylaVCHY_4sXt1i-Nh8LQHBHk-Qw__kySFEcI_HcYiC735wCBfMRuloxI8-a2gc3RV2JhHBh6mM_Flb-ao_w2uqzt6HGyK8hASFGymiSsuhjih62DtlMqoCocKpdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت Figure ربات‌های F.02 را در کوره‌ای با ۷۵ تن فولاد مذاب در فنلاند نابود کرد. آرنولد ستاره ترمیناتور، حمایت کرد و در ویدیو حاضر بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/694654" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c654b44b2b.mp4?token=OLp8DVr_EuEicbKFVchGbb9g30PcNOSQslcXTyBPoa_eow2KIcFoiNnU085JNTsyP__M3Gb1k_ILy_00US9wpM8HGbAFHmuxZEV7_ZUxJdgao0bB98QNVWDvXJCIKjkfABiWfEyZPZERArWP76t42kRM5s8M1zhO-Iccvstg0Hhm9K4YtVXH1Hj4ZlOfT_9ZZGe4dt5VW94Tt4wM3eghMXa6LuFtFK_RF4WXn1CkRrOuT7k-IJqpdT5zj22tCQZiv3vKsFQQinGKKQPtEATowRhatxHKSapvjdRbzhy5l_VM779FLLQDLbe9iOUwS7VSLNcQ_RYmBlBNSNHkH6LRTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c654b44b2b.mp4?token=OLp8DVr_EuEicbKFVchGbb9g30PcNOSQslcXTyBPoa_eow2KIcFoiNnU085JNTsyP__M3Gb1k_ILy_00US9wpM8HGbAFHmuxZEV7_ZUxJdgao0bB98QNVWDvXJCIKjkfABiWfEyZPZERArWP76t42kRM5s8M1zhO-Iccvstg0Hhm9K4YtVXH1Hj4ZlOfT_9ZZGe4dt5VW94Tt4wM3eghMXa6LuFtFK_RF4WXn1CkRrOuT7k-IJqpdT5zj22tCQZiv3vKsFQQinGKKQPtEATowRhatxHKSapvjdRbzhy5l_VM779FLLQDLbe9iOUwS7VSLNcQ_RYmBlBNSNHkH6LRTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه این ترفندهای کامپیوتر عالیه و حتماً خیلی زندگیتونو راحت می‌کنه، حتماً ببینین
💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/694653" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg2PTf5_cZKLaNWyJsds-TEPcvKSbalBRp8LIz5MwBHDzHQsDrS07metOxobBWIO0QEYe2QJmn3fZXnTG4S5n5CfdJY1ftlLqGmOh8PVGhwergEmZO-wClLGKZo51mBKjfR9hRwqJXGSbDrYyTPk6bsw6Hr9RZxkqCaZMceCO9iPHD1xLpQ42Er9q_2UqTIl_ia5nbxNlMtLHmcB19lbjSeDkt4tX2A7FtiSDOhHAMJOp_zZYbY_Nr1zHVK6mDbQV7pzRDfzpBVd4khAMOkMJFcMVaMUc7Pff0gI_DspD66X8x1airQug7fMYR23azPXV-vPCl3c7JvjHqEzMn4oTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
آغاز فروش ارز در ۶۰ شعبه منتخب بانک صادرات ایران از ۱۱ مهرماه
⚛
بر اساس دستورالعمل ابلاغی بانک مرکزی جمهوری اسلامی ایران، فروش ارز در چارچوب مدیریت بازار ارز در ۶۰ شعبه منتخب بانک صادرات ایران در سراسر کشور از روز شنبه یازدهم مهر ماه  آغاز می‌گردد.
💵
بر اساس این دستور العمل کلیه اشخاص بالای ۱۸ سال مجازند یک بار در سال تا سقف ۱۰،۰۰۰ دلار (ده هزار دلار) نسبت به خرید ارز اقدام نمایند.
⭕️
لازم به ذکر است بر اساس دستور العمل یادشده خرید ارز در قالب یادشده مانع از خرید ارز اشخاص در سایر سرفصل‌ها اعم از ارز مسافرتی، ارز نیازهای ضروری و... نمی‌گردد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#ارز
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/694652" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBsLA0jaD5axnjN1a1SuCF0hOFhbc9uP5D7cyDC0Op5YJcGb6oEDd_2srYEi1j33kxdRmp1b94Eeo14z8NL6tSz1tMUoFPX8w_Sc138I-PQfsG1QSYLgquO2vEkcdkLu4s7zMAhRvEV4a__b5VdSrcWntfSfwOiO_Jp4mAFtpcmK5t58Kq1sTDE6O6ox02Ul8NSRVjUtZsCzIP5XL7vQA5jn7SGqDHs-aJsD-z8T09JJA6zDFaXKgKUyujBltzVXs9rQCcKa_aV8n_ZYfqXZTi2mJBZJJ47xFdJOXOBReWPizYuGYSyHdj_pT8DlQs0a32frlAQuSjRXjwsfi3gIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پیشروی نیروهای یمنی در جنوب تعز
🔹
نیروهای مسلح یمن در جبهه‌های جنوبی تعز پیشروی کرده و نیروهای وابسته به عربستان از این مناطق گریخته‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/694651" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پوتین: کل جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/694650" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFjvgI8m3yfU_2ePTkSorqAN0HYT0ASerCRCP6ptbA_wIFRMer6owBhyvDk60b7ISGd8hRfXHJVX3EwCgPVOLlmusz79KQ0ZOKxQHg9-7PDFhWo-QojXAB9Ghc1u2xJ5Y123ZrqgXCXKAnEe_B0rurBZh1KD3kQ8-MXlIA-bzZz0Lb042zRoFpi1Xum2c0hjay_QJfymsRe0KqGqEh_J8ULKdjXa_aiYSs9GYGRvYvgpFg_rECa8l9o2z648zMNdzYf5_fsOaYjP47ZE2r0RL00plV4qmrmSDhZ-WYV7LcMfy_49WW5T6gMJxqUUWECpkE2GqLwwUaqh6_JUrUrzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های کمبود مواد معدنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/694649" target="_blank">📅 21:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=IUgVoS1cHEF8Em2Xkb_v2lgk4_dQRr442UhvnUTMVGRYtWg9qfJbTlbNZOpgNKeWn1LSiZ4bkvl-ZNGnM9dHzHvlh6Jndr7mM6_QTubriMl9PYO1JjhlpX7mMKMVn15fL23v7nJZInvtnpFjZLJjUouZE6_3DUoKXvix_BBQJyyJfTSP1yCZC7VTUOR3NtBvGPPHAXMC88nj7Y7Z8AZiNYbcCBJiGORKwIv3i7a_cEOEa_rps4dfzKkKh1w-Ijyhtr3URQr3fN9x4rrV86lmTvYhJBoyrJS-LZT3QhK0H7nCW00_saYZpFICGCU90wCXlgqbGqGj1913-vqKlCVhJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=IUgVoS1cHEF8Em2Xkb_v2lgk4_dQRr442UhvnUTMVGRYtWg9qfJbTlbNZOpgNKeWn1LSiZ4bkvl-ZNGnM9dHzHvlh6Jndr7mM6_QTubriMl9PYO1JjhlpX7mMKMVn15fL23v7nJZInvtnpFjZLJjUouZE6_3DUoKXvix_BBQJyyJfTSP1yCZC7VTUOR3NtBvGPPHAXMC88nj7Y7Z8AZiNYbcCBJiGORKwIv3i7a_cEOEa_rps4dfzKkKh1w-Ijyhtr3URQr3fN9x4rrV86lmTvYhJBoyrJS-LZT3QhK0H7nCW00_saYZpFICGCU90wCXlgqbGqGj1913-vqKlCVhJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلی برای اولین‌بار تصاویر بخشی از ذخایر طلای خود را منتشر کرد
🔹
صفحه رسمی پلتفرم میلی با انتشار این فیلم نوشت: این بخشی از طلای میلی است که از بانک کارگشایی تحویل گرفتیم و با دریافت آن، تسویه‌ها سرعت گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/694648" target="_blank">📅 21:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518f939343.mp4?token=qpjiYYQg9N_X-qngZi9k4-HunFCpjPl-TyG8axkIWF6x7UbUBgayO6pZqjrr-lBgbprcSkrcs0zmhGfzAkyb2sPPWPuaxMOPNvmwR5oRyksR5dKswu85ker5eEwPX8MlY_5f4A_a18knhJkfy0gWyBHOLxzFjXYVDzPUGvWB9HEATAJBmuVI5tGp12h8Y2_HVchXggMHxNlRdZ9sPTVS9BOQcDMstL4R0scaO11qMg2nuncdx9P-FhOJg4a7iIeEdRLzROhwp32HKGeJjG6Zb0UoOi0EwWImiQsBMEowAR64BZE-XB0R9mwpvKXkV4P1htc1x6vb57TcfuVlSQeeUAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518f939343.mp4?token=qpjiYYQg9N_X-qngZi9k4-HunFCpjPl-TyG8axkIWF6x7UbUBgayO6pZqjrr-lBgbprcSkrcs0zmhGfzAkyb2sPPWPuaxMOPNvmwR5oRyksR5dKswu85ker5eEwPX8MlY_5f4A_a18knhJkfy0gWyBHOLxzFjXYVDzPUGvWB9HEATAJBmuVI5tGp12h8Y2_HVchXggMHxNlRdZ9sPTVS9BOQcDMstL4R0scaO11qMg2nuncdx9P-FhOJg4a7iIeEdRLzROhwp32HKGeJjG6Zb0UoOi0EwWImiQsBMEowAR64BZE-XB0R9mwpvKXkV4P1htc1x6vb57TcfuVlSQeeUAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: کل جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/694647" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
خبرنگار: آیا رویداد مربوط به پایگاه نیروی هوایی سلطنتی بریتانیا در فیرفورد ارتباطی با ایران دارد؟
🔹
ادعای ترامپ: ممکن است داشته باشد، اما باید بگویم که از اینکه آن‌ها این موضوع را علنی کردند، تعجب کردم. من این کار را نمی‌کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/694646" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8yv3t0y6NCw3jZlNWupyvh_JKzg9bEcRIC6SYDubENnBcL0ah2wxOZ4jryDhw2TFzWeITOzotdbeRKkLVmYguRA-zoCkPSAdQBKS_uIk7eB0WV4nOCPV3gjMt9juOcLNbMItsEQaQVCKlTFIL1eOS2KejGcexD8W7FsjFe0be8emv5IC15wXs68nOTDw-uCjmkT7u3e84mOF-YSWj-srGqp1rSHrGXP7nAxDuExTkLkuSJ2K_Xe4cBrq7FrIPcOTAmLkIN3UanYRy5CpMxTaqQUHHxY1eZWBVsBwsOsdrf3t8BKanO3f4zHNwewEZPkac4CGrXoFb27f33QvmU4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ تورم مصرف‌کننده در شهریورماه ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/694645" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/694644" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbzkBflwwfiao4PnZuX5i3fHyjJ_K1zG4ubWdpGcHkknWGptH32Z-Pkee_IK1XI8hBdZKIfFcUZWdj_qDvBiMtGxn_BxqQnd5Z4Kguo0EHeNBUdVQUFnG1tBGYN9yA28RpROLr3BGVPUg9Bp5eaSiAWB6nkil8Ig1JBZZq3ixD5_MXJTESRCgFwVPtC2a8SRCIwI1YIrNLNuoSgNUjs_1kd3bNN9KdR74YyN5AyVDpFq4Y6MMjjYtp5JPoJzR8VFOEmsWe_56YeApuVq8nT3i7N84u5dCL-LaATXKRXpErtJ5ogKpsosXHagqscRs-m4XMYAT0fzrzjP2M0eH-efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ ترفند برای کم کردن کالری غذاها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/694643" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223c1228bc.mp4?token=kalAThkEG10LM7Ot6q001H99Sv0Un6kcaSaVQKLGRu3V4wkCTQ4-5jFdCr-jV-2J4uBqTfb_mWtN3O9OTZK0_542XLmmnQd5SXf6wDicKsT6fAwrOUPmL-ji27xW6hG9ac4ZdP4UsoJUxhajDvzZTr7KG6fBx6H6A1_gvrT6oL5fd73fRgtAx6aYrl9bRdWP5Ndc2VV2Pzb16d9YJPdw1AWYU0oelSJmuVyLRNEnyecOxEiAaR9oNp9T0F4wbD5AseSMW83KmsrCteg-w9XlcXbghDWtqGy9Uu-X64hS5Ju_9jvBmutMmjkbakmaevkaMDT4opC2FIX8N_DMnSoK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223c1228bc.mp4?token=kalAThkEG10LM7Ot6q001H99Sv0Un6kcaSaVQKLGRu3V4wkCTQ4-5jFdCr-jV-2J4uBqTfb_mWtN3O9OTZK0_542XLmmnQd5SXf6wDicKsT6fAwrOUPmL-ji27xW6hG9ac4ZdP4UsoJUxhajDvzZTr7KG6fBx6H6A1_gvrT6oL5fd73fRgtAx6aYrl9bRdWP5Ndc2VV2Pzb16d9YJPdw1AWYU0oelSJmuVyLRNEnyecOxEiAaR9oNp9T0F4wbD5AseSMW83KmsrCteg-w9XlcXbghDWtqGy9Uu-X64hS5Ju_9jvBmutMmjkbakmaevkaMDT4opC2FIX8N_DMnSoK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: آمریکا با ترور افراد باهوشی چون آقای لاریجانی، موجب سخت‌تر شدن موضع ایران نسبت به مذاکرات هسته‌ای شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/694642" target="_blank">📅 20:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ایران موافقت کرده که سلاح هسته‌ای نداشته باشد
🔹
موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/694641" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyN0czwS2AQM7alCa1OAPpZsfLaCNOx1fcc3lsrDWXtQj-jVgdfN16NxGLz16VbqWdGvP2-AEBBvgBIAKEAh0Ut7a-Xb0lH9IAaNBLS5IrSZjNEJhZN5wXFFitro79C2W-N_D1x66vrOISyAawt72cswHPqE3R1DRJW2BFlW59OZTVpw64rG2v_2j905mAJ2wzikWIXzntQwpEjUyQ0cIBilLkqKdiZY89orKVT16p59fPHvXVlMB9htoIxmIszapUr6eaXqID6cGlejogVYxbyaLcmZuq9xW4krbY8UWmD7DHL0aiaGtWTjcFYAuxWRJeM-DQlfiWq7I-KZR_JT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی رسمی از سامانه پیامکی هلدینگ رسانه‌ای خبرفوری
🔹
همزمان با یازدهمین سالگرد تاسیس هلدینگ خبرفوری، از "سامانه هوشمند پیامک خبری" به عنوان گامی نوین در مسیر اطلاع‌رسانی فراگیر رونمایی شد.
🔹
این خدمت راهبردی با هدف دسترسی بی‌وقفه مخاطبان به اخبار مهم…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694640" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c71ebc28.mp4?token=eBFgjcFV05pe-EJFqOXXpBiX5k2uhkd3PlyDiJUPeJx4Tlbw1cufB0pF9xFnZG7-LkVlD8PORdfWDGSDjEqwT31Wr6vk-cmBNLxBAbn28vvV8L_Pvub_Fs1y4i_VPRWW7scZo4td9vfqoIDbgRaOQwI7522CxIbyfJseVnqjo2uQ5MUI427wZnb7lAZWiDwogxBNLrtKb-GW63Of4BA9hUxHmeonTnlf2N8yYFRVkwRavFquzL6r8DOk7S5BwLkNY_a3wsM04dabYfFu4cV2RoO1IcPITcnsYGLUhWzwlRh_yCaG4SzFEyqVx6addQtIt_W6606azcmd7KrUiBH2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c71ebc28.mp4?token=eBFgjcFV05pe-EJFqOXXpBiX5k2uhkd3PlyDiJUPeJx4Tlbw1cufB0pF9xFnZG7-LkVlD8PORdfWDGSDjEqwT31Wr6vk-cmBNLxBAbn28vvV8L_Pvub_Fs1y4i_VPRWW7scZo4td9vfqoIDbgRaOQwI7522CxIbyfJseVnqjo2uQ5MUI427wZnb7lAZWiDwogxBNLrtKb-GW63Of4BA9hUxHmeonTnlf2N8yYFRVkwRavFquzL6r8DOk7S5BwLkNY_a3wsM04dabYfFu4cV2RoO1IcPITcnsYGLUhWzwlRh_yCaG4SzFEyqVx6addQtIt_W6606azcmd7KrUiBH2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: پیشنهادهای روسیه مبنی بر انتقال اورانیوم غنی‌شده از ایران به روسیه همچنان معتبر هستند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694639" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اعتراف ترامپ به کاهش ذخایر برخی مهمات زرادخانه پنتاگون   رئیس‌جمهور آمریکا:
🔹
ذخایر برخی انواع مهمات در زرادخانه‌های پنتاگون کاهش یافته است؛ واشنگتن تولید آنها را افزایش می‌دهد. ایالات متحده در حال ساخت چندین کارخانه برای تولید مهمات سامانه‌های «پاتریوت»…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/694638" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694637" target="_blank">📅 20:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">21-1 Ane Manaee (1404-02-08)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/694636" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ویکم؛ بخش اول
حجت‌الاسلام امینی‌خواه
🔹
چله‌ آفاقی و انفسی کلیمیه، میعاد چهل‌ روزه خدا با موسیِ درون انسان و دعوت به میقات قرب الهی [02:30]
🔹
عبور از حس‌گرایی و دستور توبه سخت برای قوم بنی‌اسراییل در داستان فتنه سامری!  [12:57]
🔹
"أُشْرِبُوا فِي قُلُوبِهِمُ الْعِجْلَ"، مبیّن اصل حکمتی- عرفانی "اتحاد محب با محبوب" [21:05]
🔹
آثار توجهات مداوم به معشوق در مجاورت چهل روزه و تبدیل شدن به تجلی او [25:11]
🔹
تفاوت رهبانیت در اسلامِ "ذوالعین" با یهودیتِ ملک محور و مسیحیتِ ملکوت محور! [29:05]
🔹
فلسفه عزلت‌های مقدس در قرآن، عزلت‌هایی که نه انزوا، بلکه آمادگی برای هِبه‌های الهی‌اند [36:31]
🔹
تعلق به مادیات، همان مصداق گوساله‌پرستی‌ست در دنیای مدرن! [43:49]
🔹
اتصال معنوی حضرت معصومه سلام الله‌علیها و امام رضا علیه‌السلام و ثواب زیارت حضرت معصومه سلام‌الله‌علیها[46:31]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/694636" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694635">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad74d45df.mp4?token=sdw7l06ObgbpCohNT1Y8y6UPviVp2jWj8VMCTFLP0YLfhB96B0eDkPmrOjhbVkcgU0uxAW6uJm-4oymGjWhI-2o44iKbvAJ8jknreI54esOi6RA6Uc0ZSS3RKVTr_ZxywUleTa1BzXc6Arg9fLZfkvAAos6uXaqpYyNW7oIybvfNdkJepdsd0SL_Q-CMLW97wbkkB1p4jKjAf_Du-d_BAjPUv2bpZzg8J_rDkfJzlE8jjtTfS2H8qw48sBzn_qWfYLb-Wy-nkwqRR4kyO7Z9ii3Lx8rkp3z0IumCqY_Hku4hyYzzqPnHKzIYIo8LQgmNDe8UCSkaatPQ0G2e6xPjOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad74d45df.mp4?token=sdw7l06ObgbpCohNT1Y8y6UPviVp2jWj8VMCTFLP0YLfhB96B0eDkPmrOjhbVkcgU0uxAW6uJm-4oymGjWhI-2o44iKbvAJ8jknreI54esOi6RA6Uc0ZSS3RKVTr_ZxywUleTa1BzXc6Arg9fLZfkvAAos6uXaqpYyNW7oIybvfNdkJepdsd0SL_Q-CMLW97wbkkB1p4jKjAf_Du-d_BAjPUv2bpZzg8J_rDkfJzlE8jjtTfS2H8qw48sBzn_qWfYLb-Wy-nkwqRR4kyO7Z9ii3Lx8rkp3z0IumCqY_Hku4hyYzzqPnHKzIYIo8LQgmNDe8UCSkaatPQ0G2e6xPjOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: پیشنهادهای روسیه مبنی بر انتقال اورانیوم غنی‌شده از ایران به روسیه همچنان معتبر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/694635" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=OxHJjmMBf_QVJjCNJkPCuzFwqHd39hd8NnaCLMJtfiIU6zW-6Vi2klQNsIWtKgxZTmuhqPYM2QUoQu5DhgZ3un3ak5BYNcZFU9aueILqHe9xkgeY_sCTVJ0JnIgdD-zWqpSxHxn8j8Ml1A2n9oXR0coYBNm2WS1kshtzt49839NOF_ZS_OVvjlz678z-CM_tSx-jZnNPoQ4zE9AbixcL9AiyDVkp-T065mDKZaHAvM3alGtM7YCQTL72xZ8QDdebaghOcp0LYW0BlhOy-gKI7x_invV95DH-jyUAVEoixW2AvG5stY1bHIYJaaShHjsgdLnR5TOCwvyy7sfUTrSyqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=OxHJjmMBf_QVJjCNJkPCuzFwqHd39hd8NnaCLMJtfiIU6zW-6Vi2klQNsIWtKgxZTmuhqPYM2QUoQu5DhgZ3un3ak5BYNcZFU9aueILqHe9xkgeY_sCTVJ0JnIgdD-zWqpSxHxn8j8Ml1A2n9oXR0coYBNm2WS1kshtzt49839NOF_ZS_OVvjlz678z-CM_tSx-jZnNPoQ4zE9AbixcL9AiyDVkp-T065mDKZaHAvM3alGtM7YCQTL72xZ8QDdebaghOcp0LYW0BlhOy-gKI7x_invV95DH-jyUAVEoixW2AvG5stY1bHIYJaaShHjsgdLnR5TOCwvyy7sfUTrSyqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694633" target="_blank">📅 20:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be03a96892.mp4?token=XP2MBkrhcCNmZ3oi4GwlLpsYUpItfAaaSUykkwiEOeuefzcgnG04qVJVpO0mb04G-UzPqupZ7Xgp8HwexJHiOwxaCtcadB6IgG79DR59AF05quIXAk_0mIFg3mujXzREAnK3w-03tvjJ1ybJj-AqEIGAuBbKbnmSuO1xk4XD3JKd7EkIE3e_mjAuwq4aLatu7AdUA5Atz0tVpC1SjtHabp5Vjx-G8ZmjzQkpFfXGS6j79jLnNRMf1unroN6jkbO6a3ApWI2oSxG60bqTDnNJofiymlN9jPgDvOmXOxAamCWIDW6VZN7PKWcxb8bFGabbsJqmAXRlv_UYKWavUw0zBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be03a96892.mp4?token=XP2MBkrhcCNmZ3oi4GwlLpsYUpItfAaaSUykkwiEOeuefzcgnG04qVJVpO0mb04G-UzPqupZ7Xgp8HwexJHiOwxaCtcadB6IgG79DR59AF05quIXAk_0mIFg3mujXzREAnK3w-03tvjJ1ybJj-AqEIGAuBbKbnmSuO1xk4XD3JKd7EkIE3e_mjAuwq4aLatu7AdUA5Atz0tVpC1SjtHabp5Vjx-G8ZmjzQkpFfXGS6j79jLnNRMf1unroN6jkbO6a3ApWI2oSxG60bqTDnNJofiymlN9jPgDvOmXOxAamCWIDW6VZN7PKWcxb8bFGabbsJqmAXRlv_UYKWavUw0zBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شمارش معکوس پایان جشنواره «چرم مَنطِـ»
𝟲𝟬% و %𝟳𝟬 تخفیف برای «تمامی محصولات»
➕
𝟭,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه
خرید حضوری و آنلاین با اسنپ‌پی
کد: 𝗣𝗔𝗬𝗖𝗪𝗚𝗭𝟱
👇
🌐
manteofficial.com
فقط تا جمعه شب
‼️</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/694632" target="_blank">📅 20:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb078f63b2.mp4?token=b6g9IT94FHhjgfeGArrzPR1T1amRqnA2pNha20-scGhL4nCh_LKWzNG7yhQDSad8_BMRJF71k0tNarLtWptZh6zQDSA6nKJgwRyvU23ljb9K-Vga5VG6u1iNk4yk5HnBrWNRlGExJFjIERu2MRAKigqRZNOEJTVPq3TjD8QKZSQPjfNK9dOjF8NMgyikLnjKhsyyOYQR9JU_ISG9whsu79vOnFig_t3-Btv3Cb0XADmH_0CvzDXgd5dJqH7EtX5PCi2b2a1bJ3N6CBg-ckP8CJ_ogMMcK8NdHuQ_TdhkExYxX9KNmUuwegVZS_R50oDnskNi5MZl0PQZdxwARJY_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb078f63b2.mp4?token=b6g9IT94FHhjgfeGArrzPR1T1amRqnA2pNha20-scGhL4nCh_LKWzNG7yhQDSad8_BMRJF71k0tNarLtWptZh6zQDSA6nKJgwRyvU23ljb9K-Vga5VG6u1iNk4yk5HnBrWNRlGExJFjIERu2MRAKigqRZNOEJTVPq3TjD8QKZSQPjfNK9dOjF8NMgyikLnjKhsyyOYQR9JU_ISG9whsu79vOnFig_t3-Btv3Cb0XADmH_0CvzDXgd5dJqH7EtX5PCi2b2a1bJ3N6CBg-ckP8CJ_ogMMcK8NdHuQ_TdhkExYxX9KNmUuwegVZS_R50oDnskNi5MZl0PQZdxwARJY_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک رنگین‌کمانی ۳۶۰ درجه که در اطراف یک آبشار در چین ایجاد شده است
🌈
⛩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/694631" target="_blank">📅 19:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون آموزش: حقوق پایین و تبعیض در پرداخت‌ها، موجب افزایش استعفای فرهنگیان شده است
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
علت افزایش استعفای فرهنگیان که در فضای مجازی مشاهده می‌شود، حقوق کم معلمان است و اکثریت قریب به اتفاق معلمان با وجود مشکلات معیشتی که دارند، رسالت معلمی خود را به‌خوبی انجام می‌دهند.
🔹
حقوق فرهنگیان واقعاً پایین است و تبعیض در پرداخت‌ها موجب نارضایتی شده و  بر اساس قانون رتبه‌بندی معلمان، هر معلم باید حداقل ۸۰ درصد حقوق هم‌تراز خود در دانشگاه را دریافت کند، اما این قانون متأسفانه اجرا نشده است.
🔹
از دولت خواسته‌ایم لایحه نظام عادلانه پرداخت حقوق و دستمزد را به مجلس ارائه دهد، اما تاکنون مقاومت کردند و پیشنهاد مشخص ما این است که صاحبان رتبه‌های یک تا چهار، ۸۰ درصد حقوق هم‌تراز دانشگاهی خود را دریافت کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/694630" target="_blank">📅 19:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT_Gm5FiK7uqoCAT8cvYA_CnRMh06crGaD1bTctc2yEGOWMf3fTnLrz8ctvB0S9CkyA2IwriB1flXui10k2sD0PbB6PpPot8hBxz1GNfYAZwP2NBQNaeOv6kmuB4CrqgcyrISfsY7JAU6T7qsegyQTeQWz8vv2jEqHKr1lAtR0WfvBOd2eRiKBmrTJkYyHjS6zgfAaSnJ4i1HGuXLxAcqKey8xr3VAn0QYfg8RKM5pKPbFQW6G6tZqBliZGoeQe9iXk586fukSOhbiFIpy6IpesqKVBPLpNI9swHR2fKQu3QE-q7selBfzxuaEf-XQpSv-MwxyM0I_4Y_3ejUGpwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنگ روغن‌موتور خبر از حال و روز ماشینت می‌ده!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/694629" target="_blank">📅 19:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694624">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر_بورس(Reza Habibtamar)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1AmXmmMlnuv1pSyoutiG-30sujK6F-QJjKOsL_2TsS9B5WF9CAdcPJFqLPFOgkBlBu_T4JTAWr4yKQZK7ZdkbkWgMSFg2Cn60tnfKD7QSAjUNwUXSg3Fu8SWmzRPosMzF9xfF2E-xA1FekH63vNTp1Ao3mJOY23k3BSBjvXBUcdZ6-_PpbvqMVXMKuiLv3EVcd2KHz5Hse1S_agkJsOj10W7ZtcHE_J0cmsZifxp1Bf6mtnDThtU90ZGDwZo05C92XEBho4Y6czQeNbIo_p5k75LPC59lg8F0GFsDsSu8F2sSLE5M6RqHNQin3T_aSLsC0O27RkhnJLGTrO3tiF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRzEcgRRPn5deNz4c-kwP4GNp76wFR57rTidvCqLxVp6VO5aezxlYNcOibtONUAlJTlb_3wN6PiEUXWCFzrvZwI_2z8N7vbkHJY9LOH8pCYh46yUKxGClXPVPBZLBQ4GpbjjEt15qIgkwsyJlhqNJX5vOW7mITxrlSudyMgv3A-suCBmoBgIBz5lTPDJdjNeUnhdQUmTtEdrsh3367kCjYR0nn14exj6qxNQgKZyCqsG2irDIX84rw2KVkKDZ5yXrot0L7lndRSW-K_7ewwAJCNIMNaKmlQkuKKwJL9XAugs7NiRN-T09s1aGd3J8KTYuXSECzryxnZDyUhTeAxBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRoJXKzajWKCvU_MIT8CJhrEd7wJG8ai5qKyFRb_DK7yUip_O7nh27GzkzM6MgUOQdb13LNchNysUCcAYR1wF_valBuZy1DzF0ANUAD9wnh93rLGmPd1utC7-i_E5a9r9fY5VIp0hDDxX2_XgUvVbTpJW9OinHjwpvDD5dAIS7XBLRymi5UjTuBvCzeOIqC0Org1DSN6_FfR1QjwZ58QhcCt9dFqq_duKAnE536hIO5p90ZJjoCuzuWPfQjx5Kk7RkgHxHzAG2JcyVWBJhvfqI8oA4BbkPm-wQmU3jRWuqyzQOD6-dZYgiex6gfHbLzOL5VZp9EHspgsorqpdzDx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQL8_zRL3e-Of2yBoh4M34uzQA_IVB7Q6aD3-OI6lqEkl7Df8nyWDvI6k3vDlRcCEZMpytduB-L4oRB79f_PiYMq9rcT7yLH8bPe_oU-1RE4dnBDJj3kezh3IM9rPvPyt7WyDll1m_xiRonBUtEH9GcMy_iaTexgAliMTSjeyBX1zPjqtOcTSfSsdHvEK1WykvGVs46EyntcNSO9UB36CtR-HaCfII_tfQzacOlunh9O0G_cVjBnuOP89E2XuTIXqVjqqLonUZQwj0_keF3ZRPH8399JRsOZli50DxfGregwvx2a5cJVMZrcwKAnjFFTbv35QHCBnNIWRNOrqDJGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SS9BOdJTe8doITCjnXUvK1O_3S3E0YocTilb1RwCNmZJLER8RQm5WvJj35q2gCum5Ir7hV4hk0XP-bAD8CksyoNGiSiKSkMFzAJi8m6K3LUsa7OPLZ7NcbesIOQe2rmChwTMYjT11wXHcBh7MDIpR6F0Mg1tWVHi4WexvnwbKVRZm6Y9h_x4WdstvxsSeJR_1Cy-IGa0_gPcXn321uFD3aFdTIw7QYyoReF72XDVNwdsvtSpE2v-fImQwq-ohOLAjrmg1R0xqf5mCOSKCkxvGKdlRlM6OmA_z7gGnj15c9-CnkNJe1mbEdN6toooqVkG1F-u7u0AbapSsbNkdPMDFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
هر پلتفرم و ابزار جدیدی که وارد بازار می‌شه رو بررسی می‌کنم، دنبال دیتاهایی هستم که جای دیگه‌ای پیدا نمی‌شه یا اگر هست، خیلی کم بهش پرداخته شده.
🏹
امروز
کمان‌دار
رو کامل بررسی کردم. سه بخشش برام جذاب بود:
➕
رادار سهم
شرکت رو از چهار جهت بررسی می‌کنه و به هر کدوم از ۱ تا ۶ نمره می‌ده: رشد، سودآوری، سلامت مالی و جریان نقد. هر آیتم هم زیرمجموعه‌های فنی خودش رو داره. (خیلی گشتم ۶ از ۶ پیدا کنم، نبود.) علاوه بر این تا چهار سهم رو هم میشه با هم همزمان مقایسه کرد.
➕
پرتفوی صندوق‌ها
فقط وزن هر نماد در پرتفوی رو نشون نمی‌ده، سود و زیان اون نماد و درصدش رو هم میاره.
➕
شبکه اجتماعی
اکثر کانال‌های پربیننده‌ی بورسی یک‌جا جمع شدن و تو هر نماد می‌تونید علاوه بر نظرات افراد، دیدگاه‌ها و محتواها رو از چندین زاویه از نظر دیگران بخونید.
یه نکته‌ی‌ دیگه هم که به چشمم خورد: ارقام مالی فصلی در ایران تجمعی منتشر می‌شه و کمان‌دار تفکیکشون می‌کنه، چیزی که معمولاً دستی باید حسابش کنی.
کمان‌دار
رو از اینجا می‌تونین تست کنین:
https://kamandar.ir</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/694624" target="_blank">📅 19:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: کودکان غزه از طریق شیر مادر خود، نفرت را در خود جای می‌دهند
🔹
نفرت از یهودیان از نوزادی در غزه ریشه می‌گیرد، و اسرائیل را به عنوان داوود در جنگی علیه جالوت "فوندامنتالیسم اسلامی جهانی" معرفی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/694623" target="_blank">📅 19:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پوتین: رهبران شوروی در پی راضی نگه داشتن دنیا بودند؛ رهبران شوروی ساده‌لوح بودند و اعتماد زیادی به غرب داشتند که موجب فروپاشی اتحاد جماهیر شوروی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694622" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYdu7bWIfZP3O4KVqDpeBkLsL8E6g_LdM48B4RB3-qvt31qnszaiYd2wCs1zQX8vMqXVS6Xx9T69HNIafFiEHrwpcSmHX_mqnPhr78Jlle2-z9335y2z8V74V0ler9L__gKpV8wv0m1TpneZe4fZcjYw0Jmngx18Qoe_za8v4agmNYvp5LD8V3JQ7VQT35Pk3jPONPqCdenonVUfBxrcRId2ooZgCCgUq4eIQod68fT_FIw-eYOBsVHoYdxif3DQWc8ajWKc_kHn3DNtYSbPpYrjUwWvuXKl5Rti70a5pg2WVtdb_HTWE_qjGMeHwQm5F-Cke-q5iotJ0T8kOSn6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین میزان مصرف بنزین در بخش‌های مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694621" target="_blank">📅 19:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48ded5e2e.mp4?token=KhrhLqQ8Q5v4RO0xM0vbjR-TwqJEvtW52hhngG-CRAdNYVDFWT3NoYiqGP9Q8MdN0mrxMKnAwGXAulD-emhp6u16vngHLsyAS33fak2rF2TY4Nsoubt89RB7vQa0EIGb2lX9Cbnkf_y8pI03HFk5qOF5trkVHbAXfR0vV-gt9ryFBbU_rFzQ3Kmotquf5xUbTpoAJ6wbkOaaA9mMX6QaPWbv_deEqBpGHrukOFkmDEpjWv6hbhiA8m_befRWpVP66nHN3J3hCyjq0FJ5tubq6cHdj6FTullHfj3cmpyjNhY66ZTdsF53UTAFYnXkJdKc83CBp2ANuAxK9XDlJgg9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48ded5e2e.mp4?token=KhrhLqQ8Q5v4RO0xM0vbjR-TwqJEvtW52hhngG-CRAdNYVDFWT3NoYiqGP9Q8MdN0mrxMKnAwGXAulD-emhp6u16vngHLsyAS33fak2rF2TY4Nsoubt89RB7vQa0EIGb2lX9Cbnkf_y8pI03HFk5qOF5trkVHbAXfR0vV-gt9ryFBbU_rFzQ3Kmotquf5xUbTpoAJ6wbkOaaA9mMX6QaPWbv_deEqBpGHrukOFkmDEpjWv6hbhiA8m_befRWpVP66nHN3J3hCyjq0FJ5tubq6cHdj6FTullHfj3cmpyjNhY66ZTdsF53UTAFYnXkJdKc83CBp2ANuAxK9XDlJgg9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوندن عقد آریایی آرام جعفری و بابک انصاری، توسط مرجانه گلچین @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/694620" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
قیمت نفت برنت با ۳.۷ درصد افزایش از ۱۰۱ دلار عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/694619" target="_blank">📅 19:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694618">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNz3ztAarYWdWCCQXT--7Xf9wJPHRC8fcO2NwpjRLpSVYzIcOf_wGIWTMHXAsiBKPbbL6M81cjrzhmyI5h2S77xPm3zzgq8PjMPjyubu0JBSRU9-ktr3Z7glPMNRAuCf-muHpo4ys_kcy3NWTLfLV5qfkzYiWlzYieP6xoUi5FN_-NWzwDWPZMnJA3yxAMeeo30c4PRTkLJl0KsOtRdQSkPqSYMf0GA5FoF1QHKONhquuxTwXiR8zbUc2SMcpA_Gaao4XIc83ktUVtdi98eJs21azGAR6c4Mc4krRXPAxo_sFAjp5lreuPAF5TA0g-BGB3DSwveHO7SLQKdINUnPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم ترین فیوزهای خودرو و کاربرد آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/694618" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS7HSLUSBVv8c3ows_HSp9tA0GPMd46xto_lTTab2heLr9Gy9MZwyEJTJTYmVWgAu5tEPEePWM2Vk9TMmzxO5lhTNHdDDkFZggne6mb50IFUt81TovJiA-ZwsBPBIvqOh7q8OsXvL3XptoNVvW0wLudn5poR22aZksiKQILwCbtxKuWiFwLhIHM8yX9UosH63gc5URO-9zHHIgEPEahdW23-XOdQSUC6nx6rGiAyXS7IgQEii_0LojmZS7Pj80ec35tJ1Vyc6YMMjAz3rzun7KciDMUCS4NQvud6p_WbDM1AfQ3jUntXj4__qFzAtWBORvPDxlL4hisN-I4n66WHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناریوی سوخته
🔹
نتانیاهو، ترامپ و غربی‌ها بار دیگر با تکرار یک الگوی نخ‌نما، فضاسازی رسانه‌ای و امنیتی علیه ایران را کلید زده‌اند، از ادعا درباره برنامه هسته‌ای تا نسبت دادن غیر مستقیم حوادثی مانند پرونده فلای‌دبی و حادثه فیرفورد به ایران. الگو اما آشناست اتهام‌زنی، ایجاد هراس، آماده‌سازی افکار عمومی و زمینه‌سازی برای تشدید فشار و اقدامات نظامی علیه ایران. سناریویی که بارها تکرار شده و حالا بیش از آنکه روایت یک واقعیت تازه باشد، به یک طراحی رسانه‌ای سوخته شبیه است. تلاش برای ساختن «تهدیدایران» در افکار عمومی و فراهم کردن زمینه سیاسی و رسانه‌ای برای اقدامات احتمالی‌نظامی ارزیابی می‌شود.
🔹
هشتصدوهفتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/694617" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6ee9dffe.mp4?token=j0cdB4ZUOnPUvLDpAC6WMIuILZYz_FYHMGdef7e4yc2DQTPE7_zGGkCL6v57Amp1u43DSIM0A0PrzwcfgZi2uVZ192dEdTn9qGBAxbw6zlZNAhQ3_z7orowkVU1bAm2p0fySV1g80apBHntEf_V5OCVM92qpAy3FbzBvLdke5OzIce8Ij013kcieqA_UhCZQmfJHarCe3fSS7arUKuae6F4WurrlVLgSEh2Fosz8XGlHRzHntsuEGvaWT9DN7uxw8t29KMr5MHUEant79ILmGm91yVeH5CECRmgMAB8pL2HdOh38Ljh0HUQf1PyUcdl_xIwkicU5BLhJwWVwUxAvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6ee9dffe.mp4?token=j0cdB4ZUOnPUvLDpAC6WMIuILZYz_FYHMGdef7e4yc2DQTPE7_zGGkCL6v57Amp1u43DSIM0A0PrzwcfgZi2uVZ192dEdTn9qGBAxbw6zlZNAhQ3_z7orowkVU1bAm2p0fySV1g80apBHntEf_V5OCVM92qpAy3FbzBvLdke5OzIce8Ij013kcieqA_UhCZQmfJHarCe3fSS7arUKuae6F4WurrlVLgSEh2Fosz8XGlHRzHntsuEGvaWT9DN7uxw8t29KMr5MHUEant79ILmGm91yVeH5CECRmgMAB8pL2HdOh38Ljh0HUQf1PyUcdl_xIwkicU5BLhJwWVwUxAvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌طوری از هر درختی نهال بگیرید
🌳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/694616" target="_blank">📅 18:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یک منبع امنیتی اظهار نظر مبنی بر «ورود گروه‌های مسلح به کشور» را تکذیب کرد
🔹
در پی انتشار مطالبی در برخی رسانه‌ها و شبکه‌های اجتماعی مبنی بر «ورود گروه‌های مسلح آموزش دیده به کشور و استقرار در برخی محلات»، یک منبع امنیتی به تسنیم تاکید کرد: مطالب و ادعاهای مذکور، فاقد اعتبار بوده و صرفاً بیان دیدگاه‌های شخصی است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link
‌</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694615" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
الجزیره: ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، پایگاه سن‌دیگو را به مقصد خاورمیانه ترک کردند
🔹
به این ترتیب تا پایان ماه نوامبر، ۳ ناو هواپیمابر و ۲ گروه عملیاتی آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/694614" target="_blank">📅 18:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvpoAar16nCp61STZVC82b4gSG4_9PgMEOBGTF9TG-nk9cBCF0Z5lfyyEzR3q3iRtyiLlQqvbc_NCv4EdEtJ17yFF8OtFHrwvlv8w8cgALLDEDDG9d2nAWSnUqlfhvdVm96Lg513kVZ6_EcJWqaumN5VDDgdTndkY5qbX6BEHI43b6Bh19WzO6Y51juXpLlry9FKkW4jEk3bBqHmXYn8NZgrM8hLi0oha2DuVZitq2qfa8f7RPTpQ8n_Zab9N8tDIrajrzlkgYeoznIffmy_EF6juNedIc_iqOuCVvcMYDah4cLc3jFp6XYlZ1tFwkXH5eNWIFmt6aRvsMSuxZVxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم و نشانه‌های کبد چرب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/694613" target="_blank">📅 18:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
معاون وزیر خارجه ایران در گفتگو با رسانه روس: جمهوری اسلامی ایران طرح خود برای حل بحران را از طریق میانجی‌گری قطر به آمریکا منتقل کرده و اکنون توپ در زمین واشنگتن قرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/694612" target="_blank">📅 18:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksKs87vGQpjoWFutekSBoAQgPkREltr7v6o2HGnGS07wP8VywkFS76FyfptjRssX9O1W8u_VbKOHoJ3OZm1hul1c3C1pV-vWVBzhpyvRieAD_3HNiQ-8UnE4y3-qYgKey0ux285GZKGlr7bF_O1HtZtNt4HADUF_m0lKypUtxYDkGxv02h1sp61om7xzqz5AhwTZAeXNWlG0t35Y8_gaM-9P8F50Qz5qo2xHuIkSyMgvxBlyt1GsDEBSpGwbWY2RUuIBd_va9t6eJTwR-dDpBL3kFtOUM409O7eb2MAbq4tNrZp-RBCk7niTQ5pGfu2-2R4y1eF-sbezpt4wa8Dfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا الان زمان مناسبی برای خرید دلار نیست
🔹
نرخ ارز حقیقی، قدرت خرید واقعی ارز است. که از تعدیل نرخ اسمی نسبت به «تفاوت تورم داخل و تورم خارج» به دست می‌آید. برای مقایسه، باید این عدد را نسبت به یک عدد ثابت در نظر گرفت، نرخ ارز حقیقی به قیمت‌های ثابت مهر ۱۴۰۵، در اکثر مواقع در محدوده‌ی ۱۵۰ تا ۲۰۰ هزار تومان در نوسان بوده است.
🔹
در زمان‌هایی مانند مهر ۱۳۹۷ و مهر ۱۳۹۹ که این نرخ به ترتیب به ارقام ۲۷۳ و ۲۷۴ هزار تومان رسیده بود، قیمت‌ها به سرعت پایین آمده و به همان محدوده‌ی یادشده بازگشته‌اند.
⚠️
با رسیدن نرخ ارز حقیقی به مرز ۲۶۰ هزار تومان، ارز دیگر دارایی ارزانی نیست. هرچند احتمال رشد آن همچنان وجود دارد، اما خطر ریزش، آن را به یک دارایی کاملاً پرریسک برای ورود تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/694611" target="_blank">📅 18:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll5wlXQMI4HWTSaMZYGQo6dUS_zleM-fwUJ4yG1OF-dZ0xUJE95lfdWfGPqSpx6aQC8gEKEMw-_pn-jXwqDUhqYKNrAqETbiD6MIfXNVLNl5SH9LTv9ANewwQLRmJef-0keu4ybkGjPaiioidOIPhgbd2vOaqTtLykER1ND4r7m0hyatNFnvj6f2Mw4Vgdwb7Q6_r4vB7SVJnl14YFCHDDHMOsRAYvkBLf6kusLlcdPUUVqsn2pfkY63npKKQSlktuUxJdIrxT3OTAO2TSGHdM4FTrf5zyWxc87h6ukV04hTrEDTz5Dz9-7anszJr4fx4CfKggECStC2hZrtfFblZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی؛ مرد ویولن سفید میان شهرت، مهاجرت و حاشیه | او کی رفت و چه کرد و چرا بازگشت؟
🔹
کمتر خواننده‌ای در موسیقی پاپ ایرانی را می‌توان پیدا کرد که هویت هنری‌اش تا این اندازه با یک ساز گره خورده باشد. برای چند نسل از ایرانیان، نام بیژن مرتضوی پیش از آنکه یادآور یک خواننده باشد، با تصویر ویولن و آرشه‌ای گره خورده که بخش مهمی از موسیقی پاپ ایرانی خارج از کشور را شکل داد. هنرمندی که از کودکی ویولن زد، در جوانی مهاجرت کرد، در آمریکا به شهرت رسید و بعدها به یکی از شناخته‌شده‌ترین نوازندگان ایرانی در جهان تبدیل شد.
گزارش خبرفوری درباره او را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249229</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/694610" target="_blank">📅 18:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694609">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اعزام نیروهای جدید آمریکایی به اطراف ایران
الجزیره به نقل از یک مقام آمریکایی:
🔹
بیش از ۲۰۰۰ تفنگدار دریایی با یک نیروی زمینی آبی-خاکی عازم خاورمیانه هستند.
🔹
تا پایان نوامبر، سه ناو هواپیمابر و دو گروه پیاده نظام در اطراف ایران مستقر خواهند شد.
🔹
با بسیج این همه نیرو در خاورمیانه، رهبران گزینه‌های زیادی برای مقابله با ایران خواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/694609" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694608">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ارزهایی که در ایران از دلار جلو زدند!
🔹
در حالی که دلار این‌روزها محور بازار بوده اما ارزهایی هستند که بیشتر از دلار بازدهی داشته‌اند. در یک ماه گذشته یوآن چین با ۲۱.۵ درصد بیشترین بازدهی را ثبت کرد و دلار با ۲۰.۳ درصد در رتبه هفتم قرار گرفت.
🔹
در انتهای جدول هم دینار عراق با ۱۱.۳ درصد کمترین رشد را داشت. در بازه شش‌ماهه هم یوآن و روبل صدرنشین‌اند، دلار با ۴۶.۸ درصد هشتم است و لیر ترکیه و دینار عراق ضعیف‌ترین عملکرد را ثبت کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/694608" target="_blank">📅 18:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwHIAloGK9XbKsU7K1CuPfamyNpocBdzxEambfNQmutcRNzvCbUNlCRXiSiG8bFQBdfK8OcWD8bEvlrYmwSyFzieMbPccZ0fEi9qVaZibojy18rJfIUSlFNxcvX66afGmHTg3b8pQ1gNjQSVzd3nC12RYtUc1CboVBqbyQUyHyUR7KpKh9nvy1yISBfEMWI8uGEsku-nnnvCkDtrQMLujKgGb4SmBUZqIa6aLK0__Teqs44drYaa7DlvHfr8LK47b0M1Bv3eGbw3P-klv3FG-j2Jc-SMT_goVz0kF4fxQhnMeKSVBiUwWsCc44vAt6-AY1qc9M-8DyJ5d9zeHhkP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک ترند جالب در شبکه‌های اجتماعی؛ از ChatGPT بپرسید:
Based on your personal experience while talking to me, please name a movie/tv character who resembles me. Only give me a name.
🔹
سپس ChatGPT بر اساس گفت‌وگوهای قبلی، شخصیتی را که بیشترین شباهت را به شما دارد معرفی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694607" target="_blank">📅 18:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3201b6bf83.mp4?token=Wt8ff6ZYTGzfBYjy8Oe8lw4oPCblGxSDopYa9C3056WH1lBQFM-YMNDtqKvBEClxwWfxGvdiRCquU4clHXoR46gsRGFcOp8WbX8gXb-EEZUBq3sv1cFWvymnI00knrrcBbryAWNlFD0PYEUr6Gw0w4XduNJyuO3fsOWxHJHzj2GTNUS6tOAjOYOUdicswctWpg3ZGmkJTq2FfHCgA4PMZ_4joiifM-qA1_wcX_mDdvN5oZM5hpI0SB9Rv8AI04jOi86bHpeZQ2Vf0WcPsq5zt265pMzc_wPdjSO2yKReOrf92MCMk6Y7RfdX9Eskyo7dQaNVEr99L5WyRpukv3XYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3201b6bf83.mp4?token=Wt8ff6ZYTGzfBYjy8Oe8lw4oPCblGxSDopYa9C3056WH1lBQFM-YMNDtqKvBEClxwWfxGvdiRCquU4clHXoR46gsRGFcOp8WbX8gXb-EEZUBq3sv1cFWvymnI00knrrcBbryAWNlFD0PYEUr6Gw0w4XduNJyuO3fsOWxHJHzj2GTNUS6tOAjOYOUdicswctWpg3ZGmkJTq2FfHCgA4PMZ_4joiifM-qA1_wcX_mDdvN5oZM5hpI0SB9Rv8AI04jOi86bHpeZQ2Vf0WcPsq5zt265pMzc_wPdjSO2yKReOrf92MCMk6Y7RfdX9Eskyo7dQaNVEr99L5WyRpukv3XYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اهدای هدایای متبرک حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به خانواده شهید حزب‌الله در روستایی نزدیک نقطه صفر درگیری
🔹
دیدار هیات ایرانی با خانواده این شهید حزب‌الله در روستایی در نزدیکی نقطه صفر درگیری با رژیم صهیونیستی انجام شد؛ جایی که خانواده‌های شهدا در خط مقدم مقاومت، همچنان در کنار رزمندگان حزب‌الله حضور دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/694606" target="_blank">📅 18:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d2aa4165.mp4?token=otgNh95FJxLVWApHSLlq5Vk-2v8E-bMsfWpxBaeIwUDuVjp4pkQZX5GyLvuMQzhNQEKiPfm-T_LNV3GagCs8W-TQ_djsbxjoBtEg5pJtAIelM8HJPAINk47M1yLdsuf_qi65U8r9dRxMn40F3JW-O3Ei8ogtvouCkpe_VIvvtix5GXmEPcFtv6Ncf0vKZTsw3gTfc1ljptbKDQPNxYA1kIoz5ThGRuLHbzJ3rW6fPo7vjUWJyD89W_-jyLunqP8kua65r8lm-hLdGe7aN_Msady8K0CHKXR7uwscZmhY7rIgKHpi0C5_8kmjnrhPG2rtxGDf1BUE-2EWNpFpOW0RVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d2aa4165.mp4?token=otgNh95FJxLVWApHSLlq5Vk-2v8E-bMsfWpxBaeIwUDuVjp4pkQZX5GyLvuMQzhNQEKiPfm-T_LNV3GagCs8W-TQ_djsbxjoBtEg5pJtAIelM8HJPAINk47M1yLdsuf_qi65U8r9dRxMn40F3JW-O3Ei8ogtvouCkpe_VIvvtix5GXmEPcFtv6Ncf0vKZTsw3gTfc1ljptbKDQPNxYA1kIoz5ThGRuLHbzJ3rW6fPo7vjUWJyD89W_-jyLunqP8kua65r8lm-hLdGe7aN_Msady8K0CHKXR7uwscZmhY7rIgKHpi0C5_8kmjnrhPG2rtxGDf1BUE-2EWNpFpOW0RVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلوار شیشه‌ای هم وارد بازار شد!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/694605" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
فرانسوی‌ها هنوز در ایران می‌تازند!
🔹
با اینکه پژو و رنو سال‌هاست تولید مستقیم در ایران را متوقف کرده‌اند، اما برندهای فرانسوی هنوز ۱۸ درصد از تولید خودروهای سواری کشور را در اختیار دارند.
🔹
بر اساس آمار رسمی سال گذشته، ترکیب تولید خودرو در ایران به این شکل بوده که ۶۲ درصد خودروها برند ایرانی، ۲۰ درصد برندهای چینی و ۱۸ درصد برندهای فرانسوی بوده‌اند‌.
🔹
یعنی سهم فرانسوی‌ها فقط ۲ درصد کمتر از چینی‌هاست، آن هم بدون حضور مستقیم پژو و رنو در صنعت خودروی ایران./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/694604" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBW2Xd_p3Vk82Kn0GcmWAnEj_OhgkRvTg2GSfADxMP8lOCRqUf95vvb2l8nc3p5dhp8gyoHbETXqCVeVu0o83G5AK_jHpojTZtF3a3ADEB7N8f8jQNDIL4k1FWaLepeRLTeHJ9hx3uL53i7Rbvn7lHCk2FfmU0y45vMaT_BUC63w7v21cc8-Hh6hQ5P8CeMO198kfxRsY31okPQzeTFEvUqZC1vYkaU9ZyoynNm1aHdyJ4seK16oNJJ_WKy_1cJwXSJSlwxiknrCbyauVikk2oFyiyJtCFlW6Ehkb_eETRxEL8hHFAXN1aMQ0WS1b4GbioD6hH56dK2ao0ktkoaaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWZ_SikP8sgusaC29D1z-q3wUi1Ah8PXvSQz2IRMTy4wddT3kK05pqIl8nDf46A2NXSLw15AzJwgeYB9doOdg-9ugE01IK3zLVeTMQ-utT6uZcezNqVw75xAGVDdXrXA5Lfgr8bpKEjyZiqalq58bpea20cSUgfdf4B6tP9wMEiTvb42kai2qBjUjUlaylMtu8akt52m3NlQg6w2ItkYPLXfx2-CxcLH5lSAISxzIMb0H6EzCs3IaHpyRLj91Zwa31Cmj8R5irbe2U63Dl1PTKWUtnzlbu5FEiepMcu1QUBUWryr5jHcHnpilcJRe5TIXKbVUSlyQhGDZjwSwvwuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkF8--vLUhTBNIK5mwMDcE6TFJQjtcNw_hw_3eGS48EJGpejbS5aspucrJd-uT3ustQ25XNWyb4hGWmbwupV0JKCzL3Jj8qPAnUer4llvrw0NWGzpF8qei9yxLLf75ufpK2HEKGnyGpCENbQrvoXECRI7sPQGZV479j5TFq1G9t2QBtwSKi_3S9F_2rJwS4g8fuLmqRzCn1fZfG0gfakTeWXs2oV4sJQ4y0yRr1DGi7UyaKNYX2fXTo338yFg9yk59TUPBn4snEeAjMmUZ4YeLAzrujpS2QWBaMp0-710PVBkT5Haeu6t5YeZBbum3VWlH4Ua4wCTTUL6orc_2Gxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvYgFclc2aqGs5pCOfk2A1PihHuiO4roRpr5F1g_GCGiwOcVPB7cXOkTdg_0SOmty69QNL_aI06ys7nI34jMs8PdstSfIF64_1yFCNA-8htdVDKCbgCVzbLt3J1JpR2h00xt1LqFHAY_Iw58WTpCnewJJ6qMG-8pMlAXGAMyzYMwFO7V5EqJ2aDlu6chtJnFxyq3D7jxgEXIZZ6-t2hJfi94MxAA-EVNx8QGuUsJab4NNdqqDpbPGSat3lRT4LicAgTmwrdx7TOEL2YnEXxIWJ3DzJBY5j0Z5GjQRbS0K-pbPV1Ws-cwmvw0rQN7hhEr0sMLwl972IWMCpjgzCGkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMqU0tnctE4LBGl9lTAh26uep5dsJ2aLp7dkYQJHwyHdJGRLNx8wWLUw7yu2INIlTZFf2gyyPKuCNUKdtbM2Xj2oYS86JbQDTJbJs1eQZ2_KHoWOUY-JIcTzu587FgH1pbqVIMY4xIreBu3Z1Ei1dxb9VAQ2kYN-5g2m_e2QmlNiZXyV4VKmXvmkTAqwNRL031dUw_VXwjpIYafkVnPMQL35oVBjGKzwevNEfWrMjCUBA_B7gC08fxrP3meRIKyxJguDMv29VMHaQHIqdGLKBnMP8zp3mr--OM0WW_7JjN1n0AjIb8Ip0sFUphWvODOReBMkNhrH30n0bPCJQrLT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7kTAtIoKyNbQ0xjhXpAYEQHZrT8_yCC804gMnhJtAGvZSGyLrpYsmCLVCmxtI26j2EtjwHXjRqJU4IXYw6DVtuMFp6dYGjJ0TdjdydsSjo2dWwzs249VCUV5xFOHUgJlqIMqugqlaTCJPripbxA32-PcS4UofQmgBK0DQKdH_XI3Hg0-jSqDeATxz1_-gSbNWi5D8ifU8IUtMsEqZSFRHwEel9hvnsjlEJk0FMFRvgweC-erj2uGQ-2QOQACK2tnZJ-Xa9YTQGlrim8K3ycH5Q5nlgkOo1gLX4AaSMJKHWsqBenNVGDjX1_8hQqb7P788-aS0JlXfezpudlj4cgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر فراموش می‌کنید که هر کدام از حروف اضافه را کجا به‌کار ببرید، این راهنما برای شماست! #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/694598" target="_blank">📅 18:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=vbP5Gb6beZxiambdLs07lxbd-LQEgy-71_UtkSFCLBMlAiBJlvP9IzUJBMxxYUGY2U5yJxo_Xga6L5JEP44WEhqFRgflR3gaWNuBJFDxwZ_ynxESr8GunZMuxjDDXC6MFB1q24oSCcnP6R5Mu63zYsWh-wxVuMyeJ6jLwt84Bgr--Dwm_7ZRvSlvuoEEN94I7QyOPTkKabXQGPrUhUKhcojrDN1Eie2xXCAbJ9LwT7t8MsQq7VAgZsP8F1Po4XXfNaYip-oIZbAt4LnBXPMo0BBVng6w9c7ZOxW3GW_Sxw6YtGO7IOA4ZnxRGOdQH6wxRWMut6tM0xnxDtE3pUuwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=vbP5Gb6beZxiambdLs07lxbd-LQEgy-71_UtkSFCLBMlAiBJlvP9IzUJBMxxYUGY2U5yJxo_Xga6L5JEP44WEhqFRgflR3gaWNuBJFDxwZ_ynxESr8GunZMuxjDDXC6MFB1q24oSCcnP6R5Mu63zYsWh-wxVuMyeJ6jLwt84Bgr--Dwm_7ZRvSlvuoEEN94I7QyOPTkKabXQGPrUhUKhcojrDN1Eie2xXCAbJ9LwT7t8MsQq7VAgZsP8F1Po4XXfNaYip-oIZbAt4LnBXPMo0BBVng6w9c7ZOxW3GW_Sxw6YtGO7IOA4ZnxRGOdQH6wxRWMut6tM0xnxDtE3pUuwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2604
https://www.20landing.com/214/2604</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694596" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990e9dda9.mp4?token=rbnR4AkieR7fsIHKMtjUdRoxvypBL66XfBSVU1wFk6_pxM-7YVzxdWGAeIZyhkFzcki66W7nS7SNw-KnFsl67oF5M7mAEx59mP70Phhwlgi3_zCawHPGXhNoAp6MgPYnbKiPxKZpg6yWAp8JvcWEVYwwks3iHhgF26Fab62wfpXZZg57XNb_RBVa1NhrftlhOqQf0uQVn6B8jwtyxkCcHDngU97S3Jw7v6beOXangT33Bkdw6A62wv-XXWFCTnNkkXLnO6b3iYzHbx0kAL6j0t35F2xNdplhZjuzh50KNFPYo5yDICTDMVXKRh7Z7r3FGDD4UrJZ9QTYNY-3BUATJrpqbAit4lUGl9w8gbrQyMrjfXam8KM_Q8eyvWv_x0D7kdVV3r0fJnK9la_e_W2mXpPqYl9-W6rDkX7MoM0lOura6SbRKBq2Ms8P8Nvspu0KqarhqDxy1hSUYUndOG6O2MnXGvVnGeLGSSGd2xDM50cEBU9YrgBFU3w1q2Uw3XXvS76g0qpm11DuQD2E7NdjaUwI1OTDc89ni7yz9AOAkGFPKoesG07N9WgoSB6gql0Ttmj4zw9e_ypyZLy7JD_gPnI9BpjuiiulWlxhyfIkaCn8at35bRMdppifdbGmGM9_peGyhj1pfzhrV7RPgPRShnRWSi0Fnx6GTDEk19MqGYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990e9dda9.mp4?token=rbnR4AkieR7fsIHKMtjUdRoxvypBL66XfBSVU1wFk6_pxM-7YVzxdWGAeIZyhkFzcki66W7nS7SNw-KnFsl67oF5M7mAEx59mP70Phhwlgi3_zCawHPGXhNoAp6MgPYnbKiPxKZpg6yWAp8JvcWEVYwwks3iHhgF26Fab62wfpXZZg57XNb_RBVa1NhrftlhOqQf0uQVn6B8jwtyxkCcHDngU97S3Jw7v6beOXangT33Bkdw6A62wv-XXWFCTnNkkXLnO6b3iYzHbx0kAL6j0t35F2xNdplhZjuzh50KNFPYo5yDICTDMVXKRh7Z7r3FGDD4UrJZ9QTYNY-3BUATJrpqbAit4lUGl9w8gbrQyMrjfXam8KM_Q8eyvWv_x0D7kdVV3r0fJnK9la_e_W2mXpPqYl9-W6rDkX7MoM0lOura6SbRKBq2Ms8P8Nvspu0KqarhqDxy1hSUYUndOG6O2MnXGvVnGeLGSSGd2xDM50cEBU9YrgBFU3w1q2Uw3XXvS76g0qpm11DuQD2E7NdjaUwI1OTDc89ni7yz9AOAkGFPKoesG07N9WgoSB6gql0Ttmj4zw9e_ypyZLy7JD_gPnI9BpjuiiulWlxhyfIkaCn8at35bRMdppifdbGmGM9_peGyhj1pfzhrV7RPgPRShnRWSi0Fnx6GTDEk19MqGYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای در تجمع مردم مبعوث در میدان شهدا تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/694595" target="_blank">📅 17:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شرکت ملی پخش فرآورده‌های نفتی: کارت اضطراری اختصاصی برای موتورسیکلت‌ها در جایگاه‌های سوخت تخصیص می‌یابد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/694594" target="_blank">📅 17:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کاربران ایرانی شبکه‌های اجتماعی خارجی را ترک نکرده‌اند
🔹
با وجود محدودیت‌ها و قطعی‌های طولانی، اینستاگرام هنوز ۴۲ میلیون و تلگرام ۳۳ میلیون کاربر فعال ایرانی دارد.
🔹
همزمان، پلتفرم‌های داخلی هم رشد کرده‌اند؛ روبیکا به ۴۲ میلیون، بله به ۴۱ میلیون و ایتا به ۳۴ میلیون کاربر فعال رسیده‌اند.
🔹
بنا بر گزارش دیتاک، همزمان با قطعی اینترنت کاربران روبیکا از ۲۸ میلیون به ۴۲ میلیون، ایتا از ۲۷ میلیون به ۳۴ میلیون و بله از ۱۱ میلیون به ۴۱ میلیون رسیده‌اند.
🔹
این داده می‌گوید که کاربران ایرانی شبکه‌های اجتماعی را عوض نکرده، اما سبدش را بزرگ‌تر کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694593" target="_blank">📅 17:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b876bf4a18.mp4?token=u5ZDl5wYyhNsYm7Ik23WyHnKmLyNiZ1kcXCBFJ2MYxHZivCvBwpjK1A40e3M95BjXlL3Aq_h1e1lYAiH5Y9Tlr53DOosMFDPaK7uaMY7fBs1DiqeJO4EMLp4r-m6h3VZNfhO0sZbMWalbuBI8XziUZxPBClAoC_HOTNEvYVB5KIXsxTP8QbzH3Yze9PV_8r3GRUL7BSznVUfnMb3xTJzZEy9Ypl0EN6ACZk0GtuQipUAjpAGZraOFFt72LbpifFzwLGsRNGtICcTDnXHj_4DbzbD8xcQCCK55LZ-fBdZ_bsKoMEoM1TdTc2LJufYywAuR8_4n9wRs6CaXh9d56pMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b876bf4a18.mp4?token=u5ZDl5wYyhNsYm7Ik23WyHnKmLyNiZ1kcXCBFJ2MYxHZivCvBwpjK1A40e3M95BjXlL3Aq_h1e1lYAiH5Y9Tlr53DOosMFDPaK7uaMY7fBs1DiqeJO4EMLp4r-m6h3VZNfhO0sZbMWalbuBI8XziUZxPBClAoC_HOTNEvYVB5KIXsxTP8QbzH3Yze9PV_8r3GRUL7BSznVUfnMb3xTJzZEy9Ypl0EN6ACZk0GtuQipUAjpAGZraOFFt72LbpifFzwLGsRNGtICcTDnXHj_4DbzbD8xcQCCK55LZ-fBdZ_bsKoMEoM1TdTc2LJufYywAuR8_4n9wRs6CaXh9d56pMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجتماع بزرگ جانفدایان البرز
🔹
همین جمعه از ایران کوچک برمی‌خیزیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/694592" target="_blank">📅 17:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694590">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a880fc2bd5.mp4?token=hAvEto9C87WbIo-h1IjtsnF666W3Qd2aODMZ0zJqZrsZD7i0h0DOr-MSmqVRWEy3pO9rxpzcKZ368JjMG45zQrDnAmq0Hfj7d50KtbIuP_mZy3roy1-FEvckQwfTUn7xj5brX8Wc7E0d0vAUqyXkB07BIlcQCFD_3bwqhDNMuK2DPhWEYwRvlai_1RYbbJp63GDD6JmVNbBb2uYkHzNskzorFju_pUqMLeQi1_VG0Ap5ulosWW48UrOCD44uAjTKDALfK0Gryta9IM7FuwpGalOiILM1PdOsfONgYJHHUpVWZtpGKKBRKp8bePhYYYZurAen0wPnYJre0pb6ZUaLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a880fc2bd5.mp4?token=hAvEto9C87WbIo-h1IjtsnF666W3Qd2aODMZ0zJqZrsZD7i0h0DOr-MSmqVRWEy3pO9rxpzcKZ368JjMG45zQrDnAmq0Hfj7d50KtbIuP_mZy3roy1-FEvckQwfTUn7xj5brX8Wc7E0d0vAUqyXkB07BIlcQCFD_3bwqhDNMuK2DPhWEYwRvlai_1RYbbJp63GDD6JmVNbBb2uYkHzNskzorFju_pUqMLeQi1_VG0Ap5ulosWW48UrOCD44uAjTKDALfK0Gryta9IM7FuwpGalOiILM1PdOsfONgYJHHUpVWZtpGKKBRKp8bePhYYYZurAen0wPnYJre0pb6ZUaLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه‌ تشخیص کابل شارژر اصل از فیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/694590" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694589">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شرط جدید وزیر اقتصاد برای افزایش کالابرگ: نه خودرو داشته باشید نه ملک!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/694589" target="_blank">📅 17:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رسانه‌های انگلیسی: پلیس انگلیس در حال بررسی ارتباط ایران با یک طرح مشکوک به بمب‌گذاری در پایگاه فیرفورد (محل استقرار بمب‌افکن‌‌های آمریکایی) است
🔹
ظهر امروز پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694588" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
آمریکا یک پاکستانی را متهم به تامین سلاح برای ایران کرد
رسانه اماراتی نشنال مدعی شد:
🔹
مالک پاکستانی یک تأمین‌کننده سلاح و شرکت‌هایش به دلیل ادعای تأمین سلاح برای ایران، توسط آمریکا تحریم شده‌اند.
🔹
وزارت خزانه‌داری امریکا ادعا کرد که وسیم پاشا تجمل و گروه کاوالیر او به عنوان «واسطه شخص ثالث» برای «تهیه و توزیع سلاح» برای وزارت دفاع و لجستیک نیروهای مسلح ایران (مدافع) متهم هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/694587" target="_blank">📅 17:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77061894a3.mp4?token=fk705TQ8rMoLALQuLXozP1OzcwrEbH0-rMTjx8MP8_V5qEsu6E_gSJyISyF2_NSt0iQ3Lk7NXnH9SQ3O1g3ESTht7gEB1zhfhT7xDoYRQlG93-jGsaWXr0VTFPgtcU-gz46GjMdDvXTg7MHOp_edTQWQrASCHyEcAwIp5R8X2Mds3u1g3d1WshCRkGgmiPo2ysRARnEpQnHixI6l9IoHS7YGGugtMfkp1RW49bXMnVXodbWn3vUqdKJ0TeqlBz06fjmJX5il3MMzn9HwbdIqFBgsdeYy0t8fGtQ227MTF1OAwcM46idFfc6tSxkNklC22dE267IopksvYFmEGfp_klsny_XKUXzltCbXi9CuH1XGv-ymci5A9m-zEeG--wPl-kyN2B5NO1d_5FwG277GNXC-DJcZ5K8_SvrEv08PTjQlI8eu8NYY2Rj3__rgofZn2jojCN8wS5bJEFyqeggzWveRqaVFhXDJBZITK0n--gPiMGZqXhHEsv72T2NJv4AReVNTnXFEhiNTZqtfSqUyAnUUPPqIjt9IUZ__9Y1K35RdQzoBgiFuICc6jTNigpemIxC1Kl1zb_in46JXgoj6tWLQgF5qWyiB1gG2015mOjgWLoomieOdMy0ot3BdZoTKlxsgKbW21Zs5qfjXEFtQHi18xrtH7Sr1w298toqtTs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77061894a3.mp4?token=fk705TQ8rMoLALQuLXozP1OzcwrEbH0-rMTjx8MP8_V5qEsu6E_gSJyISyF2_NSt0iQ3Lk7NXnH9SQ3O1g3ESTht7gEB1zhfhT7xDoYRQlG93-jGsaWXr0VTFPgtcU-gz46GjMdDvXTg7MHOp_edTQWQrASCHyEcAwIp5R8X2Mds3u1g3d1WshCRkGgmiPo2ysRARnEpQnHixI6l9IoHS7YGGugtMfkp1RW49bXMnVXodbWn3vUqdKJ0TeqlBz06fjmJX5il3MMzn9HwbdIqFBgsdeYy0t8fGtQ227MTF1OAwcM46idFfc6tSxkNklC22dE267IopksvYFmEGfp_klsny_XKUXzltCbXi9CuH1XGv-ymci5A9m-zEeG--wPl-kyN2B5NO1d_5FwG277GNXC-DJcZ5K8_SvrEv08PTjQlI8eu8NYY2Rj3__rgofZn2jojCN8wS5bJEFyqeggzWveRqaVFhXDJBZITK0n--gPiMGZqXhHEsv72T2NJv4AReVNTnXFEhiNTZqtfSqUyAnUUPPqIjt9IUZ__9Y1K35RdQzoBgiFuICc6jTNigpemIxC1Kl1zb_in46JXgoj6tWLQgF5qWyiB1gG2015mOjgWLoomieOdMy0ot3BdZoTKlxsgKbW21Zs5qfjXEFtQHi18xrtH7Sr1w298toqtTs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدو کلاه‌دار شکلی از کدو که هرگز فکر نمی‌کردید وجود دارد
🎃
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694586" target="_blank">📅 17:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL0Kkrj97c5dbzsFv00pz7Y8QTNjiguxm8p_2u-X9ur9GPYizjRdutBEQ7l52uJWuNQWLUP50QUPswilzvGwQne8B-cEN7KvMHuGcagj6NdpMzzKs3sgSc-r_Cb5IxNb2jXJRO_KhcpXZfBtxvWmdNR-K1BVYWdiSvBNEOIalJQL-m_sbObsX8G3wiqKXGmckmxrlkOyG7ps4pll9gv2Cl9mdfOuSEiIFBgKLpyqWtrM-enL7qEHKRnKYSBB1Za0TkgZ1WwhkasPcOv8CBJ8UKreWvo6sj3Xs7LV4tyVyKZxVcef_PNqbL4r81JENodEXi2eJKY-Uc_JLNDftEde-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارنامه مالی هفته
🔹
در هفته‌ای که گذشت، دلار و تتر با رشد بیش از ۹ درصدی، بیشترین افزایش قیمت را در میان بازارهای این جدول ثبت کردند. در مقابل، انس جهانی طلا ۲.۹۸ درصد کاهش قیمت را تجربه کرد؛ روندی متفاوت با بازار داخلی طلا.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/694585" target="_blank">📅 17:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سه نفتکشی که سه‌شنبه در هرمز هدف قرارگرفتند، با ردیاب خاموش درحال انتقال کشتی به کشتی نفت و مرتبط با ناوگان عربستان بودند/رویترز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/694584" target="_blank">📅 17:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNRA0DqsUMuMSeD5H_f9qp0Im9y1rrKBMdtRXodzvNM_QPkx-PpR2omYwE_wbGEIY9oSXECDOvvuryEX2fbnyASOzXAki-zOL7U-lkiYRGXo47cjBCwaqEn-ilKPS8vXiOc761owlNODin47Gg4l00en82heTGJVb8P5ZcuvuBchMEOQL3L6LDhvPEmRxEAcwfCcFdYFQPvMQUgJn7mYIC3jl6HiDVK6ngdDKl0UkChEijQkt_ARz7h0-jbvaSFbLe_Xz6yGAWRREWodPfkVt6JkedKsta4wxPFhPM4MQCXStqb6ts9awSVRo9j-ff3HF7SKzU16Mi0znEPQ83dB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مجمع وزیران ادوار طی نامه‌ای به رئیس جمهور به رئیس جمهور از عملکرد دوساله مدیریت گروه صنایع پتروشیمی خلیج‌فارس
/
هلدینگ خلیج فارس با عبور موفق از تنگنای دوران تحریم و جنگ وارد دوره «جهش سودآوری و توسعه» شده است
🔹
این هلدینگ «دوره رشد و تثبیت» را پشت سر گذاشته و دوره «جهش سودآوری و توسعه» را شروع کرده است و اکنون از نظر اندازه، سودآوری و ظرفیت سرمایه‌گذاری وارد مرحله و موقعیت متفاوت از نظر خلق ارزش افزوده بیشتر شده است.
🔹
سود خالص ۱۸۷.۵ همت سال گذشته نسبت به سال قبلتر ۶۷.۴ درصد رشد داشته و تولیدات آن به میزان ۲ میلیون تن نسبت به سال قبلتر افزایش یافته است، در صورت تداوم وضع موجود، این میزان در بازه زمانی منتهی به خرداد ۱۴۰۶ به ۲۲۰ همت می‌رسد.
🔹
در مقطع حساس دو جنگ تحمیلی و محاصره دریایی، علیرغم تمام سختی‌ها، روند تجارت و صادرات هلدینگ خلیج فارس به‌صورت شبانه‌روزی ادامه داشته و در بازه زمانی دوساله اخیر، قریب به ۱۰ میلیارددلار ارز حاصل از صادرات محصولات شرکت‌های تابعه هلدینگ، با استفاده از سامانه نظام مالی-بانکی فروخته شده و به کشور بازگشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/694582" target="_blank">📅 17:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORiPF2T9GZOBIiJJwkpWtHyEQu60xxgyTNnFDfLOTto6_f0kLxFB_pNdYRB1sHFUXKNPniSUZH2fcdcWz50DV1gHkLcmveZPThM72vxlYBRiF3Rr_71xvf8tUj8SAaTauhX9MG3UmCO8rkHAOsQY1I31SmPrBvKiqDDDfwoDRtTRMjdXFQbguceSKNu22NXBJA7u4AH1gM2ShtbSR0fNIkjRIunaqVO7o6loaWy_5o4yJs1164h9G7Gm_on6o3MJgwa9naCljjj2BTLbHWGdMOwT4QSpvqNDmUj3iHKkJpYu78R5mci4lyVNP1gpeZHcmfA_wnZy-28ySwVP_mvr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناره‌ معروف ژئوپارک دره شیرِز؛ کوهدشت لرستان
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/694581" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سفیر ایران در گرجستان احضار شد
پایگاه خبری سیویل گرجستان:
🔹
وزارت خارجه گرجستان، سیدعلی موجانی، سفیر ایران را به‌دلیل اظهاراتش درباره ملکه کتِوان و «تفاوت روایت‌های تاریخی» احضار کرد.
🔹
گرجستان می‌گوید اظهارات سفیر در شبکه‌های اجتماعی از حدود فعالیت دیپلماتیک فراتر رفته و بر افکار عمومی تأثیر منفی گذاشته است.
🔹
ملکه کتِوان چهره مقدس گرجستان است که ادعا شده در قرن هفدهم، به دست ایرانیان شکنجه شد و جان باخت. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/694580" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/414c940d77.mp4?token=PhMbJ3rewwDUoBXm47Bs-g_ZKfeMBx-ZJK-U2T9w6zK1bpOJpq9IqZPNT0WCzvAGKff0xaYIaJWXBL8N1dX-weTtI8Yi2z-aOPMdVQla9j2UxS-HXgV__wn6bEeig1MayR5Fdyuf1XqOSWUvr3wIawAOTQHhKo8RABuCI6DcUWgKOGILlg71DRNW7KNjHtYWo5ta1F4A0_bOlGrNskjIQLMt42KeeeetRwNsztk8p5Tijs_wKNT3zNyFuNtnQJeXCe7PGv_sHdSUlWHYQmVJNWDPBjbb6UNe5dCd0OPO-rzK8ZUKopUN0siIzSTDU0cirnWd9JsUPHk4aLRvpteI2ItJjf8Q-J87rCVRaSYZSGVlClsRQ1GrWb0O2FD1DWtJzm314yNOhgf3N9iXtDkIKxnJHGmaciT3jmmuxFtfxutabpzZyr47GFvC7K6-vMMAsMcspL09gXMNsLj3hqNw1PfdA_ako-4ybsFPtPhbsNJZCgNh7t4Kwk5MgVcfKE3IUwFEXofTYCWuQGZoJU_x3SQDta5-dS23NAcohg-BghfZulUkTkM7i-vyqwmhfYCXg6fH7-eMaej2vczgVC9OG7Pm52FqDblOFg4JN4LGY6le-Td6156QzBM6x5376ZKJwERkfBI1pYsiscX8n6k1FtxqvH1838_pg5gvC3jLv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/414c940d77.mp4?token=PhMbJ3rewwDUoBXm47Bs-g_ZKfeMBx-ZJK-U2T9w6zK1bpOJpq9IqZPNT0WCzvAGKff0xaYIaJWXBL8N1dX-weTtI8Yi2z-aOPMdVQla9j2UxS-HXgV__wn6bEeig1MayR5Fdyuf1XqOSWUvr3wIawAOTQHhKo8RABuCI6DcUWgKOGILlg71DRNW7KNjHtYWo5ta1F4A0_bOlGrNskjIQLMt42KeeeetRwNsztk8p5Tijs_wKNT3zNyFuNtnQJeXCe7PGv_sHdSUlWHYQmVJNWDPBjbb6UNe5dCd0OPO-rzK8ZUKopUN0siIzSTDU0cirnWd9JsUPHk4aLRvpteI2ItJjf8Q-J87rCVRaSYZSGVlClsRQ1GrWb0O2FD1DWtJzm314yNOhgf3N9iXtDkIKxnJHGmaciT3jmmuxFtfxutabpzZyr47GFvC7K6-vMMAsMcspL09gXMNsLj3hqNw1PfdA_ako-4ybsFPtPhbsNJZCgNh7t4Kwk5MgVcfKE3IUwFEXofTYCWuQGZoJU_x3SQDta5-dS23NAcohg-BghfZulUkTkM7i-vyqwmhfYCXg6fH7-eMaej2vczgVC9OG7Pm52FqDblOFg4JN4LGY6le-Td6156QzBM6x5376ZKJwERkfBI1pYsiscX8n6k1FtxqvH1838_pg5gvC3jLv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه آتش‌گرفتن یک هواپیمای مسافربری و تخلیه فوری مسافران آن‌ در آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/694579" target="_blank">📅 16:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: تحریم‌های اعمال‌شده علیه ایران یکجانبه هستند و از سوی شورای امنیت صادر نشده‌اند؛ بنابراین به تجارت خود با تهران ادامه خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694578" target="_blank">📅 16:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0571b8208b.mp4?token=f_-Z-OD1kxQlsbZZCFCblmmFEaWaEEARp18gezxyGhQeZknNLedPFmGSiOqq8tg3Gc0GsJdIK1tPW0tphedKOoVzUF9bh80htoH2owuY2yWHKlin5NXfL2_7l9LMINlserVqAQNV_7vXHwZxuqQ8bX6DMTyVASsmcyenJBsVLqzhyA0re30ekfRZwm7JW7icSg6zd5VkwJWHeXxkcLIudljxerSyhU-Tb0KHm2kre3WjbBjhbHjWuXJRICxzz5URo1QZimntkaUC9RZhlm8Fn3PBFqmgN1PJyeO3zpWBOWdE_s7-0WZu_t1EweB6llW_RXkKToL_BgltWspA3QAUsAzfA0FizVXi5WK8zey-pbnvfgzVIU94ShA4e001ToOrAkAXwVPxIPj8XRI2cPJYZhaY7QNbMdoRCGjcaZWe_j0eaPt-yLReeoQa6XNDTiFcIOTJiEXuMfph17CUbuRB4Wf9lmcpxSnP1RFqr_VUoOgdr3xpXgAe0Er5_OtxlKbKikJyGognGJlZsQMASSKlz4dMm6Gbbsoilxxn9PGu1oPZHpSBF2WWJFGBCHkuoFbAC0DjDswLTiPCdrn-Nr9crSrtC-DQxA74lbY9mFJ3AnClw20oh8Uep7yunN80aVSAEGQa8Y6uMvZFZ9vbR_pKMikwUBtcSouYj03cIEnaJkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0571b8208b.mp4?token=f_-Z-OD1kxQlsbZZCFCblmmFEaWaEEARp18gezxyGhQeZknNLedPFmGSiOqq8tg3Gc0GsJdIK1tPW0tphedKOoVzUF9bh80htoH2owuY2yWHKlin5NXfL2_7l9LMINlserVqAQNV_7vXHwZxuqQ8bX6DMTyVASsmcyenJBsVLqzhyA0re30ekfRZwm7JW7icSg6zd5VkwJWHeXxkcLIudljxerSyhU-Tb0KHm2kre3WjbBjhbHjWuXJRICxzz5URo1QZimntkaUC9RZhlm8Fn3PBFqmgN1PJyeO3zpWBOWdE_s7-0WZu_t1EweB6llW_RXkKToL_BgltWspA3QAUsAzfA0FizVXi5WK8zey-pbnvfgzVIU94ShA4e001ToOrAkAXwVPxIPj8XRI2cPJYZhaY7QNbMdoRCGjcaZWe_j0eaPt-yLReeoQa6XNDTiFcIOTJiEXuMfph17CUbuRB4Wf9lmcpxSnP1RFqr_VUoOgdr3xpXgAe0Er5_OtxlKbKikJyGognGJlZsQMASSKlz4dMm6Gbbsoilxxn9PGu1oPZHpSBF2WWJFGBCHkuoFbAC0DjDswLTiPCdrn-Nr9crSrtC-DQxA74lbY9mFJ3AnClw20oh8Uep7yunN80aVSAEGQa8Y6uMvZFZ9vbR_pKMikwUBtcSouYj03cIEnaJkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهنام ابوالقاسم‌پور با حضور هیات ایرانی در منزل شهید حزب‌الله: قهرمان‌های واقعی اینجا هستند؛با وجود حضور در خط مرزی، خانواده شهید خانه و منطقه خود را ترک نکرده‌اند/ من به‌عنوان یک ورزشکار، شهید محمد را که هیچ‌وقت اینجا را خالی نکرد، الگوی خودم قرار می‌دهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/694577" target="_blank">📅 16:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
آغاز خروج اضطراری اسرائیلی‌ها از امارات
🔹
روزنامه «یدیعوت آحارونوت» از آغاز انتقال حدود ۱۰ هزار اسرائیلی از امارات به سرزمین‌های اشغالی از روز جمعه خبر داد؛ مسافران تنها مجاز به حمل کیف‌دستی هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/694576" target="_blank">📅 16:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dadef9e3.mp4?token=EAXUzzrzEtR8n1e1fzO0IHFXO6O9J2VlX4aiIwTjvBay3JznPGc_4N48kOFcbUrnQkTbit6azVc9bzGQTpT8OiE-tQmQZwuf1w8zNHptH1lcPi9IOm2yTaqf4fhnQN-vrAG9BySTT-tN_NA23Ei6WXt14dO_3Hf58elqULNovUyxkaqd50BFJuL4LnSALl07uTnz57CnnpcgILAxxv5qY72WmwpJRhABHnrxPojXUiroMPEYoesQj0WAjoHc47bZeZk0d8crScRpmLuegeCM6ZxRjrwGLWSCdZShNyzoAW-M00x_OWugL6PeFNZrGEy2VmxPwgt7iwtpire9pZ678w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dadef9e3.mp4?token=EAXUzzrzEtR8n1e1fzO0IHFXO6O9J2VlX4aiIwTjvBay3JznPGc_4N48kOFcbUrnQkTbit6azVc9bzGQTpT8OiE-tQmQZwuf1w8zNHptH1lcPi9IOm2yTaqf4fhnQN-vrAG9BySTT-tN_NA23Ei6WXt14dO_3Hf58elqULNovUyxkaqd50BFJuL4LnSALl07uTnz57CnnpcgILAxxv5qY72WmwpJRhABHnrxPojXUiroMPEYoesQj0WAjoHc47bZeZk0d8crScRpmLuegeCM6ZxRjrwGLWSCdZShNyzoAW-M00x_OWugL6PeFNZrGEy2VmxPwgt7iwtpire9pZ678w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌ترین راز رشد گیاهان از زبان خودشان
🪴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/694575" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
خبرنگار نشریه‌تایم: درباره ایران، آیا قرار است پس از انتخابات میان‌دوره‌ای بمباران‌ها را تشدید کنید؟ گزارش‌هایی در این باره منتشر شده است
🔹
ادعای ترامپ: ممکن است. ما سلاح‌های زیادی داریم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/694574" target="_blank">📅 16:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV_Wh0Epbxv1rd4TeNgTyChfbb23zHJobjUV_5Q6k0zCW9_1rBi3XmcZQH8tOlbOKyQhFeO72z8o4dmmVlheA-kEMht1HnoloXSPB4fDh0W9xBofIYtVgcgd8632oAH1jQxJ3wb4ZOeSXhXi26vBjc3EAtTg8FUrOpu19WF8CODuIaz7DcO4jUhHWnU3LXHPo59J_whmoJR5ViaU5f9RwwYBwmC_YT4nexybDS5w8xhazaJyLbu49iPrVV5FUeiGJvyyH2jVxkZUn2jk73mFb7ly0OFVjBZzWpjAkY8NqSHhjvxg_ldQNHGvEr9xbJkDLhpG79wPgy5e5QwamW8z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف اینترنت اینستاگرام رو کمتر کنید
🔹
برای اینکار نیاز به فعال‌سازی Data Saver هست:
Settings > Data usage and media quality > Data Saver
🔹
با فعال کردن آن، اینستاگرام فرایند دریافت محتوا را بهینه‌تر خواهد کرد تا مصرف کمتر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/694572" target="_blank">📅 16:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
حاج حسین یکتا در منزل شهید حزب الله همراه با هیات ایرانی: در جنوبی‌ترین نقطه لبنان و خط تماس با دشمن، مهمان خانواده شهدا و رزمندگان هستیم/ اینجا همه یک سؤال دارند؛ «حال مردم ایران خوبه؟» پیداست که یک امت و یک ید واحده هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/694571" target="_blank">📅 16:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOFGxVpRdWYauraV3mJ4zMPHujwCqDxxHBeOTZy5Y3iNMWJh2Ejp8pqxNc-SXEOUgzfKI23dmCkd73FxIDzVINyHpZ4GBlasikPkFOuAbxCNFmXrir8QMecDPlIpnHbHMKaP_TMYaI9BtO3s4pbcxEnNTIrHblInDPBF2bTavnyUUnROGvul6D7uBbOww9pVvq4dUYfMJkLmDRouIUM2XhwEqup2_v9Vq-hzfxt3ulFST2fpF0lH3l-t-VfzBdcqacJdoI1gnplVGM2AbzOclFeTqFMXidzXz1zTjRYMh8dybC5bsYoIA3aI49Rw8n_mo9YIEhO895fcyUdOPXZ4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش نخست‌وزیر عراق به پایان حضور آمریکا در این کشور: از این پس تصمیمات امنیتی و نظامی کاملاً در انحصار نهادهای دولتی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/694570" target="_blank">📅 16:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای‌نتانیاهو جنایتکار: ما می‌دانیم که خلبان مهاجم، تحت "فرآیند آموزش و تلقین افراطی اسلامی" قرار گرفته بود #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/694569" target="_blank">📅 16:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4ef28a16.mp4?token=PPNTGjxD4x8zVtSXwj-n5ANA5eVdakfyPS00mchLcFtrO-xQITTfGDuvHcIrRxg1NJiHp0hy6Lcg6XG57Ujxm7jR_qCukz5fPasfVpoSCX7hsJeCJDel7OqrSTfYb4VWAVRvAxY4XoMOguF1gx1eXPpTLpb8Y_JKdVv9wRqQK2l7oflnRbotZX9MCd6yZkC-0gz5kNtjmwxHuvgQXqWZzgQ2Chg5yzRlatXg91sQRgal5WhEqnpi6su7QMwAaSsw4fgsBkqPSFHRGg-E7waW5PvHJz3_0eRO7vfLDgwCTkvSectw2imw1x9AuEpVa4qvlr5II8UOVfWRZRPW3KsFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4ef28a16.mp4?token=PPNTGjxD4x8zVtSXwj-n5ANA5eVdakfyPS00mchLcFtrO-xQITTfGDuvHcIrRxg1NJiHp0hy6Lcg6XG57Ujxm7jR_qCukz5fPasfVpoSCX7hsJeCJDel7OqrSTfYb4VWAVRvAxY4XoMOguF1gx1eXPpTLpb8Y_JKdVv9wRqQK2l7oflnRbotZX9MCd6yZkC-0gz5kNtjmwxHuvgQXqWZzgQ2Chg5yzRlatXg91sQRgal5WhEqnpi6su7QMwAaSsw4fgsBkqPSFHRGg-E7waW5PvHJz3_0eRO7vfLDgwCTkvSectw2imw1x9AuEpVa4qvlr5II8UOVfWRZRPW3KsFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جانی: ما می‌توانیم ظرف چند روز مشخص کنیم که آیا کمک خلبان ارتباطی با ایران داشته است یا خیر/ الجزیره  #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694568" target="_blank">📅 16:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd932658.mp4?token=uvwnfysO7WUKZt7PzjxTZDJNtPwBe2vvCaK0HLEurKfZ-BdW9MDNuHFrl2iBKTl3SB4gHYtqHhtIDHMwxYKs8uMxXFiYlE77tSry2XKgHBjUzDIZ0w0_VSCBl_3Ob-q9CFfm0W1JOgtS-BHH_QaTZo81Dw-jMkD4PuQvtAQhqVOlE4dYhWRXXvU5sQfLwA6CYS2foS6E96uPLeTl3N3WTcmOjCH0A1kWxIr9np_TDTXtc1AfvoW7VP2LEyAc2UdRG2E6SJrOlTyVDjjytvuJ4AGRCcna_rmB46L9hx3qwvNzHfRZq8KzNgkHhXD9y7XXGnIR2fbxYXA-0w0iaxe6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd932658.mp4?token=uvwnfysO7WUKZt7PzjxTZDJNtPwBe2vvCaK0HLEurKfZ-BdW9MDNuHFrl2iBKTl3SB4gHYtqHhtIDHMwxYKs8uMxXFiYlE77tSry2XKgHBjUzDIZ0w0_VSCBl_3Ob-q9CFfm0W1JOgtS-BHH_QaTZo81Dw-jMkD4PuQvtAQhqVOlE4dYhWRXXvU5sQfLwA6CYS2foS6E96uPLeTl3N3WTcmOjCH0A1kWxIr9np_TDTXtc1AfvoW7VP2LEyAc2UdRG2E6SJrOlTyVDjjytvuJ4AGRCcna_rmB46L9hx3qwvNzHfRZq8KzNgkHhXD9y7XXGnIR2fbxYXA-0w0iaxe6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر فکر می‌کنی دیر شروع کردی و به هیچ دستاوردی تو زندگی‌ات نرسیدی، این ویدئو رو ببین! #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694567" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d731a499.mp4?token=XxHiXdD0nu-95swkg5Wgn_2_pDsQVC0_bGWZ0WYWJRMnToejFqQwHT3ORX6QFHP_NIn8B9AbFcReWE9geyxIy5zB1ubTKtXsN4kJHg-jRlgp5ttGN9dDQvUjO-CYw0z1syiijiPYTH9GiNcxjAtb2yeDZt2QZOW5DJC-F2KMLkLDx9s4l52-fF5RAac_jQYX-hpQHOlhlnv0un1uvaIDY2M907NnD6ntvxUM48JHJ2Q8Y6wqBzsPURF5B6jooPXyXJiD8E4qmO6Vgbaz1YLmAf6Ycqc1JHES45lz1SA6H-RwlBO0gtl7cBcsAF4bVc869bhBxRQeCrJizzpqOQjqITPmhU6HssclnlXQa_sb1TV9EIPBW7HhEpJY-nIHmMuyzydkYLQdS4PSCUslx4iHqo0G3r-3_XPSZDzOBcb-uGSTTgL_0djBsOFxvy1sPCkE1sNqZD1_ODt-rQOGpWfvC2z8h78gbu-t9MyS-C6gWqezr-TyhZ9YahjdSazbZM--d28UVSdGyMKVFWOzZOxStitA9ozGrHbVsqwyyTy7gp5e-2VVHD0z_evyJ6OZBE9sANLGHDUIiaH8zD2oYQniijSgJRNdgt3u3zyrizKgZKag7Pa9LthwQ6bSkOYNf7IgRpirld3F0DNxmZdMY9Qa9ubuA4nl1PrCvbVd9ppbUZc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d731a499.mp4?token=XxHiXdD0nu-95swkg5Wgn_2_pDsQVC0_bGWZ0WYWJRMnToejFqQwHT3ORX6QFHP_NIn8B9AbFcReWE9geyxIy5zB1ubTKtXsN4kJHg-jRlgp5ttGN9dDQvUjO-CYw0z1syiijiPYTH9GiNcxjAtb2yeDZt2QZOW5DJC-F2KMLkLDx9s4l52-fF5RAac_jQYX-hpQHOlhlnv0un1uvaIDY2M907NnD6ntvxUM48JHJ2Q8Y6wqBzsPURF5B6jooPXyXJiD8E4qmO6Vgbaz1YLmAf6Ycqc1JHES45lz1SA6H-RwlBO0gtl7cBcsAF4bVc869bhBxRQeCrJizzpqOQjqITPmhU6HssclnlXQa_sb1TV9EIPBW7HhEpJY-nIHmMuyzydkYLQdS4PSCUslx4iHqo0G3r-3_XPSZDzOBcb-uGSTTgL_0djBsOFxvy1sPCkE1sNqZD1_ODt-rQOGpWfvC2z8h78gbu-t9MyS-C6gWqezr-TyhZ9YahjdSazbZM--d28UVSdGyMKVFWOzZOxStitA9ozGrHbVsqwyyTy7gp5e-2VVHD0z_evyJ6OZBE9sANLGHDUIiaH8zD2oYQniijSgJRNdgt3u3zyrizKgZKag7Pa9LthwQ6bSkOYNf7IgRpirld3F0DNxmZdMY9Qa9ubuA4nl1PrCvbVd9ppbUZc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهنام ابوالقاسم‌پور در لبنان: به‌عنوان نماینده ورزشکاران به دیدار خانواده‌های شهدا رفتیم و انگشتر متبرک آیت‌الله سید مجتبی خامنه‌ای را به آن‌ها تقدیم کردیم / تازه از نزدیک فهمیدم مردم لبنان با چه شرایطی زندگی می‌کنند و چقدر نسبت به ایرانی‌ها محبت دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694566" target="_blank">📅 16:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای نتانیاهو جانی: ما می‌توانیم ظرف چند روز مشخص کنیم که آیا کمک خلبان ارتباطی با ایران داشته است یا خیر/ الجزیره  #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694565" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اطلاعات میلیون‌ها نظامی آمریکا هک شد
پنتاگون:
🔹
اطلاعات شخصی حدود ۲.۸ میلیون نیروی نظامی فعلی و نزدیک به ۳۰۰ هزار فرد فوت‌شده آمریکایی در یک حمله سایبری به سامانه اطلاعاتی پنتاگون به سرقت رفت و هویت مهاجمان همچنان مشخص نیست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/694564" target="_blank">📅 16:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe71894de.mp4?token=N5KLExrAFFkdcsDoG99yOZfmGwns_Z6s3g86LSkacotSfh095fq-RbWd8lMq5q41hKXsYw-Qu4RC9XtvK8GMit79nkdumwQZZIGyuxf_NAnNacVpq50R9aLHHsunCSHEqgqBqn65xs26hWNL-ki7JwXXhsv_bt5tO7rtMsTlhBPoLvV9_Z0FANXaAVxwKjYbkSxM5iM4xAOuLMvA3tOnoM4dN6jMGDOYcP8W-oo1F_MBl66iHgfy4Y_6p8cUQV8Xxhg-FZDy7IbK0ijnJaND2uayv8UWi_YhYZrt4Dv_PzpBGQDOpVxI4OFrVa5DLtqyioFW15cGzRUdhtQBqcLVag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe71894de.mp4?token=N5KLExrAFFkdcsDoG99yOZfmGwns_Z6s3g86LSkacotSfh095fq-RbWd8lMq5q41hKXsYw-Qu4RC9XtvK8GMit79nkdumwQZZIGyuxf_NAnNacVpq50R9aLHHsunCSHEqgqBqn65xs26hWNL-ki7JwXXhsv_bt5tO7rtMsTlhBPoLvV9_Z0FANXaAVxwKjYbkSxM5iM4xAOuLMvA3tOnoM4dN6jMGDOYcP8W-oo1F_MBl66iHgfy4Y_6p8cUQV8Xxhg-FZDy7IbK0ijnJaND2uayv8UWi_YhYZrt4Dv_PzpBGQDOpVxI4OFrVa5DLtqyioFW15cGzRUdhtQBqcLVag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج از نشست به یاد ماکان و هم‌بازی‌هایش؛ وقتی قاتل هزاران کودک در سازمان ملل سخنرانی کرد
🔹
ویدئویی پربازدید که پرس‌تی‌وی از نشست سازمان‌ملل منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/694563" target="_blank">📅 15:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای نتانیاهو: خلبان هندی ناجی جان ۱۷۴ اسرائیلی در پرواز فلای دبی بود #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/694562" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe40db7c0.mp4?token=MI7axdmIhlAS-3bC-2k5nxdtEEUbnMYpN3d8Fqw0nj46WRy7PcS4rC6E_g2xcGSN8KUXjizT08r4w0cbsKIr7mrlKYt033G-Ct9JMWk2PXXqbiMTLjJc40YbhEAkIkw1R3e1FjqqPKFuXbAyjZTg6dZfV2e7I12VWPA26IHfopLJiNsGzlAE7aAVE_2brSjiC43Pgch71s0G3euwZu8YAmpvjFsJB2DL92YUV3rgsOAzV2o24RUe5Rse-zYkC6w_kujHWCEj7nymC6jY7Kylq-YvfNNMj6wyiwW7qYwN4mOKKhx8Ur91YsBMzYY4vu0WheCZYgnzCo4WnAJ31mmUyLSn2nx2votCI8IWdFdizyi1ICVgDBJkL2sUq56dk7R5oB3GC3_aA08COD3zsbgW26jPJNwhX0VkZwAGoz6-t1kZ_OBwVtj8ACFUoNqEU_gnuZGXyOmePMWsfRWxZFb1OLug2JQjCMMYuIuA0D1V36EUGWL5tYoXvo2VyrMXLl5Eo5HuIWW74wPtg-nLQ73VpM7kjMFs3Nhg3EfFPsrsGa-ZVyOcakVXdvucRriV18vgyfq1kGyZkVhGn7qL84wehqS1D35HLpuPdgpYRudqb6qCnnNAsltu5FmT_-c9JuQziwtmXJN_QkMNw7uCGCcAiMMwS_tO96ylxwUGm-FJgUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe40db7c0.mp4?token=MI7axdmIhlAS-3bC-2k5nxdtEEUbnMYpN3d8Fqw0nj46WRy7PcS4rC6E_g2xcGSN8KUXjizT08r4w0cbsKIr7mrlKYt033G-Ct9JMWk2PXXqbiMTLjJc40YbhEAkIkw1R3e1FjqqPKFuXbAyjZTg6dZfV2e7I12VWPA26IHfopLJiNsGzlAE7aAVE_2brSjiC43Pgch71s0G3euwZu8YAmpvjFsJB2DL92YUV3rgsOAzV2o24RUe5Rse-zYkC6w_kujHWCEj7nymC6jY7Kylq-YvfNNMj6wyiwW7qYwN4mOKKhx8Ur91YsBMzYY4vu0WheCZYgnzCo4WnAJ31mmUyLSn2nx2votCI8IWdFdizyi1ICVgDBJkL2sUq56dk7R5oB3GC3_aA08COD3zsbgW26jPJNwhX0VkZwAGoz6-t1kZ_OBwVtj8ACFUoNqEU_gnuZGXyOmePMWsfRWxZFb1OLug2JQjCMMYuIuA0D1V36EUGWL5tYoXvo2VyrMXLl5Eo5HuIWW74wPtg-nLQ73VpM7kjMFs3Nhg3EfFPsrsGa-ZVyOcakVXdvucRriV18vgyfq1kGyZkVhGn7qL84wehqS1D35HLpuPdgpYRudqb6qCnnNAsltu5FmT_-c9JuQziwtmXJN_QkMNw7uCGCcAiMMwS_tO96ylxwUGm-FJgUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژیلا صادقی در مزار گلزار شهدا لبنان: آنچه در جنت‌الزهرا دیده می‌شود تداعی‌کننده اتحاد و غیرت است؛ در ورودی این گلزار مشغول نصب تصویر رهبر معظم انقلاب هستند / امیدواریم جشن پیروزی جبهه مقاومت را در کنار مردم لبنان برگزار کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/694561" target="_blank">📅 15:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1761a9ad21.mp4?token=C1cyEIP330pClF3RRJtF7Bh7VW8soPlc3jmYIBAb2PGHnXo0G6fr0esPod_nllWATnK7uaulrxVPJrDuJdr5zk_ruCUwm9V49pfOmRTpL_6k7Xi7BHpF9jl9y9ed28p85aX80Zrecjk7TLG-cE5zs-1nd6940VaNAk0e1xapnF4o692_wOSTZuBSHDD2Q7NpBL2K47HVsWiK8seWl8Yz43S9at-5QSWbnEv2dBoflaskllZJ410OGe-rndbyT6JmJCCHvb7w-F0_DtzfnQyIG4ivHYXgrvtDDl3IYb7vTYIuAWRJbqrI7BrRp7AOBexQXtVkRKV5coBHWFBxi9Xu5Zk3MSOYGaN9ik80pSvUwjh8OcA1VBRPEh3CYaleYmQj8yKY4mw_UArHZXYBC0KEGZvsIxMfgShmvqnwEj0km1rMIaoouQMZGl16xwfBn7AoJEog2Q7jJQfCoKQS30TH-8weNnlH0fFdzuJRcWXvOMDgsy6oa50dxSTJIfGfjgnK24qfzFFTZpNQ8VW1JtoochSstiqNfHwachE34m8zVhjdamwkUmNAxBUc1OPjQ68frOQY0r5Ie2wZHjKDiAmaTLsAJ-obSAqT7gO80nMzhnhpgjhd5n7jyhGwZWFIqZtr9RdWpAqR90FQvtLeDs-SUl1S3ZQF5CdXRWziIJjIWAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1761a9ad21.mp4?token=C1cyEIP330pClF3RRJtF7Bh7VW8soPlc3jmYIBAb2PGHnXo0G6fr0esPod_nllWATnK7uaulrxVPJrDuJdr5zk_ruCUwm9V49pfOmRTpL_6k7Xi7BHpF9jl9y9ed28p85aX80Zrecjk7TLG-cE5zs-1nd6940VaNAk0e1xapnF4o692_wOSTZuBSHDD2Q7NpBL2K47HVsWiK8seWl8Yz43S9at-5QSWbnEv2dBoflaskllZJ410OGe-rndbyT6JmJCCHvb7w-F0_DtzfnQyIG4ivHYXgrvtDDl3IYb7vTYIuAWRJbqrI7BrRp7AOBexQXtVkRKV5coBHWFBxi9Xu5Zk3MSOYGaN9ik80pSvUwjh8OcA1VBRPEh3CYaleYmQj8yKY4mw_UArHZXYBC0KEGZvsIxMfgShmvqnwEj0km1rMIaoouQMZGl16xwfBn7AoJEog2Q7jJQfCoKQS30TH-8weNnlH0fFdzuJRcWXvOMDgsy6oa50dxSTJIfGfjgnK24qfzFFTZpNQ8VW1JtoochSstiqNfHwachE34m8zVhjdamwkUmNAxBUc1OPjQ68frOQY0r5Ie2wZHjKDiAmaTLsAJ-obSAqT7gO80nMzhnhpgjhd5n7jyhGwZWFIqZtr9RdWpAqR90FQvtLeDs-SUl1S3ZQF5CdXRWziIJjIWAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی سیلاب اخیر گرگان، این موش هم برای نجات جانش دست به هر کاری زد!
🐀
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/694560" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR6xpKOUHdg9wTOQEtuhSdH2yJiugSFi35o_NgXHSewubBlPdkznhVZhKcg2XmB_Pmuaxc1IXcLS7nSzVTv9Q9Ha7t-RVBSBA8IG6VjrLZ0NPfsbg3zSpwivu-C1X6ClApmMoYAP83lnr0IY3l2r9PJrUbk9WlpUerXIpunroEqqpAKUY6hlx1i96IQwF4PnV05qZeBtIfwYlpiijnFlib31ygAmYpf7USZ5adNOoQ8K9kA4trDWa_cvhCdsU9y-ZBcSKcsoyVj-9_lpHRI_51BrxK7IjBQ1RVb7ecQSQrtaDeXNwoIQkWkje_MOFfqrNKQP7X40gXFW243lKSADQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاخیردوباره در حذف مدارس سنگی و کانکسی
🔹
قرار بر جمع کردن مدارس سنگی و کانکسی بود؛ اما وعده‌ها یکی‌یکی به موعد بعدی منتقل شدند. از «جمع‌آوری» در سال ۱۴۰۳ تا «نبودن مدرسه سنگی و کانکسی» در سال ۱۴۰۴، اما حالا وعده به «تعیین تکلیف تا مهر ۱۴۰۶» رسیده است.
#اینفوگرافی
#وعده‌های_نافرجام
@Fori_Graphi</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/694559" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3cb7d903.mp4?token=kWpKvFGIXoSSh24SlOjvlmXXIc1h-ASCfAJ2K1C-a-wa4Er66q3P729f8OZUh8ck9wEOoA8v6B26Ob_kTvdJR-VjlGqshuzV-0Ukvgwn_-kPWOGZ0GJBwbzsYt6KgOGS6jAS7GLVAIYeDgEPH2lwa46HQN0Cupv5guki831CGvULRlTIfzfC72BBoiA3-jF-nOk5qIb6ERmpj1JfAMRNXZRrU8fXtZq6QrW0bJ1wG7co5ocpG7giQrjq1V_r-4dSF2n5GKaEBxTLh-fg3ZAcQoxM1Or_JNDcRUkJnEVhyFL4U7JDW8IjV5D22lgc72u3sDj8BJdDSnj8aXuzlFezDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3cb7d903.mp4?token=kWpKvFGIXoSSh24SlOjvlmXXIc1h-ASCfAJ2K1C-a-wa4Er66q3P729f8OZUh8ck9wEOoA8v6B26Ob_kTvdJR-VjlGqshuzV-0Ukvgwn_-kPWOGZ0GJBwbzsYt6KgOGS6jAS7GLVAIYeDgEPH2lwa46HQN0Cupv5guki831CGvULRlTIfzfC72BBoiA3-jF-nOk5qIb6ERmpj1JfAMRNXZRrU8fXtZq6QrW0bJ1wG7co5ocpG7giQrjq1V_r-4dSF2n5GKaEBxTLh-fg3ZAcQoxM1Or_JNDcRUkJnEVhyFL4U7JDW8IjV5D22lgc72u3sDj8BJdDSnj8aXuzlFezDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر یارقلی در برنامه نزدیکتر:گاهی برای حال خوب بیشتر از هر درمانی به آدم هایی نیاز داریم که دوستشان داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/694558" target="_blank">📅 15:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
خبرنگار مجله‌تایمز: نظرسنجی‌های شما هرگز به این سطح پایین نرسیده بودند!  ترامپ:
🔹
اینها اعداد جعلی هستند. من امروز می‌توانم هر کسی که در انتخابات شرکت کند را با اختلاف ۲۰ امتیاز شکست دهم. افرادی که نظرسنجی‌ها را انجام می‌دهند، فاسد هستند. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694557" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
