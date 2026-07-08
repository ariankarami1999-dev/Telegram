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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
إن نقطة انطلاق أي دعم يُقدَّم للجيش الأمريكي الغازي لشن عدوان على سيادة إيران الإسلامية وأراضيها ستكون هدفاً مشروعاً للقوات المسلحة.</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/naya_foriraq/81705" target="_blank">📅 11:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">▪️
وزير الاتصالات مصطفى سند يعلن إطلاق طابع بريدي بمناسبة تشييع السيد الخامنئي</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/81704" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b35997085.mp4?token=KrMaKkJmut2zOAETVcwCyO4O0lTwDT4oBJAk8-eD9hJO1oXKj_3md2Xm-a6NQ_hQKJ38eVHw9B01Dx5EAwawY4UrVijRxinZdXO3OpfhbDTiPZCt1ncdgdw4OeUOiypASv77mGlZfNqibkYsJGVqAF_qlC3pfOAwXL1yvg_9IGexOF5Gzhp7DBDbeMZDRQFy-j8KtpejtirKgMGblMz505aRJNIDJxCcDlIcqYqfR0p_SAey6vCjo4x_1zwFMULQO_XpiX30EaLIOlYjztVNaUMVk4ahA5XRdTgA1BES_UNC-Y8i4SqSspsDq1DwDdshQrF9KHL8asMrb99nqf02kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b35997085.mp4?token=KrMaKkJmut2zOAETVcwCyO4O0lTwDT4oBJAk8-eD9hJO1oXKj_3md2Xm-a6NQ_hQKJ38eVHw9B01Dx5EAwawY4UrVijRxinZdXO3OpfhbDTiPZCt1ncdgdw4OeUOiypASv77mGlZfNqibkYsJGVqAF_qlC3pfOAwXL1yvg_9IGexOF5Gzhp7DBDbeMZDRQFy-j8KtpejtirKgMGblMz505aRJNIDJxCcDlIcqYqfR0p_SAey6vCjo4x_1zwFMULQO_XpiX30EaLIOlYjztVNaUMVk4ahA5XRdTgA1BES_UNC-Y8i4SqSspsDq1DwDdshQrF9KHL8asMrb99nqf02kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما ضم راسه يا حسين ابنك
النجف الأشرف مباشر</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/81703" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
وكالة سلامة الطيران الأوروبية:
على مشغلي الرحلات عدم تسييرها في المجالين الإيراني والعراقي.
عدم تسيير الرحلات بالمجالين الإيراني والعراقي يستمر حتى نهاية أغسطس.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/naya_foriraq/81702" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🇮🇷
نتنياهو:
الخطر الإيراني لا يزال قائما وطهران لا تزال قادرة على إعادة بناء برنامجها النووي.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/naya_foriraq/81699" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الجثمان الطاهر للسيد الولي يصل بالقرب من مجسر ثورة العشرين وسط زخم بشري كثيف من المشيعين
🕊️
🕌</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/81698" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA8TeIq2euDixQik0bjdjLtufJX7hw5YWRE_CT7uxsgJsBDLlINjZNjNaMdzDQf2V4QQUtUExL7al3sJTk8A4OeHrUX9FIikdB52IPSzr0l-EFRLr5-9yq20XGwH5NJq7kJJR7foLlQM7nQJfeUvXxYiYK-6WnElFUd3kMGn8patF5hw0PNy8VzzGGJjLBdBKVDBQPQBiK9DpgZ9SOXgCj3vJ0-KA7iNKcHPml1mz1aSVqBHSKb7XBZyiYqqKvsQCOxMNnQf1acSTupByySIOg5cNoOKrDL2ExtH3LTkSXr9KI0ctnTW_iWMprJMe46J1fP_EgUkX4Q41nvrPmvKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رايات حزب الله في العراق تتصدر التشيع بالنجف الأشرف</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/81697" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوي انفجارات جديدة في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/naya_foriraq/81696" target="_blank">📅 10:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">أصوات انفجارات في بوشهر الإيرانية</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/naya_foriraq/81695" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">استقبال العراقيين للامام القائد</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/naya_foriraq/81694" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4544c070a4.mp4?token=CxUcjmIKz4wuqQSGS4J4Kt8jXUvbX4rnyDQMaC1ybg4pTx91M6NLSkE1iS8RoIZmU2PXxfWYfrWRVrANHTJelw7UNMF63-eb5vz0ma7Syv83rXCVk_MJSekrPGNJiaasDM2f2YqQpfeYi0wy8g_isivHydbH72Gbzcb4amUhkz45a5_FXrHHXDoe6NGGciZ6N7nsgg0oZZa7TeCAKuaNVkJuvZjxqpXVb-c7sY_8PrzBG3zywIk-yH4uV7D_0zxqzF-zPXHZuyJNdSEzm7I0ihSFb9I03WW0dzAsBcOwxwgjTsz80hMLb7rMkOHev0W1GHJ48q9rAlnpjgRX9Q3yRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4544c070a4.mp4?token=CxUcjmIKz4wuqQSGS4J4Kt8jXUvbX4rnyDQMaC1ybg4pTx91M6NLSkE1iS8RoIZmU2PXxfWYfrWRVrANHTJelw7UNMF63-eb5vz0ma7Syv83rXCVk_MJSekrPGNJiaasDM2f2YqQpfeYi0wy8g_isivHydbH72Gbzcb4amUhkz45a5_FXrHHXDoe6NGGciZ6N7nsgg0oZZa7TeCAKuaNVkJuvZjxqpXVb-c7sY_8PrzBG3zywIk-yH4uV7D_0zxqzF-zPXHZuyJNdSEzm7I0ihSFb9I03WW0dzAsBcOwxwgjTsz80hMLb7rMkOHev0W1GHJ48q9rAlnpjgRX9Q3yRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر للسيد الولي يصل بالقرب من مجسر ثورة العشرين وسط زخم بشري كثيف من المشيعين
🕊️
🕌</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/81693" target="_blank">📅 10:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🌟
استشهاد أحد عناصر بحرية الحرس الثوري (محمدرضا خزيني) في مدينة ماهشهر بمحافظة خوزستان جراء العدوان الامريكي.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/81692" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJnjniXTTGyhZCVCxbQHCDN6osyV5B6H3p9Ne6lvdnhruwwG7aadiq0IFHICC9o64ELUS0eu0IH1QVynnz4uYpBTq8yxZEh7Ms4UYx5N77MACPVBqP0eEoHzyX_EciQ0fYwGBZvTXOkC5GTiAyQfxjDAjNiuRQ1-SZqsk7ehBKHcVw9TsRZTCfzRvpC2heMxJacuaRny3GybLN_yqaHKvBAAHQU4qfSD-YVOAtnnkVuFKJbTWTKKrgYSsjTDSLY4fZS-bAt2Tv2c3WUD3NoxT7fkSv4I0hQPTgY5vil_Etv4IPebDt2seG9Fw7n9uz-npoIWH0QOV93nxXQyw_XVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dn3kYmV7UdTr5G73XQRQmQ1R1v6o67xPPyEGzGHdsq_ZEpeWNn9oFcu2nKAMpbL_xOHp40NT9YnuknryBgbH5u5NApKCgGiO5-EHTMSbuNI4lXHWlu3zRD8LlpRrAMw_5BctdXm6_NFioVzDfSiaOzQiVaUEIfQl3taicrfgsMhuccJGBjKEAdYrc0Ji2jiqZPiMCt_v2kKdZy6lWGoQohs-6rUE0vgVMU46L4apJtJI2EskKl0Nx-Ku7gFUqCZptGy4hTykq97CNItJEEJq49QcScO4K0B7noAg9kvhuEHqj4HjHBzf-2D4Xm4j5xBgkgHJsjclMUlxhqs9hIvUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4DOPa7d4Ok67sWXvaHVBUAP0il-T1ptNaauAm8YiXKwuh__tZwU9U0oYRuoUoJqL1_hJBr80MdJV4oiVL-UJt4zQUd2HXPwqCMfBSyX8lYayx1qkQ9IEYGLsa2qlQ-bA9MMUAWxhYUDUzjLqcFVsvB1m6bWJgmFDUNt2VroVHdgmnioFHECyC2zc5MHKiXhvu0zJUM6NMSniSckIjHFLbwPjh8v2sSnms5en214U2OvyPN-fcZrCpjqF2IWn05eUdNVbzMuGORQ8u1bQWZoI3r5tPucFr-XAjJ593Uta4b8-hXIUqjNUZ_SJk0QRE7Jw-l36rlDcVxVcl7LVBsYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udZPX3chwhe_JS96gQzttpwwcix20uOBKIxRSN6AaVkeY1-6evDsTu-Kzfp7QY8TuruPfe2YPFw20r8KEoS1G0Lue72XgOfGCy7D-jrqXT5vnIVD9fIRqJ7x3Ahpi8a1GSQyiqeQ6elObUla7ByTlc7v8r03mLbl_o0gt21LJpZK8pBG5DL5qo3UTVWYoVlAblTD-eEJHeSdD-5JTeHz1ajvTgmgWu7iMn4_fENU4CdcAdaU_Ou42p6I-kyFggb6IbQ3cTKKavF4Qi-gDtbhIlxsSOkdTfGt8TfAxIriGmRrG6AXBmKROz5HkXwKKsEuTTekHcMsZ-o7ey3DCrCY3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لحظة وصول جثامين عائلة الشهيد قائد الثورة الإسلامية إلى مرقد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/81688" target="_blank">📅 10:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c977db3af.mp4?token=SZ1SSujtC38VDr6DGnMBKgng6iS1zlFaLwOJejOPSlbc_M-7nFZD7EgVCEGwea769_B7E7AUSH0w4gDz6Frql03XBA_TTZF5xAYD3ump8qpC1JONnCFqHS6Wnd6eX9Z8eTE_74MWKN8jFDkisquYsArG9_9wQz17_3W7gUJrxP5kkqwCaGegyK3mRPxDEdTEJSZJUWPBJFPGnzXZf60ltBntEXSyGkO0BHuPGGu2lqylafrvDBKXOa4idotyS6cd5RfIOZcYVy7Ttwxtio201NbBaaOCZ5rK0L0PVHJ3pgR1ctrteEQu5HNT6FGfL20dk9yslykiu1QnR61V5czWSF0f05D5kJNG8f3p2U8bZfFOoA6CEfQEX1sYKOv0QaviW5tEOBJESZ4VSchFZcbbMNt-nwHFLQoPC9qsip6dErKXhvMH72SZzIj1pLuo52QW_8h_pHrjd43QT2RX0e9ikc8bted3bkmG6EqDXH8lp_7YpgeOIxcYDKmf9LHL9PvEjxRdfRPXOrLfTyCyqmpq2-L0OUprjQE7CJBlhSUIja9M88bE38wFBGZHF9-33SuYAc26vH_Mz4RVitxO8HFqBPNUldjK1bJttBsQJKGc0DIxdtQDKtgAi8W9VqEdCza0uxaHTCq4qQoUQjt-NNNSfev7XKEPZHy6jgyRV_BqaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c977db3af.mp4?token=SZ1SSujtC38VDr6DGnMBKgng6iS1zlFaLwOJejOPSlbc_M-7nFZD7EgVCEGwea769_B7E7AUSH0w4gDz6Frql03XBA_TTZF5xAYD3ump8qpC1JONnCFqHS6Wnd6eX9Z8eTE_74MWKN8jFDkisquYsArG9_9wQz17_3W7gUJrxP5kkqwCaGegyK3mRPxDEdTEJSZJUWPBJFPGnzXZf60ltBntEXSyGkO0BHuPGGu2lqylafrvDBKXOa4idotyS6cd5RfIOZcYVy7Ttwxtio201NbBaaOCZ5rK0L0PVHJ3pgR1ctrteEQu5HNT6FGfL20dk9yslykiu1QnR61V5czWSF0f05D5kJNG8f3p2U8bZfFOoA6CEfQEX1sYKOv0QaviW5tEOBJESZ4VSchFZcbbMNt-nwHFLQoPC9qsip6dErKXhvMH72SZzIj1pLuo52QW_8h_pHrjd43QT2RX0e9ikc8bted3bkmG6EqDXH8lp_7YpgeOIxcYDKmf9LHL9PvEjxRdfRPXOrLfTyCyqmpq2-L0OUprjQE7CJBlhSUIja9M88bE38wFBGZHF9-33SuYAc26vH_Mz4RVitxO8HFqBPNUldjK1bJttBsQJKGc0DIxdtQDKtgAi8W9VqEdCza0uxaHTCq4qQoUQjt-NNNSfev7XKEPZHy6jgyRV_BqaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استطلاع رأي أجرها فريق نايا بين المعزين لكلمة وداعية للسيد الشهيد الخامنئي القائد..</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/81687" target="_blank">📅 10:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQm9qo75VXImJEBp9Vt-vXWnuTtwxWVIS0Kjbdqp8YgHD8-tqb_Og9ffl8FwOq916cJyCkidQco8zp8CpIb4uTgf7tlJBh6zQaxCK4O_wfZxPW7yaCE9jW4eErTmEmu1y9dONj6tZAa-nfE0Vqi9Mlsd10kpHRg_HJkMBEgbaCLIvkoyWxbisz--1Oam0b_nug064_nYth7LTEiWlATAtDCYL8DtOKcepWw795PiP3o0kKTegznFUUEF8LKrY8zNGuHRLI_We6m3jZve_qRI4TKeOSrAfAn6fw1bfr4vP9DnEtzFtx6VuXIxhwRlzPQlflw5sKDSJEV8EpGEyIjkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
بيان وزارة الخارجية بشأن الهجمات العدوانية الأمريكية وانتهاك صارخ لمذكرة تفاهم إنهاء الحرب:
الجيش الإرهابي الأمريكي، في الساعات الأولى من صباح يوم الأربعاء، ارتكب انتهاكًا عسكريًا ضد عدة مراكز للمراقبة والرصد على السواحل الجنوبية لإيران، وذلك في انتهاك صارخ للبند الرابع من المادة الثانية لميثاق الأمم المتحدة. كما أن هذه الهجمات العدوانية تمثل انتهاكًا صارخًا للبند الأول من مذكرة تفاهم إنهاء الحرب، والذي ينص على وقف العمليات العسكرية.
🔹
تكرار الهجمات غير القانونية ضد إيران، إلى جانب قرار وزارة الخزانة الأمريكية الليلة الماضية بإلغاء ترخيص بيع النفط الإيراني، وهو ما التزمت به الحكومة الأمريكية بموجب البند العاشر من مذكرة تفاهم، بالإضافة إلى انتهاك الترتيبات الإيرانية في مضيق هرمز، واستمرار الهجمات العسكرية والإجراءات الإرهابية التي يرتكبها نظام الاحتلال الإسرائيلي ضد لبنان، قد أدى إلى إبطال الأجزاء الهامة والأساسية من اتفاقية إنهاء الحرب. تقع مسؤولية العواقب الخطيرة لتصعيد التوتر على عاتق النظام الأمريكي المخادع.
🔹
تؤكد وزارة الخارجية أيضًا على الالتزام القانوني الدولي لجميع الحكومات، وخاصة الدول المجاورة الواقعة على الساحل الجنوبي للخليج الفارسي، بمنع الأطراف المعتدية من استخدام أراضيها ومرافقها لارتكاب أعمال عدوانية ضد جمهورية إيران الإسلامية، وتؤكد أن أي تعاون في ارتكاب جريمة عدوان ضد إيران يعتبر تواطؤًا ومشاركة في الجريمة.
🔹
تدين وزارة الخارجية بشدة الهجمات العدوانية والانتهاكات المتكررة التي يرتكبها الجانب الأمريكي، وتذكّر بمسؤوليات مجلس الأمن التابع للأمم المتحدة والأمين العام للمنظمة فيما يتعلق بالسلام والأمن الإقليمي والدولي، وتؤكد أن القوات المسلحة القوية لجمهورية إيران الإسلامية، كما أظهرت مرارًا وتكرارًا، لن تتردد في الدفاع عن سلامة أراضي إيران وسيادتها الوطنية وأمنها القومي ضد العدوان العسكري الأمريكي، وفقًا للمادة 51 من ميثاق الأمم المتحدة، وستستهدف أيضًا مصدر العدوان.</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/81686" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S51DFskCwHDy_kdG4T772wp0G4yZR7lhSQ6qqbWWoKH3GGG94D5mxcpXgAgdwReg3I3-dRaP9a1UhNpGbgU6NZwiC99ngAtjQ-ZMU08Ua2zeqMdZfKJCoqYG-Dv_JyjXTLCk2ynVV4NWQXo_HyUAaxvUaKTfZQkT25yCCV-zJ8II0REh2zc941iyNzYFIk8LRlQOdgmUtcJdcynfzk5YyWkPW1-6AzasV17kO3mBDQb_l9tr7O52rASIGwLPZgEJkCp-UU18__2xafgAqyKEX4rD9k0sCVPXnK20BgwXt2mKCLb140pcH9tNF8ETbjBRa8iRS-QykjsFoniBpvhUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية جديدة تدك البحرين</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/81685" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3569e18f7.mp4?token=ih_7p2nLmEeIDIE3sVZMY7YlZqJLiZVL5uLDRSLGaolaS1891m9yXUM-aBZQsr3-qVsMm6Ky6lQOOqNS2MBjsIFn8RZwjxf55oNPN0025dlOHfxTWdafSKK39bruezDXtEcPaJBwEKQwagGHZaYP3aqQpJMGhAicNo2TPJfMaJ-b1xlg3TJnH2JpiguttYFj541SOjzANbv8ksEiuAAQ-hq_EJEUEPdc6fb8ayj7WEWCq7AlQRM9sxE-DkSitcSjoTUj4WGIGxMJRCyZdPo8jS7Kr0U2-HuPeg353AzhCu96yLCaE_bgUdIWKmfUJurh457VhkJkstGMcIzyP4r5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3569e18f7.mp4?token=ih_7p2nLmEeIDIE3sVZMY7YlZqJLiZVL5uLDRSLGaolaS1891m9yXUM-aBZQsr3-qVsMm6Ky6lQOOqNS2MBjsIFn8RZwjxf55oNPN0025dlOHfxTWdafSKK39bruezDXtEcPaJBwEKQwagGHZaYP3aqQpJMGhAicNo2TPJfMaJ-b1xlg3TJnH2JpiguttYFj541SOjzANbv8ksEiuAAQ-hq_EJEUEPdc6fb8ayj7WEWCq7AlQRM9sxE-DkSitcSjoTUj4WGIGxMJRCyZdPo8jS7Kr0U2-HuPeg353AzhCu96yLCaE_bgUdIWKmfUJurh457VhkJkstGMcIzyP4r5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أُغلقت جميع الأبواب المؤدية إلى الضريح الشريف للإمام الحسين (ع) مؤقتًا أمام الزائرين، تمهيدًا لوصول الجثمان الطاهر لشهيد الأمة، حيث سيُطاف به داخل الحرم الحسيني الشريف في ظل إجراءات تنظيمية  مشددة.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/81684" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRPsGO7BO5Io4gOs9XFaxjPtIm6bzXChoqmIu6_kZ4-nBB_tvzheGbIngTlywQNZuE5qtOTJH9HCS1G2PjUBX8BblpYRzqvcIkTL_BUbN0MWhrNU60Yp3ElOIpMNswCmXMVpSgDcxGoyCrKxxztZjWm3s12lp3qMHV3Y9ehaJLCbbouurRYkaVhakX7S1QKhAsE5a_Yk8U97yovd98A1GekAR50uid4aaPs1bWfwXRMNnrRW961ejAqPXsTBQcJp6qn7aejCUUbx88gYjMxJYvx8xJdFyBWxjWM_ofIwBB-YEjreIzkmv5NBu4uPvpAPa_w8m0vVqCtd7UepzFFjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Us3S_9kzVYlkGX84Gy0sr2dO9SuKBGvRS2Co-nFqMupijGn6zie-GFQe6DsT5A7LhABC67ClW1sFzTRHI5I8HdHcr-25dSawHAJ90uEvAMCevD4YjIIXXc-m2ihZAYIs-r63Rxcpdj-2ZhuKgCExWtsD7NUibvDtxEXKTUYWnI7gaKjiGI41Sbg_f5OpqwdMHHk3mhPt_7LMoi1i55eQajQTpfbn1M4ph_zQQH-Fbk3s9JsZHlJ5_f8wCjd1vKj-nVLgcta_IkOsh_0Uwl8IC8paSa5eFX6YQhjHZxLvBVJZjOIcSJAF7OIdHciVNb8lF9uALUUxUVmLLfKspjiMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-bTQMs9aS6WI5R35o2gim8V9u8rGfQwWI3LzCMRWn2dkI-CGK3umEl4167wTVb6gdQ0CHRjVGt8V962q7WRNEpbNEvpHgpaazHKTtGr2RxEw42NF9t08buaMtYbqGPo_KwYhhAKFY8msncCSUf51m9XZRBwseJNBwpm2mEqGvmqorVWm8JR7SMvgA4w6SO-wqwUoIy3D9kBuAx8sbi4EdG0juhh5mriVsTFz75iaU0v_EYy05tyXlP_bWaaRP51bQGd_y-uFUpwvK2eVllDKhOTYFeSLLS1OYyE8Wl6ZuB6o9gdEESTtVjLaQwTbeGxpSatzrTc_il5aNe_Wjo8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTG77jq1mDMp7YhpnCMq2TNMTh6tZE8kXWdkXAl1TwDOE261mZNekfoQ7OTx69i16na7BKva51rxyT6PGQZh2wngK1FcsuiHcSH2aAKokhs0fWX9sfMMO1IEq0mhUtGAIHSu5GAJPQAV0g2a0jN9vqKsZUy3O7qSJ6SaHapR60E-kBrrhsi_SQrTXx_feEh2nBQQybWCq_CrisMYAjo1DfvBGAX0Oe3SZ0lzfU3aUtxOaGsawldHLtWhrTxBn_kW_8DbdtyxJ6-PSQpIzk5Cr3h4LonVCsSLB0WK3VzyDcziyUoWfaATFY93QnyDdbl5VB3hOcX3Wfz7U9Nk5SE4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجسر ثورة العشرين النجف الأشرف</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/81680" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81679">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">أصوات انفجارات في بندر عباس الإيرانية</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/81679" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbpPpGLgqh6gAPmZON1NT1JrP9z69QG8VATTAIlVLmTdFUYH0-aCjenAD7oKp6jUSVKmemel4FE7ej5PkW4Cxk6LvyWejtieV9qm3cW6qIY5_pPq-6zDNvWQKMcN4cL3d1PtlATmwy1ouP_XOudYrfP1zGu6tfluhdIomwASiZ6lLe_MjbKORjTVPPFte6OssWwkJN7QsKCLguyisXPpbEZW58CMoBY0V2si5GDQ4JhcDb9nnkM7vugIdWYAxUmAiy_3IhJw8D0QdRZOJb_Fqy_bnPy8MgYpi70XPPCUMQD8M5gmonyvW-RxxODmalwBB1WPr-u7idbygg_hBsmVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت تدين الهجمات الإيرانية التي طالتها
😭</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/81678" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/81677" target="_blank">📅 09:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مجددا انفجارات عنيفة تهز الكويت تحديدا منطقة الميناء</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/81676" target="_blank">📅 09:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/81675" target="_blank">📅 09:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">أصوات انفجارات في بوشهر الإيرانية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81674" target="_blank">📅 09:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الجثامين الطاهرة عند ضريح الإمام العباس عليه السلام في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/81673" target="_blank">📅 09:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقجي يعيد نشر فديو على صفحته الشخصية هكذا ودعنا الشعب العراقي من ضريح أمير المؤمنين بحفاوة</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/81672" target="_blank">📅 09:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c219ea94b6.mp4?token=kdS_wdP1mmrXwkE65r9VQ296M6FYg-C3bnYp5PVgqpwORfMz8B4ZXp22OlPXmNB6T4nVncovUWB7wKSwj7CvXzgZPheWnnXCG9Bf3kuxUlH9uld5CDMjRfufvWJQkLzNbzD_gZyFk_PF9GhwqKZItR7xEa-kQEEKyrQWT63qs-mbtXPpcQmt2WdvAAvaZyxVxhn-CJWtO-Bo57Aj4SEIhA3mR2clPN8EOWXOkIsuZBxCfq6lbzAirfAJWUvQWxAkEkt5aEotdRg58OkJD6pPv3tH_Ui1vUGnlPvyBhC2rAq7WwapvakKCwawcZuvKspuW6rFOK9_SWfx1M71Fg2hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c219ea94b6.mp4?token=kdS_wdP1mmrXwkE65r9VQ296M6FYg-C3bnYp5PVgqpwORfMz8B4ZXp22OlPXmNB6T4nVncovUWB7wKSwj7CvXzgZPheWnnXCG9Bf3kuxUlH9uld5CDMjRfufvWJQkLzNbzD_gZyFk_PF9GhwqKZItR7xEa-kQEEKyrQWT63qs-mbtXPpcQmt2WdvAAvaZyxVxhn-CJWtO-Bo57Aj4SEIhA3mR2clPN8EOWXOkIsuZBxCfq6lbzAirfAJWUvQWxAkEkt5aEotdRg58OkJD6pPv3tH_Ui1vUGnlPvyBhC2rAq7WwapvakKCwawcZuvKspuW6rFOK9_SWfx1M71Fg2hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وداعا قائدنا
🕊️
حان لهذا الجسد الطاهر أن يستريح بعد 80 عاماً من المقاومة
🕯️</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/81671" target="_blank">📅 09:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الجثامين الطاهرة عند ضريح الإمام العباس عليه السلام في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/81670" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793a6bc56.mp4?token=MTStiEqXtpWRewV2rhErLB3MKrL4Der_aWie6MYOzSFjepLdo_6kX0AxFptK8y2SHVK4-b59D53uaHGE9JCiY3fDM5n4k6c6NXFB4t2mY4KvfdLYyIpfdHNW1l7RSQ8kGIwj_cBGGucJSsNW4Lo0QiRNCT-V-oMG5G4KfLO5Srh0_JNUFuI5VUpmebHESyVhtNsBBLg5fgOqq6n9BaNImbi3SjLVjqoQMERgdiPaUwNWZRvmxF_MiqfSIkLEgc8a70d3paGIhoHLGraOMA8aRlp9h6CUY1xImEVuxIrt_Wau9R3UKSMIl7zcPCspPj9V4Obs-OWiyqFPY_7pV5n_SH-ulnN6CmxYUL1zzFFjcW3nE53GYXXoS55-MB5qqB6mYbjB4zxzByQKo8pHSdH0LYwfBvj_t4Px_pWZMMJmkzR-QRaesmFddqQ2sK6tGK3fGrpITmjFMox0emeUshYmEMVxI9jGJCyeNHHbhJ_lr1qjgdRtEy9EPfq24Cd0UWp-zzW7w8gofchFmFtXk3ik3ZjzZX-2BtRTA2m-jFFBpy2oIcm_6TuT5vW7JygTaMMWaB-rEx9mqVeU-P3plk6tkQTw52VB-PjgLej-M_4bQ6cEIl0cFghyafHOdwOdrEAW0PCHkYGkmR8TVED8tcswBT-dj9KJzGdTVL46hoW9b74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793a6bc56.mp4?token=MTStiEqXtpWRewV2rhErLB3MKrL4Der_aWie6MYOzSFjepLdo_6kX0AxFptK8y2SHVK4-b59D53uaHGE9JCiY3fDM5n4k6c6NXFB4t2mY4KvfdLYyIpfdHNW1l7RSQ8kGIwj_cBGGucJSsNW4Lo0QiRNCT-V-oMG5G4KfLO5Srh0_JNUFuI5VUpmebHESyVhtNsBBLg5fgOqq6n9BaNImbi3SjLVjqoQMERgdiPaUwNWZRvmxF_MiqfSIkLEgc8a70d3paGIhoHLGraOMA8aRlp9h6CUY1xImEVuxIrt_Wau9R3UKSMIl7zcPCspPj9V4Obs-OWiyqFPY_7pV5n_SH-ulnN6CmxYUL1zzFFjcW3nE53GYXXoS55-MB5qqB6mYbjB4zxzByQKo8pHSdH0LYwfBvj_t4Px_pWZMMJmkzR-QRaesmFddqQ2sK6tGK3fGrpITmjFMox0emeUshYmEMVxI9jGJCyeNHHbhJ_lr1qjgdRtEy9EPfq24Cd0UWp-zzW7w8gofchFmFtXk3ik3ZjzZX-2BtRTA2m-jFFBpy2oIcm_6TuT5vW7JygTaMMWaB-rEx9mqVeU-P3plk6tkQTw52VB-PjgLej-M_4bQ6cEIl0cFghyafHOdwOdrEAW0PCHkYGkmR8TVED8tcswBT-dj9KJzGdTVL46hoW9b74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جثامين عائلة الإمام الشهيد الطاهرة في حضرة قمر العشيرة أباالفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/81669" target="_blank">📅 09:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6a0226b7f.mp4?token=BUCJNS6wWP-uqoO_iPTTapxNaOTX_4xAQKDickeh_VmGcUWzuhfFzywCE3iCkTiT4wtkzJOK0IJwp9xs3cCMvwhIXP1-BBGyZXlahfQuShy_XM1Enl4pOegIa-OV1ug1JBzA0aajAopn69Lq5VJ4k0dvfoywe6P4f2xUGF0xeNfUhyp2TaPoXAmH5Y1X-t7aJ_MII3dctj5kqutU2tnnRAt0OGzILDzTV_mkRTxcr9UU0c7OD04ytVG6O3O4PV7GTfmb6kWsCswdw1BmM9U9is1YeX82iLfJbn1CPJuoDb5aM2wzLIPeDV6njm0J-C_HWOzt779GXRrIlctYy_YFAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6a0226b7f.mp4?token=BUCJNS6wWP-uqoO_iPTTapxNaOTX_4xAQKDickeh_VmGcUWzuhfFzywCE3iCkTiT4wtkzJOK0IJwp9xs3cCMvwhIXP1-BBGyZXlahfQuShy_XM1Enl4pOegIa-OV1ug1JBzA0aajAopn69Lq5VJ4k0dvfoywe6P4f2xUGF0xeNfUhyp2TaPoXAmH5Y1X-t7aJ_MII3dctj5kqutU2tnnRAt0OGzILDzTV_mkRTxcr9UU0c7OD04ytVG6O3O4PV7GTfmb6kWsCswdw1BmM9U9is1YeX82iLfJbn1CPJuoDb5aM2wzLIPeDV6njm0J-C_HWOzt779GXRrIlctYy_YFAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جثامين عائلة الإمام الشهيد الطاهرة في حضرة قمر العشيرة أباالفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/81668" target="_blank">📅 09:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9042c0965c.mp4?token=odt8TekeOeZTsMKCNEKlItuqWfKWhxrjswylkMdnGd3Ft-vvJfyigEB07kxy_aTLJMRxcHccrrLY0ps0OQ7VBUwAWLMWDu7QSiBW2WLCn1g643vGHENCrTQdSFHMKeQe3q0qItHvoCgs_ZowYGr7mPLOcipGqdMwtkVKojySidl0hyaRbrYyhAVq91LBuo6uiQnKh1mpXKL7YfPzd0HnJdMxWVjBgWzIRmk2epn3IfegxuFoTv5NYo7O8OiGTdsWgHY3W0K3mBlAmHj09fV2n4oL3O0st6Qkn6hHnW-rLCJJLnXqKxjUJRjGcLuGINlByI51d4enaNb_M0xneNi3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9042c0965c.mp4?token=odt8TekeOeZTsMKCNEKlItuqWfKWhxrjswylkMdnGd3Ft-vvJfyigEB07kxy_aTLJMRxcHccrrLY0ps0OQ7VBUwAWLMWDu7QSiBW2WLCn1g643vGHENCrTQdSFHMKeQe3q0qItHvoCgs_ZowYGr7mPLOcipGqdMwtkVKojySidl0hyaRbrYyhAVq91LBuo6uiQnKh1mpXKL7YfPzd0HnJdMxWVjBgWzIRmk2epn3IfegxuFoTv5NYo7O8OiGTdsWgHY3W0K3mBlAmHj09fV2n4oL3O0st6Qkn6hHnW-rLCJJLnXqKxjUJRjGcLuGINlByI51d4enaNb_M0xneNi3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النجف تودع السيد القائد.. انتاجات نايا على التلغرام</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/81667" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peg4zuroZBZapTNDm1qgHm0LbSCPyoWxV_sFBlzNkNEs1eS5l7mE6-CfeSAmPBx6lNDzl-j1nFOe6WS82SVbj7Aaee6ks2nXOsK_pzmO3VmnrC1K2HVFipFAs3bdyvPDZEL-lAuNKtOPyLj-Fb_EfQLISjQcYN3juoZKSywnU8O8BLg2R4-PipCiWQZnACBhAVy0EkeEzfnfp6zpakvmHjvSB45WrnlCmt3CMV7HoPT7zIkRo8KhQ6nXORdhyVNLk3Kt8CEr0lGPNbNVLJBgeTljlgGHTs_2L-TAjfrz7eNpx0f8N2fwH8oeARnJ3kotA8Jo6jjdFAsZHhdNeXGz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQ3wdc54GmifLshFwB0wCtQAfDf8OofN0ji4QpCvJa97U0D17hnVs2KcwZxwczWiaM9FJZoPoSsh3f48xhI_iNOhBoqRLB0lkBrDdbOtk6PKa3_HOdlQ5o5So8Y_V8qgVGGJt0O7-sjfpPuVs9VOZS_RXqVg4GRfZjCiiHFvMytYV6jG5KW5sljrQoT4Q4F1Sgq5hfNJpewZ94slM_-9u7RckTXqN7xixw2KR4qtm4lr7UnajA_idBDdUbZwjWIDwmcnKRv-zktZuLCmx7Qu8NxyNeQ1E7VfkEk-i53Lx-NJ-BTqIdPr5MJ0OigvCifvcpp-4hsDrancCxxaa0kqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O01PrGoEJ8dUCvE6GFPcvlWmkT9zfTZDGXXP8EiY8bD8J1BTTifD_jCAyNatL3bT51_r0Vy8-Q8mQkj16W7LTFReC3BcUxJthYA3HCXTG6hYaBEVdFC-HU3I38oCClYM_Wjpfl_7y17JVrfQo5JCbFlewj27MOrqFOehs3HZo10mEXuS-fUW97sZLiTDQMA1sTBCv-qjw-GAl8bMRGlpor4xEN8fYFXYT6VhgK6RLd4CY3nQwNrfDVq7KDZGttD-iaUwjuMr9GNP3NKb7_pr--fiRwPUPKsYO4NIMO-SnRBgd2QvYRLnKDvVn5UwhgwaDZ1Yc4tIG_iglEs9wbP6KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">التشيع بالنجف الأشرف كان محاطا باعلام فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/81664" target="_blank">📅 09:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or2vBd-2K8LwbjSGHCTn35mN_QPWs1iFDmVETK1SboQW7WcOiSiHeX0Xh-lcRcQMC7b4JTjdTEZVI5imyYflrso4K5yOt-QOR3p-agKwt6k1oDzcKMmW1BRktf4LdgtkmL1okePC7GuFUmvQ38gpD9kuTH49qZzuypQWR8iy4gqRsMHf6nHs7ujj2dMVehxnVAx93a68ipSTGUfxGpANzDBs__b06clJIdHu1kI9lLNkXxzwrme6qU6Zt6kZEmrt2k9dOBOiMhEJMSqjvVbkpkPVMp7Irs1qyBgE4LCfe9-pspH8chM9PPhoxngA5-EOPIWbZ-ydTMhCdNzgHP3rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nfd5x7a6Z4tfKLJBr7mcYYgnzfx1ogt4ZHt0ZuKHXmLx_UqCd-aot3Ph5ozuObWKH5OY-ltIf_eZRNa-XMFfNff56QfHKRYXnXabXTIDj4iNvcJLxJkJOQiYajhEMUF1OeGHygjpS1K5I8MGED6UMDXBjGqtdz8EQRBVoBYUCnX3Zjmo0hEDBOK37GCFImD1yKv_mAoPFjt6nCkY89uyPmdcyYOwS71ILXYa7aRuy7D0ZaDLvLcVUd2Sr_7UhAE5FPm0WSUd5tvOlK2clLmqWmTfR-ryREsX3XguvWrKe8OCz4vTypOLY0G3-6NgJr7Y7CNq7TzD1eBvdhEDqzrfFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تشييع جثامين الشهداء من عائلة السيد القائد الخامنئي في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/naya_foriraq/81662" target="_blank">📅 09:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQ4-YCwT8s1k4h36J4JLrdkpMWXCNbMrSmzU_ufO_DL-ZoMH0rtLh91h0ov1YxFuxQbHHq6MKrdy-y-8agMKQZPHJmt1DCMq7bsGddY2xlNwWvtbFyzm7HUtfCV66Ogy6Un8DtAGuAv5DXZZ21MAiIeuUWVyPBCO3dzsvTqwo62Mfhzl1SBIkF1ajR7sZ2IbCawmAO2pQy0ciXz15IVKuhMRqH9Pfm2Vyo2Gh-SpXyJVVdoHmNbqNKGY3McqPjPOeR-1Wkct7fsasNrcSmH9R4bY8XaZUvsiNOr0QHZOl1UljtCZuDpkVWYOtiPJOjM1scMeW3AJea0BH5XUEhUokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMr3Kter8xD_Y2OOZHlF9IQwuyVsyVrT6wQ4xgXmtvz0DuwVYgKOJR40zUFltKb4sRnRL2f9fo-IuCl09Bs3xnxlwVJ6J3hlyZAzcISiS1pY_szXf3-SktCERsv4Rd8Ykpb6f8P6VEC_z0NaBZzFQU9VQ5n8E-2Q0IwG9zx2KRTxIGDXVGDuY9xn4m8fRev0nTf2LOPxtKw1-ihLo-NToF2PUlLGhAIYE-K0OAxIvHtZDmhGd31JwTFq7CbzVqf2NWqTuWMphgwxOs7QHN4y10s_yC8kQwDRleJuMMj_43vBWxLvLkVBOIGi421KDiaPujpRW-zhhAyg_TpNkNEx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgG96t0U8rBoW-EWpvmJ-o4ek3daDXSrYjyteerP3Ft2xtdl2CPKvaihQV_2zFWfuYcWdlJabD6kxn8C9C4QU0ZV8XUAkMV3-1tek1fFfqj6iLrdxjuktfUix19987KX-up9Jc5yNFDLtEVlJwhHK8olDwjlCWdH_DfwzRBMOIS5sC0iYx9tcBES9XZ6BYw0rTW_NkP1qL7eNUY77FGhESbIX3p88hXJJKit2F4jLCJ3eUmOcKRPrc7sLUQdRIzcIkL-eW63htKv9mIvlBfcjuCQDqRPxTDnvK38azNg1lOFG3diEMJQyBkI3oh5iDp_aCCraA3mQDWec_PvlaG9Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مليونية تشييع الإمام الخامنئي الشهيد في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/81658" target="_blank">📅 09:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقتل غابرييل إدواردز القائد العام لسرب القتال البحري بالمروحيات (5-HS)، بعد سقوط طائرته في بحر العرب.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/81657" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/81656" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81655">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875458cfdc.mp4?token=Queh_pRCa3B-opyhhvl6PMH_d2P09H4m2FTf0j3o7FFSJzdzq586RSIBmloYuqHyQMT0IJ1fA3z9ktqYYFZaa60J1lFAY_H79COWT8_PRwsxilKxxj4wGWyexAjn76p00MbrSOR0EiazpK2m7R3687_XtcHy-47hRMjGWJtTuBMxcgMlSPKqbv8uf6hgDccXrtYX7sHfvIsMWzlufDPlpQuw7HIGyiyB_WNqZUvqQ1PMEUSUfjhj0tZfcxiKKExIGg_CRq3l98Y78RdgOFVNXnPCgJ83H6Q0V5thBUWmsoKVRUYbVNq-VeyrE9V4CEy-ua2QVUqpQ0vmXUJEmPKD2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875458cfdc.mp4?token=Queh_pRCa3B-opyhhvl6PMH_d2P09H4m2FTf0j3o7FFSJzdzq586RSIBmloYuqHyQMT0IJ1fA3z9ktqYYFZaa60J1lFAY_H79COWT8_PRwsxilKxxj4wGWyexAjn76p00MbrSOR0EiazpK2m7R3687_XtcHy-47hRMjGWJtTuBMxcgMlSPKqbv8uf6hgDccXrtYX7sHfvIsMWzlufDPlpQuw7HIGyiyB_WNqZUvqQ1PMEUSUfjhj0tZfcxiKKExIGg_CRq3l98Y78RdgOFVNXnPCgJ83H6Q0V5thBUWmsoKVRUYbVNq-VeyrE9V4CEy-ua2QVUqpQ0vmXUJEmPKD2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Mavic 3 DJI over Alnajif street</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/81655" target="_blank">📅 08:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bab1b56.mp4?token=VtvaWL6Km96riWu1G2bPzm60UUd8RKvMkn52OJoVRb57wUFNNGzwtHxcFXjYbmp2H7g-WUdgTrrBDh6Wq8tPkHTXww8IO8KdfiD-nFCJkfz9AznhLoywfmKkBjcEoweoqpPDGOpqx0h9sHtwrHHsDyhvW_PajVO3qHluoltjzwVq9yCZfpqwGZyLENJwu0OgbsvSYiNrj7jU9tbhVIBgjqZ5s9ZTxFeGFeKNe2gY2VRqvYcszZg_sRq01LtxROrub2ZEMUGzColv58vvE3Rn8c-J29nl6aSaWfe-IHOZBV3zT2uxN9FjCjJvCMSaU4dWrCuKK-W0ce44FCmjG7pFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bab1b56.mp4?token=VtvaWL6Km96riWu1G2bPzm60UUd8RKvMkn52OJoVRb57wUFNNGzwtHxcFXjYbmp2H7g-WUdgTrrBDh6Wq8tPkHTXww8IO8KdfiD-nFCJkfz9AznhLoywfmKkBjcEoweoqpPDGOpqx0h9sHtwrHHsDyhvW_PajVO3qHluoltjzwVq9yCZfpqwGZyLENJwu0OgbsvSYiNrj7jU9tbhVIBgjqZ5s9ZTxFeGFeKNe2gY2VRqvYcszZg_sRq01LtxROrub2ZEMUGzColv58vvE3Rn8c-J29nl6aSaWfe-IHOZBV3zT2uxN9FjCjJvCMSaU4dWrCuKK-W0ce44FCmjG7pFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراق يشتعل حزنا بمغيب شمس ابا المجتبى الحسيني الخامنئي</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/81654" target="_blank">📅 08:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e67f30d0.mp4?token=o5KBGAVnRzosSlO8rNfp7nkrUy1mXwXp6heH0wSJzovmpv98c-aHqmBwZibqGfbQDHUeezdb-ffijQIZcgV1AZkTL8Ftz7cujUAqBVhYdUym5dnhLbyZz-bMwHh_5OMqCCvb6QlCiJdFpe_SwB4-LOjk9I-p-rZA0BxoUeev7uO4LezyftnvSErPVrFFxMck_h4y7GMidNe4TeeQmJT1rEnLfw7CM7RRLX5BlQBwJbGRhoCnahLzXRKD7mQUDH6-Q3r76qHHyOAKuq0gAnqz57sZFjE1013TeWtbhFMNeHw5M5je93ZO00kMlV1W-EnMbJavfqk_m3Qms_6iEf7ZuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e67f30d0.mp4?token=o5KBGAVnRzosSlO8rNfp7nkrUy1mXwXp6heH0wSJzovmpv98c-aHqmBwZibqGfbQDHUeezdb-ffijQIZcgV1AZkTL8Ftz7cujUAqBVhYdUym5dnhLbyZz-bMwHh_5OMqCCvb6QlCiJdFpe_SwB4-LOjk9I-p-rZA0BxoUeev7uO4LezyftnvSErPVrFFxMck_h4y7GMidNe4TeeQmJT1rEnLfw7CM7RRLX5BlQBwJbGRhoCnahLzXRKD7mQUDH6-Q3r76qHHyOAKuq0gAnqz57sZFjE1013TeWtbhFMNeHw5M5je93ZO00kMlV1W-EnMbJavfqk_m3Qms_6iEf7ZuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه رسیدن پیکرهای مطهر خانواده آقای شهید به حرم حضرت اباعبدالله الحسین عليه السلام در کربلای معلی.</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/81653" target="_blank">📅 08:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجددا انفجارات عنيفة تهز الكويت تحديدا منطقة الميناء</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/81652" target="_blank">📅 08:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هجوم صاروخي وبالطيران المسير يستهدف البحرين وانفجارات عنيفة تسمع بعدة مناطق.</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/81651" target="_blank">📅 08:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
العلاقات العامة للجيش الإيراني: في أعقاب الهجوم العدواني الذي شنته القوات الأمريكية ضد المناطق العسكرية والمدنية في جنوب البلاد، وانتهاك بنود الاتفاق المكون من 14 بندًا، قامت الطائرات المسيرة الهجومية التابعة للجيش الإيراني، منذ فجر اليوم، بشن هجوم على مراكز…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/81650" target="_blank">📅 08:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
العلاقات العامة للجيش الإيراني:
في أعقاب الهجوم العدواني الذي شنته القوات الأمريكية ضد المناطق العسكرية والمدنية في جنوب البلاد، وانتهاك بنود الاتفاق المكون من 14 بندًا، قامت الطائرات المسيرة الهجومية التابعة للجيش الإيراني، منذ فجر اليوم، بشن هجوم على مراكز تجمع القوات المتخاصمة الأمريكية المتمركزة في "معسكر الشيخ عيسى" في البحرين.
🔺
إن عواقب انتهاك الاتفاق بشكل صارخ ومتكرر مع أمريكا المجرمة، ستكون استهداف جميع المعسكرات الأمريكية في المنطقة من قبل طائرات الجيش.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/81649" target="_blank">📅 08:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81648">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Mavic 3 DJI over Alnajif street</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/81648" target="_blank">📅 08:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81647">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رسالة السيد القائد الخامنئي لكم يا شعب العراق العظيم</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81647" target="_blank">📅 08:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12ac0a9f4.mp4?token=dh0PK5FY-R00G9SniBJOUb46AOT3jcHNsooOFhRd3RuYF51cSmu9DwrTM0mazLessVJUOqKYaKruPDYDGAx9Biv_WD4VkFI7JEW1ubQgKoXZOVTemXnUX2hnyI2dk9NE4SF2ernISOaZJeBwsuHYrgAe7bSFrrVVl0BJL_kEzkQu1Kc5AXk8FOewrLir6LuQlCP0s7hyyhAZJ6kB2WFIREncDHCKCtiV2Y8sMAfkiXzQlK9JDeR7eSmrKOVEMDSJR934WPGdwikLOj0olhBZYYV8K5sFEqhalE45jXgK07rBUu7qFJwOnTAgxkjvWB0tnNSB5bUf5oEaI259_gc-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12ac0a9f4.mp4?token=dh0PK5FY-R00G9SniBJOUb46AOT3jcHNsooOFhRd3RuYF51cSmu9DwrTM0mazLessVJUOqKYaKruPDYDGAx9Biv_WD4VkFI7JEW1ubQgKoXZOVTemXnUX2hnyI2dk9NE4SF2ernISOaZJeBwsuHYrgAe7bSFrrVVl0BJL_kEzkQu1Kc5AXk8FOewrLir6LuQlCP0s7hyyhAZJ6kB2WFIREncDHCKCtiV2Y8sMAfkiXzQlK9JDeR7eSmrKOVEMDSJR934WPGdwikLOj0olhBZYYV8K5sFEqhalE45jXgK07rBUu7qFJwOnTAgxkjvWB0tnNSB5bUf5oEaI259_gc-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس خلية الإعلام الأمني: متابعة دقيقة لمراسم التشييع الشعبي للسيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81646" target="_blank">📅 08:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4e6207d4.mp4?token=PrEBuq6PlXbapyEPkNnpLp6DhyRZe1GorjF7w1mjFUqQPdL9zCCrw64Ux8gVeV30gOIiuNXNH2_7S3FsTa-YabK3UTrue4U7QJ4X8eeLbXWNBcwKRYKG4yFCLaRiGQYAUEN_9BXhTssI6CbAwItDZefAEoFLmTIqgxcmZTki-hRf72ceWjYkAEzkRJTAr5MePW22KIdAX-4Mz9W-xRUnpdZuN79t-PhIh5_7uDUhQMPk4kR6jH95PCyp2hU5AqCqJjI4LvdlTGWmFCfnZ7x18g9VbTEUzoXcL96bk2mh87BPCPnk1qpfACmhPz8l-WS0Rq0mhqLO2ct9Sfu37YPHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4e6207d4.mp4?token=PrEBuq6PlXbapyEPkNnpLp6DhyRZe1GorjF7w1mjFUqQPdL9zCCrw64Ux8gVeV30gOIiuNXNH2_7S3FsTa-YabK3UTrue4U7QJ4X8eeLbXWNBcwKRYKG4yFCLaRiGQYAUEN_9BXhTssI6CbAwItDZefAEoFLmTIqgxcmZTki-hRf72ceWjYkAEzkRJTAr5MePW22KIdAX-4Mz9W-xRUnpdZuN79t-PhIh5_7uDUhQMPk4kR6jH95PCyp2hU5AqCqJjI4LvdlTGWmFCfnZ7x18g9VbTEUzoXcL96bk2mh87BPCPnk1qpfACmhPz8l-WS0Rq0mhqLO2ct9Sfu37YPHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر لنايا : تشير التقارير الأولية إلى أن عدد المشاركين في تشييع النجف الأشرف قد تجاوز مليونين وثلاثمئة ألف شخص حتى الآن.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81645" target="_blank">📅 08:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81644" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0144dd6d2d.mp4?token=sVAa5hPz7-La5o5TD3GMzO2lEPDgE5mjo-RgQKlmT3dK5C7VOM8Gj8TJ7tCB9mKOOVPKdKlIUDb_ce4-iDfP3mN5RqJ5Qsfp81-4BKbVSX0-tDkLS9dyCOm_46gbnOGF68unt7uUhiBNXfBz7ZZ_IcrO7xI76ijmlCz4jN8_iYxKMnuRTdZnuUD-fTHf0ZrZkwbaX5aOqe8TBdqSBtKyQTJP1ep_YN5ZwmnnzKgzSmG0OTrFvyU1RnSU61KDc8vnD3lAkY294k9PhcoRI9gxOwMVb4rQdgEgk3grT2E2YVTh4Q-l5Qd5KsGyIt99VwNBd_ExPEhP7AzLNDzvdUql_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0144dd6d2d.mp4?token=sVAa5hPz7-La5o5TD3GMzO2lEPDgE5mjo-RgQKlmT3dK5C7VOM8Gj8TJ7tCB9mKOOVPKdKlIUDb_ce4-iDfP3mN5RqJ5Qsfp81-4BKbVSX0-tDkLS9dyCOm_46gbnOGF68unt7uUhiBNXfBz7ZZ_IcrO7xI76ijmlCz4jN8_iYxKMnuRTdZnuUD-fTHf0ZrZkwbaX5aOqe8TBdqSBtKyQTJP1ep_YN5ZwmnnzKgzSmG0OTrFvyU1RnSU61KDc8vnD3lAkY294k9PhcoRI9gxOwMVb4rQdgEgk3grT2E2YVTh4Q-l5Qd5KsGyIt99VwNBd_ExPEhP7AzLNDzvdUql_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاركة السيد مقتدى الصدر بتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/81643" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91606094.mp4?token=vEWGfVT4eouz6mUa5bBoIQdLkRR3nsGP17Bl0qIlmniPQ1W3oSiqQiBLMeK0B55H5ClsKiNxi6_CBtnkmwqZTxOg3PiHXQH0Jk98SIhMBcCcAGMVrTqxx4FiDIqCltjmvYZJ7lb9pP_DyQRdonrq4hBH0OvXAr2HICA9WplZLvvTk1usjOIJKYR-fLyTfyHpIt41Q1XHVxQUvEbX6AOF2KEwlyfuU0I7kshGMfBCi0dnwzEU-dc80bYdYoUl2R-qyvt5L_N4x8D83Zt8JWIyHTfs8TubxxO8h8OOBi2HnT_X9ploM1IblXRb6MFN3wFeOH6U9Wcuv-60fqSHWbGItb0YKCOm142lu1QTg2VAJTbzheJyGTtE4x0ax_xZdUV1CdrwTYbpap1y3j_bb37PPr0JPQyQuK5lO7oEl3QrrTW4UpLDPuQQ34Dst3ZKXhcYb6pE2Kt3zB8zJkUGVmioAGtn6ecm3aGtVd_gQ95LiZnmxs3Dae5W4a3dbbGR-vuvWZwZyACGpDGAadIdQW3o2mkfKl4ynefU9PSkCPH2p-n9j2M36XuxPQiDCzRaa0bW1Qy417Dygpo1q0sraTgz_WSHiPoRd2vA4rektJHbSqPRDKFGetL6cgLY9w3aH9U-4Wk5xRFjZIzFrExETjlbBLQNCNIn9iOnPOqEY6WATo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91606094.mp4?token=vEWGfVT4eouz6mUa5bBoIQdLkRR3nsGP17Bl0qIlmniPQ1W3oSiqQiBLMeK0B55H5ClsKiNxi6_CBtnkmwqZTxOg3PiHXQH0Jk98SIhMBcCcAGMVrTqxx4FiDIqCltjmvYZJ7lb9pP_DyQRdonrq4hBH0OvXAr2HICA9WplZLvvTk1usjOIJKYR-fLyTfyHpIt41Q1XHVxQUvEbX6AOF2KEwlyfuU0I7kshGMfBCi0dnwzEU-dc80bYdYoUl2R-qyvt5L_N4x8D83Zt8JWIyHTfs8TubxxO8h8OOBi2HnT_X9ploM1IblXRb6MFN3wFeOH6U9Wcuv-60fqSHWbGItb0YKCOm142lu1QTg2VAJTbzheJyGTtE4x0ax_xZdUV1CdrwTYbpap1y3j_bb37PPr0JPQyQuK5lO7oEl3QrrTW4UpLDPuQQ34Dst3ZKXhcYb6pE2Kt3zB8zJkUGVmioAGtn6ecm3aGtVd_gQ95LiZnmxs3Dae5W4a3dbbGR-vuvWZwZyACGpDGAadIdQW3o2mkfKl4ynefU9PSkCPH2p-n9j2M36XuxPQiDCzRaa0bW1Qy417Dygpo1q0sraTgz_WSHiPoRd2vA4rektJHbSqPRDKFGetL6cgLY9w3aH9U-4Wk5xRFjZIzFrExETjlbBLQNCNIn9iOnPOqEY6WATo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل جمعیت عراقی‌ها غيور در تشییع پیکر مطهر آقای شهید، در نجف اشرف.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/81642" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba481ca1d.mp4?token=qRdRNLSdGFppNsBUM5s1z6_PQjS8j7x-KY3-1NsRqOH_0tUFNdAl7EtYpA6PhnBwUzUAb0DbTpue0zVpwWbqYp95rzzFQi7r3owSQ_ai3xMpgtarAtrN6YlZCojAw7K0W4GWZOs10joqwdEUWYcrsIJSTPI4iXNaRbDU_IT6m1vSSqT-Ak2UQToCqThe3DLxgAgV_4b3-nl94wUxnYxTs9ORAmrt5bZHxojfn_PJJ_lMKC6W6WQ2oPcezmfDUdS1fgCH4kLPcrlsXFkMBWIDwelKFZQeNFQB2aHFYUGV2MCisgGcm4mqoZmtuC414buHS-fztZy-hMCohty_eRzqhlXQ6NaiNgWMg7hX6--Fwj_NhRCQk_E5f2Zlg3S8NoZJWgcwdrDMcO-1sRMUQRDsUy0vfCVLdh_A2OrS9cKEGj9ZKJwj6uHRsN_SxcSmjCNL2Z6n2hQ3xpLkmuLkWC0WYdS9eZuBaPyKAaXZAoQmOUbZ5exshyOEIwAk1sX6LuKlT6GREOcTxUgtLB_XPs7NkhMyLjC8m5zps9W80-ZJm4ZbkdgUvY5xEGEK2NnvUzv16xwTnKbts9i4F5_GRRkp1k0xWknOYVihzBVHC3RJ-TccdrL296YE7aN7hjDk2YwRw-Z9B71MhmODlA9gnrVANoXqZTK90JgPvfj4CIo71u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba481ca1d.mp4?token=qRdRNLSdGFppNsBUM5s1z6_PQjS8j7x-KY3-1NsRqOH_0tUFNdAl7EtYpA6PhnBwUzUAb0DbTpue0zVpwWbqYp95rzzFQi7r3owSQ_ai3xMpgtarAtrN6YlZCojAw7K0W4GWZOs10joqwdEUWYcrsIJSTPI4iXNaRbDU_IT6m1vSSqT-Ak2UQToCqThe3DLxgAgV_4b3-nl94wUxnYxTs9ORAmrt5bZHxojfn_PJJ_lMKC6W6WQ2oPcezmfDUdS1fgCH4kLPcrlsXFkMBWIDwelKFZQeNFQB2aHFYUGV2MCisgGcm4mqoZmtuC414buHS-fztZy-hMCohty_eRzqhlXQ6NaiNgWMg7hX6--Fwj_NhRCQk_E5f2Zlg3S8NoZJWgcwdrDMcO-1sRMUQRDsUy0vfCVLdh_A2OrS9cKEGj9ZKJwj6uHRsN_SxcSmjCNL2Z6n2hQ3xpLkmuLkWC0WYdS9eZuBaPyKAaXZAoQmOUbZ5exshyOEIwAk1sX6LuKlT6GREOcTxUgtLB_XPs7NkhMyLjC8m5zps9W80-ZJm4ZbkdgUvY5xEGEK2NnvUzv16xwTnKbts9i4F5_GRRkp1k0xWknOYVihzBVHC3RJ-TccdrL296YE7aN7hjDk2YwRw-Z9B71MhmODlA9gnrVANoXqZTK90JgPvfj4CIo71u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه رسیدن پیکرهای مطهر خانواده آقای شهید به حرم حضرت اباعبدالله الحسین عليه السلام در کربلای معلی.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/81641" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
🇮🇷
فریاد "لبیک سید مجتبی" عراقی‌ها در نجف اشرف.</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/81640" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFTps_9oS8nU3PhKfSWpj7N7vjBXSzRjDuZW4NCwkz9-ri-bwLN23SkLbx3m0_LBlvudovHEi2givn13ccSFzkO_Pow0I7rC1tipCVfG1tynaIyZWz5TStlElkcwiFg5sXA4UgqB9g2OvKyzPfD9hHn2Q0siHTP5BFv9KQjCQw5hp9JQZ7zlo4rXEik9C3hWdz8Yjs4xhjREUeMFt4yoVasE2ckm4AIFfepz0HUc-NzV86d40t3H92AjYVfkq3YoZPY0knbwzW-Ww5_7YMk_6DvEeGjkrKRL9thHBKihCk7eRHr5tUbaoat_zNo1dQHpO_qO1V22yCv14ZfYA3KRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زعيم تيار الحكمة السيد عمار الحكيم يشارك مع الجماهير تشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/81639" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b86baa7e.mp4?token=G0W3IXih_Jr0aeY9mwCFeT6W1EG74a0dvVop3hsC8GmUxpesyXRc2AA1tzUfNNXsdcQrux0LBR83po56W_94j6AQxg40EkojxkK0m_NvSDDyIZN6ysBHACSRskfdFvezK68wqTRdJpU_IY1wBJlChwuZ_jXB-TJFs3-CLSUQoAkByiJlrJJCZIwaApw5oCIApjG0rDJJB-oPk7zC6d7cFc8pqPOFRoNHPKvSWzFdl5x_8LmN82oeQflPCobkYTpZVeUxommyHvpw82jCbjzkX-wLU74XiZx5xF-js6P7hbh2cVR3Z2letPMsU9T_hOvupjQblybOKr10C3V5cj4GJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b86baa7e.mp4?token=G0W3IXih_Jr0aeY9mwCFeT6W1EG74a0dvVop3hsC8GmUxpesyXRc2AA1tzUfNNXsdcQrux0LBR83po56W_94j6AQxg40EkojxkK0m_NvSDDyIZN6ysBHACSRskfdFvezK68wqTRdJpU_IY1wBJlChwuZ_jXB-TJFs3-CLSUQoAkByiJlrJJCZIwaApw5oCIApjG0rDJJB-oPk7zC6d7cFc8pqPOFRoNHPKvSWzFdl5x_8LmN82oeQflPCobkYTpZVeUxommyHvpw82jCbjzkX-wLU74XiZx5xF-js6P7hbh2cVR3Z2letPMsU9T_hOvupjQblybOKr10C3V5cj4GJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
فریاد "لبیک سید مجتبی" عراقی‌ها در نجف اشرف
.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/81638" target="_blank">📅 07:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d48fd446.mp4?token=XwdbMCT3WJ-euH3inp6EAPAp3wai3HZin1OpvjrGHcpezcOR6sswbwpYZ-t1PiH_z7nWPABbpm0lhphkSHysVFnXmUUy8hQA-jA7S31ty9r--Knl35p9tzzXEBzZ6zdsw5LGuqpqNZ082jrAaP-4IbaQiVDUSkzOflu9txnU_04M8ohDMCbSOv4q6vZTK--bWI6yJI9j07PCodiB3moay4ZFYHnNdHu9rdiev_ekF62fq_pnnfC3baHdBqlCO16yGDK1EGrK_rQKtDTQAan0GxOcFEvH4mmGDVxzty_KELQbUlzgoT4Vj-SEBuLCzlZKQe3bEetgM1VqIgsc2eIXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d48fd446.mp4?token=XwdbMCT3WJ-euH3inp6EAPAp3wai3HZin1OpvjrGHcpezcOR6sswbwpYZ-t1PiH_z7nWPABbpm0lhphkSHysVFnXmUUy8hQA-jA7S31ty9r--Knl35p9tzzXEBzZ6zdsw5LGuqpqNZ082jrAaP-4IbaQiVDUSkzOflu9txnU_04M8ohDMCbSOv4q6vZTK--bWI6yJI9j07PCodiB3moay4ZFYHnNdHu9rdiev_ekF62fq_pnnfC3baHdBqlCO16yGDK1EGrK_rQKtDTQAan0GxOcFEvH4mmGDVxzty_KELQbUlzgoT4Vj-SEBuLCzlZKQe3bEetgM1VqIgsc2eIXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا النجف الأشرف حيث يُشيَّع الجثمان الطاهر لشهيد الأمة وقائدها الإمام الخامنئي على أيدي أبناء العراق العظيم.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/81636" target="_blank">📅 07:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">المتحدث باسم جيش العدو الإسرائيلي:
وقع اشتباك يوم أمس بين عنصر من حزب الله وعناصر الجيش الإسرائيلي داخل المبنى الذي وقع فيه الاشتباك يوم الخميس الماضي في منطقة بنت جبيل.</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/81635" target="_blank">📅 07:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=MKhW6w_iVuRurx-kNd0PvDNRwWXImxnkvq4lk-VJkRcDsE3PzfQ5RCPfrnVPYN4mHW0ngXUDT8LX0Q9YUUGNapnimxOsFg0D_Fp7mREQolgrkVaPayn07PKGHbQGNuKKG69E7fwcjRIMVBM69RjjJvIoVSwjimJtCwEXwq0E9qpOyc_x5iXfuPUjxQAG7hdHDIudgOsj4dv-Y42H9yEyxJPtTN3HP1otcpdk6YbDAuU8LIkXEYUqXG4kJs3V8vetwvYlRtbSHKKoFdYmq9ZmriLydazmfA1bTfTnKMncZw9-Cb_Z9IEAB1Sx4lysn1_oiEIDxRbGLRvTycsFF4cWraID5VkCVK3pkqAPgryfOhlWA5_7x04-LHpBmss1sLjQJDdJJnwMojIjVjj_6PB0psNAR5pSA9Vkc37lLMmjRbfuuqlDPuex3y_DdMzlaYQLZKsAN_uIw56zN_SDcn9Z8p24EiyRsgxM6A1g8xIhQbZl7cHhoAZSzvc5Xdznctq9mRKtBx0FfSJjZRPTl5kr_lIsEynN31WO3iklWOmNZoRC-Qjj-QsMe7PMaDUC_Dzdg0RouuLfy5kCVrXg-lYn2t46hZtMNmTmh_4fjFbdiDqXMa8L28-KNcvtpLdj9RWm9_BhsFg7zpqjfzVxxmwYXeVj5-rACqI6L7e3uZeeWRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=MKhW6w_iVuRurx-kNd0PvDNRwWXImxnkvq4lk-VJkRcDsE3PzfQ5RCPfrnVPYN4mHW0ngXUDT8LX0Q9YUUGNapnimxOsFg0D_Fp7mREQolgrkVaPayn07PKGHbQGNuKKG69E7fwcjRIMVBM69RjjJvIoVSwjimJtCwEXwq0E9qpOyc_x5iXfuPUjxQAG7hdHDIudgOsj4dv-Y42H9yEyxJPtTN3HP1otcpdk6YbDAuU8LIkXEYUqXG4kJs3V8vetwvYlRtbSHKKoFdYmq9ZmriLydazmfA1bTfTnKMncZw9-Cb_Z9IEAB1Sx4lysn1_oiEIDxRbGLRvTycsFF4cWraID5VkCVK3pkqAPgryfOhlWA5_7x04-LHpBmss1sLjQJDdJJnwMojIjVjj_6PB0psNAR5pSA9Vkc37lLMmjRbfuuqlDPuex3y_DdMzlaYQLZKsAN_uIw56zN_SDcn9Z8p24EiyRsgxM6A1g8xIhQbZl7cHhoAZSzvc5Xdznctq9mRKtBx0FfSJjZRPTl5kr_lIsEynN31WO3iklWOmNZoRC-Qjj-QsMe7PMaDUC_Dzdg0RouuLfy5kCVrXg-lYn2t46hZtMNmTmh_4fjFbdiDqXMa8L28-KNcvtpLdj9RWm9_BhsFg7zpqjfzVxxmwYXeVj5-rACqI6L7e3uZeeWRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العلم العراقي ورايات المقاومة الإسلامية تحيط بجثمان الإمام الشهيد السيد علي الخامنئي خلال التشييع في النجف الأشرف.</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/81634" target="_blank">📅 07:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c202b369.mp4?token=Cqf4C_kaQSlsJfxM6EXqY99nQRL4dAB2TbIS3TYtdopMp7nzhtTde7jsXgUVl1tUvSLLobFmGJMLlh9lUFcNnNDGMi54M3ikayn3XZCWSs8zAIaza_a2FcAsRGN2Bn4NBuvFw76bQZdtZM2oPpHNFy_OHtGrI4URDJipKfO3O3tvp73Kh2ZxLvn6jqUtIrVHEe4bpb-GzCZrUsLQM-AhrIJ6ryoz8iyia9A2c9cUiUxcNRjI4FP0H_rso0Fhbw6GcKR6DndnlriWJWpo-aYhDufRx938xqMAY3v46BGDgn5Bg8yjEHp6T9ru0n8PazRKA_rnnlZHYjjprADWG_FuYxEqzRTneH6f5fvWxMd2PD3AFzK5uUVtL5u5IlJCWpTkUGYIkKQwuaGlIPe-uWb2l5oajPMHEGSNUC9mtKempX_7by_2GpGpD8Khus04dz6PjVVSkkLHGjDe8tzOLUPJTjBVd1PCj7iL9ag6zetFE6_kis7535y-IFfV61sx-isdwztFKVuHeyYzqVR4MVOSS7Kt3ns2LsljgcYLBa9xAWXUQ793SKGacHAkXyvE_Ki4WyMDf8pMb99zaRb7vfKxqwWuO9TWEhEUYfcj2m2SJDQGDYGFFxPwFgQV45JSwKn6zfTiGR0WZKu4_yEFBa4lUHHF61__TnhYcnkLvcvfoC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c202b369.mp4?token=Cqf4C_kaQSlsJfxM6EXqY99nQRL4dAB2TbIS3TYtdopMp7nzhtTde7jsXgUVl1tUvSLLobFmGJMLlh9lUFcNnNDGMi54M3ikayn3XZCWSs8zAIaza_a2FcAsRGN2Bn4NBuvFw76bQZdtZM2oPpHNFy_OHtGrI4URDJipKfO3O3tvp73Kh2ZxLvn6jqUtIrVHEe4bpb-GzCZrUsLQM-AhrIJ6ryoz8iyia9A2c9cUiUxcNRjI4FP0H_rso0Fhbw6GcKR6DndnlriWJWpo-aYhDufRx938xqMAY3v46BGDgn5Bg8yjEHp6T9ru0n8PazRKA_rnnlZHYjjprADWG_FuYxEqzRTneH6f5fvWxMd2PD3AFzK5uUVtL5u5IlJCWpTkUGYIkKQwuaGlIPe-uWb2l5oajPMHEGSNUC9mtKempX_7by_2GpGpD8Khus04dz6PjVVSkkLHGjDe8tzOLUPJTjBVd1PCj7iL9ag6zetFE6_kis7535y-IFfV61sx-isdwztFKVuHeyYzqVR4MVOSS7Kt3ns2LsljgcYLBa9xAWXUQ793SKGacHAkXyvE_Ki4WyMDf8pMb99zaRb7vfKxqwWuO9TWEhEUYfcj2m2SJDQGDYGFFxPwFgQV45JSwKn6zfTiGR0WZKu4_yEFBa4lUHHF61__TnhYcnkLvcvfoC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاصل نايا  قبيل انطلاق التشيع ازقة النجف تخرج عن بكرة ابيها لاستقبال الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/81633" target="_blank">📅 07:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9a8cb9f.mp4?token=lt0KVm8GON2ZX4RjDG4SgT5GdS65cekCW_TpSE1cgu9PRIREbFAkZT5k2foK-O1L-SGR2GmMk4KvpPCylIkf0kVGDemBJ3DE0ecyLVzVLksD5aN1T6v2Fo3boxnRSj7ZvpoNWYjGPjOIYFw9HKFmjGm5kUpFgc7mZde2lf_t4qBLxL1F82ePY29t6hAZRtE0fjFSaES9ayMSD8wsrusjM-BBQj95PlCthGrr7tBSdsqX-OhRoev0wyEF-Lw8kyIsHYqNRp0MYvko5ClCwFWHY9nvNQsj6U4C9ryPhNnw3yR57kZyfgE87qBQYOHBdMzYdd3zdCodZw7LOLLg55a62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9a8cb9f.mp4?token=lt0KVm8GON2ZX4RjDG4SgT5GdS65cekCW_TpSE1cgu9PRIREbFAkZT5k2foK-O1L-SGR2GmMk4KvpPCylIkf0kVGDemBJ3DE0ecyLVzVLksD5aN1T6v2Fo3boxnRSj7ZvpoNWYjGPjOIYFw9HKFmjGm5kUpFgc7mZde2lf_t4qBLxL1F82ePY29t6hAZRtE0fjFSaES9ayMSD8wsrusjM-BBQj95PlCthGrr7tBSdsqX-OhRoev0wyEF-Lw8kyIsHYqNRp0MYvko5ClCwFWHY9nvNQsj6U4C9ryPhNnw3yR57kZyfgE87qBQYOHBdMzYdd3zdCodZw7LOLLg55a62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاركة السيد مقتدى الصدر بتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/81632" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فاصل نايا
قبيل انطلاق التشيع ازقة النجف تخرج عن بكرة ابيها لاستقبال الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/81631" target="_blank">📅 07:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تشييع مهيب للإمام الخامنئي الشهيد في النجف الأشرف.</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/81630" target="_blank">📅 07:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حضور مليوني عظيم في النجف الأشرف لتشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/81629" target="_blank">📅 07:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6726247e.mp4?token=QHgegov5EPF9jF8kJQfxPg2XbBU6ioB57HlhQtLX5RCFw3Dm7jTV0afx6ofm5phj6LzL9Zc01HluZEdxMaj0Wj0qfLop_h9x_mOBr-B3gpTFhngQtYAsEiKl8KqT-Lc4PFgvCh4ty7l3NUSk9i3dLsQ65l9xSwx2MF747Whu10pTpDTMMtcSAs4Z-ko_Kew70EKu17Nyafc6lp7tEY4nXa30QvDy7ZpvT2f2S9Fd8uPvhxaTjWQZmZDgbrokbSmCcWJ1CNfLkKSJRaZ3pNUNpU05YeEeKXFnyWqYTqXZr0amjMJyL1m41WxxZvXgKBniBenmGjzHEGWo--h2_DxpGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6726247e.mp4?token=QHgegov5EPF9jF8kJQfxPg2XbBU6ioB57HlhQtLX5RCFw3Dm7jTV0afx6ofm5phj6LzL9Zc01HluZEdxMaj0Wj0qfLop_h9x_mOBr-B3gpTFhngQtYAsEiKl8KqT-Lc4PFgvCh4ty7l3NUSk9i3dLsQ65l9xSwx2MF747Whu10pTpDTMMtcSAs4Z-ko_Kew70EKu17Nyafc6lp7tEY4nXa30QvDy7ZpvT2f2S9Fd8uPvhxaTjWQZmZDgbrokbSmCcWJ1CNfLkKSJRaZ3pNUNpU05YeEeKXFnyWqYTqXZr0amjMJyL1m41WxxZvXgKBniBenmGjzHEGWo--h2_DxpGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيل بشري في النجف الأشرف يشارك بتشييع الإمام الشهيد وعائلته الشهداء.</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/81627" target="_blank">📅 07:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c734f5ee1.mp4?token=QjqlJkyaaA269_1Sp5A_wQki1Ork74Slf7y4Jb3HI1P6NedUKCxJT0tyPNB-N4PoX1MxnLkZWFrEk4R_0v6m5orut2VRqROzge_0rvAR-hI2OtYXzwKV2NWGT3lX8NJA5upFjiQbs83m3PcFdqwwN_w1hbm7LfWgEMZZ7cjfVYHXJAHdoNPSArXhpQwl5ryxRp2dPtymmFFkm2x1SQ97tFRz3C7cgTUC67vKlS0sUc7w5hkqIsqTUrhqkKJsZqZ-X8179HtztU_hKeuoNdM-YYuyacJUp2rPhSih8shhDJpIZMSBaSZi3hy4elOQ4rMFRHXbetAsEedIB0jYQ6HWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c734f5ee1.mp4?token=QjqlJkyaaA269_1Sp5A_wQki1Ork74Slf7y4Jb3HI1P6NedUKCxJT0tyPNB-N4PoX1MxnLkZWFrEk4R_0v6m5orut2VRqROzge_0rvAR-hI2OtYXzwKV2NWGT3lX8NJA5upFjiQbs83m3PcFdqwwN_w1hbm7LfWgEMZZ7cjfVYHXJAHdoNPSArXhpQwl5ryxRp2dPtymmFFkm2x1SQ97tFRz3C7cgTUC67vKlS0sUc7w5hkqIsqTUrhqkKJsZqZ-X8179HtztU_hKeuoNdM-YYuyacJUp2rPhSih8shhDJpIZMSBaSZi3hy4elOQ4rMFRHXbetAsEedIB0jYQ6HWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس اللجنة الإعلامية لتشيع السيد القائد الفريق سعد معن يعلن انطلاق عملية التشيع الشعبي منذ أكثر من ساعة في محافظة النجف الأشرف</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/81625" target="_blank">📅 07:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9eb9d8e47.mp4?token=oS6Jg4OGYBIGf00UCJjC6j8kHIZ0Sf43y7tPzIietIUHY6FOgxzvlj64XtTgPCS9pROLo1NRMo1T17Fg967zyZ_rvy185QY_csj6qbODZ9XrBJojzlXk17jwOQVXDopJN-nyBIxuXaDsCe6ge5ZIDil3wqYnJK627X7ylj_cpMHNDS_ug-xeDOcGWDpGmUHjZCBfLE238gJ8y8onehIULSv59g6IiM4dUaQCyZ_1OU1h1dzork7AJ1qSdFEGmINpzLaTFRvi6bp4M5wot0q2S4ES0Yq0oRxaxENU8KXFdVUNcpUSQWQv7_vsKEy00J81COGvUtZGLnXRUJUc5wXEnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9eb9d8e47.mp4?token=oS6Jg4OGYBIGf00UCJjC6j8kHIZ0Sf43y7tPzIietIUHY6FOgxzvlj64XtTgPCS9pROLo1NRMo1T17Fg967zyZ_rvy185QY_csj6qbODZ9XrBJojzlXk17jwOQVXDopJN-nyBIxuXaDsCe6ge5ZIDil3wqYnJK627X7ylj_cpMHNDS_ug-xeDOcGWDpGmUHjZCBfLE238gJ8y8onehIULSv59g6IiM4dUaQCyZ_1OU1h1dzork7AJ1qSdFEGmINpzLaTFRvi6bp4M5wot0q2S4ES0Yq0oRxaxENU8KXFdVUNcpUSQWQv7_vsKEy00J81COGvUtZGLnXRUJUc5wXEnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايين من المشيعين يحيطون بالجثامين الطاهرة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/81624" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b515fb2d.mp4?token=GCmjBPOqcEkcAbYM6lvvfIBHCvZ1D3u05d1Zl9naJxru5hdB6WaQpZB-oXVEMYLrDZ6VQdSKB2ueUXdoS-sLQMhZG6Kc0ktRj4H_ydJyHz05QaT0a5yToPbYdNYZpV1-hKGYJj6lILn8_9RJi8ebnSus-DClIZvegBbEdJdLYtsTPj7JHSS18Xk1PbpagQVmWpIdUTjEBlo-05oDpW2qEct_ST28f94iEig9H71CzNDK-mXpc-Noeuxiskg6EVKIxjBRx6TqmIiv6VzbDW7wv3WhR4tHZzTafh-alGytrtpLcFgB1Vn-Vy4UbSVwrcknRpS8FUvy1y7X2zbOS3KX-Lg9AstiTqATPHPmcFz4GCUnjI65uTfi-Wr13zjP2pv14FjkmYOifvMv0L0mCVYmlHRgqx1ExCIbONlCt6KURQuDV88xXSFP1Z_8Wy3Hap_hJuk8to44PU_NM5sETv4AL58B4pryQvFBUrkFyRjg4IfXubXn88jJCqhGbJRxRn7m2qxZ6ortIQ4WF_FJPKoGMjHJvkKY7AZrvYrJNnN8A7R5nQIOn0gjCdvqYmUID5RoL9IC7Pa5tVG9T7sjMssFnx8vJHs9D-fthDqeXEA9D9v7Rd_rvm5zjkwUF5Tpa9vZYvzIQdh3U7IdKYniisqdDAKMF5iESvLjYXapnppY0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b515fb2d.mp4?token=GCmjBPOqcEkcAbYM6lvvfIBHCvZ1D3u05d1Zl9naJxru5hdB6WaQpZB-oXVEMYLrDZ6VQdSKB2ueUXdoS-sLQMhZG6Kc0ktRj4H_ydJyHz05QaT0a5yToPbYdNYZpV1-hKGYJj6lILn8_9RJi8ebnSus-DClIZvegBbEdJdLYtsTPj7JHSS18Xk1PbpagQVmWpIdUTjEBlo-05oDpW2qEct_ST28f94iEig9H71CzNDK-mXpc-Noeuxiskg6EVKIxjBRx6TqmIiv6VzbDW7wv3WhR4tHZzTafh-alGytrtpLcFgB1Vn-Vy4UbSVwrcknRpS8FUvy1y7X2zbOS3KX-Lg9AstiTqATPHPmcFz4GCUnjI65uTfi-Wr13zjP2pv14FjkmYOifvMv0L0mCVYmlHRgqx1ExCIbONlCt6KURQuDV88xXSFP1Z_8Wy3Hap_hJuk8to44PU_NM5sETv4AL58B4pryQvFBUrkFyRjg4IfXubXn88jJCqhGbJRxRn7m2qxZ6ortIQ4WF_FJPKoGMjHJvkKY7AZrvYrJNnN8A7R5nQIOn0gjCdvqYmUID5RoL9IC7Pa5tVG9T7sjMssFnx8vJHs9D-fthDqeXEA9D9v7Rd_rvm5zjkwUF5Tpa9vZYvzIQdh3U7IdKYniisqdDAKMF5iESvLjYXapnppY0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايين من المشيعين يحيطون بالجثامين الطاهرة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/81622" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الحرس الثوري، : استهدفنا ٨٥ نقطة عسكرية أمريكية ردا على الاعتداء على إيران</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/81621" target="_blank">📅 07:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGJir8uhZdTV7oc0eM-Lh3cITtLOc5AeDDRgEzdfhHOGFWsdfHA6DnwuuTJFnodNxt2OXi_y_HFL1Zlg5w4_w2QFIL54InxVR6NuPOZkT6ovxVy8ifAx4eEm3dyJZCky7dvyWcNiyBRCtXbqQSMP_ZwGSmaOVveCkkpMm2t3nSgBkx7c-3E4Qgm_KXS9-kKqwNIJBuFKTczEB4Oi3Lq2U4aPaURN2pspMtLsRkXmqoZfZQBjFYElkdUZEuX3w5ocflPIX9tRvpRLI21WAIC2nsZFKCVUYdVAWoMtBd4h-I3gEoufzH_WREL7qx9IxD7DFhbdGHQNzcG8eoFDMlqUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أعلام الثأر الحمراء تتوسط الجموع المشيعة في محافظة النجف الأشرف العراقية</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/81620" target="_blank">📅 07:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مرور نعش السيد القائد بين المعزين في محافظة النجف الأشرف</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/81619" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a1f2f805.mp4?token=BO5ZPeVCd81ghK1giER-JH6qwKm3sl3KJ-lbJKImC6Ios4VSIQMWzviYBLX5VwLZfpZNnZ8e8bGQtkfGQi-8Mz2_Xuw2FKdfLLshuazMF8KsK20idlBBUpYFmp85mCbqegEa2wwdcIlYYc8EPgdub-1u2m-8ahQknmG0_HMToGn4-VhTUkcmrq53ADBNCGv8JN56GBe47z26_nSVVv_fd8yuNZapaQvESgF4Ze-z1UBdnVpXAGLQLrtbOApmywiKhckag9shxbxS6dPTOAMc1a8ymOYN-33cNFv79HG4Al8AJIXNLtIEXDkCgdD1AFZt47z2nQslWXk1EL1i8_OG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a1f2f805.mp4?token=BO5ZPeVCd81ghK1giER-JH6qwKm3sl3KJ-lbJKImC6Ios4VSIQMWzviYBLX5VwLZfpZNnZ8e8bGQtkfGQi-8Mz2_Xuw2FKdfLLshuazMF8KsK20idlBBUpYFmp85mCbqegEa2wwdcIlYYc8EPgdub-1u2m-8ahQknmG0_HMToGn4-VhTUkcmrq53ADBNCGv8JN56GBe47z26_nSVVv_fd8yuNZapaQvESgF4Ze-z1UBdnVpXAGLQLrtbOApmywiKhckag9shxbxS6dPTOAMc1a8ymOYN-33cNFv79HG4Al8AJIXNLtIEXDkCgdD1AFZt47z2nQslWXk1EL1i8_OG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أعلام الثأر الحمراء تتوسط الجموع المشيعة في محافظة النجف الأشرف العراقية</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/81618" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDJpB0eKo9RyBRbaiKRCb50snGTbhGH4-l_7x2Kw59y_OdiM7r9ivm7b6ZqGkBWbtlwg877fpAz3TjA0dpAsB_glg5uRA6I-V7uG1oGXhfjWc8bDgMiLIE15AHtAlUrIk0p1S09yNIFJD1gqRihGeXb0Jm4UhyJPFOMOsptDk_spl7-_22iYRw7o8JOhWg0RHlSuxrxRMXVGfqkJMmzOedF9YmO6yK450ENhuFC6mXZEikyDcMWr_6jeh8mkbLcd9I62ewI3Jd3ohenFIn4QFFdi7GyGK__NCdJbTGBVDEkhde2tngogT6IypZAAiN2s9D2f-fwDyYSDmW4GAc0iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0zUBMrN8S54W_avH8pry4Oqg8ARYLYmgIr_ktS8r3Vdfhmsru7l1BQl1loi3kRYV5SqlVdzbKs6XqyWBWt8XSux9XjqJgruxFMGHV3ArFXm22P7cCVjj3SMBzCXlHNaUPjsdwDTqyBjniM82J6IcVoHbRYrp2YUavIYsU9lej2-as2sw-nhcq1i3r4BjqA_qR9nl_pA_hI9tl3stoGrGu2X2D2UTSwzqgxNK3zFNwEDxd-Xh5rPjkT_hqRV0OZeMtKnIs5cneHz5t2ZIIgWifVSfRlP6AvjmUYYzMJxg3I3dlskDr-YONUKzTrjk4Sl1yGm25NGOR78bsNgt3D4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmWv9zdMZsR2NlZHmJRPdv_MV4SDC8BdqgcCKkd6Zn6O821YPaQJLdtUcNa66q7kH1OC5frupMpAngrKtlH_y7NsFud6ssym2vudgnm7NXN285l214rVHK3Mo3wLCN8NceAoYSaY6xWC60bojcuBXImi0C3bzFwtCdza6jpzDFEv7S-N2kuEwDfTu5Ko8qNaFBss6MzxsnR4T5FfuVbU4hj1GoVCPQOiIq-4gou7VUkhHmwO3x1uh8Oi2L-3rOiS0uQwZHXMu_9VamG2ll_bP9jxsbewIer1YFChGIytHVvI1_dBM1LxOQSldO9SvXewr6c84fGnLfBiMu8j0axLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0I7qFR2tnUECMFgrIRSUqEqt_YFHY-KhJnaxDRirVG1482S7KUntAgoaxjv6r2d4oKxqaU9k16qjnZ8v9Y-rr5WMYpc876nSMgKe0OoootGu3rUaR_RVsgfO3CBEbdfOUsTkFijUFyVrBsiopuD8ZoF5nM4iDHrWQaFezeWwnnlaq1Y1lb0CNdsFnlI_3OsbvQgu5uevAbTix3bsoq4meQsrTcYLQtzb3lnsEEV5Ix9AVUiUG2jKUN8H1XT5UGEZhEImreLlGOKp2CPk91ZR3z763jOHmG8PIjMQK0cb5fkW6I2NFqE0cQ1ML_6GI-IwRaaBET7XpEbbowpfLXR0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جموع مليونية جاءت إلى تشييع وتوديع إماك الشهيد في النجف الأشرف</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/81614" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94a03fac0.mp4?token=rYdzmiV6kisxft72d9pvGj-crN7z9HiM7avBTWHyiOdNXHBAE5B-i8w83cmcuYjlxu-0nybuhR-Q0AbDA3HFmVOih7nnPh8lwywm1nAgDP-lbnO-AoJbNZdQd0wFLqXBx-pTWu8EMLPBwXFs9dWLbMb8eiDc4HOsi_lO8rlU6QlCIJlxm8RcoZt8bAymB7_QcfY668siN1NiCyyHxUGxhlIbmiECZJCxM84z5SfxnYWLC6StzdPeOblYtClcw37UIS4njFNYY8LbgJ-Y82PA5cTn1oV7MwzklgsyPOYsyLcoV0UQBx7rJnJXEJGLzjGxskcTD6DZn6fm8EenVXoXzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94a03fac0.mp4?token=rYdzmiV6kisxft72d9pvGj-crN7z9HiM7avBTWHyiOdNXHBAE5B-i8w83cmcuYjlxu-0nybuhR-Q0AbDA3HFmVOih7nnPh8lwywm1nAgDP-lbnO-AoJbNZdQd0wFLqXBx-pTWu8EMLPBwXFs9dWLbMb8eiDc4HOsi_lO8rlU6QlCIJlxm8RcoZt8bAymB7_QcfY668siN1NiCyyHxUGxhlIbmiECZJCxM84z5SfxnYWLC6StzdPeOblYtClcw37UIS4njFNYY8LbgJ-Y82PA5cTn1oV7MwzklgsyPOYsyLcoV0UQBx7rJnJXEJGLzjGxskcTD6DZn6fm8EenVXoXzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای خراسان در میان مردم غیور عراق در نجف اشرف</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/81611" target="_blank">📅 06:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a264bb9b9.mp4?token=Bsd6MkCunUcJtSrlzfQ9A0-xLG5GMBg13xq1aQG7daOKWfhunuEWwyWo_nkz31vJviDHKHhWs0bzRf8TZ4JNhW3Gk-Hm3Frx5YIDtKClVV08JpKn8zQTJXu-G65bhmRdbEJJdEINK20xshRUf0WBEn84NKplrvgk0JOGNkRRS1J1cTuhG58FDq_I7C6qaSs5BJsJLtAqMGvYATSPVAZ0d5xwH0laN2uakALiFBxXF1IG3Fe1iOybbEzO8dGysOvh_tpQijDuhy_T8W_1VFAV-eqluEdV8aJjoDxg0OUSV_PEA-yFbXuDcK84-ii3JraWVSVU2-Aydz3e8AgHcfgwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a264bb9b9.mp4?token=Bsd6MkCunUcJtSrlzfQ9A0-xLG5GMBg13xq1aQG7daOKWfhunuEWwyWo_nkz31vJviDHKHhWs0bzRf8TZ4JNhW3Gk-Hm3Frx5YIDtKClVV08JpKn8zQTJXu-G65bhmRdbEJJdEINK20xshRUf0WBEn84NKplrvgk0JOGNkRRS1J1cTuhG58FDq_I7C6qaSs5BJsJLtAqMGvYATSPVAZ0d5xwH0laN2uakALiFBxXF1IG3Fe1iOybbEzO8dGysOvh_tpQijDuhy_T8W_1VFAV-eqluEdV8aJjoDxg0OUSV_PEA-yFbXuDcK84-ii3JraWVSVU2-Aydz3e8AgHcfgwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلا حقوق °°°  لحظة تشيع الجثامين الطاهرة في حضرة أمير المؤمنين لعائلة الشهيد الخامنئي القائد</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/81610" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الانفجارات في البحرين لاتتوقف</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/81609" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b412db963.mp4?token=G5UykuhY7JGvYcQSCqQnHMNjmtiV7WWQ-E1l3bXghYOAb4mAqryi1QFoS9-5xS8YLBCT5s2FFy6QYvnulJUjoKu7HyinBGXj1S-q5PohXbM1dM-GTLqLqUvw0M7ard33LZWO_avToPvp54gg8zVmolf02XTs57sckd9qwOO1K1zHejinpAP2oyOcxIKDHNi5MFH-tDG27f1_kMj8FfWz8SXDz0NNivi1rIDyTQt9pPrQTfoZp5DCG8tKkjkpPvsCQpuFOeQMxahIqqo4cHeE7DArluCmYQz4M-PZBZEzZwmivotRiv9Ef69nRiFpLGi6hEQH4xZv4TF5lEY-ZktN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b412db963.mp4?token=G5UykuhY7JGvYcQSCqQnHMNjmtiV7WWQ-E1l3bXghYOAb4mAqryi1QFoS9-5xS8YLBCT5s2FFy6QYvnulJUjoKu7HyinBGXj1S-q5PohXbM1dM-GTLqLqUvw0M7ard33LZWO_avToPvp54gg8zVmolf02XTs57sckd9qwOO1K1zHejinpAP2oyOcxIKDHNi5MFH-tDG27f1_kMj8FfWz8SXDz0NNivi1rIDyTQt9pPrQTfoZp5DCG8tKkjkpPvsCQpuFOeQMxahIqqo4cHeE7DArluCmYQz4M-PZBZEzZwmivotRiv9Ef69nRiFpLGi6hEQH4xZv4TF5lEY-ZktN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلا حقوق °°°
لحظة تشيع الجثامين الطاهرة في حضرة أمير المؤمنين لعائلة الشهيد الخامنئي القائد</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/81608" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benc1oPWwQF1x5Pzd9L5_UGwBhHEE5aa5TzkdPQnc4Mc7mHpQMNTx1V1wUvtQz_qVJ1gBEvok0SjQwooqV5OuMqVs7QDXCjjhRkNBZnfGH8A_7FzR-ryZVFE6YHGDjQOHa8xL3W2I_TGkH-Dst3qTeBywNMGWcbicbGpXLjLfqd-ntO9XCe5SJh4z9UEHzgyg13VEf2W8gZMqDzj16JsNeL5MTvHUhOYO7QS_U4zbfQxCJ0687riPIGgebTwLDiordBx-ag7fVF0DOFc-wSHz_lGBQCW2hMLCpK0m3RmXDYPVYZUXt9OQ_WT9cGhLnABtVMkvmy864xowIhuxGW8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز قاعدة على السالم الأمريكية بدويلة الكويت</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/81607" target="_blank">📅 06:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سماء البحرين</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/81606" target="_blank">📅 06:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بتشيعة طكينة أمريكا</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/81605" target="_blank">📅 06:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOAJGVtahJ6zf7nAdQPda1_aremqVOIHD3mcrS1-KDZx_0Zqd_iSNmS_DOPIrqrqasiEOj8S2j3bRiSf3kj3j7felY_JXDezpQUfJYZ8I_3gZhzwHeWkTTjtgo_8Gpsvqoxta7imLVTifVeMQO5cFItuhIb4Dc0jUDBDB50d_ONQHvI5JDz9REeexClJuH_eKyuAYMq5Z9asRDepZXVoN7eyOK5Zr4jfBsc15Oqscp47QBs-M-SXkGT2pOhlOV5od_rUZMBM37YJ0Yjno0q3GgK34dv1Vh6BTwAOKc7KeLCQGA-dUlPkOEX1xh9twVivJ7k4wX9P6gE3OIRLYB97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في سماء البحرين عقب الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/81604" target="_blank">📅 06:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8493c96c3.mp4?token=D6xTC6KdHNlkk8vnIG7AQ4G8aDbdEViYG8v3m_x9L-19aseO6qvGy63ROSje7wOke7TqsMD19u-aCild8sC-RfcJEevP7ig6w7vDG0ajOiFv9Z3L65rIgK37g1SxQSoCV02621xN8dhlZotllRYgoi_sErdJkLrRTo1olMSdr-yskeqLmlqjBz7ys4rwIOymAKLzBOdj2IRYTmOiEF46X6bL7zYJnZot_s1q_kK_Z-OAU8EORNEfyn-TulJqOntMPPfu1UGmOVfzKUCyctTrcG0AIULHPSjjb7S95zIoX7O2GYtTZcDh2f0ndeL_8MhL0ZCCSoffV28Tp4HPEYCdcCgN-2sfZVUEv1yP-xYvpf_mfy0XOnOHBgl_kIcc8I1viIaeSATOEnx6lDjp1VWw8kqSzXuTihETp8JD_05SAbq-ycG7yl06nO74-wApc8NuscdKfS6dM1noYlLEnHVy9-0MIPNNHGvmsInU5LJ4_bF8ryRTcmzGy0zf0IU3sGg6nNKuUnH_FTUXopoBjRc6ofJf-8IHjLP8amy65Ud7Nz0ro_APsL3_uCDJ_ypdfCFn0iOhcBEuVckmpiaQYP388BLfuKUWW87lPLSwZxyoBFamJ1Uzdi8CFvKM7QJTCmS4Qei5gFXRVsswQI05GWn5kAw7Pp_oT1PsoH0ti1Sdx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8493c96c3.mp4?token=D6xTC6KdHNlkk8vnIG7AQ4G8aDbdEViYG8v3m_x9L-19aseO6qvGy63ROSje7wOke7TqsMD19u-aCild8sC-RfcJEevP7ig6w7vDG0ajOiFv9Z3L65rIgK37g1SxQSoCV02621xN8dhlZotllRYgoi_sErdJkLrRTo1olMSdr-yskeqLmlqjBz7ys4rwIOymAKLzBOdj2IRYTmOiEF46X6bL7zYJnZot_s1q_kK_Z-OAU8EORNEfyn-TulJqOntMPPfu1UGmOVfzKUCyctTrcG0AIULHPSjjb7S95zIoX7O2GYtTZcDh2f0ndeL_8MhL0ZCCSoffV28Tp4HPEYCdcCgN-2sfZVUEv1yP-xYvpf_mfy0XOnOHBgl_kIcc8I1viIaeSATOEnx6lDjp1VWw8kqSzXuTihETp8JD_05SAbq-ycG7yl06nO74-wApc8NuscdKfS6dM1noYlLEnHVy9-0MIPNNHGvmsInU5LJ4_bF8ryRTcmzGy0zf0IU3sGg6nNKuUnH_FTUXopoBjRc6ofJf-8IHjLP8amy65Ud7Nz0ro_APsL3_uCDJ_ypdfCFn0iOhcBEuVckmpiaQYP388BLfuKUWW87lPLSwZxyoBFamJ1Uzdi8CFvKM7QJTCmS4Qei5gFXRVsswQI05GWn5kAw7Pp_oT1PsoH0ti1Sdx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة نحو البحرين</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/81603" target="_blank">📅 06:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بتشيعة طكينة أمريكا</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/81602" target="_blank">📅 06:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/81601" target="_blank">📅 06:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/81600" target="_blank">📅 06:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/81599" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/81598" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b25147f9.mp4?token=aUWdcZP9u4k-G_v7OJhSTJVNf8AccY9I1qVYM9kuvUtM-osZcjzZYXsh8uNwpzq6S_bmnftzDQf9u4CqDdNOFDq-danNzGx8nlpeLjr7i78FmW-LBbz7KDQ47YujSYnWc9aMc3yQ1yfB4yrvPVHWeImRvDi-7GfwS6-lqooH12p4P678iGIzYNMi2gbdL28mOFv3XCvXskPJLPOwcOIVP9zYvAvb7L4Wnk89ETFtpuMMj-t04VgQXm4aYLzCzHfwae-VM7npk2xI9UaOp78ul-7LWpxDth0xelIvhmhu87JPBAN2Qg_DXqvOmxft6e8DKAQriT2d-U0kHXeszhf_zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b25147f9.mp4?token=aUWdcZP9u4k-G_v7OJhSTJVNf8AccY9I1qVYM9kuvUtM-osZcjzZYXsh8uNwpzq6S_bmnftzDQf9u4CqDdNOFDq-danNzGx8nlpeLjr7i78FmW-LBbz7KDQ47YujSYnWc9aMc3yQ1yfB4yrvPVHWeImRvDi-7GfwS6-lqooH12p4P678iGIzYNMi2gbdL28mOFv3XCvXskPJLPOwcOIVP9zYvAvb7L4Wnk89ETFtpuMMj-t04VgQXm4aYLzCzHfwae-VM7npk2xI9UaOp78ul-7LWpxDth0xelIvhmhu87JPBAN2Qg_DXqvOmxft6e8DKAQriT2d-U0kHXeszhf_zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقطات مباشرة من مجسر الكوفة.
عدسة نايا</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/81597" target="_blank">📅 06:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الصواريخ الإيرانية تنطلق نحو الكويت</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/81596" target="_blank">📅 06:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW7-SnJsUV8xtPta4o-vqF_tIJDcC-B6X4Nmp9UFkvAbqao_BDkdqAmN3LVOXUr5THc1rc8qD8XcZ9EnN8jwf7lq8OJ7v2SoQKUQiY426C4HYd1uB1thFbvyYJTT31Nah4-xp4cWXGlGY-oI-kI4KviWhGsDrOL8A1g4f4DDssEwxw3fSVGJir5vw4BSIJS80-0tlr_prpILCQKKXHHfoztsanJEWiPKcqVJRFWS1cy-dTtba0IWEA_1DJqVHY6qPIvmDo5CaH3tKyGZXdL1p9logPPZXMn4vS5ljiWAAU-leTuru87PwFVnK926BjQN6iHS9gkZP7d6pJuhe_yUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية تنطلق</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/81594" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/81593" target="_blank">📅 06:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/81592" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81591" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/81590" target="_blank">📅 06:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c1bdc161.mp4?token=mg4CAY8zIvpFQ4S3hB_2sMD3mJc8UDQInH9yWCqp_GNCce6FFv7m2DXRT8BXojXaqkW1ZnQYIemIsSMSPrmK2lpMAS5UtoyJ3AGotZ4knMFwBAr1W88qWUilrD0bZx5-9NLDDyhgnihO2TJSpVLOZQXSkNPMxWMbUL-F2gmbB0VVVvV97IHmuRltY1bQUf1C0v4C7Xl-f_JO7OUs2DNLFRUlsoNM5mO9h249JqbnYZtQGSnbBlMYtsJFYEUk_p1Vp4MVdsDdLhsmttU8HidI0TIgOI0gfJ3ubOCuhK_ABaK6ds91rmrAZXoztR8O7ZzTy8kDCqAIawNJ8q2Wus4B6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c1bdc161.mp4?token=mg4CAY8zIvpFQ4S3hB_2sMD3mJc8UDQInH9yWCqp_GNCce6FFv7m2DXRT8BXojXaqkW1ZnQYIemIsSMSPrmK2lpMAS5UtoyJ3AGotZ4knMFwBAr1W88qWUilrD0bZx5-9NLDDyhgnihO2TJSpVLOZQXSkNPMxWMbUL-F2gmbB0VVVvV97IHmuRltY1bQUf1C0v4C7Xl-f_JO7OUs2DNLFRUlsoNM5mO9h249JqbnYZtQGSnbBlMYtsJFYEUk_p1Vp4MVdsDdLhsmttU8HidI0TIgOI0gfJ3ubOCuhK_ABaK6ds91rmrAZXoztR8O7ZzTy8kDCqAIawNJ8q2Wus4B6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوم القيامة.. النجف تخرج بتجمع بشري هو الأكبر بالتاريخ</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/81589" target="_blank">📅 06:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d95cbb7e.mp4?token=ixZds6TfeV8QM9lhryrZFWe0INQTfHbU9g3bCnSoD0NfrhAQWAQyVDdslJ72ET-_t2G5yIx12Ne4FO9Fl78k9hulZ4RVD3gnqDg35KLMkHDRqT8qKFufzKQGlAQD51X9GLAAfJN_sFjrZ4ewf5rfm0TYaOAN1l0WSBcjieIUh7gu26yJQcBejU_rq-5wkM36IKLqBNvyfFLED9KQsLX2I_Z2TegYUZaVqn48xCaeGWtI_P1FUkcn-2g6ohFc4HrTd9PVdPpsK6vWhzVbozf6F3L1WujVO7Wqfa_J2BRNykRAeoPcdxkvEl-9lZ-F1rt9w8nfXEPbigFSNp2ZNAL65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d95cbb7e.mp4?token=ixZds6TfeV8QM9lhryrZFWe0INQTfHbU9g3bCnSoD0NfrhAQWAQyVDdslJ72ET-_t2G5yIx12Ne4FO9Fl78k9hulZ4RVD3gnqDg35KLMkHDRqT8qKFufzKQGlAQD51X9GLAAfJN_sFjrZ4ewf5rfm0TYaOAN1l0WSBcjieIUh7gu26yJQcBejU_rq-5wkM36IKLqBNvyfFLED9KQsLX2I_Z2TegYUZaVqn48xCaeGWtI_P1FUkcn-2g6ohFc4HrTd9PVdPpsK6vWhzVbozf6F3L1WujVO7Wqfa_J2BRNykRAeoPcdxkvEl-9lZ-F1rt9w8nfXEPbigFSNp2ZNAL65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الملايين من المشيعين يتجوهون الان على مجسر الكوفة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/81587" target="_blank">📅 06:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الملايين من المشيعين يتجوهون الان على مجسر الكوفة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/81585" target="_blank">📅 06:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMeaBdrkLIb57wUz29XqaKeFy12UwMAraQraHPnxcfQkhnjxVAxIet-kH_8tiDy2299SXKNyOF7u_vgEC6FVqbVWSWdR4P83YlRqEmWenvmL3O7hSigHd4LDgYi9dsmCn8vGZ4T-QSOfJpaj6op6RjX7NGVGniCLGR2fq1YvHM0cIWUiT3Gl0ATrRsYe59Vcz5fC8sWyAL3fYSziW7jkeqxU8bX6ViqGlRHwpYkRNe71mcth-5OcLZF6Bir2Ko8dwCJIOV5utRfZA8D4V0OakxWMUkPNdo3hocQzSfm3NtWnOYIkftG_ZXXXEt-b_NWRtvL9gnNVlxnmBSVhYS_CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار الزحف المليوني نحو مجسرات ثورة العشرين</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81584" target="_blank">📅 06:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1065c221ce.mp4?token=AaIzwSn3ENAF2Yu6VyEy9Bq9imbV0TNNmb1uk-zuEE_p02Rvh5lJIF81S7sA8vQNeTnOv8FX09ptu0PXLvdQF5fuSQTfiDAGLO9Oq1iohyb4ZY1a1mn9-B64pGG0awKcR97LNjqd9kFB1XwWArqtjZ0bfINQeyyG64TGLFRTUpfSHMLYGhTJxi0Aj8fc2JOdc8EXbVx06KzNsmS7bLALB27qRQ1W0ZJtS81XQ4libfdhqi42cHFSBArWGc-TPlZSdqE-j4al3qeqMWnv3Uc6ybs5BoMFZ60rugQ88c0t7IclPHeS0sC-mYW5GCtXG9mi4aoBhuq7cQ7IoFYtEUbdSDQKkyf4mz0yrGvj1l1oWK_F4P-xYqVgnDvViRdWRwWznvAlJwSZFLTFoAIRJUyEiAJLIc1G_Jd0r7uzi8J-Szy2WFHWB3jI4kdDTkV34dNKiEEXudHtbhuQ8oFte5zeRZFUxGGYThU9QmZsmn22RCuNvjtfD9Fx1sTmEdu94DfAi4OsSqtPre7Lc9aZZqTAgBD7n0Wc0e-kYsdzelhMATK2kSRUEj_LnHT-VMUFX4DBip7FCzVf538v2bQnpQp59Gs9iSZUCw3U9TJFSgxNFiecpHjwbjbAoCacuQpxdImdwqoLyR3u3xvsmOj6hJCJXoWAOmU_xOdXQ12-GDIhb0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1065c221ce.mp4?token=AaIzwSn3ENAF2Yu6VyEy9Bq9imbV0TNNmb1uk-zuEE_p02Rvh5lJIF81S7sA8vQNeTnOv8FX09ptu0PXLvdQF5fuSQTfiDAGLO9Oq1iohyb4ZY1a1mn9-B64pGG0awKcR97LNjqd9kFB1XwWArqtjZ0bfINQeyyG64TGLFRTUpfSHMLYGhTJxi0Aj8fc2JOdc8EXbVx06KzNsmS7bLALB27qRQ1W0ZJtS81XQ4libfdhqi42cHFSBArWGc-TPlZSdqE-j4al3qeqMWnv3Uc6ybs5BoMFZ60rugQ88c0t7IclPHeS0sC-mYW5GCtXG9mi4aoBhuq7cQ7IoFYtEUbdSDQKkyf4mz0yrGvj1l1oWK_F4P-xYqVgnDvViRdWRwWznvAlJwSZFLTFoAIRJUyEiAJLIc1G_Jd0r7uzi8J-Szy2WFHWB3jI4kdDTkV34dNKiEEXudHtbhuQ8oFte5zeRZFUxGGYThU9QmZsmn22RCuNvjtfD9Fx1sTmEdu94DfAi4OsSqtPre7Lc9aZZqTAgBD7n0Wc0e-kYsdzelhMATK2kSRUEj_LnHT-VMUFX4DBip7FCzVf538v2bQnpQp59Gs9iSZUCw3U9TJFSgxNFiecpHjwbjbAoCacuQpxdImdwqoLyR3u3xvsmOj6hJCJXoWAOmU_xOdXQ12-GDIhb0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات الامن الأمريكية تطلق النار تجاه مواطنين مكسيكيين في مدينة هيوستن وتقتل وتصيب عدد منهم.</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/81583" target="_blank">📅 06:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0869ac3.mp4?token=ra-Op44BYYw0bBmL4CeZMPlbyH0zQu3l-Ncfi_1cpl9ELzrT4d-7z-iVZRf9oy4nD_3pBvJAxgLj9i-1BGlllAXdv3gmOC-YFdz_tPCl_vWfTrzLew8XTMusMx3QRP_mjPwsE_iIG74KyRZ6cNTkfK-RNk1jYoPY-5iLkK_0UyrGiO8tr720I7ajWlKkViIz7PpU3UB1GVeFd-yl5X1MNZgsVkFKQWjfvkykCghnQ0QVQUHf6hpXPI5mGWAtyPRdvnMXlOckzWu3576iOEgatvSG_5cCC697bQ-R9zwkx-QeufINc9esGafFfeITB_5pMwo-j5ZiQHzKyvLDAsPDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0869ac3.mp4?token=ra-Op44BYYw0bBmL4CeZMPlbyH0zQu3l-Ncfi_1cpl9ELzrT4d-7z-iVZRf9oy4nD_3pBvJAxgLj9i-1BGlllAXdv3gmOC-YFdz_tPCl_vWfTrzLew8XTMusMx3QRP_mjPwsE_iIG74KyRZ6cNTkfK-RNk1jYoPY-5iLkK_0UyrGiO8tr720I7ajWlKkViIz7PpU3UB1GVeFd-yl5X1MNZgsVkFKQWjfvkykCghnQ0QVQUHf6hpXPI5mGWAtyPRdvnMXlOckzWu3576iOEgatvSG_5cCC697bQ-R9zwkx-QeufINc9esGafFfeITB_5pMwo-j5ZiQHzKyvLDAsPDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران إرضاع جوي أمريكي يحلق في سماء مدينة الرمادي بمحافظة الأنبار غربي العراق.</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/81578" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ea001678.mp4?token=nBXIuVhQLC0akBPbRR4KHLUKqlQCMVQ_yBa_0kb_KwGEG7PXbDjUsf-MGaHfH2T0kCcZfbirlyk9sz8OFSx2pdRgu0CiH2e2uthzIG1xPdnuhO-xfZURU1Fkt-Fb4CxcC9zybEVaP-rYSFF1b7jgiV4aWAOQGiXHrsBTH3yLR61CQUUIkAOiZmzqgxv64wqurciZycluMBqq5S_eCHa93gNSDQtc4sOusxK5EIfqn7seXme8fHVVRWMWXSjkpv67Nin-T__mBZeTeaX4ZjVg2VJmBwjcbQk7OUFRTGa9WdxzmAN_j78wzvHxWnLGPOnqAQC-cEL4mVzBglSRpAcNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ea001678.mp4?token=nBXIuVhQLC0akBPbRR4KHLUKqlQCMVQ_yBa_0kb_KwGEG7PXbDjUsf-MGaHfH2T0kCcZfbirlyk9sz8OFSx2pdRgu0CiH2e2uthzIG1xPdnuhO-xfZURU1Fkt-Fb4CxcC9zybEVaP-rYSFF1b7jgiV4aWAOQGiXHrsBTH3yLR61CQUUIkAOiZmzqgxv64wqurciZycluMBqq5S_eCHa93gNSDQtc4sOusxK5EIfqn7seXme8fHVVRWMWXSjkpv67Nin-T__mBZeTeaX4ZjVg2VJmBwjcbQk7OUFRTGa9WdxzmAN_j78wzvHxWnLGPOnqAQC-cEL4mVzBglSRpAcNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجهيز العجلة التي ستحمل الجثامين الطاهرة في النجف الأشرف</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/81576" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42531eddcc.mp4?token=v5smEHiMuDLeCtnclc9E3Mp1vTp6Boy3VVKBGr7-J117pg-saZTMhqc5FMq1q5ZH0sc6tE8JebbWvwvRSK7z4Rj_ILni0h95yIsEvyOXOQSaw0NeSC-OH4WQg8ilwXLGGCBR2FKhRz7BrMOcdQVyJPtEx0CXGioQGTsXwrqcMiW9peZBz_C1cGN3509KYUJat6AruKXHpHVYBq3FccXkjzc7SToA3APaCrdED8qWZG72LFA0p4ubH_2Cn9VcfgmfnNLo-D3YJca30gUc-9bIREH0oAGqcmICISkbqXrFJdlz8OKkAvYdXag_SxNO0qpbHJ_X31pzOWKnimJNL5w-DD7QxEtbsbP_SPdwySmfStIfx-7nZMKVvRXUhB5UycZbeOOd5_Cl8t5GYMpUpefkHX8TNANZ54xLMa1nYSsKTn7xgfzY_TEgyKfbMQgrBdNDxVLGS-rHgH-5O4hJQVNtD4eG9kI1MZiPEB5yZvijxCs95lBxaQTUaIg4q6B_RQeBTy7gf_agoxYkfOEHiQtqMR8dOZ-yJIOxvgmrhZqwFIjeYT7N1jxqo7kBB-hZjwIXF1p6dzan_TVKWfEtFAhsf_F_4CmyIWNSqH5oqnQJpU0Jz2Tua9JbHDiZ_4vm7MDt_8KEUmNCjbyazemxNoJdn8E2Eggh7uqq2NlEMdDfnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42531eddcc.mp4?token=v5smEHiMuDLeCtnclc9E3Mp1vTp6Boy3VVKBGr7-J117pg-saZTMhqc5FMq1q5ZH0sc6tE8JebbWvwvRSK7z4Rj_ILni0h95yIsEvyOXOQSaw0NeSC-OH4WQg8ilwXLGGCBR2FKhRz7BrMOcdQVyJPtEx0CXGioQGTsXwrqcMiW9peZBz_C1cGN3509KYUJat6AruKXHpHVYBq3FccXkjzc7SToA3APaCrdED8qWZG72LFA0p4ubH_2Cn9VcfgmfnNLo-D3YJca30gUc-9bIREH0oAGqcmICISkbqXrFJdlz8OKkAvYdXag_SxNO0qpbHJ_X31pzOWKnimJNL5w-DD7QxEtbsbP_SPdwySmfStIfx-7nZMKVvRXUhB5UycZbeOOd5_Cl8t5GYMpUpefkHX8TNANZ54xLMa1nYSsKTn7xgfzY_TEgyKfbMQgrBdNDxVLGS-rHgH-5O4hJQVNtD4eG9kI1MZiPEB5yZvijxCs95lBxaQTUaIg4q6B_RQeBTy7gf_agoxYkfOEHiQtqMR8dOZ-yJIOxvgmrhZqwFIjeYT7N1jxqo7kBB-hZjwIXF1p6dzan_TVKWfEtFAhsf_F_4CmyIWNSqH5oqnQJpU0Jz2Tua9JbHDiZ_4vm7MDt_8KEUmNCjbyazemxNoJdn8E2Eggh7uqq2NlEMdDfnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنويه  ينطلق التشييع المبارك الساعة ٦ صباحا</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/81575" target="_blank">📅 06:01 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
