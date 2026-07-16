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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 514K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5pGA1QTNGWe_P60Eh59RtXzOOQVSlelDrjX-EmAoUiTMoLhRPT7OrA0rUF1x8PhhadoyfKh7DabzR-FS6AjUfJwghboMS0oIFxTva0QtZjRX7W43_WXeqZ3lZeqU23nzTQdMMQ50kuGtd4iT3LutISISThs8QP4Tdy2_4lg5lZXjhsjd5nljmRVmIXa7JFqQVutN-w-1cb32fbJc8ZJXJhnUK1ZzcC5qgOnYfo-r20OTFKjAdighcqP7sPX_9VdeLEWcD059Or3VU2p3ApHiAourVxcQPeqB8AQzls-TVbosW1SMXpueqxp-jNdHhz5SR8eI8YktlkZ7V7S_xvlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kS-OqDCwga4iA2I_evu88QFhdaIgNBBTLV5XnSKWT9OcDU_XryXe7gQCgsBETo4FYQV7Y3GvvP6U6lHoNTa3X6mvbuYH7igz34kWNb5q5GSg-Mr-92AtroKc79u3smVysQUbhCvC-yDXNMlZffhzIUX3FJ9QyJcDHQm9nm9plICOvEL-nZF6hqGU7BXdDFQOenIWcv9GKq8QSVsGIpVn8-lchyO94ohwPkqc_uRWFLNSeSnxWIHCH5bwZYFb5o2pkYBc65PI8sEaxWXhQA9sIXCNEEbiptvkVPh4IsV5kCXmGwanFKmYZyF7RZ85fFSY8DJVHcPMqrZ70OUE8rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpg0uvlB4SPhNvcn_FTjx3l6Q2wM9tjdi1DcgaUZ0ouPoS1HKhG5affL0mbqWrIjs4CUTB1fmlnxT5TK3M3mWNgQcwWh3ed14m5nhgYC7Z9mJoqAY3_wcUe5QZHQU_chx2hhDQc_AkvED24oe_T6e49BgQznyHEI4T4pt1gv6rkLKr5GBtjkOgNCVVcI2cZHX55_864Lp67zkEY6vccLpOKVBf8RQUeqc_GjhP-zD4v8_bDOKFURwHdvpxjotDF8HAcm6WdPGxQHueRpsG3Wypqc-Amuf-mz8y767I5cMjVPePm7gMogsDB9d-l6nesvGimtIEzk207cDl_weVfacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTkZcuUVIDXX-4BWkP7FHLxUD1qIhFrN0Y5mY5xZ2McE2C_EhLiEGaCTHzg7FdXuJlivYX4GtT49CSYYA5Q4COtj2vnhAYsr3r0tGjex5X7XLVnDeXEh8JJR3icqNIzSlUNSnifEW0xEnprf9YJqOu2A5HCweF2ZL9qpUAZmRnrPlWLAB9K7e_6jIsEG7rSPbXrZWeSNQ5cyYLUhYV1dYEnIDo5XMgIO5rJh2nb7thnuwkKDCFd5xDbAIpAljRaBShy_uqYglY2T06IJEsh9lv_8Po5R8UHQW34KWX8_9DE8WQxAAsIWBMbourh9VaHEqkJ7vQgnVtS0JGjUDGzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_JFtDeThjS6eBLbAF5D4dlklL4Jzug1pj7Cm2Eq3J1j-9HyY7vplR3TZzrfwbSLjJfCii1PMlqZ8XrqCB2xOJfqdJvAl2XOsk4UcBZzkLxK0C9OUtcI7-uaFIqWJUpSViULQlIxWBKvTdBdA5NvvxxUweCuho58B0Y65NUylibtoMNZ3gbXgdCk-6AY-9MX029AnMh0zzwT1PqKaHA8Z6d7rkotHV5BJJyq85HesgbzfUC2NZaB5XD0969hKliLsFwfMAyz93Jw15wkuW6gVe4S76sjeXio7OUW2XCR0bzzuyuc-pJX7V4nK6Me-kxjPHnJHUp_ACTR-SViiVMpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjFhuAenKQM89fzTmSfhmwjlFxnnUWDjiy35sgFHrh38DjSdqHRzzM1xmNQ8Y6NE8QJNnQfZ8x9VBViKhOauOdkX7CY0hdSwHf2huvgSzBRUCzjAtWtahyhccsQtzNYdL3thW1hSzG4nEw8Y-UW-PtGNku5L3iTimikbMZVx4oj2oWVjRQJbxeKi_q8AYeElinh6AkxRE832j8rjhOJOGhANfcJ6TPNvV5QD8FexoDVkVxUF6YCk0h0aT8Horz7vwpDh6wdYqk6IYWPaXJIKLiwg3u6T9SSI7BOQzru87yAFg-wz4VAKqNxoW10jy4WNBPJyJkaeDdYykm9yPLidUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPaibF1C3IoEkJUH-wRWYoluk_91G8ocvOFpNEQNQwbH_UoeV4sMr6BYeawcP5caaBZrs2Sh1WH0YLllxsLZhd8jyo2LZ_fFT5_qZSV0UB2JJjnPSK9M5hjmQd_RpJMDDIDzefUqS7juJcvnJH0u5QhA_-CZlULxDIi8z0lasvpBonwmkhFodN_CNYuAw1lYlZqwrGeOAGIQjwf0H399IOxnE6FDJhfPIlrFrPu376tZln4fzGwJqgUCUilVyMv2BHkmaNPvXYEDcbCAQQwPjQadaATdn-LXs9af7kIfqJd21PJu6UTnFHz15j2GAZ9F7vyF69s3kF3ttTJTlligVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoPlbqhFqECZq8hx09ERitieaXS7pSaNsoL_MLCGFBMfu1wlaI5AmT0DySCZQ1uTztSHpi5GkbOCvph4Xk664JG3Of__2iKd4KD8yQRpSkabOCwaIYu5_3bR2SvZ2i97afu8pweqDxOTtzrg8Bg4uEa3oRaCxViX55GTPH2DLdA1LaTZKDfxZww7L7STI1s7VV79MKa8_pg4qrhegzarw1Ysz_ERWKuF9JaLWOUO6MXelt4K0k4pwteovhfKQ2tI7-hFJ7JUnvVBXXBBFNFXGVD7v2OPzu4fqIZq-NMzwKUIW-OaV0PXK96G5kUtR7p5mlraxLW20uGBIBboNrRL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2MjEQTHVNucdUo0fM_-vOTYOutnugm0qdmMqdI4GVDylfNcs-MvpkaJwHEM2hVSInKqcX-Ow20mabh7pUK0ZpNT2vNqKnF7JZ-_ozf76kjwW3r6QU43vLqUqcl_J0m8TbSSLOgdkANXC4csKfynTXSGE4w2tkGjWZtHOUlWRdrdQy0EwgIoVmW-vGSLyhHjCE6i-1XdeT5xYZpzC2mAddMqjJI9NvIp_f0czhelpWO2iy2LLF1JPo5PhgGn1JKJ_oMSkmTd9cdPkpd7zBU9vcLq44Le09Beqaf8_WtD2NL3MTk-Ip8i057FOAtrt7htnXt27Qx2hLM9iQTG79i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXClf3SE5oPpS8Nf3kIu8tl2oG3cyNAnoZWngsvaoJu8tOsgGDgZw0BcgvMFboDWbDj9841y0waKxl9ZFtGarq000YtdI9JaRrAn0tvahFVczfxYO-m17mpDSacl3qeXlqN8zpecrm0AJq0FstzYpq4rqJxPjtqBvwgVW4eH2cZqFTBzBV0X_lZvTPdL1BqoLJGtwLt8PknJbrJBdb_QTcOyBXTJhNkWFxsvlli_-wBgEcf-JrUDasRZ5i6CI6T_forpCkRQUdH3Q6Mo-tWuHajDQwwOl0kyHKYCTsTUGg9iRFSB5khutU4gwjpwa6mERRY2OtPvKuN5rsK-EwiUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیش بینی مهم ترین مسابقات امروز والیبال در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
بونوس 100% بونوس اولین واریز
⚡️
بونوس 100% ورزشی یکشنبه‌ ها
⚡️
آپشن های متنوع با ضریب بالا
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25861" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bm-2gMgjfnEZ8SXV8OskO19KOPhjr5X72sYUGDI325cv51-Qb_BBT0Tme0IJtrLQRXicn3BneBKboRyDjjdLAFWA5J5FJzcOKNQP5Zn3dBfIMd75GCuWe9mQJtKQIWn_6yKwj6SXqA3NL7r7rAGnCILKhY__WspzbABYpipuwgpSfAK-pkY5IubsFZZIXSAuP1Ed8RwNiQoJzp9otgwjFPasT2Rrli9aocF3X8SBa4YHgXdWuzMMzpSzIDRLrnB-FBRAEwX6xb9TomMXlcAXsuAqh4e3Z0CMnLk6nKioz0Ry5K9qbY65jC1M61WCkDfBSBrkIfegPVTtFti4QEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLyYY9jpUt0IG1JhSmEO8iNm1ZytGtG7afvI8xFj2VlR9FMlGO9D3YOqrVgChsJX1XpO6yVyzY8F9oL4v9lqIutpwH89ENz-3zIcXiWy81FxzW-uFhoHlaD2B9VbyjvFjhhrzm09yOxfirNoyXS1DDMk-mGyYZ9MiJhtbulo2IJBPmVWhIXnpKt9xw9UwZUYs-USDVJxFmNuGUzxxomPt26DnMxGURSooZd3K5sAY2gQIEE6cgFQK3n7AVK3PH4DHTnIRLxX_qM51hyPEWb3MLYfGrielnfi7WtaFdIUILhjKKWit5LxJRO4ET2MsnCT-1o-T5PtBja897hript70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9hT6NWKkTiruRxQv-aUHKSCjcWMD7UdcDXdlIi2IQFSckuMJf9qyZQjHn4jjM8LTHnTap9MFqKyxwxBQK9YgeCOuZA-RR9JZDFLuje3eU0typ3crgu_WqbQYyV8wiGm7OHy1iFFubth5KtS6PU4IfUqtRKAbh2HEhyddoWaEaeub6hGtzuTndO8YZyDR3UvuR-UsjvwgwOgN1B3MFH20S5FYL0TvCRxg-xDAZgriMjf1n81fHxDzVfcfT1WtLtYjEOfvL4T94nUOaFYsLuPpuoRJfS5XnuoLwnowWnUNL3Hxey7oED6x_2dKrD6VwhNcy9ATEz2LrYtpLONB7N2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkAtoveEhhRVQV5kd06YMu8FcrHimQzz1lboRO6ksc-e1A3qBBkmi1d2N_ITaBwLgeEovP9f1AIiXYMukdVsT29FrZWtcbcqM49k__lRPN3BJv-ZhGULF2G_AkqmPVuduXY3qFtf55DnrqmU9ZhXt6gNWiO4py4P9MHPI-Qn6xgqXnlpyWjU-GM7CJ9rn5Ev85VcwejkOR-inJ9LIo5yNR0zlSAQbSwaI-r__Qy3x-1tdQrXTMdiV6R_39d_pxcgU7P07bvTI_ri12Rj0q_ucVVKhhWhORvB7PK_b9pZJ6wIVDlY49GzbOa6abeFPIIo3VjvyRpptrMM7jaIwr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjT1p6dZVHhKgCdYBLiC8VU_40q2Wg7ihPwT_cuiLU5LQ6b1mq8zfeqkL6oKr80IjyhhF0wQSSo8TCvQcL9CCbP_1Vte8KjYMnqzWy5Eq5hsNik9tYtoAV-S9hy1IoDw9kztAusjiIpK9VsGfoTjLiZ-uVRZ4a4l5Z9TN_fOrVf_XaAc2WWy9FaFZeHsUK6la-ZDXudgue4iLVgJZM-6-K2tvQlZRsWWnKa12_5OsaYLwEkekd4n2lPv9Mr1hfE4XpqcLGom1FiO6PzeRlyNbdMCRcjyITfxUIZT5wY4C7PIrhortk-gJ-ncyAgWemSnKWbm0kmwRCZ6RjN_6-0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeKQ0Ejvp0YIeLWK195OLoOUCH7D4Z5J-mOBzH9X6Zwl9M5j7pDCIS24e7sMADx_pJ5z1fj7Gyj0cPAg-gO-Rbh1DiYK9UY_ITJiUPqjOWorZ-rmVfQOIJVeUCFncBL7-S-UQFRXhpmHR-D4x3zpNYmOLgxi3g3IO8ibTs5gElc_TM3HYdoDBjbf005G1w5KcDCHPhDzdm5sxvRICbNW_-ofxqID3CMSB7EU7s1PRQp_BlOVc5fINRC0Gj08j3yxr1VuGiB1LH6bqlxasGwTv8kGStAvK0vX-zpFPZpcltlNKOACz1wRFvTMUfAtRixDsCtcD_y-5S7l6aCmvczoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlHEZ2BU8gHW554_9dxDtQRm80dMH1UXyQf39ZH_jwJ9Phy41HSOrnZhFru_HaUt2Ku_ckGA1Fncvm4g0jcZ-OKO7GNt7S_xQ6eKVaIee13JkpB6trA7MAFuCsHNMTJbQmA5FSM2MGoxwwoAaFygPQzQQcctcqbKsIoDN0q-ybVJoL2OOr2XW9MMI2fUYo9KTYnCouvp3Am_BEhn4MiKyCFtX91FKLowPaPKPY-DY16XMWbM0e_KiCT_FeT_4pHn0Vy9q86DTljNhVqMay9BTapd3w6jNCOl2h55z7V0jeWpoFDaNRJrIvFFAlmYG2GjiVWIsUAbz8wHANxbZ9kPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlk-YXMg9ShBP2Lk1wHaMutolpiaG5zX4ZRJA3pKntA4w_N_lU4ZssR9R_3G28g9ijc4Pn5zvso1GMvBNntFo81dpKht8jrtkMr2uskaVlg0ybbLViDUHk5AfXtYRyln98D3XKnXWvU-wRfa2aBXzqAY-zYy-hYlXYSa0PLX-y9p9IeHZ6Cye6rUCFHtbpmj09Sx0wUMyv628Kv1J4r4gs9XULuy2S9x8j_LgznHPsNgOl_DqbtuIhDWOZxLNdJxiUei5Cp3GQn4jyZHSJc_FAKnZPDCes9GRDVfQpWxOD7oOEhuX3lw3mBPPFqsxguzNJNHA7knhhAU1kr2RapD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwXUKj0HKfOEPHsNVwy6glA8BU2GVizua-XOaqVhInHvxVimWVSpYpa8pdRt7r0_c8Lpwl2IhnxCk63TOx4lQPGUrx1MYKdW-To93EuZ9jy5aQ88FGHoegjfm9ZIa2OFm3inGbm0DzRE_zTdFWneGB3i0HD8CfE7l4fiSuMYQXvMryd7DyxN1uy25OKUWbBkymtQzB83JOs-jLzASB7jeUSzI1mF5pFD-wv-s5p9uyKjabKeBq7ADxUiBdsRCgG1830DKY-EIH9SIFofqN6tPmUo6AL3eAGK5KO4cTRdoImSFPE4Gwg_8JaXrXhrp01QggwXnMlfojBcaNfNSRZ9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEcR0BSHJqTTO9Brj77H5SYCYctIfBcsqJ_NeWFNLKV15phO1-8LEeVu9708QdXnLyfJw6gIx-A7goAKThnKRt7w4AD7Xz7diwl7fD7x3x3NqlAfDp8-fQumQ1bHJ38-RVzFun5j07PCi4Llt6ZONFjeznnNNhfTwgiXTaS3WAgjEam362yigmRVVEcJpHey7LuCsSfWK-I5-LITr8gzv4G0L52gwfeoaNKcYrBmstbqcE64Iw13KxLvXLMKAbAt3fwWLHaGLpJ56_lIRpD1-6blNMY7ayHVAFFFo2q--KcW1u3TtQmX-bEIpgbFKRAifr6BjlRaVALvyTWKvTxi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BL_809yDcDoQ_Mta6CuGjx-rxdmCvuHCmNBIV1N6Rhm7r2MYfBwxZl7frM_LhTUIr1fMIAuTkYPRzP8JlTHyaAXbTpF8Mdb2ti2v_QP8HmEf5cwn1rgOqlpyrq1Mz1h4GEmpyu3uhT5n5twwTB65lldIkg9HA8kUu5WgiqaEPopgKvIbFMStutvv7bAE4zrgf9LcNfGj_NBxjfrdh0wRuWZBaEdeOXQaGRT47U84nWS8mgtr7qC4bemBvVZVybCg2aJuZ0Jro-hmisk7N6lCk6tcTx-rrONm1Ul2FixnrCtt2LaYP4R3lHovyJjDgtKB-6yz3-0c2QEeyqni0fk8Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxC-V6wQZHVHsCgCqNqk6sIrlHWSXMQ1aJky4iDNO1zdcYQqA78WnLkmbjYVm-4va-n4w_KiMHnHZh_N4u4kAyejTCUbKLxE5eTZTc4TQ6JoMybPK3cZZptFAbsXBKhH_fX90Slj0_DXayMOZ7bU7JpKkMR1dIJG36frUeZDDWJjZlPRgk0jJcBGocaVxb-iO_JExKsr2vVSKLCm7Af6-zlNo3qrUrMS01vAF8TuAzt97OOe0To-DBNP070mCR1iPN-6nRPX3ISsGeV6zjzyj-Ll7yA3ei517hsyQpVDduB-wMJ_VZBUBrpqXHdt_0YgLYa1pENCjKdQww-bOKrLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=pVMa9X8HJF5SFrV3Z4qYqRtx8NP_a1RO1D9LP_iMMjVHLSoI1t8DYAqCYlh9VmA29m_pAzyX9kxw5M6ApwI4V-ppD84980FPgOto-soceX8Lcv3s64HBCKzoPZ50Spt2yKa7PQX2R_Dfbu2NftEGIPAE0gPHp2C3t-zNph8GOU133GPZ7owzWOZ3FVYfP1SRuULvK0i3Ns_YT6I9UEUHqA1jQHXzPifLmk-kqLC22QuJj1BiCnQ2XAk5qMSCICAqYIyh0jde_1zr4sLQAgiuSj1itc_awVa-jz3VsGvpixZe8mN7AKe1p6R7HbSSREDBWYej3oz6Ozvcp9MRC79d2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=pVMa9X8HJF5SFrV3Z4qYqRtx8NP_a1RO1D9LP_iMMjVHLSoI1t8DYAqCYlh9VmA29m_pAzyX9kxw5M6ApwI4V-ppD84980FPgOto-soceX8Lcv3s64HBCKzoPZ50Spt2yKa7PQX2R_Dfbu2NftEGIPAE0gPHp2C3t-zNph8GOU133GPZ7owzWOZ3FVYfP1SRuULvK0i3Ns_YT6I9UEUHqA1jQHXzPifLmk-kqLC22QuJj1BiCnQ2XAk5qMSCICAqYIyh0jde_1zr4sLQAgiuSj1itc_awVa-jz3VsGvpixZe8mN7AKe1p6R7HbSSREDBWYej3oz6Ozvcp9MRC79d2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8jGNOjbF0cmVxwQj7V64xJ_Ki2-OZqwICJVdLTJdAsB6wDe8427gnwFRbD9KHi5j0NezsfOUh1M5M-8E-1wmuBKIh3EwET-oqmcEeOoXP2PBrwxS-gQZ3_4NSEj3Pqmh2cUy7mTILjSY9Pvjb7MU_6PMwGV9HP6Y63BmdCUL5BJxy2CPpXGneDBo11RXI4MkiIy9RcSz0MJSSMK2swpsEls2uUwPO-2ijblB3s_WQlCwCwti9f1QDaxt8r4XbIa4HagIysaOzeISp0ZSPx1LsYhul6bgxq-IhaQXbMTMp5anwDZigSFbgzC9wRIBsbfcFe7wO7XJE6QY4YJyLT8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBGGaOoFUmfAP1Qlb5NRUW28hUxfskW8CUWlcvE9-4tEltANQdNSqfwx6TftFRJDCdkxb9RpNhY39uxctVwPWZcD3ASej4kiCCpfZJ9WbUwERitmoOE-vP1Z7NwPGAVTamEtbjYcSX2dSBS9CTCpl4zPRJqQm-VdeLufLHvHTciy00DoGefb-Eh50u-YBKCV42woE6bCfnsesy3oh90xdkJ7gqVoWzkG0Gq5zm3Uiqz-AKbNQJk8W0_yM6QYRcHM2zOYt6WTfuCYf0PiOP19oY3Zc8Tizc-ZKlRocXIkbw5dO6y9ALnH1EHf1lAr3NvOr0zkTaolSxyH0mT_u3myFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=PSEQ9l9oim-7tjvWNIN3gfifIeLXfKTKU_1m7AKLvylLoLx44A1a8hYOH8vLgWaAYkKBFHnZz4t_Y3Acctv6yxlP1p4JYaB5YQVln_fUlJsQQMUkDWOgd0i-XLqUXz5Bl7E6K3KySaSmdz4sVAgoJZaKs6qHtJFxm3JUjUrj-Sxa7DX8reIUVnruuRS3Jox-8tRBG6A2iaiZ0rah2ozi8PuSK1cPhI97XPExIz3h5ZWELiSOuCZ8GPYoodo2KtDR1Dm2TbNGy4RA9sIk6GoNfZ1pfFMPa2eIfUk-iTVfCIzZr7u7U8Yyl2LdEXC_QjpAI_R97yK6ZVMYSVj_9c4ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=PSEQ9l9oim-7tjvWNIN3gfifIeLXfKTKU_1m7AKLvylLoLx44A1a8hYOH8vLgWaAYkKBFHnZz4t_Y3Acctv6yxlP1p4JYaB5YQVln_fUlJsQQMUkDWOgd0i-XLqUXz5Bl7E6K3KySaSmdz4sVAgoJZaKs6qHtJFxm3JUjUrj-Sxa7DX8reIUVnruuRS3Jox-8tRBG6A2iaiZ0rah2ozi8PuSK1cPhI97XPExIz3h5ZWELiSOuCZ8GPYoodo2KtDR1Dm2TbNGy4RA9sIk6GoNfZ1pfFMPa2eIfUk-iTVfCIzZr7u7U8Yyl2LdEXC_QjpAI_R97yK6ZVMYSVj_9c4ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPFQHWnM5ITh-5_vcmA1ArzxHDb865qhRLH21XYG73zAZhOdB_B2k3xJkW5TxiJzdcoqz860KVtgfPDnxtsrwl0iT6XC3YH5CBD2J-jWFAJxZiSLosO124SvwXxbsPKC1463xS0DdVR08WCTxvFg57oH_jI_QwhRlzOwVKFGitlLWOb9g_LR1DLezk7YgzRKDcQjouMyZCYvJpdsm0z5yAbf5Pr23oQGUFVR8ynUXdOJyNfVa4EJY3K0GSVpzw76svC4outfh4P_NgpX6OwNVz5ACN-GIqQNFK2JFC450uRYNDUD8mmc_jsWkvxyM94FOLUjre0aKK4zp0Zj4kjxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=g_8SkXjeEk_5Q9k3Ou7EZLPwiQFB9pe-QM8Gj9ULuAKqQfGFCCdpWWjLzaB0-Y8tghXjY4GcxhXX9gsbEi6BGcrdP01Sh7EYDJE3Nom7t3TJKEAfuymvtWvQNBVnZCUjAxGWLweEBcy2vsFnl3r-Z_bKnTOI_qvN14KoHsdb9zlXYW6JPhbJaIku2ZwxtVbn7-bUUuDF25K0pHQ7F9OV9LIL9mIkw-NqZghorzhlZBxrk2Bl2ht2QkdNF19LbguWBfvw0xCByjura01QyubprpuWiptR2LxkYGlnBZ-YLLWfZiw1Qvv0lqkdzSPWeLSe1BxvR5MFvLzbMT8Bi9ELJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=g_8SkXjeEk_5Q9k3Ou7EZLPwiQFB9pe-QM8Gj9ULuAKqQfGFCCdpWWjLzaB0-Y8tghXjY4GcxhXX9gsbEi6BGcrdP01Sh7EYDJE3Nom7t3TJKEAfuymvtWvQNBVnZCUjAxGWLweEBcy2vsFnl3r-Z_bKnTOI_qvN14KoHsdb9zlXYW6JPhbJaIku2ZwxtVbn7-bUUuDF25K0pHQ7F9OV9LIL9mIkw-NqZghorzhlZBxrk2Bl2ht2QkdNF19LbguWBfvw0xCByjura01QyubprpuWiptR2LxkYGlnBZ-YLLWfZiw1Qvv0lqkdzSPWeLSe1BxvR5MFvLzbMT8Bi9ELJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtv4K9SwuSdX6bjwiz1jraXI-giw8pcG2zv1U7lLaPVVykqottED4yye7UF68Rf1-0FDNo-vsefSLL1zK9ikfcUUqTamzVGa5oImG-OxgBzn3i7HeVK1t1lNz7GzG_vAEp8TOTbtCJElicTgvmv2iASn0hGrDs7OOxXVBcm2JSq3GHQuYyc5nPeGRgX1UTcC_BWEtYt_aJPTrbQhj7HWzv6Cgmvdz_X8GGjQUCvRCir21xCPbsgw4KjTlf3FblSMfeae5C7DXa2in3f2ZVsLnUu0ug2HoYiTzRgitl0noBfGG3mNNQpVleFvW20zrIwgem2moCZ7jMM2i09zKy0x_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RixHll-fGkn7tYOQtcFVAixTBXC-vNmN9CRQL_rGNpN4fl61W7wcOgC3o2juD7KmPo0mBX1ohcUQ7WBnpv-hgFZtJMcgF_L_RXS3oSuxrXx74ovpx4bA7jnV7i3UIK1WTdopMtQpHpAG7RFrFiomHHRi02xjNiLrEEFF9JrLiXejV-VdNkuGjhwuqla8klJqVJAgNcr1sIr06Jr_1n5Ssc4W2HCP3B6Uo0ua9gIemFfpN6A9pQdinKS-ikgMAKEakIQm1JteDwrZI0miknrpxQtYYrsaTDRWA1B1cVblfKbfrtj03I-LSA5assttkantDML6x3qgoK6zNBcv8AB3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4h-T7iHZXS7dNMSfI85O7DM1ao-TC3SQKXKPk_e7KEHuBcWvWllZ9zbyx48WsLI2ihy0syJI6lrkDVHBcpmvhvlUKbMVPfubCXSm_gJUCZHBjJkHNvnkggNEF3QHvq66crXlope-Exg_OHW3cZ8jHHxjQKMb8Sv3Cn_ZcZhytv9oGC0vu52SQAXCZBGy67dXtUy3fLdAv8qUUZYO5MU7lhINL8uDqqucbU1SJlqFJGZbOC2VgTVXa51QzH2u0xT47Ue2VjxWGaHHY5AS6xPfJfRDtx7NO1s9lsqkIzB-n2Y_bdUMOkCn4PgG8c1rtrs6_XJTJcFGANgJ9fx-A8gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDXLmaw5jeeex3JBjZKkO7wZprF9SsiEekF5HK4CTHjmMwrLbXk5fyDg5ECpYGZxxYia4tf9Ka1lfzk8CG15V_xrsFaTk4lxX_m6mKRgLEtGyB5rCMKsRyal4EzRmCNe_CjypioziQF-a8qDXN9AvQmCHHOs1OsxS-nqNnCvWOYQr_LumD1nK5zZeVsNIxs3vNmy0ykhSBfvOuYCNA1NG2t5CjjJgjEhnLwJF1MLLcmVUi_OQRICmG7JFf04iAQL7yznqWW2LlbIGyD75TWUUegVjd4L8WmZZ7p_yCpUmmXIRhl2Wi48BceMLsHR-xbWqZJpp43eR2Gv0Dzlcl0kKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp_moZo_xxLvjBDSfEwN7_D_BpQRriffr5de5-PEnwOoJW6WRoFHey4Lg2QhfrrY38h1MHrl1FhZ2-6gbwXOtGV7zAfrSasjlvuhnqoHSsjL0cxbfDiOP_44hBnuJ-bKlcueneYQhI_7PMUai0iEKQt6muu5SRR44Hm1T1UpgPtqj4626Q2Iapmy8ms9hZj_lQdo5UWlulDL-EPhaoBfK0PzsmffT8267_Jt5Juu86Dyh1_KTkdnCi-M8qeW6GW43DahsFbB3MJC86IWX6cPj5EWZ0ccU00aG_7XSqzk7-4Vw6YLc8M0wWaWojc3bd0oqjSYj-yCQEUxkA1F5BtnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6lyIUcmDmI8uxREROMsZRuWoGMfrx6WNlwbFogBoxlYZUbBlf4jObLaezwaj3HEj3NkdqyzEvHg0MNumrp3OmydYmNvk0vDIMDN2SFcLa_QRECTnqgI8MkpqnlXqowL6QSOWNbpWCFSBZJjxmxMdOb3cESp7xGf1aaXsFBOupW0HCicJR6ZgpWIFESDpMs0q0DzwDNUVyX3CEeK0NnYoCuKnIiIWBHy0SMxA6x2-k44hOWxIStVG6YSrcpNRHma6l8SQNBCzPQuAhkOb6u9gyrycf5jU9pLmreprBjmbwCyq2WwRzsrZJgEpOUBwrSy8IlCrq-3lJmasX9ruwsgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrcCVpb_GOIUlqap_DU1kNHkAlPk1zYSaNBseWoE1vnO256H-TLYVBVNkXgThiNZwspGoi8NfWzHkc7WXI8IdjNh_tA-PG0yzIvXsO98c-_QyGub7hPvZ9oa4B3YslHJ2amhBBediKhLjs7iqiqfAAOyZyYHzUUIZtJzeKp7jub4bQPhJCeJIIBuMfQOBCDZsS0FYBEQVHxzjL5JaO-8xJeTAq6PqtbBadYlRXxShJ-W07jDTruAyFPITnr7JKx90usWimaMO9ACArjMa7ghT3UT23KZl2lXFXtxSe5LHQrvIIlszsHHZ3wzhtHUL8zk0CeqtrAXdpjFEVK3ntNeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4vGhu9Shc3CXWYnD9QGG-7ZEE-MrcC0wZVaByIqUlx4B2FsV9BeBLc3vhsyU1jXewGISAQR13HL_2-j-Y8ADzgiyGkA2tY2SKz-d7eLDEWW_3KvduE4Sy7gxOy0mxO6aXCvDFJUmGd8bgm2EZQzt7dCmpAEutn9GXbbzgBvjjGorDmHdviENdkZiMJQrsllrouPZpBiDTm7gr5XOORDpnk5YFq8ZqAfAeU4G3Y8uNflkUgIVS3u7XPDA5FJ4LlTQ343csY7XKsIt1CXIrDMR1EOVAgJxly2Ka3ZGCqAFCdDAKD8agOTWKkac_qsw28lkhD58BQb6Bub4tV8g69ECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZquO--34j2keH04BM29h8M0J7ieL3NAvTpEogjPBptr7Fou5iz8wE7_aO1jsRLu6B6rxlIMmB-BBOW67zi3cz_pl_E1zc0puJMZ9eY2_XiC-fzkI5wa2q-QyIUpm-pFcQF-LWL4O7Ei6l5b8i-4Ud_P5A3sg6e4MHptUdFpkz5qs5stplAQwEIjCYq3gnH2PxhpboU0KPaFGif8jkS9PL0sxrm_9btSIp03_H3DEqzu45vmdRFqBjzS-sibpWFYMYBge-vV87xT9yyP_4XtRK4v6FR2mCV1dTy_tfOhyPExOs_Z7yi1M-5Y6cfZ_pvFY6oHJ_VdArAiTiOREiL1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVfSY06b2tGybblCllo9qHEtUgnK90Teio_PTCA-Ph0HKNKFeoAWBVKolxQa0rOhwFeTtQtMJqdoiguflFSrCWTG56rIY2TIBZ-Ph3ze8b4XQfzFoHtrfjmPENVW-IRYIRn9C6SnlHoo3_tVIU3drWeWFNGf0ojYDDISYDW-opcuXC07IvW9yLf46u6h7BoEfWWCdWiBckT92E0xMGaYVJW65uK_0GLURrQb9OjuWFVJSnVlgqCzxXfgR9mmmX3wmyGMA5rHGZ7BidiQ5lSl7ygwh9EP--uIK2lrMeL4L7GmrKqkTH3BbnQyOsc2D8HVIsx5qsro6pp8mPs6EBx8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=TxC7TjWSlmVjOaTfQLKQSPv89vUz8xWl_0E8Kekq2yWZxCWKbq8HfVRUUlSaqcdmK9y7g8v-iuUdktYLiLkHhHJetw0T-x5dQ8EvOka2va_WZZ_-GBJZS9RhpYHgvvGLbv9DA2U7_fZLpqNCdlOOUtWfxH0IYhY11tM1HqJ1SVICLYTkmVTYowCyqzZb4K4ctw3BJsvuqYCBBmwDdTkB_juKz8wNB3yW3gojcoTVVDukY3JLI3r7I_EOMVCjsq6n1_Zyeegqh2A4VwS42vT_9uSx1I-LIsCeI2D5rQny1kXNRIvL1VgeAS6QpK0EStaprlFuAGgbcA4HpXMXmbjbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=TxC7TjWSlmVjOaTfQLKQSPv89vUz8xWl_0E8Kekq2yWZxCWKbq8HfVRUUlSaqcdmK9y7g8v-iuUdktYLiLkHhHJetw0T-x5dQ8EvOka2va_WZZ_-GBJZS9RhpYHgvvGLbv9DA2U7_fZLpqNCdlOOUtWfxH0IYhY11tM1HqJ1SVICLYTkmVTYowCyqzZb4K4ctw3BJsvuqYCBBmwDdTkB_juKz8wNB3yW3gojcoTVVDukY3JLI3r7I_EOMVCjsq6n1_Zyeegqh2A4VwS42vT_9uSx1I-LIsCeI2D5rQny1kXNRIvL1VgeAS6QpK0EStaprlFuAGgbcA4HpXMXmbjbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=azZY0XmM2bUceIDs_ljxx0jeWOyVTclOALDut2nWlgho_2LFLgUfG4fsJinqdzQdT-gNgU1lYgRlGTmO_yS307pbg9qf_jtSYtDzhyjM6E9m-bsicN1FXKIWXTU3JjX2BowjlK4HzoEC54z8ILZkMpDxEEvydpwuLwDl-ar18l-XxA0pYa8VpaJwcmlQqBoqHREl-uys1ojLPrPIL6vLooloc2PqkfUHo7Sy5OGz7QQ1I2svnUBOKnVtES6LV8uEoAbv0O9Icj36fB45sq8UMJDCvfxUx51qjhf6tisVlcU3gbO4PJ20997_XhfhyaHxuLv9GRMY7-vTP_-Ue6Negg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=azZY0XmM2bUceIDs_ljxx0jeWOyVTclOALDut2nWlgho_2LFLgUfG4fsJinqdzQdT-gNgU1lYgRlGTmO_yS307pbg9qf_jtSYtDzhyjM6E9m-bsicN1FXKIWXTU3JjX2BowjlK4HzoEC54z8ILZkMpDxEEvydpwuLwDl-ar18l-XxA0pYa8VpaJwcmlQqBoqHREl-uys1ojLPrPIL6vLooloc2PqkfUHo7Sy5OGz7QQ1I2svnUBOKnVtES6LV8uEoAbv0O9Icj36fB45sq8UMJDCvfxUx51qjhf6tisVlcU3gbO4PJ20997_XhfhyaHxuLv9GRMY7-vTP_-Ue6Negg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=vA-08I5u4SI_YG-e9ItI6dOLK3kAZXXuKoVShfD2mWp6LtBMlSCDtKNehSKjV_sutqS0RPufDcDSfzyj4efo_NRRnHsDEHJbPDKQCpoZJQw5LFJqtcNulFD_uwdyOwcvfqbd30GDRtrwhYL3LPh77TEZUx9rNSmKMlNRGfVuptZ7YbuQgOyyZ95Qv6V9RQlOA6N4MO5Lks4sar0BDX42jQA87WmEq9a4X3L3DZoaVb7sCpKeCNQ2Xx_4LPj5Zhlgg0UVpzg79ZtQFZAfcsNWvKufxgHnf1HUlfkCYzflNvgd1Ve0uR0pL62UJFkG79QKbpDPGaa-yi5AFgR-313T7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=vA-08I5u4SI_YG-e9ItI6dOLK3kAZXXuKoVShfD2mWp6LtBMlSCDtKNehSKjV_sutqS0RPufDcDSfzyj4efo_NRRnHsDEHJbPDKQCpoZJQw5LFJqtcNulFD_uwdyOwcvfqbd30GDRtrwhYL3LPh77TEZUx9rNSmKMlNRGfVuptZ7YbuQgOyyZ95Qv6V9RQlOA6N4MO5Lks4sar0BDX42jQA87WmEq9a4X3L3DZoaVb7sCpKeCNQ2Xx_4LPj5Zhlgg0UVpzg79ZtQFZAfcsNWvKufxgHnf1HUlfkCYzflNvgd1Ve0uR0pL62UJFkG79QKbpDPGaa-yi5AFgR-313T7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbH_WEgRkAnwRf_jfTPbPAPrFXAd2PDB3kQ3JRaPXy0djFavFrMnIFpM9nlUwX9ZRUDOZXnuEsJ11pw4GfouFu5IfKd0bc2ePZIsRoAWd50Ea7cd6HG1juVOFQQKeV8u3SD9UgGY8I-DMM4pvdlg48c7NG3c-tW-D67Y2KBkxjWYcoB1RMHrtK1Fd2tdCJU0lWCEYhqFRRIW5cr9gzr2AuvoFi0f_mGMusZwVqzHxmF6uC0AaSZc-IWWs7kpieXH9CxeTH0RH-1ftIdfTudJAB48fH43B-QovMBI3KwT5PWfZuInkYbWxYPyKqLisYjG0KmS5SM4zkhSWv8X7jYsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FljAEM8ivdeAZ2-dxkCT5k4Sk-xhUMbP1q7J8b_iLjRPErbdprKBXAaJrF6H1viUWGC1aHCxn9UfKQMAvf2dO_P1A5ljPRK-3MCpHLfGKN-pbLDZCUBptG-9xP6pTYq6g7xER7WQp_B5sh_J45rGRHNv9xtv3MOUu6YJvITYnSaEvc1V8ZifyyVReweCArI3nV5AUL4OqIB6LkwYhnfko85D1xiephOU4r_gH5RIOgUoPOd76eYDgxx8mHxWE20apDREeNgAWqCCkLiOTUg7SojjKbJLk4p2CCXTaMH5sHeYY2V5b0SbGGORSosiT1_6Mgz7CZxMGazIDZMceKPOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8H-a51KtdbKMG_bjGms8rypJ7kqBXzwpZup-BQvwrjx-OdMhhP7TVMml6hZXcg2duJl_fgjrkKrHmjXNQWSKSv1fXsZfoO9ktwK8QACyGBZIS6ve5dg7Xzkl1YCVIdNHHT5SWufDFN3ynCB_P_QEXIEco2aRSFhC6cxSHQg6Ugmz_OwWXc8EEkfbDPWMfi2kDIAbjBuAZ-WQ2Py775Faz1Z8P6McA3fEnIjp89SHO3bsSC_LzzstjvwZzI4vZsjyNSa5d7ipjxgudg1b3POpc6c98JxOBFJF8x9H1EDynJEO9ZWoWjhJPPU1sEP2-LsqxKHo00iENGMDJexYlb5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=nAGUy-poI6c7n1oV96Z8ScNkk2Cdy_0u89APJms3pyc3TzvBzscqh-Jlj6WospzqROi25H1FlosC3wygEc5evfpJ7WGTlXWApRr2Wdol--bntDB12c_UGSoa2nd_vZADWARQQQ5Ij7jqKoJC1YamdZ3C7p-rX_sTyIYxn0WgaTViNyJkDWH6YB_P9LRA0s8kovOVhAsewMJhkRCawHRReIiQZWobi2osjz_b0VR4rX-5Fldv5hji1ToHOrST6NzlmD85e5ggUQ1gExm4KI3q8s7khKNbCAdJXLqOAGCj8dmhTdR1kTbVSI_xXzYOXAvWSvcTL-3jti01aI4BnA4z3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=nAGUy-poI6c7n1oV96Z8ScNkk2Cdy_0u89APJms3pyc3TzvBzscqh-Jlj6WospzqROi25H1FlosC3wygEc5evfpJ7WGTlXWApRr2Wdol--bntDB12c_UGSoa2nd_vZADWARQQQ5Ij7jqKoJC1YamdZ3C7p-rX_sTyIYxn0WgaTViNyJkDWH6YB_P9LRA0s8kovOVhAsewMJhkRCawHRReIiQZWobi2osjz_b0VR4rX-5Fldv5hji1ToHOrST6NzlmD85e5ggUQ1gExm4KI3q8s7khKNbCAdJXLqOAGCj8dmhTdR1kTbVSI_xXzYOXAvWSvcTL-3jti01aI4BnA4z3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR-CGEIYwxzctkttedtBzg6ne3B8SEmg8fFTq1cbqDL-LhSMjci45S-FoJlykrIYAmYwyQm9gwobHVDXXVs5ofuebVg9XEodOzRz_bROuNsuKbFV_W6p4sA9nJZMTCAu__fr5kI17Tnt-r7NG-ov7dlk-Tns5-mn4j5xTfx_yb4E3iivn8feZ6x5vlqS27-rov-ijVCwfZHHg8AWS4spyjuTk1pda5JgvmVNIHyjIgH8qmhi_xDONp0pBvfNwLeOcGzOTU2WcdYDRJCdEghcy2byt7jCwIE8FwFcuJVuklndY_QG4BlTg4FkV0KgAB-9tU3S4ICelgLbW5GEnZJlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=ehQP16eHeH5mSHEBH2V21gBTb9TLn9Kr5oRZbBXuNR5zOfNuD3Hnx8r6YW9E3tf67eCyjZGp85ezxwWNyuTLf-AVACtA-RuuhQAXow7RO2V6NKSIKaQzmUR7Fw_AXyP-qRy3RJVio7t7EPjTR0NL_aV6wYYcinz8ZSaYN0YXA2Fkg1hzRiEYgKcErdlIU1ZNmd_s9vW7BR8RYJZZh9vA9nNkNYgqWGekjfHQyTecfhe1oY7hLimtEWeoX2AWOwShZINHHYfuAascMgs3Mezh7LdEyebb-X9L_iHRxRqC8pOWEVNovqLmw2Ey6kIMhvvZL03nVsb-gp-z7RlmmI8Kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=ehQP16eHeH5mSHEBH2V21gBTb9TLn9Kr5oRZbBXuNR5zOfNuD3Hnx8r6YW9E3tf67eCyjZGp85ezxwWNyuTLf-AVACtA-RuuhQAXow7RO2V6NKSIKaQzmUR7Fw_AXyP-qRy3RJVio7t7EPjTR0NL_aV6wYYcinz8ZSaYN0YXA2Fkg1hzRiEYgKcErdlIU1ZNmd_s9vW7BR8RYJZZh9vA9nNkNYgqWGekjfHQyTecfhe1oY7hLimtEWeoX2AWOwShZINHHYfuAascMgs3Mezh7LdEyebb-X9L_iHRxRqC8pOWEVNovqLmw2Ey6kIMhvvZL03nVsb-gp-z7RlmmI8Kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYyDZSwAsUC-Us7J7eDbRcGTn2R3rgTawz8_eg31g-XqUZIgHRD3HANOVIf6D_sW5sZaiy6TULHoiibpC8WFXdUHXmU3tRdVLdYNdKUVcD-VfxHaeQsWKmHNxt0krsFX0EDKgcbf54WxiVEAlIdeJjYqRJH5RiPUQTBY_Y1_hXl-07mS4sBhFYDIajBF9aAWuCCW7bnEw7oOxWbuGsLAyTj8BfLV1CqDXRv58XNLPxeIa9TvCVvULUTB7_BbUck9ycyxqzP3S0CjKCabOIk_gU_zzn1AHWk_6PkpYSMKmH0NDf6WMMji8eLDcWfVrIv5uPhrQ_z0xWve6-R_nJ3rcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=exPXOAuSmMobTMHZO8s9wsJha21XHd9GB6nSpr9rueO3EKFPTmGqM66cs9bSd32KFyaAS3DruO3YGxEYw_PnsJdZADl1QC7Sp6btiBP-l-bVCPX9NQwzYUVQkAQyB0SRMfp4Na29044d9DNuwwx2HTmBa8f3rAfWZ9MSEs1vrbReFGa_A3ZA-k4lvwAIoqs-O4cD3Qzh2s0K8R8UtchYJJ_qXSZ8VNq0TekmD37a_ze9e9nrEvmmTVfQw4wNHXDTcnPtt4pOhFDdfmh3W64W8IbkdJnzIA0K-rqOQDSd8f4erW1qD2xzYCRO5-aJlKNmHxUGuCA6NsReE713CDP1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=exPXOAuSmMobTMHZO8s9wsJha21XHd9GB6nSpr9rueO3EKFPTmGqM66cs9bSd32KFyaAS3DruO3YGxEYw_PnsJdZADl1QC7Sp6btiBP-l-bVCPX9NQwzYUVQkAQyB0SRMfp4Na29044d9DNuwwx2HTmBa8f3rAfWZ9MSEs1vrbReFGa_A3ZA-k4lvwAIoqs-O4cD3Qzh2s0K8R8UtchYJJ_qXSZ8VNq0TekmD37a_ze9e9nrEvmmTVfQw4wNHXDTcnPtt4pOhFDdfmh3W64W8IbkdJnzIA0K-rqOQDSd8f4erW1qD2xzYCRO5-aJlKNmHxUGuCA6NsReE713CDP1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=YB7YCT_jTngYzWrUhyp10IF71ckYL6j9nDZ3TQ4zay2R5aUWCG1h5AtHsPjnAjNcEyo--XBVWmvEA7iYVPsPmX9kGAkb8zjmoAax3e08l1qjk1bTWzb5ODZhiEi5jhhbzJrYnWTPx39_lbVoU9Gk6j4R-29vE-ylD8lSThaicJ6-Li90vV3VLPvj58DSLEZ6vUVgA0vTVBD844FKC_-MhrPS-2aaFmUQJnisBxIrvOgw8kPgtiJnBuGCCtUJgtbZ4Bdk427qQ6CU01mc7KuSBdgOo_WlDAfUowpv5Q-KL5Fjly2gCP5rNVC_JAjSwk7sU7E4zkQ_MNS1Ai7urAt1S4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=YB7YCT_jTngYzWrUhyp10IF71ckYL6j9nDZ3TQ4zay2R5aUWCG1h5AtHsPjnAjNcEyo--XBVWmvEA7iYVPsPmX9kGAkb8zjmoAax3e08l1qjk1bTWzb5ODZhiEi5jhhbzJrYnWTPx39_lbVoU9Gk6j4R-29vE-ylD8lSThaicJ6-Li90vV3VLPvj58DSLEZ6vUVgA0vTVBD844FKC_-MhrPS-2aaFmUQJnisBxIrvOgw8kPgtiJnBuGCCtUJgtbZ4Bdk427qQ6CU01mc7KuSBdgOo_WlDAfUowpv5Q-KL5Fjly2gCP5rNVC_JAjSwk7sU7E4zkQ_MNS1Ai7urAt1S4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-3QhjcWXadHSMATiu6_4Xw_-sxSLf7uCQivLkIEgK7n1B3bjpsCqRR7kBfbmjiXKBRCr6IqwMCuH5JDElOX058o7VkHmB-7-0SY37nmdFa89apMMCLnBTQuXV507rUoEGsB02lWK9YRD8iee0xCu7vWhWEcL1fndZ_UtmHaBQ9B3qswymBLL7G0avjE-Z05r-p8X7q0jpgx-X36OXXvd7_vyiGooBMEL-DmT8BrLBO_2yIll5lMyR-chyVxfz4aLW2kvjtgzGIp96NqhVpqcJIx27IrFEX-J6ZZWrHaTsa-J15vx4N5v3fKpq7Vo7kXV15doOzD8b81-R-aXDXjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMyJBdH7OywXoURhxFWMeDpY17NC4woVynEybrNu_RmAbPiDMlBUdIOd-AW_pOE0R_5rMco9Ra9GjusZvYna0HHrQYkjNx3LBKR4xI_3Z7HwXd5xleF8GZMrw3D5Pkk-QdXltnpxmp-1qLPFqFOSkgm2xNpf_nDEgs3_dKnLisGnb5LpkqBz3BBJdu_5PqSf4l13RBY_hB6CgIK5vYp5XxnVenwQ0gOSCotoaTw87MZpqaGGrbL8c06NnkRmEvjpvTzaXNnddUxKVnbNpn5ObpPj2ygwth5mFCWXeYU28Rq-zkdy1mJ3RSjjcEzaCTydiONy4fNL_hWXLGECaeu2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moinDJnaW8G4qkjW39g4H89Q9Xwb4-qiVAbCFQ-wRtpBgztFE70rRAdUpdswDAm_7EDwPchZ04h1Tu1WV8XSYIJsnOaesXOhJE8nDmG9vfy4S42WXuQ6lkuj5eDBIlLr1oi40vl-1LoQ5YxMOt8xH8N7Pzps-SM2-i3kpQfySGtz45iKrDb-tx7m-vW6_GiLrmfxT0dLC6cgKkKxFRdr6aR3HOcAXZC6QNNT_HiKxGKL4Yd6TOTFaLGXZz0u7qYFHVkeynpv1YA6moQ5HHynJYXlu0adJxP4ok4gH1kgs3FacQAl0Q2sHtSfHEEtSO_s6Zz9c42rvxGfedmQl_mg3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_8ftmWW1GboxgJy2CKpCNCSQ1E2Gz_B7BNex17tljkMHMTonsL_PCrJj39_4Zyjpjbd-K6FOxUweCUCkWeMHSecJlse7g0bJxPPivSByxcE2Ea75DmCXwAjJfNS_SnBCM7gcDrGzse7VZcHabtrO_JpQbXnaOYiBsbsAU47IvUNsvNirOz-FU3GNhYw8gUzK38ggQ0O8HZxb5jppz5t1kMLZW4tve-fzN-e1i2r2tWztUNdz46X2EIcziopzkKQeldgOsGd_xBYuSNiZAvCbG1wwr-LTsa3FQgypleWfldAMOVOxy89baqJ-dHaBM9sbUVckfQ2SRQwLkbHGE3pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZJuI4QxyAGwzdoU9dKcxl85-Cp_d8ZVv4J7TaEL59tsoFJ_0_BsTkqVuDZYCjFnW3hkuWzQspZjpyf_qmmdDTMRQl2KeiknL3KVx8os1NFdygn5r61zq4iyByl9wpNe6_StgnmgtriBf89QdiDmPBQGMMeORmzIMSo501SiXB_LLpYbTafgBVEY4Cx4vGhsE4a0nr5gS_5CWXd6GeqPTVi39M0l4hIVoWe5HwNqEUGlKy0bDM6PKtRH6IpccR3_HYjlPygqMazvrsnWYr1mfq4Vhu9XrLLewo1whP3zYQmYohO576pvKm8SsWEBLUZkHLwW6U0_QxvlQcnF6zxTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=Cg6UgddK8YkFOLxipuCDMPhBhKLj_FAPEJnZLmynimjKW5BbL7xooH4K6PiAuSbhdLRFFfThKrJJgh4gdIBeA9a-XK31i5COPdQrTl7ccpHC5fHTUgjA27Ed1hOwRe4HXsrKnWl990Jkgc_Ed5Dre4IZU7b8AdyQH2qooLXGrYjiFvLc6dAcpHLr8113oUp8AoXf4GjJuPViLut6MR2w0Rtyajfo5noEMchyeAkuZuzKMOqY2as4vAI9Lunmh_D0w1m6iJ1qA4NOdU_dFvxq3HhNJkViTtgqDVvOpLLyIm43uylYN8_ZH--uPobN_pXF8eeji9lKczsncD5FK0mY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=Cg6UgddK8YkFOLxipuCDMPhBhKLj_FAPEJnZLmynimjKW5BbL7xooH4K6PiAuSbhdLRFFfThKrJJgh4gdIBeA9a-XK31i5COPdQrTl7ccpHC5fHTUgjA27Ed1hOwRe4HXsrKnWl990Jkgc_Ed5Dre4IZU7b8AdyQH2qooLXGrYjiFvLc6dAcpHLr8113oUp8AoXf4GjJuPViLut6MR2w0Rtyajfo5noEMchyeAkuZuzKMOqY2as4vAI9Lunmh_D0w1m6iJ1qA4NOdU_dFvxq3HhNJkViTtgqDVvOpLLyIm43uylYN8_ZH--uPobN_pXF8eeji9lKczsncD5FK0mY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8-Kcf6NSARxOtYAQIYhRiv33jsjnnMdygk1FQraxPe_OI-DS6nsIwSEM9t3cyA5dH6ea4MxkCct7eRDki336ByrbqJhFXj0UcD8F9zkLaXNoFdjJFKM0sk_ZCDgvRPZEszErFsAsI2oTpLP6Quc-GAWAsToUTNqJWmTC3XEAHkxSAy2RLvBVW87gv955T4s8mVr-GHrAoUXdNVVDJlitVmLWeTQwoTn8EVLpIgIrXUrB6mW4sYt7jYgHoW20lELBPI9eBWBM2kK5sSm9LRzEf4R03-b14B4bjKEZWGUnvAfH11qUChtlv5WKUio33rUxmK1PR-EP_df6wD0OT656w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISQ1ypfCDve9V4cjAHJnHAaVqdJGN2wE6g-vPVtw6Q-xP0YYPoZGjubvQv6gyV7FReY81Sr-3GRUJHVERvQwf3kK8uoPQAVO3SLZrIllsKI1sS4ZJ5d0HVMwC2XwKRewByOnaL60Mq2VZp-G4YpZoC5FOST0u2c7JNCoe0cM02PBWrxXu_rm-IYGdPPBx_XJ1900ip11vAF3b-aJ6jmbANuvda4osilNrmrF2MvNtLXOjOQzHsGX-f186vBQG4EgtTw3-fuJkxnGo4IjRt_EeHAVJjOvXfmXsyzIQ51JzezJzBxTrDCK_yp10RJZ03zMMhAGma2Kf8Oiqlgux-_2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S01ecE2Qwx-6-VmO8bZbLUZ7-oZ3I-6LSfHRAe7WUfmBgVN1KlW1HEgzvauZbY01BqrrHCMWX32brC-5a9M_YFWypUuFAePL7oBelGzLSZxduWIaRMcc-4WpHGk9pUbqNRlBxmaCnm-8FRhPuUmG3jLjOCdpo5tjls4EyTnkUzNJCo-M3A3E5hPJrHK3h4lMKFUFNyElYOL5-bSZ02hBUUsRxmsONwvHnv7EQ8Nyaj6DPXo600IXau27hwByHrTJgeqllmFaka4yUHMI_Th9tuOEg4AzJh2fBapXVNxxTY4qajLXGVpo2bVy5oNAplgAEjT9CDU0hAmvOTWQt-n0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ8f6VpLPTefwxgIFOfJ5gp59TgazyaZdsXdFVmsdTopTiALEDaFDGNNtZGf_P2qtY1H9wLgVjlVgMJTE9ozlEiWNGuCalovt1yZca0vCBL_cc2TvCPsf5JS8nQjLT2nb_3xP9d5s-q3TQRuX1wAw1CgzuIUJXe7VjJZuX-uZGyNZMXhcya2FNV73XMHavQu46cXA0LVCHUr2XlgMU5y9Xc4ZY4zPgXwRJzy93IoYtD9Dcs6c_rWhXPUMvPVagxNPV4qTv8Oc0GYMSIDMJJoiXt6XAJn7-JbXxA44Rd873jXjGbM-ESDNkA-IFBFfsIq6OUDuLswv0fri2hiiDU-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=Q8Cv7-d75jYY-_N5Lwd1bgUneLt3sIdL4YZgHg19TqRqqUTSnC1-UvkqrO8O8ILCaNVLLL8BaGdGmcriWNGFeePJMznSt0KysUH1Z3o0r0S8o_77aFqmoICwPdeZbYdgNPKNRKRjmywGtZ51QV1kkfoyNB5pG2-TFk9hbKGywurIWmlqaoCsi0pnDCVFNFBKpzoV45UDXclACeDkCKnWXlARCpk7P7ZWaThRr5J93FKHD-awKSZDUM8VPUUIS7FiYPlfHYOYkRpLTOTsHaDfHdcJxUgbTZ7xTUi8OLAFUtrr7W3xYGe_PeNHhIQwC234BmYx_WLky1TjzMV0GBaI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=Q8Cv7-d75jYY-_N5Lwd1bgUneLt3sIdL4YZgHg19TqRqqUTSnC1-UvkqrO8O8ILCaNVLLL8BaGdGmcriWNGFeePJMznSt0KysUH1Z3o0r0S8o_77aFqmoICwPdeZbYdgNPKNRKRjmywGtZ51QV1kkfoyNB5pG2-TFk9hbKGywurIWmlqaoCsi0pnDCVFNFBKpzoV45UDXclACeDkCKnWXlARCpk7P7ZWaThRr5J93FKHD-awKSZDUM8VPUUIS7FiYPlfHYOYkRpLTOTsHaDfHdcJxUgbTZ7xTUi8OLAFUtrr7W3xYGe_PeNHhIQwC234BmYx_WLky1TjzMV0GBaI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=ZQRJdmODrvUTyg6gnQmNbQsJqFkEOwDXJsiDh4uQfpj4AshKPNjfhC7PjC0EWsh_uTOznroaUmkpjtfuhVexZPf9lIW7nbfX3lCn5QWnVhYPeo8kJv1HSHvr9zstEZ2xWlbXqE8Rr-Rwjd5jEKse2GMSKoABDr4aZoBI-o1HPKe_08G7DuRYU5x0DZpoA8SZevZCfoM1ewmUG4dmy0JanEqmHOQZKZpo2KhG2-72JXb5tawF6ySGAS5U1Y7vldnLJ0fVmz3db0CBDIgHcFn0Zpc55QdWBTawTb2oRT7E9MEmgvZVZHzNJGSFOdX7XYvx4ailzv5bq0ohQUXpOLSMrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=ZQRJdmODrvUTyg6gnQmNbQsJqFkEOwDXJsiDh4uQfpj4AshKPNjfhC7PjC0EWsh_uTOznroaUmkpjtfuhVexZPf9lIW7nbfX3lCn5QWnVhYPeo8kJv1HSHvr9zstEZ2xWlbXqE8Rr-Rwjd5jEKse2GMSKoABDr4aZoBI-o1HPKe_08G7DuRYU5x0DZpoA8SZevZCfoM1ewmUG4dmy0JanEqmHOQZKZpo2KhG2-72JXb5tawF6ySGAS5U1Y7vldnLJ0fVmz3db0CBDIgHcFn0Zpc55QdWBTawTb2oRT7E9MEmgvZVZHzNJGSFOdX7XYvx4ailzv5bq0ohQUXpOLSMrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Ahc72J-LRD3otrRhk_8vDxmi2DrtsrvAOK1FF3BHcNFhlv_s5mLPQuEu3SdCer6E3SFq5Rds1mMzmRyPfsnclIjGvrVXSO2WlFgkqy-j9i-ntfDTU2cibpbAxgF7Ixse98z5S-4j50D1PNDUNXdUIrkl4vmVCMumcwLMRZQ8zdKsNFcIwkQ0xNAHzpCRpwSN4Mp9E6mv9-RPh6BSHao2CUzNWDhEVSLimNbsgDtwmj3NUA-NrtH9yAEIgB3vaJcox5vB9g3uHPWZHen_bIVf-7m8JEmXq4hL9_KSd4t6LyVErCX_1_qE6p9YQJBujHrvoeolyDB7GoVD1mReKJpFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Ahc72J-LRD3otrRhk_8vDxmi2DrtsrvAOK1FF3BHcNFhlv_s5mLPQuEu3SdCer6E3SFq5Rds1mMzmRyPfsnclIjGvrVXSO2WlFgkqy-j9i-ntfDTU2cibpbAxgF7Ixse98z5S-4j50D1PNDUNXdUIrkl4vmVCMumcwLMRZQ8zdKsNFcIwkQ0xNAHzpCRpwSN4Mp9E6mv9-RPh6BSHao2CUzNWDhEVSLimNbsgDtwmj3NUA-NrtH9yAEIgB3vaJcox5vB9g3uHPWZHen_bIVf-7m8JEmXq4hL9_KSd4t6LyVErCX_1_qE6p9YQJBujHrvoeolyDB7GoVD1mReKJpFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCaQv29gPs6TTTo1L0NO2r1dIvHVDXzMmfLBT_91hzXMV0yh01YDKbrMRTzjcK6sF8mqSnD24N8gzOr8fL0HoPo1JvXIwe5fO6OoibEVcIPaDayOHWl8bMyeUcWVLgR7V4beb8F4RtPKFN5wjPF8idhGxx-7cst3CTeiP3kzjgwl9UbJffZYt5f_0CyM66MkzaKghM9sFr2LdYf6CWLGfBQ9aElyyPXJlfNzOfHFrV6d6UZKJ8umo92ExlV2PuKyzAv6y13QIZQoAxbFpCFI-SVttbm0kpZ5ItlJZHNws-ninczd940Q-QoDwvH0JC1KtjhfoXj03jpgg_DjV1SaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsJgk-EWgR8Pl6ugmWDChgUPszWh4RXx0F9zDb-AiPjuQ9z_B1gsS-dIrsz91iTH8KSRRVZHRKxjzFDdFgRS8Kv3KR2iC4vhYW5tUoTh2JytJElC5dvEuFlQOQ8SO-lrLPOULbwUT4tACijmpQHkSvT-O8Pd_Y0L_w3QjxZWAnDzJrQNeForezAwNcM9_C848H0KnHsuNHh6GwslO1MvRc-RXff1FcrSN3r9_Rl4FMFpdAGWwIdlxDG3AZi969BdFq0QUNFM9Z6jeQJURJIFg_JywosBI3jQD2FB0CCwXG_LiMoU9YDGoDH6I0d2ZsBTLXfYfqNYxB_pm9eZbNRfhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEBq_W6kZUmud851UxamMJUhFYtpStsLHzpiYJp6s1E7r0Z3Kfo4--QCRIchxomMulZUpYrPScK_UVIAglGBweBhhLcezAvKcpxJcl-eXhx1kaI3W6Y_IbG6zipbLAq55JeQsgOWMNaIf3ut8LaDK1xwud0vfhFbhH2CeQM6rYEN1-bBMcWW5m10HVS_YUPKwCMMuTfrPqiSzCVXi_or1950TAeyUyr8hFitoRrtrzrpqCkyVPj76FvGVYn6dfMIhlNw4YQo6fpUnhQoVbBQcZGyrU_-iqSU3PeBVJKi4oFDGDc6WvqDbN6tBZw0f2G5T42shRJnQ9dyOi5Wo1c3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWG05UoMITFx-VVvHbEBll_IlYmv4HS5ZUQBvvEEKrwj6N3kdo5ecrMYOXOJmkHPfWUmrZZJv4wBQYhMR3EJbSDd7ZFvDUuB7zeJEb2HqN5ifDGGFQsEXGTgmzYyGk2oCoUNhbIQKXtP--bTrzbcny_hNWGCWbC58Af7ICnTxsq7jQYkRsJV1X8STXlb5aieA1bDA3snyaOpxE92t0NJ_UUGHz2E61uerG-sBZfcPIVSMkhyNx9KWv9LG7Qxbu-hNsnyLCj8_L1TjpYsP8bzZ8yatTthskYBwcNWOSLqvz92PU17fhZt2xxmGl4KkEdHjW1fey7XNaT8wUSyMb7iFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKzDiaDHmr0PY4lh-HN-MctrUJ2PgkfnqBVMKULBElnHwRAR-ndso2K_8q23SprQUsUZt_xmJFG0tfguH30PI-BYhaNd4EHkDvLNZDPnpCWPBFY-d8Dpf9KNeXmiDhsvRc4RSxepes98kjbAm0-vlKU78uF6RT1jECxJa7csdgyq6AQwp_BOyc5aShsUPkiO-0njMjQPljR7VPXS8DXe3guFE78lLw-1SPnxnrh8HNVKtmNLDq8xQmq7fViZpo1an1R3T5vdiHA80pBcb-qKR6eAswJ-y7S0ds5QOkfe72ZyK6Y9W_BXpK1mUxYFFGzp2T_Nbwx04XEzAWCjMQqD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipnuwbsyGGp6_oTcoOAiWGCl3n_WzIAhd3fDy5Ev4rxio90VOeP2qGapFiGjvpfDnG9uRyGpW5S9Rlxc7yY_DtWMshDnGWhU7Dx2f9vLMuWtELviLns5eWKioQ3WCYO4MG7863snJWoyL7Vp7QPx9jOV5yG86OiHF9s0Akx8XUfi-C9VdQA18StRf2lHCYIVp_EJc3kZUPuGmgQIrmJJAXPtytZbGXYzqX6K1k6mSPfOok4V5qEItF4nmyoCv9cvBWVC2PlPqJ_24vgZUTdPqf74SzYUZQ4h3658AyG8c0xzF6vYM75NfBO8TEPWKZesy053ZERyds30Sbm8uk4Jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSK7FeVxU0S2mFFcmnAet3BBmovWvau_ri-saArFls1EZnaF2jB_fN3XdK_Mx7bqJCiT6Yr9ypSKLoYEPZOyaYfGEw2odrNJHVKTfnREmhhhymx2r4Kr2YFxwfvZyXX9HsZxG972OeglaXE8rBgCB3K9c-6LrZC_2Ja5gtJySchcdkxl83sn_nDaJprtZZpsMrkMQNh9LWMobZFsJDtpJFqbzrugCDVtqZHJbApZR-zjeyQkU7tmFq3YnB14rsxRxjV7yhSOYqCrr0Jt6a0RjdTk1IriAeKdPmeZKmFhq1oOm2NG_0_7ifEyoqbyU8ZZiS7aPc9cG8J1wRQ2AECgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfXIJlPsjEyoHbpLRdabbRarH_ZmqihLXEbnxLWTY9JKS9tOEqqRYNPpzyECzKQZLDMK0wpf-lqKFXNY5mqOk1XsuHCeMrHfWuhLW7F1WAYb_NI933aRMSPqODX_oDi50Hsjt3rBq0W1TWt7GXha3GHwtBbV5NhmcVw5IXluuHeb29SRWY0BJHl1ijxAFu6GAHfUIpKztO5RZde62VgC26-U8jcQAsiHFYzGVQVFDXYiOqXo7hrgmWE_zd7K35oPaGe-t7xDMApJ3wHkaIR3y3wkF99xvWPAczs5WhAwnTFIARX6YdnvhYlqSvDIzcBEtNeLErg_cv-6VNSENkDdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1scGfQo7E3iUVcDP-4PfA8mKT1vUZ2escC-zq0HFZSemNZjq4sVhw5wYPWGtQuVsnwVdJSpQaTh43XiSFkqikEJ98szrIHokjZLjA3jRs83gXaSrEkbZzkZU1Zw9VjX9IXya5ni2lP8h8-_kTyhoNmPN5GKXXjNBNtURuGrGJFPaDhQZrPTp4c8JK8WlKMPodmk2s6DMYyhUmHegvT3zSNnCaezkoZnvOCy1wfXevtp8GIkIofuVmVBMK_gA4f_RWeXZmPiKlMV03iIOZxbq3camAvSEEx_qgJTfNwy7Hh1WE5tiL9AbKIkJ4KRdUcwhnZEgTcWDwY7mQcVMacJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o60tQ6H8vIDvrn7Q7u81lC_tU1pzfwBXcMll4lqQB_d5ksE85DVfoF7jlm-FdeVGLgi0XLU_EfgifEbbIPRGIPMAWeO7as3C0QJVDY004ZQSsA2KjHp-xtJQgN8K3PwQJP4Xm5ZnUtfblXlXiDu7YPusmuHC-VfM8c4l2XnykeSuDcvZOaqNaWS0wgLJoadpNp6UsFd7Or8LuZTOisMF5KagfVbqDAZzH1rgcOOjNsNpOwc7uHI92mKcyC03vJJp2TV6a7SnBQdTqu3zyE8qKcPPj8K18cUgwkghmDDqhTUih2FWYQFxVHpdtGLpwpbSG_DKf2NtBMsqL9-5E-Gufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtSw_SrRdbOKkhSFoKqBeYSlDIdRfPJcYnO7zdKsYHQlKMyCMUmT0FR86TywowHy1LTzs9wCreKFp-GLNMFVljcxhG_IlXsuTUnlRWROGKd-usmRhOuCOPB5EnWZQpxxn0Qwh8ntTAnId5flzaRO8pAzM2d6oaatRWJVq_e_tD0wuj1U8oMvgX83RUkbSkzqO5J5Eaf68STuv6oURBaXd8CzrJSYzjJt7YXzIfzBqnbdAQIyISWM4oPnd3K0we1uva6Werp0pILJ0J9WBK9UD99enEGFwyB1lYJpaeiW6sk8nUNjBSbjfif75mqYYRHENFBv2JVVKv-AoKMXDugqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
