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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 20:15:02</div>
<hr>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjmUzi9johmzWQWPuTw11kOZKyWRKZE6Rq4YsD-fC-AOJBezxFPt7NthaHW52aQmB4njlxuSuayXzefi1ocVOFcSfRW2vukC5tY3NMDNNYIA0ZDGKM2k1FGiP9snPbUkywkhXau0AlEjyomIk3z2tvODd2SMM_2TcviHl0IeMWRLOxlteICESGIK9erT5m5Fx2N7HgKhsGjQmM49knQeffVHfmTk62Q0NdMUZWXIh4Jm-CWb0llYdR1K4uB8RmuhSgiHd4wwfquEMCZBkk5RiedxUKNo1fPi0jsLkKKhPTAHkqb8i2pogu60qQuo6h4nXlGrDGvK9VDou57v5AlDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxEBTaWPYFYgBoVjH8ycpvW7Ua9nXYqGenHF4kmK2m1AWxh_9EwC07szc_QqWWZCgY6SgzCzjfx7XFjgGE1s7XFA1TAJ_kL62Up8UuHb67pnqdZdFlcg_ivTvhMbHpq9TXPqgtXkK1q5pLiPzVBfmiZZp-2RCul2bpMiz7jylxPxc8MFTuSQa5RSrpQlgiOoeG0f2zyfdrAzYVCZhx7jMulFQxSWs3vFDCxlwJn4_-i-4jiQmNe1gtSl4DhaibvLakRbvGCSU4QlhYX_DtImhB-gJDy3QpcnFwqXhZMZM7Aff4ZoQ-hRPkynDrR1VjRj5ARtUhT5Yn_-JNe62s_Ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux4JP_UJNbqObqzZZGH-AGkv1nLgdm1iw5prRe5mWIBgNt97bMx3F6s8fY9k_DywtOszslc0ueyJ2KtlmAx805UJOt6lF6bxge765DarpSkqzzQaIaSAt96k8welbnTmoiH4uHwrTB-_hTFYRn8acGS-_U1WNQ3w4gycxmnIStTvxTxyDRgb6QEHnzl7FYZXUBLlyWSlTuOzFJazVoIQDjp9G1KkH9fuDhFt0TFMc375alVrc8zqZaUwNcwPOptEG_v_64Gmz0VGTprTLIpQuNxwzbLOg5DEXPHgVlVXFMDZSi0nR4m8Nv4VUwKsH0eGmevuY4PLluKOw7oUeM9rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h34S1sitHZARC9S9ZgoOJEPSK4fO_qebyzEGXAb-Cl9mGBx-dzESy9COaR4HhY5RMdSLimRIoywb7a0cImifT_i5vlM9RV2UQwrWWOHFBlwFz3LrR3_FnKiKWfYo4EszRg-Ub246J494NB44jsVsQM7sj8clZY3SYaG3j5PhDMLnKIjJpXJ1ETPjUBHOXuuVZlfmA0HBxH51ancdJXeaY_D9fsnQtc2E0zUyWvudbjkjb3hpbuMtTjimNHLxH0P49KEjr0Zwmxkiu51tOMjSPJ53Zkr5Mcixb0w2rBVkyXPowOMHTOd1tCW9dOnbQHLdU5-wcz_0oGUktHrD0PLcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=ecKwJ457toFi5EcEDqD7T3YN96UoAOo8v8CJ5mB_McvnzgM_dj8cxAmmUiAX68hfnS2img3uDZoxeuYxPBLg0W0a6B9uUGL6gdmXki5BMSHcR-pyCodZYxVTcvq7gmeOYJFpjX4xSyA0FHjeEt2DQ6xvrjySbaZi55ZwLsYhRx4yMmtkgRdOfwTmFwNONhGEzPiMnnyxNLdYM3mlQOLT0nq71Jad57yGK0NfCvoyINgmk30GvYqlIak0LQFGCiJ7FIgwFrCmch4JSR2SVVgBwFm8hUuD5Dtk5aVump2mOLlomcpXvoVo_5qy1qNno_oQhPY-H9_yvc3_bUJpQmenoJalUZWxo3MpQheLr3mOFjIwDaKz5Q881UU6qk3YSOUh_GHp3CIdJ90WybHwTUeeHY9kUKpDJs60ZRNpy4FnIrGcDHpI1GkeYs1E03s7FT7kwuQl6CuTlrLGYvxVWnaAm1OFmYAPaFQOEmJKmjLFHZu1ctD9winTg-QKBCZ8por7qBTclmbm-CzAcesoO-CDVolLpclVDBtwZOiCxKIryNYvu1t2483y0RPxEQDpyAj9g1MhdvFKuG836Ihb6dWo-FLHJ8x6iAvxDnKOXFFSQJ5dKHqMi2V0IubbfyxNm59FCDAgEpdONFPtFN6K8YupB7Nw0dX-ZyV0643-EgXf09o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=ecKwJ457toFi5EcEDqD7T3YN96UoAOo8v8CJ5mB_McvnzgM_dj8cxAmmUiAX68hfnS2img3uDZoxeuYxPBLg0W0a6B9uUGL6gdmXki5BMSHcR-pyCodZYxVTcvq7gmeOYJFpjX4xSyA0FHjeEt2DQ6xvrjySbaZi55ZwLsYhRx4yMmtkgRdOfwTmFwNONhGEzPiMnnyxNLdYM3mlQOLT0nq71Jad57yGK0NfCvoyINgmk30GvYqlIak0LQFGCiJ7FIgwFrCmch4JSR2SVVgBwFm8hUuD5Dtk5aVump2mOLlomcpXvoVo_5qy1qNno_oQhPY-H9_yvc3_bUJpQmenoJalUZWxo3MpQheLr3mOFjIwDaKz5Q881UU6qk3YSOUh_GHp3CIdJ90WybHwTUeeHY9kUKpDJs60ZRNpy4FnIrGcDHpI1GkeYs1E03s7FT7kwuQl6CuTlrLGYvxVWnaAm1OFmYAPaFQOEmJKmjLFHZu1ctD9winTg-QKBCZ8por7qBTclmbm-CzAcesoO-CDVolLpclVDBtwZOiCxKIryNYvu1t2483y0RPxEQDpyAj9g1MhdvFKuG836Ihb6dWo-FLHJ8x6iAvxDnKOXFFSQJ5dKHqMi2V0IubbfyxNm59FCDAgEpdONFPtFN6K8YupB7Nw0dX-ZyV0643-EgXf09o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=o8iFd0EtWfkqK32C6Z55_3Dyl0zA4lFbAWYU3vVkE9Jios8xVr0khYdBMfJHqfbDvFB0EKpwUiOI827hwJimluaX56tFDJUfMjLFMi_oapCUWf9b4V4WL52ykuae7TgBhhOF4Ld4fOKZPZW7X1_kRILEkpA2B3PDUfi4RQ1ez9sKnBCCWs9uKpFN1VCflE6y5zLh42xxuHqXrKBcxVffewwg1W8pmXWRdQEOAfPJUyT9m2ev5_3sOPZeyAgQyplWUINASgi6q8FQu1p0IO-U-bSNyCixYi7mj1Ws41BdZaGz444kZw_7ZXRwF4K9jzFT78FXE8dBgn1cy5LnVp4yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=o8iFd0EtWfkqK32C6Z55_3Dyl0zA4lFbAWYU3vVkE9Jios8xVr0khYdBMfJHqfbDvFB0EKpwUiOI827hwJimluaX56tFDJUfMjLFMi_oapCUWf9b4V4WL52ykuae7TgBhhOF4Ld4fOKZPZW7X1_kRILEkpA2B3PDUfi4RQ1ez9sKnBCCWs9uKpFN1VCflE6y5zLh42xxuHqXrKBcxVffewwg1W8pmXWRdQEOAfPJUyT9m2ev5_3sOPZeyAgQyplWUINASgi6q8FQu1p0IO-U-bSNyCixYi7mj1Ws41BdZaGz444kZw_7ZXRwF4K9jzFT78FXE8dBgn1cy5LnVp4yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GNTyG2DG76xF2d6x5CKy7cDlQTy2z5FNF6wfV6_1oCR3JpPqoMjnbZKeSFlCkJkIj16S8lxngY_P101eJbeebFnPtvd2F0WWM9nyrFMkJwW33OTZPjg6FUgjyZeT_qn3xCOU5O0c9sArBcchchQjB-_pynWeBKjm3hZoGBCpweJ9wPO6H4M7SSIhFwQ7Ok0PpuEy0T2oMy8NTfaetMYs4AFd_R_dnvsrbak-n3IRc3GBqdNFSeEcvqW4vnHUyIUtbWI7WLrh_TBrR7Ly9wWeOTNCpqR8SEYKTlpmERhJLCwr_J5sk2Zk3ewUoWba0SAlQUJs_ZBMGDtRvOG46b7nNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GNTyG2DG76xF2d6x5CKy7cDlQTy2z5FNF6wfV6_1oCR3JpPqoMjnbZKeSFlCkJkIj16S8lxngY_P101eJbeebFnPtvd2F0WWM9nyrFMkJwW33OTZPjg6FUgjyZeT_qn3xCOU5O0c9sArBcchchQjB-_pynWeBKjm3hZoGBCpweJ9wPO6H4M7SSIhFwQ7Ok0PpuEy0T2oMy8NTfaetMYs4AFd_R_dnvsrbak-n3IRc3GBqdNFSeEcvqW4vnHUyIUtbWI7WLrh_TBrR7Ly9wWeOTNCpqR8SEYKTlpmERhJLCwr_J5sk2Zk3ewUoWba0SAlQUJs_ZBMGDtRvOG46b7nNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGZUv2hVgHwG1OiaidADmzsgIVw1LcQk0GvFwoy6SVeKN969qc_OF2GEWgBhbSHvpKPy14aB75jyo6zN2wwP79UA92aRnja5icAQsnHgIXXue6_iX42A68JIQ5YdtWuF9e9jp15CMH7HKD424GwCHXC8dtJTbkYVIuGvzulVjKVaLPrtFk3idqs9Uqnpx8bSgZ83x-bbZw3Cd97NjNriJQUog5aa9lkKCmGeIfBRj7Q_eO6u3-nx2lvaDJO_VF-qXVnESuJBB5mEGJ81MyjzM-3Kfr1NRI51HRMUtHczqNOwdcFMU06X12xhklVpaYDGFGtvAGFh0sVhSM484ZHKQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=fnJKvgFmFosRP7zR4B0jIE_PDQ0eRfhZ6vyq1G32rB4VyeQrd1hrHsT8fczGkhIKfuBDRAH9Ksh4xJIVOylEh27Fh57J_L3mXGbzzQw9s4fqYi4NEbTu5hf-i92IyMmQ5UCaUgqYpjQZ1iY20jLUK2mJKsz9XMcYoQCWGrStaz8slkvFbL5R8ip2Ec0hTqt4hrK5mSuqGVO6h1EgEY-cWWcRrwaFaSbOe6HS3_r9qh4u1q9fTr6p05eCRhqZtOaJRSkLq0mSSOTKJrj5TNhjE_fIXr6k-VDXngYLtXXbJlpecJxWPgVO2Fke5DPdisXbjdMdRDPOFV05aXQc2epfcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=fnJKvgFmFosRP7zR4B0jIE_PDQ0eRfhZ6vyq1G32rB4VyeQrd1hrHsT8fczGkhIKfuBDRAH9Ksh4xJIVOylEh27Fh57J_L3mXGbzzQw9s4fqYi4NEbTu5hf-i92IyMmQ5UCaUgqYpjQZ1iY20jLUK2mJKsz9XMcYoQCWGrStaz8slkvFbL5R8ip2Ec0hTqt4hrK5mSuqGVO6h1EgEY-cWWcRrwaFaSbOe6HS3_r9qh4u1q9fTr6p05eCRhqZtOaJRSkLq0mSSOTKJrj5TNhjE_fIXr6k-VDXngYLtXXbJlpecJxWPgVO2Fke5DPdisXbjdMdRDPOFV05aXQc2epfcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts8GSi3NtztnojJEWZzisW21jLw3aqM7hC09IYNFO-JwIplKfwLNyAEEmqqz8mizxcTbx_KS9XmvLMhs82tMD-V80Va00_eN3JOuRfMcSLTH1pVSzGCyjUFFqZdwu-2nXXmdsiTxqgzi4TRrSF17jvhdoaNRYzE2JZQcdCSYWIRhE9OmtQ52SaFOAPOiJjhIeWeJSr1CZoKvXc-sieaNC8FVXY4LmCOgvX2pHxH0TTkRUUPXP4DckO2eazNKqFyssh8-eEo2skExVBCE3HQKM84jmVdf8e4b5AMfEyZqlnszuYm__YLZPewtuAUXREx1-Fy3HuT841di2L-04HDj2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T218IwKLVUVLT3SjA6_5on8Um0FKU3fq3vRvGkY2_nn_I0z-ipKTu0P5JUd_HIdIRinEa-R3ksiOE-pZ0lKLRNa6putIb78h1oqwUXDbHagqhzFCab83YoSBsjfDrp8iGNr3xmdFHA5JrdRPJd6tO7BTpP46wnFFtzRn7SIgiUFTiaMhc3zu2vqhOUFvtKyCEk_4Uph6fiaOz5YE2yuAF-dhylbe3eY8e_zFw3WObavq1EMHPY5TWjXSxv97WdDFMVUQhcQ7SE-i9itb2LaEQDHHayWklXctc_pbZlt7sZ5pywmA-uf24jYqfirh5Rrm_JfF1tpBjgvhbG0yyRPKmg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=ZO_AwSdSU2gRdgqJ6MxfwWOtLqanZltpFfv5CD9P9lQ8YWGsJfgZNxPQ9K1kPWW3pLDNr0XvN6p6UdAgNtZsrnnZ0lC0LWk1-3Q_LSKrkcKvYK80mo9KhSJmhWL4k2aEmnjFhEExvU3IMRO5UxmU4h9NMDOruylSU_nDvlrdDmKAoMlndxEREy64mFcG_mdsTmlkgvx9rbhSl2uveLWPMawFGpHOI2OHGVYofDc8eUvIigD-g2W3t5wnurUcjF-6iYewRO1t5Po75ciz5tfu_8kcBfKO0pMCddEVedrkacZ5g0HjDFyZhQZE8ZYAbrKWbDq-Nl6JDVYIIvxqKfPNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=ZO_AwSdSU2gRdgqJ6MxfwWOtLqanZltpFfv5CD9P9lQ8YWGsJfgZNxPQ9K1kPWW3pLDNr0XvN6p6UdAgNtZsrnnZ0lC0LWk1-3Q_LSKrkcKvYK80mo9KhSJmhWL4k2aEmnjFhEExvU3IMRO5UxmU4h9NMDOruylSU_nDvlrdDmKAoMlndxEREy64mFcG_mdsTmlkgvx9rbhSl2uveLWPMawFGpHOI2OHGVYofDc8eUvIigD-g2W3t5wnurUcjF-6iYewRO1t5Po75ciz5tfu_8kcBfKO0pMCddEVedrkacZ5g0HjDFyZhQZE8ZYAbrKWbDq-Nl6JDVYIIvxqKfPNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=kOEZ6nXifOdPCiR32D0svsaWLeONM2OsMwdOfCuDM3UjQajW01HIZWFWAu7Tge6CKsrrh7ELBRuysVjO5fIsuNaUiFCr1l4RavtUxfK4kApNn6DhYr8BrrTdFqvVuAJX7YYJ5tKRbCLko0tLe2CO5qukpoXrYp63mfMxRzi1LTQuXs-ho3X_qct7py_PJsIRgkstvtZgOpoF665ay6-7T-zGiMSwCIW_GWIYiv9w_UJXBTjwDRoB7pT3emhXbg6_KwkLqpvTZsUmC5DgbkRmcq4wz03QEFpBCztn8YeNwVTku_PqdI6LuW-OkADKw659cnyqEsMDel3ro-aFwS178g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=kOEZ6nXifOdPCiR32D0svsaWLeONM2OsMwdOfCuDM3UjQajW01HIZWFWAu7Tge6CKsrrh7ELBRuysVjO5fIsuNaUiFCr1l4RavtUxfK4kApNn6DhYr8BrrTdFqvVuAJX7YYJ5tKRbCLko0tLe2CO5qukpoXrYp63mfMxRzi1LTQuXs-ho3X_qct7py_PJsIRgkstvtZgOpoF665ay6-7T-zGiMSwCIW_GWIYiv9w_UJXBTjwDRoB7pT3emhXbg6_KwkLqpvTZsUmC5DgbkRmcq4wz03QEFpBCztn8YeNwVTku_PqdI6LuW-OkADKw659cnyqEsMDel3ro-aFwS178g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjLEctZElwMpNh2kSGG4s44F1VAWtfX-yu6h3-qjVd7Z5I-Vv7kRKiDGhbnpbzumZgs3zwcOMqZpsHyKzq_6mrB3vknNvVSV0M-6WD6gVKQpqkjVWX8YajfFIszejph8RanO7Lohk2EuzYQMS9w4G8xqQZygBxmlN8ZmcQYLGqwXHBjGYf7RYlyg9IfqCZ_Q4scXGP9ox5G8oMc00Y9ui0maPlwwkQG7NXft9m7GPwxgXzOgzRmXtXoJQYC5IPFdGjod6Orle22hAl1cvf_x902MSegva6ww8XaG2VAFKzEFe1sUKlIElMHuHGLyS00nEqQM_RSDdOTnVe1ybtv02A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-yXTQsr5yzsZ3O3GeCz1BvwhdsD-qIbIVoAT_TYkLzTCT7DCq2jp0It4VljbMcQToLh8OriOpgcIV9TTHE7Hzwy1_b736mxcR_NTqiwywVy1Zw2Xk3fPN1DrffSUSKyobjrqQIqNqU7StxNbxmei4vujjGA1l-LGwzwOXb17b8m2vIYhI1Djp5SjZoPcY4xp-x_L30AH5SRSJHPhQMQoXtfjS59toSRrt5JH73LVZ9M3UsLDJqUl5_3VXC1yGJK0jM-4hrkPmeG3-LcFo94pj5NzN_2nbjMwyPMj7u-xf7z6QgCOcyGXWl6sYaZmVI8a4WHNXkWO5LKtit8BBgqz6Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-yXTQsr5yzsZ3O3GeCz1BvwhdsD-qIbIVoAT_TYkLzTCT7DCq2jp0It4VljbMcQToLh8OriOpgcIV9TTHE7Hzwy1_b736mxcR_NTqiwywVy1Zw2Xk3fPN1DrffSUSKyobjrqQIqNqU7StxNbxmei4vujjGA1l-LGwzwOXb17b8m2vIYhI1Djp5SjZoPcY4xp-x_L30AH5SRSJHPhQMQoXtfjS59toSRrt5JH73LVZ9M3UsLDJqUl5_3VXC1yGJK0jM-4hrkPmeG3-LcFo94pj5NzN_2nbjMwyPMj7u-xf7z6QgCOcyGXWl6sYaZmVI8a4WHNXkWO5LKtit8BBgqz6Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=Uyj0s1nQrj-YQRvrKCwfQEd3u08BngRZPakKBHgg-eb7DiPsn0orewXr44NK7z2ioU3qz_kUk2tmHYlWuLIB8vqvL-siXbMudKUQKQbNj-hPexX4aPETKgCg4gsC3aCaZpMMQUixWEyQllRE6HgKhm5Z-VO-nCJS7VoGeO0dyJ2vroXQfvHLn08ntKay8IYWVpIujWg3wVsFZN6ouzPUipbldLYYJ530QBlZktOfhnZRXjtCAy0skHXtUdI58WUgjbDL0gPfEM2bpBOHNLN5QtrMwTL-GCnosKxLMZx1wRrLwXStkcTQ6EPq7KH13GY4bJ8l9GvHZ5sYR4XvjL-OEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=Uyj0s1nQrj-YQRvrKCwfQEd3u08BngRZPakKBHgg-eb7DiPsn0orewXr44NK7z2ioU3qz_kUk2tmHYlWuLIB8vqvL-siXbMudKUQKQbNj-hPexX4aPETKgCg4gsC3aCaZpMMQUixWEyQllRE6HgKhm5Z-VO-nCJS7VoGeO0dyJ2vroXQfvHLn08ntKay8IYWVpIujWg3wVsFZN6ouzPUipbldLYYJ530QBlZktOfhnZRXjtCAy0skHXtUdI58WUgjbDL0gPfEM2bpBOHNLN5QtrMwTL-GCnosKxLMZx1wRrLwXStkcTQ6EPq7KH13GY4bJ8l9GvHZ5sYR4XvjL-OEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=GwVe8ebnxs8CenwrmIQtAVZPBmWy-DSGjWpvEA-x6f1UQe8TpVCESR28-bOKcMJ5bTt4AI8SE8Orpr1gubOMZiWn1z0Km2RoEagZ-1jMPuULansHJgC0oBeTL8i77OFmcztEPKwvgkPc0rlmSW-oJJ-foBQV1by--rfftHTUpDMd8coCMx7yrvztvamhJVT7tXJFaVRlpyLyjeV6wHcRzkMOAbT3uA5bXHgrDGZzJbAVQCydb447VM-aHs8ryFlvYpAM5iknrWKV4HsLjOFgqykyzhd7880IkfDkygkQ8WZ7E439cfLUjBu4yIOqOHTyYNqdoDcL4geirdw8lvVULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=GwVe8ebnxs8CenwrmIQtAVZPBmWy-DSGjWpvEA-x6f1UQe8TpVCESR28-bOKcMJ5bTt4AI8SE8Orpr1gubOMZiWn1z0Km2RoEagZ-1jMPuULansHJgC0oBeTL8i77OFmcztEPKwvgkPc0rlmSW-oJJ-foBQV1by--rfftHTUpDMd8coCMx7yrvztvamhJVT7tXJFaVRlpyLyjeV6wHcRzkMOAbT3uA5bXHgrDGZzJbAVQCydb447VM-aHs8ryFlvYpAM5iknrWKV4HsLjOFgqykyzhd7880IkfDkygkQ8WZ7E439cfLUjBu4yIOqOHTyYNqdoDcL4geirdw8lvVULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc8Q43b9ciSuFZ_L5dC9UNm9s_2XG10hTDDj-2PFp_AePxemPrQS6JyOJEjNm8OIoS-OXKkJlRmT4CZJC8Bw9FP5S6FA36mQ6UGEagkGfcwSB_FsgyGWLiGx2sbLLeI0s558yd9G1bwyRkg0nm_yJfxUINbNRxEPtpouwsPgJkQy797-PuB1LzT6FbsNGpla69PH2JzmRUh1qmeKdwu34YEJ2YYooc_IZjBzJrzDZDsnW_VvbLjhfBbZXkWZNCz3Z-dzpW-cm6dTUfvLuKoqvnfb9xUVjH7dwpk_3VKF3m_u-LulI2Ob4zzpYP5ghgEzAyANYW93fNlaG6ohuHNgPg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=gVfqDfgaXYnwvjHwrx7KDF4hjGyFm3NAvXTZ1h0z9GD1IA1EE9wUYaKXDH0A-7Aq4KtgoAY8rHc9NTLJAbQPz9Sweryt3MUx7FKyZByQdstZSFvbpmfLWcQpiVdE_Rtby0zcZViNX1nKzvkBcsvUo50t6nTmbjLZkUDFhwGgSiLXHOpKVjbV8OcNk3ue2bOKu2T5iKQiAPkgQbXVyzD4RkOi0sD5FpuXIErfNGMhYmiY1Eoy_odAZ0KWBeLDKNin_CM07F6k34t9eqXyWZy-FWjM292_KVk5uZGM8VJj9nW1SU4dd5t26ncIRB-VjWPl-O-3NmMVE3dOtfFGy0SldnEzkdoR89iYHfpXH6j57u2WTz_cG4oD36gJ6GTtTmvcggiCNoA9fKaD02-HZD8vvTY9Ds28F8qGTa0UCr8GX1kFhiQppZ8gOX6OdNc34z6QIyQQGi669m05lDBrrLVWr6jcNKUCSFdguSvkQ-gmnLzb5i0_dtcEOm-PEF-ysQtAB1jcVPjRlgLBpkCLdOxzFQdAIpbMszWOQZef2ryL7WYiVzHp8D1Yn5QRvKjcK8hl2k6KfNFBwU9pvXJ6C2Y8nEkpQW8YhJAUclC6vjlZYh8xrHH1uhmmkn2XOXTGBbBggGtEVI8Zavz7WlWvvF6XZT4A66XvGfFdA4MccjfTFos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=gVfqDfgaXYnwvjHwrx7KDF4hjGyFm3NAvXTZ1h0z9GD1IA1EE9wUYaKXDH0A-7Aq4KtgoAY8rHc9NTLJAbQPz9Sweryt3MUx7FKyZByQdstZSFvbpmfLWcQpiVdE_Rtby0zcZViNX1nKzvkBcsvUo50t6nTmbjLZkUDFhwGgSiLXHOpKVjbV8OcNk3ue2bOKu2T5iKQiAPkgQbXVyzD4RkOi0sD5FpuXIErfNGMhYmiY1Eoy_odAZ0KWBeLDKNin_CM07F6k34t9eqXyWZy-FWjM292_KVk5uZGM8VJj9nW1SU4dd5t26ncIRB-VjWPl-O-3NmMVE3dOtfFGy0SldnEzkdoR89iYHfpXH6j57u2WTz_cG4oD36gJ6GTtTmvcggiCNoA9fKaD02-HZD8vvTY9Ds28F8qGTa0UCr8GX1kFhiQppZ8gOX6OdNc34z6QIyQQGi669m05lDBrrLVWr6jcNKUCSFdguSvkQ-gmnLzb5i0_dtcEOm-PEF-ysQtAB1jcVPjRlgLBpkCLdOxzFQdAIpbMszWOQZef2ryL7WYiVzHp8D1Yn5QRvKjcK8hl2k6KfNFBwU9pvXJ6C2Y8nEkpQW8YhJAUclC6vjlZYh8xrHH1uhmmkn2XOXTGBbBggGtEVI8Zavz7WlWvvF6XZT4A66XvGfFdA4MccjfTFos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAthM4edUxpLQIbqMlH2orsc8yAx699kSjAL3lvrM_a3vcksSBRXWVHSfLzymFo1xRXYCLVH7MDyJuc16MFRJYxn8xxdUEpwQCqbLcn3mai0RYh5MN9zKhNEEjnkt7cyh8ofIaxGcoQO5FvyhKdcp76D5UQIUgmXauo4F2JmT0FpIomZvnWPwS4SGvvt_7Ai7u3p9xw8GAYWezGJN1puQWMCZyvFohreXyurK8lgrtCw6QWC5I4OQ4eTZIp0ctb37Ism6tDQnfUWnHubXzEzNlJfY3ZaI6q3m3Bu51yhaiM1b6nwbWyAXMEEFfjaTPNL5BkS8Mpx8_QU5yqu581iOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=XO-VIs-TZJ0BK6ACOutVsqDTMmqY3aIJQ2DEFHmx1J3AfrXZtuHHrDXCiNhKHOzNY0c3siJwQYgpH_peBCjxcahuT9fKU4xI81ZvMbN5rPFNifksfzJvewkrfV2Py-trz5-0r39JHMdgvfvDyXAXv1M96GatbKXa4_mv9sKjC7lrihJbQ83h2RwcIYplMughV-EfsI_1VfKBWVAw7TzmAAOB5iKsbQdm35zj8-lF09g4e9fj_2pI7F79J7KM_nxI42-uZ_Ujf92DAz6JuY0Wk5P1XRaRKfBDWT1k5GKhILpZmrCj0VlGSCqx1pbY-4He37TSpm0GRqG3G4yXVW2OjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=XO-VIs-TZJ0BK6ACOutVsqDTMmqY3aIJQ2DEFHmx1J3AfrXZtuHHrDXCiNhKHOzNY0c3siJwQYgpH_peBCjxcahuT9fKU4xI81ZvMbN5rPFNifksfzJvewkrfV2Py-trz5-0r39JHMdgvfvDyXAXv1M96GatbKXa4_mv9sKjC7lrihJbQ83h2RwcIYplMughV-EfsI_1VfKBWVAw7TzmAAOB5iKsbQdm35zj8-lF09g4e9fj_2pI7F79J7KM_nxI42-uZ_Ujf92DAz6JuY0Wk5P1XRaRKfBDWT1k5GKhILpZmrCj0VlGSCqx1pbY-4He37TSpm0GRqG3G4yXVW2OjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtR4lgL_-SBMDc3244eGOlnLj8iWgPgVYhurnRE6ogs819De1HGo0D5B10BwcdMW_FtGQ5xO7v4MGHE2WW-F7JM-L_Y8g3s9MmMZ-7OUcSrI1M5np4GFSiLxuMfdwpelM98Il_gWUpgHwmoxUkBegDB5L4DlSFVMLGBDoaYuc9mpciJvFv9A3ctBEljGrriJ2xXOg1xYGgvT7uvR5AJk97j-0451E_ZoO-9ySOPMRO4FPS0G-PLgpYtRV4RRxuD1aTK8xJRuDYRlOAc0MpHG7UR5qj_7ya6iCxNBn3N6qX8GDgzU8aJAiS0nX6u5jVlqANP06KSlY3e2I5MKUxkWdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQm4xQhG38R8Y3Ya_bBVrO4EG0zqBVXCbyo90MtO0tGE5kEsPn-G0nD2gUqqMMl2g66Rv4fmkZULDhJ4UJzRYaYyM2reHbuKFP0T3UOGZVEuq5I1JgLH57NA2PHqX4r9Gz1ngK-G5qI9bNNv1W-q5TqwB6fG9BWv9c1IFeKU_xN8IdznaTHpoyQrRordJ3O_aQBz2_5VklPhWHYw-5aoguzPfjq9BGG-TU3K-Gf1-N4b59_vae81zaE-6IOPzUjoHusV_aFP1IM-JCZyB61Vo3GuRZGb44ZCI4H7tloeR01mJ0M8q3Fn_7Xjru0t_S8x1e5y17yC_vo0NmmvhvylnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wquwtzc9nMWDg5CYsPEgI64yp5Z7v5Fzq2vxVhKoYXvsr8AWCJyLYTVG-Vg_MV902TKAxURN70GZ3K7PjpBTciTQ3nwU0cLUR8xXRjsSyX5oQNxbeDqIJe4altIruLdKCoWKsN-zlpBDgPQStlgLrfS3o0u0-dCpeF9vMqwMccqx3S63eSc6An0nW2cimX489A4AiEBIz-PpvQvo_8eU7fEZewATxzzFvpbnmWtBjVKb4XtnmZXgp1F4I0HeZznE0kFqWdfP3tTehfT4xeRBy-M8dbpaKiEVZ_yHhifkzgp_d3IG6edBJJuVloC2PMKiAt0h5uFhYWvopEWEFPb6tw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=tcV4Z_eXWPF-LHaT27U6Dlsi2MJSd7eEqNa4KvC436J_1oseZM7SuKmiR-WgcB_VrX3KB0t12ETi8lEkRuWDd5-CUYKkYhe2fAgSVp0Pv0jgFpLgn8kZTxm6cid0j3jWYBdFleSvr0jp_dcoP0m3AReShi-V2aU-_Fz6mbC7VB18xlAgv0PwwnU4nzA3OmChq0l5EYNuJN0z72RUQ3y4EJA3OPCPPRrPWLDGZvOT9RO8r15u9fIwx2q4S8LGTMGNCoe6zzhkH3v1J-pcfu-am7qm_k7ROXS7hM_Oe7XTY6CXL2pvBhyoGt1UqKyXBBq8_VNgKPDXzOZ_-dzKry6c3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=tcV4Z_eXWPF-LHaT27U6Dlsi2MJSd7eEqNa4KvC436J_1oseZM7SuKmiR-WgcB_VrX3KB0t12ETi8lEkRuWDd5-CUYKkYhe2fAgSVp0Pv0jgFpLgn8kZTxm6cid0j3jWYBdFleSvr0jp_dcoP0m3AReShi-V2aU-_Fz6mbC7VB18xlAgv0PwwnU4nzA3OmChq0l5EYNuJN0z72RUQ3y4EJA3OPCPPRrPWLDGZvOT9RO8r15u9fIwx2q4S8LGTMGNCoe6zzhkH3v1J-pcfu-am7qm_k7ROXS7hM_Oe7XTY6CXL2pvBhyoGt1UqKyXBBq8_VNgKPDXzOZ_-dzKry6c3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=gvcrdixqL38awv_M0mTj2C4jjrTn5HiMmo-73m_iY6BfDFAopS-It5_5Y0BGbAOZtPQIB45riL7GZkj7ZqN5u0l9aimR7sBSjS0HauzI-jPd3h95-GfQTN53VfvCz3RPDVvjUalvcPBxTlxvKVlGOklmOVXhBhY5Cytyo6ZlSvAcgXhmFkyJo1nJITvWGuljKx7NIDnLL3W_Oyixp83C7I_U2h35cwlYz75KOXydTSUm2PechweYj7lDI4YiZdIE5sDTgHaacLkAGqIXYArEmS1SVivy4rhDoQd60ME4hufyZUEJJSE8IXazZET12uZXv9Z8VQ9RnRRE2BiqoptoGTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=gvcrdixqL38awv_M0mTj2C4jjrTn5HiMmo-73m_iY6BfDFAopS-It5_5Y0BGbAOZtPQIB45riL7GZkj7ZqN5u0l9aimR7sBSjS0HauzI-jPd3h95-GfQTN53VfvCz3RPDVvjUalvcPBxTlxvKVlGOklmOVXhBhY5Cytyo6ZlSvAcgXhmFkyJo1nJITvWGuljKx7NIDnLL3W_Oyixp83C7I_U2h35cwlYz75KOXydTSUm2PechweYj7lDI4YiZdIE5sDTgHaacLkAGqIXYArEmS1SVivy4rhDoQd60ME4hufyZUEJJSE8IXazZET12uZXv9Z8VQ9RnRRE2BiqoptoGTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad7JO5Iky0JP6PipxAf9oaLGnuD6FaJL5uELiwaeBSDHlkjkg1J8V1DwtkWRld-QgL5vx2O5PolmJku0Oa9krtafS9JMi2fVMqJHMcxycWcy43tV4OGF382ClYsAjv9-9C9LXI0KAo3Iu7g8ChB88bHIc6Rqs8CeDpXdfIMOruckdq3ZPZ0EgBgBR_9yqj0OCD1Ob9nFuBLrPlxxAvItkHAWFYiI3kjuflOsBwj8_4oddWI65akhBo8HuMhrsj9-Z6Al_OdTfs-RHKW9KuuU5zNDQXxlisMICSXw1rjZPyiSVcKqwwJ7Dwmy0-8BR-hvB4oaSc9bxJFYemPq-mKVYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_DTMQa-UB6z5ZfOh96c-oGF6decyiDeQatp0mlL-2Q3K_tRweQytSv29D8zbxuRXK9X2v1w5YB3pZi2Q9ZjNo88Lw0sDRf1w7Znt-qsQ9T1Kwx1t1F76s3gcO38A8ZjF5WbYfzQLyGjoWiqc25SZSgn2PwXJFPQRytGb1PECXFhDvaNLKBasq49UcPDai6U1zRjKKIJhkltGtxzi5_rNYJZfUuDhOU3UMAT5-SuTWvLSH3GiEghQigpCq_TMtWwbS-Ns8l2Yu4IKDmNal0kWLlbJDZ3JJLNA8dIuPJCz2efxyLHsQZxBOhkh8ezbxJq5Ke7hCUH63GJI1uzYzvBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=JtMJtYKU1UCVo9NITs5h-LFYclAu0gYNslbXQUKCc0r9BSBrbFyWWE8ZzOWmKAvPsKgaGEpD633xWYAPBnkWqEWsTPEEAATUHzRIHvAjk-aXYTWfnCR-G_qegL4WapvOrZ1wI2hF_FcE2l2F40uU5tV4HFbZNhND2-5umwyLfj9c9ZqfsEbsxJKom12xUOJGcsK2vSh60vTkNbtfxIrbYLlyJymL3BUuCQ8Ez3abx9B7ZB35YxnnZYnKTtLok0oiaOBmx-6yGOSHsktUYlbSkOsT3NNC2YaxwLmLlSvHFXSAvP7ZTNCWQPaVl9F9roGg6YL3CrU2qaGCfzCpA2E9UE9XR0WxPeEG8ekO_NiCf7J4CVxNRmE4x0QWTJW1qFy3nbI0PjeTALoheWdzod4PnIZheU5aCM-e_4roKYExZo5kKvRSKCzOr5DrgDLQwrb8iZvm_RR3JJJ2HDcWuU16a19cC8DopDXJsodKsvTy7RMpoPciZHpdhek1P0CKSoMGIljJ0qRErCI2uHFlcQfPR3WYI6lcIbpbgXFcnS9vWipwUcxl_j1PSOOabDULT2rZDPwg04N8RPokf_jANWNEpNiLr-7X9IKdinXFx2Fc2S0MQsH2EJ2axYSIDz17UpEMBCpwwpb-0UNqeG_3JiJK10kDAoiiffCOq0D0dD-IGhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=JtMJtYKU1UCVo9NITs5h-LFYclAu0gYNslbXQUKCc0r9BSBrbFyWWE8ZzOWmKAvPsKgaGEpD633xWYAPBnkWqEWsTPEEAATUHzRIHvAjk-aXYTWfnCR-G_qegL4WapvOrZ1wI2hF_FcE2l2F40uU5tV4HFbZNhND2-5umwyLfj9c9ZqfsEbsxJKom12xUOJGcsK2vSh60vTkNbtfxIrbYLlyJymL3BUuCQ8Ez3abx9B7ZB35YxnnZYnKTtLok0oiaOBmx-6yGOSHsktUYlbSkOsT3NNC2YaxwLmLlSvHFXSAvP7ZTNCWQPaVl9F9roGg6YL3CrU2qaGCfzCpA2E9UE9XR0WxPeEG8ekO_NiCf7J4CVxNRmE4x0QWTJW1qFy3nbI0PjeTALoheWdzod4PnIZheU5aCM-e_4roKYExZo5kKvRSKCzOr5DrgDLQwrb8iZvm_RR3JJJ2HDcWuU16a19cC8DopDXJsodKsvTy7RMpoPciZHpdhek1P0CKSoMGIljJ0qRErCI2uHFlcQfPR3WYI6lcIbpbgXFcnS9vWipwUcxl_j1PSOOabDULT2rZDPwg04N8RPokf_jANWNEpNiLr-7X9IKdinXFx2Fc2S0MQsH2EJ2axYSIDz17UpEMBCpwwpb-0UNqeG_3JiJK10kDAoiiffCOq0D0dD-IGhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3Hy-u97VCqrzufNz8AQo1g87hELB92CKOKOhq_rPiNuW8deFXE5Zoq-pDK4qTMjernFI6MoLSQ06p9HVV-qN-PraOmYxTI7F_LFT6qHAY91qFa-WQfQHva6t4kEBBAJPLWl5FJp0ggxioJ289mnLEJ7wHRbW3qW0jjPiuhdITtLSsHgZVoEL0D0t1lB6Y6FzbvLL2LJJdH4ySM0xqmAKrtsuj_7hpXS-1iYlYTsQnuLwLyt9gCgaHr6gzeopzHc9w1y_85curanXyO7IzFLIxGZ-fPp9DvWX4Q0_lcMKayCCRdn4oOOqJJfOYQFAYGDYCJjvKM-tyRo3gP1cmPUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlWltGurRRptnRfT_ckUMl_i_pZib8vpY7qRP3JAokIr5RZp7e5cyFfvTse3P6ZNkP0nGZRu-5R-eIqI_KLqU0rhvPIwYjVoa32A7eCjSvjXZKt2igOY9AmbRaGOICVvE1NO93Cx2uQGmFH1UE3OX2k3uy4_-nk74YQ_ooJGlImtaiD6N059ww87i4B4ROe9eIXo85sA-xQscqLQVbJg2o6pgITtg3GiuKjPp3wWZkuj8PuqhIGIAAXHhENV4hJye2YuSgTRXrigjb2cl6Snkh0LKkABmxO1lw59Wb5zEfdFYuLNwm5rVqrWGW-3Dv22qyaOH7xEoq_r5li21e04s1nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlWltGurRRptnRfT_ckUMl_i_pZib8vpY7qRP3JAokIr5RZp7e5cyFfvTse3P6ZNkP0nGZRu-5R-eIqI_KLqU0rhvPIwYjVoa32A7eCjSvjXZKt2igOY9AmbRaGOICVvE1NO93Cx2uQGmFH1UE3OX2k3uy4_-nk74YQ_ooJGlImtaiD6N059ww87i4B4ROe9eIXo85sA-xQscqLQVbJg2o6pgITtg3GiuKjPp3wWZkuj8PuqhIGIAAXHhENV4hJye2YuSgTRXrigjb2cl6Snkh0LKkABmxO1lw59Wb5zEfdFYuLNwm5rVqrWGW-3Dv22qyaOH7xEoq_r5li21e04s1nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=sAfwfWrVgP0szHrRLoVnFq8DTEX2VrUfBluJ9pBbs7v1OJIDDtyM91JiSwlKnItxGAJuVkgA2859Xxsp9EZxFX0wnxIi8MLKs8Oltz8AI97RzBjkx0kClySoyJJkBDd-dayyP34naOCdyXbvT_4Qi_doSC_Yz_3s7eKwsFryvT9vzS0VVKHA3F6fyf1x-R-Vah1c4DdVYjJ3JaHd2COc-KW03Ho3hpJojuuP1hLO7FJiq5GAmsFd9kkkfY87Rf3bESNAXIDFKg9ofOQQUQOQ6an_zDH_gcUfiYsUuR8Z6sXYnqVU--anKW3fGXHlA1VvU9LKaa4IGJjZS5n9VYZgQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=sAfwfWrVgP0szHrRLoVnFq8DTEX2VrUfBluJ9pBbs7v1OJIDDtyM91JiSwlKnItxGAJuVkgA2859Xxsp9EZxFX0wnxIi8MLKs8Oltz8AI97RzBjkx0kClySoyJJkBDd-dayyP34naOCdyXbvT_4Qi_doSC_Yz_3s7eKwsFryvT9vzS0VVKHA3F6fyf1x-R-Vah1c4DdVYjJ3JaHd2COc-KW03Ho3hpJojuuP1hLO7FJiq5GAmsFd9kkkfY87Rf3bESNAXIDFKg9ofOQQUQOQ6an_zDH_gcUfiYsUuR8Z6sXYnqVU--anKW3fGXHlA1VvU9LKaa4IGJjZS5n9VYZgQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uf5_nJK87u3YfW9jA4N2HVwEUubbvoI1ppbnlPo8jhjfZvetnfeSNRK3BzWY2Qda3qv-3Fo5dEWXeqGTuf9kR8V4k1LprjUkY31YNIiDV6uW_jSaeDqSGW38jddhvm8Zqp51HKHV0K6klDWcTzE-BYKHhfy18GRldeOWrpeygKgOZcHKWy2tlyevuur6NPEVawYjrC4FY8W2QPlPyQCgHX5TszCerIZXxyoCryP1qSOWZneruEp4pzRFd85GTpdLvmKqnCPMtuTBo9oh6-288U3tmRPaliML11u9mFbE8Mv1uT5p-1qQkskmRQB2gTks-66z6NKZcSqZELx0oUxonRvJdglfI8HYfxVOTY9Xb7cnSeWi2MfzuHT1hiVjeYfCbvxGBEf7BB9D3Sgg0jhHNLcTRDrexaqMw8ef6fH1z4dJzTkjRyBUT7FP4AFE8NOSRtlDaaZPkZXaw2B3idv2Yrfhk9AcyEEwNYZQOZrFYD3r2AwTKvKJdwRHB0RI8bbwzTcn1tJp-XJJ-G2epmUEpLMwEWvwkGGKI_VWvpg9ly_-F10_uKvTzCWYtBiIyyFPD9wIm7h0UIep9rN8zQ6_LYl2NhU6rajUtDzFXNQXGR5qfQr8V-xYrPdGl4PZIyzfxsbUJxesfqDhsk3g1KCIu0w6rR9VcQYNKYbDgyQJpzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uf5_nJK87u3YfW9jA4N2HVwEUubbvoI1ppbnlPo8jhjfZvetnfeSNRK3BzWY2Qda3qv-3Fo5dEWXeqGTuf9kR8V4k1LprjUkY31YNIiDV6uW_jSaeDqSGW38jddhvm8Zqp51HKHV0K6klDWcTzE-BYKHhfy18GRldeOWrpeygKgOZcHKWy2tlyevuur6NPEVawYjrC4FY8W2QPlPyQCgHX5TszCerIZXxyoCryP1qSOWZneruEp4pzRFd85GTpdLvmKqnCPMtuTBo9oh6-288U3tmRPaliML11u9mFbE8Mv1uT5p-1qQkskmRQB2gTks-66z6NKZcSqZELx0oUxonRvJdglfI8HYfxVOTY9Xb7cnSeWi2MfzuHT1hiVjeYfCbvxGBEf7BB9D3Sgg0jhHNLcTRDrexaqMw8ef6fH1z4dJzTkjRyBUT7FP4AFE8NOSRtlDaaZPkZXaw2B3idv2Yrfhk9AcyEEwNYZQOZrFYD3r2AwTKvKJdwRHB0RI8bbwzTcn1tJp-XJJ-G2epmUEpLMwEWvwkGGKI_VWvpg9ly_-F10_uKvTzCWYtBiIyyFPD9wIm7h0UIep9rN8zQ6_LYl2NhU6rajUtDzFXNQXGR5qfQr8V-xYrPdGl4PZIyzfxsbUJxesfqDhsk3g1KCIu0w6rR9VcQYNKYbDgyQJpzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPlfAe7_Ut8j9bddaacjWS8sRjzDto-s36iRwuWjBXfYy48OBo2CNSfrwXjWCyVdJVWunykjFlxpMgy5REwhPAXk8Sbuwstk-uEhM8ZHlD5WohBr8mfwKWH3a1xS8QUf8P6YoNjDicrHk_z-u-S4yxwtI6go6cQDgl6eO4OWGGtod0nZofJHi32BdNGMqQSJ-ekXmwFGpZNwb6Di4n-jEvr1wPAcNdbFq-NJSEijx79G-peqhCvXm0KOJv_Zd2CA8ADYJ9Vn4mv8eABSaQf7frJD9WpMpbHA2gzFnbnOuO8EHOZOIhlo5Hvo1ZrumaQ3crHFu8cI8KldUicUV_lReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTbwsvRgMvXDhoHdWznlIRVsZfsTVnaCcx4NqkkL8dzUYYeB28Q7ij-dRuXv5lafbdj8RJ8MSpHJWGy-oJ7W27TJbG9FHOBaekysEeRuGSQXqgix4yAZLwPq-vQFyIZ7THD9hut2Z6qEdeRstRIC-zpB-l3c3-tbZliAbnBGD7MECfj_aITxcHjdu9wSzRiY_E6By12mBfOSw2xuozC4DLuPKlcjYak_M0Q_ox-ivHysuJi6Y112KV4cBL0H3HCW9bTJuVGYjuZ7QbtjGZ9rvWpWrWP-0CaSgJJu1yRbvCuEugqp-I6ENMjWyvTvzpYsK10LjcPQ9sR6TE9SgT5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=pwsjjHIeEmSfsqkiLNY-i8N1yjEgnCgtBQw50pwMsX1XuiauffnEvem1vpCEtoz4vaJEwTex0RAXH4vHCMNXsrt8H6pxL9ucRW1HFnSxh2Q-ePe_E5Ee7eo27Qs-NTPRNOhjSbNZr4CtdRFd10rMkuXz9JZJDDDZIQVePCLb0pwJGNZrjmgISx_kZcR4SQRoeSy0gZj93qDKeDrV83_2-CbVfRNAjNnkP11hM_vuCys0cdIMMDYmyMAzGnPZfgYh4Rp_pJ1fvY-7oG3C69-AY6ha9rPcLOUK61l7RV9Dy9mqAPf-YpyNrA5eqDanYzO0oDeNmscDMqQ8XsjjZ4WnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=pwsjjHIeEmSfsqkiLNY-i8N1yjEgnCgtBQw50pwMsX1XuiauffnEvem1vpCEtoz4vaJEwTex0RAXH4vHCMNXsrt8H6pxL9ucRW1HFnSxh2Q-ePe_E5Ee7eo27Qs-NTPRNOhjSbNZr4CtdRFd10rMkuXz9JZJDDDZIQVePCLb0pwJGNZrjmgISx_kZcR4SQRoeSy0gZj93qDKeDrV83_2-CbVfRNAjNnkP11hM_vuCys0cdIMMDYmyMAzGnPZfgYh4Rp_pJ1fvY-7oG3C69-AY6ha9rPcLOUK61l7RV9Dy9mqAPf-YpyNrA5eqDanYzO0oDeNmscDMqQ8XsjjZ4WnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
