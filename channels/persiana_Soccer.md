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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 451K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFXpI3PnehZNluM1a2e4uzbkTi5V1zFerlHvK709BC1r4_zwnQNcGBburScgDr5YsG0dnrCleZVpZJ7-c_fPY9glp6MxO_p5F-wbenQLmylz8ez0RAwD_mldO8aC_9vK-rYm1CQXIKtRfZloq2M8E2qveozZUHXt0Q645D-TeK5VOrsWchCGQEikB8Jx6hUyBBGAyG7zr69I6Cu4_XiWMaTXNqifD2iB4z6HgeKptzbYv66fzWvIvsl9iWrZPlXCbqbA967Jb5VGoYqmENTlEeX2GBU-nP3E1Izmdm9Cz2XI2-q93viSWL-qmVqm9QIwcKa51DSKbBGAxAUbHSaznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZXEjtKUq5rGynQaxNOkHfaMrd-TSb8JK_2GDcF5WfaSXJwDmH0eV9VGD61hPpnnFmLwuNWaBedD7u9nwkTgzkQTKWrlHWiqj1i8kU5Anxzoeb8WkmF1DJl0oFw-4WFafr39Zmp4ZMXarExvXJvwBneT3U37IRXW2uQWDvsMkqsDygW6Ro0BFHJt6YSBAKK8HmtBnSQbbJLD5pkivbK2iYvv3daTDasG138n__A_43aVAIEnwzBgGng6bandabh7llTZBrKdphFqGOu4zp2wU07N20tmHAe3g3t2MCXltYzRN_SJf0d7zv7G306LtkKS_stZLb-zOM018ow7nybc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTzNKoNzgcZqmhN8wdV6dJNqBMxaU3kTRgf89QGK0T7wCb9rRTAcwN_ONhi7MI4cGS4katheCfWaukNv5F6PT-i474-oTR2cpNKO7OuksbH5TS92AzrsThivLxwdFTSoESmYXiN2wcNntnQie-NJM7nK0Ftcu4YOFaVbsIWqDOTN2sBP1fhWBawzUzA6Rx8mTCiU9KW0KxgjgeUO56YV9OW4Jc9qXqEM2Zfg1c-sgBtjV0ArkDYMYedqkoI1X9WC3VjJd1qhsBcW0dEzhs3ZpdTC-LHqL7MuXPTjsFmw9MrV1XByG99A9QmFFeeq_o4O6mIiVUnraKTHw338BZSVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAO0eZN1cOKbfUHAX7QCdNIuM5fhYd65JsgwrnsxyCIQjJOCdIqla7seiTO7XmJYQCikK0GpUlY2Y3AnHIqkJ8QKQ8xaHwKrmSjOmIC_GfOo5QMg8uS2DHCB4cLn4YFmU7WeHJ6dwEe1YgmgrpqTq17FZzmuAPx-6A6aJL96q3GConWXi9mLqD6mGRrGWtsT9V4doAd40wWmwga8BGpiGmYMFscjadk2zOup0i9i9POZncxlbC1YfEcNs9iEbK3YREGdk-fAdiIuEN9PIS-PYRp-ebWPXiiZmBplKHvJk5vJIKKHXzNS3WUAVQdEZUB2Ax2a8rlb6UnDMSTYEv7Fnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3X0l4ycQSFH3gxWsN8YKeheA0fISO-oqqiEnJGQyXXsYiQ4KPtpi7uL7Y6APb3DDgyS1q4KjRJVIUtj5ZHTVgmOnCwYutJo4Iq77FBwYc10Dh0Dz0BerOGdqAYYZA5J4j_0Wk6WSfZRaVCEnO3b3dPoEZ8bMvL5A_6uNwdy2YDZsvfole0AMLYnfjKnQHzQ37IDyDVrst7WHv9mc0DXPRzCuVRxsLfgrX_59bAvRvV9QLh5REfrmihocEVJTN1Kqmj4_k7zbTccNLSuyzSQ9y5-Ap_4hCa6loaxfFrLkchWsnMxe5yarGJghBRYffW1YbKQL2okO8PzjbE7zsoakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY4s1FZ3_DL3dEjaNvckO--jZZ_uv3smttXnZ_t-vwDZx8bVfKyfq-G0r8W4rxCIQpF1m1fqNLFIz47Bw7ijJCXAzjomCb86XmSU79Rjkqhdt8F4F1FLENLAvkz0fULBGMlk4x_0dtf9WT0YZfEtCzE0mlcIPOpn1KKU55XuROv3L9Pc5wF9DGI6Vw1f010Txud6uCJEvovgCiuMz9i-nHYPLXwLmP0siNpR41iDB8L8SX616hs8NmQOTmoIfmyXxUtNyTj0oQxWwArV4yQdVQjH_Vt_KNLhd0WE-fMzhe4sVualQBcN3PyOoIC_QLzHongqp-cCeJMBsiju0aYTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v48NcmOV3al35Vm7KMhVURsvAqzk4YTphuFi7bHZfgY9oQxztYkibkECt1myAkM1SawV5UlEkGE__wScROqzQhOcnAKkTdwamRwSovG0kqoOuTwngvt-e7tGXQsbDwaYY7JYsiDNsianB7FbhMDVyD1gtw8Blo0gWMQIAdMzKsyOodfSuXZxfZWx2Xyife2NcVTn5exlL-FFitXv7OVvs9Wqb7wL1llYYlaw79mcqUDS3OzQ6j0agbChBkVn-l2lpfhtCbR2odacA-yiR-svQFsWdKBrNf2mVKp2vz58mCUsuC6kaXB5NeB_ILuzoctzvAj4va09wMFgx5KJFGR26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZNO3-BuTv3-pjQ0pssGxBOCCa0M2k0gNcpQ_EB8Ps4NS9atIVooIp5wlTbPnIrjKpRpihTS7VuW8Yi30vo5-mzckntQw5MuQipcj3Odqb3SSRBmw3QyN_scFKzX-DJSOEEo5y3XVd0Nt0p8Kfot7n1Cl_d1QLX01hR4jsvwNrPuFezPDWtlQMRuqOC7m_Ev9VhZpso-EJqLc6pko5d0sPXlXmK0a9D6YYxAM1Os6--2gZLkxvDBaRCUz73Tb5IAIWcVZip9vTLITQnM7hKSRj4xMZOJusAWtPOd6x6M4IU5YQ4R3p9c4SwQMLwr3gPaCbFRTgBKK2syWoYx9sUX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-78Q2Ul-Kn0HRsEgaIK0ERarZFdei1xcCOEL8PsibSVtKc9iVicIIdzHvu6gslZNWaMH4Z5bqIf5_gAahNh_ahZzKru1vPA-17KNBMXq6Fx2Isy0eUFT0oy7yNeT96agtXvCdf4npdB09qgKO0NOnOTiSTyNDuicPCnGYhMAisxxjf5E6Ss2TKHbFv4BHfSz-tJF087Lo18QeYjsVe7jxiQwk--NRiDrS50sCumx6i-3JqeSEGuNH-6tsxu1A5zJEhLKz3Fq5xLfxpZgNi7H8HxQmXw9tdyfZY6qYC0tlSZsmLFs8NRmtOiiJVyuIGwlwR8Y_eUMnF0gln7jyfJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Demse5jCWndEOsVb43HmKULJOO_4lRBRB5OCjN8or8I0RyObftshrTtq8x2x-8cyrkMuiWRfShQY8VHLSTjB6n3FfELIPedabczuDXPNh7C1CqiP3sFIKU8stROTl0k5UoWshX0Zf-BeR9kTJk-MDp8pn4_FhAxYaon4CL8vdWFSBRFbVZaO8x1YE9O8CkX8VumXABuA0b0WUrZyZsLw08RMcmebP4V0CW-Vnb6rWKNJtf-1Ut2oDNOMkMgOjA8yzSAzB6C6WGf4sXhnJDDVcXT5ifnhVbs8ZcevlHZwzXK5SB271pUbmiKLWAPnICjbgjheYgwbfyvPEqbAbhordw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnZXvzzeYsBnW0hvNewarJLDiCpJxHTSC4feeUW4QRDtTV052YPCFGh5OIHhNDvdwA8hfLD96Hrc3pFzSUPlnrGVQD9KSRMyq1sCQez5Ue4Z4AEAj8UfdiCPvTlzYRPg5_xleFAOE93HRnxkRGMr0v5BwPGv5u5iFJKKWCOc_nip34wfuPU81vXI1SdeYTvQZSgOOfcxA99EGTLlBtNvEG-gEB8RREEkVg-epDyyZoCWccsFpaE7U1u0XSZrzudxkIVvrWTnDyYd2K9_uWCUd_0uSzji4BX_5wNbYSbufuy3cJSKoNuVi-YStKTdWj6yFgDjM_PzMO-i0H7o0OpjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDHlvjtomttDwL6eQijls0Wl3B_Di1PkkPLuMo75Zy24qEOLNDppOnpZXSyluq0WMci-7tEIbKTXHGxrsHqv7Tk76PZHh-VVwtKrxwDQz8QxYlHXOFjrGipk2m9ZIuNW8fH2pQ7o__Vftk0xyrwrFE4PDNCt_h0Sxo3q2OnxFNfBjBlVORU1-7FikZy9fey1xyGUnryzPuFV94_39gvZCe6uiwXhDLZqgLajiELt8TxVIijSUsZxTprcpRy1Cg7ALjk0kYy85grQ4ChxPcJ4VTbad-GyqoI9MTaJsemBskxTo5s9xU4CZKSE-EZ69cR5H5OPXLT7E-kPOFa8hmdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=lJNMpn54lnzgD0NRX-ag_6uTAtr0yWeH3lVa0c3l9kRGODZ8u1BA9_15DuKtmOI2JvSnwRlrmh9gMrA8vujes7VhEVmToLjvEKTic7R5j9hBGcGwiMgbPiwG_lzDVxcVIQ7fqMQZtmSLQQ9ZS2Z5T6XZot3jAW-Xzh5KMjFVEnmHVp-vuMNDGJf-6_6f02MhREtt3QClhzz1tqH_MlQtL4JvSIvHa6yiIRThtSGBkYAUNkg4Y5yohBENFHhxDzgRia5TikhLfu4V-O_3xkbd4SeTOthOB9qRIcLLTqu43Df8tQjue-_YGJ-mPUT7nrpXyyQPE70U8BFCuQ_o1BIrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=lJNMpn54lnzgD0NRX-ag_6uTAtr0yWeH3lVa0c3l9kRGODZ8u1BA9_15DuKtmOI2JvSnwRlrmh9gMrA8vujes7VhEVmToLjvEKTic7R5j9hBGcGwiMgbPiwG_lzDVxcVIQ7fqMQZtmSLQQ9ZS2Z5T6XZot3jAW-Xzh5KMjFVEnmHVp-vuMNDGJf-6_6f02MhREtt3QClhzz1tqH_MlQtL4JvSIvHa6yiIRThtSGBkYAUNkg4Y5yohBENFHhxDzgRia5TikhLfu4V-O_3xkbd4SeTOthOB9qRIcLLTqu43Df8tQjue-_YGJ-mPUT7nrpXyyQPE70U8BFCuQ_o1BIrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=uJATVYfJiYzubIvcifaHEGiEjNAdWm1LWe_AMtLB-93I8_EHPrIGQsgfK_vLoHJZ1q_PWjEBxuzGJv1mERmv6dzc8EP49gvL1TsRJ9St06tB6ptmJTc1Pa2ycJluTvm5KlbW990faMMx1UJRy4gnjM36uCW951xNTx4LakFKWKYwBG-oB7fmimuPpNoE0GaF26pKZ0Sm6DdUqeWnoARln6HhuGXQOcLxCvOV5RzpAWczNhZmbAXDpri0E9dZrnsY0pXZRM8ahzrhxv6XJ6gJXSfWoB5mJMhFE_oTxyZ50-FoNroZRfP7XpLiwByg407pOTZ0JzRIEu1x-Jl4dHUyaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=uJATVYfJiYzubIvcifaHEGiEjNAdWm1LWe_AMtLB-93I8_EHPrIGQsgfK_vLoHJZ1q_PWjEBxuzGJv1mERmv6dzc8EP49gvL1TsRJ9St06tB6ptmJTc1Pa2ycJluTvm5KlbW990faMMx1UJRy4gnjM36uCW951xNTx4LakFKWKYwBG-oB7fmimuPpNoE0GaF26pKZ0Sm6DdUqeWnoARln6HhuGXQOcLxCvOV5RzpAWczNhZmbAXDpri0E9dZrnsY0pXZRM8ahzrhxv6XJ6gJXSfWoB5mJMhFE_oTxyZ50-FoNroZRfP7XpLiwByg407pOTZ0JzRIEu1x-Jl4dHUyaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLTM7XsFCjS-nfUuWjAOjEx6z8s4M-uMnBR-ek_nOUeRj59X0n6eV-7s7Q6C2K_LopnrW2PXzzHyacOtoRO3gl0r8CZwA2wbtG0OEYK0cJfU8Mn8Q7W8D7tpF40CE9uyakta2BAoJbqC3G5VjSBtejbetbd4FQ28pyiW5sPSoWUAcQlPyHZZdF8NhTLwhRy1u02S4Y5NQZjnjkVq0x5G17bv4KnCLz4nRp5Gu7cjZxegylR42tvdhXdGOgnZ3bMuXeKQTpWbVbZ0WJSFOJw8alWquWOd1ymAh720zmXWC3RYDeWueURQcZF3KCdB-SW_qgLwXDZfTB6e7gIBKvnRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxyd5iSWyBniqe0luiGRYoEfShq3JNXjoYEHv4WlwCol0_yrguuJcUkbDTj9x3pszj2aBF_fW46_2C7FJU7sRoMin0ahIDkuM5_UhgLzcL5Krn0D7RtZxa37VOwxMxEvx4s86u9_QPgtuaTLstVQqNaHZDNYuD0oWVoO7LgRP5EHSm5WhSrJeGR2Vf_WN9S39ozQnp_id-N9uDehWCyYR3vNpVFPWGiHrEs3L5WLLPPfO7swDBK0fC8ZrU9vZ1-Gmo0FgjSZmnBRk24BRwAy94geSRw1a3ESVKsJJAwQXMw7Aq-bacwAxbJwBsDdHtOWBnnZssZDpLuZC0Oyr1PbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-jHzBcAGMfFe2GJsi1imo_YZycYf6SlMu-ypq1zti59UoQvSPHslq-NiAq5NCf8ZzIDmSq2dUVcciUEdfUw-ho-7kcnuUrFKuTGj_JbmfSqWRyoKK8SZy1b8YNPiR3t2x1lIcmuMpel7QlRjko2WToAlyZrhDZgbqilNopJ-V3VcnAiokdjQtD2DLw6d5jH57ZemmaEZcH51XQWfmPDC7c-eN54OBPct69eBS8coU2zhfKr5skIJWOg8MT1hq_uzK75jFFlXksLdfvRk3jPp_tO_YA0kvCxQDjFXPtenJ1JEcx_hKiz8lUFkEZ5KQPAfCxYpocFN4_z65EpCTgu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqriLFHajIRHfwoOfqnmDuI2GdvzQKaqejMctENwh1daG0Cf5fPO7ZuhN71ROBoMBTEdj-VsRhbItxgkvVScsfy2c6WR6kx7AZVSXeJr0fJ6WOZtIMJ3mJfljjEpF-Do6s1FtozzCsujQzJd08nLV4bQpMJzzDBWOeGkyMUfKlcpyrx-TSsgktOFCEamO-EvRMqbjkXQvEsYPFCOghpZazilSpKMTkKXpaypxBsI-ZQst_O0Kq0GxQPgd9q6_AlnDgM0omO5PZAp4A3ybG88Igtis030AjYROmW9uLep_iFrRZHBS7Z8AoCU_XpZfvjVTQvQljSrfP90DX9Dv3ioeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCBs5rkN8CTmcWkJjMIu9_HZ3v-0PZT9EmD3sqv4RrWK6GS7eq0PLBfjSUxhLUcSC4txe3wdJyqhocYcfuH_ZsWxAelPG7MRpMNnTOaiN5h6KYARK6SV6DIPMQH5ZMk_fOfog6QzzC2ZIl7XgQER78MYsMxIqVAvDMcBvG8G7coK6XRS5pMvD6Bvf95pD7B-4go9U6TaYzpNlFXlmLRUu9DeLXiaXf1wdqmeGUuvI-vJErWZHBnj3dQzTIpadWuK_08bJCofInO5aR0tmpPbdAVy7xKVx8xZWsQ3mZacrWXrY3lgWj8PyzCVI6bNXrNMa6_iRRMP2Qo9LUdnvlaTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjuqlK7DetvZpKR1A5e1wIT9awh_M7pRtiFoVYkoTggjcUTJtA8nIV09-Sih5lkMs-PEbwn1xO2b4yBlSpuBj5B1l51L2DWmbiZvDX53USM4dtFFxhA8tZHzMIddEO8j-8l2ogFHAvTVEL6I0qONN0_PCCTgiQy8-P-VeA6eh_lfbczEuk_TcA4F-6r6yaYaG3nWyPYeaJKNCXK_4O6UatLbGCbgOwRHRQ28dn8rb9irg22CKkY2hUtAF0axLGiVs1EybncvGZANDqqj16z-NIGyxBYcd21lIvlh6m7RvSfbDlI4TLYjLymlv997EE23NOZ7NaqAepPKgbsp0KLpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTffYSjIdZMBgC9KzfB6wehFLLFK7VUues_HSd2qgMuL79TAZq93deMJRrdyi--bKdIBXiUTc0WymZNqci5OZ3OtiepN2BhLroRQoaUH5igCu2CW1PUmGss-yQkm4CsLvSAgfhzrbmr9AN51eyMUD2uJOYUbkYWx_r-U0GIfeEX_u-VlW_pyPIHsRxn74Mo4K0CwB23wbPcdU7NfPkZ1CbB19-0jwM7eSk0Q0RuMZUjbdtFQb6ZRIX0HDlC_f6WJpvngpt04OCl-8fLCER8bZvP_7urRtU0CUy-NqplDd2Ad97MdwhTSVQxQshkYdfnGi0iCzfgmB6PsP_vXG6v2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzygQH4GgW6QiNJlvi4-okX7wvc2aRKrhaGNX-7YNfw1pS8lhczTO180gof9SXPqlYfdcK-KTeDb8TyvLLd0gfRuiVoXYA3p8EhZIUZU8KcoP7NzTMYl6z9xdAZfaqV_0OIr8DXkVp89mGD2goe2mkELjVjpCzsUt-04NMUEq9nmsdZz35uS3ZD5rt-3gu7BNKIAcPtX3eycLUdJqOleYE1oQ9Uj0E7aCjgY4hd_jdZYISSm_o-ZBDjhW0Yhy_lM6NYCc-m9ToVR7HBMc4qx1fuV7xrAp3mYdfX5NojYcf4hxFejcfPNvex7vzWgZnubSegHO9dFF7RxfYgOf2wc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGEe8bTcw0OhECXnIxlNt58bo9oMob15GHL25Q32M6nm7Mzfei9bslCK2xMmqqobRhTmpx0crlD8TxwaJ5BbjdMtD-VWaHHJYUDxtDVZ7irAYFxSq2HoJYqzHtUluBgJ6Pr8T9QTkYFZ263WRlFZ8P1BENPjV_0liSydIr1PCKUCeHkIjphEy4dW9PNj-FsHM6Z4BJPIYRw-O-zCW0RmQ6GozO6BQ06E7-np6TYLvfCKhXSqrRn6X3KtJC1hNRl5Nhzk4Wzrs0ORzBJsbgWARIT4cnoLeoH89lAuQxL1plq6oRWPLeIXWUxVjnZu9NsLqcQws_pik9kWSeUlJC4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXNjP0uhQ3RdTsmXsGtSQCODh5GdU5imEZ7cSjNOpbV14TUxVyAeHYcCp5lGNOojSx3kJEHQAmgMhB6p_oJpOuv3JZ2zs89yGtXxCTCseHMKsDSVaXxQzfMGBfGyr2DGLJ4YujFuOmWg7YO-sTj9AGwVlWP8yCbf6NibrtT-zduABIkYWFBp6esay9NuECNzwdlLaQ361piemOE6u4GYo28Yi4wBkx-TOgLmsuNntnF7yYW_4zPq_KgCMYAhUapEdbKTYURfUoIrOjxr8wj_qfKPXBIPos9jx_U-l7ZZg5K-p6P5Bbf2Djb5tdZ00nGZvnDviOT-ycoTy5E-TatI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la5b1-qvOLXmh9NrtIx9Nq_pI52klFrZCAkHfSIDdXLz9EcCqTuad__Bg9Lcbo9YuxgnnFNeI7TtPFoBkp4oEVoh_p2Ij2vG1oFVmSMOKR0AEl12fR4Bb-9sssa6yGuAYtJJaRNkbQ9XFGPNygyjXz2__jGhQ7mTwqCv48X0m5ZlhMl2MbCzojMHgv-5nucSfV1sfA_ynmgZsEAWx0nOSKdNrybJ135RYlxzNk5YlMSovcvLEHsXC4Myb9i5GtSzj5ZIjJYfNQFSQ6XHJaqd9TU4GbeWIHFUUk2LsrmvN_s8DW4JaBQWyJGLru7jOMRw2-bU46_bCc12_F2fCpNdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOMZC92PiEuLeIRGniHWCrYaZD9Wza2ZJdwcqCstV9me-ACmlnWAVRi7V6S3-h4OAu4cD15GmQp7qX3J2NiX84nOLDHUHVRXaHjj7D-HKdgOk3jN8yxQTzPMbe0ad4hI532fD933maezqjtwBTaW2LS7wi5i-z3fhAdV_q0buqjkgzCPXBAbgiOBSDh7hDJfwYF4m0RfjRgNkubHx8ckifaAQt8wjcN2LLWzSF8XC2f1pFq5g5htnVbsTms9o51V_Mfu7Oe3zBrxtAMBjXAE7IjZkt0gliM41526aFZGSsMniZM2K_qaFo1LWh2Dd8yub8P2jA9OfcnN7n8vkY6pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=GwrAZsIO0SfXKfPqA6w7Itoah2EhXDcbfDbCq3KlYEtESDJohb1fH9kRpHGkX-WHvYT7mh8IAqQHKggUzcWljWLy6z6dj4i5xuCVhHiU9eV8YO97xIfaeM8R0opBmPrXZHvRqaARxkMl97tj6rUzTlaVJjGeYt5AAR_1G7nFtHdeSh4ekZT4HB6YBLpGJpV2a4sz6ltbpB0fsib4M1mXyxnsn--lUhFxPpbnQNoueCOccgitiGLUYFXIn9ujlCbFUA-t0Asjl0qYdItvew7FXPzwIyGlEnaDkcPIjOtu5yqVaxHfOKVc7HOyyl5FlGXB9NdUN6Aoeu7bI0kvjzEnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=GwrAZsIO0SfXKfPqA6w7Itoah2EhXDcbfDbCq3KlYEtESDJohb1fH9kRpHGkX-WHvYT7mh8IAqQHKggUzcWljWLy6z6dj4i5xuCVhHiU9eV8YO97xIfaeM8R0opBmPrXZHvRqaARxkMl97tj6rUzTlaVJjGeYt5AAR_1G7nFtHdeSh4ekZT4HB6YBLpGJpV2a4sz6ltbpB0fsib4M1mXyxnsn--lUhFxPpbnQNoueCOccgitiGLUYFXIn9ujlCbFUA-t0Asjl0qYdItvew7FXPzwIyGlEnaDkcPIjOtu5yqVaxHfOKVc7HOyyl5FlGXB9NdUN6Aoeu7bI0kvjzEnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMv9_AdwwddkV5pEeTx_DqqZUeLlSsm_cuYplI2k3gLUJAgtPQfmFX7g289NH0n3xrLH-gsA48zdW4uU8Re4xCWb1egppWCP4ZxafVY1OCz7-NSh1GBE52esaDJRQnTwFHYzj6Rcd23nw0vBKxgbWQ8p_NO4F5cugrbrGZ-eHL07pI2RUvTxrj9LvMekBl7fgWv50MaYiN_B_grrRRHGbf58ImphtWcef4wskYrl0DiZNjd-oJKqlwoVFYhkfEONFyEitiCk-QFoJYsXc0clEANf1Zs9kFQRjghlBs3AAzTNfzdMwBPsiZEOGuqpllc89P4hKVE06XfhP2NhlChaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLMPc7vWx2r5sFZXVogu3pIrv3xfDVSeq53IgHij9ASr07pmyEV47n2YsrJq6AuClczR8V8XEy3JpPV8seKadyCWW0hrIceEtbYbYU4J-4r5Dic5S7Owwya2RC1yUcLzhtUEiDefJ1X7X9nmUPV6aJheq8E-PlbjMtRV24wXHqsLHeGBUq49om27-tIGHLrVM9KzwHTJr2iF51y-uKa8YXCaeeTKRx3GACLd0s1uvLaCu2ZXvk0cJj7UoqEYS_q-CleWgUnmV_pFFhLA-FZ7GC6Om7duw59FpwcITAzmnaxpFoMphr1zYjjcSzxUnu_jEvwD32iTZoALFCe1J7ftow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQc3lGnupxYEIU_SQhhwarFrzHhcsjX9gfTgmMbzbKCUS0yQZg1upBMzT8gABBGYD8PRT_1pSPYOyrV88pXzwfMTc9eALcFJDOSgBVhjTxNjkCa3D4MEYqnrzg-lQkKOGm-fBR9Wrh-mx2B_OG6VxmJesb4Ee5YZ9x87fnJ8XrlOvEnFLlo-sBfaYTMu-fWgmOJRvY4l4jmnm6Cg5tu-vpZb4VjrIIPnB7jS6EKHTeA1qfDfg_Z9yyghV_uW8idgIKiYRKz4WGwpT8F6fpg-v6UvdLQYN_Zlar4jjUKtlXqxLVN-d-iJdW0h15AJI_Y_VrInhxY4xD7d-UlkM7BCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMUDcp3OibnlOECSqHb5wwwHK_Jg8yI2nWZjrt4IYBtjfx6OBhTpmrjliE9N5np6mEmlSKi9MqFzMY7-wpxNo9dWSJ3ko2pQ98a_I56n0tnbpMP0EHircEfA7WA651Ra_cBoVipL5O70FPxmJtrN09WpySt4iLJkpeTDIMwXJylJ3LbSQHiSYklElEukH-fG4na5pgF9PtGcF3pmVV_CR3NLQ77lPX0o6XChs3ZdBk_SO3vOM2nkxYFEA4DUsIG5DFkyZQUm6ku1RmgFfKwlOyoKBHoXQ1mLtTdsW2QYCrlc-Y4_haOybXXJhbyVCg-w0AKaHobeFWl1Pqf3wep2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSBGGdsgujj_fuFkZRC501hUl4D83SX30tAXb0HCXsdU9Y8mvZtZlcXkhBzGHUPOtaHKUBskSb5G96k12cF3P-0DvUx1UDQ26qDx59_0z9jm58KEbORMjnGV9G8dNlBDO-sUBr519IcT3WMs6u5N-KFwXXd8ep3CQpQ5CR7lQMrPbpB4h48RqtULC7x_tA7ohi1Q7JYoR5IwN2yUmEt3K0RBb3mTePkWgpoVykQMGjapreO6Ughf0U0G_l99Ux1GSE5D3Ou1AXlvTh6RR4Aj4mbVN7xZpXWyKM9O44K8kHoxvfwBfcOWAN_L6_Wrm5oxDxfW4LWJJ8ctRGM44p8aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxjEPC9zddTMt0fcLV7vE5ZWaXsyd264zZudMPbA6QGLrpst_ZZpA2pxvhLx2UdI8M3e3WdioXaVjzLztevZfEu83T0MzMxdPEatrPK2xmBv1DO31CImIy8iWruszMVnJ40F3XkzVn55MJeNIz8zwT811A3yukRqoc3Nr16XtS2uT3UgwY6ufApLpAyOgO8y2y_AIZBORWat3Q12XRtQxy1qDci97DR0MbT4EgIjF5tjN0q9rzaqxNTBpZqjdIngO79OLGACaGR9bXh0w6uyUEhluGMF7WrlfVtSum6Y3Mw7wgbQiUAyB5Jb30ZAemix2NtA0N0uAPVgVC4Ng4LMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaEmdcIzzJcIfzvLuQMAQydxBK8sJ-DdU_yeOLYGXV5Go3nfURFFtEAsN6Ym4ThyxayfYIMYxhtNlVNWVyvO4Ge6fbXiVSNVhxomIFyNfsV8JqT3VgjQTz3O9ZbHeth_XigoavfUekDJffd5Swomj91hsW6ApCAruTpf3ZtS6ziEBj3OwTzMPsgH8QfkcqqPz7et7vJSE6eK_fY6DiBo65l_WmNlAofNycOfvh0k6XPI5oIsppb7wVdqHrDrWaozlFG6JXpRh3YGuTarf_x1Y4EAcW6on1CBGnP5WE_3UUnTLL-EBRc3g8Du_8GS-3fJLLeihfwYefuvVj-iG5uT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YswHQ75-zEUlaIcN8WIjmpJnQjWbPLH9XtV17zEHy6hS6qcQ0dWLw-fRlASQFfgfVGYfisJA7spB4dQ_xdHy4GYVTJsbuqL63X9bDIrIpIdB9cVBdDa3hg7oD5NksdoFSsrstwXXD4g3mdlGyDqjCV7JxhFvH6QQ5kahxqGr12S7FMXrA-KRCiRimHzC95en9q_NKidV0FSXz3DhQw9ODgwuViVmBd7qMc3U3fXaUYdh0ZmATWSAr7ldpgB_OQ1lDDANL4mHXw-A2b-QzuEQzUtr19Lob8te7PL8zDjsetq9tgr8en4h1FHI9lnpKJkvj8hp9ScvGXVtTrq3q2Q52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdkWUJxeKjCqgyvchHHdkIPKMyI-eM5Em-DC_UR6DKH_-JqjckVpzX7HeDnysIHJv8RddNzP3G6jxhWcyI8NhTSdQqgaF5xzqixEf37twyH4U2jJXbJ8wgP2whUGnqjd5FtK6DTn6RVd9-utlkV0nsj21bkGPIi5ainU4dPnqD_8oJHygJJLIqW1jxTFnaZoQVOVE-VhlSyQYrp31w8ZTtfuV4bd8ivaLruSZsxljgmK14RaGZ0-VUBaQ6LQP7KFM2ZECwKfcDeYAg6w-wWJVdbjf5HaNUHu1w5TTa-E1Wpzi9KH32m636uMAPp_BZbhDYBNXgDBIhppbzsTtYVPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djf9mjpfq17Trf-9b2jHIfHSeyqtOMzw5vvOqQuq3Fz1JIhlbEJ0VuU5kvNl7VWxX-tgx3-Mcu8aw9nIzgDmeMx0LVOFwUUmVAlJMZ7gnyWcIaojDQQW5BrQsIE5IeMhwW5LeVfA7M2WzYeRL-hIUh45vEO1_-Z6essll8gdrA1fYC5JWc8jnt082m8KElkVRWuPeRr-WyTENJ3ev6oYvTlVB1s-9zeGGQSMAA3E-IcF_dnUAORmSeZ57XJw0d9J2V0WQ8yavwnvRg97bZD-0fdJ9niXzraZjUgqlgZmwxLdoab0zckaqMb43FJgwTZlcBF6oe6SBkEKlYncjjZ11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVBIPgWwaHN921pvBulwIhNS_szBvgmsl3an3_EbQYc--d2VKfkQQIROV2BhCJO9e7QRqDe3qaoip3FwZiBhLqBgC60hfhsxWVbrAcLu1Y4Shn8E2DS-s0EC0RhgDqDxUvJCBRzhMzHt95HkpDbbN-u8d1kxRdGT41Y0K4PB8UKl8lPgbinZNHe4DgLCrznPipj8VgRJwhEJCP_725xh-SwXFp3zKcpfLp_8y-sbLWGQRHU0FhhLN2hxnE3s52f1zcOvr_wqr55uO-BvRr45dr3xgppWNOeNhdAr9_enqvHeHp-DQ3x8jh37I9IjyN9izpBmb71KYwYSZRo-VLx3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Avzkr1_Xrw_J_wCuFGjqSTM8_pK2lybMof3KWvM15ij3hoiKrMt4_7vlH5ax-N4OmsEwRpqQwLoCrbxR6v--TQw8u1sHiM6NXLqH-nAmXgOw8lzalM64Uqx334EVI2WQJ6Ao_u1v8pmmSCSEYBdjMQTKLyjV1UpZPT3LwZar0fLnZg3Yu3fU9g1iE0WtfZI-LBt3W-oPIU59Gv4LXZ19dXqplVwvs7cVXMEcG-F9lxuHhsi20Qud_geA1T-_rGgcJFm6Tqg7jPl8IRAQPIygPEDQI_TPSINMavqlm_HMt_Zi710dOvq0xrpjDcc4ZM-K4rd0_VuuzlVx8DZ9pvsq6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ryut8uOSY-lhRCf12mzC6gzr0YwEp7LrhLbpK_MFBYqeLhAFQ_7BBDeeJsxnHzrV1ipPKY2sBypN6b9nbHXETAyViT8kdyJ9iPjfKSpU7ylC1IEX-pPbyRmVeRUU3aX3KqvtyPiPXZtIKEw21HorxyR-G-6BW0W2aAsY1hTRD_Qpf9S2gjlt-lJqupQYcggYVwctfb2zAqlbch6qDyagAqgE82LitdETCcBzQyYHuEXrNMzbsvgW_iCxqaIE5WKKUmS3-TEBYsuoSKMaVZJ2X6y4CtqDtzAj8NTvcNad7ZsQX2CyRX2d46Hg97aTWcRuMQmfr2T4VOMqC4ApVPR3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=PcSQo4rqQfk6sgW7elgo4whJClg3bvskI0e8Nkmmw_B1UUojJzB5AVUcCxuk0OEaxpFeQUl2wPct-Ea0v5a3vzivIZrFdTcdCW9_70Mm_aysgBBPNfigLBRz_dpiN3soKpF6i_O5jn4r2N4ZiisGxAVMKCPm8BUGoD77EUdaYN5GLh_wUljOeiuxbCNp8Z7qPzG6WSqG32TNltyqoDIMxlmr17aGWvsoHxbtYrja2ZyHkt0BZYS_zYVJJZ19ODBW1smLgAkBalZqHF-f0XsWeooEpUYbT3Zt-vcU9ZI0yqxYv3b9pvxNJRVYptVqdJ2JGHKa0rVx6k3cmmDQ_M1UPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=PcSQo4rqQfk6sgW7elgo4whJClg3bvskI0e8Nkmmw_B1UUojJzB5AVUcCxuk0OEaxpFeQUl2wPct-Ea0v5a3vzivIZrFdTcdCW9_70Mm_aysgBBPNfigLBRz_dpiN3soKpF6i_O5jn4r2N4ZiisGxAVMKCPm8BUGoD77EUdaYN5GLh_wUljOeiuxbCNp8Z7qPzG6WSqG32TNltyqoDIMxlmr17aGWvsoHxbtYrja2ZyHkt0BZYS_zYVJJZ19ODBW1smLgAkBalZqHF-f0XsWeooEpUYbT3Zt-vcU9ZI0yqxYv3b9pvxNJRVYptVqdJ2JGHKa0rVx6k3cmmDQ_M1UPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPbmTqezNvudCvW_ZFbAa-6UnVhX4eZZeqYxRtJ9toL2_D5svcaGJx1rLm9jf6Vcc1MihheL2d79iNWBhJuHMwTDsksjj-rfgpLSQm8N2ivfMgbOCBuDxnNV3l-B7o5OLl013xpySPwGCxU8W-_AF0cYSd9--FfjTkalUI8LQnKzevpO6ClbglNWCyzb-XqBFVAUSEX-U1jY-GZrRrO9zjkpCU25jXvvXgWw2tMTvY9a5vGIJfOd0am-m4DJOPEVwECanxTJMehtnv97a_36ucoQbhFKnTNCruXz6koDqwyPQRlDk9ejaQBT3QtgxpF_WebfTnTEkUrB5DgKkQW3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckGRBR-0L9iIY9lRoxQwihpEFT4BWBjJ3KDIcTjAsGmDk4AEUZ-pGwY0tp1yOEq68wEPTLCsMMBrOsGW5TSlARU7byp8aBAhnTjZY1UzAubrPDDHPlVKS2EwgW-EF7qRNBdaWutUH22Bdlcm_Hg-wmDawpmNPmSSwFrf6tMI1mL2fFmj0M6ii8T0sxpNUjDAvZpsve2k19IbYLwoVIHTZCu0IvUsb2k8wTjeVMyJTwsI7vUnUZdNuMs2T4L0-O6LofpbacRjXHjkiRh-KXH4zuRXQPfvzkr_ayfh35uzGzKiVvunUTZuqPL7mQi0eErs7duOWzJ5pXUUhYFNPx_DnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL8IlLOlNajM3Y36aBzGpikugi5-D5XBGDtUSDCdBjkJqBpsugOzyP5LGJ_bCnCVgvSzldzf9Y-rYywpZwnUHDbSiKlt6Wns9nfuxco6JbIUvtOJXfZgNaAlj0RhEpNIYWk25QRRPUOm_csl40AiwL0IzxXnMY7WtOMcdWqJHj-KNt-6hi7HFTBqTgj9BAwGrvprBBFNYuwAHD4zKWqlfVuT0Q8rJTu2CfOkMyCr17A7EKDAC2jdW9xyOscZoofRz5o7liImTCVrBYFfnAKmM4d6QRNgjX-bBJV4DkRTD9_i2OHi7Z2WivajCjHTCJfb_FW5DQkmwJvTDFKAT5nuNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDnnk8dxx3TABCVDyrEXzS7d0J__ReEtRy3PCs8A70l87DpkdxluAzasmzuNcgDuM_LWPdRIjYMWo730eZtoGKwIyIdfXJclrs-19ljSobWI1itnnjX2ngp74pmu2Vgp1KDwGOJin8f1d7M5vECqiNs7AyTp2e8iCGRb4TFxMdQxg5nUoUvR45P5YPjbaAecOJ8hmnUe2D0fNlFbWYSOa-6Nq_2yRnXEch7BkWuEyvDtnfPkmXq4Y3huAMRQ3G8B_cr5ZR7Xo6VLMitz4c_-w38GnmuxErVo1u8OyG9fOW_NpWf1tB4NLAptrbws_eIUY-y0SNuXegsjeFC_EjoKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB-VOhVPC3FjI4hjQAdKzNny__B4YTqRsVWXtucElx-yBEY6Vn3cW-IV8srdX6S_jf8kclY0T0fox5FMCsOaktpqcw9xuEkYDpN7XeHCvl2B7HChKOpZtGSn64S1fcrA8ToT9ZKhbCOZHx2bNGNOcSOlg0J20HNHSGHajuZK0896kKa_6TWqf4bl02eKJNGvs930E5SaPeHA2jwqUfkvarvM7ev8Z6sPhfbZsGMesYu-jCKDAxwGIaViibXwcS7Kh37fGlmMFoXhTHZqg6yUTz2hba8py83fSlvpaLFOsS_qxPnZ-oMENl-4vLFMKcuTS5MK2Z8ZjCs18LL1agHlCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3YUxPAMgLGyYecKWObNA_dHFrouoXrBEXXMODJrYOyJnbQW_h2h04qRB8tttf4TGtifL0zZ0IJ42BQo9177kVqO0tBY6hlzSUSx7y3V75Zm4y6bIIsp0OVPkbeNStiYzJhQx1FE6M34ZBV4zAVBnMA2EWiOZPQKw6ibsOwKkIABSLNWu1kj9dyW_Pqrl_SVicjHmLDoYuugKMUt30oT8mCx8eislybzFvGtsjJ2GWK92kJjt_fp-H3FbYFG195kLMsSKBuX-WaW1jFYOG1oX6Ukz4dMzKjAh5Tys2r6W96T9FXahERCi7jXgPZYFHZ2JzaMie59fjWWWirYftVj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tek5w619s8dOCKxhQYa6DXgiIbCvWsj9hwVULxZX5UvWgKllhIvs08N4BeJ2154zeY7Hg_EV1tjZU7do2szaa0lbfvnuSfl9Epe_fdVFGg33ho_9unEs427ZX7Cw30zjKMd-RrloETG9OUmf4HIfdsiNdGjHlvEW60tk2UFylQFwZzbf3HwMfC4PfvMwe0qQx_IDK9S748Mbjyy4DxvdO8VMhVV2SBgMVlZ8l1bBI9YyBcemvkbcjHu9TpeqJ78_D7WDQx1ZhrvlWciYAXe9i_Bm73HUNnf0l2d2oSsSTf2DaxpfKIRD8v4p2vF0lBVKQSXs2UIRRXRPeaPxBDIQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvxQfsulHw8G6IE_17woquaHtYk-69CaDHfnTySj2nFS-cvIL6wq8L13saX1KoqzWOzIWsOvLwwvkP9enBqHhE0vp_nHcOV6Niud0cA2NcJTYAf4AbgutZ9VuUYQ1MIxIq9yjGzOaQlsPAHEiAG6RC2NjM0vgZT7EJrk3rOF2gkI4m046J_aAlQazV8y2e9WqR3Ec2T1PGPIPS21SDL8Q30jvjKLWzrL1AZxp5oTw5-aEOVH0L5zT3FzYMhJDbTVYzjjtO8MyoWBntidB4cTuM5R-Ul8iVDtvRrrJJnwJmf92jofZYEGu9WtHkcWuOICSrRagG6koYuE5WliPy6Wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfjyPrMK9R_pZbQnD1qGvmFxhwB9IvfyVTd2ZTnh02cDEIqqHPuju5vfPpk6eRcQkgGwIieL7wvsAg_vyrHG71WJ010OefqXoh9cXgCE0Bf0M2o_zelhDdA7H8MbmaENhNsgPCgQRMFza7d36V6wgfCkZa15gE9fKvJjWWLCAz0qnLpF5Blh8665yGTVhTWTkF3gNVWWMU9W4ChVctyb2XKnNmkQDh8MvdjTynLJlcFVDO2t_vAxwVKnj6mRw3e7dRA37dnQLyoeEAphas7EJe3GoottItPzXyvIEVH0TSDXCT1IhguVNHRHT2bF5Jbkn_ukxHaGiz0SHDFjPn_NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq1ez2_KTZyRWR8-9GMKowEju4bwoCnhX68jB-iGQZu1xDZHUkGg2nmptfPsAeD1MbobVWuG-PI4JY0clRKEiXzEyLYsxg1JAjNOdiv-x8RDgXEDCd7TBRFFQRc190LBQsPRFxMH0RTdXNrjS64Mscv7hBMGtZpJ74M0l4h_C0N2OC7rRsnBiCpsU6_rN4U9j8NOdnwVPPx4ZFLQuLRWJQdt4UE7c1MqKbrUA5SlP0wrss1L8EVsi6hhQ47i_EMR52gt8VQRJTnVs3L47aCX152waukPSZKngUFAbxTuff_LQAdfNhhfVrwLFre3qOxp9UAEejgDNhuXY6wyQQjKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWtGBaZJcd6VHtnoG9zT8CRyH_tqs8bY4L2ibxlweWHG6VErds6WD6s6h0WNP_GFARFB7APjKAccb3mHqIYtZiO0Cyvo53bWT3r5NByVR03CYXZrctfaOxyTLdCnCBiY7ntwhO5aUk7HlJTILL1mdlWatHfO_647nrZUxr5YeGnbVfNzWis09v_xFsGsETTUJ8RBi757bMR-1ghgzesvdALyydYBJnI4coe6ZrWFaxy2-hLU4hi3KhuJcp1cpm9G0Fnyq9LuxsSxZOoGGNolYWiaqj2PyvB141EnZ5arxvOm_eQakd0N1qJN0fMXsO59aleP-UvUsUDBBnev3o45wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب حداقل 15 میلیون داشته باشی
💵
اگه نمیدونی تواین‌روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 15 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
https://t.me/+HOIRMsG7xT4wMDM0</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25574" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=Imlx1hajGwvY7HAw4mg6Oy-LSnCUmdXMd7g1TMqLZD7DGUX4BgtejY4vyRdIAshjEG73wihrox6M5p-NXHMeef7ED7fU1yUsV_LmF_u0MdQhZSJhpIdyXIVqWI8ijoLXQwpBZ-LQV6Jnd7DnZ-pGg_rbOkYnLfmaGtqId0I90NF3aqGPhTNsQXmczw0kvTaz66R0hJ6mhbv_3OhJCVpnyCE56no-1q8iu_EUTPE-_2NYPktOlOg-qckb8Yro3CpvZ6LyEa2e-Pp9hCFA5DSbGiG1aUyOxY4z1VwxzDm6k1BvXfcglZ_c7kIGV4pJJX5r_E0Sj27x9hF9B_mBrZiq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=Imlx1hajGwvY7HAw4mg6Oy-LSnCUmdXMd7g1TMqLZD7DGUX4BgtejY4vyRdIAshjEG73wihrox6M5p-NXHMeef7ED7fU1yUsV_LmF_u0MdQhZSJhpIdyXIVqWI8ijoLXQwpBZ-LQV6Jnd7DnZ-pGg_rbOkYnLfmaGtqId0I90NF3aqGPhTNsQXmczw0kvTaz66R0hJ6mhbv_3OhJCVpnyCE56no-1q8iu_EUTPE-_2NYPktOlOg-qckb8Yro3CpvZ6LyEa2e-Pp9hCFA5DSbGiG1aUyOxY4z1VwxzDm6k1BvXfcglZ_c7kIGV4pJJX5r_E0Sj27x9hF9B_mBrZiq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTog8reJ-fBd2ywk2HDaakLIib3JJnZ5-MLUkXtbdq7P0UC18RBctYwaB6V1IfdwdcQPrD5rSYCkggSGA10F-M1KzrQkGHYVa6SlfVxqXMkiWEC5q2scQ3rb_FHkvfL1ptv0ws0826U7i1bv9J4R302k4lU84rTebXfnY_dM1qr1Rb936J1N-XoWRPi0kCohc6h3uAqAHXGedQjshUB-4mYYsKfdVT9-z6m5YjfTZhZXqIaPVJWWZxI1TkLwtbO3k_QMBB-Qa18UVrx9WIkXoGI7aEUOiEa-xqmqSMyp_ZMZA2IOP7vhgEdoWlE7-i5530IYL7TVgKxn2czIpmuk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD0RKi0c_Hne1dusaJ9CMRyRQf0n_y9FSxHCCZe70F67NkBWbKa4--MNlZzC8iVoETu0EaeXh2NE5sbUxD32m9edwjx7f-EJiVN28sRu_6NkqnXUW3_Rmkt7X97NYOrM3UL4zxQlJPv38ND3n2oVwKqOJjtu2pqzeWufy_0SecgPnshnOTdnpqLFQwnTqI2JTpysVj6Ez8TGgcAPJeHYLd0iZyZlKbDVQPp3wYKodh47gdBsjyTsHtBtvVQJWiWiNgTP0iNIEVlc70k6bVNaZ1otyqPrnJyomZLE9bYHa6WXMTcHCsPQ5uW2dF1W4hjXYxKuZhEq796O0VZErWhQnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RbUOGPLnKD5vV174ueVwoLWMoIWx8JDS6jwtE9FIZ-wuR0mnPP9aOpaoPmvP1BkdntRxS4XxRDQJ1EcHA1N9zkA2IBlTAnsv0laaNtSdpeXcRUcX5vidX_kBba9vW6K9xWOvfheHg4-Rp1CZoDuyTCeqoZ5NYdJMH7c9yvwzVaAhtM3gPr0oQtyBRUzgoiMj2kJIVT4UXfnV0H_1vhvn25g60G0Hg_GpVvWWS9qXxiDsNyVBUFK7yNDSK6s4bJ_daqQ5f0b26UbuFpbQrUC2M-cg6P7vLSQRHbwmcEwHaQaLROKaFArQiSJfPWoaWjzHigpGW25P3KgepQfn1FhKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RbUOGPLnKD5vV174ueVwoLWMoIWx8JDS6jwtE9FIZ-wuR0mnPP9aOpaoPmvP1BkdntRxS4XxRDQJ1EcHA1N9zkA2IBlTAnsv0laaNtSdpeXcRUcX5vidX_kBba9vW6K9xWOvfheHg4-Rp1CZoDuyTCeqoZ5NYdJMH7c9yvwzVaAhtM3gPr0oQtyBRUzgoiMj2kJIVT4UXfnV0H_1vhvn25g60G0Hg_GpVvWWS9qXxiDsNyVBUFK7yNDSK6s4bJ_daqQ5f0b26UbuFpbQrUC2M-cg6P7vLSQRHbwmcEwHaQaLROKaFArQiSJfPWoaWjzHigpGW25P3KgepQfn1FhKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0U8ZUlwXcFoNFrIyFqbXqoeE2WBXGYL9xP17Dzc-JU4BeUHgxP3EshYxDVA6znx5YxfyPvD1yiqHxAztOAvTcQjHXPzN-ASP5S-GavwTWw1L544lt7IfzZb2zy2HoFRUSLmXCfnHCxXGYnzQNLshLMFhIxMNPetHXqcc_JC1yxXsm0atOuaDj9X45C8c6jRlJ3JtL3WOLR3WWFZ-RPQ-o26jSTcOqPkrsyTvvERD4BzgKsmGZH5RcQ6bPnrLLGzVCUXWSat3WAuEjpJALwXV-_jlDSB1KzCXQPeXIo3b1oyaO3cIDGFGSPS3QBlV_2KYH07gZ67GxyF7X4dTTQn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NedJR2OiUW3SfeXUkxQOGYgOw_XRqKMaL11hmOPuGp2Ad7kz4kZYPQ3TniIrqOw_aVO_0MDK8hY6rVdJatnhIyWnpG4XhfattXSh7BRwdtpnvGBF5LcOwSAgEWhoxlAI8f9VtXvaW4fPG5-EKODqReG1FzlO5FPhkwlN9GhB6r53auTqu9v5t3WhPZ4eJevAuqFpomsxWVQA9vQG3l-hn8vznTMII2N5FJYL6LxWGnUuWTnGl2Hqt72U_k_mS5fcBmOnq0m6tsEZFb9N6S0TC9xdXFwLD2ptMtBrfTjRDlyZkogJfsX1f7zbQ7LTeV5-jrfL_J4N8pSsEWg5nkdNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bog5nTeZG7b52uD0vFEIxpPJk9mBPguK9sNrU6ExGyDeMSBb4OToeC0HJhdh4fLt_EKPVtHi04SycuP-FMmMRfMjYIAtiPAPjrZMM0EPDOdYxwrKKbNnghfCsf5MQOuQPunbVwE8W0hQJ9NOG5Ev4mb6QZHaTOzKDdgvblL0AkAEGoVOHJNnOFhabE8w8EGNtSc5jw0GeX-0D2QTOxHKqv4rk2bWBRBBqEaDnCiw9bXDvBj4V1sHWlJPc98J7Q0tDMilVLqxtv3a_qvlpTs9t8z8z4OGAGLytbgVJ2s9LQwDZs-VrU4bV6J_kXPz5hXmnbPE3s5xUszNSFPTo1ZEBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k97xgpDOCXoZQgPdQtIzo9-cDj11NarHkzrfkBxl2uxKewuxJPsGHR-Jhm39rEHbWwY8M7EXSac1Ib7c_zObafZQix0FjzIymePmFXT9lO1PQL1n3n9C-5jqMzuPAHJ9xgazKiaDXAE_HGRW1yR7nVswm4nK7T_YNz3uPJLDhXcJsmBckbOJNrIgWOTlO4B8UwBV18tp4GQjwdhbjws9MaYBdu6fkz_gC1P2qL-088VabBZNQbRFBiDbSrew3HMuZsfcF6yVJDDrWeAIgP32x1vr9TOhGV5LZoJulhnPQAR5JuNlkzVg_xnfJsMFivXzCIwCZ5CHHOuKC0oQprUwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=LHKRBOLB4D1aKidXkU75gXlEMrQgKyF1_rySNzbGTGxqvRNfKPLOxRdk1kVDTmjLo2kOhaLzlZayanFhW2AGK0ae0XAJPg_Qhgz7xtRZpq1c41iVI6LwBo-lgWJw52UMKozWxXs_smWWSil35dfKkjFe4qqGpJTpzccoEZaYFD_TxCZuj_EHVzHXyo-XUG-h7Twnx8P_dcNcnnEZ1LepLI4JGvOCJV9i9kEZe1zKaeb-9HxrYo7vTGS4L-lNccHFqd1BmmXkvYd8qed4gvIbDMu2WcPbNYNmkkKxDie0_Ov7gm9oixAzVeeWRuBvDTF2v8G1iI0eO3L8_QC2xxgHpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=LHKRBOLB4D1aKidXkU75gXlEMrQgKyF1_rySNzbGTGxqvRNfKPLOxRdk1kVDTmjLo2kOhaLzlZayanFhW2AGK0ae0XAJPg_Qhgz7xtRZpq1c41iVI6LwBo-lgWJw52UMKozWxXs_smWWSil35dfKkjFe4qqGpJTpzccoEZaYFD_TxCZuj_EHVzHXyo-XUG-h7Twnx8P_dcNcnnEZ1LepLI4JGvOCJV9i9kEZe1zKaeb-9HxrYo7vTGS4L-lNccHFqd1BmmXkvYd8qed4gvIbDMu2WcPbNYNmkkKxDie0_Ov7gm9oixAzVeeWRuBvDTF2v8G1iI0eO3L8_QC2xxgHpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=lpX9K0dCKbz38QHB8ldw2F94mPNNQnUVeCTsNzLSRaWnyXDtupADv1CMXpBzm3kin-gKKJShRJ8AiMr8Q-2ZJXK4c9hMRx9LTSgAM4n4ACn0iqzwCDu-Qz1beOnht4v9HqMMWjEiucZs1PdW_MncHf7CHYjQN3ssG4sY0ii4uDE5BDAn7k-H69cwWDNB0MFQLm9j-kulXFoEO0HMyMs67Y2ZBD-M0oniC4kPUcDfpL1-De4kqeDlEcJrZ-ncO8uPVin2Nf1I_YjYjw0F-xvJ7dJI5CgvpH2Yvfmn3coBa3cDbCB_fTCBp6sFJhYMZO3UijD4CHaseMkR060yUSBjmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=lpX9K0dCKbz38QHB8ldw2F94mPNNQnUVeCTsNzLSRaWnyXDtupADv1CMXpBzm3kin-gKKJShRJ8AiMr8Q-2ZJXK4c9hMRx9LTSgAM4n4ACn0iqzwCDu-Qz1beOnht4v9HqMMWjEiucZs1PdW_MncHf7CHYjQN3ssG4sY0ii4uDE5BDAn7k-H69cwWDNB0MFQLm9j-kulXFoEO0HMyMs67Y2ZBD-M0oniC4kPUcDfpL1-De4kqeDlEcJrZ-ncO8uPVin2Nf1I_YjYjw0F-xvJ7dJI5CgvpH2Yvfmn3coBa3cDbCB_fTCBp6sFJhYMZO3UijD4CHaseMkR060yUSBjmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=WHhEbVb8hqNGcms7q8ATfr1BrrE0k5xLb7TWhETewTAhuAsI2Ix4Wn3y4C_dIPTNmJo-_GNtryeLha2HmnlzG_eWfcqucOgA1FcDdeQpQVyi5Dsn3MrKLpnIwc2o-rMWsj4p0AJBOLgB8YqFDOIr2RKUP5FRxhGbXosHF__Ud2pdP_AGtPJ5dFG723qhGkODoZ94fwdfWbONLI36142PAwcEZWdr0uRwC5lEykb3CtPsnUdDJBaCd19GC5pkwwTzUTKhG26DdiDool1f9lJwRxcxC18XxztvQEUVqfv1iUd7A0m2sJboGWuZL2HGJwJtb7RYdt8Exbsrg8MZtsOWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=WHhEbVb8hqNGcms7q8ATfr1BrrE0k5xLb7TWhETewTAhuAsI2Ix4Wn3y4C_dIPTNmJo-_GNtryeLha2HmnlzG_eWfcqucOgA1FcDdeQpQVyi5Dsn3MrKLpnIwc2o-rMWsj4p0AJBOLgB8YqFDOIr2RKUP5FRxhGbXosHF__Ud2pdP_AGtPJ5dFG723qhGkODoZ94fwdfWbONLI36142PAwcEZWdr0uRwC5lEykb3CtPsnUdDJBaCd19GC5pkwwTzUTKhG26DdiDool1f9lJwRxcxC18XxztvQEUVqfv1iUd7A0m2sJboGWuZL2HGJwJtb7RYdt8Exbsrg8MZtsOWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhO4VioD0QxrZCovwXgWxmfHruX8Eh_xO7gtCDtZvjD8V3cF_1XlrNDWUfT8c2gUwepaRatZOH54vbhaI-5sA-egsp_9ZMBjTyK_JvH1MpqPnAjqc4FqZPSKAadMc5sLGbKbuH426FQeR268SjDlIljAcXqR13VGKEYKjOrMX9zG6PNbqsJXkABn_SoS8DzKVCNMoTifKoWiaRaNihhiM0_1m2z4Mv_JOdu6o2VjhqXY2e_a8iL3aZg_umM8hPqOa8FY9d_B0e8470XxhUR1OMX_v2fMq0t13ozZhNp_TCCrHqyJPW7NFsFYhfrz-fM2L5USg2URpbX2ZHXBPtknjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ3MbWXCDmE1ZrT_tcnKP7ykLOA4GGZGPkoLrPpCcYVbXXRR5_wMZiHHP_BnzjhZF1KOJD4Pkg8OiK7QIm3iG0LICE-QamNH5PkX-_O0vNLQ-7zhZcPKrPeqqxDO0Iifq8n2DzFNCBp5qtJNVGFLBh4-ODoWyFKPE733zyMeO-qnyROE2DJ7omEKfG25qFifVYmJKOez3I8ImfLYMOdChSpqY58Pwcr6YMYtkJEXfPz-FIarGvy-f7eLVASgXjlFezJ4Tc25rSS3cq6LymmF7muRs_NsgViDDNRoQxOH5PTx038KdT1JVA6txILWHVEX6U8bp9zjLVWcbDUaU6BjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V29ZjtMJRSd8W71YdxPzGmcRflBpV5W2kXj6OFVRb76ruKPpRYgCs6ORhZ0opkGnprYFgUAkyWkZV6cL1cMRdC41K0sBAOa5CwZpUgcM0-0UiJuvkSNWjh9Sli_qQRtU24khtue4vJPW9aaqZUq7b4LTYOaF7TcvebdGl0JJus1KgmNsO96mpF0xjK9Wia-rUXb65iPT4MqUqHb0rYIL_ZKon_MMLBibuALJNL3A6GJlergfRpwqc7nnLzXhBIn8HUdku9BaHPczC3uGmQsE0kIpQfEdgVGXDst1TF4Fo7dNWiFrTTwlNgsISwhfUrzM9SklKedhgmKZXnUrD1Iwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=LyEU3eA4ACQKVQiz1k4Yc2LM8bA1tpdkHqRPrUcv-dYBqRzJ0ybdjvK14X2imy_Gwpk49qHvKoaPR0Hi9mUJck2bSGoy8P_QuB5oXTYGAETpNDwCHC3yVDpm0vs1JPm8VWsR26T0gQbvsZ6A0sToeZ0_EllBZSe54wetFWp-BuXdv7soDJ_xMHQHFTgOi_4bPl1-s3H54dnHjee_Yoq0y8MEddpsU6SzVPKp5Ozb5r7uLbMFCsbfd132Gnc0R_asP85KVxURVFKg4Lb-MuDFoBBHlkXORMrMUrZFvZfFhiwDo6ZTRXVl4BJfLZv1iP5DM2UBq7EZRU3r2VBl042NWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=LyEU3eA4ACQKVQiz1k4Yc2LM8bA1tpdkHqRPrUcv-dYBqRzJ0ybdjvK14X2imy_Gwpk49qHvKoaPR0Hi9mUJck2bSGoy8P_QuB5oXTYGAETpNDwCHC3yVDpm0vs1JPm8VWsR26T0gQbvsZ6A0sToeZ0_EllBZSe54wetFWp-BuXdv7soDJ_xMHQHFTgOi_4bPl1-s3H54dnHjee_Yoq0y8MEddpsU6SzVPKp5Ozb5r7uLbMFCsbfd132Gnc0R_asP85KVxURVFKg4Lb-MuDFoBBHlkXORMrMUrZFvZfFhiwDo6ZTRXVl4BJfLZv1iP5DM2UBq7EZRU3r2VBl042NWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCUX6BjG3xmoI9-JJ0IJ9RFWt9Ptle15hMXyYAyLibE-fFtgrHk-WGp-m9YAlvywXC06ufLPur_xBVEBuqC7xSIGQ-8ENm-rHzZONiDMJVBLEWSBWUjiQcJQ7X5cLph6kqa9rQjWnb4Ot6QJMPekTqBB_CvygRGBHOB4Hu4O-czLLmwuL5b4Z9orADDCGf8WfgRCgWPWyEQXkcJD6T4pM6h4dElaMexvxLvPhiXqIw_tDQY03GT7q-My4elDjrvA8et4gp93VHLRthNoA4IKVMEd3nGDZZXzwKwe7JfiSC2qTCZQLDzo-y2eUBozoEk4gR5ZtWY7OXBCaLAWU-jGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyKW6zlG4bRUWwd-0mI4Wjt1M0n5WDJlb_3C-ZnqbBpFQiEhCLQnM7jD2rG2Hfrot05VVWQdJAMEkRWcIIZCh_hKHvgh3cFxW7guw9lCVVPU6oIf2ClM7mgLG1184kAssxBMd0KVBdCqlJh8Q_34I7QPS8m_lX0HaAGUQWpoJg_iYN7MRn6o6SC9kIOoSlJhaFMlISZndhJi1R0Icx-oLtSmqUkB0W-Gh67-9jDIDvQ_ISGZutsd5rKQSXxclFdwh4ugTkgzDBF6dupiWrI1jzWKtII1fDVvuzoG6yrlJ7tDspI1kG1FB45xR2fEUkZWWkHT6rsTl79Z8rmLPAPEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbopFCLOrAhVTfiRPmPEKgAz9mj2uyvm4oDWCcE6g2JPV9CqGH5XzeSukzXlsxmkMaQXVL913aofUfam149JEbZ_xWY2g10IK3utQpcJHnCIuNFiWxyV4pDInS380oJ0qDlNhena9oZ7T3fxHbdfh8UIbDDY01p49A_Y37BfA8IRzUUltrwVWfgXp45Qyp9yX5qwTgdXooQIOSYtd9_YGWmeDMjKZ6ZdLLndPn11KBXLE_gmrMxQ1-oe4FYttW63u_UHFRXGiLtP7Fz23kATCC4wy0pQ7PSfHM-2urrZmzXlb337PeYaRv1EiXjgRUU9Hd9WHlnDiZdaoNT7vHgrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkpnRBmjvqWrMKIuJODbx3-LQAQ1nI79E39KlMKLJlA5vM5S_pIcnfgnUnsycHRIAh-kcAuO3pRy6ZbcfFB9w7jFWHGsBL6ckqQQhejlzmZVkg6B2e0C3bYt8TuUqzE7fmkx7Vf60bmhgouJ-HvxDSsAOhTKqUV37egl2Ico4ndygaoKj-Vd8m7lx3cPjbWf1Md5balBIYGZl-0jlVGQEgRc4tMsMppp1C_eaqmxgr983ajVJHwQQt7zbIcuNpx6yejCM3sCZb_iyHFC14j-zOCE_kzz5e0eUqa0VVUM0rP1sfEZpdGTUeHcesnVZYXNZy7gbjGa3iE7Ybs346wJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O23HLF83Pd9xlGKrV3CioJhVss_7UHpxEjJ2_W8pUyFdX2Vz0_IeKnubXL5RY4mbYUqjcR7FltYfLFwI9ubdD0bsvW-ZdSmfCd6tCKFADT83aNzVVzRxAh9fLYm3kNx67cUg3UY9HYUjDAdntp64nfEAul0z2xQn8m4B066XhsHYW7jPEQuzuGUB9z_Ey7WxbAQDRTCyCmL7S3SHcR_NjLrYElVqyV-j8YGmqELrdlIfAPY0gAbzuDXvn-Rd9DExAYZO_qsFNH6Yhu3PijenPs1omvysGcRQVAjzLmdmYla5Da1kfF20stM4EaxQpCFVIYtnc331juy0F3i55r6eXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfzbfrM8quvM-svBYL4LGFTXqiPe4NV8M9FFCyXYVYiYUHXMwp5-k0_HxFSSJiyYq4mgUyL0ZBc1UgDKSrlwemMvpGLO7MfSaCOF1CvW1aeJxSY8YIHJr3_50ZOHnAvFmrgKVCVYwJ4_00wUMWXe5SWjuaVFz1Np-q2M71QEW-QHMmv4wlaI4PiKOK44kbSvJkj6d51-vzK5GcuEbRTImipmz8pveEnDc-cGBdPfIykHQaqgzPk4fb47DTlqL-ExTSk2JlDx0ou6b5aMQ-VhuP1n1_vYOnNaxcAH91AAF0aiDc7YB_H1SI-hKd2Ai__rPugBcmbVz2qTanAODocpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgZxnEfcIkRyN7BZ0mICyoR5diccB4SC0v9y3wXwMM10OMCLtPSub9ncRGXAPJSGdyVU_2VoAvTdB13QCY14C5bQPtKEcwXnmukcWVz0NZWRFlFeyg8hch9nkPgUegKhMq_athu_n2sbjRZf-vOuBUuw22ls1Nl0_PrnKzcdwLCtS7pqB1ZI0CsszO7gmV5BSWDC6A9mLQ3OaJo9G2sf6dOVJx_gy9Esvpl-FaIFzr40C3fpnd1FdDROhL-ZUwZA9vOO8wK7UuOdOBgkGVPgeW8UTJX_JbFp7VzLBuMasNFFYLONGZOnrFH8n6KKcDTpKDw4gVJx8_CSRb-7q0qu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhcTN8R94xOY_qzRpCG763YB7PtRUmCqC9Wj6CGl8h4wUAIC3wYbeEDfx1fDyGIVL2WgJ8lHn1OaihdvEuYlcYI_rXRipEHam1uT9ZPAr52IlzL3Gsw495kBTK-ZUuQC3Wtdo4x1CkMcgxTXxD-DfCw_ul0D71NTnIb_8G_RgZnWocZto1zUwsmDwRiDRxd_jWhU5JVt2edxkrfjRjKgEPu6DnlLQwZITyU5F9FX2tgImOxKTNak2jIujLzd1UbK3_wdvt987neZsxzekjLzjUBWjpvtVVOWZ-dmIYlhb32gl2ZXlg9dqsIDLlmQkRT2wNZ3Y92qBEQmRn2_xbFuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUoiijpVfao959CCFMXBXLCYpa_lgn6ABAkG4w0wbIj7mf7vK7JUmXDyxz3QD3quehyCRTjyPFPYL3fw07doF_8pGPaTXJ5mueRaVtN6FYDokNGK0HsFojbPvDHYqEJ_WmLVZLuI3dAnSZfC7p2p1GLaOK5dKRRtMw7rnBDyJ2NurGC4hpVnrMU_58f8r2EbVYPcHm81FgZQu5COjbFuIfbHMPldFsPnwYUZYb902uHbrcu-miJNqJ9I52lahoq-ZwTsRwNW4JDkEYqABlTDBzAwKvVPuglTfgm2PWQfv2qSkdB1h0vdFqYHvRepFJPcUub3IhrQ-EHDz6Bymk-oAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=E0bfLc-XfbkCpNvkf5GmJ1448DP7-rmqlH6jotOKFsb7Gh4TiV4Fbac_viQhztAbWa2owm2BztNzIspWT_fpL591P1z9M-EXZanMpfXV5OCHC7V3x6VKjmf2m83U22Am9E2gpYEMpfQFdp3gvydM6KQiSawFBjAjFaXWVW4z-2pbbWfx6oF2Dc2lsQSc0jOhlhlcDrC4nXEO1P_jfTNrLDnYCluveAvOBjS9A0t6YRKSEvIY8xP6BuiVHGioL3nmnjr4VuGZVqd_GJNy27uy3zLjKfs9F2QX_JAPnqtZDr82ifIj5ZS46vi4T4SqFxGyKpq2TAEIuQPf9Og-0Dga5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=E0bfLc-XfbkCpNvkf5GmJ1448DP7-rmqlH6jotOKFsb7Gh4TiV4Fbac_viQhztAbWa2owm2BztNzIspWT_fpL591P1z9M-EXZanMpfXV5OCHC7V3x6VKjmf2m83U22Am9E2gpYEMpfQFdp3gvydM6KQiSawFBjAjFaXWVW4z-2pbbWfx6oF2Dc2lsQSc0jOhlhlcDrC4nXEO1P_jfTNrLDnYCluveAvOBjS9A0t6YRKSEvIY8xP6BuiVHGioL3nmnjr4VuGZVqd_GJNy27uy3zLjKfs9F2QX_JAPnqtZDr82ifIj5ZS46vi4T4SqFxGyKpq2TAEIuQPf9Og-0Dga5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG7MrCieiQxuGiVbaxLrnX78TBQVTjA8bw_xoVDiBXcFsYcJDhhSCCo2iG90nrrN5iMn2_3jX8S6k8rbu-njO-nvhfp3oaeOAmXPaykjuUlFEQOfuj45anYRmyXwuRXENrJQPeaiIPZ6SVzXFQZXxSvtdh7u9gcWqmOHp4YZZ7OIY2YfSrFVMaevs9ycodZZiFgj84wJSkvrpIfcHp-cOIVV52eWg-FTWwSqYZmDqMBGjR0K1KcmN-EV6E8bvdQ6oqj4NjAq4r9Nlr5qGWYBtYEXS0ovuCTQECZnz-NOu6rXwAhmqYlwaA0CbLkcsvlgAGM8bwxtluTboqHf5Tjk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxvEElsthB-BD5hunQkcicXtXzmkFmPoEweBZj8NRdcZBcgbYsjaYZFuD9Efbu0eW5T74FZMsnI4dwJo0PXfiG12gHz-_UWBtd-Y_6TGauM-L9S5Bb_KflI57JUPaSNWzfyYJblu5toeuW7sx53Pb0VzNfLxMl8b5V6loON0D5TdQe2qicHdfcH30fiIL1KWStsVq_PaI4auYJzSubSK-v5DoGammsgXOKoWbxmzac9ZbCv7RqGDdB4wRboOfdg-kEDztSlC3N8cggGmUSzMZYcQiBKJ9eoj4XFUN6OanoWKcaPJOApwmC7H2IWP1Jx7HsvudJjveLXloMNDyUfQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=ekfp8mFDf0VTVQ1zDTJ58XRv7PqatfamH_Ix0QvaHpX5rr1ohA_b0-RTYEdTcZFuZ8OSiEWFVY8oxq-srr2uE47NYNkkSO40RWdCtK8Qa0xpJ0UafyFAlmympDR2om425ntp5k-xETBqWBsw3ZBkI9XH96bmm0lE3VctyqgO1fhDz0WDakLF36QbtNvATIQrzsFbLc6pqcMrU8nSQ87y9wSYd0bRLW5EDX25PVkmFRhD1fDSiZgqms-sna7kQ601mjqysbdtTblXLLpTjG7dGi1_1a7cLtobaamD46YM_Ws5hzq1uFa9W0ht72-YCfntAPrqx6YVXvCebR0JUml0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=ekfp8mFDf0VTVQ1zDTJ58XRv7PqatfamH_Ix0QvaHpX5rr1ohA_b0-RTYEdTcZFuZ8OSiEWFVY8oxq-srr2uE47NYNkkSO40RWdCtK8Qa0xpJ0UafyFAlmympDR2om425ntp5k-xETBqWBsw3ZBkI9XH96bmm0lE3VctyqgO1fhDz0WDakLF36QbtNvATIQrzsFbLc6pqcMrU8nSQ87y9wSYd0bRLW5EDX25PVkmFRhD1fDSiZgqms-sna7kQ601mjqysbdtTblXLLpTjG7dGi1_1a7cLtobaamD46YM_Ws5hzq1uFa9W0ht72-YCfntAPrqx6YVXvCebR0JUml0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNOFPK1zKV4FcLTmPvUOaWXWRP4VOHcw-aoRpK-iQAluYJ32nYvVP3HIqU-GXhTPWLvrTsz-Dipdnhfp3U7tynQp46Q5Uqd9W3bsQ4oxJsxThzFn448rw9ZG1ZMrcf0VQh5o8qxA2RqQwXUPOeFj5tbF5nt8wF3SK76VyewN6sQ1alkjI4JwFud8KqH4Xu_P7mXTsxRWtRszxr3_XMQdqI8ic9LnzO4Qh6nqnpCHTy5oFkx6FW5rEIFbvIU66umBYZiWQ37rqx7j7uVhyY7EqoQo_RulBAu9nqlvV92bayQxdH0zRZoBYZxCXsJgGSxEkzMDxzVHZ1ybyK-Podv6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0Tnaj7vTkDIjih9M55Ci__9VUubjCG1DhxihkQp-BhQn9qHZrCcv6x1rJuXCx_kTTjpLuEzz7BoAF-CGb3lSXv0J4RhKAg9GuwrDRNJtmSuahMRxekr5ZuQQYhKIWkyClI4WxevSvHTig-Srhw2sTQlAGTYhLiI_2ElBscqDLkT4mDcR8LCPMyTeUOa8YG1GzzSB93bObfVSZjR87Ki3HHSqTZkZrOk26Uz-So1P67dFCmAwLLCbHwcMdKzhBPd6-z0x3kdLNhAeWcBV6mdQZLdJl8bwSS87ltW8zg7KCA2__JYbphOtnmAIF80AI6_ZkQpR6dRdbqgWe4-Y9Zuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC0-SmegPkxMtJFTfVk8zCc09y6heNFWUno_jKYLRLcZo6P9JCMNk3MLWtgMC4hxgnfJTJr5zmOmsqehH6qT53Q6SM2kngcr_9Uhr6CwTLbjwv1nVNsqpygF0is_o_3NIlDR21EE70jGK9bj4hom9kXw4z32cBw-o5ty0Lm-MpP5NKauQ2zXEVcpRhsmvj6tbxLFTTeWLy1xp9seekJFg_GrNrFyXCs566DERxmSJ7KvHQS6Xg-gFSQtt3pUgCS1ruyTHGGXBrZj_5aTyXeSjarAfq85B7IUWpcCS2rQ3GJMYcy0HrGZAU0tZXnSQL2yB3pLzzoCG_ABfi4uhwBZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=rLtCZr9oDBWftiBa8u5CQbwv6X0OHqmZNWgnr1GI1Q8nR2L3GOzho-cVXgDl8kq7vVPE3Tk2lX7Ce38sXuQK38nLbYfKZUxFNCW_KQNKUFdUS2d4UxjRSh67mizz-6KMSvklPtPBd52NE1GRYUphR6H2djKFECVj-18O5-WqxXdXCdwrOTUL3U-dPaexOlOrhUaAuJgSyGW4x9JXdI5e5y6XzUyLok4Gvrb5JP4n420fDc5hFIdSxP6_BvTRnU4PK7-H_oSOsgrBYdsQfhLG0HRrSyzZwUBDp5UkGSOp6vsLpX4tIzxDJP-hX9jqY5dkedHeNAvyzppUwSd1Cexz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=rLtCZr9oDBWftiBa8u5CQbwv6X0OHqmZNWgnr1GI1Q8nR2L3GOzho-cVXgDl8kq7vVPE3Tk2lX7Ce38sXuQK38nLbYfKZUxFNCW_KQNKUFdUS2d4UxjRSh67mizz-6KMSvklPtPBd52NE1GRYUphR6H2djKFECVj-18O5-WqxXdXCdwrOTUL3U-dPaexOlOrhUaAuJgSyGW4x9JXdI5e5y6XzUyLok4Gvrb5JP4n420fDc5hFIdSxP6_BvTRnU4PK7-H_oSOsgrBYdsQfhLG0HRrSyzZwUBDp5UkGSOp6vsLpX4tIzxDJP-hX9jqY5dkedHeNAvyzppUwSd1Cexz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcNe5Ecs0HefEIaFiD2n7HGY8DbWJG-9DXSSV9Y-T1e5QGEJ3Ap_Sd7J5B7RfJgA770QAeJBp1tZzoMBweebp7t16uNoVi07iWDEzcv8ecKV2s8DCr5EvFr76eI-Ig5FLDjg0OXQ_pMEQo38f6IKP3kt90w7-zhUjrgAN9LxDF6fciUyxhZ3LR_T6HcQlQ8RYqHvBdNplg9OsQyOW6cSIU9Ehs5IT4U3hRgWBu1c5YZyZW520mzANFlshVlJu5zYMmyvyV60MKPNdQ8pyUgBIKJ0PWtyMBRZ-PvsPd09oClxdQe72vIQG_hn66LSk0JLqNRqasCYWGxQIhjiQdJq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Kw7FbwwLde92ijqaflCvwq-H1aClueno2Hxz8hg4m8y_lKxKgEm9RzlRUJu50S7EpPdWCAwcmpTGDPG2Df4dnER-v0sOf_QAmTxEAq40wDlQsiLMOQfxb2fM-pVYIYnfXz8Bj69VErguzI3b7VL6uiuOvo5ssbZUjP3pZM066DjMwRsT360B49Q8nLj1rICMPddiZ2L9g9N_m1e80sLcpBAzpR7UPnk77Z5QRNXGdZpYUBb9VtmHZcLH-BoycKLA32K1fniF6r7lXN-OgcbRnV1r588Agvpwpw9zQEmsD7tDsgRcJBzI7wc9pcD_7OIQQ6aAaQEWhkSvl1wtqzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF46Cchu29900GxeFqmFdi6hZv3q5gYMnT4pHi9HOgS4zSjpouGtHh4Zt9kTz-fEy1cQYkAb1X4AJ6QQzgDgIPrrRdkEnFy5VMRyHN3OC1yN9lUb3I6_JRqU4rGkZnPgD63GrJG4goyNnP2qGqJFu6oNhio7u7BQeDbFa5aKj3tiLB8izUQhpP9vzeXHjcefLRMFwquA7ddcLx0M-lFh-BLgY-0VHSlW36MPtFsBvGV4KtO1ZUW-t2JJBZ2LVDW1xCNRnn9NDSTQ60V-KCjc6QRazRvkaA7f-vEDbhNranE3rNfCWDLaIxur_C1g32x7N09WuRFm5zQxqpe88ijEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=K6G90V_pTfwyW6PY_XkuCuBAI8nnpjHkWLGu9n4zVO5KWeYcsWt3tGUkPUIXnoVrtHo72En482AxijBq4AI4IGsRxUUItP5AACBAC9NEqwdy-K2E3y4q-kuH8vHqs_foPKuVx1Df9wkz088TpMEHdKbaE9yaOUuiYfTrwbYeO6ryklpGY3b30_0IGB4r-hvPRmad7-U1OjJS2LT2b70rA5_MyNTe33xsHtedjqZ5RzsPR5Md9wd-C6_gPO4u2hptN6HPmOoMC1q65jBGwsQG0a1QBDZ1rkDOITHfBUaeMWi6xe45m-3_U1FCPKOpkh8OjOWEXiTXSC0krHgEx4CeRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=K6G90V_pTfwyW6PY_XkuCuBAI8nnpjHkWLGu9n4zVO5KWeYcsWt3tGUkPUIXnoVrtHo72En482AxijBq4AI4IGsRxUUItP5AACBAC9NEqwdy-K2E3y4q-kuH8vHqs_foPKuVx1Df9wkz088TpMEHdKbaE9yaOUuiYfTrwbYeO6ryklpGY3b30_0IGB4r-hvPRmad7-U1OjJS2LT2b70rA5_MyNTe33xsHtedjqZ5RzsPR5Md9wd-C6_gPO4u2hptN6HPmOoMC1q65jBGwsQG0a1QBDZ1rkDOITHfBUaeMWi6xe45m-3_U1FCPKOpkh8OjOWEXiTXSC0krHgEx4CeRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=Vl-zapv0F7DH_gbiOGprhRMNIrHzizJ0bYgkE-S0TTSYasDBkvjhL0PCgkYoTzy1x40RoPcCPNC2bbN4FxP06FJ1X1yI4h5noW6zvukYvaCOQ0oDeG3NrarV1b8FA7ZAC5kvOm_Mq6O45ixzA_GVoOJj8AL6y7dYD6bRHIrRPD3YqMvl9Y8mmTAhrIOUCash4dQim0NGyZkcTHMq3z46vPRsSeoHoM9RjPdw3G4UKx8V7oYsOE0hE8DfKFmUeWrUqM41nm8tjZn17fCc4MU6UPNfi3W6rb6tqeYCCZrKzfsmQdHRr3_V-i40NMpHzD2KVLxkoqtk4AmXj4RQuNku6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=Vl-zapv0F7DH_gbiOGprhRMNIrHzizJ0bYgkE-S0TTSYasDBkvjhL0PCgkYoTzy1x40RoPcCPNC2bbN4FxP06FJ1X1yI4h5noW6zvukYvaCOQ0oDeG3NrarV1b8FA7ZAC5kvOm_Mq6O45ixzA_GVoOJj8AL6y7dYD6bRHIrRPD3YqMvl9Y8mmTAhrIOUCash4dQim0NGyZkcTHMq3z46vPRsSeoHoM9RjPdw3G4UKx8V7oYsOE0hE8DfKFmUeWrUqM41nm8tjZn17fCc4MU6UPNfi3W6rb6tqeYCCZrKzfsmQdHRr3_V-i40NMpHzD2KVLxkoqtk4AmXj4RQuNku6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=HSitEP_Y-UxHz-hgp3-L9m7fTUOSM8pBYuP8KZodp5EY0JhEku4O-1rxRzT_TvjTHOUWHk-9o5AnEK1-ZYjbLHg4CUDL3Nd6ndcSgugZCLZ0mMI2eC_IInvZ05BzoENPoRxHL_PU0i8qZg9t3zCpBJvQux9ckMi9V5sXiKEBbr_Z61mPGct8h3hHuZsIGI-q4IqFsv-wrT9vWvJlZ-KNeJrdHg7rcBRWBSqFvoA9U8TxJJd03_3PoWbl5IUgxsIXmYRMAq-SuflY1B7RPYIDkTXL3nP_N770achPwM0W3NiH0RYkTYb8yzOaOf0afQxD6q1MsU17vBc1rWywTAZYgoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=HSitEP_Y-UxHz-hgp3-L9m7fTUOSM8pBYuP8KZodp5EY0JhEku4O-1rxRzT_TvjTHOUWHk-9o5AnEK1-ZYjbLHg4CUDL3Nd6ndcSgugZCLZ0mMI2eC_IInvZ05BzoENPoRxHL_PU0i8qZg9t3zCpBJvQux9ckMi9V5sXiKEBbr_Z61mPGct8h3hHuZsIGI-q4IqFsv-wrT9vWvJlZ-KNeJrdHg7rcBRWBSqFvoA9U8TxJJd03_3PoWbl5IUgxsIXmYRMAq-SuflY1B7RPYIDkTXL3nP_N770achPwM0W3NiH0RYkTYb8yzOaOf0afQxD6q1MsU17vBc1rWywTAZYgoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXaebLLN143D_SunAPBujwqr3-t9RDLxfGyQ_w4IhRyVEMOSYlq7H2NwGO84tbVoPvASdE_jKQAVhYuu60ykghuWUJiawh9ZVHbza9aU3LVveKrK2JT3dxati2j5VqXulQN78ZQTpcCHNj4zq0_2E9aEFobG4j5-hTHML-cTBsb-Qwwu2GtUZ4N9CnKQ1dlwtLFGhjhGtxlUnwLZhjLxOTmeOH7UWrEraVqGi8k28NkiErB6mO3kmrDOyIufHx3f848pdA50lBGheIW8CczMQYRknHlRMJ4IB1A2gt0wNMe4770DrxcRdg0ank9UQQyDIA3H3JOw0pXKCRnwdF4PNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfRJEDiYGmNx6jdi-uyL-ftZg3hvajLGhDFzJlJbhyccCf_pSOGTGjhdlaALU2egVWWujSkCJbHrPE8kTuOHC8Ghp1bzcnYSf741MTOiPTQ1tWc45bTsxdob7WG1Usj8wHJ0hMmQ9c69z8Nm28i_8LX20Buq0L_cXjL03heJ02DUQXK3ii-pgvImKtPdgzpWIGScjMpjKVQqq26s968qrI45EHf2A2nTjOCPahnLc-niUQ1EQI3t3H45zgaGRuojDn-UGmIXEHOMGjuBHndomP6B9-y6mQAiQf0xiBVR7YzFAFr31HF68bPFSHTl3LBb4jbkzbgKEvF5bSBe2pBRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjNx7csoKRCGJ6Ld6lrVSOay2HP2kxdQFwEEHGUDa4buaPbXDcm-rgNy5e3NJMQkrMu2lgYkOTn_YC1354gXqqhFAEWdml6jKk0lmAVPIbo35Xh1OLlB3SqdojtnbGOmK3Yy-HUMtDFEfYbm50Ph7ixYNO6lic_4B9nCEybsJj-JSyzCxvtf00qk2RaHy_EvoDGh16DwImfnkfmrmv-ECPmD41uvMRexCuZCLgVtC7akFIxb_NSwUxO5J5-UIxZKuTcdqzsBjn8oW5SmvgdCl31b5LyZiJTCWJyxSE4obM1br7US7kIzdE3kH7xV0MF0xtrrRSUnkwDHUJIctSYPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzTzvUy_cNPhnxQDSEN4A9wb9EVlO-Z5a6qYhYxZp81xy5Hq31nz-20YU92phgR2V-3Kgm7RVA-QQBcHAoQGoKBN9SAy5YBcHlGWwEEzABE0K8pJbDvyT6WZhDmEfGJfBnOA-ptymck3V-nKRxID0X_qTk1gdeyMQYjiuGnmGVXv8IiADB1_sfoERexhdWpZgoZkOr5ywWvSqUTgoSmpiwAy2deNViUubQbTIxrCmXjgTd2PJjMPKx6Z81iJmGWEjptG1iAE6HPeWVF2VBEsohgQ2jpmOqbhxC3fOgyXlvfwd8379zFU8gPaiEvEAc20wH68tY845b29eOCOnVe5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=IF9dBYX5H2DiWnAiQpQwIYIXUhozBC5pQ4PACKi3NjE_jInpR6wLe-V0tdR98OlirCM-O4otAQfcGUn996dftPmdmhLKnyrxPBY3Map0cqNpA01XM1wHKGT1YkyaRG1vNVWXloYdtgkxgbJx0zANXPcR9eKNZOwrsKkVa4Wr_xm8UNyKiIiaNoquJDJWHUMI28XMiQD8f-vCDODhkKJwVguNjdW6mCWnYEYFb_r8Op-kQoGqdVzXVNldLALeloCeV6pkPrYBOd7z6j8qobsUhGZgRaPv4mkAOOPDDbob3mTgolfQcHWQmU_65gvp6j7DJPh2M4qQJr4qeeIkk1ihkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=IF9dBYX5H2DiWnAiQpQwIYIXUhozBC5pQ4PACKi3NjE_jInpR6wLe-V0tdR98OlirCM-O4otAQfcGUn996dftPmdmhLKnyrxPBY3Map0cqNpA01XM1wHKGT1YkyaRG1vNVWXloYdtgkxgbJx0zANXPcR9eKNZOwrsKkVa4Wr_xm8UNyKiIiaNoquJDJWHUMI28XMiQD8f-vCDODhkKJwVguNjdW6mCWnYEYFb_r8Op-kQoGqdVzXVNldLALeloCeV6pkPrYBOd7z6j8qobsUhGZgRaPv4mkAOOPDDbob3mTgolfQcHWQmU_65gvp6j7DJPh2M4qQJr4qeeIkk1ihkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=DAA-US60rO4WwJDNW5UFUsNo1kbLwf2X5KUMUusYyfwxEwcZ2zKJEXRgIkrI4-v00qLf9_4tzSjhieUnoBAjR9GVpPS45eV4t20WIZSib37IT1g1Hexdgs3s8c_rFYX0trisbJV5MWuFLAvDL36TwOh8qssObXIIigKPAO8UQZyC3zIRfLzQ-RF8Q7EC-gOzzAa_QOxo4acZvPNduyhJaytmQWUyxcx5sCl_N5DJc9e1kUg1bAs5Q_Tufq9rlMeGZqTijXTwtkOgC3LLPoxzpOoiP17kEUMHNmi1el1WnU8uYvQ9QM6PtLGbH_z1fBldNWNEspoDlzlyWrJkYHJRyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=DAA-US60rO4WwJDNW5UFUsNo1kbLwf2X5KUMUusYyfwxEwcZ2zKJEXRgIkrI4-v00qLf9_4tzSjhieUnoBAjR9GVpPS45eV4t20WIZSib37IT1g1Hexdgs3s8c_rFYX0trisbJV5MWuFLAvDL36TwOh8qssObXIIigKPAO8UQZyC3zIRfLzQ-RF8Q7EC-gOzzAa_QOxo4acZvPNduyhJaytmQWUyxcx5sCl_N5DJc9e1kUg1bAs5Q_Tufq9rlMeGZqTijXTwtkOgC3LLPoxzpOoiP17kEUMHNmi1el1WnU8uYvQ9QM6PtLGbH_z1fBldNWNEspoDlzlyWrJkYHJRyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=MJcuhQ-vIhfbwqP3DToY05hzUrxE_Z1SxD9IvujWvilZUJA9C70CueTMYiWUmIU6x2-UAk17I055fWAVgQdq41tBOe9k50hvxY_uwIS-6AonJ8nbgU7dK0KQJsMtbxuGFe-OuxQANdVEH1ke9SCc3Qey-TIupvM19zQSmq56lDJv34teW7bI4EQqlNpZBP5ujAJYqWPz5dIjbZ4UMDjkS_FQNbsu7DJy1BJ-TGhJataFseipNWyfF7fLtvgGi3Ja-jvCNwfGCgp8n2ySlCgRjShg9j1GyVteJEMy3Fs-N5Xcp1A__vy5g5uCfTBALsTPlvZyJwQHK2bF0AoxHia8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=MJcuhQ-vIhfbwqP3DToY05hzUrxE_Z1SxD9IvujWvilZUJA9C70CueTMYiWUmIU6x2-UAk17I055fWAVgQdq41tBOe9k50hvxY_uwIS-6AonJ8nbgU7dK0KQJsMtbxuGFe-OuxQANdVEH1ke9SCc3Qey-TIupvM19zQSmq56lDJv34teW7bI4EQqlNpZBP5ujAJYqWPz5dIjbZ4UMDjkS_FQNbsu7DJy1BJ-TGhJataFseipNWyfF7fLtvgGi3Ja-jvCNwfGCgp8n2ySlCgRjShg9j1GyVteJEMy3Fs-N5Xcp1A__vy5g5uCfTBALsTPlvZyJwQHK2bF0AoxHia8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq00f9Y70DJ_zpRkoSqoSw3fGSrJ9n8XmVFGO90tQCfQscqH_S-9xZlDNrKGxOWwwVVrNakrVk5zZP4EdLkuk1V7gZq3cqNqHnpFNUxf-Shwbti-Of1eUmZVrZmWV0J5kuD6m0MUPkj4Q_GuZdvdtK3P49eXmHmKinjVnUYLO3vCq3Xt5LdGXIuf3TfeX--MF5L7-nDFaZs-F41jEi-mL20dyMDMQyjDnCVO1D0rg_6q9wcXe-ylZ3KdadYRmSFARrfgxkwJMWOf3UVzPEQWjyk7q-DXDfZyHfAVFgCeYfbnympbD9cgiYvm_sJq0KkIViui0zId3KcRR1Mq-aoKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MueuBJtvNrR_KaBWK-m0hlAPW1VEydYBlXouB-7Az4elh_5gEir8VNMf3b9R1jsbnd_gg7da2_J1gwfNe2RXIxFTYz3RJg4A0u-WipbZ-G4RTWFRUkoth102NrFfheYXCnX2c5Ploaq7Yvsq4ReTrJHX1PGg-o7F_E2VQEsqFw2HDhtJTAqwUhe7UbqCmbsELCVFr8nuzU7n2U7J9BQDDta0mEFv53a7VUrdWrGTJZ3u6f9Eh_U-H-wU8M4J5vVVO-yd6tYPmIAyc1vgTI51jOSSB9HsskdaCOdhkPs8NnBzCh3fBGM5uYLpgKjxcmkjpCQiiMRP4zCgr_mB2d913g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nibru0SZCcz11f9EqLa-r9JAcJeI1UkxFNPtgvSR4pjiJzi59X6izr_OztsgZdHhUwhDxyS8Kr4SLh2sSFOC8QBKj5ZFHfT-AUaQ9TR6Mbauy3z6VPgVKfA6-kxUdLLo8CYXMvBNXYA7sMrHKMoM1iUpxinp0wI0fBWGfaJbwnZtSmuHN4-Cf3A2CdmhBf93-EK0uQkGcr-AWE_qo6UHN1srko2vY-sNgaq0bMUXu_Jj5SwGKU8Cy3iFwg4yb8iJN70ao4z84qxpsSOB6zdiYoVdaPRm2iGYuZAORMVwuRfI_TKHB9pT68psQDTd2kLTOWbzljQqfydtnnOuF4GfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
