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
<img src="https://cdn4.telesco.pe/file/mswG9WrXWmyTnlM6inCcPUKERp5ISVy92UpEIGokcO7d9ep0KC2Bv11jJR6yxU_ahekZsIwnuek-wTbXb7JdQ2pG9eSluC8jf6ruPfLvJuKTcb_bjPfjE5FTkaUgj-M18QKmfglEOfbMEzcj_9pNuq7MhCOVj4uDfd2VMmcXhOTxHslKBmsmWGKFhDQ-XriC864glkL8FNu-5bnMVJneGSY7Rrz8evabqStrRSaKLfGzlgxpj26BxFxDjyHEVqcY_ZPgqguK6lUhi-IE57oXsgvkq1-vC7h9p8a66zfna5byc7f6sf0_pMGkyEhqYTVq5p2eju-m3f9dy1Z64W4-Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-663519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fN7HulHmX0vpWrDJRzKVfHRkQQdnISM5g0m4EzhyrUbynWYDT1d_ThLYezK27LGN2L7DzmgOG_oebkGC5B7kR1JQF5M0-MMWEq_Ns6-_RGhks4jjIalL5ZzSzS4zh7l9Ttp3v4gaCljFSeMO1ymoygvQMo-OgcZuWyvBePIlrFN7oPJVRfUh4dmfQ-IfOXrAdDocpn8XWfwcJWeaKpxqDIMVqlkLpJZuJt75NPsqOoxhhXzaBK0-5nwhaE4C0zFjrjaz7KTbv3skBsa20WNvCPa6jQiHAv9zS7wOvonlYD8hjE8k30--ZH_RyDp8W3CHh1OTr5k9HHSkX9sZ1BwyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkYSwEY49r8XgFf1YmMdqWnNUdh5ZZ4CDcrXJn7VkFtVDKMau4RXWet-1F8G-QpQcRP_XyNQ4o9W-M3EjdbuPvI95y_HWhQfN-wDnmt6kMVkKEJnXcCigquw_GMB1xHSGYYV68XFiJxaeYNZt_wz28SAb0N7RKFiHs_RpW2wju9xRS3ez9pRILroY2F13U6Lx-6GIP8C7Pmskx0WeGDldLM443OWGd9PjzdRT4z5WkUWOSw7mGurIeXqIbFDYLmijVqqFfC3nDIqJ2EtTlQ9tq-fiZU5mrpDZuZguH5YTe2Y-nOvsKLSlUoWSwELlgJxJmIUnIXW_7hiTSE3thDADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwc3FVKCPemAlv4da7S-TSu_Qy3SI3rV0b97dyMHDWE2X6khsZfAaQGBt2gabh86IbnaukvZUVIj_7cykgB0yk6Vwpxjyd_CZsSRD45wEv6PIybOeneWD8ATMmox0D600fTXF0_4TEASRtTui9uXuWIgW3Uu9Zh6rwWEjqjlyDP0EWEHG17rdThq5sVsrfGqbxovnFjL59RwZ-OVmObrdtnOiAYVzBZnpWebQNnH-qp7L62AGt51VU8VVQyNmiP1r_wePU4jLKIZxdkhE8qhzpWsjtTBeTOxwOTJAWCqx-sqqYo-nvBlnvdyOEapy5NeZDev4bDuKwXCG33Xc5AXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnRGOJNCvd2pPG5e6dlSMP23aXBHjuk54GJb5I4vEnHYBhXpSzMsrG-cKyqOryN5TUlqyM18L3ZcOpxoD9T2eSi4B5GM3MPO5aBksaG3BjCj5vBrQMXpQoC-wQYcj8smFtFwc9kuvFgDxbK-6bUtuKpC5VmIVQV3qTyb-u03SNj67YKRl_HbyFjvrbss9ThoLc0Or6xcBhR_LHUjIuVW-FSwmxMo9934uUZYS9aTJECUmMsSQnNAeiGPFyPCjX3sgayIc4GRCTegj_jDJD3YUgQfQ_ilk4s-D-jPFz8G_e1zEO12NhK4AUKYmCTb0o34fWD8nmyHrqCcUmRzndpCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRo7cSRx6g4pFqFdjEezDudl06-tZbwCgjlIlXaicdou4ATZBrnOV246bV4Xxn4Hr3FTyDKwFJZe55Zwu8WPPMc4UI0IouLYepqMgXU6qoisoYoPj01-Z9KnMvrwsaLdzDypzSqUAaLO2IHZyWnzSGqoEimZ_5EQjRZK_g_s6FK2WHsqD45Gva8x2IDzO5tSSQJSV0ooBEYAqGRkh7GlZmDB4QbwMlclaKKXKM_4NtuWxj_2wYXQbA6dn_beuTBt9bZVZzq9jf2O0DM_9bAnqn55K6qaEPLYwVLRWIuOUvQjsrkpkhXnBuVXUD3lbl1rgwXxrVWfOzgNi5cw9hq2kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر هوایی از مراسم عزدارای ركضة طويريج در کربلای معلی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/663519" target="_blank">📅 18:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663516">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjGaH8D3TXZaRTZo-Af1TNHXYg0BnwqRtXjli4cum9O8ybXANPuA-cqa17hmZ5tTWhPWmwmiSY3_Jsch7sht7NxOd7oo91AJawE0x1aiJTiBCt7sGzMDfVA1VDUJHscy-0u4gpGSnmb3068WVTqj3u1hupC1wT0utn5PFT-RXLOB7YqP8-AFPo0LhSHGkfKklP3E4v0LV4orvgw4YAeAwgmNnRTNLmwLLjaCmJ8NLsQFpx5ozWS2TWZ8BXrv28iAqpPwHLR9ZyADpTEPwNmCvXJ5vG7kl-5W3fY4r5pkUoGdYu3aIS6y3AiqpSDLrkYVrD5Qk1mOjAaveuigSDahIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCQC72QPRoXebjuOY7Cw1uHXeurj639RG-K4l5FWBbP3Wt4lC2n2Bb5Rw_5YLgNkRDpyOFL-s500_BDHjjxnDD3v1yfUISNLfhf1KY94O40D7fZE8E-4Te1tE_QolHgVap7C3_DJl8Cd6WgidHxenRZVu1ri9O1ehPbotTuyxQNI92pPvPInXcV9OqQLZKaKx1AqQNNpISA-Pmot8X3JyBAcb9DUh095JC3cTaY-UwmZusxiuRNdrvAkSLOQKyslulxmD7v-D0l2rN4sK0rnbCeGYZMRn29S8ovsFgcMs5c3M63wTawTe36NW9zRcteqzg6kEC2e11X64rxOB_DFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8XHQZFG7U6iV96aQmuCP_moGehjQUhkLcqjzuZ2sL15OUsN04Qsx00xmBCAx4hKeO4hLb9NIGycZukeevOZjJto2seQJhsezXXO8dKJPzMwP5QKhh1h2DJGJbiefNX6EGTuNgT0eGpnScfiwsVqe6lXCXOaCOR86rF6c24YbVj1T6u3XkztvLTaHGOd1IRcaILtewxtciTaaSGOWR-A5FEw5ur1xF6UWHTw6XbL6oPuEgF7h2raLdujEKYw3z1A5P-lM1PLWD5fmpMyPNJRyFQ7X5W5JK25F17OhPBcxIf8hmLVfQzdS9hgUGNdYCY8HGfiBllpjbjFN91HVIl9Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در مراسم درخت‌کاری اسلام‌آباد با واکنش طنز کاربران همراه شد
🔹
بعضی از کاربران با اشاره به پشتکار وی نوشتند که اگر نخست‌وزیر پاکستان مانع نمی‌شد، پزشکیان تمام اسلام‌آباد را بیل می‌زد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/663516" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663515">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKp7RTZSwwfRXlz34WHNpRYXB6GgK13afSfrogmIvxNP9B9NyNf0cYeehPp5HgpWU65ddwB3ViXiHFZOxD3gtGEfuiOUmF_GXXL7nodagilwSQWzc6Mf5amOLu7cLQHXAxBKmEpOsVs5xippKapj94pb-pJlRz778q6UnilNEJ2OrYPELU4BDKF0ocjD2a2DRvToLtX2w6oYsYuOoz0BtJd9xlEzpe4FGE1BQXZHa7dQn9De_eXLUIZ3cyQvbS8pEMbAB3cwEdCIIiHhoqCIiAxas17kbpQrGEqoCNPu06mPNt6pSv_8IdPfVjX4rwA5QztKkIuNb39JqomjHzq8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
منابع آگاه از ابلاغ هشدار جدی جمهوری اسلامی ایران به دولت مرکزی عراق و اقلیم کردستان درباره فعالیت گروهک‌‌های تجزیه‌ طلب خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/663515" target="_blank">📅 18:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
خدمات کارتی بانک ملی از ۲۲:۳۰ تا ۲۴ در دسترس نخواهد بود
بانک ملی:
🔹
در راستای به‌روزرسانی، ارتقای زیرساخت‌ها و افزایش پایداری برخی سامانه‌های بانکی، خدمات مبتنی بر کارت بانک ملی ایران امروز جمعه ۵ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت ۲۲:۳۰ تا ۲۴:۰۰ در دسترس نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/663514" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
دبیرکل IMO: بیش از ۶۰۰ کشتی در تنگه هرمز گرفتار هستند
؛
۱۴ ملون در جریان درگیری‌های تنگه هرمز جان‌ باخته‌اند
دبیرکل سازمان بین‌المللی دریانوردی:
🔹
شمار زیادی از کشتی‌ها در حال ترک تنگه هرمز هستند و از کشتی‌ها درخواست می‌شود از عبور در مسیرهای تأییدنشده خودداری کنند.
🔹
طی چهار روز گذشته ۱۵۰ کشتی با حدود ۴ هزار ملوان تخلیه شده‌اند، اما بیش از ۶۰۰ کشتی همچنان در تنگه هرمز گرفتارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/663513" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سینماهای 4DX در ژاپن
🔹
در سالن‌های 4DX، هنگام نمایش صحنه‌هایی مثل طوفان و سونامی، با پاشش آب، حرکت صندلی، باد، مه، بو و نور، حس فیلم برای تماشاگر واقعی‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663512" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyuSx-PtPRp1bkJ-cYyNLrzgxGRRyC5xJ_kz4R0d2dJH5-inHGnUqxpR1MSTKJ7eaJoOFgT-fcxdAbOkouHGa47S19h1KIfVvZz6x5DtMfbvRPSci2jnPZ4NsUTbaZexFEC65MEKFFDujMw3Z_ztwo3s9mkIKzJ3hh_2Z9wOEifsqQqjF3BGQM5dRY2yQRDwLWSi7zvBKRnIFn0JgU22auh5XzrvWG9h3P5q8NEWnTDZlYk7tSjAwn-NaRo6TnBXAmV8QLtMFTnOa_cbIT-blom_3i48CxTpKO6BAHB9VWdaUYzlM23tPlA-hMWzqBME77jTkrXea_K8NpNA_vcm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/663511" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663510">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران و زنجان فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔹
تیم ملی کشورمان ۶:۳۰ صبح شنبه در مرحلۀ گروهی جام‌جهانی فوتبال به مصاف مصر خواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/663510" target="_blank">📅 18:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSXUUYk1SfRmf1KlB8PNv3UlrZFLTqqoN9hAMEBLUyoMoGAmmYzShV6lFFIeFUgzBra8UIRpdkvUDBFqbEzPIIE6RnKPvn3xM6hIKrT0jmLvYSiK-zY6NnH2BrnjMYJIB_pZK3W1aMsVHK9B_RxFfeJo3vgnmxPHulUuOKaCn5Q3tn3pJewJJgTnXGigowvDl-EhtXY6R5D3vRrYO00ym3fm5GMGkdFLjPaQXwglYQM0XWsaZFsRYM3gSIcYKwX75Hi7U5yCVH3OIvfTFJHHdifHAEt_VEd4xHUHJ9l_iAv95QZ4ne2OILhNTxFXZ1jTbzSGQvZQrxJaFxTnUY9LGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUkh9v_saz8msBT5Q_OEZfajS_NGvVnlSeyxJ3UBgtyZd1kjdzgfgFg7K-knqUP0VLzXvbja0kLEDLq2ghuTTO4f98a2gIkLs79YlSIAH8BwnCo-gv6Lvj6LLqcVX2Y5G1UAcAJQ-7Qgb2xP-T56NKfpQaREtOWj0--Y2ZHcszpY6kw8xN78ddZKXmGwTRN4A6tgkMr79sndf8MlBELCiDsEsnTyCmLmVRSoS8S1I-SQyZe-xd4MBt1E0skSmnFcMscO9Dig5ds1V7KppqC2SKYM-fCmEh0N9pJz4DJGZzXKY5DAqbE_KkkxIyDnU0QvftW-HZhuAEImiMMIZStSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY1EGut6F4bdK7wsuE7GUsnhoKeYicKgReo2A0igX6vCHqH_Th1R_CblQXw6VMwSlomQGesx4plp53niVR-U4F1OCz66rMhHe3w-07MssHy0lREqPq7OGh1W4PhKpDwOB552Ndmyv8FzgxG_Qjs-_aJGmHBmoQI-hNfV_fnn_I13bMU1kfD6yj9SXQIlQNtQPDDMko_1HHmB_h1oqlMcCe3jRlblIQYTxEDTn7JdzXqGSWeiqdEVrLatAN5_UbYsxbqDnb4b7QbOxoMyqhS8NxQRVAash-DXB9R8AJ3fBJ6NRm4k_aOG97rz3wQLrXgEOLL0VPLyolIAst1cIAzSrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور مهدی کروبی در حرم امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/663507" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7V_08iUw0bhuFc5xltYRTFxZge8rpCVHk00I5V4MMAZNpbuQXVCjN3-9NbHsuVnUzxQkSSVAvrrwgsNlU9-LGCgmRhh6J4V1Aa0-dzBR1mNzD9fVQkHL3ZO70h2lP4GQpi_qU6IVSJviEPQST-SvtakUIQEqQAwXT5zQvO7tK3BobY6P67H76mwsbFVUSQo_jjeDVeKk5MxwR6Ojc5X_LcljXkqI0TDXLJLkwiyu4bt-a3COz84LqP7sdQBGCSvLY2C6rgobRBgyEqq5IGCB3cwSHUqVaIkS2rCxWr_04b83z83zPguzXw95N-H7ePoekDl1FItnfUSky4z_vBtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ3SNrjW6aIGjR4PLudD6HIQaIFdu8j_Hmedm0FKGdEKr7jx03lT7sExFSsN402O_25bpAkiDNJui-E9UkCk_mCW5DvFIvYwEL5alR8AssIecOMR9BroqnVPFdITOMHpdafUr6sFT133eV0xiZVRC7uiv_VXt5fkzff9j1w4VfLVdKuUi1LJVnTWnV1NtbW26orzf9LqlrM0GadEZTgGi6EnleaoAQQTHcJEg_W11-aJBRHKFl6vn9awbG6yYZ6ekt7_0-KvtLjFEWnKTEQEwF7BEa8qJP5R0FSQq1iJDsdVOp4L3fiioSw6YJId_-rZ6ygioI_g6PNX-7lDOCkN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9hESdNLbUP-jlIyK3nWh7z5Pq8UYOA9rcQHKKHnW6nPGtRQEYZlVGTfwIx7fjz9vPLGeKh-Uip1Ud0QeQNiC-QZiTxSTRH3fjeDV3HObxQJTmN2C-6Fd7Z7JHFFKguHUI-2wh2wuIEXobQq9PKgblwXbjeG1EBkT6v40Eu46A7m2JmRCrHE_ekVa4DheXZ_oK0N3ScsUjewptssbNHLq-Oao_sNAKEX46DlPJ6QeDkuwC4eKFv5vslDZnhCsYa_G4ztcitufGF-0g3p3AYGpDiplLdRx6d6ngAIQMn_zsz7cV52BIoM6JHuzmT30o5dV8o1ROZMZ0jCyfIDnyhCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdE_MYga_PnUNib0Sm5nA4V3ZqFe_B_9p0bl9lvV3XguLdBOqPiQ0p2ygwrCD6_LVhFvTD7q_TO6EFBWDtnYLXfktKPALSjBPrPXIoEtHxr4NJUe1YoRakIWPdv4JOY7JDfyscAASzjWvpjWhIEmghb4HjhcIgzVFZXuwNzS9ZN8Mzp2inwe1cDJbEnfJRTl5sstR6SDbTzIAvDLECAqjEJWQu5wqYVijBrHtbQfbGgCXiIZZlODz4bARj7I8IRRvmPJKYC6k9cfYTo6h-NFmWx7gr0ocV_b3DiSbRgvHNolVw_8ccJm765whChL9ouifbpEQyYShtWLTdWLW4QLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7yDNqvHiGMjs9GH0sokPJ2ZKpSlk4L6xdq8kT2aUaBg5k6drqfhvk_i95FKUHL6AhCQD5nIJjuj2NF4Hx09lRQACwy4ocMmqgOrVnSZVQ7izAEIy8EXe9dop0SsP9QIHsL5xdkpBGSgIm9P-jTaFO4yJXvDjftmFviuNF_ZaSZhWS7P2gqq3xUX2SXEDaho1kahL_zHFZn8y9naQswFmO5rS3we7MHlE0_2lAsCG9dDJz4bBEz4fMevBYWJQr8lWIbfjSqh-28JLHNffwUqMnJccAP_6oSOmyhHljQrXAaTNhjAd0M3Mn5L0Ve8-Cd8PebR1gH72lc1bhXrY9nPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqrzBgfPHdKAfnbNzQ66bUiDBuvPYPK9Ofg42_Q7aKdbNcRnZMmgrX72Q7-cnBki63hWpUYGlpxzh5KNH7X-HoNm3b3MJ2ljddCgIoPIfWEkhwCkywEmQrbWpi590yDPJHTCIOZNnQPIM__69zrRUQuqDI9SDMn0WrOGt6LsfzCI6_Xu6lwKuWlWRtYLbCN_a_eSw7i41evJFdJEeUw65yf4_jLMsIwGDKaIkGM1Nt-w1elx9vQ5uPYI5b58yrFDdBJOIXWwpIeOtxDpxFYsKJ0lXI1EUruvCsfIaNhhdZQ0QdowQR7RYKtmUkFmhTb56fR8vGZiMBJ3evdzGVV8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdp0DMC_W4t_sE1R_t8mMpJLtOrpUP7KEhNj6Jes-5KtV3ld8zm3IQdF1vrk8MmkgbcaFVjpKA9DJorhPMUGQKH2gqb_X3petNqem9aPyUqXN9UMOhFGe7KsXAEcZt66RimLtKePtCONxe83wU9ZXh--0mUaB9pYVlpN1GCssEEp3aKuCP-aLzcYansNeDRzUTBrsG21wouJ6IGw3DzjtMae5wNQItQ4PHPWaGrFTYQrL07MRsRWMQuBAPxDFc0DBzIIPBCwaJOnTN2HHAOuGXTVTddsIEy3epHJvN1xtNCFBeWDv1KTYLHyBvor6mjHp-2aKiZZSTKE7EEgnMqWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmi-kutsgfjMk9HqtI4umSPQx8xDAfNlXCMA1ShvUiodowaQ2IR8ttTypR3Mo5NdzyRafgp2I_vp7hn042ONkx7rmJnQmkVqlMu2KrvNxcbVZo-1jhiBweX-EH1YbpvFHABI4Le3LxuicOXXXHKF1m5TMkiZHuYshmZ0sLdOjLobb7zNaR_vjqsClfuil-EQ56EyHIzVyxyGs6_vH2tUHn1kWllfhdcKjbmyOFA00A21tast4wQ-MFrF4Aw5T_AX5qtJbJw9tHnSfhkv12jtc6smdc8Z6JQkMOXLiIpSSsO-JrwNT-MiOaFYD1UoaR6ITzb1FwA9G85nMGRTfr3aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuks0JJdEhM7ht1mRhrsUOgc5rbhgFkx8T3quJp5da57H4Itk7ZtnnLdG9A77cxy1oJNGCN3aXnM66_HRqwj-dQkEyvd9oF9fBwm1dkN6oMc7hYIK6C9gd1WoMeq1uKSWNTMenVtSB4rTaiuQy-0aNLjLSnPMCSJ53s8KwZy24lrmsesHzx7gacDj5BvbgNPpVjTlXsfv9R_1iOuCrrdCHfu1ErXLOhPC5PXhXpBX5p1VxrIXMIS6rrW8J3fwNgwP4tHprZ1a9g4HdEtaGceQ8kdBx9AyFZdEnFd3yjhYzgBeHy9U1qVOMEPf1E4yc7qDS1u54RXAMomwPwwsB0M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYlRymn2GiWGsfAPYeGOEHsEpBwwZdaS_KjbdN_imVz9t9FWTLW_c-SRhLmRpuzyt9dXJXkwJM6a7VMBCa1gVcYhB7AlLlcKLP-hR3EtxM3oQKB_rgEDdat7cximsCPvmQonJ65gg0nTE3IZq1k6Pt3C3_PINEPrl6Heua70ygS_NoyqioTxzo-6R_MOK6nW6a2ci6HZnasfbZsqlw5o7fQL09qZ6PYaUIMSSuGC1gdwIH6-KB4dpsdXAN8xX8yKi0X5YMyy90FHK6KoaCHNB7ov6ewJbQGEhL0lhyAm2lmhoCocvyEOSVS4sLrNWxtrt604WrwojVFPE3fo7wnBjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برگزاری ویژه‌برنامه‌ محرم برای کودکان در مرکز شیعی بنت جبیل آمریکا
🔹
مرکز فرهنگی Bint Jebail Cultural Center در شهر دیربورن آمریکا، همزمان با ماه محرم، با برگزاری برنامه‌های متنوع برای کودکان، نوجوانان و خانواده‌ها، مفاهیم عاشورا را از طریق قصه‌گویی، بازی، کاردستی، نقاشی و آموزش ارزش‌های اخلاقی به نسل جدید منتقل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663497" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDXHTH6R_PrgXLyJPpPxdxaj2M_pw40-EcFF23LxQk6gTD0I8t9mhnKfZDyGBw60GslwgK9iapdp279ULz7xT3Zpi3tVwFmCnhDdYs7fM8rTRuGaw9ApHJlJdwfR3v_zD8tML066tOkKk89pxu8UydZojGMNqm6n-9iC5uU_GXNAc7a8flPzvZBSecK_mLW0fP_E_mbzH7bbKUfgIe2YX0HoGdBp2un-J0eSyB7bz65o7NPR85xJz-ctFStgfWbd8FuGDcQXsr3iIGfftQnxRGnOgA8QIIBI950GkKYZ6YsG0S1K2ta2w8UnM1D9Ph47VBDq92l_Wl1rQ3ih-FjcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید «ستاره یک» منتشر شد
🔹
«ستاره یک» اعلام کرد نسخه فعلی این برنامه به‌زودی غیرفعال می‌شود و کاربران برای ادامه استفاده از خدمات، باید نسخه جدید اپلیکیشن را نصب کنند.
🔹
از این پس دسترسی به خدمات ستاره یک تنها از طریق نسخه به‌روزشده امکان‌پذیر خواهد بود و نسخه‌های قدیمی دیگر پشتیبانی نمی‌شوند.
🔹
ستاره یک برای کاربرانی که به نسخه جدید مهاجرت کنند،
۵ هزار امتیاز هدیه
در نظر گرفته است؛ امتیازاتی که در قرعه‌کشی جایزه
پژو ۲۰۷
قابل استفاده خواهد بود.
دریافت نسخه جدید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663496" target="_blank">📅 17:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0347f806.mp4?token=bGssg1rWBbg98Q1ujtYyfCKvmNgHjUntwFWqOQjQdxlrQWBIqzYKcZnRTyTmmn_-zv5EcDGC9PQehz8gTiTUaewGXHNZ1p3Dld4wVZWNflRnbXI6uQTKXJiOn5kJlAVRLWdDg9GH7juLtofXpojFDv7XfonQwwazN76uDA0awhiGilrlAG7gtpHr09f_s4HyYFyeG4WLeajPTzfsXbm6ZlMpKz5HV0Jd6TD8saloEL4B6ErhYbTIzpZS2o7E6OLc0_0n9SmNGo-WkR676ZA9jV58MPMYqhOFqJS33CAU4crzr1B0LE143C6nfUE-rVV3dv1kG-FPiCV9exOIzT47vxJq4oCCZmUPvuDFwZIsElwZXJmskLQ6JZvhrShVGXAptPCIYRw19QpSM5nMFlI5zEE-UEuEsKRz_Dh-pquYeptokmNVcaQMJG3aZ1YMNeVR6oh2kudUxQOxgsema7p2ZgvN-mkNfRaWOLmaazLednRu63f_8T-SyJ4oXltYt-ub5srWXZufCb8tYyEQcQLaUfU2SEgnwTThgeFRtYegRVIuPKl-ccZ5uh2atLzxB6wuDeWGitHGOPt_GvTFX4_7AbYhH_55gS0FQLda1xB1YN6KqOHHqSTXeze6H8xZXWgBxhtJt8WB06wDR2eH1knA4An9VGf3ypMFcKlzl10irso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0347f806.mp4?token=bGssg1rWBbg98Q1ujtYyfCKvmNgHjUntwFWqOQjQdxlrQWBIqzYKcZnRTyTmmn_-zv5EcDGC9PQehz8gTiTUaewGXHNZ1p3Dld4wVZWNflRnbXI6uQTKXJiOn5kJlAVRLWdDg9GH7juLtofXpojFDv7XfonQwwazN76uDA0awhiGilrlAG7gtpHr09f_s4HyYFyeG4WLeajPTzfsXbm6ZlMpKz5HV0Jd6TD8saloEL4B6ErhYbTIzpZS2o7E6OLc0_0n9SmNGo-WkR676ZA9jV58MPMYqhOFqJS33CAU4crzr1B0LE143C6nfUE-rVV3dv1kG-FPiCV9exOIzT47vxJq4oCCZmUPvuDFwZIsElwZXJmskLQ6JZvhrShVGXAptPCIYRw19QpSM5nMFlI5zEE-UEuEsKRz_Dh-pquYeptokmNVcaQMJG3aZ1YMNeVR6oh2kudUxQOxgsema7p2ZgvN-mkNfRaWOLmaazLednRu63f_8T-SyJ4oXltYt-ub5srWXZufCb8tYyEQcQLaUfU2SEgnwTThgeFRtYegRVIuPKl-ccZ5uh2atLzxB6wuDeWGitHGOPt_GvTFX4_7AbYhH_55gS0FQLda1xB1YN6KqOHHqSTXeze6H8xZXWgBxhtJt8WB06wDR2eH1knA4An9VGf3ypMFcKlzl10irso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تأکید کارشناسان غربی بر اهمیت هرمز برای ایران
فواز جرجیس، تحلیلگر مسائل خاورمیانه:
🔹
تنگه هرمز برای ایران فقط یک مسیر تجاری نیست، بلکه اهرمی امنیتی، نظامی و دیپلماتیک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/663495" target="_blank">📅 17:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a8e8128b.mp4?token=mKiStlOuULD7v40WxeHkhiP_oCkiTleZIjGS_mkm0ItMUNaBhmZAei-pVOLR8qJyc-UdARcOp-Io-f9gFyFAC8T_Ac0UpVFG3Y7ewt2OjoCk66hI0SGE2Wij5ss_CNoJep9-qMGtPURuS2fkfOdLsCDU_OACUCSuw6N7-xVVCbPp1fOKxCWcqXzeOvasNypGLM3JUFpHOzJ9pDaWAzYefU0hjRWzl7F2E8YoP0gt5h_6ZrPirAJ-QG3rjytOVRgtnOSbtQsu2sCUKXNzWwsiCn6wzbTH7iqEKejyYdnhiO-mcAp8fh25aFvSv01jhSBwppXgnmz9cLb71L4sRWSfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a8e8128b.mp4?token=mKiStlOuULD7v40WxeHkhiP_oCkiTleZIjGS_mkm0ItMUNaBhmZAei-pVOLR8qJyc-UdARcOp-Io-f9gFyFAC8T_Ac0UpVFG3Y7ewt2OjoCk66hI0SGE2Wij5ss_CNoJep9-qMGtPURuS2fkfOdLsCDU_OACUCSuw6N7-xVVCbPp1fOKxCWcqXzeOvasNypGLM3JUFpHOzJ9pDaWAzYefU0hjRWzl7F2E8YoP0gt5h_6ZrPirAJ-QG3rjytOVRgtnOSbtQsu2sCUKXNzWwsiCn6wzbTH7iqEKejyYdnhiO-mcAp8fh25aFvSv01jhSBwppXgnmz9cLb71L4sRWSfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصویر پربازدید از موکب تنگه هرمز در ضاحیه جنوبی بیروت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663493" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFqYgsFkGaytdsqABJuL6MAsK_omJ429tqbNHby9dvOyhyA2hhNY5uWFBhO_e5fenzEV03u2ggbKLWb_UCEDbWtZ2owsN8sYWibt-6zsG1DZUm7UcLNYjiItS_PqHfkmqa2pI2H4UisrLRycgJ36YjA-VQwYxyeJ_J3_k94DpuNd3heUV58yMBd_m-GkVxwa1myYaZgVIX-SNhdHsIsz_-V1RfP1sY51OYpUVmMDjcZOS4o6ycMAXfb_MQaiETA3I-uS3shIq_6gWzFEloXHwkIyR8Jb6ROSTxPO1gkkU09Z7Y7JKPAZTTNFnKAevV5vv6extDtNwKK5rR5HAUSxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
وزارت کشور امارات: وضعیت در دبی عادی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663492" target="_blank">📅 17:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYGtBt6E5pe2CnkkSHTnImYR1xLCJWrnyiKD7owdlxURCoPg0kpDOuXjaPC9nEOJ_pDy49H8pM99FUMGskgCX8-oKZE-QPYDPgz1eORPak8LMrlxPvaL22q-CHitwqKvbPbAA-Bty5QgCAt30YrTquYg21BWlBJz2wY_2ERJaNlqX7uDqTnPh6LwD3FtHHd7wzmqAVCwS6ly5CLtu7jIj21v4brKIWbonBI-eahLuV4cR3MrCeYOJIEli0-i2fjLp1GnwaArIdIPowamx48KfohIqCKV5MRDIP7jT_Rrsf5J2a3-s6KqHS3K_PDJVGGKYUUv6ndlYCm8DsxVzdbsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگاه ششم ایران در میان بزرگ‌ترین تولیدکنندگان سیمان دنیا در سال ۲۰۲۳
🔸
چین با تولید خیره‌کننده ۲.۱ میلیارد تن سیمان در سال ۲۰۲۳، با اختلاف فاحشی در رتبه اول جهان قرار دارد.
🔸
هند و ویتنام، پس از چین جایگاه‌های دوم و سوم تولید جهانی را به خود اختصاص داده‌اند.
🔸
ایران با تولید سالانه ۶۵ میلیون تن سیمان، در رتبه ششم برترین تولیدکنندگان دنیا ایستاده است.
@amarfact</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/663491" target="_blank">📅 17:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
۲۲ خدمه ایرانی نفتکش توقیف‌شده توسط آمریکا، در کراچی تحویل مقامات ایران شدند
🔹
آغاز مصاحبه مجازی دکتری دانشگاه آزاد از فردا
🔹
روس اتم: متخصصان در هفته‌های آینده به نیروگاه هسته‌ای بوشهر بازخواهند گشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/663490" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfiOMnBnds5JnwTZ9rlOgT8Hot3A4O76i4QRMWd_IEnz26HlM0Ge14ZUSmDSca6CasHrHZit4VGKcDQ3x1mfbvRwGz8zK9-naJ-vornk5jyznhRn4NdnFkDnxlbUUCcK4YybOiREPSsRxb3QenLn3jDKHd3MEGFSm8vxqfh6ED44F_Hb0IFdkSJvBEKM7YJf4bJIoYIZ1sYADlRbjAL0Tge7Qk1Yrsaef9XPSOxmHT-x53wHJKYTdgKXI9yMRz4ArsUCo_aZTVbVR3lRdHOA3O2TPBzrEoWbuoUAoY4U34JKj99m4-qI38IyN45yl4tWVNHgeKMkQMVgpQj1fMk7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر فدراسیون والیبال برای دیدار امروز ایران مقابل ژاپن در لیگ ملت‌های والیبال
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/663489" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc1o1iNQoznTko11qMB6AgCOYxsB9dv5JaIFZBhHt_8kKpktuXynTOau20ULDVxA-9U9H8VNTl-s3YL6rZOJ1e0pRw2HZzM87trDSP1t9Bkc9m2joY3v3K_EHy2pxxikTG4-En4p6T3FNag0tWwVl_cXA5-CBX2wjR_OZvyMlwcn6iLWWh2mGjMma4N6P7-iTkEdzNsE1cczV2Lsvyg7Mw32zlShFlWMvRbBd6ng7DxWAn0_4be701xCmXr85d3u-1rrnPqv2tFfo_goH2bnCAr5sopVm7paA5WglyqtgK6UVVL-kJw1yKeQt-O3PwTUvj48ihmlcMoGH8hRaRBeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شنیده شدن صدای انفجار در دبی
🔹
منابع خبری از شنیده شدن صدای انفجارهایی در دبی گزارش می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/663488" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔹
شنیده شدن صدای انفجار در دبی
🔹
منابع خبری از شنیده شدن صدای انفجارهایی در دبی گزارش می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/663487" target="_blank">📅 16:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-0aoX20zgB_ryUz2BJekIig0Sm9fI6yyFb7gwnnbzNh0WIXvUk1XNnjO-uVOI_ilPvjL_M0KrLVMgABg8JpJpDpPJrgcY3gHo2LMEvUJYvbeL3FoU5r10Zmz2392SRS47piG8mqSdYo7QVpaZq-SeqXzns41d-tJ9IZgDvzgAcjw856oLwQHyutcMBvYySPE40PsYSIZNiCzG-28M29V7OY6tj4Brqz_yqIeI_SPvhC3x9U94krKqwlfxTi71L-mjO3W6bBRehi3DMnTEt24SehiCagzUC0-9t7IH5PCXbeDcAYKMcjtNFzv5EvjAqWjl5aZUQqCNee2kYk0i8OYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه بیانیه مشترک کشورهای عربی و آمریکا را «طنزی تلخ» و «نشانۀ درس‌نگرفتن تجربه‌های اخیر» خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/663486" target="_blank">📅 16:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a2e0060c.mp4?token=JJO-6IUp1csnjtVd98IBINHCNDo1209dILmtre-DZRxsMnbzZdwKaGZksksyhb1mJX1N1GizUpGFH36fPGl5g-GQgYpG-_1kRK0osqvowbX5J0wn37l9SFNXHDyZ--nP0xu60jGkHGfMB-SDITRLCWusiXz96B2HQ83qkbmXSye665fHYv6GU6JJ_7Ii9n3miYO2yCI-YJU6lsH8r8HmiTF9FLLSqkff-n2lcw3BJpIDDGpn0U1VWClP9wGqWlhrDx_O_M6xYJqiSNpsw73mhw2gSEBHO5c8o4FZd5eJH5DaYgV8oSFkENsa8dPYH7tKp4evDSQmRNJ139k84fTbpCyVwf0XgUa0ZkJs3X_0uNYISFkYjqYCNnMPGCl_Qd7XEHZrpw9GeIH3JyM-uykRSPeE_bVm2Yt4lrXRXXC3QA_ckEBrjLyrOT9M3qwGIxc8c9-NDVcHG8fymZh6UUtbZWKbRPUWt_hvtQthEzVEAj0hTm6JySqw77weaM5BSMo2fsPg56IIbByXkIueb28EfUBC6uflcSGx3mnhgsvvJTWLt6ndej7sqso0zjXuSGEqD4E7VGDHEf-Ha-737I9Rd5b2hdxghAPBNlZsEMg8uCCbRDc_Li6bY5Xr2a3JYZHOK6EBJIzvMVIe4YZTCfX6RynoS5TO8WvX-iZhRoWUuuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a2e0060c.mp4?token=JJO-6IUp1csnjtVd98IBINHCNDo1209dILmtre-DZRxsMnbzZdwKaGZksksyhb1mJX1N1GizUpGFH36fPGl5g-GQgYpG-_1kRK0osqvowbX5J0wn37l9SFNXHDyZ--nP0xu60jGkHGfMB-SDITRLCWusiXz96B2HQ83qkbmXSye665fHYv6GU6JJ_7Ii9n3miYO2yCI-YJU6lsH8r8HmiTF9FLLSqkff-n2lcw3BJpIDDGpn0U1VWClP9wGqWlhrDx_O_M6xYJqiSNpsw73mhw2gSEBHO5c8o4FZd5eJH5DaYgV8oSFkENsa8dPYH7tKp4evDSQmRNJ139k84fTbpCyVwf0XgUa0ZkJs3X_0uNYISFkYjqYCNnMPGCl_Qd7XEHZrpw9GeIH3JyM-uykRSPeE_bVm2Yt4lrXRXXC3QA_ckEBrjLyrOT9M3qwGIxc8c9-NDVcHG8fymZh6UUtbZWKbRPUWt_hvtQthEzVEAj0hTm6JySqw77weaM5BSMo2fsPg56IIbByXkIueb28EfUBC6uflcSGx3mnhgsvvJTWLt6ndej7sqso0zjXuSGEqD4E7VGDHEf-Ha-737I9Rd5b2hdxghAPBNlZsEMg8uCCbRDc_Li6bY5Xr2a3JYZHOK6EBJIzvMVIe4YZTCfX6RynoS5TO8WvX-iZhRoWUuuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کاش از ایرانی‌ها می‌آموختیم
مجری مطرح عرب:
🔹
بینندگان، شما را به خدا قسم خودتان مقایسه کنید، ببینید ترامپ چگونه با ایرانی‌ها رفتار می‌کند و چطور ما را خطاب قرار می‌دهد، ای کاش از ایرانی‌ها می‌آموختیم و اینگونه ذلیل نمی‌شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/663485" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2TkSF6ou1Ur2aClDg-t3ZOhpHh-rq01sn6wShzB1qHC67bKm-t2zoSeXF9cqrwjfSaiZFFAJT_wxnvbDfMG7Cd2KOOh6A0Clt1eVQJ4FhM0LB3zJ94i6dymkXPve5SYSzblcGnAlCvjZHtGEpmObCg8j8qaVOR8kqq-r-grtH4jr0cOZbT-ZW98eTM7ciVYvzPOfRjuzS3nbTEKLSQTFm_UUEnwIbbZ--pmP_R7AVIA1E_-laUpkG2ZbiUt-xEddqOIX30OSaGKkLoGcT86dpXFVbINCFE5J5waltDVjvaw2mPuKOuXdStyrQZbEmnA9uTUaLXgkQrLXa3KysTivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر پربازدید از موکب تنگه هرمز در ضاحیه جنوبی بیروت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663484" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
ادعای پرس‌تی‌وی: یک خط ارتباطی میان ایران و ایالات متحده در تنگه هرمز ایجاد شده است تا به جلوگیری از بروز حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، کمک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/663483" target="_blank">📅 16:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkvdCbqC2C9bAOupC6LReUy7ut6_RTlEbkzE55KIfKBhqQWM9yd65gZnOOyWj6UE3eniGZ4gB91F4rY-pD-A6omquRg8pJt7VBXtWtYDxFVpEP92nn8k_Nwv4TjhGTqRT1kAa5XP5X6bLdNK5hDuB2O7foSbs4B1hXceu48jxKV068KfOC8LRcZzG80v0NTeAf4ksbW6EmERri40LbTD7F27j-bKayFA0zCryPmrMc9hEI3tBO5oOa0H5P-kT8IF3uQvAVUMobK-ZBgSINwL3jrUUAg1cOyz3OeZsuLBbnKt5lkxiA5sqj2I7WHnSS73MRBHiwWRaQbAE_TepGKruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی خطاب به سربازان تروریست ارتش رژیم صهیونیستی   فرمانده نیروی قدس سپاه:
🔹
سربازان متجاوز و تروریست صهیونیست ، کمتر از ۴ روز ۱۰۰ نفر تلفات دادید!!!، اگر با پای خود از جنوب لبنان خارج نشوید، حماسه سال ۲۰۰۰ بار دیگر تکرار خواهد شد؛ همان سالی که…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663482" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔹
تلفات زلزله‌های ونزوئلا به ۵۹۸ نفر رسید
دلسی رودریگز، رئیس‌جمهور موقت:
🔹
درپی وقوع ۲ زمین‌لرزه پیاپی در این کشور، دست‌کم ۵۸۹ نفر جان باخته و ۲ هزار و ۹۸۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/663481" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔹
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/663478" target="_blank">📅 16:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55fc979037.mp4?token=tHkvIqCtiL3Mk31chjHNkNxJr3kZKfL42OsSjj7mCZZEa7pr8H3MCBVc2tDeg8tb_UqOmdTM8lv2a_W5Fbj8RXTAamhqsUlpGaTzQdzrWc0S9BJscVgSO-XVe85KWtGDJX9CHQDJDxAnD-zgCn9cvvZEbq8T7PbvAGKS4ExmHFlf5Ycj0kstMoJhoDFPujwbS2h7A4RSgKxdQo2coD0B3tRQTulROZEe0cWf9yypdgm89D23XR-N3sr1BkSFRVlWcy2CeTw4SdtdCDCmNgtxu-3SUGDgec9NSi2rqapdN_mroyNhhklxc2kATrInVBxmm40NjK-1a2mdlZx0jdevBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55fc979037.mp4?token=tHkvIqCtiL3Mk31chjHNkNxJr3kZKfL42OsSjj7mCZZEa7pr8H3MCBVc2tDeg8tb_UqOmdTM8lv2a_W5Fbj8RXTAamhqsUlpGaTzQdzrWc0S9BJscVgSO-XVe85KWtGDJX9CHQDJDxAnD-zgCn9cvvZEbq8T7PbvAGKS4ExmHFlf5Ycj0kstMoJhoDFPujwbS2h7A4RSgKxdQo2coD0B3tRQTulROZEe0cWf9yypdgm89D23XR-N3sr1BkSFRVlWcy2CeTw4SdtdCDCmNgtxu-3SUGDgec9NSi2rqapdN_mroyNhhklxc2kATrInVBxmm40NjK-1a2mdlZx0jdevBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
محبوب و مردمی مثل کریم باقری
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/663477" target="_blank">📅 16:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idoFQzU-NtSTWXSYGFFyYSf3gGwaEA3T3YdgHqSNTRG_YBu9YfF0rQ2yFLF6PV7THzWViQXwBlgfbwXg7F_fas0rkNBhdwMfTcrZcHnzfXmI_ASOnOO99gD3A9H35oO8Hx-YOfIUpHEbzqDLVvNPq48Z-a31-xifyy4hMjhvrddGHcbYm9Tagh2GXY0TrJT5rNtpRB9swrjCwE8pakRBv-pz_Dz5h81KNovJgZE7xjt0RE2akmj97yzxrmK77_jjpq9kBqIez_L7zZvwgKLjPRK7Q-JRfd3Uig6s5MFnsAQ1c3qbnXQ20kwjBOlZwHTR1adKZHF55HzIHK7pe8-45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیش به مبادی مجاز «ته‌لنجی» اضافه شد
🔹
جزیره کیش به لیست مبادی مجاز ورود کالای ملوانی (ته‌لنجی) افزوده شد؛ همچنین مقرر شده است تا ممنوعیت‌های اخیر در واردات لوازم خانگی از طریق رویه‌های ملوانی و کوله‌بری، در جلسات کارشناسی جهت بازنگری و اصلاح بررسی شود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/663476" target="_blank">📅 16:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d190b96eff.mp4?token=ozYtYRDBsadMErhXf5USSLqFYlS-CDIJwjC3ei-k52Khll68ODPVqQfCUWHIRPkz6yi2ZjGPWDuxI8ngvPiaTNohw69DufqiyBb0rXQLUTFsHq9_sq7RAXxi4mluvJ79C_W5sSEMzVtBO2IqNjSV7VOhdAWr5e8d0naqBTdoaAJbzp3V0bp2DSVZKyRERmZzcNCxemThg0w9Mu439qEP5Qf9gB_B99r2G1jqfV2uixwFqTOMGOzxfSTfbc3sp_wcNSQOzeqzxZEyHCEKzmLyk4CBJEkXme26cv4-3NzakllWZ92PaFq9o7hpEJSpPRPwOejTtyUOxneMIA68tmYwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d190b96eff.mp4?token=ozYtYRDBsadMErhXf5USSLqFYlS-CDIJwjC3ei-k52Khll68ODPVqQfCUWHIRPkz6yi2ZjGPWDuxI8ngvPiaTNohw69DufqiyBb0rXQLUTFsHq9_sq7RAXxi4mluvJ79C_W5sSEMzVtBO2IqNjSV7VOhdAWr5e8d0naqBTdoaAJbzp3V0bp2DSVZKyRERmZzcNCxemThg0w9Mu439qEP5Qf9gB_B99r2G1jqfV2uixwFqTOMGOzxfSTfbc3sp_wcNSQOzeqzxZEyHCEKzmLyk4CBJEkXme26cv4-3NzakllWZ92PaFq9o7hpEJSpPRPwOejTtyUOxneMIA68tmYwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر هوایی از مراسم عزدارای ركضة طويريج در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/663474" target="_blank">📅 16:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26aab3e5c.mp4?token=Aw1IByCHrWN2lQNn1C4_AAqeBa9xCvIefCTnXXbTBwrRT8WCbNLY5dFruXQ_QLAaBFVbPz63wYItyWstspUTEQmWx0LC4Qs_BQcHZcGA9Hz3x96fbBRPeoTKLVrdBsXmpuw-PgeCeFyOJ0CCRcgF4sNl5hpba4_p5R3YDUyDaaU24eGT_zIXh7vQKuXpI6t2H6sa-rjNNQQraPYr9pTSbfAwB_kYni5P6tDMO99ZwTS08q_ThP8vWC1_ArynTTFIJWBEEPNDYtmhnoFX2L81v8AAUSsa2LzYxboLFcyvSW7n0vvG72ChLO0q1feR7afMmtMkBWbzs2UvEKaf9fLcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26aab3e5c.mp4?token=Aw1IByCHrWN2lQNn1C4_AAqeBa9xCvIefCTnXXbTBwrRT8WCbNLY5dFruXQ_QLAaBFVbPz63wYItyWstspUTEQmWx0LC4Qs_BQcHZcGA9Hz3x96fbBRPeoTKLVrdBsXmpuw-PgeCeFyOJ0CCRcgF4sNl5hpba4_p5R3YDUyDaaU24eGT_zIXh7vQKuXpI6t2H6sa-rjNNQQraPYr9pTSbfAwB_kYni5P6tDMO99ZwTS08q_ThP8vWC1_ArynTTFIJWBEEPNDYtmhnoFX2L81v8AAUSsa2LzYxboLFcyvSW7n0vvG72ChLO0q1feR7afMmtMkBWbzs2UvEKaf9fLcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قاسمیان: مذاکره‌کنندگان وصل به شبکه یهود هستند!
🔹
اجازه مذاکره صادر شد تا منافقین به مردم معرفی شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663473" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFX-zTfqNVmWKJxJ1-uSouTVsxraTA8FpQCSOHci9Ti0bJdKsCreUcrHiaOCEofwZ-uj9usNQcyLWleHNSfCsEAxXBAotUTHHoeGjL20pMilvUu9efF1nC1QIJrJ-RC065GUnkuX8I33MZbbTKBaefu5yyjuepapbqIfgW_parrEhSsyzOGPbvvuiW2w9F98EVpNFLpQiCZ32JWwqyb4ZMngDrKhcABkTh-plT2H8Cp0KO2whk0KmCe_9mJy-OvYtJW7q9zB8J6xkdX1tJU6UjuswplVbYmWFrFwgoNsN0mtGzD2Yzftmb_6YpDWqViVeYP0KTDO4nqb7Cxi-LAETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کارگردان موش سرآشپز اعلام کرد که قسمت دوم این انیمیشن هرگز ساخته نمی‌شود
😢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/663472" target="_blank">📅 15:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggo2mR9gv2PTmk9y-TrAjq3dgaCjihGYajdEQYcxu1SAT5IBGl74tv6YL8i1wJok4jASct-ZkULJ91rA8dRwdSd_-9bTy0C3MSAdfKlJlNqBPDm0IyV2qiEpcFI2p1ZrMdgK0vxxqlzyqpQMvKL36ZfioQbcINXnnwmv5dhy82Q1pG5A_qq8q37_QUmkjIjEhg9THihWZ37zCOH55dN2PNf1MbuJzj9Sptx2pUHMS9NsPDK2JdEFQZeOxvzXxlK8rOZ4NmXIXvt8Sah2lAXaDqSde9d0lYKkshDHk5Czsufi_XhcxxKaoP_nQwkkvOvFK2IV6GF36GEvioXCxRqQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663471" target="_blank">📅 15:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
نیمکت‌نشینی گران‌ترین بازیکن مصر مقابل ایران
🔹
سرمربی تیم ملی فوتبال مصر در دیدار برابر ایران قصد دارد چند تغییر در ترکیب تیم بدهد از جمله اینکه عمر مرموش را نیمکت نشین کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663470" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a6136739.mp4?token=t_auHjKYjpFMUagc5tqCoKVE5g_pp9GdRzwNeHuCDlv6bg2KbKWuTIhkPvlW5jdHYJ4sSz9iecPqrPHpn0Jih7bBoO0iP_H0CdopifLfkWuBu6DxGNXiT8XRfYUK1S53OqrlAvpmAi08J_5VZCqgxURcdt2MoGcnYvnXkvCTRzO1sdUO5sLpmT5zilHkA3EcEnjX_njFvzuJ9jOb8w96ILq9i1EIsght0Ywiq0S1ZQfFSAGUrsKusyYjkt2lM9G6C0BBgVh-XURgAq5VEHtFGDPqM9C2eSf-94bJYgM1teb8sZCv-O9KFJ6LUTgD-uImW1E68gv49ILULsP39KIi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a6136739.mp4?token=t_auHjKYjpFMUagc5tqCoKVE5g_pp9GdRzwNeHuCDlv6bg2KbKWuTIhkPvlW5jdHYJ4sSz9iecPqrPHpn0Jih7bBoO0iP_H0CdopifLfkWuBu6DxGNXiT8XRfYUK1S53OqrlAvpmAi08J_5VZCqgxURcdt2MoGcnYvnXkvCTRzO1sdUO5sLpmT5zilHkA3EcEnjX_njFvzuJ9jOb8w96ILq9i1EIsght0Ywiq0S1ZQfFSAGUrsKusyYjkt2lM9G6C0BBgVh-XURgAq5VEHtFGDPqM9C2eSf-94bJYgM1teb8sZCv-O9KFJ6LUTgD-uImW1E68gv49ILULsP39KIi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تلفظ اسم بازیکنان بارسا توسط برادر یامال
🔹
به لواندوفسکی میگه اِلامانوسکی
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663469" target="_blank">📅 15:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IY9O4xr28q6rkV9Srz615bGa8tswJ3bb05NljcyX1sJum6hebLmmv8Pn-L4rC4VAAoulJgY9feJbTQawAUU6wM_oIRxadSi6GKbLvCJOvPkYcTNPYsRR7VSNjDXbH83Tr55POkipgeO21lNeTAeq-GxtslF90_udoTkSLu3W91ce_V4oN8o8r4fJWPG-QMo3eQmEDCg3cWQUk_gk2Nh_w7Rtq_BMZBve03JOMAmHFx2h-Nk0G59MRNCq7kdeyV-wsDLqUtOrZl3pPL13FPYf7iloR8cIwkit1BHqqyfXsR0PykbjEut99ludnQuobCsosYC-AAXdDo4mDhs-cElexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivcR9OCj35uCHA7K9tN9cIju0_penT7RLjfUAo9YtEjw2FnVezFprD6we7RwFsr82Dor6_-TOWsi8a0ZOSiCsJ4278TuZjP5x0ymlJZL-auztXg3YEWxlNotMHahsWTfYV-63yw9bL_IdvstcWf4aH6_ynV3kpmzwSvGIRTdaee5veX8nxvUM50cGNgAhuojRCCYtm-tij0Li_mQ82VqSzarAr86vV5KNhQsOJk_QSQDy63e7QzL7zxC5UpESl8q7vf9lN0uTCsSEIggLAc_JeGklYHwlvOAFfw7PYJAcnkn4fLfFKpgGULiE8KQ7EVKqWe5Kc66MGBFA0fGDdcBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAWT9xtaKwTKrAUSL62tTqjZqfbnOxhLRQFY7f6TFE8-MX6kznruHkbaFhPUvqmm2QOtKiZT3Hp7TK0OKJLuUY2GB5G6mtNEzIPZ1BF861N8RM2d9uy_GHeA1IgOwC6fV1vyQr358pZIjQBcYNwMswpfrhSQ7TKIAeD_MZ1ZYVX0BwaORO1I2EO7GSfWMMRaZ_VyQVXSvEZTV_X-8XBn5R9z_de-a08hhTpX9kkToq6IgHcQFoSbVJ7BTqz3PmJGMvUrodUEkEaUsk9_By5-QNsR1U1jy1SfXXp8JN-O4pyJmOh1Hd_pjecIoYJt9c_1gJgPCy7hbjGKg_a-QoO9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcNyrEGKtoOA9i167gxLp4DdFauSx4mcFTVPtZoi_TspcmBrY84zAz-baXdISgSzz1ArXkYKY9L-WJnriI3W-uNUET-b7-J3LVpSgRPhh2Z9N2zs7XIvNALUVnwbHRDpxtYuYZofwCFgHdHMjo0HkeDsFQVET43N8VpvJYqDLH5SDS52zx3wwU0rldajJ027aIpezx_pCCFFREnGxfj9In9KG_iGLaaIztN5GWxxCUWBOKEuEEWo-_ZoxbA5HNrwcCeslYl-6PmBTX14w4ro_oDujDVCyDfy-P5gjXfMoCvZ4oOUIwEnC7oyBOdgxvEDOmnNXZoQiPka3bvVSJ1pZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
قیمت بلیت نجف-تهران و بالعکس چند؟
🔹
با افزایش تقاضا برای سفر به عتبات در روزهای گذشته به منظور شرکت در مراسم تاسوعا و عاشورای حسینی، قیمت بلیت هواپیمای تهران-نجف بسته به نوع پرواز، میزان بارمجاز، ساعت و روز پرواز متفاوت و از ۲۱ میلیون تومان تا ۳۲ میلیون تومان فروخته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663465" target="_blank">📅 15:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41b8f262a.mp4?token=pJeMS9IokKm47iQ3cmmJRjaHz42bJ_B-uq2Y4M9o4olXLHGjhQEel5Lc6zIxAU2bg-YxpNLv8mLwQ_c3sVt2dP6hA5pVcB92vCwIqm8431wFRVQZYHJoKXNTxuwtGWlJyMGUcv76Jn3x-2VpGf_O9lqKHKHzcZ_r7wy8ybha2T05hYMu5bJ2BPCNtdM2WPhzqKsa67bkkHKBGqPo1LXDlz2VRSWxvouALXHC37VIGz3yF-BTDvuuHPLTNPAF-rrKETXWdZ3_KjfRJZz0QZ_xcdgX1vxn-MqDmtDVRGhnNHPjs7eBF9Q2OCv_MKytyckQ8dYlfPjlcXBn7-j1muAUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41b8f262a.mp4?token=pJeMS9IokKm47iQ3cmmJRjaHz42bJ_B-uq2Y4M9o4olXLHGjhQEel5Lc6zIxAU2bg-YxpNLv8mLwQ_c3sVt2dP6hA5pVcB92vCwIqm8431wFRVQZYHJoKXNTxuwtGWlJyMGUcv76Jn3x-2VpGf_O9lqKHKHzcZ_r7wy8ybha2T05hYMu5bJ2BPCNtdM2WPhzqKsa67bkkHKBGqPo1LXDlz2VRSWxvouALXHC37VIGz3yF-BTDvuuHPLTNPAF-rrKETXWdZ3_KjfRJZz0QZ_xcdgX1vxn-MqDmtDVRGhnNHPjs7eBF9Q2OCv_MKytyckQ8dYlfPjlcXBn7-j1muAUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در آسمان روسیه یک ابر رنگین‌‌کمانی دیده شد که شباهت جالبی به نقشه ایران دارد
🌈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/663464" target="_blank">📅 15:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a549d6b41d.mp4?token=aqMfvyQJP7x7DseEudAYJK6CxiTK7SUkj2Jp3sfwzQ_ZIWNSbXJXbNT8wGVhUFZw7nqRrYlTiJRd59FWPKy-ba1zAzfLwXwZ4ywsh3CJXQd3cd4C6XSUpV82JRmsUETFYTXIsDjtuXVu868bbjzx5_UEGAJxS8D8iWJiwAaWM7VgWdcFs_vtGFazN1La5U1iT30fYj7XohnS2dE91G-Y9ZIfJMsnnm8S9GCzx2Po912dMGX6Y1_duH4eeYl_Z9YBY3UM1FdoqUcC9wnLH1rSd83ovPLOu7x5ONVJL9HEOqKlHnC6WP8tclZS2r8sqx675zj6QNGtRx9T1olgwE50fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a549d6b41d.mp4?token=aqMfvyQJP7x7DseEudAYJK6CxiTK7SUkj2Jp3sfwzQ_ZIWNSbXJXbNT8wGVhUFZw7nqRrYlTiJRd59FWPKy-ba1zAzfLwXwZ4ywsh3CJXQd3cd4C6XSUpV82JRmsUETFYTXIsDjtuXVu868bbjzx5_UEGAJxS8D8iWJiwAaWM7VgWdcFs_vtGFazN1La5U1iT30fYj7XohnS2dE91G-Y9ZIfJMsnnm8S9GCzx2Po912dMGX6Y1_duH4eeYl_Z9YBY3UM1FdoqUcC9wnLH1rSd83ovPLOu7x5ONVJL9HEOqKlHnC6WP8tclZS2r8sqx675zj6QNGtRx9T1olgwE50fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شادی جنجالی سرمربی تیم اکوادور در پخش زنده تلویزیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/663462" target="_blank">📅 15:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/663461" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
مهار آتش‌سوزی محدود در پتروشیمی کارون
روابط عمومی پتروشیمی کارون:
🔹
ظهر امروز جمعه ۵ تیر، در جریان عملیات آواربرداری و ایمن‌سازی ناشی از حملات اخیر به تأسیسات منطقه، بخشی از واحد ۳۸۰ این مجتمع دچار حریق جزئی شد. با اقدام فوری، این حریق در کوتاه‌ترین زمان ممکن به‌طور کامل مهار و خاموش شد و هیچ‌گونه تلفات جانی یا خسارت مالی، نداشته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/663460" target="_blank">📅 15:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGXI1dJDoG3BSl2OwgpnEkED34sHMASIFInx3vKefA0mLAyNcYFCeuJBkCvnbV5yjypzRjCnUuQPaVzVfLYnGl8VPAQeowAxa-DgS8a5jjNvN6zul0CYNuMx1JXBGnAS0AxNSyplZvDzbINZiZIoi_o0LbDglOzP0vQbhn-ZMPRIgCJki2k3a6Q5NyWh1M1BJxQYDBC0P4DTVHl5xfSAglryd5Ep-wxB-jxwjo7X9p_PPAq5CwzH-292IBwJOjiAVvHrsAR27m5m_DNECzH4Gyj69Ftd6HSGHBwIRjh_YwwaRGim0_2NWK2ZxN9GAZwe9jPwJKNC8rU0X20KIXKrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/663459" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74883fc491.mp4?token=uuZDMw1I0L7W3daKjHknfuwUmqsHcWgUdNtXZQEUzTzaMq1WT4K66KoSmhDul1q6K6j4QJZXuhvzoVUp7V-r396wwrXQualAlGHcEJMCaemI_ve-4XUmtKtsC7ray7ap30FB3S98Sx3wUvsj-dcoovUJl1AW8AkDz8qJ6-fS4hLhzNEJ0Ibn-Kq-YV_0zMlrX8DLHqS-WzQf6v4lFEHDAI3y-SRWYI_gHaLEVtoJugAfADZRGIGDHeMDuvSitnXJJZZT27q8nafVWIxZpi9xX0bnd9jOu8jk4dktrx9GzTUdsSJk95YGLmUF62QSnEIeOtclcz8ISw4Kf8zzOTqQ5Q1oXaqOK05yfxQ6QbVN06xwcAmFfi8iHRj8pC4B-Saz_jSEAQtIDhcTEp_Boyuq-0QJTCZSPDNgVAUijPqvEZ2WtlJf2H4PjCSGiBP6xHX-PNFbpmwdMbpaBdO6s9tgbK4Y9WvE7JgXNdpaGxRGF9zFbYDTJ4jzr21iZE2iZuNLLaU7oZ1LLBzDCqNXt0ZcXEM9w_n5_iOovdur274eX9zJj-8Y-S7Ax34PQu-mwlD7hhtghgLpEPj6D7-6_lzgVlWvyrNoLhcjtUQaEK1MZNvYu-M_jEzFueKuEcVPS5TU0Wuw2v1Z_vG2tqx6qe6yNGuFmWxHtP9LEcpHTUocFLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74883fc491.mp4?token=uuZDMw1I0L7W3daKjHknfuwUmqsHcWgUdNtXZQEUzTzaMq1WT4K66KoSmhDul1q6K6j4QJZXuhvzoVUp7V-r396wwrXQualAlGHcEJMCaemI_ve-4XUmtKtsC7ray7ap30FB3S98Sx3wUvsj-dcoovUJl1AW8AkDz8qJ6-fS4hLhzNEJ0Ibn-Kq-YV_0zMlrX8DLHqS-WzQf6v4lFEHDAI3y-SRWYI_gHaLEVtoJugAfADZRGIGDHeMDuvSitnXJJZZT27q8nafVWIxZpi9xX0bnd9jOu8jk4dktrx9GzTUdsSJk95YGLmUF62QSnEIeOtclcz8ISw4Kf8zzOTqQ5Q1oXaqOK05yfxQ6QbVN06xwcAmFfi8iHRj8pC4B-Saz_jSEAQtIDhcTEp_Boyuq-0QJTCZSPDNgVAUijPqvEZ2WtlJf2H4PjCSGiBP6xHX-PNFbpmwdMbpaBdO6s9tgbK4Y9WvE7JgXNdpaGxRGF9zFbYDTJ4jzr21iZE2iZuNLLaU7oZ1LLBzDCqNXt0ZcXEM9w_n5_iOovdur274eX9zJj-8Y-S7Ax34PQu-mwlD7hhtghgLpEPj6D7-6_lzgVlWvyrNoLhcjtUQaEK1MZNvYu-M_jEzFueKuEcVPS5TU0Wuw2v1Z_vG2tqx6qe6yNGuFmWxHtP9LEcpHTUocFLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خبر خوب برای عاشق‌های هدیه دادن
🔹
دیگه لازم نیست برای خاص کردن کادو، هزینه زیادی کنی؛ فقط کافیه بسته‌بندی شیک و خلاقانه داشته باشی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663458" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
اظهارات تکراری ترامپ: اجازه نمی‌دهم ایران سلاح هسته‌ای داشته باشد
ترامپ:
🔹
اگر آن‌ها به سلاح هسته‌ای دست پیدا کنند، جهان با خطر بسیار بزرگی روبه‌رو خواهد شد. اسرائیل از بین می‌رود، خاورمیانه نابود می‌شود و کل دنیا در معرض خطر قرار می‌گیرد.
🔹
ما ضربه بسیار سنگینی به آن‌ها وارد کردیم و حالا از موضع قدرت کامل در حال مذاکره هستیم. ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/663457" target="_blank">📅 14:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
هشدار نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
🔹
همچنان تنها قانونی که بر این منطقه حاکم است، قانون جمهوری اسلامی ایران و نیروی دریایی سپاه پاسداران است./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663456" target="_blank">📅 14:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📖
اگر قرار باشه روزی فقط یک آیه قرآن بخونی...
همون یک آیه می‌تونه حالِ دلت رو عوض
کنه...
❗️
🌿
گلچین بهترین تلاوت‌ها، آیات و تفاسیر کوتاه قرآنی همینجاست
👇🏻
👇🏻
یک بار وارد شو... موندگار می‌شی.
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663455" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ff56f338.mp4?token=MZBVJ0-6-nfPGL9wvHHIyeLZWvTk60viXA2dMdgJq5wPDz_eWsvKH7oV9CcI8wdVsdmSpfAdFovsuDEuzBKWKhO_KH62h1qRvDsd9j0pVdd2Wm0pfjRcuMmB3MgnaTLPez3UgMNDuzSYTtWxjBj9WB9nJB1J7Glx-x-LJyWe_ELuGuwWgDqSI7Cuc9J0AyBIvIZ1AXhR1hkpG9gOTRIyjS4HJDcCL1lcirnY4YkoTi1B5m-Gn3xZTb1aTW_Y6Xn9596c9QGW1NCZ9DebyJbG_LCtGy7USf5Q31tAXUwxruXKXjmBuKjMcIqFmcdFVX3zqARD2c38MY4mh52sJsaF0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ff56f338.mp4?token=MZBVJ0-6-nfPGL9wvHHIyeLZWvTk60viXA2dMdgJq5wPDz_eWsvKH7oV9CcI8wdVsdmSpfAdFovsuDEuzBKWKhO_KH62h1qRvDsd9j0pVdd2Wm0pfjRcuMmB3MgnaTLPez3UgMNDuzSYTtWxjBj9WB9nJB1J7Glx-x-LJyWe_ELuGuwWgDqSI7Cuc9J0AyBIvIZ1AXhR1hkpG9gOTRIyjS4HJDcCL1lcirnY4YkoTi1B5m-Gn3xZTb1aTW_Y6Xn9596c9QGW1NCZ9DebyJbG_LCtGy7USf5Q31tAXUwxruXKXjmBuKjMcIqFmcdFVX3zqARD2c38MY4mh52sJsaF0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ریختن بنزین روی گدازه‌ آتشفشان
🔹
وقتی بنزین روی گدازه‌ آتشفشان (که دمای آن بیش از ۱۰۰۰ درجه‌ سانتی‌گراد است) ریخته می‌شود، به دلیل دمای بسیار بالای گدازه، بنزین فورا بخار شده و به گاز تبدیل می‌شود. این بخار بنزین با اکسیژن هوا مخلوط شده و به سرعت مشتعل می‌شود که نتیجه‌ آن یک احتراق انفجاری بزرگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/663454" target="_blank">📅 14:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXGadWVuynbyS-z8EbZs-j5GJ5nVjdNg8CczV4p0nUcmIewBi8BLDQ8l-TW48WvjxitMwA2xSBSDjPxA6O9H7qSl6YGWTSMaoNk2_Hw5ibRd1B0pTEhVm5eQXmk56dfj4yczMjgpV3rTEuTBWLorUPNaXwrvaL0wKZ3osdS3zHxljPvWHyfy58VESju7Y8skxsNgwzDkTG1pfKCiEFc90M7N9ILBrhS0wXH12Bj9xjfNJltqqxYxJzEamR7kvgiSAEj9JqpkMssfjlHrVAfPeBU-KpLnl-_tbVx0gGzQBig1C-pPAwv4H8oexPluDf8nF-6FuBlNE4dDCcViFvfCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ولایتی: ثبات امروز اعراب حاشیه خلیج‌فارس، مدیون مدیریت قرن‌واره‌ ایران بر شاهرگ تنگه هرمز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/663453" target="_blank">📅 14:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdL7coCgkB0p6nqoKeQiHyGsnWyvooinQ81flO1cphjPJO_sqhmAa5I7-F8zYhdHesDWSrTRvmsnfaDkdtsjBcP6ji7bOozi4WdQCINOYRtEmrmyzATO8jsDtpXzrnm4qbMki44pq8uMMF64dS9v_qRPaC8uu71ZKb2hDxPTTAcfqnav_JkmMlYjnn0ulnErlRIO2wlSkOflE9siQe-2-r48eYlAn2Nznt-hFKNyVnXur4EUD43FRTmsS0mqVQNiV13f_4feNxMeFluHyK_D2mwmZD_nzdB4HDwb8JGLRoMwo3HchCrmWbKMaOPql_WV1PwCYoP_M6LMHfrhd58i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAs1fWlojLMLfOzAjhPCXLWaarchLqKQ20jhCRuOZYTPZtin144-fP-DInYsEsj379Dnq6QmvBpr69aLaEJvKxG0ORLckR4zKA3zMlXQNhFJlgp4V-kDuD0QkLNa09Zn0VaDzf2HcZgHLqaRi3X7H1qPqvtADSp5R7XnaPNeDPuKUCvrobLzLxW74GS6kUunq9s6M36xYNmLGiW-BFtVg0pWQKAEAxPN1IS4rYFSR-S-yZMRuTy5xwSrxKxYjvc7eiekGp_JzDwM0_09RABxuO6rj1OaZhdVS9QuaCN9GJOjYgNb9P-K4g-Ag9Zq6fHM7QqjA0MLxRif-MGJ8DwJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJiyPoaOoYLX0IjlsRLvsGJ0rlxW4Hg5NZ-137Mvv31rQHYcKI1f8Wdg4SaeJ-IDMFe53SIwtfLoxlSdAyhTpLRBieI2VMFVg2-Tf6YlGvj_3ZEewJ0LbFY3cwMhqYY9lpLNxBTaRfEnT8YSRmvWFcCHLG252vIXopO1SdgFZgxXuP_I-fwAWQMwFfERpxTWM5i9W1Owm71YXEV5LKy_awrPtnUT_oz7ysA0nUfVuDI3lF97CiIAYwxv6fSx49L-RGaNWtW3y7HkGFCMGmsd-ZP9rclFV4xPqcD5eEdmqZ0FxWQ2tSKC83OmTJDaE7J-X8vvlGTmuez7htsSbd4m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcQUDa8Y6px6yVnO67QslkLymXWBxsjVsLRnU7oWKy699jAGVCTEyPskECEUZMCYqqvKoOnbsyTTFxq4Sr_b_8EWHB6zsNQxrBJmRfl3I5GFwKIfZBILgZytFfNK13EGRPGjweOcssmySLlk2rlkDJ0nS7tqrmMmM8-JPJb3ZpTi6zN0k81TwxiTgVxBrzz0iwOtRbAvdvO4p8XFpMIhI5OLpAf9Inj7VUsXnv0r2iGWo1-Vz3cmYL3GwcqRDNwgDB9kk6pJndH2Ka87Yn27wbMGGBc1d0n2kmGJleUjh1itLUoaWU9PSpnG-jQ-ZmcDrDMAXUm2GoSIwKtY_cce2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویدئویی جدید از حمله هوایی به پل B1 کرج در جنگ رمضان  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/663449" target="_blank">📅 14:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe0859499.mp4?token=JrgaTwYQqWnvlD3-ap3z5W0P8d88B89aJdTbwN5Pc73egb1bFS36m-S6uLW0vaXEwp0oWEKB8u6GBd-Pp5jfeey3cBysEiK26KzY7HJbFZWTDpEtFnjjqn6LV2lVgUsFv3neY2sG0F-INx55XFA6fkBcmntWnTpzg_yUhKr4mzDk3QWEzBzP6qwo6wEg4HjBX8Hg-QzPP4OlRmYktO8U5Fp9lRIR6se9D3O-ofw5QUTnGjnN7BzYI7D3O6c9ObLmGVChiGbbjt3pU1EBG2Z53aR_9J6CjspJ5mzZXS7jpGFohtbkrGhsFBhs81IAmZQx8h5ZwsnVupjC0M9yg4h_qR2h46nzc9-zyTRJYPRawxp8bLMaHH6g1zvOtA5ibZ6bF5wGQD_ZSG-HkSKWL0JEWPqzgxM6A_yw4DAsux2xo3ThdCNapM8ykO-LUOk-SLJseB_j4dlP5WX6wQ54hSDWz4ETijd4zVjUqv--vuZrQjY50ghDpgjF7tE-pgdBKaPQSIKdhOcmkU_1Lq5IgSGcR5A8gd1alh8g9txgbWfi7nz4ShRiva7QRTOscH_CPhGd0_x4MpleDszGjUiOjrsNX0NEoe4OHo_bXYeuBtJjMack0SC25n0JOX8op411oWgSn0S4t3uQvCJ7vPFvwIBi6PV7PUun9w8apfumTqE_liA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe0859499.mp4?token=JrgaTwYQqWnvlD3-ap3z5W0P8d88B89aJdTbwN5Pc73egb1bFS36m-S6uLW0vaXEwp0oWEKB8u6GBd-Pp5jfeey3cBysEiK26KzY7HJbFZWTDpEtFnjjqn6LV2lVgUsFv3neY2sG0F-INx55XFA6fkBcmntWnTpzg_yUhKr4mzDk3QWEzBzP6qwo6wEg4HjBX8Hg-QzPP4OlRmYktO8U5Fp9lRIR6se9D3O-ofw5QUTnGjnN7BzYI7D3O6c9ObLmGVChiGbbjt3pU1EBG2Z53aR_9J6CjspJ5mzZXS7jpGFohtbkrGhsFBhs81IAmZQx8h5ZwsnVupjC0M9yg4h_qR2h46nzc9-zyTRJYPRawxp8bLMaHH6g1zvOtA5ibZ6bF5wGQD_ZSG-HkSKWL0JEWPqzgxM6A_yw4DAsux2xo3ThdCNapM8ykO-LUOk-SLJseB_j4dlP5WX6wQ54hSDWz4ETijd4zVjUqv--vuZrQjY50ghDpgjF7tE-pgdBKaPQSIKdhOcmkU_1Lq5IgSGcR5A8gd1alh8g9txgbWfi7nz4ShRiva7QRTOscH_CPhGd0_x4MpleDszGjUiOjrsNX0NEoe4OHo_bXYeuBtJjMack0SC25n0JOX8op411oWgSn0S4t3uQvCJ7vPFvwIBi6PV7PUun9w8apfumTqE_liA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تیزر قسمت بیست‌ودوم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای اکبر بابامرادی که به دلیل آسیب دیدن و فرو رفتن ترکش به چشم در جبهه روح از بدن جدا شده و با صعود به آسمان هفتم با همراهی دو تن از ملائک درک زیبایی از عالم دیگری را تجربه می‌کند، نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: اکبر بابامرادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/663448" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
درب فردو و نطنز چه زمانی برای بازرسان آژانس باز می شود؟
🔹
بر اساس شنیده‌ها از متن تفاهم‌نامه مذاکرات هسته‌ای، تا پیش از توافق نهایی، ایران تغییری در برنامه هسته‌ای خود ایجاد نمی‌کند و دسترسی بازرسان آژانس به تأسیساتی مانند فردو، نطنز و اصفهان برقرار نخواهد شد. به گفته منابع مطلع، بررسی نقش آژانس در این مراکز به مرحله اجرای توافق جامع و تحقق شروط تعیین‌شده موکول شده است. موضع قاطع تهران، ادامه روند فعلی و رد هرگونه زیاده‌خواهی آژانس پیش از توافق نهایی است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663447" target="_blank">📅 14:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d333ab5ac6.mp4?token=L6WQdbSfmyQKtFyEB4v8ILbbxvcBKWZNm3sQpG2xApAWAlFiAWJzGqWohSaRRsvpEiQ-BfzabnpSynQ-3IASPSgXBEJJnYHKGCSixiWS5NN4m6lk6fOMCny9Z6Vh7Xt8GMdeCmGbEqujlf_Ee6VsdxhQYH4H73JyhXsL4MRzzeYRVgXTU2OCIBC3gm7_eK0QAdc-LM0Gkh4DFgGhE_CCKENpeuPxUGslEz9Hob6yN6eVy_gNZDiveJsh8nq2acjkf5Yqgb7Sb847tQHIlaZkRgLfpWJy6qiwRgGKRwHPz2Am6phnJHLAEXF3hVN7QPDNLgtFlhhu92JjsoN2mkm-mRA3GdJauIeiDEjhsAJi6honLf_coWMOtjeC-2LSZuuxwI8-a2CJ4xb2gOwg_aEBSzxxf7EHK5bApwP7c-GBvH4qDxaU71k2P3adL8tOmsH69ZFCpiH8kXummQuFfbDqk5HLU4imBEIeS6U0UAopZSOEuKc6gfkNNI4ooLSYkKkCpN9Q4dAvArgRkYqWvfILdm7lnxCUedNPw7dbRsc0U8WpElYIm9oifLYykIUOOaIUXrXHMh3GXiAOvzhCURVUz-yzU3i-7IDm3WIvH0YwM-uoZVmNKaEaqx0TUrmGehEBoHE7a3Xw9ImP66YBYC-9re0sEZ4UGUuXXqlo2ARyf6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d333ab5ac6.mp4?token=L6WQdbSfmyQKtFyEB4v8ILbbxvcBKWZNm3sQpG2xApAWAlFiAWJzGqWohSaRRsvpEiQ-BfzabnpSynQ-3IASPSgXBEJJnYHKGCSixiWS5NN4m6lk6fOMCny9Z6Vh7Xt8GMdeCmGbEqujlf_Ee6VsdxhQYH4H73JyhXsL4MRzzeYRVgXTU2OCIBC3gm7_eK0QAdc-LM0Gkh4DFgGhE_CCKENpeuPxUGslEz9Hob6yN6eVy_gNZDiveJsh8nq2acjkf5Yqgb7Sb847tQHIlaZkRgLfpWJy6qiwRgGKRwHPz2Am6phnJHLAEXF3hVN7QPDNLgtFlhhu92JjsoN2mkm-mRA3GdJauIeiDEjhsAJi6honLf_coWMOtjeC-2LSZuuxwI8-a2CJ4xb2gOwg_aEBSzxxf7EHK5bApwP7c-GBvH4qDxaU71k2P3adL8tOmsH69ZFCpiH8kXummQuFfbDqk5HLU4imBEIeS6U0UAopZSOEuKc6gfkNNI4ooLSYkKkCpN9Q4dAvArgRkYqWvfILdm7lnxCUedNPw7dbRsc0U8WpElYIm9oifLYykIUOOaIUXrXHMh3GXiAOvzhCURVUz-yzU3i-7IDm3WIvH0YwM-uoZVmNKaEaqx0TUrmGehEBoHE7a3Xw9ImP66YBYC-9re0sEZ4UGUuXXqlo2ARyf6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خلبان اف۱۵ سقوط کرده آمریکایی در کهگیلویه گفته پهپادهای سپاه با آرایشی شبیه عروس دریایی در آسمان و مثل یک میدان مین در حرکت بودن...!
🔹
اکنون شبکه‌های اجتماعی غربی‌ها از این فیلم‌ها در شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663443" target="_blank">📅 13:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=Vwk_QUlzPDYE5qwiqFAfKweiLYHf7nFs4-ql8fVbPRQAj17GJQ3nTm2iOUq4KmGD_D7sGaWmMo4_HlpYnluDdGq4Ggyz8H90Bfjhw9NETn2H3UrndYxvRwyc8-VmqoosIBwfwmRROkeqBRVinCFaMDGzi4uIaYxOCKw6F2Pp-jvOx4a1056GMf0rGJeCaQ__DkwyvkBhU5gVTHrtYFkMbuWWu8JdHGdWGglmwoidzv5Q--SaQl1Ar0UyFsjyNrVxIc2ouVPr4LA6S1PAknFMXVIWDMAXIy43bR3EWnX6-JC2ulfcqPkNy1RC8DZBNDkPyoyxjUquvrMYh1mv24Z56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=Vwk_QUlzPDYE5qwiqFAfKweiLYHf7nFs4-ql8fVbPRQAj17GJQ3nTm2iOUq4KmGD_D7sGaWmMo4_HlpYnluDdGq4Ggyz8H90Bfjhw9NETn2H3UrndYxvRwyc8-VmqoosIBwfwmRROkeqBRVinCFaMDGzi4uIaYxOCKw6F2Pp-jvOx4a1056GMf0rGJeCaQ__DkwyvkBhU5gVTHrtYFkMbuWWu8JdHGdWGglmwoidzv5Q--SaQl1Ar0UyFsjyNrVxIc2ouVPr4LA6S1PAknFMXVIWDMAXIy43bR3EWnX6-JC2ulfcqPkNy1RC8DZBNDkPyoyxjUquvrMYh1mv24Z56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663442" target="_blank">📅 13:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df00549cae.mp4?token=EMCanRpzPbbyNzoso4E-wBRWEMHd-6cbS3VsnWdAgaWuYtk_O_Z2U1ZIJgF9ftw5RFPw3UZvZIkHB6MI-_YisFX3pxlHcqpoMi3INyaVkMSbrAY6sePvD-lsoJU8WecMxSkUQVb5CJcuxU33kNFP2QB-sHgzRi61xmDEKsbQhV0XAGUnGU5SscpFA51jFkxqy0meyvwJRwQCgJiNAtW0MmiipIzIGz-NhfX2_s-SaThqPcmNAyw-K3twLvJDkAKXjnvOywU1uPMcmqe-lKbN2-fg1dldZF-937Xa5NNa6QrF7E2mv07yGOb_zegJTs3AmHjwjlVGK5UZ-hjO3XJklQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df00549cae.mp4?token=EMCanRpzPbbyNzoso4E-wBRWEMHd-6cbS3VsnWdAgaWuYtk_O_Z2U1ZIJgF9ftw5RFPw3UZvZIkHB6MI-_YisFX3pxlHcqpoMi3INyaVkMSbrAY6sePvD-lsoJU8WecMxSkUQVb5CJcuxU33kNFP2QB-sHgzRi61xmDEKsbQhV0XAGUnGU5SscpFA51jFkxqy0meyvwJRwQCgJiNAtW0MmiipIzIGz-NhfX2_s-SaThqPcmNAyw-K3twLvJDkAKXjnvOywU1uPMcmqe-lKbN2-fg1dldZF-937Xa5NNa6QrF7E2mv07yGOb_zegJTs3AmHjwjlVGK5UZ-hjO3XJklQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برگزاری مراسم عزاداری روز عاشورا در پاکستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/663441" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
زمان مسابقه پرسپولیس - چادرملو تغییر کرد
🔹
با اعلام سازمان لیگ، به دلیل پخش مسابقه تیم ملی والیبال ایران مقابل ژاپن، مسابقه چادرملو و پرسپولیس به جای ساعت ۱۸:۴۴ در ساعت ۲۰:۳۰ در ورزشگاه پاس آغاز می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/663440" target="_blank">📅 13:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663438">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ2SF5Tej9QTb0UND8KetcIFK7MG5X9vcinvTnD1Z0_XZOSMwts__v9K693MEA24QaBS_RCcAjYwDhp0A5t2AMtEw0P5CGbZVpMy258V2_49GhU1AtZ4a5Fj2Hk85OwoLZZky0UHZPpuFPolYCUxYGvnxSMKZmne78SeE4kf3BDl1JA6AEQGrn9McWvNuzqZaxEsBlUQFhWeFI-51t-0LjX7OInuHzwWekWOIIQ__BH_myWRxgczrULzY_c0ESdG9Hgam4ctRDyVF90SPALAqNn-F0qyfYky0S5vXKSEFFq1JQEBvun_ZxjbaB9UFgCWOLG16y4_Bd0rCT0TylfZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه: آمریکا نیازمند احسان و خیرات برای حل مشکل گرسنگی است
🔹
طبق گزارش "سازمان جهانی آموزش خدمات گرسنگی" «در ایالات متحده، بیش از ۴۷ میلیون نفر، شامل یک نفر از هر پنج کودک، از دسترسی به غذای کافی برای یک زندگی سالم محروم هستند. از سال ۲۰۲۰ تاکنون، تعداد افرادی که با ناامنی غذایی مواجه‌اند، ۴٫۲ میلیون نفر افزایش یافته است.»
🔹
طبق گزارش سازمان "تغذیه آمریکا" «چهل و هفت میلیون نفر آمریکایی با ناامنی غذایی روبرو هستند — و هر روز با چالش‌ گرسنگی و تبعات بهداشتی و اجتماعی آن دست‌وپنجه نرم می‌کنند.»
🔹
البته خبر خوب این است که مدتی است مقام‌های آمریکایی دیگر نباید چنین آمارهای ناخوشایندی را ببینند چون بعد از ۳۰ سال گزارش‌دهی مستمر سالانه درباره وضعیت ناامنی غذایی و گرسنگی در آمریکا، وزارت کشاورزی آمریکا (USDA) از سپتامبر ۲۰۲۴ بی‌سر و صدا تهیه این گزارش را متوقف کرد. بدین ترتیب اکنون نزدیک به دو سال است که مشکل گرسنگی در آمریکا حل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/663438" target="_blank">📅 13:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZx8QPlSG7NFRjnsZv9-EjGtsmwgw9pkZswnW7YCA3W2p6EnNBumLCCJwzhP8NDg-zc1snys5EcVr9sZtPSzlFW_RrnF735Jtvcja-QL3VXsxjw37Xmpn9MpJhgXSK-EscvcItoYxYWOhzR8unS1OVPC-hCCBq3HEqH_Mk7NLo25P_E-na40mV4zLNY7jEHG0OGXJgXdku8FVCiLO-WbVLP85vZYsCQnWfK16sdgdVCKvjJXjB9PRHoP1a07kdY4GDOQMCAc1qzXDBeHI8zIIAAORDxysPdlTXWzufSdMd9PsIhaHCrDy9jy7w_HHxxroDcLLFlZxCCXxpWCRFN_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG6qQ2YuvTq4TjjlHvksIq3Nh3FNHHz8JiXcbfd1KMCju08175HD-iDyZwheMRmrMCQyfvdtzYW9PPa3__NxtZqYNKWIgSdo5KQwpMwiblaUpOEJ4L9P6cLw3FAbqsdKmUgAl4ugm7O6xUFCxQRtY3e2Oc1I_-LcewgBR-dQlaBwRH47-fXTGt1R1ON4LrSaRV9LAQrry4-opVz1PJCR7xuHL6cxq7QzvramMR3_Sf8b0kGjgdlLPSEWSe5x4k4kt2obAJ0gyY6xBy-NUmYj8Ure30ugkDo8RignenbrHsKaXCwuxf1An2C3bvk_DWpShK-8QAh9RIFItEn2thsFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8NydjYmhMIcF5yz3hUj3SoWfKag6VsYOc23NWyKwzA14PkuPKcsC6M0gPxQkubZGqBuhOG2IhESbvRYL7K9O0V2KHu8aBl4gdINadfSleR6hegGyR0Blj0006eshw9yNuPln_czZBc4zawwD5n__8Lfq9ZMHnX6g0-cEUlkiqGLnvqJSyccpNDfkEljKdvhz1AvGvi6ra_6BUS7Kr-lKGsTpBDBXORi1ooeT-WkPs_XZjJigWSnt0NEwhm8Sl7gyxg7T50KgUQdeCAOGM3tikULuifABTCHF40cD8tjf5Hn9ucOE_5XLI9X2jht5AcAzc9pvpETKqxHwCuaO9vwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRWn1ViidzWEz4fie3kUphIyfeiIHcUhXYZOYUm7OV5to2NkrjyOLNSyj3zT4SGALi_zdmQmc7VfLDp4NuKbbq_a9NqhkpWttNm15UdFeSBydGHfg-vYYGCSLtRiFGa6XCbOv-_hRB5d8Epb8ZNTI4uxvxtdAGOpdGjDeDOjbYpYzXrsxKXQMA1Gb3TVVv9vHskumbGr34QivFGI2F9rhX6R8g3GtBooW9SbxaGyFtnfr1ZJgiqsPUo-O8hX64wubHd-ZqJh4gFgdTJ64BQ_IwRjHz2CZuF-lDI5WolmM43xB7EVFnQemF7DeIvuXe9b4fdO7gFO-HL77kURP44_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFfrPaclNxMCA_iFjgxcnMREHeMXFbtnWIkTw7PHpRtx7otjTc7dS72-875cjSFAYWmqLPsFqE_TWXtr16yH0_5KkeCHWhdapDLuPyGTYib1prOb7C1ceF9Ve5GHQz6-scIJGIMUIBmSKmHuk3ooi4U0QvHmunA4F2F3SLKSFXxi82vqK_f3kiGEuZE2kAdgauKnmr44ug5E0w6kolsfFbvDncKo6SyO2NyF5OcyojWUkE6b_41LAGS-xI_7IVCkWsneO-QqY5VipUZZKmmYSHkvXmPG_14OJp-ET0L9RLNRR5jH27G_QxOd7gV2iuDqyOrvVzxTnPZCZPsgCzveGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fla2qWhAJHCSmNYvVtmCYTvhZtTEwY18Y7XzglFwn-AuU8DWgRzxLku-Dg7h1b4xRNbqOaOuSJcqPcLvWwhCOj5L0vG8ARVTgcXg3Ci0zagsTX76s_R_u-FD2Aw55SF9uP3O1xNO4ETqACJa98rUJfKyFcslGA0eoDTNCptPnPL4OqDPmvphaRzdElobP6mIcgtKDooEFgu3ZBi9sFHZmCnx3J6Mstb63NBMTgikCxG8uXP2QLT4RXHunylViF2zjhWI5873FDivgOK7Tr0vanYz6FxIiLJ_Agcd60M2H6oM_R2SWsZ_XIEVonRihMzDSv84WFVKNkaL8PNAJ_8z_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر جدید ماهواره‌ای
WSJ
ابعاد خسارت‌هایی را که ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین وارد کرده، آشکار می‌کند
🔹
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663432" target="_blank">📅 13:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S20hePo2Cq3GEJSfj4aWXFyNXzRpiAOyJsY35eI9qC0vC6O2qkOWfFxOHim_cSBcnc6khzWf2Bofb9seHClxsT9a1fWX0eUN7Da6DsNphwuwttk7fXJaMNWxXgVeENA1negZgD3LWjC4xdv2JJM8tocmMNm8ZvYIP2La8cyxtN55pfXeKaiz65dR2C4tg8v3DU2-zOA-s_4AXSY8a0R4SLP3x7VPnYG58eQ8a5iNWgCyEnuEiYE-nNMcshnJ77NkHJGAigc6EimmVjIqxrmjp00Tx0FMgUW9YFHk7rxVuek3lbU0rlu06Y9wdZuLhcfRpLqz5b7-D_h7lGyhYcCBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هشدار آشنا: جایگاه رهبری را در حد فهم ناقص خود پایین نیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663430" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663429">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMcW10zBhoZ7dbrwSkyueiWTjEvAhU9tKF3Ikagrwo_jBc9TAgbiYOX9RnCcDyUOBdAwsR3dG6F--IhZKmLa2k9d1_dizuBsocQ9yA26xCu12P8wkM4ZqCp8iNgAdE47ckBo2MUMpUPbm3PmoCyaaBAcRCHPU8NmZklWQ15RHJmLwltfbXePZ7S8M4KUndGSU8nNC75QfwRttZks1WIY2enywTN7HUJeMQeTIIUdINFWplyDVbc9sJZM0AFeD7lsirdmDDl5DZLDgIf9M4a6PqjrkVxkEyHLIYp685X0whf0sfyyxQRjjI3Y8dyswHiWtEbCDKacff1hfL8wasn-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چین اولین هتل کاملاً رباتیک جهان را تا سال ۲۰۲۷ افتتاح می‌کند
🔹
شرکت چینی Pudu Robotics اعلام کرد قصد دارد تا سال ۲۰۲۷ نخستین هتل کاملاً رباتیک جهان را در یک جزیره مصنوعی افتتاح کند؛ هتلی که تمامی خدمات از پذیرش، حمل بار و نظافت تا آشپزی، بدون دخالت انسان و توسط ربات‌ها انجام می‌شود. این هتل ۴۴ اتاق لوکس، رستوران و باشگاه خواهد داشت و با مدل هوش مصنوعی PuduFM 1.0 فعالیت می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/663429" target="_blank">📅 13:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مراسم عاشورا در لبنان
🔹
این مردم، سه سال است زیر حمله اسراییل قرار دارند، رژیم صهیونیستی خانه و کاشانه آنها را نابود کرده، مردم را آواره کرده، فرزندانشان را کشته تا تسلیم شوند، اما امروز سربلند و با پیامی واضح به دشمنان گفتند: "كِدْ كَيْدَكَ، وَاسْعَ سَعْيَكَ، وَنَاصِبْ جُهْدَكَ، فَوَاللَّهِ لا تَمْحُو ذِكْرَنَا، وَلا تُمِيتُ وَحْيَنَا"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663427" target="_blank">📅 13:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663426">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
امروز ۵ تیر، آخرین فرصت ثبت‌نام در پذیرش کاردانی به کارشناسی
🔹
آمریکا، مذاکرات بین لبنان و اسرائیل را برای یک روز دیگر تمدید کرد
🔹
جدیدترین رنکینگ جهانی تیم‌های کشتی آزاد جهان؛ تیم ایران با ۱۵۰ امتیاز در رده سوم قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/663426" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663425">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
آغاز مراسم عزاداری سنتی «ركضة طويريج» در کربلای معلی
🔹
در سالروز شهادت امام حسین (ع)، میلیون‌ها عزادار حسینی در کربلا، مراسم تاریخی و باشکوه «رکضة طویریج» (با پای پیاده و هروله‌کنان) را آغاز کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663425" target="_blank">📅 13:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663424">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxQ9UtvFH5MRcdNaVGn18CEUmpJh6qv5NG-0q9UMr04f17LOw0EMw6mNuefN9OK7lVJ9aLCINRsk4fY34mCM_839EtI_bJrt86Q1RF3kTJf2Z_Ub7XI7XBBjPNwzqdENolp5I2Rulhu-hQ-6BqPvwu4yzvC-BfAeqKLTJKIs6I99arHdimYNJgSkl4nkOT21Pm2VmmmYMg1WPGCTK7_hiisUj-zd-SQQG4JaGimqtgVSuvO-ZarKLH-7q5tX6Icxhb3KyoVF-G3acrRXpLJh2tEaEb3hB2a0jYiXVn8Qb96b7dNgMZTFfSvlPxoLiX0QZQClTiwdP9DfOH3mqFP1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غریب‌آبادی: عبور ایمن در تنگه هرمز با تصمیم‌سازی خارج از ملاحظات ایران تضمین نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663424" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663423">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e439b39199.mp4?token=Ei-0HnAkvsDvC7bCkaSp-uPFDbmgKRyn_HyZuXoirEbbhgmmOOiywpb_KVHvdtHJ7TaYzpbDcoAfGBw9dxkhczv88vqydT99DD8Kfa8rq_wE-zIPlGySBJXr6cGo95KRFcK5xHSvf083Mhj67wAalZeSQdUERn0wrsk3J4IGKJtVGYI-B_JQ_6bCOVyaBracH-LaVYvSo93NHt_VXB7ixkcMWEphZI9JcTSwH2hLCmtntrnP7XU8gw24NhSN6Dd2TJlRb3QwmUv2if_5N5qHQsUWGf4ceHdufrklATp2YmXZm8IUgnmy0kR6BR8L2W5mDPVpxxbzcPeH0ZAMBZ3ZThahWZ3o_33ykzwJQksgN76QoP9wlw5Gv0L2WSccqgx63hLSZCTW1zcYf_TYOtlGOVN2jpRyr_Qmj6XqmDUe1EEeeTPkcXV-wVDsh7x3sI4xx6i9IRD2OzMPTerMwq5syeSl-EzyFNcLuE8IJLTE2k4M9X17TkeQLIRQzFtHo9-dn2UhRzz7t_-x473k67TRSxrr6v2s57ROg97hjmCg5Y7GG7_z6SM9I3qMx2hMWbFIpvdQzpl2Qb1fz-nazHG6dsktC40UEWD2YSuFb6C74U_QJvR7wTipr40AldZpgkfBojLiEVZG3seH_EgoKw9Ul-5qfQFISB0cvApUA_73N5k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e439b39199.mp4?token=Ei-0HnAkvsDvC7bCkaSp-uPFDbmgKRyn_HyZuXoirEbbhgmmOOiywpb_KVHvdtHJ7TaYzpbDcoAfGBw9dxkhczv88vqydT99DD8Kfa8rq_wE-zIPlGySBJXr6cGo95KRFcK5xHSvf083Mhj67wAalZeSQdUERn0wrsk3J4IGKJtVGYI-B_JQ_6bCOVyaBracH-LaVYvSo93NHt_VXB7ixkcMWEphZI9JcTSwH2hLCmtntrnP7XU8gw24NhSN6Dd2TJlRb3QwmUv2if_5N5qHQsUWGf4ceHdufrklATp2YmXZm8IUgnmy0kR6BR8L2W5mDPVpxxbzcPeH0ZAMBZ3ZThahWZ3o_33ykzwJQksgN76QoP9wlw5Gv0L2WSccqgx63hLSZCTW1zcYf_TYOtlGOVN2jpRyr_Qmj6XqmDUe1EEeeTPkcXV-wVDsh7x3sI4xx6i9IRD2OzMPTerMwq5syeSl-EzyFNcLuE8IJLTE2k4M9X17TkeQLIRQzFtHo9-dn2UhRzz7t_-x473k67TRSxrr6v2s57ROg97hjmCg5Y7GG7_z6SM9I3qMx2hMWbFIpvdQzpl2Qb1fz-nazHG6dsktC40UEWD2YSuFb6C74U_QJvR7wTipr40AldZpgkfBojLiEVZG3seH_EgoKw9Ul-5qfQFISB0cvApUA_73N5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هم‌اکنون کربلای معلی در روز عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/663423" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663421">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df46663276.mp4?token=gJFhJ7L7bSfZUnfVW4sOg0F8ZgDZvSIYhuO9yY7cC3SgfVZr2l_SwrOhAgKbXzCLD01X-qPqKOWfSdkjSaWRU_17jCmp8ElPBIoKpOfhQTWcy19Ij13Us2itQReHh2hOjfYHlpOrfpcUSthXKnPmONMmu8uoM2Ly2IK3O1erArDXeaOFlQl0q-p60ByaTQvX26K8SPYjLTS9tObOMdSFwqTnd9xE2ob_dYaes2JSIOkT4qV5RaDf-xkRI4yTQVgkPUNeciZ302A2-ogbNXTMig2vOjlADHYqWwDbj8odooMweh5MIt6P_Ft-Ff8SqTmhk_ZkZJbHRm6P8VHfHp26Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df46663276.mp4?token=gJFhJ7L7bSfZUnfVW4sOg0F8ZgDZvSIYhuO9yY7cC3SgfVZr2l_SwrOhAgKbXzCLD01X-qPqKOWfSdkjSaWRU_17jCmp8ElPBIoKpOfhQTWcy19Ij13Us2itQReHh2hOjfYHlpOrfpcUSthXKnPmONMmu8uoM2Ly2IK3O1erArDXeaOFlQl0q-p60ByaTQvX26K8SPYjLTS9tObOMdSFwqTnd9xE2ob_dYaes2JSIOkT4qV5RaDf-xkRI4yTQVgkPUNeciZ302A2-ogbNXTMig2vOjlADHYqWwDbj8odooMweh5MIt6P_Ft-Ff8SqTmhk_ZkZJbHRm6P8VHfHp26Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تجمع هزاران یهودی ضدصهیونیست مقابل کنسولگری رژیم صهیونیستی در نیویورک علیه رژیم صهیونیستی و قانون خدمت نظامی در ارتش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/663421" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
اکوادور غول‌کشی کرد و به‌عنوان تیم سوم صعود کرد؛ شکست ناباورانه شاگردان ناگلزمن مقابل اکوادور
⬛️
🇩🇪
1️⃣
🏆
2️⃣
🇬🇶
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/663419" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روسیه داره باقی مانده زیرساخت‌های اوکراین رو میزنه
🔹
اینجا یک پمپ بنزین با پهپاد شاهد ۱۳۶ هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663418" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پیش‌دستانه‌ای که شکوه را به ایران برگرداند...
ماجرای کامل این دستآورد بزرگ نظامی
👇🏻
https://youtu.be/AXNLsCbNe7w?si=DA0CyGP385V7uitO</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663417" target="_blank">📅 12:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔹
وقتی نوه ترامپ راهنمای تور کاخ سفید می‌شود!
🔹
در ویدئویی تازه که در فضای مجازی منتشر شده، کای ترامپ، نوه دونالد ترامپ، رئیس‌جمهور آمریکا، مخاطبان را به گوشه‌هایی از کاخ سفید برده که کمتر جلوی دوربین رسمی قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/663416" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFRORvIgsfoV4itmd_mnZoIAArkCNQppxpWXbeR0Nwdj9fVPZvX2PrEf00zM90k8CZTvkC35SlMKW0T8_B_szSPI2IAAR9ZhDXSiweUBWdGZj220dAUWzoAKDmQjgOzKg85JYdKoY1tZJv6aSxRu9irR1NIwhm4lr1IlTPz8rY_gOFNuM8CEf2xIGaTmf_UaeaLG5ahELAOYnKpkMpp6Wofq8tlGTXO-E9Lqc8x3zDsQorreSOA3F3G4YYwevZV_oZSblErXOjVumwQzg92Ja0zmX1DpgLEYgr7i1rySO6GIJRBfu_Ab9ZEpPThyMpJeFJgdkihEn7FP86Al6_A4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۲٪ اسرائیلی‌ها ایران را پیروز جنگ می‌دانند
🔹
طبق نظرسنجی دانشگاه اورشلیم ۹۲ درصد اسرائیلی‌ها معتقدند ایران برنده جنگ است.
🔹
۸۷.۸ درصد معتقدند اسرائیل به اهداف اصلی خود در این عملیات نرسیده است و ۸۲.۹ درصد می‌گویند این جنگ امنیت بلندمدت اسرائیل را تضعیف کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663415" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توزیع نذورات در میان خودروها در عزاداری شب عاشورا(دیشب) در شهر دیترویت ایالت میشیگان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/663414" target="_blank">📅 12:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لاابالی یعنی چی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663413" target="_blank">📅 12:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
طبس گرم‌ترین نقطهٔ جهان شد
🔹
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/663411" target="_blank">📅 12:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImsY8fTugR1sLoBKs1jBWjolnXYpVsfFo6ayZaDFlhbsHRwdw9gxDh_lfA0pAoRABhCvVBWQAWUOaLiSlU5FOdnoQWrQiyrKKXM0mTbIdTn9q_ALVtPpYB4tUm2hFa5hT0quAyt8JDS151biUe2vYqtEAfUqPXR8bvUwqvC7aekURR-h30GW0C4ZMOvLV6YS7uwiZwcJxDw-W0l9Y1q0fiXgBPSmVWo6JPYknAOsa1pyH1YmRgjjrOJvt6bAacJ5W2L5KzPr4LvDUCJ9dE8pkTAyltC8xa-lyy9YLS26h-bclStwJRjw25p8sqaHUKTNa8wznVH8iWovHZWhFbB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اقداماتی که بسیاری تصور می‌کنند به کاهش آکنه (جوش) کمک می‌کنند، اما در واقع باعث تشدید آن می‌شوند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/663410" target="_blank">📅 12:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663408">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
کارشناس نظامی لبنانی: ایران باید استراتژی خود را در دوران پساجنگ بازتعریف کند
روی، فعال رسانه و کارشناس نظامی لبنانی در
#گفتگو
با خبرفوری:
🔹
ایران در دوران پساجنگ با مرحله‌ای پیچیده روبه‌روست؛ جایی که نبرد اصلی از میدان نظامی به جنگ روایت‌ها و رقابت ژئوپلیتیکی منتقل شده است. هم‌زمان تلاش‌هایی برای بازترسیم تصویر ایران در سطح جهانی و تغییر موازنه مسیرهای راهبردی منطقه در جریان است، موضوعی که نقش آینده تهران را در نظم جدید منطقه‌ای تحت تأثیر قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/663408" target="_blank">📅 12:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663407">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
بازداشت یک ایرانی در مونته‌نگرو با درخواست اف‌بی‌آی
🔹
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
🔹
بنا بر ادعای اداره پلیس مونته‌نگر، این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/663407" target="_blank">📅 11:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663406">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=sB0nEAjj1K1p5akBSIGHIOhFIdzeUS0IoLxj47-bKAA5M64z18gNhDYN7P5pg6BJbkHxCr3H0OcNp0-RFe1d-6abU62OpoliJD3GAtL5TNFulpgC-L5j1qQGKGAMouivGOvPmV0Qy4YwIvTiXNd0iqgeL5cEzJom-eSVWJmZcoai0K2SfvM89fZkfp6X9elckwgmWAeC5iaffnsL5lJJGZgG4SEPjSAkPiqkrbnd9oEt-O_dHI3wKC4iEnJIuCE6isqm_8Tq9_6pSM63VjQHhuSvXlI7ExSvlvLzq0siFbYGZjHs5brmL_gkcN-6wufIBwO7wQBaoSeVsSUKQYfQuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=sB0nEAjj1K1p5akBSIGHIOhFIdzeUS0IoLxj47-bKAA5M64z18gNhDYN7P5pg6BJbkHxCr3H0OcNp0-RFe1d-6abU62OpoliJD3GAtL5TNFulpgC-L5j1qQGKGAMouivGOvPmV0Qy4YwIvTiXNd0iqgeL5cEzJom-eSVWJmZcoai0K2SfvM89fZkfp6X9elckwgmWAeC5iaffnsL5lJJGZgG4SEPjSAkPiqkrbnd9oEt-O_dHI3wKC4iEnJIuCE6isqm_8Tq9_6pSM63VjQHhuSvXlI7ExSvlvLzq0siFbYGZjHs5brmL_gkcN-6wufIBwO7wQBaoSeVsSUKQYfQuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قاسمیان: نباید فعلا مذاکره کرد؛ باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663406" target="_blank">📅 11:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=a9S8g-10FD4Iu35mMV4N16AeHLAEj5QXr7pDC0Iuiodu8wvKRGvaj0prc4zXMYw3IQezeEfvPC5GdLoyb7UrzFdAviuxAraEW24igLmEOP5A-yAAn6K2UiDGKL1LN0IFVjjECbNitTWd2oN8KGugVmRm_svP_5uftqBjXFoF4I5i_dOXfkQMBSpP3MHkmPtaxq2dLMO-VHZkI7T-P11WTfLDG_KiGgT1R5CSoR4B0BXC55v7ZFOPz-R0n_MjvrKrxq1OcLnQM5IM0Q40IDAfTtU8d3EWkDOVPjAyEglCrYfnSwG7ZFMxOq7GuLZRsOfoOacXXm4kLi_tn0T02c0o7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=a9S8g-10FD4Iu35mMV4N16AeHLAEj5QXr7pDC0Iuiodu8wvKRGvaj0prc4zXMYw3IQezeEfvPC5GdLoyb7UrzFdAviuxAraEW24igLmEOP5A-yAAn6K2UiDGKL1LN0IFVjjECbNitTWd2oN8KGugVmRm_svP_5uftqBjXFoF4I5i_dOXfkQMBSpP3MHkmPtaxq2dLMO-VHZkI7T-P11WTfLDG_KiGgT1R5CSoR4B0BXC55v7ZFOPz-R0n_MjvrKrxq1OcLnQM5IM0Q40IDAfTtU8d3EWkDOVPjAyEglCrYfnSwG7ZFMxOq7GuLZRsOfoOacXXm4kLi_tn0T02c0o7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یاسر جبرائیلی: اگر بناست با آمریکا ببندیم؛ ظریف را ببریم
🔹
یک بچه و بساز بفروش و پاساژدار را به مذاکرات فرستاده‌ایم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/663404" target="_blank">📅 11:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgQNwYZv4TAX_CSwkQM3jIbygno0PHDuPtV9b3Ow9fqcWO85VOuVAGu1-b-PxWjA0SYxtkT8MMfwRlDDsyqDHNTcVx98z-ii4Rd7zDYxg6gLP2WYRO_DOq9kQYHGpHIDK553qKd9JnoCS6xbgfYesyyk4QI8QvsmRQ3hdPEabYgWjT519HGTMd7eS95Dxp77ILRAQLVt3gYfQiWjNEMtljuFDnwT3TxoU5fUoVheYYmbhnOO1onweuh902IFxN77ySBX7_kOEaASrxNQ9e-RYbi97UZpVNwvZlqNch4Nkb9_gwhbBrK5a8rEh96zw8s3mzOtJblJ17_XPVvaebAPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هفت دستگاه موسیقی ایرانی به زبان ساده...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663403" target="_blank">📅 11:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔹
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔹
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/663402" target="_blank">📅 11:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igstEMSkxB8yvzEgLr2DhTvW5IQuZra--9Apn4skd63o5jwT1q9bfl3g06DHCIIBOiM5Q79eJE2VyIh0Bdz-IPzwnx2vxYgxFI3ODVC-dhezrYYN47wOWCo90k2pPVyfTma5-18MCtYsAq2_7BrBcF5KvPiWcaDADPDu4tC72TBqNkyXiMbsc2TQwLIGuvxFrSN__z1fUiFBFlHMxshbzByyg21dlpRCJFC-l99qHo4LeZl3MTYxZNmtCGl57rvolKMmwhW1E2oyOcOxEACJlCt388ptyoiOV2OpQ-GSP9uFX17Cnr8NI6d_CCTmQAnGZuh4Z-YrgsC3V2wE9sCETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlEZC2-nU5HebGeNTN-4KxkN_-u-j2n2numglkYILT_8KkQJhPdxKLv80aK9Wj-reIMZoA_R3ESWzPbBmSdXMVtxJch-wEN7Su11ZrgV7fFTC-sB39d1H6Wts2P4Ljn5n1R9FGr-k07l2W4pFk1dqSVKPuFpH_YWYtZcNKjuVIM4UqObzIbEdzHaQ0GVzXRtaxBvJxZe-hhL3Y86dy-7wceBMN2I-lSthmUkwJaM-k2KlwhVew96aODuJ_MExlpBFpJv5yrzBN2gEwQYaaFJDh84jVbaP5NQ916SHU_qCJV37e_h_mvO9FcvRIjuGg1GJYGW4KYh_XxO8FL16kHLlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بیانیه وزارت خارجه درباره بیانیه مداخله‌جویانه وزرای خارجه آمریکا و شورای همکاری خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/663399" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhmR_9QdIf7b3MXIiRTccKYiGtBf0egchPLk-qh698gRuliBL5qM3ia9_u-fNEMXJZMQMK__3kQVkTDXzPkWTr_Ln7itV-iyT7YwKV45GPvY8vbpi56q37ImCWer2oqLrccYhHGlhOJ01YLS_tRgSbcc-j_s5nBopUTVYE8FgJkjDsCig0UgqHmcx_H7_WHxBgbpBgOJvsusp0IIlLP6KO4rwwr0tIuvbLNgaD8LvGaRvNZSZxtplEQMPn-GALmpvPRHZNYYxcGbIl5wWSz4gBkohdboxrNm4hxTLgAzj7mVR9VOU1-GMJFbx5kP1nVyXPuZ4EwqvrFG5U57nkfUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه مسابقات روز شانزدهم دور گروهی
جام جهانی ۲٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/663398" target="_blank">📅 11:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
دبیرکل حزب‌الله: در کنار ایران خواهیم بود
‏
شیخ نعیم قاسم
:
🔹
ایران با ایستادگی خود موفق شد به تفاهم‌نامه‌ای دست یابد که به معنای اعلام رسمی‌ شکست آمریکا و اسرائیل است.
🔹
امسال، شاهد باشکوه‌ترین مراسم عاشورایی و حضور گسترده مردم با وجود آوارگی، درد، فقدان و مشکلات بودیم.
🔹
امانت شهدا، جانبازان و اسرا بر دوش ماست و از آنچه فدا کردند، محافظت خواهیم کرد.
🔹
اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/663394" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiI_iAu5xDiyXSQbRYDOPa1Z82cE5Glgvgs8-go12-lYlu-7b5LVcum45kwBQMQETnm81J5GQEgkT4wK74r4PmiD03pq64cRLoC8qsUAnmASuB76KkemxdU7P4U7t1hXiMZgC-rzFqLriDT5GZECx8ere45S3dx7EYAvBq7IsBH284flTk6JzKSlA0_BS0P-hvSshZn13eUJYWW_TIZZ3tMPIig2m1DB42tr0Rf_xnkSRrkBcdISKWI6QdG4Cekvp-AFIyThSZaFC83HGeJVhaWvlE3PGSq3IvWnrvY9wjiLYtCvIKOwu5jeY8UrIyU0ha7z3ld2wdLeDFBt8t9TBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دانشمندان ردپای بی‌خوابی را در دهان پیدا کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/663393" target="_blank">📅 11:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=dZGFUbgQgpyxdcnVbGhnmTLNIlKgUAJj6NXlv_NHjSq7btlFffm4RyLHDJ07ekrQR7w7eQEP50qTfshqNcsKNQAE_cgMfa6pUx8PH-MZ7Qri2ttKma8uh_uJ9L5MpP7_F6m4UHTeO8CbtXJ3VUDusrxTo3uoNr_KPeCvjyT38BUml-skz45jyUTmpj23rsCqPCMM4LlYJB6Rgt2CMcP0jl_9YKCdb91oaFPXMaUxVh0y3V8nCt1SLqKxA3ClHkwxDGSWccWmM9_E2c6HZaH1XY4BpOoFsUk4DCVkjLHmfVevhJQHpvglzw7tUmnivaXc0xZgX7NNx2GI8zignN4O6g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=dZGFUbgQgpyxdcnVbGhnmTLNIlKgUAJj6NXlv_NHjSq7btlFffm4RyLHDJ07ekrQR7w7eQEP50qTfshqNcsKNQAE_cgMfa6pUx8PH-MZ7Qri2ttKma8uh_uJ9L5MpP7_F6m4UHTeO8CbtXJ3VUDusrxTo3uoNr_KPeCvjyT38BUml-skz45jyUTmpj23rsCqPCMM4LlYJB6Rgt2CMcP0jl_9YKCdb91oaFPXMaUxVh0y3V8nCt1SLqKxA3ClHkwxDGSWccWmM9_E2c6HZaH1XY4BpOoFsUk4DCVkjLHmfVevhJQHpvglzw7tUmnivaXc0xZgX7NNx2GI8zignN4O6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداران در روز عاشورا در استانبول ترکیه، یاد و خاطره دانش‌آموزان شهید مدرسهٔ میناب را گرامی داشتند
اخبار به زبان ترکی را در کانال زیر دنبال کنید
👇
@AkhbareFori_TR</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/663390" target="_blank">📅 10:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hQ8uk93Lp2Oe-TUMMliwqMd7wrAa9gMU8Tn_ohyiilX33ALfhnE5v5y1ohX-jG0RV6jsG8x8-bypfXJx2qFkrklcZBqV-kOHXr62gQjXsHJer0WY3LEB_cIOqDUHf3jfcRXGANdvsS55x9Q7XXM9WxXlUCiESjJoqm2yHIYvuP8dtW27tWUjuO93p_9k3sZpRhmgUC3n2d_a7daJgTjgZp1aMUqBYu_grUpttbE0sCmY2IuDSRi0ofNaQ3wIlxwNbNWwY9aqRUeMUc-jZzLG7cuWW-Lh_bKbfFynk4omT6CxMtuzi2Q7haTHPRl9IY_VrY5x6yHcL-wEXUgTOG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور شهردار نیویورک در مراسم عاشورا
🔹
شهردار مسلمان نیویورک با انتشار عکسی از خود در مراسم عزاداری امام‌ حسین (ع)، تصریح کرد، عدالت امام حسین(ع) الگوی مبارزه با ظلم است و این ارزش‌ها را در ساختن شهری عادلانه‌تر دنبال می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663387" target="_blank">📅 10:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=BnAnLIdPKdvNphaJqzpuXbMy2zUKwnoA3BpV6AsRkaiCproJlCH9q17Vo_B36Pp2BM_01kfKqIr7hrwO9mGDIVWf3hjEI1BzIvvpQ3gwe3T0SF8JxDD5lskMnKLkZScKK5u4N4CXB0mWFN-Yscx6Ydo42tzy-3EKGjiKvsodXaFhFHdG-0CchwJXbYG4JVNLaTNhIFP-3-oKszc5jZa8dzneeluYQrcGNfV8SOo-cXXTGtGDIxULBwjVxsxJpL0F_QPSA0Qa7yF8qvwThpCqUd7Z33WvR6zsMzQ6bnTo70mDJPCUMSUxRGqlwSdHSy_vW9orL-D2U_xuLye4Gt1UwYClO8gLVes4yXkN4oyZv-o_g-D5SbqTyewJ3MADnGpgPgsv_lRuy89-MbBvevKV_B2VGp6riO5f55a-RHXn1YEtLq75nyLjnyFsCjx9JSm1o8axt3Dv4eWRhGUnuSM-xGS_lunHqmbdXLy9ib9JotQPQLA2-u_vQfQkMJ9KqPBdUe52WsRF6e32QGWk8C2IgBSUn22_BFXdP5aw4wVmUpxd4lg0I641AkOt015ksyju14U2h5MMI9KshlnApZOHzqZ8qnNQxFuVfgfHELhFSJyLHgaF6TACZvZ9v2psJ7dIOY6TW8GtvrR01sIH5Rldunm9JEENSNOrCSSEYDtxywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=BnAnLIdPKdvNphaJqzpuXbMy2zUKwnoA3BpV6AsRkaiCproJlCH9q17Vo_B36Pp2BM_01kfKqIr7hrwO9mGDIVWf3hjEI1BzIvvpQ3gwe3T0SF8JxDD5lskMnKLkZScKK5u4N4CXB0mWFN-Yscx6Ydo42tzy-3EKGjiKvsodXaFhFHdG-0CchwJXbYG4JVNLaTNhIFP-3-oKszc5jZa8dzneeluYQrcGNfV8SOo-cXXTGtGDIxULBwjVxsxJpL0F_QPSA0Qa7yF8qvwThpCqUd7Z33WvR6zsMzQ6bnTo70mDJPCUMSUxRGqlwSdHSy_vW9orL-D2U_xuLye4Gt1UwYClO8gLVes4yXkN4oyZv-o_g-D5SbqTyewJ3MADnGpgPgsv_lRuy89-MbBvevKV_B2VGp6riO5f55a-RHXn1YEtLq75nyLjnyFsCjx9JSm1o8axt3Dv4eWRhGUnuSM-xGS_lunHqmbdXLy9ib9JotQPQLA2-u_vQfQkMJ9KqPBdUe52WsRF6e32QGWk8C2IgBSUn22_BFXdP5aw4wVmUpxd4lg0I641AkOt015ksyju14U2h5MMI9KshlnApZOHzqZ8qnNQxFuVfgfHELhFSJyLHgaF6TACZvZ9v2psJ7dIOY6TW8GtvrR01sIH5Rldunm9JEENSNOrCSSEYDtxywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جزئیات حمله زمینی تروریست‌ها به خاک ایران
🔹
خودروها خریداری شده بود، روی آنها دوشیکا نصب شده بود، به آنها قول داده شده بود به محض اینکه جنگ شروع شود بعد از ۷۲ ساعت وارد خاک ایران شوند و چهار استان ایران را تصرف کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663386" target="_blank">📅 10:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKenSvo1Ou2fjsfk4bfAWpvCTm3-1Sdr2iRz_pjYUwoGOtredkD5iygBQLbUqblBsBCWCM32d37jIyiLHtMMrQTA3wKy852Imagn9unwmAsRquMVlX0oMwF0jn24TbzHJCeQRFTKqybVYzfuLkUbo9OZ07y8ZZ7n_ZLx3I2BsnS5dlzWQCilg2WvO6rdGqUl8TT1z_x5XTDnzgNrMASpjfNgXNv_muvSTVnYKGtUh00SsE9Q8MSCYeVKjmt0pCykNUKmWjry_EqlxJc0Wdt602jHqAyUJ0H0AgkxzsiOROQNuo04RtiiYoQMEtoFp9Jp4oMMcQDmAtsOoKHwaQ9rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی زیبایی‌نژاد، مدیرکل فرهنگی شهرداری تهران: حسینیه انقلاب در میدان اصلی شهر‎ تهران و در ادامه حضور مردم در میادین،با شروع محرم صحنه ای از شور و شعور حسینی شد که با شعار ‎
#يا_لثارات_الحسین
به مطالبه خونخواهی رهبر عزیزمان پرداخت.
شعار ‎
#یالثارات_الحسین
در ایام محرم و تشییع امام شهید در کنار شعار ‎
#باید_برخاست
محور فعالیت ها می باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663385" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a96TbPIKSGUu_NFt6M_0OD0MNdhsTzTvrEDsShkm-Xa2VFfzZxhbtLlDV-AZFowdcAOZQKy9yGz-o3XR1D4XMeBgXiEn51FsKtRyu6adKXRMg1Uq77_elyJv386znrQMSqdevBqDuDQZNv6eij6neVcX6ARuDn4iujDwntmYJi-qL7JPPKK5fVP2EPUTcUhdbFOFqSzZ2JPVrcXtl0_4TWQIeOAiUdflx052hcDhIb0QBRkDGddvizocFiQlP17ymomNbebs6PD4aUXF4XrZlKn7bv0CGGKgG-BaSHf5daDTQM5R-m2Miiaw6eWa8dzgLsUGXXpe0pjO0CjqV1SdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهنمای طلایی قطره‌های چشمی؛ بدانید چه زمانی از کدام قطره استفاده کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663384" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43843f73b.mp4?token=lHPuSdcUaWLy-awKMFPLXHLq_IOWeVrfibWDXeeB-K91AYju373GsDLRiyyy_MrMFe7PC6BdmpbgrgO0evuRUd-Fabcz4KZG6j_BDjASW7l1NUXReczCzebbUHX_pkO_RZtw9bUSvxQZbfa9tK3hybgOeqogF_xP4ak7BEsJGLBsgcL2mo_4f4Wk70zx16qNQIvxzFPODzCXkwBYI1AJYMMEg7PFr3ObQfFlBusmDi5HBDtJk7mjO8mDbMdtv18FHf0tfwrvXMu2aezteRSQDxmq4juG_jWapeHQXvPYeLwnc9pbwjf6mda0Jk1QgoYWElAgCb9RzgGwcvNlSiq0EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43843f73b.mp4?token=lHPuSdcUaWLy-awKMFPLXHLq_IOWeVrfibWDXeeB-K91AYju373GsDLRiyyy_MrMFe7PC6BdmpbgrgO0evuRUd-Fabcz4KZG6j_BDjASW7l1NUXReczCzebbUHX_pkO_RZtw9bUSvxQZbfa9tK3hybgOeqogF_xP4ak7BEsJGLBsgcL2mo_4f4Wk70zx16qNQIvxzFPODzCXkwBYI1AJYMMEg7PFr3ObQfFlBusmDi5HBDtJk7mjO8mDbMdtv18FHf0tfwrvXMu2aezteRSQDxmq4juG_jWapeHQXvPYeLwnc9pbwjf6mda0Jk1QgoYWElAgCb9RzgGwcvNlSiq0EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اعلام مخالفت ایران با عکس و کنفرانس مشترک در نشست سوئیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/663382" target="_blank">📅 10:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwUeZRw3Rbwwf4tJQhm5Vj3Uieex_eHSZITucWX2ETswOnwVad6s_5WOCXk9vov_luKD1xQEJFExFf9H-URZUtXazXLyZXiYgHjMW_RPvBCD2clGSp1V1xHVzRYmyYByyq0YozwLX3_Fk-rSKDzf5fTflxKzEOuPlOh7V07np9P14Q8_00J_bfyHJhw0ffkYJeMD0x2vA4kB4zncqlVtKBLVkV5MOO4YBYWXU-Jw8qhsKEi1YckiJWoOh-ElDvoZD2T1nEvrIafcfVofThlfiCqcyUY8wC1w8d8zPtk1uO7gQ8DT6dFCzkNzCMosyLfVtHwJxLaNiHWmDPV9aDYXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر فوق العاده زیبا از دشت پوشیده از گلهای بنفش گون در دامنه دماوند، امروز
🔹
مجید قهرودی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663381" target="_blank">📅 10:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f558033c8.mp4?token=F_HbMfgG4meL7CQlCdextAxdtDnYR6lTseJaaiUQPN-9jsPj3cMGKXarZa7oOvDkKBT3DquRgLqQTjr6rvFNGtrbxk2hQJh5vE0464Ff_qRoFcnl4yPJY7KifYOO-4XxcxetCqec71DzHrw4cEI3zGevfzn7h3tfNqUw2JqizhA5Ox-NCNX97tQOmv-E1I0kUGMLK-YotEyP6kmOjgGM5m77JcXPI39p_7Gn-KvLJRMs2WPcJ6dhRXdiDRVso2AvdJXeNU9LQmpvpCk7XYBYqSkoeoYf85ASqXmBZVY-cMEFaxbcSAt6JNyhWXJOR_4QaAnlWz6z-K5WejxniLpFWJdL91u9fLtwKZT__GTdiziY0qPSkcr0ONFCNXDi8zPCf99SyuCkdO96WWgPKeWybRIhqEkMryTG4lgmFblppTn4B-j6Tvt9TkaDAoTB4oY_I9COUWFP6b41i8pcLM0mako8YEa4xEndd0cj6qrcr-XCZCuvZrk-dJVO6JG-QKJtwcGUtZrleTa0KdJ68rwsJJU4moR5zRxTqqpGD1tQ4GDcND6fg4aycUaB-auY3sz4L5e9xBfxI7nB9ri09ArqKbHB1GcQimmUTU2gCp3mGpqpVVMp1NFgMp8spK5R79WlqGp6UbnDo7GnVO2h0fbrH94PdZIRSGcyDqcy9QFm1EE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f558033c8.mp4?token=F_HbMfgG4meL7CQlCdextAxdtDnYR6lTseJaaiUQPN-9jsPj3cMGKXarZa7oOvDkKBT3DquRgLqQTjr6rvFNGtrbxk2hQJh5vE0464Ff_qRoFcnl4yPJY7KifYOO-4XxcxetCqec71DzHrw4cEI3zGevfzn7h3tfNqUw2JqizhA5Ox-NCNX97tQOmv-E1I0kUGMLK-YotEyP6kmOjgGM5m77JcXPI39p_7Gn-KvLJRMs2WPcJ6dhRXdiDRVso2AvdJXeNU9LQmpvpCk7XYBYqSkoeoYf85ASqXmBZVY-cMEFaxbcSAt6JNyhWXJOR_4QaAnlWz6z-K5WejxniLpFWJdL91u9fLtwKZT__GTdiziY0qPSkcr0ONFCNXDi8zPCf99SyuCkdO96WWgPKeWybRIhqEkMryTG4lgmFblppTn4B-j6Tvt9TkaDAoTB4oY_I9COUWFP6b41i8pcLM0mako8YEa4xEndd0cj6qrcr-XCZCuvZrk-dJVO6JG-QKJtwcGUtZrleTa0KdJ68rwsJJU4moR5zRxTqqpGD1tQ4GDcND6fg4aycUaB-auY3sz4L5e9xBfxI7nB9ri09ArqKbHB1GcQimmUTU2gCp3mGpqpVVMp1NFgMp8spK5R79WlqGp6UbnDo7GnVO2h0fbrH94PdZIRSGcyDqcy9QFm1EE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری تاسوعای حسینی بر روی قایق‌هایی در دریاچه دال شهر سرینگر کشمیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663380" target="_blank">📅 10:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XH-Eth5Odgw3sNOBqEVAG4tjgmj8-gia2bGPXSqtQQ908K4RGTzfFq_ZQm49FZW0bhR7QfFRfLTqdyesQgFhY43CkT7oQkDxNDq-f-lMvqZCNYNUKpEBOzJD7KyK6cL2k7mtHBG_ahFikfB1S5cRFdQF2iqEuDrkBw4JE566e4rRUea7UZ3byNpEKxVXEv8snFNhBTiwhdbQXDTkQxkg3bnM4zAmoKEVD7XmKP9m0yphTXCh8Sw0IKPpPt44679i7Uuj724N2m14uNCqMcovLGNgeCfSP8obCHzQjFgStxvCOCyhd364_4J6hH18HVY69rgezfXPMLGwwoSjlvsO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۶ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663379" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpIfJv-ZDTYzvW8IhfSqrp56XDBPu7izXaxhBTb6Jhz6F3-JwZ7NHlX6_kOsh2MyAmRtpFEMmdGsz_c07fvbbrPAD4ZVbNLc7Rrmpk_S1Y2r2CDDE4LSH16HVLlD7HeD0ySZ-ZiKYr9A5JdLWM0rQvX8HG_b9lOK2vf1_9-QCUbh-dZ53DlMDr4MDUAorDjlcWWRgNw1oWSyb4tzKymNkHPuNSM08CKJ3IVSriWcufxrWxZavQ7tpY5YG5VEGWCuvq6Um15ifco2Vb6sTrC70r4wD07ZePlgY9hGJVbCTDNdd-TX5vuZyY7_CV6S9bkC09Xhem2pTD46TTnHvBQ6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل دو تمدن باستانی؛
🇮🇷
🇪🇬
پوستر فدراسیون فوتبال برای بازی با مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/663377" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663371">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdZHDwcPrDNYCmQl4vVfKVQDWYQsZPPr3Iv9gnNdXCnLn6vTl7TG236poOW8Bg6f4vHHrHB6n85GcVs-z0zMsHBzo4O77acTJpLdISm7UK3japZkk4XhcTF2yAbujDy5WEhIZZ1MBugvCq0sDAGLh8XIKlWdJepFoNhLfrEI8ZMmbdUJSMZBk19VC5If_4sUr3dsmh3_Mot6SKRdThVLaIm_Ay_87E0nTEuZhlnkyE0_VwaKAQtjQijxYeUcfx3AcV40Qe3l_lw76dfIqGCHFM1Yip2kcECQUHSvvOTV8D4v-mZ0Ny8LqhKSdbx7JKDwClSk-oaMFIVouUxHRD40Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDUIv8805mGKa4G70s0SEgGIlclul76kHtMeDV-DKj6v6EJyRc2ZEchT8z3zVjmY57ZrNwGCriOkGGXa0wxfiboLmtS71TosMV-Y9slq26hxO44PnBM-RncMn8b2w3RmiLQCec9zNgxa7kAkOC5VYVpzW77cT0q1NE4aLn1_FhAgPOVLHQdTGjU8Qq8sz_eOmm9pOVmOppskGPPOM0EvE4Wm7Gn_x24b_qd-edCnVglSmU_Kx6Itm7Ob8Q6Rj9Ot0opnhtZEv88KOKuYcHWRcfNfRY7JDZg2Gt-XmgFsdZyzs5ZZnao354TVERgFz0TwZOfopcWRLN88A10BVfKJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNxmI8RsOCOHT1GTfRkpznlsqsbpOglxbFxQ6kISk6WvXWgK9jgIjIy93vbpjPTXT41pqmVEL-feu7TOznymiIE6BYoulObVSvbd2iOX2W8yPgsgAe25n5lZlQOnNCjGi0FRiiGzOt4fPHu6J5qBvgM6CI4pEGFPWxPJl1ZPyjMx-acC9zkTY8dQjnxaLbI8FCKeF-RUfxAua8FKJjYFFGU4hLRZmC9Em6vRlENEi2ElpMjuigQCmUyG3238DkGcaydly_2IYWwsDPPtpd3g0uC241XKZFrNxMjWSpSWWwmzGOtSjw0CMVbu2Zn1tszmSCphomxrobWSiOaFMBwpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLmUHInosEWjGhVFAGAt_EOiG8_wt4sV5chMteaF439oAWzuRReDczckWqnRytgq4lyW1KkLwwh5-HYFJcmslYN5q_pmRWmeYEtTheBqVkgUHNdLCav6L0tjooolqgiG_82TsC2MG2XO-krmHMdfqtc4ZpZjwwMqkR4CeT2YlqMvblYWDBBnHLHhu7pV_hN1UMQiIKha6Mu0YJL_nTPArAOXn4TEttPpAdS2_qGmdXDMo7aRTtVRUyagV6CgOKI6YBS_q9KOAKy6x6W1KGHyvmvdDdfC_WE1RjN1OpARIHzhh4dupZ4pHX1rS535pdCnNSNjxCuDpWiM4rAMNjswCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_ZQsOMWYvVPneKfgrIWlWHUOBhhrKBQs4vHELF4HfTy6O__ej4pxnCeU6-s0xiigJr0MPnMDAbEz6On9MLGC9JTzPC75Bbrbv7QX-QNLjm2K1HI1KYuUIMHfbH9tU-SzC1H6lG7JuSArVB3w-FCGBrUmt8KKPnFfirheAUP72yC50QY334qbfefOKks0YNX96on9pSviCgTNHM_yy_rYt5UHcb3Ckk2zBjLUOndDlI3ScpdVmXdkJ8BZ4JHYuIvgIIpzrhGK2ubUJ_D1Nl-cQjw-gkjs4U4GTrCwvsoowSlIifr8eW9591jnDuO4S1_6htaqnAaONp0HzdZNZw5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcmgIsjCXTWaAfTlj95aF5ioG_3uIq683lY5tLO16cuPlzkW0gXroTp2uKDw_59o4crMPIv2CBH2c9tBw7UPU72EskKFJDx87A8jVkfMaKNA6DTDyGuoFy-hpOQnc49ORW1vCphpVSygKXL7XHlfy1PLXV7BevbdQv4v9WvZgCgtCRmbO8D6BeaJQtA9lzpSDS4X1yfSGD7-IMDyzrjYXz5nXLJOg_QHBw_BqYbZV3RzPNd_M2jY8Uz473e1o1gelrD_DriKF7r1tr-NdPjOJ0jJwjoQlh7R-dFXbK3S8-z6GpVKcC9iqSbRSe_b4X7iST6Kqdx4NlV_mbsl5-FNvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
فقط با یک کنسرو تن ماهی، ۶ غذای فوق‌العاده خوشمزه و فوری درست کن
🐟
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/663371" target="_blank">📅 10:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2OpuwGS7-U8adfe1csumWz7QLyEOSpqyGl2PenUg2bsBuRaghXv9pMDc6G8ezp9UwaD26s5D3gSk8KX6EOCz-oD-JK3PqZKOgMam-nggIaHuUoiPfNzL4JaO_H3EP-wm5u8sVooPCO_TZEwC0LbBhj_Rwq7WVpG95qYsF-DGlUTVKI-mPlvbNzizhzl4zR6WDQLfs5B708SQay0LrswjK0qGtmxCFi4TE15F3X1C8rv3ClB5_5vtP588ukBqr6jkvL-vivOwJGeEIVxqwcMyVFLKMcBOnbo3w8IW6z4BvcB89VqxIMLWnUeo_W0ckoaPFsboBIdzx46rblZqJfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کار ایران سخت‌تر شد؛
آخرین وضعیت بهترین تیم‌های سوم
🔹
با مشخص شدن ۴ سهمیه از ۸ تیم برتر سوم، شرایط ایران سخت شد: با ۲ امتیاز قطعاً حذف است و با ۳ امتیاز هم صعود قطعی نیست (فقط از کره و اسکاتلند جلوتریم). همه چیز به نتیجه بازی با مصر بستگی دارد./ فرهیختگان
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663370" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663369">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI_jcNxHZlpKmViSZwu89OBDjCWjolp2_JV9hen4QRiPf5GkY0gbqv5fZTvBEcpFhmY2bYx00sJ-WqiteI7gQSf-kCb-uaTCw3AYxTtATa8H6DwuDfv-rervd5q8va7mDcN-CylcnQzQMK1r1lwy7loOB2QLlNdZMnkBeH0A5RtEYLOyhf5VydvVf7hRV8QyQ4HfbxTDhCo_IDRk7NJJMGzDiZ4r8aDiXtcIu_DSb_jonBtpwBaKBeJZHCSrwR-YriSMETaIT7of76BFx9NGfnIvdzEEHy49xhqQQaMM2VaDX6J7W2wS7hno5O0zr18udndg_tCxtnFvScVa8eSAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
وال استریت ژورنال: حملات ایران به پایگاه آمریکا در بحرین ۴۰۰ میلیون دلار خسارت زد و آمریکا را به تغییر آرایش نظامی خود در منطقه واداشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/663369" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663367">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برخورد صاعقه به فواره مشهور لهستان
🔹
فواره معروف در وروتسواف لهستان، پس از برخورد صاعقه قدرتمند در جریان رعد و برق، آسیب قابل توجهی دید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663367" target="_blank">📅 09:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYQdgEl4NC_0vsJ5BdFG8Q4Fl-TPp9zTrCmPgS4uI7kodfUcRbR3XNQyHl79k6p9Pbc0SMD4MhPoeCLokdW3NiieCksHJ04ewcNbblaSixRF1ecINm2gyng6kiRvSNjwYiNMGAM-FBz9L18klHCW75NVtuqskHb_KufjeVNWz9W1oCaMo9vx7QNMjSpvfoYd4m8grQQEN2s1Huhxwc3X2hICB60gFiMFhHv3vdjfIoE9fraNb61A_42U8qwagnicvlvRA07SHqTeLZvUa2CXjhmY-Mo_0O5x7X5LQv3gIvbNHW47GRNOa6eUEabYlgxmNmYk54rpNhMegvkveBUUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همه سردردها مثل هم نیستن
🔹
سردرد همیشه یک دلیل ندارد؛ از استرس و خستگی گرفته تا مشکلات سینوسی و میگرن می‌توانند عامل آن باشند. حتی کم‌آبی بدن هم یکی از علت‌های ساده اما شایع سردرد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663365" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیل وحشی به اتوبوس نیروهای هوایی در سریلانکا حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/663364" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3rEp4L8Db7Gizcy5S6rmY7lVhsG46o1THnd2EpqgpFbqKrIN2_bLJGAd7AqFfgvCUGX8XTshCyLvVaK_oHKX1GFTLSicgrtsWSrQ7ZoUKft58_L3U--pi6Gk_HZHyAmlVdOy3yN8DQ5KztPD35R_awvH35TkSjBVXb0vHO5o7RH6wqFsWrOAgznwshQgKMLIPPnBe1ByXZdR71Cb-jCipvTLwx2ndvoyrwfU1c3ek4UOQ6uUkW6Txf5kGhzq-Pc789RS7tb2m56y2KGVbESYX9Ha6nBqFZalxrY511cIAPd11Cjs2TKFTh8Ch5G3c7AmS6f6iiUMxPbZe8t1eIibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بازارهای آسیایی در سراشیبی سقوط؛ بیش از یک تریلیون دلار دود شد
🔹
جرقه سقوط با افزایش قیمت محصولات اپل برای جبران هزینه‌های تراشه زده شد و نگرانی‌ها درباره حباب هوش مصنوعی را شعله‌ور کرد.
🔹
کوسپی کره جنوبی: ۸.۲-٪ (۳۴۰ میلیارد دلار)
🔹
نیکی ژاپن: ۴.۵-٪ (۳۵۵ میلیارد دلار)
🔹
شاخص چین: ۲.۱۵-٪ (۲۲۹ میلیارد دلار)
🔹
بورس تایوان: ۳-٪ (۱۲۷ میلیارد دلار)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/663362" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE59kcBWxz4yJBmXYG9SN-pPEZTBQCuvQrasiVB7Aq3lFlSRQ_G5khnyPZOb8M9GtnF80eFz7jATHirAK9zYh7a_Y4GG2ZuSu7334OxcXg_d7qeOb-_-idpqlvJHahCdB5VLdSUlcC64U5AkF91mvA19PwK5BjXSK9f1jWK8K0gsJO4Re06KCJ1ICkYv-3ltZlkHY0ujgCfYRhmALPFAN0s1BWxi9ANQJGPgwjb-xW6hzg3LGACNtYAGpk5PwsLAsSJ6LEnsLgFOJhtscFU_0g3YSkhop_FMS0QyvnELOIR19p-X3PhdNDLO04OThFYNCWNhBfyexhl7FAy6kkzJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgQ2VI3w1ouBiILivafDio1DGqmOOcBJJ0wagkVXw2E6hSqHtFVqaVFAcsycqXKam8FY112NOq2vqvnu0hrcDxrbbSSSjnFHoHNQpyJdP1-qRowVG8BqomGAo3o1BLn79sgeBFD0-6StUqE8EtaXafpLKn1xGJa0Qwb6uSD5Se8hoFVm0R6fFYdDfEnki3XsgbwepSOpRzvqa54yEY_SHjSbRnt9vQ54J_BezlY946R5fK3r7k9_RxZwC9QOnCfXR28fCKygbnZEloqwOuRKBvE6QeCt9x1rieXlhFkm3GWhdlRQD1ol4X8A7MCnh2yodYFYEtEGmyGGyiNjbhCn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2GPTx9m85Kv70Dq4iTX81Hfb-YN0WKk7q6QdPJhdRZXTKTCEVmjrIsBYYIS68ZlOj8hvDw09zgubMsP91sMhRsa5rimu7r18W3Hb2DkP5x4RCJnq1yqrPOaRPvGUiipRUfWlvCcLr_nKNQFscBqaU3Tru9Ba9Rl3B4eE8CXs6p1d25ykkIThgA0QOiIuRbZ128lI_B4xgu09GyMr6u0Fvap3EPCmIj20ddzaySgiWH0f2_6fgZ4sG1XfYDhCeWR6GF5GmkYB7eaBReEsA97IYGOYgba4wsXU08IewHi-tVf2_K8cavPlWRH-5qHSNb4Ro9LYi1PXOIKR7rOMj9L_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iio5jXDyyR8Qup4cRbbyVfZEq_XX1KpQS-6PuFh-AnFvoCZmg1s_WLjvkC2RnATETf1QC6xaqu1GwGL0vR2TC9_G278EpVJcMkBr4hmKvm8iGLfmq8v18eSUi6O1YWuyBTjVIn8hQT0GmJucEeEuqhwO3PXWRZM7R7dJwayc5clzjAtD5AOLWmDsUrO6bFT4T2hFrjTUR0e2qn-cy6RhDcp-ZwOlIckSjBXOot6hXRXONj9dOI22qOMsbe839WeIcDr4eMoQBDhjWXy4wu5ON86_HYnnnkKdfKK92GEeaWXzhWoDZrMP-mOyq9tKnREJ56qOWH8hQrUQuTvZZMEE6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید ملی‌پوشان از ورزشگاه لومن فیلد(محل بازی با مصر) در میان استقبال هواداران ایرانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663358" target="_blank">📅 09:30 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
