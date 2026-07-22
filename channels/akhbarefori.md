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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-674020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر زهرا میردادی و فرزندش علی سالاری از شهدای میناب بعد از چهار ماه تفحص پیدا شد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/674020" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/674019" target="_blank">📅 11:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674018">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اردن
🔹
منابع خبری از شنیده شدن صدای انفجار در اردن خبر می‌دهند.
🔹
برخی منابع گزارش می دهند که عقبه اردن هدف حمله موشکی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/674018" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674017">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان نام فرزندان «الهام علی‌اف» را می‌داند و تلفنی احوال آنها را می‌پرسد
رئیس تشریفات نهاد ریاست جمهوری:
🔹
صمیمیت پزشکیان در روابط با کشورها خیلی اثرگذار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/674017" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674016">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATjv1HQDSt4Xc7bsPNLc4fVEbtyIjrsNcgvlB29xg-ToyaVWt1VGURIAxIpvgQZSj557GwP1Ip_8IqkIp6c6mB889GP_5ncQ_xbhH_d9_wnz8rGTmTe6I6AUg-FIBhItPLkhRU4SgO1YhK8e0DHqEFawdwhzN28-rT8Ex6y2FiLXSnu-XFFWADeIat2909Je9TWgfGOkgfSm175p-Kwb4p5lc25sy0doIDzlYAm-154sXaRMeBnlIusUOGWGhltYp4D6-0YUO3SS-lRYYaMseGpYRF-AyGLGfTiZjv9tJznH9-QgIcw2QufQ92LhcZymCzSPr7uSuJborqSNZM2tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل ارتش: پای کثیف آمریکا به ایران برسد با هرآنچه داریم با آن‌ها می‌جنگیم
سرلشکر حاتمی:
🔹
دشمن به خاطر بغض و کینه اش از رزمندگان ارتش، هرچه در توان داشت، علیه آنها انجام داد ولی رزمندگان ارتش جمهوری اسلامی ایران راست قامت ایستاده‌اند.
🔹
در قضیه جنوب اصفهان، آمریکایی‌ها تصور می‌کردند اگر پایشان را در ایران بگذارند، از آنان استقبال خواهد شد ولی با تنفر گسترده و ایستادگی وصف‌ناپذیر ملت ایران مواجه شدند.
🔹
با نصرت الهی، قطعا بر مشکلات فائق آمده و دشمن نیز بیش از پیش، در رسیدن به نیات شوم خود، پشیمان خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/674016" target="_blank">📅 11:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674015">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جنگ تجاری جدید سگ زرد با ۶۰ کشور جهان
🔹
ترامپ در حال نهایی‌کردن تعرفه‌های ۱۰ تا ۱۲.۵ درصدی علیه حدود ۶۰ کشور با بهانه «مقابله با کار اجباری» است؛ اقدامی که حتی اتحادیه اروپا را نیز هدف قرار می‌دهد.
🔹
همزمان، تعرفه‌های ۲۵ درصدی بر محصولات برزیل و ۵۰ درصدی بر کالاهای کانادایی اعمال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674015" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674014">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhFN2q5Nb_xt9lDDwo5YAw9zHxeBe8fzJIvZCu_FSZYr4s5adLZC3kjtM7mPdc6TKgv3DHESxR1QpgX02I2DNIc2bB-x-a7gXQiRAKReLEj6x_RO-Hh5r4X9RKVkDIsGW9iQ6qBaS0osT4nUUSe2_8mM07SJcLSjFYixlzlOBdbf1UiGxKnf7V3YQn7R0cflBqhzL6FTYdSPu9gck2J7-CMytdI3gXbAlf7opJKPPEdNos1iZI_uw8cBz8F7kbYyN2Ld-fqGZtewbTra7ccOH8wNsPLeiesCS4PDINmGnoBRZmd8VBNtlpIRD6kH73Jehgugk0mX-HBO1hJtViSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۳ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674014" target="_blank">📅 10:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674013">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع پدیده‌ای نادر در سواحل شیلی
🔹
سواحل شهر «واسکو» در شمال شیلی، بر اثر تلاطم امواج با مواد آلی، پوشیده از کف سفید رنگی شبیه به برف شد. مقامات تأکید کرده‌اند که این پدیده طبیعی هیچ خطری برای سلامت انسان یا محیط‌زیست ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674013" target="_blank">📅 10:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674011">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: مسائل قانونی و شرعی گواهینامه بانوان حل شده است؛ مقدمات آن در حال انجام است و به زودی شاهد اجرای این قانون خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/674011" target="_blank">📅 10:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674010">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee7eZOpNHOGAmf-ewArdhl3tRlRawkT56uPOXZSLPlepScVypD1wYtW1NlGtyklX54fo7qZ0ZEPA6SMlYpMW-FnEj0A1_s4Q0Es1P804a_Hm3OwiwARc84tJcI7FNZgczWxFmAtk__bePofGdBH3RyEwwRx7OYPNZFtuubWmvh_TsLdaShTDJ1NpGrUI2wIgpyIuMvConS-E7U1WjTe0RZao37H6OCffAVuOEc4hE-HNSqADPTxP2DJrHz52X8R95YZiOXHisDyVJYabTXOJ8dI4rUIYUNQWaz3nIVKNr9Cw_5_fEoa57_wjNKZ9zn0eAibTQaIqPk1D_FnFDfw5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول جام جهانی پس‌از اتمام بازی‌ها
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/674010" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674009">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
برگزاری امتحانات نهایی در همه استان‌ها از فردا
وزارت آموزش و پرورش:
🔹
امتحانات نهایی پایه‌های یازدهم و دوازدهم از روز پنجشنبه اول مرداد ۱۴۰۵ در تمامی استان‌های کشور، مطابق برنامه ابلاغی برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/674009" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJx-boLqTNx7N-r4tieVdUIJxzb0u6bolHelPMlzZejbqpfon0PwzLPSrNZunGbMyH5-djl0a5WxzvlR-nrWD6LZwq979LR7vooOcryGsCPjt551DLEOorQdqVPAVlE9ciTUjaE-S4a0YKQUIXQndDIZ1nlRD9eFcFcqG25s3WcBaQ7B3R4H2L5AudwwQJYXQ8SKZ8C0gzqEisdhwGlRkLHQIr5BjeRe9BgzsyPy4BndDYnMz4YCiY7Sr1fGbxnWEZE8Ko92c27HLxsYtJeshdIhK26a_pO2U4SRi6O9BRmuzMe3k1TJNIi1Whlm-bt81kefvVzNdvnU_4reXbrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoUSfo_yJ1vaONbHQmhw81LHXc8nwtdxZHoNiYl_AqzhP-sMauP1w1eeeKl3MZPzFvNTqLArD_0zkuPi8S5Ng8d5wl4I0d42zYF-QT9b5REhrSGlfIczYwrKbS9poh9ibYYb7EAyf-xyi5Gtc-HQbZL3H4GPqy9KCJoSZ7YC5grzJVmPKmnZhy05GaIKHum3bai9TFfOjCPc5hOGP-p1fa991-B462KRjGdR-bEpP0YW-ky5POfhS0ebebHrkRqU46Rnm73cFt4e1dBqYPVxKDQR-0JhRq4qVLj7h7vK56YfsuzgcdqgntpRIBH7IQzyQIk1NQaICph3rtSmut4n-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9neQ2wDqF1ZqedxmmBS2pAddBhnzaO4ZCZfh7owBsu0MhlsAgGvnafMN5UPF_c9z1ltjxDfag0gEnIpGsWU0R8pVmS5GOtQl7mw0zw3ebgUDNRb_-fuT8QuV6cXUf372Kb-rmx7yJi0gjqYjaU4n8uhu8CxxHP1KzEkzc0GGNSUXB9ZrQonxCpIJTUboGQ-aAyAcz_pg7NNSKm-BjL4QwgPY1fRSHfnlR48qErem_xe4V-eiaPRCI25896aCEpd0H1pRJfjnsg4Zf8Iw70RHcYXPQhQ6ifZr97mRey7eD2TkQUir_xMfyi5qoRNOaH73xqqXUMHFaXCd77X5YNuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbUvLZw37_lQvTvMF0IkJIxcw2VdkIET2piuejik0m1wk6QmrhMNzbflnEmiKg8ranL9r9HLzdUyVjzGKR0hcRz8a_uGJzOWulQa_x6EqM74mJffrhS5n0sx7Co4JnQGDX-xV1YYTLyEV7HeEi-fe2vQtINw2fUpVs5o9w2aT6KMHIS6LA2ExyOTU68Lfe_pWYG0LXCQEvjKdxD2ODkfQivmazFQWdK5CU0HiCE2fr5a9AE6TTnbvTB1VzXBkqrcGyNzpAIL49BbkvJ2hZN_vp2_C97nsK7KGHNE88yQp-54kLKyexeFBuJ-xm4Gf2LsOSOasCnK2PZxsuHK6YGZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u05A1xhA4zWsXDA_dmEGOtfQpnOHmBalzDVNiBpxUong9PhJ7ftUHSYj_C7WhwGUCVlI3jsl0653V7NdYChum6S_PJcebjuPficK9GfJ_I6QIRoLMgrauvDD7WZISzX_WYyjm80Dw7N5tqU0V1n4w5J5CZ6uT7JKvSY0MZlFi6cIsoURNTXtvvAWzNxf_MbVYRlcPFN0779gC9z3qMc7oo-UxwPOw0yb6dCXmY8AVyQAoPLOqliQu5nfygOpkJy5i6TzZOCU4m7NlIZ0PsXffv9cJ-gZOhsDX__dTYcXBc0N-J-ObggjzXjZH8TTQ9RnjYdQMJeTTKrYpc8BCqqIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HncLOpAcdq6mIMKnL3HFz8Cuzu4XubbIFiyDJmga7yKW7nSdKgdaYqQcovw5vo8RxZRclZdDdEYB7DFyRhFcEw2LAxJ7501XS9r1wjEp0AxZMfmrabvydaPuyvZYKAy9lakveBoNkzDOORrQIByn_J6MNtjtA68u5cChzuOtgdi7cZvc-edqfbKwcVnOEGO3BYtIMUTN8W0cd7d1Mx8iV-Txtz9mNrBenCa659vIdATgfeRKCpi4txEahBL3b8YOq0lJp17xNMNBSwIUlqkuwZWLUU-tj_X-FqhV2DBbU7l6PjHkpPZNfC93zk5kRLmXypWunhOcrMkZhxXZ4azKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هنر بازیافت خلاقانه؛ تبدیل کفش‌های قدیمی به آثار هنری ماندگار
🔹
این خانم با پیشینه فروش کفش از سال ۲۰۱۹ کفش‌های قدیمی را به گل‌های زیبا تبدیل کرده است.
🔹
نکته برجسته این آثار، حفظ جزئیات، لوگو و بافت کفش برای نمایش هویت اولیه آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/674003" target="_blank">📅 10:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674001">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده شدن صدای انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/674001" target="_blank">📅 10:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674000">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
همزمانی کاهش ذخایر نفت و بنزین آمریکا با انسداد تنگهٔ هرمز
🔹
داده‌های مؤسسهٔ نفت آمریکا(API) نشان می‌دهد که ذخایر نفت خام، بنزین و فرآورده‌های تقطیری ایالات متحده در هفتهٔ منتهی به ۳ جولای (۱۲ تیرماه) با کاهش مواجه شده است.
🔹
براساس این گزارش، ذخایر نفت خام آمریکا حدود ۳۹۹ هزار بشکه، ذخایر بنزین به میزان ۲.۹۳ میلیون بشکه و ذخایر فرآورده‌های تقطیری(گازوئیل و نفت کوره) نیز حدود ۱.۸ میلیون بشکه نسبت به هفتهٔ قبل کاهش یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/674000" target="_blank">📅 10:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673999">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9NZA7GWTTlXIhttnhfXN1gZRp1W_v9qhnXNp4frNBfBERa9X8-iij41Ucu61-obc8NfPN6uRjj8IIZyvdSQijukC3la7pXVmwNN5933dbLeGO1n7wFWDwyZmc4gPIwwS294h33WgUjJwgalBUwCgcd3iylB_uFKTTkvEcvu1fC2je2l8S8cAkhu3gP3aa-omm8vI4LxkktXR0yx9vwWi1U0SW8JT7xS5noiZYPCwwe3dvY5FHhHQLpKglrM-nTYdHYql6QUq_VjOReres0Ez1LWjMcRp7KZZK9TgciV64ls-LwBLkWoPVpkx3jUvgFD2iAnTmw_AN_U4sdB-wXVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط تو ده دقیقه و بدون روغن این فیله سوخاری ترد و رژیمی رو‌ درست کن ⁨ مواد لازم:
🔹
نصف‌سینه مرغ
🔹
سیب‌زمینی
🔹
نمک و فلفل
🔹
تخم مرغ ۱عدد
🔹
پودر پانکو  مواد سس:
🔹
جعفری
🔹
پنیر کم‌چرب ۲قاشق غذاخوری
🔹
پرو ماست ۲قاشق غذاخوری
🔹
جعفری
🔹
سس زیرو‌ ۲قاشق غذاخوری #آشپزی
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/673999" target="_blank">📅 10:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673998">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE2j1z4h7s-Lg3jAKNYpfYw3N_w5zZfDTcmFmN4l-oDGNLx_OYad2yMA9OHIR2XdRRNPb7GZS1vl0uIJlJlOBI87uQnwblhwt-yAuPJpmihzx2ou0ykurzQ1QuHFyDVj4ZNQ822mfaDrjfRN4pxhi1xSlfsAgyqMU3IgxYp5iMQLiRc25XIX_c04b_48N6aOOWw2Z0VkGyp1XBm8V7lwH7F5vP5_QiyvYnaWyTQFOL7cx_kB4IL3wx4C2Y2XM4rL8qjVMw4g4dtxpbbyv29d_9YQTmWa3iw0pNABecicXPKWsGgFU__id8uPeG-L1lxCaQZ_VBkXPCRA8wBtQpB0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قابل توجه سهامدارن بورس و صندوق های طلا
🚨
بررسی کامل روند بورس و طلا در کانال زیر
👇
https://t.me/+werraAXV39phMDZk
برای دریافت مشاوره  به ایدی ادمین کانال پیام دهید</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/673998" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673997">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دور جدید ثبت‌نام خودروهای وارداتی آغاز شد.
🔹
مراسم قرعه کشی لیگ برتر فوتبال فصل ۱۴۰۵-۱۴۰۶ سه شنبه ۶ مرداد برگزار می‌شود./آغاز بازی‌ها از ۲۳ مرداد
🔹
هند تعلیق پرواز به اسرائیل را تا مهر تمدید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/673997" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حکم اعدام عنصر فعال یک گروهک تروریستی در کودتای دی‌ ۱۴۰۴ اجرا شد
🔹
«مهدی خانکی» عضو یکی از گروهک‌های تروریستی ضدانقلاب که به جرم جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی محکوم شده بود، به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/673995" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله ارتش رژیم تروریستی آمریکا به چند قایق ماهیگیری به نام قایق‌های تندروی سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/673994" target="_blank">📅 09:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSYKAc9ZNotK4HX9V5narYBWFvoLF8kc1kZaapdhGBnJF57rqpEL5IS1wWsC1ZWqMEM-Jwk65WQqgy0-2nXsNvrzomHFcNJT_soOmjF_uSDtiBRAJCC27Rh8VX1TKmKzaCGFMLql6wwsQIsm_RQCtGoQDM8JR136MOfH2Xf3M-XsGd40rGDo3LZPz4zPWZtQJpYwui25_nQlZa7h_qMu0YnToDF87zDjmK2ouV9qQyji4e-sQL9oREIIQFtnqsJbJ1mJyIpN3Ttve5UEvpOieoMCIfqLuNUofAGeajQnIXs7UL6B9GEi7JIyhqzMR4gfXMviCdMi6i8hvULEGscfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk2nprB3H9AZQn_ri7YK2SQSdCsfLPbEDpik6qBSaXQZRAuJKezaDRxrBf8teD8X4lTZbiERr-4FHuXDxg1zsgTPqbjuN4mkJcjgKleonYL9YQzE9M8uzL9XkCt1QHZG2ywjp61PjT9HwnxjzG490dKxSv8vDqk3dfaCX-Jnm1-8Tec_cCovd2y6icOPV6acmcFpIACcIjZtKsX06GK0MNkZlrH1U1-ZvIPR6KoYsBe-PH4faSxDyLuqC2xyjCG7jdvU2jlc0UByxgr9uFDyR_kenQMSPqRmAOLz6qszFzgz6ZvKDOXDegfsJy6Ucsmoa_eSl4m0mxcGeM78hFgksA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از خسارات وارد شده به پایگاه آمریکایی برج ۲۲ در منطقه التنف سوریه، واقع در نزدیکی مرزهای اردن و عراق در اثر حمله ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673992" target="_blank">📅 09:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
جزئیات حملات بامدادی آمریکا به بوشهر
معاون امنیتی استاندار بوشهر:
🔹
بر اثر تهاجم بامداد امروز ارتش تروریستی آمریکا ۲ انفجار در بوشهر و یک انفجار در اطراف خورموج به وقوع پیوست؛ این تجاوزها خسارت جانی نداشته است.
🔹
برق روستای بندرگاه بوشهر نیز که براثر اصابت موشک‌های دشمن به یک پست برق در حوالی نیروگاه اتمی سحرگاه دیشب قطع شده بود با حضور نیروهای خدوم برق پس‌از ۲ ساعت وصل شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673991" target="_blank">📅 09:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb3633452.mp4?token=NJTeOplRjrfOk-BwexfJFkHm83XJGwIMiNqO6mhQwpYo6IcUrhXwQMduk-Lk4kAbppxNiP_bif3iBPg09YqtgTv9DTlHdPymPPZhx_72OBxca_Y-0VOJ_qg6FPu_PgRyX8jFad6XQei0fGHyZzvjoSaxyyUYt_aU0iffwThyYs5eTjFe3REhIMYTZIn1UEV20rRCtyVZoQnBkNxEyvypcymOTU33DThGp5a7ugBwnBbXvif3SEN98qWNDuKX2Z9uqmzGxTpjYiXzZCz0XRZfMb8p63fSKlHAba6udhdH-zdPqYtrI0bmUh8Y94F7NlJAPA4oTV8oKq8mAFGxS53cyU5LMLpRF-jquaS37JZgaLf9Q3K0Lgs2M7DgAsTAx6k3TqxzJlB8e3JGHQNG8IsdhVUq8NK_aXL8ZBmaDubMNJu3Ro1bcKi0mzj0_OPjUr4LNqyYXp4loXUBAu4QAAt-VwMrtb_gCirXvAHrUT_Lap-m0Pwyt6Nfw8to9CjS0HAuDj0tNNBYPgP3YzwDYUZMkm0aj-i8F76Zy8RuZDR_cLDvu8CyNEbTm2gW5G2Paj9_aq75iT4vbRz-Frj8NLwDp-ch55a8iNm0g5EVJm5_cTTwq5PCX97jbZbdqp2iAXd60DmJDGv9mo6Ygoevchhvd4GijSZNlj0-w8rfq7ejD6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb3633452.mp4?token=NJTeOplRjrfOk-BwexfJFkHm83XJGwIMiNqO6mhQwpYo6IcUrhXwQMduk-Lk4kAbppxNiP_bif3iBPg09YqtgTv9DTlHdPymPPZhx_72OBxca_Y-0VOJ_qg6FPu_PgRyX8jFad6XQei0fGHyZzvjoSaxyyUYt_aU0iffwThyYs5eTjFe3REhIMYTZIn1UEV20rRCtyVZoQnBkNxEyvypcymOTU33DThGp5a7ugBwnBbXvif3SEN98qWNDuKX2Z9uqmzGxTpjYiXzZCz0XRZfMb8p63fSKlHAba6udhdH-zdPqYtrI0bmUh8Y94F7NlJAPA4oTV8oKq8mAFGxS53cyU5LMLpRF-jquaS37JZgaLf9Q3K0Lgs2M7DgAsTAx6k3TqxzJlB8e3JGHQNG8IsdhVUq8NK_aXL8ZBmaDubMNJu3Ro1bcKi0mzj0_OPjUr4LNqyYXp4loXUBAu4QAAt-VwMrtb_gCirXvAHrUT_Lap-m0Pwyt6Nfw8to9CjS0HAuDj0tNNBYPgP3YzwDYUZMkm0aj-i8F76Zy8RuZDR_cLDvu8CyNEbTm2gW5G2Paj9_aq75iT4vbRz-Frj8NLwDp-ch55a8iNm0g5EVJm5_cTTwq5PCX97jbZbdqp2iAXd60DmJDGv9mo6Ygoevchhvd4GijSZNlj0-w8rfq7ejD6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز بر پیکر شهدای شناسایی شده مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673990" target="_blank">📅 09:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر هوایی از تشییع پیکرهای فرشتگان میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/673989" target="_blank">📅 09:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ce7fea5b.mp4?token=I_GQcFwqBF4jv_KE1f3jIyvc0EGYKgT0vUWUQ-en7jnkAmchHmsG_ErkR3oOUzyYOBM_jwzY9uV0zNIDyLNIydbi62G24ACW02Er4Tcyoats95Uf6wmOnWIRkDZ0CjWnpqubtx3HADzdhmL_cEjCKUsMS-hSXLyZbK8eAxgD9HcHNZLea0OFNXechAKk4I5Y-VnY8VUCDOu1VLulYONYw8LyWZENpGb8JoBKTTfSUmc25ZKiSr5B9oxt0QBq889IdDEgqqfEKDNsKyO2liXxCVrAngtWvkW7Od00ZzRhuuB02q9O3OC_hJfDlRHUoAF6CrBWHAFGiawJKFpTxVYiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ce7fea5b.mp4?token=I_GQcFwqBF4jv_KE1f3jIyvc0EGYKgT0vUWUQ-en7jnkAmchHmsG_ErkR3oOUzyYOBM_jwzY9uV0zNIDyLNIydbi62G24ACW02Er4Tcyoats95Uf6wmOnWIRkDZ0CjWnpqubtx3HADzdhmL_cEjCKUsMS-hSXLyZbK8eAxgD9HcHNZLea0OFNXechAKk4I5Y-VnY8VUCDOu1VLulYONYw8LyWZENpGb8JoBKTTfSUmc25ZKiSr5B9oxt0QBq889IdDEgqqfEKDNsKyO2liXxCVrAngtWvkW7Od00ZzRhuuB02q9O3OC_hJfDlRHUoAF6CrBWHAFGiawJKFpTxVYiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارد شده به بخشی از تاسیسات نظامی آمریکا در فرودگاه اربیل عراق در اثر حملات ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673988" target="_blank">📅 09:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bESu0incjMWeJEbrQX7l4RS9e1omAp6WWFe0p_RHv9x14ryRPdwsulg_b27vpugZjmcCKK69Zztx1ACYd1u7FIed-rLlwnm3_RKsoIPn_uAdvMOmLGElKYzDBtjaGEYeFURJvlsBF3YdhRJ1CrbgvCiJOk8nQ_43Nfg_DAigK4zH-gEYXvvHCgAk3Er0qvorykq_-ug1-o00f0KoKnREuZhkme4-YQkAlgSeap8g2OxIg0xyQa_LX6k7-DoPhhP8iFYF2RuP4JMALGeo5e6COJf-cfwPPlTbViYgH9pdh9LnIuReqPPNIStLLB5YLkoYvXeNTHQyMeRdpepqDhyfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه دردهای بدن؛ هر نقطه درد بدن، نشانه چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/673987" target="_blank">📅 09:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
4
را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673986" target="_blank">📅 09:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادارات هامون، زابل و نیمروز امروز ۲ ساعت زودتر تعطیل می‌شوند
🔹
کپلر: دیروز تنها ۳ کشتی باری از تنگه هرمز عبور کردند
🔹
آمریکا و چین در سپتامبر درباره هوش مصنوعی مذاکره می‌کنند
🔹
حمله پهپادی اوکراین به تاسیسات برق جنوب روسیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/673985" target="_blank">📅 08:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سپاه حضرت قمر بنی‌هاشم (ع) چهارمحال و بختیاری: احتمال شنیده شدن صدای انفجار کنترل‌شده در بخش ریگ لردگان از ساعت ۹ الی ۱۵ وجود دارد؛ مردم نگران نباشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/673984" target="_blank">📅 08:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع شهدای تازه شناسایی شده مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/673983" target="_blank">📅 08:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من ایران را دوست دارم چون شعر دارد هنر دارد تاریخ دارد وسوسه ماندن دارد وطن در دل آدمی باید باشد
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/673980" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب جان ایران
❤️</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/673979" target="_blank">📅 08:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ حرکت مؤثر برای کاهش درد و خشکی مچ پا #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/673978" target="_blank">📅 08:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی پیکرهای تازه تفحص‌ شدۀ شهدای مدرسۀ میناب برای تشییع
🔹
مراسم تشییع و تدفین اعضای پیکر مطهر این شهدا، ساعت ۷:۳۰ امروز در میناب شروع می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/673975" target="_blank">📅 07:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۹/ زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و شجاع ایران اسلامی؛  با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/673974" target="_blank">📅 07:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kExtpLglSV1zNJGMOJVxe5v44JNKfgIqYzw2LbOhnphZovd-tiIY-U0n61mcCNnrChZxRCj01D4kK9indi04P1XxyB22mz3Ux8aG3BbhwQomomyoh4ktexMWEcOqFkNUuOIbb1FmdKeFeKozLNAa8qCNar27UsCb-9Gn39YTHnVH9wYlyeBuLXhBOvbD2syNysZaUKy4OWlQsqmYzi_R6LMR4HE_F0_3hP1e9QG_zltGqpmrq2lrKZr6pEhunltPp0RKD5Q5esDjJP37Ek7lJrjRvYoTzxAFHZF8cvyG4Bi_lhuQRaQ9BuSm-CL52pRO6f2aKqHT32eyYbOpw_NFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳۱ تیر ماه
۷ صفر ۱۴۴۸
۲۲ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/673973" target="_blank">📅 07:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هواشناسی برای برخی مناطق هشدار سطح نارنجی صادر کرد
سازمان هواشناسی:
🔹
به علت تشدید فعالیت سامانه بارشی هشدار سطح نارنجی در ارتفاعاتِ استانهای زنجان، قزوین، البرز، تهران، سمنان، مازندران، شرق گیلان و غرب گلستان صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/673972" target="_blank">📅 07:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/301b24f24f.mp4?token=q8uq9wf12pNAfCaVv3SpQds1ualaa_kwlwAmc7Xgpx-8HMUBnqf66QyFcuVvMvRJVMFr_KL_9av7KQ_JIbKT-19U3e8uvJhYtqwJdlk-2dB5s-jeILDZXNrMGMjYI3D2FFZ9s6UGAkRA9YcbQZ3hOzCmvGMCKHkWDp8P0uJWos9__OLWisTqgtiuPoS0KHUInsmAk96tJFv5q--n6LpjOWwS6qlyPNjfveft4Iq6gOAJDKHeLrIcHGf5e4z1MEzc_7oxUKfcWxiBD-NWC7P_r83YcRYGxesWDoHuXd1kbvKBKh1sQTngo-069RjAF4OYnqL_wX7aF3JWqbtf4mFYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/301b24f24f.mp4?token=q8uq9wf12pNAfCaVv3SpQds1ualaa_kwlwAmc7Xgpx-8HMUBnqf66QyFcuVvMvRJVMFr_KL_9av7KQ_JIbKT-19U3e8uvJhYtqwJdlk-2dB5s-jeILDZXNrMGMjYI3D2FFZ9s6UGAkRA9YcbQZ3hOzCmvGMCKHkWDp8P0uJWos9__OLWisTqgtiuPoS0KHUInsmAk96tJFv5q--n6LpjOWwS6qlyPNjfveft4Iq6gOAJDKHeLrIcHGf5e4z1MEzc_7oxUKfcWxiBD-NWC7P_r83YcRYGxesWDoHuXd1kbvKBKh1sQTngo-069RjAF4OYnqL_wX7aF3JWqbtf4mFYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست‌ویکم عملیات صاعقه ارتش؛ پایگاه و مراکز مهم آمریکا در کویت هدف حملات پهپادی ارتش قرار گرفت
روابط عمومی ارتش:
🔹
در پاسخ به تکرار تعدی دشمن خبیث به مناطقی از کشورمان،ارتش جمهوری اسلامی ایران در مرحله بیست و یکم عملیات صاعقه، ساعاتی پیش، " انبارهای مهمات" و  "تجهیزات لجستیکی مرکز فرماندهی نیروهای زمینی" ارتش جنایتکار آمریکا در پادگان الدوحه در غرب کویت را هدف پرحجم پهپادهای انهدامی خود قرار داد.
🔹
الدوحه، از مهمترین و اصلی‌ترین پایگاه‌های نظامی آمریکا در غرب کویت و یک مرکز پشتیبانی برای نظامیان آمریکایی حاضر در غرب آسیاست که حجم زیادی از تجهیزات و سربازان نیروی زمینی آمریکا به همراه نیروهای دریایی و هوایی در آن مستقر هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/673971" target="_blank">📅 06:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تایید حمله هوایی ساعتی قبل به نقاطی از استان ایلام
فرماندار آبدانان:
🔹
ساعتی پیش منطقه چوار و آبدانان در استان ایلام مورد تهاجم قرار گرفت، این حمله هیچ تلفات جانی نداشته است.
🔹
همچنین حمله هوایی به منطقه انارک در چوار منجر به آتش سوزی در اراضی منابع طبیعی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/673968" target="_blank">📅 04:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بانه در استان کردستان
🔹
بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه هدف حمله دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/673967" target="_blank">📅 04:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ با توافق هسته‌ای ۳۰‌ساله با عربستان موافقت کرده است
🔹
این توافق دسترسی ریاض به برنامه تاسیسات هسته‌ای غیر نظامی و احتمال ساخت تاسیسات غنی‌سازی با مشارکت شرکت های آمریکایی را فراهم می‌کند و همزمان نظارت واشنگتن بر این برنامه را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/673966" target="_blank">📅 04:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای سنتکام
:
ما یازدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/673963" target="_blank">📅 04:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcrY8LbQrulbdiKPOP4hMQNWqFl8bx-3_BisSWr8FkuM6E1b4RUgKrOXGannc5J_1BYHKteYhG5-jAfrDmJIal99EIvG4UnEaGPgXdWG1Zw57GW9Jdlso4bax2Ru6FRmGWHQRGLHq6F327ZfuEwcDdwQ6Y1z7-0dJbvianPG1O407yhf41FJbp3izJXFtWOEUVT6TShkCOO73b9ilT_ODHpmjP3Qa1MN9Y6mkUZE7H_491tWI8Q08n8fJC0twkuNS5Tzu-98yYS1pFejOyIdufNm4NrBPZCsgc6kqmlRYxCv5QO5dSsGe9E3yAjiFOdKLU9-3hoUwMQ4j--n3GKmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پلاکاردهای معترضان ضد جنگ علیه ایران در جلسه استماع سنا همزمان با سخنرانی وزیر جنگ آمریکا
🔹
نه به جنگ علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/673960" target="_blank">📅 04:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پدافند تهران دقایقی قبل بار دیگر در شرق و غرب تهران بزرگ فعال شده است و به نظر می‌رسد که پدافند مشغول مقابله با ریزپرنده‌های احتمالی است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/673958" target="_blank">📅 03:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع خبری دقایقی قبل، از شنیده‌شدن فعالیت پدافند هوایی در غرب، شرق و شمال شرق تهران خبر دادند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/673957" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/673956" target="_blank">📅 03:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
دقایقی قبل دشمن آمریکایی نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/673952" target="_blank">📅 03:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شرق تهران خبر دادند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/673951" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/673946" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هشدار مقام ایرانی درباره هدف گرفتن منافع انگلیس در غرب آسیا
خبرگزاری تاس:
🔹
اگر لندن به واشنگتن در جنگ تحمیلی علیه ایران کمک کند، منافع آن در منطقه هدف مشروع خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/673943" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ترامپ به دنبال دبیرکلی اینفانتینو بر سازمان ملل
نیویورک پست:
🔹
دونالد ترامپ خواهان انتخاب جانی اینفانتینو، رئیس فیفا، به‌عنوان دبیرکل بعدی سازمان ملل است؛ پیشنهادی که برای تحقق آن به حمایت شورای امنیت و تأیید مجمع عمومی نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/673942" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHBH2jOAgBaulvD3aQQTGoXh2yDXlLg7GEqaF3wj5-s_MTxJ5a3-Q9BooilB7ZXhYS4M_LF27d6hn2yuhyw1D9oWVA8gjlG6lbKAaysrQjz30FW2T6X7KTEyLzH-oxBH1kCpnFAqQyyyxmKXbRvGt0oJidD4qdoiBTKm6aTY-QHTqkNGaIvabur-HFYUI9yiNTu8aFlXQmrsVmEkhY1ih0PyFC1zEZqhGDLtYPT3msLgJZ9hF8hoCqzTTCWnuT64D5Y2YqI2SSNiewDkNeFBhoglH-JUSZOiKlj_Hkc4szyUEpPHDGMkrL624a4AcA6H_hNMmeeBy2f8L7zPw7G_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر خارجه چین به ترامپ درباره تنگه هرمز
🔹
خوک نجس: برای بازگشایی تنگه هرمز روزانه به دو میلیارد دلار نیاز داریم.
🔹
وزیر امور خارجه چین: تنگه هرمز قبل از جنگ باز بود. ریشه مشکل در اقدامات غیرقانونی شما علیه ایران نهفته است؛ شما از هیچ، یک بحران جهانی ایجاد کرده‌اید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/673941" target="_blank">📅 02:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تناقض در ادعای نابودی موشک‌های ایران؛ چرا موشک‌ها همچنان به اردن می‌رسند؟
🔹
گیلیبرند، سناتور: شما همچنین گفتید که برنامه موشکی را «نابود و از نظر رزمی غیرفعال کرده‌اید.» پس چرا موشک‌هایی باقی مانده‌اند که به اردن اصابت کنند و منجر به کشته شدن مردان و زنان شجاع ما شوند؟
🔹
هگزث، وزیر جنگ آمریکا: آنها ۴۷ سال است که تلاش می‌کنند موشک‌هایشان را در زیر کوه‌ها پنهان کنند، دقیقاً مانند توانمندی‌های هسته‌ای‌شان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/673938" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی در کویت، هدف قرار گرفت
🔹
ارتش کویت نیز اعلام کرد که پدافند هوایی آمریکایی در این کشور، با حملات موشکی و پهپادی متخاصم درگیر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/673937" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/673935" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره
هر چهار معترض
را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/673933" target="_blank">📅 00:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/673932" target="_blank">📅 00:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: من اذعان می‌کنم که ایران هنوز هم بدون شک توانایی‌هایی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/673931" target="_blank">📅 00:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673929">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GybwSWiyRBfl3Ns7iNItnP6IAzZKkaTqkTzIyEidQyib28P_yhnfmZ5Mj6jbsL4waD4GhR5LMWNAwy3NleKddYN4WlizCKN__qFOuitTvZh3sbO5nTksogpWkdmR0D2zX_VXdUFFFKJf6x2snFzR1zEnzeSEJR_Bnh1Bt9A29kITFhf1e3nzVgRVBW4gFDVduvgjs7ktN4-EC_SIngM0LyyqHUAB47UYoNYZz01BgBx7N8Z4VkCFV8wl5SAAFgFaGoQof84zT4LIl6f62oTRx3ZW0zZ6X_PGeBpP1IqFgyqsh8B_eJGIxBoUzPGp0Qa1NWGCQVhHISvcqqZbEQYMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/673929" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673928">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3eFET-B9x3b5yaIpm3h2QcmnptDVYB2VrZs_8XmtVqk_OftFuQhdKe5OniluDEgNEMIguF7kaBcCQ-4DuQF6DkQ3FN9NHI7Ax6H_nsKlnp53PYeXPBybYeESWKVW8ksHzRpTUG-y8rx-dzF4uihyM36ObMJav_Ad53s1exMbRyYDUfPBEvJ5CTgRj3d_9wFvz-0ooX4r_bg65fXjgZXsOav4zI8Iqe525Gf8d2p06Hwcf3PlNzt9U_Uni4ZY7qG46uKuxVUCj_5qqOGA5SYeZqJItNZF7Kaf3us7jTkt1kPhB3IC0aj3KPWF9GO7wmiwAC5Xlz4gi7P1VKEk22fQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاتر تحصیلی شفق تولید انواع دفاتر مشق طلقی فانتزی وکلاسیک ،رحلی،و....
تماس
☎️
09129318455
دریافت لیست قیمت
@Ghamilou73</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/673928" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
🔹
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم‌پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/673926" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
واکنش وزیر نیرو به خاموشی‌ها: در حال حاضر برخی کشورهای همسایه در شرق کشور با قطعی برق ۱۲ ساعته مواجه‌اند و در برخی مناطق دیگر تنها ۲ تا ۳ ساعت برق متفرقه برای تامین نیازهای ضروری وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/673925" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی خطاب به وزیر جنگ ترامپ: شما چندی پیش ادعا کردید که ایران کنترلی بر تنگهٔ هرمز ندارد. اگر این حرف درست بود، ایران چطور توانست هفتهٔ گذشته دوباره رفت‌وآمد کشتیرانی در تنگه را به حداقل ممکن برساند؟
🔹
ادعای مضحک وزیر جنگ ترامپ: ما مدت‌هاست که کنترل عبور و مرور از تنگه را در دست داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/673923" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: آیا توانایی نابود کردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/673921" target="_blank">📅 00:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyzemymJEu5J9j1g_fq3obVsQKiOQdd48wk_R5b3mxFoq5qF8u6bfFDnd-OcY7UDWonnFMVbkT3gtRXqAzuixuohvxs5Y3vkQ9pGbcYzwDWCALo6brC-LKgiJ6aOWqWQ9jS_z8NDHw7as2U8bIlvff1xMDCVjnCqj65FXVJMqXDypL7m47bNJa7Ijt8cnom00b1A25R2EO-cte7BB1Dmoxh45NiHwDuRijYiK5SJ0KBmhqjH7UE5jNqxK-EukWhWEz22rODVHtvGZ9L81OmFJV4LAcL9NHKj9VC_dKlAMIPpSG7nTg8Nb3fAtgwYtdByCR6z6tqfXZe3AVzJG85ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/673920" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673919">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJr10TIUEogfrtitFSxUJfrUEazEIGe8GNAotXmBfkvJEQByN8f5-0SK08sMWdt8Rg3mBLu4buwdPkaaDigj4RrDUUBKJR-eW7mtO2zNoU35wLnxUZ-LvptwZmQCVCW8FDKKnyCNUQ_FbpOi01KIbcnHZJ0eniTNSVcAEPwf_HQdDDvjhhsV5EVV7qn7YbjLGQIJjx_jAPzh0LC0KbVLiJCv8ikXQnBxny1caz4GyLGDVs1sEhs4iwdPg-zittu3X9kwxsp2ZN3gJplVdtT5IDcawExBZ9-Q-RNrIjBsIMPgW8mcdiEmeNHtipMQSD5CbQvwUeZNMkFYR5QLcKpEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ترامپ برای حمله زمینی به جنوب/ ایران با این سلاح ها آمریکا را شکست می دهد
🔹
نزدیکی ایران به محل استقرار نیروهای آمریکایی سبب می شود که توپخانه ایران فعال شود و ثمربخشی چندبرابری آن را تضمین می کند. توپخانه به دلیل نوع پرتاب توپ و نحوه عملکردش قابلیت رهگیری توسط پدافندهای دشمن را ندارد و به دلیل نزدیکی به محل استقرار دشمن (در جنوب) ضربات سنگینی می تواند به آمریکایی ها وارد کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232047</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/673919" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673918">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای پیت هگست: انهدام تمامی قایق‌های تندروی ایران، تمامی تیربارهای نصب‌شده بر روی این قایق‌ها یا تمامی موشک‌های کروز آنها امکان‌پذیر نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/673918" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673916">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/673916" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: جنگ با ایران تا کنون ۳۷.۵ میلیارد دلار هزینه داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/673914" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پردۀ فراخوانی که به‌ اسم انقلابی‌ها منتشر شد چه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/673913" target="_blank">📅 23:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگزت را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/673912" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlijnJ8EW09oJsobnvM7g_Z4hpLPPi4E7K5egDIZzHu104XYb0wsuoSrwf34yWFt1Bsw1gqHOJWuleakiWm8xZ3m83MpKKXvcTX06L0qhadvuh5byUMifJXW4wUUmvpxSWYKaE9uFtB9V6Pk1Cj6zkP5zBlKueU5L1v5FxM7wt4Y3a6XfuhFeAjXO0Fg5AgKB69luhpVaBbttTObaQRmwomRqDR03iIwD-Nn07DRboDNOs8AfXDw9Xfxfuck8Huaa6AxaHIVVHI9oGOqFxbLCHZ6dSiCSExAAYQFktY8_2yN2QLX6QgStLzSoRGNxMXhr37baE01a1gQ4DRXPLlVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: ۱۸ آمریکایی در جنگ علیه ایران کشته شد
🔹
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته
🔹
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
🔹
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔹
جنگ کره: ۳ سال و یک ماه، ۳۶۵۷۴ کشته.
🔹
جنگ ونزوئلا: ۱ روز، ۰ کشته.
🔹
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/673911" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673910">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ahwWr2Q0pjXDsnYu-6P2qghDfRB5b16fuHeGET3mn1Zp0QDxKEVFe7e6tyZobWZ-9JliFyaHGFvpkallfOuH9EV840PYc1ax_hC2jOOG1o6WnvWh5qWg5R9Tefxcux20nZUg3exzl518Wj-EbgYp58xCHNEUklTFMzbm1cknBR4S52MPqIeQ37X4YNvrGUOB0k48rfOGzoFREQKZvkAZ6khaTEEvdMTTt67smITLHI2tViee1Vfp6Cco3fqteL5F2SHHMwXWYzsy6TuhhAQYmm47pS05MOXgJUmk_F2sGkX4zq4bo8hWHTe5hPA2UpUVa4xS2Bb_JHjB9LCm3qlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام معنادار امارات در روزهای اخیر: اقامت برخی ایرانیان در امارات دوباره فعال شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/673910" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673909">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خوک نجس: پرواز‌های مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود.
🔹
وزیر جنگ آمریکا: اقرار میکنم که ایرانی‌ها هنوز هم توانایی‌هایی دارند.
🔹
الجزیره: آمریکا در حملات پی در پی به ایران دستاوردی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/673909" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNEgdx5Xn2-CnvuyPPigT-z6RekhF0fWTZS3hzLBh-ZhM6JDmJcA-XhaWqtu_CCqVPu_DyNnbb6mm2rJwzyoquXPrD73yZ-1b9cL1DaF10BxbX1EGf6pC9NyJqjuYKF-ax2miO84SFUQyO-O_x0U64GYMljdRlvHDOqgcpxfkcwcQhMcYadVZ8MfsgTJ2ivNeaLJ5g0n2DcFLXXxorQ6eud6rsmTIX8zzHTm0XShU7XocO1UuB4nPFdPzU33JA08NfSdQOheax9BWAT_IIvNNhn9Um_rKiLJjsieSv96Q9LNyi0o9wJY3borcLM4kd5n_Fh67O-_NoASC3JU7OB7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ اپلیکیشن هوشمند؛ برای یک گوشی حرفه‌ای تر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/673908" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/673907" target="_blank">📅 23:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر ساعت ۱۵۰۰ مگاوات در برق صرفه‌جویی می‌کند
سیدجواد حسینی‌کیا، نایب رئیس اول کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از ظرفیت‌های عملیاتی برای کمک به ناترازی انرژی در شرایط فعلی، بازگشت به تغییر ساعت است. برآوردهای کارشناسی نشان می‌دهد که این اقدام حدود ۱۵۰۰ مگاوات در مدیریت بار شبکه تاثیر مثبت خواهد داشت.
🔹
طرح پیشنهادی در این زمینه تدوین شده است و امیدواریم در نوبت رسیدگی قرار گرفته و به مرحله اجرا برسد.
@TV_Fori</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/akhbarefori/673906" target="_blank">📅 23:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673905">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVIPu3P6VQyX0zq7QY88n1yCaxslyCTkt1xp3W9oigZ_ouYkg16bOXqrn6vzaLN8ERp1z4Iekzy-xsVB1xKbVuNHNObzqrFnkK_HdRK7NZwAmKcgv5sd-m6YgxAtB3QN_ceCxbizYO3x4eEjQszaNCIbRdXHBmObX4JZuWUQ_PyJrr_MZMSW5e9yX0xMDZhrIevrXrp8FR1Fn3f7dSPSwS-upTAxZhBe6HQ3EndXHzcYkf-XAX1E26qgl6E07bBpaGw4MfDC56IGD-AExzXgRV-IXG3H0GWI67KOnGbsKF5D3EGgU40bKpjeJeZqgMM5TKQgKy0uJL2gkqwe2TSzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر جدید بریتانیا استفاده ایالات متحده از خاک بریتانیا برای انجام حملات بمب افکن به ایران را تایید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/673905" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673904">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۰/ هلاکت تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش تروریست و کودک‌کش آمریکا در منطقه‌ی الرُکبان اردن   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت بصیر و همیشه در صحنه ایران اسلامی،  با دعای خیر شما عملیات تنبیهی رزمندگان…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/673904" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpFZFzII_KPcGRmPesVkAlxWdqKwHlThYovMN6RVvcvIa7-VGmOcBHPMI4rxmh-NOZUEUIzIc9hGEupSsitLBJ7vJ6J4ZKXNa75-R2Cmhwvt-17njcDlFJ9x-V_ja8O0aPtPmdXTCHdedewvW75mBADuhosExrVvIbfy_HrcjTZBOegp3NZ4rIrnb5Y287UwJqiy9IsU3uizKqUv2iYLtJ76P0DzNIvM75XKZZMw-3Sr_ESjvLyYMsdXrzsW5KpCmo0RfmGjweQodiB8OkK_Zjyv5qlk5uJj3RcaTPt03kRwI9pTZBBgsVESoZF4kvG6ahCXhOQQ1ehMlL6ynljjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت از منظر امام علی (ع) چیست؟
🔹
از نگاه امام علی(ع)، عدالت تنها اجرای قانون نیست؛ هنر و توانایی فهم درست موضوع، دانایی عمیق بر قوانین، داوری شفاف و بردباری است. کسی که حقیقت را درست نشناسد یا در برابر فشارها آرامش خود را از دست بدهد، هرگز نمی‌تواند…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/673902" target="_blank">📅 22:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تحلیل جنجالی مصطفی خوش‌چشم از تصویر مقاله ظریف در نشریه فارن افرز: تصویر می‌گوید موشک را بده تا بتوانی نان بخوری
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/673901" target="_blank">📅 22:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که یک ایستگاه پشتیبانی زمینی و یک مرکز تعمیر و نگهداری مربوط به یک بالن شناسایی آمریکایی در فرودگاه اربیل در شمال عراق، مورد اصابت قرار گرفته است
🔹
به نظر می‌رسد پهپاد با دقت هدف خود را مورد اصابت قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/673900" target="_blank">📅 22:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشورهای عربی دست از پا خطا نکنند!
🔹
کشورهای حاشیه خلیج‌فارس معضل بسیار بزرگی دارند که اگر همراهی آنها با آمریکا ادامه داشته باشد، شاید ایران ناچار به یک تصمیم مهلک برای آنها شود.
🔹
ماجرا چیست؟ در این ویدیو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/673899" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673896">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه دوست‌داشتنی فینال
جام جهانی فوتبال
🔹
شیطونی‌های برادر یامال در جشن شادی اسپانیا پس از برتری مقابل آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/673896" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رسانه عبری: الجولانی برای عملیات علیه حزب‌الله آماده می‌شود
شبکه صهیونیستی «کان»:
🔹
با وجود اینکه مقامات دولت انتقالی دمشق به صورت علنی از مخالفت خود با ورود به مساله لبنان سخن می‌گویند، اما در عمل دمشق در حال آماده شدن برای انجام عملیات علیه حزب‌الله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/673894" target="_blank">📅 22:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR-KiskaLIVsA3zL5RUbKxAtrj3DiJtiQOn6VNNG1s3sJQTG2aWIDLz1-uR2XSw7_4AB4bpwyVEL6Qt_VPQdEL7PL1FEmeUHNp-YBcqj6_ILkvn87od7ZOVojo51psuOTW47TkxwucAcG9VHdkj8y19OUN7g4sOofjqCiYrtMJNS1DltdAnkJvqERBl96uUO48ZVJAWbv3hlvGO3srtCaZ8myCgxusA07GtcvkqN5dyU0gn0KLXFbI5zD2B1gslPgFP3tHCbdYtmRo4BkUbnbuOQPuzyipaOPLvVQNjBMbG0m-Z33Tf6_rCeJxUmOddCmTgH22OXp5AXVfYYXc1xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبانی از دشمنان ایران و همدستی با آنها، نشانه ناسپاسی و فقدان آینده‌نگری است
سخنگوی وزارت خارجه با انتشار عکسی تاریخی از سال ۱۹۹۱ یادآور شد:
🔹
ایران در سال ۱۹۹۱ با وجود حمایت کویت از صدام در جنگ تحمیلی، به درخواست این کشور، تیمی ۴۷ نفره از متخصصان خود را برای خاموش کردن ۲۸ حلقه چاه نفت در میدان برقان اعزام کرد؛ عملیاتی که به‌عنوان یکی از بزرگ‌ترین مهار آتش‌های نفتی در تاریخ ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/673892" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بازسازی زیر سایه تهدید؛ فرزانه صادق در کنار کارکنانی که خدمت را تعطیل نکردند
🔹
فرزانه صادق، وزیر راه و شهرسازی، در جریان بازدید میدانی از محل آسیب‌دیده راه‌آهن بندرعباس، در کنار کارکنانی حاضر شد که در شرایطی دشوار، هم‌زمان با تهدید حملات مجدد، حضور پهپادهای دشمن و گرمای بیش از ۵۰ درجه، مشغول بازسازی خط ریلی بودند.
🔹
این تلاش بی‌وقفه، زمینه ازسرگیری خدمات جابه‌جایی مسافران از ۲۷ تیرماه را فراهم کرد. خدمت، حتی در روزهای سخت، ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/673891" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBDJH2dMtIFUwPXrGrU8NXB84O1S2PvVAJPtQH-dAK8vW-7QsJuxHsPUW4wiG4AIC9SJslM4cKQNPnl0rUtQAJHWddjvSyCiKjcQtvuNjUPUoJV_8J_Gs0J7EW4fLxvnOi1Bhb4rVTaL87r9Z8cVpKAqYnhCE_mezwp5ihcZFThsOcev0Xl6ksMiQEZ6P0db5e_BDzRv97abZKfBEYJlTAR4WYwCih4ror0AZoRZMXCnTwD91K95L4k3WjFUK0Y8ZAxcQDN8OQKr_C_Fl8wZ6I-h_l7yx0Dv5U7_B1_mND1aB5Vh61f8tNdntTRjod5ACjrbWZQ4k8VC_6VQhSaCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام چند هواگرد متخاصم در ارتفاعات شیراز با سامانه نوین پدافند هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/673890" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNJsSsAgiVQpU_SCGWJGmtmBA5UxQ0Du3yN--4j0o4hl1ehFGRswl3th7yq4CEB2ZDmG1Wt243EaegfUEwOGXaoCdv2RvFcFshkLdOEtD0WPM1PJKHNllFnauLmfbb9uMlq-nIbqW4opFGRm-Z1pS0dlrklTcQobnqXMlrbwZYUVX286uvbChQ2mDq_ZoMZW6W5Xdrdq7P49JetdmWdscbzSxCDrS0cct6A1-lZx3R00K40WI4QmxoS4P2-k_TP0EVfWGGJY438Q1wzLW4qw6V0eqdAV6csnA7TBIuB-vayEZP4RyDgCryJRlf_br04UrixK2hkzv-aJ_da0x57Lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب؛ غول درآمدزای ویدئو
🔹
درآمد جهانی یوتیوب از ۱۵.۱ میلیارد دلار در سال ۲۰۱۹ به ۴۰.۳ میلیارد دلار در سال ۲۰۲۵ رسیده و در کمتر از هفت سال حدود ۲.۷ برابر شده است.
🔹
بیشترین جهش درآمد یوتیوب در این دوره، بین ۲۰۲۳ تا ۲۰۲۴ رخ داده و درآمد این پلتفرم از ۳۱.۵ به ۳۶.۱ میلیارد دلار افزایش یافته است.
🔹
بخش عمده درآمد یوتیوب از تبلیغات تأمین می‌شود و با رشد تولید محتوا، افزایش کاربران و توسعه سرویس‌هایی مانند YouTube Premium، درآمد این پلتفرم طی سال‌های اخیر روندی صعودی داشته است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/673888" target="_blank">📅 21:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
منابع: منطقه‌ای که در بحرین هدف قرار گرفته، محل حضور نظامیان آمریکایی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/673887" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb76U0BxJsuA1NWxZw8xZnm5m3xuNpzyqBmH3jWg_gkXO8GXCvnsdopp-7WYJKQE7JLmpCODfSqPJbxJVhcGwbVaJ8W4hX652wY2Un-ky8fgMuBReSYCCHF62qvqzcU-Cn8us9HzF7eiYJFiB828FjHwtrtepaNZyNdHTNDx9lXOa9aAkMKyINYS84zTg47N63vh4Sjx73jzqYucDYxTgly30Q9u7lHLqIT0GLvBGZQoIDnTn2bQCeJcSiRKUEY3-l3vsu4FS4CLsYrxGBfTHBhHo_3rQqlSxnv_PfRi70vTTj7hORCMt00FLEJK3G7nVqwxwu67OCa_Chw2xvpubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔹
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/673886" target="_blank">📅 21:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: حوض نقاشی
🔹
ژانر: درام اجتماعی، خانوادگی
🔹
خلاصه: «حوض نقاشی» به کارگردانی مازیار میری، داستان رضا و مریم، زوجی با کم‌توانی ذهنی است که با تمام وجود برای ساختن آینده‌ای بهتر برای فرزندشان تلاش می‌کنند. فیلمی سرشار از عشق، امید و انسانیت که با…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/673885" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673882">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/673882" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673881">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhwFJWAX4GmHVhI0clH2rE-qPxkJGNlLL_qqhskzbyerqKr46fI_i1scQLfOhjesI6hDgVXjitI-f95-7UKaJVqyJ2Ce3BzgZCIPoAc00NNCdwP1xUvYXfTiMRxbOj7ULmH25JD_vwJlqspVuR6rTXlg_FOpWyvF7M5X_YA_AJ5NAI8T4Z3vkaTE2KVkv25vmvJqVbnmR0GtkWwlIAYVTRDlMrONeXMXSFJomrW-Ak4qoHteDPywiNOaOnlvH3esCwuckK2ajwECVY9vKPuGROZJAFOM7B6aJJYKey2mSPTAZuewr8Oz33Fjr3JG_XXBmIn1J2QZil2phI1I3GMexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر آرزوی
زیارت اربعین
را داری، این فرصت را از دست نده.
🔸
به همت هیئت قرار،
۱۰۰۱
نفر به قید قرعه عازم سفر کربلا خواهند شد.
🔸
اگر می‌خواهی به نیابت از رهبر انقلاب در پیاده‌روی اربعین حضور داشته باشی، همین حالا عدد
۲ را به ۳۰۰۰۱۱۵۲
پیامک کن و در قرعه‌کشی شرکت کن.
شاید امسال، نام تو در میان زائران اباعبدالله(ع) باشد...
🏴
🤍
@Heyate_gharar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/673881" target="_blank">📅 21:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673880">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fujFvC1hZPl8L5Ah8P-5oIWv9Afy62OHVfk6nY60yIfGdzshRLxIa6FYTZBO939pWX4P3PKiZAf9TQFCatH7KYlddODUmlpq5ChM99UWg6aGbP0qafdftEMfpjljbgYTmdad7vTiekoq30f9Agou4dMcg0FFbJTHubIvd_QmutgJxbxW-1FJf0W_FmDM9xpwukcC78VChivJBD-5v6EZ2045wtg1koe-YjKezVnhKS2107LPUBfKcTDFEulwL6a6XYjx9m45FSe1YyH604YbaPcFvfOZku2Gy8io5S7dc1Aa120xsUdzpgy34kRGr0VYrX6I3VS9xT_4S2OGLSIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
براساس همین یک توییت می‌توان یکبار اختصاراً تاریخ تحولات سیاسی معاصر را توضیح داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/673880" target="_blank">📅 21:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCWVg2ajApHQW72ejor3bVl1PJcAN-CUZhhXp-6A6-7rwPjoF-xuwZqCUcpPGcpEm-0U8QDEoA8fZ3dFt6E-EXydGVgEJBQpxz1EyX_aRBb2F1VK0EiXeRDsmjreCnvlzrl36rbOQhmi19hmSB3wyU1zky-ZPiC6Rku6M14STPdewWZhCdcWowTVuQRxJRvyfLRMfbOY2nGUlg9XH9AJijXX7sQ53h-Uqvk5rwVSV8Arx_TikmFb9TCbtaRuiJsFQ1But6H0ZXD4oZ42W3vB8EYVgXIyLe4lmw4wIcsQXpD4zRD_vU6yd2W0G_XyzBKZWLaMFptuXcDAEmFdul2Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد رآکتورهای هسته‌ای فعال در کشورهای مختلف جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/673878" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده در رسانه‌های اجتماعی پلیس نیویورک را نشان می‌دهد که بعد از قهرمانی اسپانیا به هواداران کمک می‌کند تور دروازه فینال را تکه‌تکه کرده و با خود به خانه ببرند
🔹
اسپانیا در این بازی با شکست آرژانتین، برای دومین بار قهرمان جام جهانی فوتبال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/673877" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
♦️
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/673874" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت دوازدهم مستند احیاء و حقیقت | «جوانه می‌زنیم»
🔹
گاهی، پس از عبور آتش، نخستین نشانه زندگی نه در هیاهوی ماشین‌آلات، که در جوانه‌ای کوچک نمایان می‌شود.
🔹
در دل دیوارهای سوخته، میان قاب‌های شکسته و سکوت پس از حادثه، هنوز نشانه‌هایی از حیات نفس می‌کشند؛ گویی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/673873" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auOMfW2zlsXK7L2iObBlnrM8xVOLZeGAGvalFnkkF6CLX2MR8O7NfjvsonT-frswkif7MuDY_v1WNJ9l6KPYHksCsRwnjX_Y2prd0-TsEzndX7vWkCZeopqRboRDo8LzfQvPvEjSVk9aKkaXYxoaDrjVBRteAlOVmCqIRKqlycSNmDSnUkgkVPFfOa73kI4-XVtq6U3BO8upbHkE3Xpd1xGWYLsUWZQFEEzgoKpxV2nBlzG-PIQZGTxCgZ9vCVYpjhiQEclxOiiPbuG3kkCUHtgf4snaOPykqKrWEwkT8Qt7vpFiMHiFfo-FH-USTipfYtSnVev8y9X5s-LVT3ayYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سیاوش اردلان، خبرنگار BBC: ابتدا همه فکر می‌کردند حملات اخیر امریکا مقدمه حمله زمینی است ولی نتیجه ضربات ایران نشان می‌دهد امریکا باز هم بدون برنامه وارد عمل شده؛ یک مقام نظامی آمریکا می‌گوید ما قابلیت دفاعیمان در برابر موشک‌های ایران مستهلک شده اما کاخ سفید به حرف ما گوش نداد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/673872" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم از عشقش می‌تونه بگذره ولی از وطنش نه #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/673871" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
