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
<img src="https://cdn4.telesco.pe/file/DhHaoOHkm94pSi4JZpxTdEsHbhDCbMPwRShJIq2_0U1MoZzSUtMoC250DbaXyyZA0tYgd8Bfox_4qglyZ33TDhJ3p4tW6TfOZ2RUcYQWFOuAJJlTbK_sRx3SSa1wKFpzL4lDl1lo5yPIZnb_BqmsoD9giXDZMvIBqL_dKkYYT9cUpQDjYmNXQ8lCvXl3o8peTYU66WihsbodYB_-HxP19WmrPGxOY7SQzhDF4gS6jWn8gMSGKqL0KB8NP4rKgmWu9Ex8zGeQN4KP7MsupLDIxhJcIka_Csacz6DL2hIrzLkaBjV9dayQ2n7P1PpPdd3cpmgHXNrtwe4vckz4U1rdVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SBoxxx/21308" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نماینده امارات در مجمع عمومی سازمان ملل:
«امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و بوموسی توسط ایران است</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/21307" target="_blank">📅 01:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/21306" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر امور خارجه ایران: تهران پیشنهاداتی را با میانجیان قطری مورد بحث قرار داد تا به ایالات متحده ارائه دهد - ایرنا</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/21305" target="_blank">📅 01:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگر عراقچی به تهران برگردد یعنی دیگر مذاکرات شکست کامل خورده</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/21304" target="_blank">📅 01:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ اعلام کرد که گزارش Axios مبنی بر اینکه ترامپ پیشنهاد لغو تحریم‌ها را به ایران داده است، یک "دروغ" است.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/21303" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjnUFySlrnP4LwxyQ0xS_AzDDkcO6oRgbYoduabBmfg5pg_ov_cCNlgtDvR8y7dC204ngEprmyTM8VZr7yE7ZXDpWDuMBaWRurbxDuPK9z3oC8vmToDpeGuBBzPV2OGXQ0S1pESSTlfh8epTC4TaTEdAGag0yyHpyEX7w1j4jdX5KP1cCj-r8Mb1dZjqAVz7WQkZRJARw6JDd6_qx2F7T3YGGaSVLbQ7lsMBgPE6SP86SjxpXuuro2Q5Ol0c4_aJh0oQr7hZHp-yklaCd6z1PVIWaQxDu-kxR7zpv-FIUtrzvmxEStjhTuZtf4zcS4RspcrO6u3lHfXTYkU4Lo5rkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!  خواهیم دید چه خواهدشد!  عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SBoxxx/21302" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_wpEi8W6ldJAH1Le9w-F1i5e7q9vsXkzjexo5QoVqVLY1AlKiVEoOMKBRcW2IHrje6JjO4sJI4rCVXyimWFLKGiU_qDBhDFpO0CZnMV60p642ytsNo3eXopqJFF0SqSjlPyg2YC5abU74n-Nfu7dW_N9_ghta6_lM9heAULl2W1-07LgSurK772yVlIeQvsMYYJOHYuvDIvf51A-qpCzsrcVGCHexEkyj7bIAWXTgmjZJmjYbkonVSuDbcrras3-9Hde82eaDiNDtDnfqL1fWRWZIJ5I5cZHQSAI8ikq7cI4nZ_DdWjEfa9IByr7bbPRvyCnrkXVvI5DWkS2IerHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/21301" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ درباره ایران:  «آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»   «من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/21300" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ درباره ایران:
«آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»
«من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/21299" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/21298" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:
فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.
بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود ندارد که ایران یک نیروی شرور است که بریتانیا، منافع ما و متحدان ما را تهدید می‌کند.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/21297" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">احتمالا امروز ترامپ خواهدگفت مذاکرات خوب پیش می رود</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/21296" target="_blank">📅 21:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!
خواهیم دید چه خواهدشد!
عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21295" target="_blank">📅 21:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایران با توقف غنی سازی موافقت کرد!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/21294" target="_blank">📅 21:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAxy4gGpvu5S5-fxRdMsb42VEQuPELkToHKkRH-FJubcxORMrNvpg_cVsTQqfmBbh5MWfx9i2I0xduxEYv1Im4tdoQcF0loXROVaQMrGBUHqFEy_Ep0CSevAc3sTXLmn0jyYWp95oXGrnItO3pJvER1-wEuQ6_XxD0ULORzHZIP2mWWGZLFW7kqsYXURTF6zFzscQKoSmtihaIt0ZrzCi2Nq-ewdYzgSHOMz4THavnFh9xKHcfINL_hH7bA7sMUQ1NkYbMvWoh2yzAhpKHtg5xdAlDeLHC7Cos7bgEV1ZVnjDKExiwIBeahAjlENdv6KPXDpMKorWjlNEfHjXn_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران ارزشی تازه دارند می فهمند چرا دکتر پزشکیان آن روز در سازمان ملل از ماتریکس خارج شده بود!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/21293" target="_blank">📅 20:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در ۲۴ ساعت گذشته، دو اسکادران جنگنده آمریکایی به پایگاه هوایی اوودا نیروی هوایی اسرائیل در جنوب این کشور رسیدند و به نیروهای آمریکایی دیگری که از قبل در این کشور مستقر بودند، پیوستند.
مقامات امنیتی اسرائیل اعلام کردند که این استقرار بخشی از تحرکات گسترده‌تر نیروهای هوایی آمریکا در سراسر خاورمیانه است و نشان‌دهنده آمادگی بیشتر یا تشدید تنش با ایران نیست.
یک منبع امنیتی گفت که حضور نظامی فعلی آمریکا همچنان بسیار کمتر از سطح نیروهایی است که قبل از عملیات «خشم حماسی» (Operation Epic Fury) در این منطقه مستقر شده بودند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21292" target="_blank">📅 20:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗
عربستان سعودی پس از تعمیرات، صادرات نفت خود را از طریق خط لوله شرقی-غربی از سر گرفته است</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/21291" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیدید؟! این کله زرد حرامزاده را من بهتر از پدرانش میشناسم!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/21290" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش‌ رسانه‌های عربی از شلیک موشک‌ از خاک ایران</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21289" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترکیه یک هواپیمای ایرانی را به دلیل تحریم های آمریکا توقیف کرد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21288" target="_blank">📅 19:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید  پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.   این پلتفرم می‌گوید محدودیت‌های…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21287" target="_blank">📅 18:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlLFL29gSmm0itHLNUWOUVD5zZGaXdbluy-kXLkQMPudslHf82KP0sf4TuUD_GD-0UW7yNJ-HqMaonUzUfjMFGJz6Qqk2uCOIKYYTaPSawSz_l8bjfWJQu1P5bw4yffzrAfK5wWzs-61UTWHh1awuZE5eGTkaDYyKHOmSLq8uVKqy2YUI9I3tcXXqDncPvmJm33TbhtPH19Rprddp1ggsRnFCXpohdIwr8BTMtksOKK6WwJMje7-bB47If050Zyisks7fE_ABNJljBQXIMpgl5pR-hZFBCdcPAeFtEIQVQP4kfhbt8IPwFSH7yGg7yqqfLCqZYQSE06quBWCbNsXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
صادرات نفت خلیج فارس به ۸۰ درصد سطح پیش از جنگ رسید
🔹
خاویر بلاس مدعی شد: صادرات نفت خام عربستان، عراق، کویت، امارات، بحرین و قطر با کمک نیروی دریایی آمریکا، به ۸۰ درصد سطح پیش از جنگ بازگشته.
@khate_energy</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21286" target="_blank">📅 17:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21285" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21284" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21283" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21282" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هیچ کس را امین تُِن های ماهی تان قرار ندهید.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21281" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21280" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21279" target="_blank">📅 15:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم — پنبه — روغن بنفشه</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21278" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21277" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/21276" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21275" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21274" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:
دشمنان جرأت ورود به خلیج فارس را ندارند
رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.
او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21273" target="_blank">📅 14:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایران شکایتی را علیه ایالات متحده به سازمان هواپیمایی ملل متحد (ایکائو) ارائه کرده است، به این دلیل که آمریکا محدودیت‌هایی را علیه شرکت‌های هواپیمایی این کشور اعمال کرده است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21272" target="_blank">📅 14:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عملاً همه دارند نفت صادر می کنند جز خودمان!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21271" target="_blank">📅 11:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21270" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAbTPefZmgPwXrEo7bdqFKsvzxaG-v97QZFu9UFk4QvMCbbdMi5Lg61LXyHBbBzAfpm1LQT1eHJv1B1786kiSJPWW2fmf3D-_kxYBp1mDLV5ZLRc2-TX_hOu9zS0RuglL2RxQpzeMc93WqszEH5LVUjxsD-WFV_V6V9Rs7QDAmYkDF_bCZNAgtnumpKJuMagESdO7aztlfb-9Q7VMLr3G26IH7wdbNv0vRjG8Z0iG0L9GHxO3g7ZcALp49CjxZxufW1BbjfF46pt_x_JQgqm_Uu789JZgXZTe2zXP3JiwBZNkwiw4kByyXSL2qpkByv91yOOIfiqy-7wo11mC1zx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت عربستان در این جریان راهی چین می‌شود.
@khate_energy</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21269" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سراج، نماینده مجلس: حرف‌های عراقچی و پزشکیان درباره هسته ای و کوتاه آمدن از قصاص قاتلان رهبری بی‌اساس است و ربطی به سیاست جمهوری اسلامی ندارد
آمریکا می‌داند پزشکیان و عراقچی تصمیم‌گیر نیستند و محلی از اعراب ندارند
سخنان عراقچی صرفا اظهارنظرات خود اوست و هیچ اعتباری ندارد
اجرای انتقام و قصاص ربطی به دولت ندارد که نظر مثبت داشته باشد یا منفی
محمد سراج، نماینده تهران با اشاره به موضع گیری های مکرر پزشکیان و عراقچی درباره شرط ۷ روزه و باز کردن تنگه هرمز و رقیق سازی اورانیوم به دیده بان ایران گفت: « صحبت های آقایان عراقچی و پزشکیان در خصوص کوتاه آمدن از سیاست های نظام نظر شخصی بوده و نظر جمهوری اسلامی نیست. نظر جمهوری اسلامی ساز و کار خود را دارد و در سیاست کلان خارجی رهبری تعیین‌کننده هستند و در سایر موارد نیز مجلس و قانون مجلس مبنا قرار دارد. در حال حاضر محسن رضایی، دبیر شورای عالی‌ امنیت ملی سیاست کلان خارجی جمهوری اسلامی را بیان کرده است.»</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21268" target="_blank">📅 11:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21267" target="_blank">📅 10:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL78SmOc4Jx20gsFqX978tOpohlzjwdpPXXqmK6X_JTGTCHF1aT0rGHwThc2qZrnVPze4THno7hb1tl72Yx3E3j3k2_tfBf45OmM002fDxxO50dWiqa64m7cpKyd5LpoxnpNHuXcqAIAj56e3VXEQNngJQ2ilT9A4indOhgI7L524Yu9k7Gp3RzUQ_CVEmytbskyYrzbNjgjMR0sFyPFVtRN5LsW9wdF16qyMNS--h0PqIumq0-BXIltlqylZtX-Ag6piwOQJlZzvtuvMxox88PkrwenE0vi4doCVtDgNBnG5NbvHHtXGUckFMN1T98zPgcBJoLWJMxwRaf7W5gkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21266" target="_blank">📅 09:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk9quWNh9HVrCddJIOQuSfw6VVNnHp-yOgcjW1Ppb1VtfNwnjfH22FaTx3lZb6eMLMpxSzzudaChyUH-TwCtsnt-cH6tTCh1i84O4ffHmyKgTklCnrqO0d_pQs1qHszzZsHCL8g75VYQYLzRoAsTSl1VqFmKtdkHs_I0SxRVQfxd88gWk-f4i7LVd_3AINI7wIFi8RwlJXTA2qxlac-UoqUsx3Cd6Pt7DHX_Q7wmsoTmHLcVjbyU_40aCt7x8iNIEou8yJyOCFg-2e_1S3-TMX04X_3Six4-1UhZZOt1izBl_AYR7l-zDjC9xRSAs45WrskhFvAyaCralpQTic0xCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز به کف محدوده بیش—فروش رسیده و خرید توصیه می کند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/21265" target="_blank">📅 09:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKQu2MhoERhZumLsgYZx2QlafEsg8yo94DHypiEUhWcMlPbjjYdOPtgImKGtHdXfFkrJWfi5_bLH1XR6mA8dWQcZzR9SXeZpduP9H6Hfkkn7LVkFTT8mjrGuqbWEGTprcQTuXsUnQZvcWDU6cPEgMqwLBZGaCSDUrjy2uaVs7HfzIsMqoqpjdQ9xw1wga0ow9T3hjvtUOQpzbqTLAhmqSQYOoKdbU3v1nDD786qJSgTw-IOa3IJ0AGhsJRfhKPM7Z0W18coZGOHui19tv2f1DOIz9S2k1UOVV8_8kQj4sHrX-RFVyV8GmQ4O0KbTFrv1cLL8zwvXgIZENpq7aDTLzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی است و از دید این شاخص، واکنش بازار به تنشهای هرمز مقداری افراطی بوده است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21264" target="_blank">📅 09:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCxXN3tGQ70KEnVgDTWP-16TEjng4zMCLlXPboW8zduDUmecNHIN4qmhbL87n5ccAmCWifSn2Ch_ishbeAQAHGcj8CslKz-DB_y_nFbhZJX8GeJdHfxfEE4WYVGWMl1CdknA-gJrlYwsfZP-PJ-qFCyeRz_V2Qs8k3WeTw9yPPf4EwExQkVgtXin9BvHW9cpbeTP9cmK_qPFEqAatbsHM_5XRLWnX9b35jFiYeHQcmp5rGgdLgmqiywZimAaescMaHHCY-7iwZCDgjUsL3EZxhMYP5kI13yGksvnuTIpF4GDP4dfrP-hY9tOe7dIaAy-kMreEJ86ZaAQydBRYqJLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/21263" target="_blank">📅 08:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21262">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جنگ ایران و بن‌بست فزاینده آمریکا؛ از بحران انرژی تا تغییر موازنه خلیج فارس
بر اساس دیدگاه‌های مطرح‌شده توسط جان مرشایمر نویسنده پرآوازه کتابها و مقالات ژئوپولیتیک، جنگ ایران و آمریکا وارد مرحله‌ای از بن‌بست شده است. از نگاه او، آمریکا تاکنون به اهداف اولیه خود دست نیافته و در عین حال ایران نیز حاضر نیست بدون دریافت امتیازات قابل‌توجه از جنگ خارج شود. تهران به‌جای تلاش برای شکست نظامی آمریکا، به دنبال افزایش هزینه‌های جنگ و فرسایش توان اقتصادی و سیاسی واشنگتن است؛ به بیان ساده‌تر، راهبرد ایران «دوام آوردن تا فرسوده شدن طرف مقابل» است.
یکی از مهم‌ترین اهرم‌های ایران، موقعیت آن در تنگه هرمز و پیوند آن با تحولات دریای سرخ و باب‌المندب است. اختلال در مسیرهای اصلی انرژی باعث افزایش قیمت نفت، سوخت، حمل‌ونقل و مواد غذایی شده و فشار تورمی را به اقتصاد جهانی منتقل کرده است. هم‌زمان، جنگ میان حوثی‌ها و عربستان نیز جریان صادرات نفت عربستان از مسیر دریای سرخ را با اختلال مواجه کرده است. مرشایمر می‌گوید ظرفیت عملی خط لوله عربستان به دریای سرخ پیش از حملات حدود ۴ میلیون بشکه در روز بود، اما پس از آسیب به ایستگاه‌های پمپاژ، جریان آن به حدود ۱.۶ میلیون بشکه در روز کاهش یافته است.
این وضعیت برای اروپا اهمیت ویژه‌ای دارد، زیرا هم‌زمان با کاهش عرضه نفت، بازار جهانی گازوییل نیز تحت فشار قرار گرفته است. روسیه صادرات گازوییل خود را محدود کرده و آمریکا نیز درباره محدود کردن صادرات گازوییل بحث می‌کند. از دید مرشایمر، تداوم این روند می‌تواند فشار قابل‌توجهی بر اقتصاد اروپا و اقتصاد جهانی وارد کند.
محدودیت گزینه‌های نظامی آمریکا
مرشایمر معتقد است آمریکا گزینه نظامی مؤثری برای دستیابی به پیروزی در ایران در اختیار ندارد. به گفته او، جنگ هوایی اولیه که از ۲۸ فوریه تا ۸ آوریل ادامه داشت نتوانست اهداف آمریکا را محقق کند و یکی از محدودیت‌های مهم واشنگتن، کاهش ذخایر تسلیحات پیشرفته و گران‌قیمت است. بنابراین، تهدید به حمله گسترده پس از انتخابات میان‌دوره‌ای لزوماً به معنای وجود یک راهبرد جدید برای پیروزی نیست.
همین محدودیت درباره حوثی‌ها نیز مطرح است. عربستان چند بار از ترامپ درخواست کمک کرده، اما آمریکا از ورود مجدد به جنگ با حوثی‌ها خودداری کرده است. استدلال اصلی این است که چنین جنگی می‌تواند منابع تسلیحاتی محدود آمریکا را مصرف کند، بدون آنکه تضمینی برای دستیابی به یک پیروزی پایدار وجود داشته باشد.
فشار اقتصادی و راهبرد تحریم‌ها
راهبرد اقتصادی آمریکا برای تحت فشار قرار دادن ایران نیز، از نگاه مرشایمر، با محدودیت روبه‌رو شده است. طرح وزیر خزانه‌داری آمریکا، اسکات بسنت، بر تشدید فشار اقتصادی و اعمال تحریم‌های ثانویه علیه کشورهایی استوار است که با ایران تجارت می‌کنند. اما چین، روسیه، ترکیه و امارات حاضر نیستند به‌طور کامل از تجارت با ایران خارج شوند. بنابراین، ایجاد یک محاصره اقتصادی کامل بسیار دشوار است.
چین در این میان نقش کلیدی دارد. طبق ادعاهای مطرح‌شده در مصاحبه مرشمایر، چین بخش بزرگی از نفت ایران را خریداری می‌کند و از طریق شبکه‌های تجاری و مالی به تهران کمک می‌کند فشار تحریم‌ها را دور بزند. همچنین ادعا شده است که چین در زمینه تجهیزات نظامی و ارتقای توان پهپادی و موشکی ایران نیز کمک‌هایی ارائه کرده است.
در نتیجه، فشار آمریکا علیه ایران صرفاً یک رویارویی دوجانبه نیست و به رقابت گسترده‌تری میان آمریکا، از یک سو، و ایران، چین و روسیه از سوی دیگر تبدیل شده است.
نفت و خطر تشدید بحران جهانی
یکی از نگرانی‌های اصلی، کاهش توان اقتصاد جهانی برای جذب شوک نفتی است. ذخایر استراتژیک نفت آمریکا در این مصاحبه حدود ۲۸۵ میلیون بشکه عنوان شده و کاهش بیشتر آن می‌تواند توان واشنگتن برای مقابله با شوک‌های بعدی را محدود کند. چین نیز که در آغاز جنگ واردات نفت خود را به‌شدت کاهش داده بود، اکنون دوباره واردات خود را افزایش داده است؛ بنابراین یکی از مکانیسم‌های اولیه برای کاهش فشار بازار نفت در حال ضعیف شدن است.
اگر صادرات عربستان نیز همچنان مختل شود، فشار بر بازار جهانی نفت می‌تواند بیشتر شود. در چنین شرایطی، اثرات جنگ دیگر محدود به ایران و آمریکا نخواهد بود و می‌تواند از طریق انرژی، تورم، زنجیره تأمین و هزینه حمل‌ونقل به اقتصادهای مختلف منتقل شود.
مرشایمر هشدار می‌دهد که در صورت ادامه جنگ، خطر رکود شدید جهانی افزایش می‌یابد؛ هرچند خودش تأکید می‌کند که نمی‌تواند با قطعیت پیش‌بینی کند بحران تا چه اندازه عمیق خواهد شد یا آیا به یک رکود جهانی بسیار طولانی منجر خواهد شد.
تغییر محاسبات کشورهای خلیج فارس
یکی از پیامدهای مهم جنگ می‌تواند تغییر محاسبات امنیتی کشورهای عربی خلیج فارس باشد. اگر این کشورها به این نتیجه برسند که آمریکا در شرایط بحرانی حاضر نیست مستقیماً از آنها دفاع کند، ممکن است به دنبال ترتیبات امنیتی مستقل‌تر بروند.
مرشایمر معتقد است عربستان و سایر کشورهای خلیج فارس ممکن است به سمت نوعی تفاهم با ایران حرکت کنند، زیرا اتکا به آمریکا، پاکستان یا ترکیه الزاماً نمی‌تواند یک چتر امنیتی پایدار ایجاد کند. در این چارچوب، کاهش تنش مستقیم میان ایران و کشورهای عربی می‌تواند به یکی از گزینه‌های مهم آینده تبدیل شود.
خطر مسابقه هسته‌ای منطقه‌ای
یکی از مهم‌ترین پیامدهای بلندمدت جنگ، از دید مرشایمر، افزایش انگیزه کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای است.
در این تحلیل، اگر ایران به این نتیجه برسد که سلاح هسته‌ای تنها راه تضمین بقای حکومت و جلوگیری از حملات آینده است، فشار برای حرکت در این مسیر افزایش می‌یابد. همین منطق می‌تواند عربستان را نیز به دنبال کردن یک گزینه هسته‌ای سوق دهد و در مرحله بعد کشورهای دیگری مانند ترکیه، مصر و عراق را نیز تحت تأثیر قرار دهد.
این مسئله یک تناقض مهم ایجاد می‌کند: جنگی که هدف یکی از طرف‌های آن جلوگیری از دستیابی ایران به توانمندی هسته‌ای بوده، ممکن است در صورت شکست مذاکرات، انگیزه ایران و حتی سایر کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای را افزایش دهد.
پیامدها برای اسرائیل
در این روایت، جنگ الزاماً به تحقق اهداف اسرائیل نیز منجر نشده است. یکی از نگرانی‌های اصلی اسرائیل، جلوگیری از دستیابی ایران به سلاح هسته‌ای بوده است؛ اما ادامه جنگ و فروپاشی مسیر مذاکرات هسته‌ای می‌تواند احتمال دستیابی ایران به چنین ظرفیتی را افزایش دهد.
هم‌زمان، توان موشکی و پهپادی ایران به‌عنوان یک تهدید مهم برای اسرائیل و کشورهای خلیج فارس مطرح شده است. همچنین جنگ نتوانسته پیوند ایران با گروه‌های متحد منطقه‌ای خود را از بین ببرد و حتی از دید مرشایمر ممکن است این پیوندها را تقویت کرده باشد.
جمع‌بندی
تصویر کلی ارائه‌شده در این مصاحبه، جنگ ایران را نبردی می‌داند که در آن مسئله اصلی دیگر صرفاً توان نظامی نیست؛ بلکه زمان، انرژی، اقتصاد، ذخایر تسلیحاتی، انسجام ائتلاف‌ها و تحمل سیاسی به عناصر اصلی قدرت تبدیل شده‌اند.
در این چارچوب، آمریکا با سه مشکل هم‌زمان مواجه است: دشواری دستیابی به پیروزی نظامی، محدودیت در ایجاد محاصره اقتصادی مؤثر و افزایش هزینه‌های جهانی جنگ. در مقابل، ایران می‌تواند از موقعیت جغرافیایی خود، به‌ویژه در ارتباط با هرمز، و از حمایت یا همکاری چین و روسیه برای افزایش قدرت چانه‌زنی خود استفاده کند.
اگر جنگ ادامه پیدا کند، مسئله فقط آینده ایران و آمریکا نخواهد بود. بازار جهانی انرژی، اقتصاد اروپا و آسیا، امنیت کشورهای خلیج فارس، روابط آمریکا با متحدانش و حتی آینده رژیم منع اشاعه هسته‌ای در خاورمیانه می‌تواند تحت تأثیر قرار گیرد.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21262" target="_blank">📅 08:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتجارت کشاورزی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiABgoJq5sfe3LcNvNIvvesNZFzaaEJZOS1AIjoSqw8xUrsTjXN1_Q3UeJ8P7I-aD0deX5nbD58DbDaXE9KrIxfSLaSmSP52-PubnX-0jyCHGOGo6hUUcOJo9YBF3vI9j04b1NTTeaz0AhOfOXEcK8QExXNQfFF8Bo24w2JQUvUNeiUOldM8kzEHZYYlXR5BWDzlkaucpJteXVIjPcUogphnJx49mzW_X5wFuo_e5x6ehOOZK8zgz7Awta4ohvK9VMCrimWfA3zaklOXBNOWDonm9WwLJGCeiXTgYZd7SlPs_WrgktBZxldtM4AZRvfJOiHA6XFsDlM950e1BCL3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغیه دولتی
به اطلاع کلیه بازرگانان محترم می رساند
دولت الزیدی تا پایان هفته آینده مهلت داده است تا کالاهای وارداتی جمهوری اسلامی ایران به بازار عراق انتقال یابند.
پس از انقضای این مهلت صرفاً دو گزینه در دسترس خواهد بود ۱-پرداخت مالیات مضاعف بر کالاهای مذکور
۲- منع كامل ورود کالاهای ایرانی به خاک عراق
⚠️
این تصمیم در راستای اجرای مفاد مشارکت جمهوری عراق در تحریمهای ایالات متحده آمریکا علیه جمهوری اسلامی ایران اتخاذ گردیده است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/21261" target="_blank">📅 08:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21260" target="_blank">📅 07:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پنتاگون مصدوم شدن ۸ تفنگدار دریایی آمریکا در حمله موشکی ایران را پنهان کرد
به گزارش NBC News به نقل از ۳ مقام آمریکایی، ۲ هفته پیش زمانی که یک موشک کروز ایرانی به شناوری که تفنگداران دریایی آمریکا در تنگه هرمز در آن مشغول به کار بودند اصابت کرد، ۸ تفنگدار دریایی مجروح شدند.
وزارت دفاع هیچ حمله‌ای در تاریخ ۱۴ سپتامبر علیه نیروهای آمریکایی در منطقه را فاش نکرده بود.
موشک کروز ضدکشتی ایران به شناور دریایی که تفنگداران دریایی در آن مستقر بودند اصابت کرد
🔴
تفنگداران دریایی — ۷ سرباز و ۱ افسر — دچار استنشاق دود و احتمالاً آسیب‌های تروماتیک مغزی شدند که علائم ضربه مغزی از جمله سردرد را شامل می‌شد. آن‌ها بخشی از یک تیم پیاده‌سازی گردانی بودند
مقامات از تعریف نوع کشتی خودداری کرده و آن را تنها یک «شناور دریایی» نامیدند
در حالی که ایالات متحده در حال خارج کردن دارایی‌های خود است و ذخایرش بیشتر تخلیه می‌شود، گزارش‌های مربوط به تلفات آمریکایی‌ها همچنان ظاهر می‌شوند — و همچنان کمتر از مقدار واقعی گزارش می‌گردند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21259" target="_blank">📅 07:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار دوباره نزدیک ۲۴۰</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21258" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار CBS:   مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد  مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21257" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار CBS:
مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد
مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21256" target="_blank">📅 22:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنیامین نتانیاهو دستور داده است که یک تیم بین‌وزارتی و مقامات حقوقی پرونده‌ای علیه رجب طیب اردوغان، رئیس‌جمهور ترکیه، در دادگاه کیفری بین‌المللی (ICC) آماده کنند.
پرونده پیشنهادی عمدتاً بر «رفتار ترکیه با جمعیت کرد خود» و ادعاها مبنی بر اینکه دولت اردوغان حماس را تأمین مالی کرده، تمرکز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21255" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21254" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی:  ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21253" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی:
ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21252" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا ایران با طرح ناکام‌مانده حمله به پایگاه هوایی در پایگاه نیروی هوایی سلطنتی فیرفورد (RAF Fairford) ارتباط دارد یا نه.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21251" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=gR0nNFXe-gpn4p0k-yXB8TambmpXuEM7Vhcy2BkBZ3q4zJMrnnXsQJwSxKZddO9ImkBQco0n5ZqkriXgraAVPT-O4nuBCBSMsW1nj7abm3YFf9PyRT8EgdTuPk8_HbMEBzctZ-Xp5DeCrPxG5IJrXSKw7jKPFu1AcT6j1zQjdHfRVonqwc1PMSALcPBnm6mj-6DTpUnOjMiRuVqJuFY-gMDX-bhWcYjCLjDq281Imsvzqd6uppl8cGcNhGEAEYCAWSbAxn5Hz_QBNl1pvYJdFYg2jx9mqOLmW4MM4g4dS2kBhLnalzxc6ps4_nKdoNe2FAYaGnyUhdHz4rdGxOCoJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=gR0nNFXe-gpn4p0k-yXB8TambmpXuEM7Vhcy2BkBZ3q4zJMrnnXsQJwSxKZddO9ImkBQco0n5ZqkriXgraAVPT-O4nuBCBSMsW1nj7abm3YFf9PyRT8EgdTuPk8_HbMEBzctZ-Xp5DeCrPxG5IJrXSKw7jKPFu1AcT6j1zQjdHfRVonqwc1PMSALcPBnm6mj-6DTpUnOjMiRuVqJuFY-gMDX-bhWcYjCLjDq281Imsvzqd6uppl8cGcNhGEAEYCAWSbAxn5Hz_QBNl1pvYJdFYg2jx9mqOLmW4MM4g4dS2kBhLnalzxc6ps4_nKdoNe2FAYaGnyUhdHz4rdGxOCoJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21250" target="_blank">📅 19:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfp7YhxJVy1x-raIUtcJykmUwxRrk7gPG4AR79959jjcG__rr8-zRRjS-W_1hSFuRUobttgEp8Dc1C5VDa3yMq95Zh0u5GGkrrb9LYKKFzoPEBA76PSA7HdvHUCS1USSZv2Y-fDfOroUawdfNBL3KU6OGxtcMasAhgG2_nxQWlf8DAW6c6_d5AKtXuBKIJL3kFzJZjchRgKUVjg_rT04P2vv2-FuOKHU7gUfFv6BoqORF0mocFmQ2k8qDL8Yxbo-4fWmlN423aIiFkg61OOKjBRiz9P3krS_qJuu6E6gIuHT91fLDzOr5ELJj0V-90x2ibmY4Ivr_VBLjP2Rmg4KXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21249" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21248" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حرف درستی است. به این پفیوزها گاز و برق ندهید دستکم خودمان اینقدر قطعی نداشته باشیم.
زیبنده ابرقدرت چهارم دنیا نیست.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21247" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1qL0-MlNP_6qFDwvMVxdoJlKKCc5cb5ucf0bjaSQlXd0ItYoS7nuW_M2Ljaea1E0ASDXHYh_u4CGX9KK6gqJ4ZyJfGNFjDebnow7xv2GbfmXpxWSHkIIrns4Yi46vD4iGoowaho0UxhZ9k0nMXBE70fhXA17-Ezcf52WOIVMjK0JFvB28ER_DtLSucbbkH7f-hP1X0TfuK4xij5oYltZp8sc-tKcH2SwaGMKd8Ot_l_eddyI4Kz2DsG2bfH5p4MLkZ4woqkEAMZNQfmlBCUOBOCvuTN8XeQd7ykWpNS7ASwQTRRR6q5yJddnywKwE1dPcp6fsm0z9VM5lwSzjmB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران امروز مدعی شد که یک پهپاد زیرآبی خودکار ساخت آمریکا به نام Remus 600 را در نزدیکی تنگه هرمز به دست آورده است. نام‌گذاری نظامی این وسیله توسط ارتش آمریکا، Mk 18 Mod 2 Kingfish است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21246" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب «پدر پولدار، پدر بی‌پول»، به دارندگان حساب‌های بازنشستگی هشدار داد که ممکن است فروپاشی‌ای در مقیاس سال ۱۹۲۹ در راه باشد، و بیش از یک سال بعد، این فروپاشی رخ نداده است.
کیوساکی در ژوئیه ۲۰۲۵ در ایکس نوشت: «آیا حساب 401(k) یا IRA دارید که پر از سهام است؟» او به وارن بافت (Warren Buffett)، رئیس برکشایر هاتاوی (Berkshire Hathaway)، و جیم راجرز (Jim Rogers)، هم‌بنیان‌گذار صندوق کوانتوم (Quantum Fund)، اشاره کرد و مدعی شد آن‌ها بیشتر یا همه سهام و اوراق قرضه خود را فروخته‌اند و پول نقد یا نقره نگه می‌دارند. او افزود: «اگر نمی‌دانید چرا بافت و راجرز سهام و اوراق قرضه‌شان را فروخته‌اند، ممکن است بخواهید علتش را بفهمید.»
او جایگاه خود را متفاوت توصیف کرد. کیوساکی نوشت: «من محکم روی طلا، نقره و بیت‌کوین می‌نشینم» و سپس افزود: «ممکن است در آستانه فروپاشی دیگری مانند ۱۹۲۹ و رکود بزرگ دیگری باشیم.» او همچنین هشدار داد که بدهی آمریکا از کنترل خارج شده است و این کشور فقط «تا مدت محدودی» می‌تواند به چاپ پول ادامه دهد.
البته این پیش‌بینی محقق نشده است. شاخص S&P 500 به صعود خود ادامه داده و در سال ۲۰۲۶ به بالاترین سطح تاریخی رسیده است، نه اینکه فرو بپاشد.
کیوساکی همچنان درباره سهام، صندوق‌های قابل معامله در بورس (ETF)، صندوق‌های سرمایه‌گذاری مشترک، حساب‌های 401(k) و IRA هشدار می‌دهد و در همان حال طلا، نقره و بیت‌کوین را تبلیغ می‌کند. استدلال اصلی او ثابت مانده است: سرمایه‌گذاران نباید صرفاً به این دلیل که دارایی‌های سنتی آشنا هستند، فرض کنند که امن‌اند.
تمایز مهم، میان آماده شدن برای یک رکود و تلاش برای زمان‌بندی دقیق وقوع آن است.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21245" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgKeadWezu8QpUZCLSQhkO1MXTUMtHUVlvJ_5M0X2NiBTzhdiUm0r2WGW_5jlloWRMcAPBjZi2BpYLhmyLKNJreJr2XxXBtsb-iYvrf8aW6rtRYP8WmrPtF4GVcj1IPpm6EgQnvuhccKTkO3c7n7j_sGRyC8O81zcHbbycIUshsC3A4BcVAup6ud0aS7rc2AfPQuTzMRMQfD4Gl2-e-h-9G4I5-Q10YE4QANxS4by4-SiOVqefafsKOsmOOyJmSLVl1E9reB4QCXx0CXKSX5L_DZ5B98wejvLtkdMJoRENMhZ-Vm1MgxfAL5awqKwRHKWwELqhYj1M5KOjwKGwdVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21244" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFZ4KmtTgzR2BnGkhLmb1tSz2iFl4me38MJHZa601tZmn2Qd96jNQ7oI5DtXR0rK9wzGjzP6RzE0twmkRMJB8H_c7a1HFci7k0pEcAMJnk2s_u9ygNNw7x_14qqNx5a5r4q7fyb2sV08eTBUUVDfOQ3m9WpcJ12pjZOeW68Ozt1d3bH6V8xJubwyUdX9YxeGbltKRhfnO2IzEU3Dn0uUFobgr5HYfu-VJMyhqgAV2qaSVUN9uBeHGXUwLICfa6ZHSHGAkzRp3os9qHjaIIczBrHhkK4hpSDuLLFyEjGMYugucPAdvuvme2c4wl3dhhjZ_9Wu3dSDQOVaJqBdwlfk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=DnrH0cMm-kqylOQHPNQSkDSbsb8MqEMlJ1salGt0Qs5dWeHuGR3t1f7SNoSIsWAz6yabyX80PGPv8HIVQM91XL2z7pEcsMIGCQ2u-i-gFaF4tDggiIscv_CU7lchnIgTuNm2dTXgyUQU30we_IRa1KrUotgilb8ztSP54V81ddvfwX-9bWtbJvyo2Ifb2G4hEzvR_1XKmJg0jNoFqO-NACuDEvcvd4Xf0tEaQovOPf6UEuoMuwpBv_T9ZP3S15pM6lexMBoyocCzXv_NlN-a_2GgouuL2H17LCnDvwZ0dfREgoHD14mMBBQGW4GG87yK0LnNmjthStijMUDJp1ts1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=DnrH0cMm-kqylOQHPNQSkDSbsb8MqEMlJ1salGt0Qs5dWeHuGR3t1f7SNoSIsWAz6yabyX80PGPv8HIVQM91XL2z7pEcsMIGCQ2u-i-gFaF4tDggiIscv_CU7lchnIgTuNm2dTXgyUQU30we_IRa1KrUotgilb8ztSP54V81ddvfwX-9bWtbJvyo2Ifb2G4hEzvR_1XKmJg0jNoFqO-NACuDEvcvd4Xf0tEaQovOPf6UEuoMuwpBv_T9ZP3S15pM6lexMBoyocCzXv_NlN-a_2GgouuL2H17LCnDvwZ0dfREgoHD14mMBBQGW4GG87yK0LnNmjthStijMUDJp1ts1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7jfPlpMQXwt_WGzVUKFrSIn2s6j1Al_fTIxwSSzVzRTjYw5dwW3JBsu1cFiT2_mwUpR5wj3odm5_NgAUkYWiVMwBZyhgYoqavE1Zj4S87yjC2YiXpSBZBPWo9bqIG1Z9-NQIJ9l-5EUoW9OHv0xGh81O-NcEi_Nz7ZD-JhSJni6Tv_hZgmyuR0oebBdsgpnzcocBD55IjzYj81GSHEIqPE6fZjB_1H_aoNGQ-4yKDtXPJ1MgYdySM-Ond3rt3rGbppyKB6s_3lkznHcQHLcCQKQ-48_133pdG6FkOyI5oyZxYJ7fu2bogFT7R8Cp4UoXsRg3GKYpb4I59osnqCi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pnN6p1tIUTimDm9j7iYjSHe1RIV4XqLBxRCEgeUljH6k_tLR5etqv5bllSwE8BXTWi1n3FwttYutE_1bWZ1C7ClDFUXspjgIOlrPovdoBiBwn-WOE0lZyMFQ1zhpv2urlJRa3G0kaRWtrS0-KuFyYMAp7mDpyPOPXzXJ3-GGZ2weKioEF45wywi50xfJP2u_42V8w3eeoD3XBiPBtzFH2EddSZXaOetDsKBQ0mtLMQAJTkJjNJMkKQgRF_d4swdeEcS6MwPJzVj8KbP79R7r-tDN8QgbCZzwzKWLNpXlU01LVu5fmY1Ef1dvBIVXxRCOK5W63nkOaOqvSECXe8jXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHOR38b7JiYcI6MBFS7p08TV96NTns7w-mtVIBRN6o6Xd_UpzGSMzDXMf8CKbnLyFuMs5QA99w-mU1EQDqpv3dzkYvqMtmFDEvdJ9POWoOn_Ech0CL6rvjGyZAHQJBeGUAOy9A7RvvRHGeY1JRfNnHcJz9IalyeG8ss4KnM4IeSX8kVnX1pFgX1fbYU-OiFL77oA928pMKjH1CRCta5kYs_aaoIUJ47nSiRdwu40ddkIib2R-xB5DP_oojXC8Y6aodWlSMGioTWH1DFPABmeCkk0yuhZ5q1UPMlSBifew5CXJXYLeSrTbmKY8KqgiKTv9AV1ckCfQ5qLAbW4GPUdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC15TEJg4u7m878ZcC0-gvVSvVmH9g5dPzbnC5JwPMrT8H9wiO5P9kUZmiRaF1yc5yZ0D6DtY4s2_-FqODdl3aZRibka7JdaOoWRDeX9exgshqPZz5-DLkZqKEupn3d36rSMvfp_xz3GiLdt7fIPHuACrkNCGuAFOWdigVWD4Hyqg8q61POvx2FhHy1vdTRJlp_VdowCstwLX2hqI4nRrBH2pILmebXSnNZTLJ5PzLYjXTVoLca2slljZWJ1GS6QHwqAP9ylD9ANO2xx3Yr4IUfNYtmykAD-5YDlOr4-sX5cfK9bhTlxVavw9Mv5-__psgui3S_zh9aaWJo4r9-owg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QljjTo4_L9f-qVeM0UE0zQtXkFYpAZ1_vI13T1frXFgf7KHisrXrPEwDAWqrQkp91qRiMSzuSZSrwkqQOvjgjMvlA8Jgb4HMLLNJuzcDMBtYyzLldMunEdxYxPfIt82-qLdF_T39EDPkKF6OeEYTTS_NQGs84GRJ2g2kzGj5iLhA_wl0b6nQWTc5jPTCAmrmSyB12wTW0Li7Q3lHfnS_gkCAMVERDPTpKh572mTtItawDk93NAfGHvgOJyN6Cg_0re_PU1wcKv2MJZjRN6fEUd_lyzhbwHv21mLonNRcrHkMn9Im497QVbIR6nfj9ONmT6N88gfvynKC-wSlKmqevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=TDLaoJOupCAXMcVywXlRU-TX3QSckDX9kGK52q8fbGLYkdxF0Dm0SrwM6TkN_R6X4JVJiTr_BWz2azfJou2aguPxNoOyNyG3v83TyVs_lm6lJJYX2DTGxAwVzn7D6iHnYTFgXyotAZoALTBp0hAHyw4RCAsWoR0Byseb4FDpIgVA-RsFYHrjYMeMMHvU2drQu23N18ElU3NvxhpTpYXOsHLx98zwp72nh05Pxrtyl2cjz-gSUSpgvXSLekxkAXSXh3VZpdc033m65KuEZDumVjd_4miRCbELk8jMtGG-FQJC40z45Icjtnk4lWKxL8QFSgwJVoDgeo-nMiyCrNMgfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=TDLaoJOupCAXMcVywXlRU-TX3QSckDX9kGK52q8fbGLYkdxF0Dm0SrwM6TkN_R6X4JVJiTr_BWz2azfJou2aguPxNoOyNyG3v83TyVs_lm6lJJYX2DTGxAwVzn7D6iHnYTFgXyotAZoALTBp0hAHyw4RCAsWoR0Byseb4FDpIgVA-RsFYHrjYMeMMHvU2drQu23N18ElU3NvxhpTpYXOsHLx98zwp72nh05Pxrtyl2cjz-gSUSpgvXSLekxkAXSXh3VZpdc033m65KuEZDumVjd_4miRCbELk8jMtGG-FQJC40z45Icjtnk4lWKxL8QFSgwJVoDgeo-nMiyCrNMgfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=LqgE1BxVVtqPzKZedDjjPexYucPtA0VFezGbQ6Zi179G2zMuOiO2UfMoy20-ILP1LNIMOE3LLYylPl4YapT3LXG6xPeHCnKhPnNAL4ITe_sxtUtuUJE4LiyS57YCOBDz9qAvEGjnqhiCFngJOFd_W6bxGE23KQ67ahn40wvZd5ll71yGYsHDflza3T7skra7EVfT2XRG11HKB75lF5EJ2ADjohWgfM60WU32UYbBAbfEvNsfm3G4jMyd-kEFWM4Q_d-JJyrvixdu9OSNAC0MPDUd-DAk8Qr8oPzJNyCHjTM4l41fM_mnd5ymZJ3EL2-_LEAbvVdDS5fFa6PC20esRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=LqgE1BxVVtqPzKZedDjjPexYucPtA0VFezGbQ6Zi179G2zMuOiO2UfMoy20-ILP1LNIMOE3LLYylPl4YapT3LXG6xPeHCnKhPnNAL4ITe_sxtUtuUJE4LiyS57YCOBDz9qAvEGjnqhiCFngJOFd_W6bxGE23KQ67ahn40wvZd5ll71yGYsHDflza3T7skra7EVfT2XRG11HKB75lF5EJ2ADjohWgfM60WU32UYbBAbfEvNsfm3G4jMyd-kEFWM4Q_d-JJyrvixdu9OSNAC0MPDUd-DAk8Qr8oPzJNyCHjTM4l41fM_mnd5ymZJ3EL2-_LEAbvVdDS5fFa6PC20esRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
