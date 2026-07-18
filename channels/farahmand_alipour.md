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
<img src="https://cdn4.telesco.pe/file/cbU3eORFKmYNVSaWUlIQMdEaNUhjNftOgBwQ1h5nHZ397Szdl2nKaEWa2E3WS0-f5klnTNxrnEtX6ckcMQJ_mlvM5exD7qdh9ILCj8PgAZD8xcT3e2a4BewtfomKlz9maQQ8N5hsJ67-cOHiMZkEw_-1f12kU4f8OllskMgvBPTouWNppR1eDfpIuOG1jr3yYpSqBjySfmHIhdUOjZ5M-k08rUcUq6GHZ2UFgrbnplzhFKqyNkCbj-PEDdbAjH__6FZfCWZGoM1GW5hxcatieEb-AAHpFq6mIYMVoyZptkXZlPY3AjvTVZ-LvjSeAD4U86Unv89fLJ1N6Kf9m9nQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 19:15:34</div>
<hr>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjmUzi9johmzWQWPuTw11kOZKyWRKZE6Rq4YsD-fC-AOJBezxFPt7NthaHW52aQmB4njlxuSuayXzefi1ocVOFcSfRW2vukC5tY3NMDNNYIA0ZDGKM2k1FGiP9snPbUkywkhXau0AlEjyomIk3z2tvODd2SMM_2TcviHl0IeMWRLOxlteICESGIK9erT5m5Fx2N7HgKhsGjQmM49knQeffVHfmTk62Q0NdMUZWXIh4Jm-CWb0llYdR1K4uB8RmuhSgiHd4wwfquEMCZBkk5RiedxUKNo1fPi0jsLkKKhPTAHkqb8i2pogu60qQuo6h4nXlGrDGvK9VDou57v5AlDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند. در یک هفته گذشته جمهوری اسلامی معمول به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدید خود قرار داده.</div>
<div class="tg-footer">👁️ 352 · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxEBTaWPYFYgBoVjH8ycpvW7Ua9nXYqGenHF4kmK2m1AWxh_9EwC07szc_QqWWZCgY6SgzCzjfx7XFjgGE1s7XFA1TAJ_kL62Up8UuHb67pnqdZdFlcg_ivTvhMbHpq9TXPqgtXkK1q5pLiPzVBfmiZZp-2RCul2bpMiz7jylxPxc8MFTuSQa5RSrpQlgiOoeG0f2zyfdrAzYVCZhx7jMulFQxSWs3vFDCxlwJn4_-i-4jiQmNe1gtSl4DhaibvLakRbvGCSU4QlhYX_DtImhB-gJDy3QpcnFwqXhZMZM7Aff4ZoQ-hRPkynDrR1VjRj5ARtUhT5Yn_-JNe62s_Ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=c33Bj3KlieK4IUx0iACiuEn87dZNDCV0nwOLDH9MKHP8y9MtU0dM2H6cEsyklFtnUU8gdMSSb9lwoqbFXFABGgEsArlqk1FaQOv2tiHtbpQYRk_hw-r0fvRyIo9ocV3VLbEO1xU5UfMcstr43HRuSfOfpkM-qkFqi1Mtnta7h1KaCt09BstFTUW5sQXLflPob66u55OrL7QyBiNNeeGR2UNimiJmLV4K_SAZfsRK2uMwj2iIrPchRpUmC9jOA6tYJ3Y2-IrFWIQ01I4BnuHCkZHXgbBUU3vF1Gni8uI4XF6_zdpGtJZts6RJaGVJNKd4ipjt3RNazoR3GCKfWowM2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=c33Bj3KlieK4IUx0iACiuEn87dZNDCV0nwOLDH9MKHP8y9MtU0dM2H6cEsyklFtnUU8gdMSSb9lwoqbFXFABGgEsArlqk1FaQOv2tiHtbpQYRk_hw-r0fvRyIo9ocV3VLbEO1xU5UfMcstr43HRuSfOfpkM-qkFqi1Mtnta7h1KaCt09BstFTUW5sQXLflPob66u55OrL7QyBiNNeeGR2UNimiJmLV4K_SAZfsRK2uMwj2iIrPchRpUmC9jOA6tYJ3Y2-IrFWIQ01I4BnuHCkZHXgbBUU3vF1Gni8uI4XF6_zdpGtJZts6RJaGVJNKd4ipjt3RNazoR3GCKfWowM2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux4JP_UJNbqObqzZZGH-AGkv1nLgdm1iw5prRe5mWIBgNt97bMx3F6s8fY9k_DywtOszslc0ueyJ2KtlmAx805UJOt6lF6bxge765DarpSkqzzQaIaSAt96k8welbnTmoiH4uHwrTB-_hTFYRn8acGS-_U1WNQ3w4gycxmnIStTvxTxyDRgb6QEHnzl7FYZXUBLlyWSlTuOzFJazVoIQDjp9G1KkH9fuDhFt0TFMc375alVrc8zqZaUwNcwPOptEG_v_64Gmz0VGTprTLIpQuNxwzbLOg5DEXPHgVlVXFMDZSi0nR4m8Nv4VUwKsH0eGmevuY4PLluKOw7oUeM9rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=vetZYwZ3EPxg4PcjohMC7JxE7h5jIJkIjJqAU1RtiMgczRt75GjvfGO20npIx6GH7tlUL7aHJG0WSpbdmHFbtWfcaf-8DKHkf0iLdjCsLc0pmrZ89oW8htXz8CRGzZS_F32fj_fz_FJCLehfvw45Cswgn1zq2KHj8wWW9HwmwWfhZ3rN5FVYFTNTvtYkWoriYp1IUOKcDsXQsB_uU4jCg3n0dpLP_X1LveXwBzxQq2xXedU0CBIL8N8vGNCiI-JQgeo4fJX7-P7XNgQ-8HGGomLvIzd1nOdJJmtv_ACcZ0Tm2itHLOWRI67H0cTlL0iQ6uTgqCggCJu6Q91q41xZQWqiUFCgNyAltPHHzlTjPQ3faCcS2z62eDC7jTA3BLBMLQ5xf2tCwv8WOrI3zB-tPfy11Sh1iBwdaDF3IwUgHRUgr80hqx8gQcFNnsQfLZZ8bB1DMl8iQz-PhJkxS9yClUfuZEcBlIOFJH5JnUcTK26eaPqbtwdrUMJLqwdod3o9Khok67jByNgq_-G7nTyzCd_FJ0XSpU6ZQiemeMsSS4Qaxttf1r-fcCXDRftJbVd1f5nCPbXaSmzjw2cbydiCy_1Qi4tos-hoTI5EwQP8ZrkrPW-qxsEr3cY2DWu_u3rjohuRrSQAlJCpTVkJAytVGIG9sCuc29XqIQxYYrJ7EDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=vetZYwZ3EPxg4PcjohMC7JxE7h5jIJkIjJqAU1RtiMgczRt75GjvfGO20npIx6GH7tlUL7aHJG0WSpbdmHFbtWfcaf-8DKHkf0iLdjCsLc0pmrZ89oW8htXz8CRGzZS_F32fj_fz_FJCLehfvw45Cswgn1zq2KHj8wWW9HwmwWfhZ3rN5FVYFTNTvtYkWoriYp1IUOKcDsXQsB_uU4jCg3n0dpLP_X1LveXwBzxQq2xXedU0CBIL8N8vGNCiI-JQgeo4fJX7-P7XNgQ-8HGGomLvIzd1nOdJJmtv_ACcZ0Tm2itHLOWRI67H0cTlL0iQ6uTgqCggCJu6Q91q41xZQWqiUFCgNyAltPHHzlTjPQ3faCcS2z62eDC7jTA3BLBMLQ5xf2tCwv8WOrI3zB-tPfy11Sh1iBwdaDF3IwUgHRUgr80hqx8gQcFNnsQfLZZ8bB1DMl8iQz-PhJkxS9yClUfuZEcBlIOFJH5JnUcTK26eaPqbtwdrUMJLqwdod3o9Khok67jByNgq_-G7nTyzCd_FJ0XSpU6ZQiemeMsSS4Qaxttf1r-fcCXDRftJbVd1f5nCPbXaSmzjw2cbydiCy_1Qi4tos-hoTI5EwQP8ZrkrPW-qxsEr3cY2DWu_u3rjohuRrSQAlJCpTVkJAytVGIG9sCuc29XqIQxYYrJ7EDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Wo4EjBIR0Olh05jMmiMQuAmP30rpUtZU35hTgBVQXIwpsS1cWnndDa9kJtD18cHeMCoWMEdEplCIvUagxXN_PiuFPzLIhy5HaPsNGKozJ_A3roMr5fAfLqTQ7vwm5k4vFpMn7PiXEG28vt1a8ibmIiXIpK3AQzltFwoLgHkFhTnj1u6iA3IzaKm07j-8XEXU_co6ryqiXZGCGR0MycHhSnC0G6Xs-4R9lI_j8wWTGQXZKu0LzJfTZg-wYwXdBUYMWRb6MxxhaqczUPdhITcyC3kpFhnFEquaFIbjMlOdtxMGIK8g-eVkZA8KW8KE2J2Xi8OyvVAr1jHe7MJbbiU2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Wo4EjBIR0Olh05jMmiMQuAmP30rpUtZU35hTgBVQXIwpsS1cWnndDa9kJtD18cHeMCoWMEdEplCIvUagxXN_PiuFPzLIhy5HaPsNGKozJ_A3roMr5fAfLqTQ7vwm5k4vFpMn7PiXEG28vt1a8ibmIiXIpK3AQzltFwoLgHkFhTnj1u6iA3IzaKm07j-8XEXU_co6ryqiXZGCGR0MycHhSnC0G6Xs-4R9lI_j8wWTGQXZKu0LzJfTZg-wYwXdBUYMWRb6MxxhaqczUPdhITcyC3kpFhnFEquaFIbjMlOdtxMGIK8g-eVkZA8KW8KE2J2Xi8OyvVAr1jHe7MJbbiU2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXqlGutcO1Af2MaepQ5rxdqjIfyOaT3EBPdh7ZS1m91ZRbk0Bn9dvWbH10Rc5J5URhZ1wDc87z-397gOJFindgh4IG4gKW433HmFm5DcmwSgckFT6QZiWmrtR4Yj2kHlL9mcMlPqZt6TZeg1KjzsVNM0LNIuXlcOJLxVpZSR-OquOAEWoEVIJF4Ja4ocq8uwwDucCirMapsDywm20NGzV-cUYkLqTK3lldnV8CJ4f2qpJ751x4_NwNIXcz2QsiNLmIzVlTeOMLNup_OyyKq_cBqtl-nbpSw3U74qtnmEQ7YoF6eE8pgkNOFfHhUaPIjtIzFKJ2PhLkhDeLc6Bh_Z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h34S1sitHZARC9S9ZgoOJEPSK4fO_qebyzEGXAb-Cl9mGBx-dzESy9COaR4HhY5RMdSLimRIoywb7a0cImifT_i5vlM9RV2UQwrWWOHFBlwFz3LrR3_FnKiKWfYo4EszRg-Ub246J494NB44jsVsQM7sj8clZY3SYaG3j5PhDMLnKIjJpXJ1ETPjUBHOXuuVZlfmA0HBxH51ancdJXeaY_D9fsnQtc2E0zUyWvudbjkjb3hpbuMtTjimNHLxH0P49KEjr0Zwmxkiu51tOMjSPJ53Zkr5Mcixb0w2rBVkyXPowOMHTOd1tCW9dOnbQHLdU5-wcz_0oGUktHrD0PLcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9net7Eb7CivbX83RYOCmz_DqYEDXMpfHbRwWkTcfiEoJ40JA42ocUfmfceN43G-mxtrKr2V7GNBW9ZlSVuRGBt6WDwDH9G8vBlIcAxw60F1kXsUEQrgCrMj4bz4M40RVJkdNRY8dAAl6T2riWentWu_MixPa9zhs5aeEK1vg3QG12mWdvLyrXTZNbv-fIM3Xi4jTs0mY9JBeIIUUb6bzkgKHgHvZEXw1h8B4v5447eooPd2XPG3tyxIgYEbX2isEOlQvkjpXTKb8unvssIAHzZiAg4JlLS5zL9RaZIkWtAEjc64VzOmXjxw4WFjSDdn6Mc7-Zoj-5FryJQd8OpmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JoUr_n53SySt2qqfJ24vEGZqs45g1ORScOf5UAQCHWJApx9VFY3zgv5Pjc9TOhKLjyAM7KIdHRyQvo6pU5oPPBzCdhMNsk8rDXUHETMCpp4FQimrPL_oM8HD_7NZ6SD5eDwNlF1fhvUWznkUlAtpFgeSmNrnRn8X_P051E5CyOiINoCMntq3kUkHcbcDg4ZMFhWgdFnGC7IhXHeVzktXvg_YkAMfQsEQmhRQKrtHaQPe-WwDEaR8IYhp5wQW__dTA0IQBDX707Qm_LuBQfpXprKfI23tMvnqYDVTk37QHE4BwUfzqew9HQLizBdgz13idV8hs-tclZ11SLi7oAIE0FM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JoUr_n53SySt2qqfJ24vEGZqs45g1ORScOf5UAQCHWJApx9VFY3zgv5Pjc9TOhKLjyAM7KIdHRyQvo6pU5oPPBzCdhMNsk8rDXUHETMCpp4FQimrPL_oM8HD_7NZ6SD5eDwNlF1fhvUWznkUlAtpFgeSmNrnRn8X_P051E5CyOiINoCMntq3kUkHcbcDg4ZMFhWgdFnGC7IhXHeVzktXvg_YkAMfQsEQmhRQKrtHaQPe-WwDEaR8IYhp5wQW__dTA0IQBDX707Qm_LuBQfpXprKfI23tMvnqYDVTk37QHE4BwUfzqew9HQLizBdgz13idV8hs-tclZ11SLi7oAIE0FM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APYyv_kpI8G15xHO3qwDVycKkWQo7Z2san4Q2mH1tZzEIDg1_LMdbqe1TnOF9WdnMyUq6EMcF0olKpqNwO6H0Yl_LE5hsQps-GB7JBWzyMRZjPR7TYXNdOxWnxec1UAw2AThTVn2guRR7Dct6HCiqUowFcqfhQMCP0rWI43WaIchFJne9Tw4DHtr25gSTGtGNsGVDgnu03FPSusn_kO_7MDaXLvj3DRgiH59cHNP_6OBGvhoV4FvdiVmte_cMG0Q89lDmvAxUvhFGU9ezSMAT31oAkk4KdedCzEJuHQf9J-4E9yL1vkBOll3GNk2mUHCo06nAb7EkBgVwwS7XqYSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=NAPizL8qsdQO4H3HJ1ei25pXE1dX-85kfayXXJMLwVDGJGM43LFQZnvU6VQLemhbwlaH8-Qn7Psa4JiPLbL2UjpJSYXrJpqMKzN0t1vvodX6xyeF8Afz-zHUvJjRbLRgv54jUuCrsjeeFOQuNbRUm4DpJfs_KkiWEpffLF6cuTj76tBX0wsOCH_G8_jp6w9-R-eSyw5itYfqAKSut6Lnlve9nK5wk9CoPKu0GcH6TIeH9mXgBAz4_Habf1ofhYBKyexqszm_7K2w-qfieN9thkrZvQGZImV-6K9_JwgZjCoR5_AeugOXlgcy_LAO2xJJiei12S2uArMy7yKrZDKNsVnrtNDpK6iLNhXoDlaCP43YKHtjnR3PU9ixsnRn43BhDtscOlJYgHL_W8hzRzh_RpxjUVKsSC-cRlNsZZUgOuCL4ToFKB1XmFs_cZyoFu4U2CdVQ9mUV68bAE2lx2wkFPztXrONdCY2uMnay80-GaXxGPeqOTPreEN8w3OHs2rWOhxck9RGBRWZdVApafYI73ZUYYEvQ0cKLwkSQ74Vt5HEPuF6JJ7530j-yu3-nHBNGq_u-whMSPuIcCxqAa01ndDRwBJkpdiwyPPUyQ3izkWsFmifJhNkRSh8vvcZOmu9lW8-87DLf5-hMnd-rdrCZZ1ZHIig741HnHDVMwn2rOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=NAPizL8qsdQO4H3HJ1ei25pXE1dX-85kfayXXJMLwVDGJGM43LFQZnvU6VQLemhbwlaH8-Qn7Psa4JiPLbL2UjpJSYXrJpqMKzN0t1vvodX6xyeF8Afz-zHUvJjRbLRgv54jUuCrsjeeFOQuNbRUm4DpJfs_KkiWEpffLF6cuTj76tBX0wsOCH_G8_jp6w9-R-eSyw5itYfqAKSut6Lnlve9nK5wk9CoPKu0GcH6TIeH9mXgBAz4_Habf1ofhYBKyexqszm_7K2w-qfieN9thkrZvQGZImV-6K9_JwgZjCoR5_AeugOXlgcy_LAO2xJJiei12S2uArMy7yKrZDKNsVnrtNDpK6iLNhXoDlaCP43YKHtjnR3PU9ixsnRn43BhDtscOlJYgHL_W8hzRzh_RpxjUVKsSC-cRlNsZZUgOuCL4ToFKB1XmFs_cZyoFu4U2CdVQ9mUV68bAE2lx2wkFPztXrONdCY2uMnay80-GaXxGPeqOTPreEN8w3OHs2rWOhxck9RGBRWZdVApafYI73ZUYYEvQ0cKLwkSQ74Vt5HEPuF6JJ7530j-yu3-nHBNGq_u-whMSPuIcCxqAa01ndDRwBJkpdiwyPPUyQ3izkWsFmifJhNkRSh8vvcZOmu9lW8-87DLf5-hMnd-rdrCZZ1ZHIig741HnHDVMwn2rOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BFCY5oYJi647Qoho6m8oftQY6PO1aDrgoOly6ArGw8HDH8Qi1K2fqgZB4wJCO87w2JnbiznGCY9HTvhezh7m-oLdX8sNJkPb0B-YOVQzdik096jnN0G62HC13CE92KuH6i9RAGwcjWXUL4F-6Ply7pxq1rFxLYtJLn6Z4yhpI2C80bDRO6MAbHLsqPjaEAXQf2hOgKcTAOFiDORnp22OMXjpiwcukrWSfcH52ybyAna398UoGSzxMBB_DaTG1zyLjPvnn69Y-fkZEolYYAzp384P_upkzjhG84Ye2YS936W1FIkTx1mbUchCab0kcEAZGv2uStNNOEbBVWU0XA2htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BFCY5oYJi647Qoho6m8oftQY6PO1aDrgoOly6ArGw8HDH8Qi1K2fqgZB4wJCO87w2JnbiznGCY9HTvhezh7m-oLdX8sNJkPb0B-YOVQzdik096jnN0G62HC13CE92KuH6i9RAGwcjWXUL4F-6Ply7pxq1rFxLYtJLn6Z4yhpI2C80bDRO6MAbHLsqPjaEAXQf2hOgKcTAOFiDORnp22OMXjpiwcukrWSfcH52ybyAna398UoGSzxMBB_DaTG1zyLjPvnn69Y-fkZEolYYAzp384P_upkzjhG84Ye2YS936W1FIkTx1mbUchCab0kcEAZGv2uStNNOEbBVWU0XA2htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5moR3gr6Dhku2QqK3eBSiUj6yM7VgpSjb4qUXnTxBhSgWkABaX3o7xVIlXnsfvavJ9QKV1aCsxxT_w7SYKksA_LlNj7O0OZQVPF0CsgpdM98Pmh527Fulcppcfv3h_KwjdPOG7JopAcNu254vmgwggJlyEzUq6m7VZsdo-Cw9nHbh7yPLjiz6TXrcZXE58xNip3OgdRL6VxmHFJQyj2JNfnEZyZHWdZX38XMlMxb-xRhTDmcZ63VriFfmkBPmppWOb-i2d84zwSOfHLNr2z0Nv4dXTUuUCku42SPJusfIiYSD51W1VcWn2mox_2xzqyk5vdCqEu63S_fJfy-qJHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=EMg8bqydSkWtyW269hOifaP5I25IKC7cX4Zm3xDnddRoMuQjyHgavTAmZrROih_lGcvHfTcZKjCHAohgFsJhdcS7D-lUmwIHnpNBbdYMaQJzWE_voYGTdZ8VVc1r1pJnsSGffmX3pbECRmeGs6qmy5GNxalIr54sawSVFCOBqgWWVOZs0isdGdrOfIdh28O4hj2S7kH14JfL3BsRC-gmRsUES_W1eOyXdAJxQmjC-CJ3hG-09pQT8XF658qhPMVl7xzhZZ2D4pdqPunL_HgRdRJc2I6WNP9WVMnrq19JDIvJOigCSNi2ELQK7lK4RNJxHik9W9vHA0KtLsGDomdKnitTXntkWVGzUlkRz_La9ssmagZ32PO_2zeVxJKnjkEOTdIyI0X5g5sXfD_FPQQNJPL0f_3DWLEdP8DQCb6fK5NpaMAIdPV2IDDpcuKjeIK0_nCoRiPAIBmam6YREyvSlpIMWJ-aTdEA3sU4QOhRUpOjWkhwPmATQUAoL2MykqykqDgb7nb7Mq2IfKykQM0e4-queN7u_fqKvv2CjW7_h8p_tNEiPINYqJ-H79_NAGR0Sal_lRqPWdxYZaxNY_jkN9p9r-5Y_5AAHePYwHVCo69tL4Kz55B7D2cF7w5LcpVwUO31EYkvLs9WIwCpPPz8sPI6vWWLghaZ4UOYx9J-FQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=EMg8bqydSkWtyW269hOifaP5I25IKC7cX4Zm3xDnddRoMuQjyHgavTAmZrROih_lGcvHfTcZKjCHAohgFsJhdcS7D-lUmwIHnpNBbdYMaQJzWE_voYGTdZ8VVc1r1pJnsSGffmX3pbECRmeGs6qmy5GNxalIr54sawSVFCOBqgWWVOZs0isdGdrOfIdh28O4hj2S7kH14JfL3BsRC-gmRsUES_W1eOyXdAJxQmjC-CJ3hG-09pQT8XF658qhPMVl7xzhZZ2D4pdqPunL_HgRdRJc2I6WNP9WVMnrq19JDIvJOigCSNi2ELQK7lK4RNJxHik9W9vHA0KtLsGDomdKnitTXntkWVGzUlkRz_La9ssmagZ32PO_2zeVxJKnjkEOTdIyI0X5g5sXfD_FPQQNJPL0f_3DWLEdP8DQCb6fK5NpaMAIdPV2IDDpcuKjeIK0_nCoRiPAIBmam6YREyvSlpIMWJ-aTdEA3sU4QOhRUpOjWkhwPmATQUAoL2MykqykqDgb7nb7Mq2IfKykQM0e4-queN7u_fqKvv2CjW7_h8p_tNEiPINYqJ-H79_NAGR0Sal_lRqPWdxYZaxNY_jkN9p9r-5Y_5AAHePYwHVCo69tL4Kz55B7D2cF7w5LcpVwUO31EYkvLs9WIwCpPPz8sPI6vWWLghaZ4UOYx9J-FQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=HhvynHucnS2cR9f_8896BygAHf9uKPdnYXhzEX3jJ1kiovIMOvwZJPcNezfKxG-dqVGPMTYwWu_wh6xjqvghTE5AZzTeZ_oRUAO5hRfMmbGUz8OwrTw7tWm5rJIywLnGdV_oFPsUWt-6qtqs5N4xhQ2E9iE_7nvISHroIbOCDZEBMh2XSbU4-3aZ4kpjhvtfpbjqgFhgF54wFxxfQ-RNes1JrBaJ3ErZPhkkweQc4BQmNrjYPs3Y_AFHZhiGkKOTdmWAzX_QhM3i4lvepOyLF6566Jh3G_EvmEB37RasLILkMD4ppwvRirFxENg_YSo_CdCoEcL08fIOvaETgEPHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=HhvynHucnS2cR9f_8896BygAHf9uKPdnYXhzEX3jJ1kiovIMOvwZJPcNezfKxG-dqVGPMTYwWu_wh6xjqvghTE5AZzTeZ_oRUAO5hRfMmbGUz8OwrTw7tWm5rJIywLnGdV_oFPsUWt-6qtqs5N4xhQ2E9iE_7nvISHroIbOCDZEBMh2XSbU4-3aZ4kpjhvtfpbjqgFhgF54wFxxfQ-RNes1JrBaJ3ErZPhkkweQc4BQmNrjYPs3Y_AFHZhiGkKOTdmWAzX_QhM3i4lvepOyLF6566Jh3G_EvmEB37RasLILkMD4ppwvRirFxENg_YSo_CdCoEcL08fIOvaETgEPHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=oT0daZy8bAH_o9miKD4Sd3focjm2rFwF_raeY4b4ed7wVn-0ukNjvqGIWkDDhwzD0xQCiSXBe0VzBaBQErJ6_m7SiTLQBkTlEhridLNdqjfS-Zz8xuwCgm2LzEogYX1phWn_5NvShNQug_sPkby8ymlZ4NRPIPszQQwy9BJzaCWuCYSDLCSL8WmOMDqqwVxTc8H9-ifgXJTh5otlXItNl-4aEbpxLesSPStq5Y1B3rt4VYns0zQolqYERrIhg-E-Z4VPFY2dda1jzdwJ0SBLFQRtemJJabomqAcINybiL5BX6gxtwDsiblS7tVeWjwmRRo-jVYe64z2ad7FuhnBFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=oT0daZy8bAH_o9miKD4Sd3focjm2rFwF_raeY4b4ed7wVn-0ukNjvqGIWkDDhwzD0xQCiSXBe0VzBaBQErJ6_m7SiTLQBkTlEhridLNdqjfS-Zz8xuwCgm2LzEogYX1phWn_5NvShNQug_sPkby8ymlZ4NRPIPszQQwy9BJzaCWuCYSDLCSL8WmOMDqqwVxTc8H9-ifgXJTh5otlXItNl-4aEbpxLesSPStq5Y1B3rt4VYns0zQolqYERrIhg-E-Z4VPFY2dda1jzdwJ0SBLFQRtemJJabomqAcINybiL5BX6gxtwDsiblS7tVeWjwmRRo-jVYe64z2ad7FuhnBFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5uM-qnXckvOLM6IsDUgJUY4K9rbCFykuB9mPuXOoUmns4C6-_NqV7kF7UDIFRbZ2pdDfBW6jt7tnJmZe51OiMb4A4GPs0YTxiFI7MJiyPO0RhGaesxrLTRFhAR82EHkQ6CbnU7PFlD6ptEudDLFK3ypYEnryIZthY8x11mfGd6iNjU_VjYSxXbT575RBjag2_i02ellp0PPZFXj4enjVJmHonJ4LxNXU9a8g1jhhikPP3x-Yf2h7XtFPdg2zbhQNQ5ozCiCYR3OyTUUkekBkgjsaVLo-jgbES7fuhsxXy8Rf1fIEwLPjkWhO9x0MTruMamGE7FQyYdY60GtxnVwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=gkbF6K5qdreGVZ6ECDinbSJ7aa8OnasVDzoVKCMOOcnZxqzo6gAUAkCRoCHhnBlTJbkrvGnZw4XnoWfgkKQrVuRSGwMlokw-aZ4bTK4mKPeB4HhMgay8SPXa5VJAa1HqlpAiKm0F5IA44IkjxUvPaB_rnWf-3_FR1nnQQWbqn5LUWby5AZMrbcdMi4_jRBtV0C5YhpuyvVYgbHpVoDXMg5bLU2VavV67H133q1huyw8zAEQKpMNSg0cuzntI8lVuB9VAExAjZ24EXp4B72RbQGisEHWQriSJhTIOYcbhl-wZMgcfjHcn7XVDNDvo-OlmpNWGub26TDxsRl31cedPYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=gkbF6K5qdreGVZ6ECDinbSJ7aa8OnasVDzoVKCMOOcnZxqzo6gAUAkCRoCHhnBlTJbkrvGnZw4XnoWfgkKQrVuRSGwMlokw-aZ4bTK4mKPeB4HhMgay8SPXa5VJAa1HqlpAiKm0F5IA44IkjxUvPaB_rnWf-3_FR1nnQQWbqn5LUWby5AZMrbcdMi4_jRBtV0C5YhpuyvVYgbHpVoDXMg5bLU2VavV67H133q1huyw8zAEQKpMNSg0cuzntI8lVuB9VAExAjZ24EXp4B72RbQGisEHWQriSJhTIOYcbhl-wZMgcfjHcn7XVDNDvo-OlmpNWGub26TDxsRl31cedPYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzkWaa1b4E4zIIGsRJ3wo4teprqu73JpLsEdvshV4y97i0HG39aqw4I2xMuUSxk5sWfkVvH8SBHsQSUqzPLEEl7GxPrYiBCKUilUQh9QOh23t_tSrZx7Xvji3qhRdN0uVAt52B-6e31DLS4l1beIQ4BmLF7qdMaTIJWqtE0GVf3q8ErAmWJE4pcw5WZdxZ9KLu6A-aHgB4XCrXINAGF8U9x6KBpnmGChEjYU3s_HFlNRhhc7ORfRXPDSPSxLFiEpj_xD5uNNIM4p-Mfmow6QTTx4xY67YaBkUrOYDM7K70hLT6RK_1O6aU00MnGr41Uk0WG3gGCoGbyyjJsGhf2gdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwdlgVOr2MmfL0sW5_hRpkCVYy7vGc14ksQANzJFCCb9S3Ys11u_81ALXwDaga_3M7i_-gqri0AXeG-faAKj2AosfLt6FqoIMUs6K5QS8e3O3Jqs_WBS_Zj6DC-97j3iNxUL0K6WyG3znEQDiFlZ07bfdy5aLM0ceQO7AsjX1uLCV1V9Thxl9c1KSFp7ijp6TJxyk04Afn0K-kJE7A6R0eoxoZ4MKzArePU3Khvg-e2YaseLm5w2mVjqbr-Xt-JeJBV1ne6NVS4AsLDrDXCnbjoh2A6ZuiRIRMNQugeMBXpp0jf-HWykETE83gOsL86_yJWhNPqyRQ93zwCGFDmBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=SI74xp7MTZx78kPOdyNHazog5CgLBrMdFbVUzaV17lVA1-DWITaVA5KvzmkMiRdf31Ny2fvA-QSmZAWxzSxDCjVvwye0M0erW5YISpQx3Cxhz8e3iP4LF0gFrChThOpoG_PTTW30NTdsMNzz2QgZe1vMI5Y12VmmJy0aAjR-6YC2oJvUILHs7QZNTs0sibaAAjI2rhyAZK-v8x0Amq11xC8tUfgLkQZTOZ-3xjwbtxqnXBsMrUX06ByFfJh4bRhOJKaQyBNKj3y-9mzEDJ-oAW3Ad99tXkJINkCnsP1S3TxSLC0ysGbexzCM3RrSbStLArNy1zUTkaGcsGQMmRxvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=SI74xp7MTZx78kPOdyNHazog5CgLBrMdFbVUzaV17lVA1-DWITaVA5KvzmkMiRdf31Ny2fvA-QSmZAWxzSxDCjVvwye0M0erW5YISpQx3Cxhz8e3iP4LF0gFrChThOpoG_PTTW30NTdsMNzz2QgZe1vMI5Y12VmmJy0aAjR-6YC2oJvUILHs7QZNTs0sibaAAjI2rhyAZK-v8x0Amq11xC8tUfgLkQZTOZ-3xjwbtxqnXBsMrUX06ByFfJh4bRhOJKaQyBNKj3y-9mzEDJ-oAW3Ad99tXkJINkCnsP1S3TxSLC0ysGbexzCM3RrSbStLArNy1zUTkaGcsGQMmRxvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=Yn-iyaVYXTanDI_-IXGKdt0nSWcdDxvpYMaS58xoy1sI0ZA8_mh5XP_4sTcGnZUn-wwRY6kbc_aNdh809zhAuQAVi4ki2ZwB-2xiDpqrYub1Rs22nt4CKsYUbFIt9WFL29ujzUkg05sGWbnOWyD9X52WdY3mjwFFMOYDfAev_JNbaSXYk-NGXwUdLAFAauGMG0AQ7JXMDnKaEq_HpIv507Rwz8E3EHm-LN533uBDR2MNoiHdqghP5K0WQ7Nkib7Ay_VWL_9FM4a2s7TKaw0jhlWSNarkIoZ-SqrMiLrij0iMC7eDYdFRGgdrXWkYuzLLyQHi85dbw9tLnsGzOXlcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=Yn-iyaVYXTanDI_-IXGKdt0nSWcdDxvpYMaS58xoy1sI0ZA8_mh5XP_4sTcGnZUn-wwRY6kbc_aNdh809zhAuQAVi4ki2ZwB-2xiDpqrYub1Rs22nt4CKsYUbFIt9WFL29ujzUkg05sGWbnOWyD9X52WdY3mjwFFMOYDfAev_JNbaSXYk-NGXwUdLAFAauGMG0AQ7JXMDnKaEq_HpIv507Rwz8E3EHm-LN533uBDR2MNoiHdqghP5K0WQ7Nkib7Ay_VWL_9FM4a2s7TKaw0jhlWSNarkIoZ-SqrMiLrij0iMC7eDYdFRGgdrXWkYuzLLyQHi85dbw9tLnsGzOXlcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBflsxC8hn9V1OEgdtfyhjjd65flWtnXKNncaFIIzM6q6K3RGPY6e7HUo7eccibkDYw0hNmgqnZdDmbfA_twjdi7UtMydp2RchGmd94euSNuPo0kZ8xfHEUrN9HUKugXcqukf3S8hyOOwYPvJJ5X-Jd1gmOwyxVXn-L_H6nlKGwL2jzwtMlKnfl73L_XWVCIuTSdbDBm4JFppCMnsrGC206bsxRB4frJbVa2C3_BDDMjZ4ngQm4-GYDGQkGv1mIVf21FlgPzGepmsqnguhis07ApiKbNnw1wLlN1tKIH8JozBar9Fq7R8EYhfs8caPU3_xiAlKu8tyldsPsdNaIrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-xlBuA8q4EKvNHUc740opJJEvxtCqV-W-4Lx1CwD6hTSm7mWNUGBQ-CPnAAfLk6AXJyZq0k24YDL1krGbxACpxBw1YXPZfqX_wHzw7Vwav1YFfVJkgoegi4pYKkx-OqHymjyAPW6RTVEtQPCcNii-wJdyOampDV0QyCE0fSJ7wNfTKpiAi0zNjLtf6xVYP5lE79Fa-z-NLBWUwhozdPTPI0V-oLy_05KiKSjmo3K_3vui-uoa3ifkTJSIhY293kBSQWUKivjdbmRqT3lojCla1QCzjWwk5pBmXF5jRSl9m3tC_PYC5yIzKhXdXTk0DaJNuXgvn7CmeGP_fTiL5kUIgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-xlBuA8q4EKvNHUc740opJJEvxtCqV-W-4Lx1CwD6hTSm7mWNUGBQ-CPnAAfLk6AXJyZq0k24YDL1krGbxACpxBw1YXPZfqX_wHzw7Vwav1YFfVJkgoegi4pYKkx-OqHymjyAPW6RTVEtQPCcNii-wJdyOampDV0QyCE0fSJ7wNfTKpiAi0zNjLtf6xVYP5lE79Fa-z-NLBWUwhozdPTPI0V-oLy_05KiKSjmo3K_3vui-uoa3ifkTJSIhY293kBSQWUKivjdbmRqT3lojCla1QCzjWwk5pBmXF5jRSl9m3tC_PYC5yIzKhXdXTk0DaJNuXgvn7CmeGP_fTiL5kUIgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=RtgRfJUd78ErxO1PqTAyWMIt7ONhzWFdJFUgPnxFCGnDHrJobRJ2Bobbur574tAaKsaxilzh90wPXbEZVglXEB5I-8-ARGBHj5LiR7kJdeRW5jERjvUM-_w_cL9ZXUv1dxKMxOP31njdufQ3WoGpy2WONf5qlJvENXqSKdWjADAJBAat6ce9tN1Qr-hHPCbAELefjSf_kMMbee-VwjN0UzMMtjkCFdZHXYlmSIMfSiYIyo3ph4rWnfhqM83d8FU5QOL-eOlMRRSlAXrzKF-yVANMNE5D8kURKkxGyMyfAkbrb8poB4zzNMVkTo3AeR3PBfbXhqKh-eYsp3GUKl1ggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=RtgRfJUd78ErxO1PqTAyWMIt7ONhzWFdJFUgPnxFCGnDHrJobRJ2Bobbur574tAaKsaxilzh90wPXbEZVglXEB5I-8-ARGBHj5LiR7kJdeRW5jERjvUM-_w_cL9ZXUv1dxKMxOP31njdufQ3WoGpy2WONf5qlJvENXqSKdWjADAJBAat6ce9tN1Qr-hHPCbAELefjSf_kMMbee-VwjN0UzMMtjkCFdZHXYlmSIMfSiYIyo3ph4rWnfhqM83d8FU5QOL-eOlMRRSlAXrzKF-yVANMNE5D8kURKkxGyMyfAkbrb8poB4zzNMVkTo3AeR3PBfbXhqKh-eYsp3GUKl1ggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=Tpsq09q7k4GrRhxQf2Rh-yigpZ7X7bCeASpLBEoC89yamtthOsj_gXmKvhqDqZR4P33jgglQBSAYv72vUvqnFGz2YX9loQUWgxUneBX-BzheEdUrkBtRd1y1bdwq32HLacbALqxXAaPvk_m41OA0nObpWn_eXv4vt59_9IWT4oKB2P_QwBDGHCxXMSCNPhO7453y7JPtcQrrIcL2MF_EKtANAgpirqDa-Lw1_1OuHBQB7-gBvz3mM6P6Hyb1eU6RcnAzw_BZvjGEoE2J8Jz-59mGwA13PWZgRBokBXncMt_W6HqKF-JM5VI16V_GiV8m9nZz2X8nCh5MImJ5DFN0sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=Tpsq09q7k4GrRhxQf2Rh-yigpZ7X7bCeASpLBEoC89yamtthOsj_gXmKvhqDqZR4P33jgglQBSAYv72vUvqnFGz2YX9loQUWgxUneBX-BzheEdUrkBtRd1y1bdwq32HLacbALqxXAaPvk_m41OA0nObpWn_eXv4vt59_9IWT4oKB2P_QwBDGHCxXMSCNPhO7453y7JPtcQrrIcL2MF_EKtANAgpirqDa-Lw1_1OuHBQB7-gBvz3mM6P6Hyb1eU6RcnAzw_BZvjGEoE2J8Jz-59mGwA13PWZgRBokBXncMt_W6HqKF-JM5VI16V_GiV8m9nZz2X8nCh5MImJ5DFN0sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDFxHNuNS2OW-ZCnyTIXiJFVRDIjBGOvya4nVcDIGyjVwlcDuqQJ3WyEz_QlgRgGAcmdEyKF2WrnSKGwkbq32JBqHvSkGlDfZEHlm1_0drqpyxlqzT68KZPQhIE8W67hr6djn2UEy5OAzlBgtRrv4YWWNbI86mAfZoiziYHZe5zITnKFUUfRqOet4YzwXDBuCdgC8vu0Xm1dDimXFHdI6d8qsIu0PLrkzCFitnZYD9V4o4BLRNVanxHdA_AFpYnSWditbMOq0EhjQ1S3v-5bLuwy9579zanpp4upyFIFgR17_upAnoRyGwmtmpQfDkAvK36oDelLm4ovDZ9DltMVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=SQbwTTeEmXCP-Y7fE5RDireNSyf2vDGeJgGf46PUx_a_uPDLwR76oVeXq_t84CbRC8YO5czejKwGltcEN0rHxL4vxV_5t0NcVNgwqKg66onqFo298o44-zlQc7MnZbmkXzuR6I4ekLWTr78jEIWUJjTcO0-sSche69yu2Zdb7GHxrrVn2qKd5Z0lvSlkTNo8hcsods5vQO3ANVwb2i9JNBuFIBo-Ih8lWX7pmuvwVAeRS_jiXcM5oMDJP56-tw43ujUg6jwILtPUHHzzAwb6mgkAyMAZRahrjrU_k1QcOHXtUNLy3cK7nxLLsmS4giKSr6KhtDyty1sdjniKNZT3roiZ0X91DfzSj_XWcx1sh426_33-hKaY-syCCs0PSwovwB--pr3VFU5mJqKMuHcaGe5oT6BnF_a38a46lzolcJkU4DgJ64dyhYoHCNmvdGti4WeAZfgFbXgnxpufS6Qu0nBze6Se7osj34i-NqWJybePdILm9hNoBqDsyoRD0QzBVDhw51roNP8Wwa_WxLu6oIer4NGgc7uNM0rkYZcr1cX3jqI-PB9Zkj-qT_luBKAZqmMJqVcnu5_kqESJ84zGkGODjzTyKDqiu6mGmkPutarYvwICUxPjaQytR93H01FJlUFTt-VU5cjRSepCgYXg-fOqUenA35Y1jwURDsjlRhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=SQbwTTeEmXCP-Y7fE5RDireNSyf2vDGeJgGf46PUx_a_uPDLwR76oVeXq_t84CbRC8YO5czejKwGltcEN0rHxL4vxV_5t0NcVNgwqKg66onqFo298o44-zlQc7MnZbmkXzuR6I4ekLWTr78jEIWUJjTcO0-sSche69yu2Zdb7GHxrrVn2qKd5Z0lvSlkTNo8hcsods5vQO3ANVwb2i9JNBuFIBo-Ih8lWX7pmuvwVAeRS_jiXcM5oMDJP56-tw43ujUg6jwILtPUHHzzAwb6mgkAyMAZRahrjrU_k1QcOHXtUNLy3cK7nxLLsmS4giKSr6KhtDyty1sdjniKNZT3roiZ0X91DfzSj_XWcx1sh426_33-hKaY-syCCs0PSwovwB--pr3VFU5mJqKMuHcaGe5oT6BnF_a38a46lzolcJkU4DgJ64dyhYoHCNmvdGti4WeAZfgFbXgnxpufS6Qu0nBze6Se7osj34i-NqWJybePdILm9hNoBqDsyoRD0QzBVDhw51roNP8Wwa_WxLu6oIer4NGgc7uNM0rkYZcr1cX3jqI-PB9Zkj-qT_luBKAZqmMJqVcnu5_kqESJ84zGkGODjzTyKDqiu6mGmkPutarYvwICUxPjaQytR93H01FJlUFTt-VU5cjRSepCgYXg-fOqUenA35Y1jwURDsjlRhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn6WVpcmvPar3hd_R_JEZca-QvUKEy4OzHK0as4t-SY4daJV53i-gxlDhnAcUiTdQKqOQtMuWY4rYICBLjkOM8vUXCTbKdQ6_sRR6jwl34RS-N-3TfPzemSIn2O0rnYkjqzB_vkXm63A1idnzk0hUSlVyucFV72IgLx7-qDcA6_tKMIWKtlKHPlSdUznunmH1a1TJF15efvkrjO58q2gWqVdvcSsU4FiDc571-BpZEc-dnks300ski3ZgyVNxKIcrv46jZlZ7RjggtzWh99EKg3oXTfARurmNEqW7IA4bFNJhWsW-zxSVvMJD01KRyFF4PcOzkSG2WMLp4fOVV6pBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=fj4X4-cZHRNkI5OCUT4WX7yRjO4zEvZPiz7ZlCyYXyBpW9fA2vSS9IRD0928r-WPiz7iBb0bsB_lEvw58LpMfUCqVOEVGcsv-BQfaGLg5YEVlbALiIVc7erIOYBQJ2AYxtO7F_yPxZGsY7mGJIhb8Th0QlKZKUIKIjPMSrxdf9uxNjFk0BhdsSynZ_HriyQwXG8aPxe1dwKA_2oCTm-h_d3z8duSgtFceym3Xj1Wf1vyJpja3EZVafGhlVKOjePLFHaN_ZPR89UBjOwogbT9NsDCcOjSM6VBwbhiw4oJtAw59mxRZO1L5NiG7PLk5uFnsmPtATkdp-dQ19ecXO-Syg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=fj4X4-cZHRNkI5OCUT4WX7yRjO4zEvZPiz7ZlCyYXyBpW9fA2vSS9IRD0928r-WPiz7iBb0bsB_lEvw58LpMfUCqVOEVGcsv-BQfaGLg5YEVlbALiIVc7erIOYBQJ2AYxtO7F_yPxZGsY7mGJIhb8Th0QlKZKUIKIjPMSrxdf9uxNjFk0BhdsSynZ_HriyQwXG8aPxe1dwKA_2oCTm-h_d3z8duSgtFceym3Xj1Wf1vyJpja3EZVafGhlVKOjePLFHaN_ZPR89UBjOwogbT9NsDCcOjSM6VBwbhiw4oJtAw59mxRZO1L5NiG7PLk5uFnsmPtATkdp-dQ19ecXO-Syg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVUY0XWxTsDY1wBQL5ZS9g--DhMWtZalyMDj83HloosIfObCg2C6xL6NH8irqfJE1CLCQjB3x4WbNohPke2cgXtNYm6luMYvG00Dr4RphyFI2qc1p24ExOXRSLi1a835Qo_AkZIS9xEJmVrngPTf32yORAydSEs6P_p-CLNMxecH1V3z8E6rHHNslzhFEqvINRp2dK9nSmvzK2ioBbz1xcZhi3PUUghTX5Z2anlN9SRhr5qmR2xBs-cNPHhTqsQTUKrtqa_gtGvFeKF1kzHcHkRtNahlI8vMfAUs3-6_lXt-so6qQduDq0xmseYNTb_qDDAq2vRZLeEfYeWAdp7nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA7EaV7nbowdYUWjJKkq74oDcGIUfTfLeVsNN2vqc8EkdGoLFq2R2QnvKW2EIoQx_dS0b4cc3sDRqX_dcAMOi7DcVgnGmfGkw3ip3dfKzcM7RPhyjf5utW0fPTC7m8ZcEiNZL8VMG4gDt8g30Z_XzyMGhIdBvlrlcYFl4BDLKSByd97n3FP_5meaQDKN-5w84yqzdfvM019CuP_X_OF1NxBAoD3yfOYETmzWDM4ULkyszxFJXtyXmJMWfUi0qjOIkYhS5QKCcehbJtX2-aPa2noxrNGn9iaSmZrnPvgeqzUTnOoVaMSNjnxb5bB7QCJw-E9Ac4nhXsC9_6z4P3YVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2cMbOGidPz6eVu_1Nz7B90jkiir0JsBbocd48k6EJM29VO4GuzqgBUTvH3ci3sUjX-h6Fce_QAOIzRlhrtqoK4ktNESuHdlIqySL8mW2nAxEXx1zu4AgMDbUYAPUH0yBmVI4n7civSAl-W6xB0u1xLqrUfjF2kMeuagJA6-RStzBrZ3jifauV2pA31YPVKh1tn6pi53rkDJ_qtNl4kLrZX1bNO4iu57T8W4Dd9HEBkSga3a8uqgE-Mbn7UVbHHnx9v635AARarzc7T-4VS1Q9_WXMQzu-FUYkXWjOrNnGY3t0iqx9je4JI97XqkbBvSAkUd8pWP29ODCzcSGLiP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=KxrDjxJV6-HpTHkAD55jztjs3sJV2DlIsyOrnvfu7l7VbQB5SyxGBoqIlR-7_SwJIb7d8dRsIatkW8rqfLyUwLPjAMXXyqlKZcsszbeu3MQozz1INmAVIu-KNIiJCkZiB8kZm7UuOA8tmpARPpw78RJbT6IGd3YI9s0Kzvfa6Kfez4TNReUMDj3RyJr9n2FWlFgJHv_ocnFCEfWpOrSntSzZbVq0E2CvskdPZm46aaoYKQpUYGXsKCOC7fmXEvJGOVpvuLoiQnKBhngB5WEWv_NIzoZJ7OO21WC9SpLgR5fuMXbuUB2J1oOVi6GAV1wxyqRJHtN9UrMqPHKa7CiqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=KxrDjxJV6-HpTHkAD55jztjs3sJV2DlIsyOrnvfu7l7VbQB5SyxGBoqIlR-7_SwJIb7d8dRsIatkW8rqfLyUwLPjAMXXyqlKZcsszbeu3MQozz1INmAVIu-KNIiJCkZiB8kZm7UuOA8tmpARPpw78RJbT6IGd3YI9s0Kzvfa6Kfez4TNReUMDj3RyJr9n2FWlFgJHv_ocnFCEfWpOrSntSzZbVq0E2CvskdPZm46aaoYKQpUYGXsKCOC7fmXEvJGOVpvuLoiQnKBhngB5WEWv_NIzoZJ7OO21WC9SpLgR5fuMXbuUB2J1oOVi6GAV1wxyqRJHtN9UrMqPHKa7CiqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=sF_tw_paRNJRzDIlz6d1z4PY7m4Kouv8SLu6ebNeSlnHkcXgD-yi7uOHhQbsQXYpI4jVVO7JpBhQiV08n3AMCk_qDzxzwFYcqyIKdqxpqYYNRcOVk2EXYr92Ln2kvIRekkKefBCmxUvV3A30oxgWFf_GnZv79hFddZikTmuiGQbijd5hRU8x6634gukM2-AwWdwjWFIV5lS17ijCyFR8aMdQ0OBwbrulQV5kd3bODnsFkX0YgRI3oBJJwxKeMkZV63yIGoNHKt3GCluY2QiBDswH5cPySINxXm1AwUTXbS8VdSwoEiPz7tudKm-Z7IllfHIw8EhcEY1WoXtMofCSc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=sF_tw_paRNJRzDIlz6d1z4PY7m4Kouv8SLu6ebNeSlnHkcXgD-yi7uOHhQbsQXYpI4jVVO7JpBhQiV08n3AMCk_qDzxzwFYcqyIKdqxpqYYNRcOVk2EXYr92Ln2kvIRekkKefBCmxUvV3A30oxgWFf_GnZv79hFddZikTmuiGQbijd5hRU8x6634gukM2-AwWdwjWFIV5lS17ijCyFR8aMdQ0OBwbrulQV5kd3bODnsFkX0YgRI3oBJJwxKeMkZV63yIGoNHKt3GCluY2QiBDswH5cPySINxXm1AwUTXbS8VdSwoEiPz7tudKm-Z7IllfHIw8EhcEY1WoXtMofCSc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-IOXY1Zcy9ZJKMOfycP8O9voNc1dQWKebNAvCZVr49lh9vmqgxf-GNIBSts5vpXrYh1IIRf1jpBMYYT0wFmEQiAJeFt7hjlC2g-0Bzotklqzy1U-AEgsxULYFICJz8Xme10MIgXRGvtbb2HO2ato8mzwkNeLmEIrHXrIQ3DgnmSYqLYqMoEM9IDrKWkPCt1ugGjabikXr4J07BodDaT25zIwQYdOm8C8tZulk87XugV05LbbMGoNTqrL8nmfHJZT-NauHmpZ3RuL3B-5PQogZJmw9QP1jyIvkikGUdIgnhh-zG0oI5xhf8OvkCcdHiD9efoHKsbGbmMUMahEY_2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8KKpxS0gtSVLicGt9kDUZzMpCKTBs8ryTEX-7gOiqDEXVX3eV2FbSYMEzPc-Y2KCpYccx8_rVXxYD2CD6ZmdLp31n2Bi6f2dCs0JMIpCWnX6FKTqSyWlLKoCIkpIfTwA4zBLa4cT9F8knhozcDj5cWwC5an-CXJc9pClCSzd8USDMJItUqcb55jUZEQq5f0z9l2B7l00knxw4EhTUAzrMM8rWLSrLhEL4Olhrwy_JO9-rsJ9KwMZhwgHzp0fzQPjCD88wa2giAF-Wkhe4rwklMm0MeLKC7-TJ-Sv-uxMzZuwqEc302eL3B96fOy6ptStgNFkpj1B99Br3mQdiHbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=mE6UeBQfYIU5qG9fc0SkqxWrja3IkHY_Yyb_YktBTm_ZAqPoDgrEbvA__hdm71nzm4tPkylHssC_77WAyESqtaPohuwjkm-bTCNMalfcXkPSWi7PPk9wUZZfcNlNG4zyhUxfETz3OHQ4PYBi-J6RMu6ZRNwphzkdF3xNRKxqizLnXWPHoCPuvigCPM6qGg7t_SczQYtuyYoOd8Jz5WlVTMxAtSVdQfZ_65b1K9ui6K4W0594Ua_b68ia0yYWD0gpxQsd5I0ltzIgiotTOx2AGFaE_MJQYSfiKQ-3x3YJRuWodmC99zK5kx4adTXMYaVCsvazw1wDRMWnr0PWOJOYaAmB0wzSkD23No__R-0Z0WfK7b0dLM5TPXEmxsQ6_5pcfePNi8oD94eNU8CW5gUzYfvmmC0cuHqQQAq-TxBOEhDzNpr5aO9KyF9MynlmB1N3lXfjbMPRO7iHQ3yQIk0r1k5W4VOMX0RmZScI9LRmw0F--iatigFDEPezEa1eC0urh6hkdDEQdlaDRxCDI-62ZwVIpe8zXinEWRlNd9wYJb0MArOPOJ1GJKHP8Uh-omRb46v3ijs3BXa5T5GiMFy4-jdRtVqjXYr3aixhfdEyeQYGh9MQ9-Rjt8nfSYMziUNJsDtILiAfQqW6UnVegErEmXkCQyP88xX7dv3a89x4Gvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=mE6UeBQfYIU5qG9fc0SkqxWrja3IkHY_Yyb_YktBTm_ZAqPoDgrEbvA__hdm71nzm4tPkylHssC_77WAyESqtaPohuwjkm-bTCNMalfcXkPSWi7PPk9wUZZfcNlNG4zyhUxfETz3OHQ4PYBi-J6RMu6ZRNwphzkdF3xNRKxqizLnXWPHoCPuvigCPM6qGg7t_SczQYtuyYoOd8Jz5WlVTMxAtSVdQfZ_65b1K9ui6K4W0594Ua_b68ia0yYWD0gpxQsd5I0ltzIgiotTOx2AGFaE_MJQYSfiKQ-3x3YJRuWodmC99zK5kx4adTXMYaVCsvazw1wDRMWnr0PWOJOYaAmB0wzSkD23No__R-0Z0WfK7b0dLM5TPXEmxsQ6_5pcfePNi8oD94eNU8CW5gUzYfvmmC0cuHqQQAq-TxBOEhDzNpr5aO9KyF9MynlmB1N3lXfjbMPRO7iHQ3yQIk0r1k5W4VOMX0RmZScI9LRmw0F--iatigFDEPezEa1eC0urh6hkdDEQdlaDRxCDI-62ZwVIpe8zXinEWRlNd9wYJb0MArOPOJ1GJKHP8Uh-omRb46v3ijs3BXa5T5GiMFy4-jdRtVqjXYr3aixhfdEyeQYGh9MQ9-Rjt8nfSYMziUNJsDtILiAfQqW6UnVegErEmXkCQyP88xX7dv3a89x4Gvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPhkHcZu8HDe41VrE-coE-GRuwIaV_f0Uf3wNMg98FeGxoa-BRPMdYnzEyw8Fh3x5Xrx5xsUW9woISNEy2gif99SeWGor4M-iegztxLbeM2TfyjfakzWJV-bnVldLi5XCWlz-lpTWyYFqhjs2H_Q_rQUOyrqCRz63k0im0kbMkp2sxz9R32nnsnSjQGSlgkGy2U6vgGUp9SpIDzRh6XEbapg4vE1_-dL19BcC4Aoo05izUdN763AUBKsawtQfBp-O_cmlXqMf1FD2RVwi6YLnx0QhJUE4p_VF13A-LQkSU-ICBCxFJpABN_eZpGD3Las2d14Rmr9lp4pZg8cEchGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlQeb2VkEbnAoUWuFabtg4op1T5EZ030Q2xKQDA8vyJStIpMzbhzDLMgr0blbyAR24fmqzr9lcZEmufe5NassXVaC_n5ZRTYht2Y9AN5QBZQWCfv9dzmUDeKRyUaLZpEDRQ9guozwIiXEN4okLG5akkTf0OPNifQ3Od5h8R1ItywdoLArxscGSkueldHjlB3MM8ZY7o_iNvspOUbj-5N7sbYWpN015hEv9S_qVn31YbWX-Mz2D7oiO9PlCEo4ZJNXzgcA1PfqRNmH1SUXC-yfBjAkGAmUB_JVy9FkLWBF_1Lg71ofB00_iGGYaBPrgmwpnNIfzfmpCV5gfrRFNnn7zf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlQeb2VkEbnAoUWuFabtg4op1T5EZ030Q2xKQDA8vyJStIpMzbhzDLMgr0blbyAR24fmqzr9lcZEmufe5NassXVaC_n5ZRTYht2Y9AN5QBZQWCfv9dzmUDeKRyUaLZpEDRQ9guozwIiXEN4okLG5akkTf0OPNifQ3Od5h8R1ItywdoLArxscGSkueldHjlB3MM8ZY7o_iNvspOUbj-5N7sbYWpN015hEv9S_qVn31YbWX-Mz2D7oiO9PlCEo4ZJNXzgcA1PfqRNmH1SUXC-yfBjAkGAmUB_JVy9FkLWBF_1Lg71ofB00_iGGYaBPrgmwpnNIfzfmpCV5gfrRFNnn7zf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=WE_NLs4H8uxttnYhpX1EzpaJW3LvUWfTTz2qus4KCTP5IJhwPFCd4LgcJLujTivth_4niV1yXN4ysUs8qBb0Rggu0dhtLSxMn5QDSgh5LbocSes8HgjHIT1LRPhP6rr4KHcnbRY_prikt0bm8HUTPJCcVyvY3ANjXseOliu6bJH12Vb-L_JpYOh5H9qDBoAmUyv0g0YzqPk71V29I6agvXLDBVyU1Wjag5gA-TOmkvfPWtGA5bIf8RIm_qIjeaUN8_j8CT8EdJARdNCZ1LzBlFa5l7qKFc9H92U7P6eM01j_lVrThe6f2DPpySJvxUDMr7nWtGZ9E5e_xtM97BapVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=WE_NLs4H8uxttnYhpX1EzpaJW3LvUWfTTz2qus4KCTP5IJhwPFCd4LgcJLujTivth_4niV1yXN4ysUs8qBb0Rggu0dhtLSxMn5QDSgh5LbocSes8HgjHIT1LRPhP6rr4KHcnbRY_prikt0bm8HUTPJCcVyvY3ANjXseOliu6bJH12Vb-L_JpYOh5H9qDBoAmUyv0g0YzqPk71V29I6agvXLDBVyU1Wjag5gA-TOmkvfPWtGA5bIf8RIm_qIjeaUN8_j8CT8EdJARdNCZ1LzBlFa5l7qKFc9H92U7P6eM01j_lVrThe6f2DPpySJvxUDMr7nWtGZ9E5e_xtM97BapVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=N7Chr4787T8hM36xUVQcra6zI1-0FNKk6i8eR2V8_xOnYuBzLYfkqyilt05gonkE-Qnkku9a4rpFDjDgEsLYR8A8KTsMpPkqTQsT3qn8GLFSvw5o992teAe-3yzooDR8ItYUwsuNZyjDVjVCHC0srT2NXlDSDA_5IbVNxPhGVP_p444ty4_dcZo9e06W94HEVCq4XEThbNkAFUU2NnT23NKDuDIjuUTmY4EsxIHZk1MLjNkYKJ4YuwgYdPYDVxe2CBxMvqS9MSIcUZ-XM6nhlZ7hymuW96s4j8XCRSaGT5rStyCRzDDalo3Ii6Cya3R8MGAGdIHupp6S9lF8KNW35DMy0MrEixgPLYaU1LvysalbTb-XZDNlzfhVihglKZdQNwmcmeM7oX7hOXpqYPWddsDdkiY93ttZAPtiHxj4WEDHxKBSlVaCdMiAPgWZ02zcBO9G1ezXnBf685xtlhUPLXGGR8FlYfERpaW4srY1LYP2-t9_chpSh0krKGsAqH9UGD1Z7asrg0mML_U8AhjiyepxavtVLaHGha5kio5tZZz2xuHr_8LyB9pxv903vveUUF3kJdHIgLdC_0ZvlViTniDHV6klAbFCrxcoKiKjnFcTVHEDyDl4J-TqvQ0gNvK44sDS14ZPbUssLWriQNJNC38WAudT5MEwi8z0Zs2TThE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=N7Chr4787T8hM36xUVQcra6zI1-0FNKk6i8eR2V8_xOnYuBzLYfkqyilt05gonkE-Qnkku9a4rpFDjDgEsLYR8A8KTsMpPkqTQsT3qn8GLFSvw5o992teAe-3yzooDR8ItYUwsuNZyjDVjVCHC0srT2NXlDSDA_5IbVNxPhGVP_p444ty4_dcZo9e06W94HEVCq4XEThbNkAFUU2NnT23NKDuDIjuUTmY4EsxIHZk1MLjNkYKJ4YuwgYdPYDVxe2CBxMvqS9MSIcUZ-XM6nhlZ7hymuW96s4j8XCRSaGT5rStyCRzDDalo3Ii6Cya3R8MGAGdIHupp6S9lF8KNW35DMy0MrEixgPLYaU1LvysalbTb-XZDNlzfhVihglKZdQNwmcmeM7oX7hOXpqYPWddsDdkiY93ttZAPtiHxj4WEDHxKBSlVaCdMiAPgWZ02zcBO9G1ezXnBf685xtlhUPLXGGR8FlYfERpaW4srY1LYP2-t9_chpSh0krKGsAqH9UGD1Z7asrg0mML_U8AhjiyepxavtVLaHGha5kio5tZZz2xuHr_8LyB9pxv903vveUUF3kJdHIgLdC_0ZvlViTniDHV6klAbFCrxcoKiKjnFcTVHEDyDl4J-TqvQ0gNvK44sDS14ZPbUssLWriQNJNC38WAudT5MEwi8z0Zs2TThE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw9XyJ07L8OjypOjoHHxQmdrgqCRns56dn7g3RuQ76y-D0CASYtyvgSN7XvZVONcaHyMF3x1VjOwyiYdQCmMoOaKiFOzjWvv22pSdu3lRnskqwaYUABdfVA1dXwPsLve7peGsWGf7JA4eQQIr-bNHoSo13ErKsITTdBOiDNRlrvl0zLV9SJr7X8JGJr1E0MXC6Ffj0vUqlQ0cO2BW-8Xnc-9_XB8Xbl_o9rpcjvaDt-m-ctWqdAMteW0Zdf9Pf_jOaZRVQp67bg-mhTjXaVDZYEHTv-bNWXHwwRzNkq2eefPfXlu40numDVzlbRdUrKKGecUX0NRpvRomixZDk8v_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyvNNViGTb9mI1Plr7jWANvTD_eDTkC9_9zwGe5ivb_Pc4Nq6BXVcm_og_Somty3ZOwnBh-JDVxYbc-Y4cjIz9zIvB-tBTKrJA9NNcTfVGbPeeXQl-xgxYdtDBcL5cAelCBQWfeSlvVDTS5aVzwKTRPTVYlfCUKshdXE53eSZBT2_npjdlq-ttfnbgSGM27sVrtdV97Bk7d76txm0LYhum9OXwQ1wu9N8HiPBRGickmY6TOTN0sLRT5KW_vDE54g94hZ6LaaSbfYGE9qXHHROdcQ9vAt6dUVPvVCT1XZrbaGl8Z-kVqd646G5le5C5pg4Dge9fAKIwV9vm8yB4isdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=BhpfRs4AvCudQ8qHnjiNVP2EFG5OJ_9rYH_ybFtRpemDkexFWoSQ8mY3FyG9Evx6_kooeA01tKp1hlzf6WZwVtL60zYFttCd8hxE9jvGGsKiI-yJkRjUCjLWwKAkSpb8rqqqE0A5WX9oabta7_e7fITFEmdMuX4Ps9J8ohWWVqag9eOCDesihtztdxBTSnuc07njpPffevrksVvFTLI_800sE8NYfVdMnPQTFzAL0MNZpNIwu3EnvrSNh75C-c8j2zEnQPHfGu5wG-AhtT207bZnLaiE93a8I_E6p1PVeP7YZgsde3ht1PlwMnr-5vtFvKx6Wvx7k54vVN3RK8niRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=BhpfRs4AvCudQ8qHnjiNVP2EFG5OJ_9rYH_ybFtRpemDkexFWoSQ8mY3FyG9Evx6_kooeA01tKp1hlzf6WZwVtL60zYFttCd8hxE9jvGGsKiI-yJkRjUCjLWwKAkSpb8rqqqE0A5WX9oabta7_e7fITFEmdMuX4Ps9J8ohWWVqag9eOCDesihtztdxBTSnuc07njpPffevrksVvFTLI_800sE8NYfVdMnPQTFzAL0MNZpNIwu3EnvrSNh75C-c8j2zEnQPHfGu5wG-AhtT207bZnLaiE93a8I_E6p1PVeP7YZgsde3ht1PlwMnr-5vtFvKx6Wvx7k54vVN3RK8niRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
