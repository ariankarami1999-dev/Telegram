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
<img src="https://cdn4.telesco.pe/file/Mm1QRsHlM6A-W2CyiV4U0RNaha1SWCnq-H4Ys1A5fIadHeRKqNDpDVjeAIwo5nk4ydeo4cxbgjlD8KtKq3tvZcR7Eye-9-aDMfTEqsmZRQazNEiE8uACIcFDjFeSn24OOS818GhOzOWdKPnMb418RKkenDd6pkQBvNKp6bd2E3iTzGAPn8B4sD-LkKGbpHEoTvqmTSkubi8V13x3_tP-BaE6n41U_gV3JAdDsbSY4cgUSqdPmV3QzElN1jTrxPkhkjHXqYPt-rFbcpuJ9CJm-SXu5MWS777BW8pxgMBxlbUfzB6RdC-WxelAjeCN1cyI19-kABnD8GxG8RowLPs7SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 533K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMBP5IS5B-53duFQFYTCZfVhwvU1l4-nbaQd8VhrkwxxxBCR-zFcgzAnmVTceF-I2iOpv641LCHR17c4OmIT_1ZkVn-xMQtnfbvhm9ydrXtHRoW90JC-AdTrodrMBcCj-Qtxa3fTESnUZa9O7XDx7kWKde-y4qdRmCWi6gWIjquRCOl8oUXjswUfbfoWiQ-B-BLOosw8slwG-Fh2m-du6hsguv-6b2VvNk7BfzPNyLyZdz-g9Ykiepg6WuZQR5A2zUbgCDVdwK79kv6vnWHnDWETIGVmVAydQKq1QYexB2YJcB7_YVQQtf_D7U3po3mQj2uqB5TqfDN3cGyhAaHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOibS_dwLo0JPUYaNsaJcq8_dBhVsUr8rbE9bTdZ3PlE0kPkrHMSpSa9rM7w9CflBGgjYVfsMDM9W4aXDpu-Kxp6yYgAncBi2cBc62PWA2PdkBjnsbkLfdklCQzxIpkQuWTeBUEEZ8w0NOYM2L9LNdNCVi0AHGMt058DlZss3jUaQ_wbDtnpnsq7B2yjGYT7PhdJ8FsUBaZJSPCPPpfis7jCw9dBOxSHN5zdT_EvE7ZbaUSR-GkbCjoX5Lt8nu8RPRV_y-fF5s1KYNib8oVO_BPMF59IRMp0e-nRZdPp5d2D1IcJn19Bq1wOCGgBQkqzfV5hXhuIPLoZV5anywUErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpW9omjGKI-mFKZZM4EBkf8SbiFIseP6h1Bg5pcpu_CHQ352FaSy4CaxMuE0SYTzkwqo8AkObmteTIUcF5_RfMrl9-Yqe_ss8iNPIEQtU4qokVotLwrYc7iNH7PqkxwPMnU4JyNi7ZgQg0J-McOO-C0AvY1w4mQbus8uc7MikIUxVVa8l-Lc6bpZ_5orGBGnlIJTup1y4_Tsxn04VJZEF7HiEAUmC80u_91zm30XgLb7NZGihFT1jdkeJGrzEQk9Ca391FEtLfBx-weeqnQgzmeIHVJ_C6IVHs-0ua8beLq4VkilyLpfgmD45hwVnSvOLUft4A8vRAI_McrV-D3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSY4el_nTO_vcoZG3J3_XhULPmg-_EebZfABHt70bHJQRAdbISs6wKmAvt3WLG0GCqdfySu09TqiHu_tz7IxOXYpSlztyqNODDt-_FE_UD4aK-a_ePm6NzxTYK-jXGR_vwAhzduJ_708HwwVDOZRkW9EX3fo2t362Ly3o1y0tEivDgsr1SsG2rs0RKnu65XyYetIOyGqV2pv1ctWJoFV_6kQm02385P_X6L8o0K2krAfliMfCmPKP-b7lKKUiUdJh0dNuCnU6pJgUS-vZMa1b7iXJBIrqTOM1wrTEVP4u_ZtCYv_vEfOUW4v8alWY7ig-jxRF1A88qENiW0COSwREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته پنجم لالیگا اسپانیا
🇪🇸
سویا
🆚
والنسیا
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/29552" target="_blank">📅 21:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6TJuf-Cx4kNW-_aVimvbMA9BqRii8a0HfnllPlqzA_achQpDPNTNyanW8Wf13dSKwGzSXUROL7T2uY0-OT8fwOqQvhwkB_Y8_0nZDty5Rmz8iY3FPQxYG6GkXuBXxBvLQ7GsVZYg19xcct1GBQZM7yXm9N78vNr2f0rWAulilDa2lQ-t9XKecE6Vm1YUgDTDD8izaipLJgJxzvDtX2EdzrrvDFH5nk5-gSP-eVaDBeCUWyJMMBqHPNMRd2wGE7oY_wuuEpAOLXpvgjq4Gup-qWVx9ggNDJVU2owibF4oXB6kef3mPJ3BjUTM833B0G4CXen-wWuXaaddg4R8Vu_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4FXCy8Gfmqog2QaW3IKRzHRaGtWpkwMShyxDwLxUH6S1733BSjCSez4dohYW_ftAHPyHnHF-F0XAfq55Ufs94mLb4ZBNFOpCH_HXdy7UDjyuHpMYA8ha_R0L3stO-FOw5DV028_pR4XPpkmwV_ObW96sktefceh9M0dQA6c7GKIyzXzqW5VJpdmQSeedxb4Eo3RyuTCnlnzHiG2cQ6oARLP0Sb_kmjFtrpt5TXa1FdTMTyG4M8ECGngk-awZcLZopzwWLd7lnXv2E-rRIlpPdKWwyGiC9QUGuwRgYu2_a_BnFuTeTF48ZsJWMtoU2516Hg_pjC_sENb46zT-pRalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tseDpxZ8VKoYKtg-kPeEzBIagYoXPoyrBQVq4AqL0-vOsxMcl4_LZ_yJYBi93RumLb2BsXI7H0c8mb3Re1hMpD38VwA3xK3Wl0Y-a1P97BaRqVp3GKDYrosb_a4cVP1b8icq1I0r5GvIJruumxpPMM7b4R4Ap480Gn3FXWoJ56bSdtuyROSgGnoFKGwacnQLL0_ScpnaQP_ZjUCGJjyAVxR3QonURwsperGJn4O3xZ7y8pCbptzUlzRwgpyjyBhl4YCFLIUCqUTPz3mI18GF7GiOP8NV774hXOC2teplYYY9NKJ6oCAlG8TTsmWYuGX5hR_FQaQXEo3VtSnyTpXfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg73U5CGEmk11wwxukTvsqaL0_RQ58tIp9xcH2CbFeWwChHOU8TtZuaYwuS0545pje34XKxkBELUjH7JYLOX0igCQI-K2Af9_Aw-gHzNCUuDMGNiLMQiSho-IJzCpza12OZjLm53VQi_UDALYz2GrLIcmXYTMH2NCq9Y0yUS5Ul4MZ6Sc4bxZb2MboZAnEA6cj9mh_dn1Ng5zIwp1SbdN5ktLMdDkXzEaySNMiddlgH6jYS8_wBknvNOQFx6Y5x0OwvAIt2ivi6711rkRMREhE9Ja3-VbzYOTASPHCPFU2P-j3wGtOt01m5ywOsVhj5wU2fOQ82Yhjw5f1_zfibDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXW1Tu70QeFR1iSTfAaiACzHJ_g7Zryi36xaM_Xqbc8uD_JlYUA2Cl6n6hkgLT1b15HrtnvhTRKisbY8qkB_2aT1vYhj_LJDG5jUL4xaLgEg0jjlh2I_symNqfARmWF3eQ_aiIEpBW4ASbqDGX3r6b2k-yxp7meCD69lUihYchg707saHTRayWEjzKYCgh1n06QE9XUkQE03WqkHOULF2Qrz0vFvG0rb7eWu9ny-OJtkDzo3CCpk5gWab-E2KIVS9ufaZZudGDxF8X1aJkKgGnirGTBqQ38U0nhGNoIlHfUTvjhPuneufBUUKZR7CIxNBcfmedyuNQZbGNmo8cG3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgC3n5Zpd5g-4zbhx4KXC3TNOzLAyyjFe6p1Wn4BTStfFkgAGIIH3MIsruoPI6-6lZmgbt3iIk0yWktYWMv8Irmk5n1Iwp_w2WNJ9ebj2Sps9kr8hUU5gAk7ayNdfKSKZXwZTLEVo0hb5m6lTvJV22epEKi5qchQMQToqZWU7OVdOAFYoVMCYS094Vn4k8naugC1EZ_LLfQeNzn9e6w1ObZfD5GWPSjC3kR-jH8wzgzvklTL1dpJSH4OOaGzZx_PiWCmB51lvNSuEv0ZLiJCC8ONkWfw911B5Lj8iK_HOMmrAQ1ufrJ1aKl9rQwJRkfV27NhdtkG8BsmGjWdUN17ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzYnJ77m9SwJ-ZJGeOR2Tg2azaoEmCgsRZr1wGH6p2E0p_gHNqpDKj1IEer-NLPAxBU6jxULY12JGirV2_k-3K52mZdGEwmzUG5L3yz4Hqquzi1TJLGo_b-2I1D_JPfHA_2fWWA4dtJI8gqIQB0bQ91GmIE6JC2m0yyWz-obKWBBdZNi0VIdTpF2Hk413rZZ7lmExKEzkBDlj2UftUwAbjymqGHOSW8i7Znix_tL9f9RRN1wCn3yZ_QJnz6wlUWNMc89meHol0P9-VQ2G7CZzSaZoj6iTmLnWAO52TmqtSka5Q34V82Lx95fC04tN2WZ5mFRJoApWzuUdi9iaYrM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH49KXbswI0p0nTyx1mY6zkzarAAJo904hSx4u-zJSmnkJfs4eywrXTP0ptr8LNGzshndIfJWkiwxCpra9_mgv_DPBapA4foQvVomyCUddLpaS1gojgJpEM54HfpmtZoOTQmBhjM_RJ4QQ4oALxRWGDkhOZsvxhgeh87T-xA1sx6hpUTYVqFYlPxv3jd4oiJnMEdVQSPB8K1sxD5Dw-ldRsqE7EZrkc2JUVkMJhhnhZE2hTHDF2TJVjXVVdX3pOfZPYtV-2J42Wq9gTmIvQeK0FnbEgyiJDgsl7C1YUGtRn4xAh19yrMs5xNuXmkfQTVJziKgplbEbw1KgzTDkrbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریزاول
💖
100%بونوس‌هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100%بونوس‌هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:g20
✉️
https://t.me/+7MwKcg4-gXBkNTk0</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29543" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxcjMdHCybd0JMMB_CocShk0M20zcfGqNdOnvCrAPADNjQxO2aGEUZMtXHmXVP_LwA9Nqhl1b-aGSNXP8EpwjegfGVp5UuiVKbh_lPu7cL31V3BFAdKQxAeFeMBUkET3D4gnrYiCqr5xndiLi-zcsHInN8wEOAKUjoJ7pVEttEKXCkUeDVyqhqJC26CsxNWMZJdL4S31l131ssztlWdSD5q5ByJ_L-CUnRR8bj0_okYFlu4ipSasjd3EaMivuuOJgCIqcIq1BzMZI-bNKEZviOaydesJSvarRSo5PafJoFRsK-sNNAI_k-dY6UnZSQ6ra0rkZMJ-SZvL-3jzy1qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2Q4YfIQynAdJB0B-XtJFbHGb5bW-sj3rXAKEG57K-jN0qCjHpS-7qfD8kGoh63W32d2yEv25_zFge6_hAAS2QO-IGsPelpx2lomqrdSndQAqGC9MXOF4JaXdZ1H2ns3xPoXu-aE046CuqpeidqEPf2ZeZ_lO_ip_noio_uUnUyFqy6HDwmjQE1BzwAmvN86moc62O1y08d1SpHJKIecp_VtolZscvglbdgAn5Plh4q5LtwGfP4u-GIOaVyxjorqpEtmNl8q_rRMplrhzHc8cqhzkPxjS8Zye89a8wr8X8JfkJDS2Y2H7c5cc0ytehMuqvh5RXHb3WBgvRX3o7Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNKSc6Hd6ZylpIbk4LDvAoiEC7psCAPk5Wl5jGRLDry1yLNcO0ImNTh9iHsQfOBkd1JHHRawC8uGhSgO3MXLaNnTjjzf1LZVbCZy_ZL8MMd5194lq41y7ROOlJ9f9H5xAL2MI9ckHQoFg1zgVbgkG9wlXNsxjizdHzffBVLUFWXcU0w4Xmgcyv596GbDzlqCfSl3vQaRGhLQJBGt4t6QK05Hq4zJrI2jVvYeeNdkpt8KquZxtoujWnSVeii3BLzEuKOjK-I7QArbYHONGK8rxyLFBKNF3gXcQVemLMOwCXizk6Aw2XDF5RSJKO2QkXHaPwopcE7-qHM48dzFY2qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwBjM2XuuyqRtympqjaJgR-0NPKJ6XRhN6mkI8OmE72ezKIC2VlEnRekMkqjSv4PYjMDneboyVt1FDJ7I0T4kr6l0may_8vlCOkf7VRpq5let1VkkzKD5odEi-NDwWHegCpuEdRymlcsURkYbG1xFB6aw6Y8KqhvsViFP07cCMZUUJ8B1AMCRxxDWy8lp8y1FDPAADY_b4VSTjaFkLw63QzsA5K0U5nY-BhoiMYeoAFx67ac8FLtTv2m9pxbqIaJxfqhQr4BsIxI-pybXv5_SAep1X3OdpUGuSnMl_3FLM-lZq8QLf37IClF2sUcXvoIKvTo4gZzAnSfvsGSN6EWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSS5c09ZBwuO2ve_xawZPmlyCMWHE66DLrCqL0JgAL4rsrbXoiuz5gM7toXWdzkitpt8QEQIHSBuuIvWmY7MrsVhYE0gzNXtSMi33_iHHQ8MmXC_mioYgpQR4ap_w-5fIANmpMKQXxrMPCkSvveyo1h3JRQ4FmCZ73FQTNAbyrtMY-0VdbpCPyjWw3-5f5xacTjJyptJQMt0GHSMAvJWedUVQD5kqfVrkqO7FqZXKu1Zt9dOlr9K9K7HKYWK8hBpVjDq6AG6ZG3Dp7u3HZGuwsavusF0MXpboLC2KlK1UikCO4yeVwGovxOFQPSppNqky4IzWO26XPkax6Q-l1IGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFreexE0WqW5djYX7ex-gH6PDilVaHiIdO_EXhLOpzV1foJCFq3SnZtQ_TFdc-76WhIoDye3dFNz1U94w6bg4VwlSgkAuVTrw1OJM1gSVN-xeePF8d6cRHdJhLN2CaaGlw3FgkkTd_ZBqzyCHERxFIbUD1B1386Bao0_KhxY0jxW8yppMFUZrXCAasuhykIkMzhlDB_w0mrPDPfYimvZPqC6yAshdDE60f7TBRgJtKFjxhrKmj9G6q4RmgtfM82m99AiBy1SWyH4e_w2ui4XeoPeIw39_sqcbHVyy_m98Ay5yQSI8V81GK6E6_kcEGg6t4dKzDDLI7jZUpxcRtR24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJTg_4JWhJMutSF9juR6v-Rx5cLiBDQtajl6fzgShEY-VxBE1hG32VPMKd66p_3TGE2Uw5f2rG_uZkoZNtwebfd1iUdpwVFBzIPY9lp4oCaf5T8gM8COxceDj5IB3YPdJVJqGDiiHcSriw3YD2AZnA1tJ0q-25IrYPkjFtYEpyuvdufZS7nK-ujz6CYUzaTCn5Z6s4kSshwJTt4zCY0YLJfBNsjc6Cr4Nu1T4tMASS557iRJ5oScfs4BSYVhuyazv3ppJsletOkmRS6t1nEDpriyns3-I0qoGximX53FmL7xy63_T0hMq73PjsVyQwBl6gjculXUYZyhDXbn0d8lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEHSIGQh0yonWPhUzrLjLdL8qCbrSSwfKIx_6VHp6l4WdA-VzHad3Wbp6dptdzFiKPHZKtOeqWCZZABIoAHJx7sdNw4X42e7MxtrzihI7YtmfiG-TOjpgWSnmdaZ_XhadxRojcCMXBJLgCB_-0tIJYiTr24tPhglFHF7Vk4nf5GElMK-R-MX1YiRNnnB9ch5KgGDfl6_Q8zOJPukjEO6hgJ3rEufnD9Pew3KV5zOeoGbAVq6gVxByFkG6D2WeH1FLQ7PlGyNFR_ng1jJrBQpj1qB7gzJdNfMX49irbgZYnk6wulH_mxgovptPfFZUbrPrTMyO8Nfk1l_eLrF1Xx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcOnzwTubvczbZKDNId8hvVMbURi74q4ontiv4FzGyQmURXi4PFsR7mhvuPv_lzDR2GLaIZ3bHHGdBbMCJoDBGgef6eV16wWjeU1i4Scv-iHjZzpkmpSU8JXVj7V6K40aqm_Ayw93xmvMm2Equyu7uzdYKV9Pg2sR_4NhuEWrsRekK-gCxAjgXUmJhQcVkcH_OsYKUjeKkQ_Yf3I3OMEa6aAbHxKXLLyy-hdWbCUy6AdkadyXptpc1biVsMWwB4vLo2i-gpSfl28-5Pa_qSURzpiNthP8_b5wzf0raP3CEvm8VpJbWj9z_tMQ4XIO3rjRQHCjWG_v_7hkotwZW9eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnJw2w4DJtno8WyGWS2NHq2uvpo05Qh6Xic535DCJWWqYXKzm8Drd1jAYm0Y7guJ09Jrmzh178tTukf4OSwviEA0py6_wsPe4ucWmcG-xRM1FGJh4_O1y3chc9Jh0P3XCeCOJoYyA7wbiZGOxwGMkcyviADrBaz2jd8DkLPjvAkFDtJPL1TRGupvCm1pON2Tm9ELC_DOwMkSDPkqEh8JKHgVSjH9QGhTaF1gt2IPUnuUFFcvGjXufTJdKAtXx0QDirLfO96v6Cuh7e_rqt5Z4nzhuUcGJcI_5kMq1L0IdxyfjrFCF-4JFhK0eEmjQR1kBbTkNaiiZ9Isf08DsF3byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ونتزیا
🆚
فیورنتینا
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/29531" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZ3m7HcstAgGq6u2zIswX5Ocnw4_VaRKoQl0I-Hx5liFrRXGmQT9pROxMVGJ-NcQ6aYCdjQFcR9Ddo9af3ZC1N1QftKhcbu_68YGL5tgNz1WK4uFXHsar9HpH6pnmE0h8riHe4ZEB_l5o9Sz-ouzpNJydSJxsSnJwBsRh5bdCL5Kay5uQTjdHgaAlzNu7pnr8-h8fNV9FLaL_S6i1zaoLy510nTfASg0Nae8w37YS6M0e387qQYNT2RdTUOy0wyVfd202bmruCrDLaEChKwOE8wgwn_nxmL-eFhtUldpMdkKXCCE8y8EO11sYsVmxCSigbNdssxSKYR6qKMNk9Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ0RoWd-uja-3y3E3UU3aXBOfuBRlqlD5I6dHEYD30MX6ll5bpIkTtZUhx_9KrySE89BxcWMKYP_PTDTc7TFHyoJNvlUbWgiE-jPyC9mo-q5VBTujmWhci2e276rWCTcvLIW9salSUz7HhxVuMU9Ere_c77XcJLVRF4G8SFOM8K321tjkz2-pZy5JF3fKeWx_OZRtSOaJKmabcTb2UhazjXO0LZniN5ib5fKp16IZwNFZak6AMsqeIx1AJd8-sUbNMY8KM1r39I5LG4-FTHurWTgTnlu58cUuCqTHyJPnct42ECKzCWhnt7j2tOJ2tklGf5QtzK9KBPzDI67vARo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzboc6U4X11RlH3G5ZhtQjv5EgX1joUiAsrTcFja88QW5-4DD2u1q_xotxVUk4JqR1LfNbQw-cZjf9whNZAQLhit92Iq5bbM1N67h90PLnlQntaqtsL65TdzPjR9d01pezB1H6I1iYIQ8pv_il-dFZtEFztGHmRISFd-ERcycGdz-AqfYMK7uD4BS_STvBp5dODAl1ITmcz0pavHDM1eLGpOEDfP6xxVUlk-Pik_FpUw9Z90GqrmxkpJ4aiGwiUUPjzDkLweIs9ouMkBk1_vaPc0_i8vX-d61vsnDlrJhPXjBdSeOVoPv88ruXaC1FmfmsfHuW_bw43AdT5IUYH2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-16LJajKqUzJ2QQgHb9jVqa33w2Pvcvpxs0HE1DBnyrUTSQrRZE-9r2cWqCps-6wLZRYyf6HoWt49sBudEHl64PPvzvGtG0Q1NEwvdX4HsNd-S1te2BqM6afjLu655lobu-EghEvuoHJ_JFLcmtb__Yo79Bjfga592sm1sU6_WtaDNTwsSbi2z9vZK5Bg61ZqQu-ErUy2d5a4naJ0EJOM5b0yUbf2p587wz9dxdqrl00UnkCEsrgIwRGPrjzewmz9YXOycYTmgP6sSyGdUY49PGzZfexHu4NUbgzEOeZfgnDyNvIgiWNtKFYVBX5SkVBwTNn4SDwMCN_NM6oZHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPy33Fsj0bR8V0MqfsAAMGhhCxkDQIAIKe2Y3KMKBpGRH3SkdVVBbEh6myOxxx65ODO6Mw_eiqbFrGg6ERx6bF1QmkydVa7XOEHV_Ct8tJk-OTG1WV1fxG4ZMHShR8vkNSZc35Ym6c64oAmsEU6ynazlipw2jwRImCwop5QKfeDenlvTN8S2zdfEFhwwCBMDSBpuq4sUSJLj6mJX4ZgodfdEnoWjbrll_lt_yjzo9mrKoZP5vIxcDzFH9-9aoyOSzEQCMi0Q5j2ruxcqguRkbvpChchhcP8636cweFU5RX3ASehYdBy6e__IBLh9PTkGub4n_ZamLxTC0C4KQccVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcOqjuaw0ozs_tmLUvj9Gcqkkn5c5X8xU1j1h5n4QKb3NABHVljFA26VfX6R3_skcmtMJjyCRiR8B9wTKr1LZQflvd7Gq3KxfmHjtt9ihxOw9VPcpa-hBmrWGaUy0Shn9dIzx3VALJjSCi0iXynI6_i0xI4F3nZN5fEut1GELItw9jTU3hdDfjcvmsIxUQF4S3eDcmIrh8UUrDyRwDSp2KkP5qEmoEeJ1YFB722TfUSgmTWvltKq_gXUZXujzSZpYYuG6Grc4pvN9mUi3-Ifr-TTLXJG4W-avTmoaA7WA_teZRC1ikDN_cg_q6zP8lIMivC9nHWRCyaIxkhKuklzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHhgE38MKs2fQJabHfAuDehKJ_IVrKqmYGtXi1MtoWepo4SeNeAEPXUckoGLXgI-6SpqLxkiHWo-0ERm8uk_D3hfajFwtJ3eorhdwxHUcQVpLiMir1nMXPwLIXNPOFZHOsroB3dCMAh2B1mMo9KdP_p1YJ5oSY1ejHLqX53RxUjHuzY42XbQJj91Jny0xhF6Wdd72sytvQPPNBohqzIbXrSWD6a2fZHq8FS5Nod2HAxNjTX3PYPgWqMZK4yLwGJ-8LiuwRdNbHi94GLVwvIZ7lRi1Brz4lBJiaunKKYSCR54iPp-dq-TfyAlj2_OWzt3XFC_urAfXfk0P7GCyp-WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7MqCbQH99GDyI6ANWbprwVRqiR1B5Wxk1eaA3gB4okKHs4fkOWQg-WwtCiqahmAk6Qlg-NHsY0RWzN5Jm_1nGRCp8YPYwJjyEHGpMxfyB831uVUFAjUMOlbnJm1WneKxPU3wUl715eIhZdawdw7AurwAtmRcmWwX7ydlia8ljBBmyc53ah3WFf_YySHfcnaum_HyroNxYpWQykOkQ2dKdHCFBceUEm_eOkldH8OXCo3xvKjIgouMox9wQbTgVrCG2EkzcOVr-8bdngJiCAbtZFbLrU5qxdPHRxbpBXljKN83bFQL8XlC7c8XW_C4fKFZZkZWHRcs5VF0aX9yy3P3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUexuaj_uDZoYBef8YDxX_TkfmLxYenYEmKA5K6-KxaCrde1RVgJbBiBCvwpPbsPYFCWLhuzKN7cRRMB583d3KkdwXvZiLRBdB4X7lMGx5HXlyuQdy9keoKqmkzlQoVbwteE_eFQQZG8XydPbUvDcS2bNvgicRVFNZhzgsyU4o8FUggwlF7tpWqkDjyE_fFHqTYcAIJo9A7dfAnNt5SyABKy_IoCpF9QawPLwimOCCJK5IrT_Dky-SQKVk3NbBpjowYC8KfT244dsmhzVJqBeKLFx_hfraeMm1xgIWm7o4UfK-ynTIUYtAHxZcPUBSaHa9qlQ-Z0lHdH5DhoIG3WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lvs-x-meWay4WZsgr27l7C9rgeFAQhzmqFa0CaUcefsK493nfwLRVuV0t3anB5TG4oZUXjqlaCURayNligdt-jlCP0XqgDZaIWOkW7MdmMH8gwnFPuC56SSMOEsLEvAW23roO2SkW-lbjSihY16N6EOzweVedFpoDbmOZqVJiECDqeXjXWlYeht7Du8Yu0yOrub3M_en3iCEaOkz3TXV-8d8B-YOdDU_qI7qKuMEbyzryZcdCs6p_A4C4tf-MAk36PDOnkiz6s1EIgafdKL1Nip1cN3ugRH-ViEYyNvX6SWYztowBpQJBL5Yigo8GxX-vFUX_7gmjw2yFakd-4Fpqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6AzB_UowzcgK0oEmyZ66yDB0O4YbG-jvdxsF2-BQtV1PptY_t0XD1FlcWHNyN1n6HGJrOM6TsDbIGmpwOoPh_-JtQnkjNkiYRZG08LRL-yBl8wgdfpTd4hXQWUyIho8GZiRhl6isViZmgYvd_-smuBZnSQ06Gc-im0bEj1QVeMP70oMXuHcbgGUfRVJuvCer9kODXuSxVbtjiyfeXCDy0pOL8v9FAPoShKvWvZ5fS0tfmdNApvD-RNGCfZR4UmOi8Sid34nfDkpZcGix-r1jjRoXayNnFzlGufU8e1eVZV_qdl4wfdwAQxmyT3Yo-chhw4qmBD_WcemtZ58nRP_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2FfLcRbCmgcTgJBSpfM2lVDua7oXx0MvjDJ1ESLSVbejHkLiK6pJPZ7jcpVvRwMDSBN7Sj5SqUPbchCzR_3175ZkN3V_ytt5LaVTaFG8TYWKZu4nloToZfjoTDQ8npP6f9eY_yIn2BeTd3t1AIQlGnzV_xAf3QQAsjXb1VVJ6Zry6q6EJa7D3taEy-G9akA6qG43jzSM3EOvzLQpw2cbktW_cfETiXV22oAZ0z_LbNZfhXiwLytcPjTP32vgj37kxbw0kgMeXKUDY4I9E5BfGs4Ti8DXsway3yB6hHcbaU4-TT9h5_xLhdFHmPBqXOaw0zJnVtzdttVnEDytVfUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJmGW_SolXxuv5kTIv_Wx2TMeRxKosnIAM6CvyQjGBaSLuiqWjeOeTJavau3iyexVtYWgKOl-COgh0NjkocruJiRbsPQ26RMluyqiQmVTUkkyX-EpzAbdfWAGlzGnZbsutWbL71cQTveXdEckPkVUJ7X3aIJGaeys9gxwX0VEDJTdysEsToGsx9EoIhTynDeKLhpA1kSFN77hlhh7P8bOlBHXQauC-Urnir4beWrq7jl9ALYrlfapsU9JGsaZjIL9zpznsu2pDYOzoMKVmLUrfz6cCK05Jl-9DWyHYKbhepswjrdS1PZvyxg_Va1r9XK_Pg-1m4J-BSl1YW59kwtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9CuWr_6VVkV_sYfAKQ4x0THsWx0JPi0uPfg07RYfAUk6vbMj1GXq3OKF0sDeUj_oJoKxjA0rJ9l2HjCoD3r3nc3wV30-JUZ1P-ki9oEJ1x6fJfPHtMOgcigA16RLJuh4s34AIb6RKBd-9xn7AqkTSb4Tjzr1vUdAyUN1ocIk-z14ll8OlDdoIF8LVAQWZ2JtduAY9ck0j-NzLEssTsSAU8Wh4UcOqczfdravuQrmCwLzfclPJbbpK0YTJXI8sVfQFNY3NTfQxrKrWaB2Pt-wJG-a8ndhd29ZGwWOGpMZWX1pP5kI2WXiGQF3ChcdUV38uC9Jt8MQ0lQZB4FLGsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3wkhJVRbLFLzI33JQ64cIeL2MYywWq2k7dYudYPz2eKHnvdj4jtVE6l7E1-FDQCCqolFb-S3syiQ0j5BdSbYYydajYyHjkWeIYRzfhnTmEoFFsp8RSqKlcfuATRpLqcbXGU8IBcULUEzi_TgJ1EfGPNI6YzbCEpt6CpKJRSJpdUoWq40lFBmOrpLflMlexj4crshR5YWjcqJ_RySCL1-uMIHwWBXXhbJ5xQFnEkjp2zy8f2sf1lacqTaNG8uu_ENnb20H2dfX3b9JTDC-BdrLF1ZBfqvT1rCeV_BVLqp1lh1gpMJ_pxu-cORyY9_Wi9m33XtdchSHBdhw2lyPEdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2CRFjQ7KnUDcDgP9cOsGv3m2Rt3jsPTXKVkJ6F7yrjKuMHZt4hrY_ijH2tio67fT2u30eWsRycuZYpGKEPyJ3h8Ji4a0_cv3GS7mtV_AduyOi_WSfYbNYe5wheW1mzUf3fEvfnJgOz5lz0d5hEMsfqSFHeewUZQ_6luya_2z3JNhdRqwv4yJolp3RidhpiFA-QRzVEYa-sVHwRvIf7lXgcBb1xBFJl27mr7HgJBKnWi6C_UVMef-i0o-wTntiqum-h86_rZvXsstxLAvfGxEPgIHPT696sx8ZDHb6JzxGkv2Krq4qdK-5soizhD8WokATIJvvVisdjYSnA6SU0yeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ30_tlNYP_9wefwghcNfOyrpu98VCCjjqjjBK6zVWJfbm5WXDjjle8ukDEXmV166mTAT3MBURM3bQ1WI1CXsaUuPeEGe9GXM5PFOayId2cYd9JBhl-QI2uZ-uTsItcmxH8p7qWQIc-9EpNP5Ty4SfkFUATOkfxdaEh-rkL29Q0NE1oU3xSQTkOHUS1rFk1q7Fkd6miVuTCXEJSSUzdTxln2eBk-KzYSAmupYWyfraOHqpJ_p518vF00WsB5tcjKND59yLpixBTheubdb088Q9nAYxkR58M8SAYVRcZQwAxWcH5RsNRN65-BgGY3qsGADHTDhQTwESWBDHloMlsjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=kK3XiGc-acZsk86L_xC8HswqCibb0Xnjp3zct3GV6Rx-as9Y-bapKzOyKQy_MwlR3HhLZhq2NfNzDfivxy6jW5ty8ckQan6NLlzFQIk9X93CXcXVaH-S8YBrjprGiIk_QmVjy7NCaskNuuuWlObXS1NQTc7joZGvS6x_-678vomt7V1CGkg0TAzSNt7gbsnTkoGoRRM2C6auytWt_rdhC9SscOuG9NDHFmIOBstNQih0PC1v3IhgdiOaimWQTdFjk_6c1zgX103fDv_H8KWC_px-Djq14VXKDWiO05fVaPjE9HUqGwFR8Bql4IUQOkvK4vuzVEwbtkVOPC8gY_Kmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=kK3XiGc-acZsk86L_xC8HswqCibb0Xnjp3zct3GV6Rx-as9Y-bapKzOyKQy_MwlR3HhLZhq2NfNzDfivxy6jW5ty8ckQan6NLlzFQIk9X93CXcXVaH-S8YBrjprGiIk_QmVjy7NCaskNuuuWlObXS1NQTc7joZGvS6x_-678vomt7V1CGkg0TAzSNt7gbsnTkoGoRRM2C6auytWt_rdhC9SscOuG9NDHFmIOBstNQih0PC1v3IhgdiOaimWQTdFjk_6c1zgX103fDv_H8KWC_px-Djq14VXKDWiO05fVaPjE9HUqGwFR8Bql4IUQOkvK4vuzVEwbtkVOPC8gY_Kmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgwo1kX9_WIj_NVT4O3rW6Pe81v3YbmDEUD4F5I4LuXXOp0aKtfum7iVJv2XpUccPxx3261TsCkKov2rzpqDMUID3OJ2AwM_v8J-fbsSZt1qIeqONNtLxe_b_UkCdLwIJNjNmoC4InX9qVeWcQ-MUyAASOJujVRZlJvbOTSqEBsLPtXj56bij7gWh_9OMx-wlfkk7xecHwnb-JlzsQOpDgo6YMA-ZdhM_m5NOlJHHibniKlm-tnwnEtDaGDmin9if5UWOJoJfMIDIJs6mHPrprGvdSX3pjXBXu2SOIptAvFyvQppzYQnImK6G1U1AzxtVM0RG0ZT-xnzhvxULprj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIpRo1GGEbxOw0oKqgn4vpwSn833-sv_I-eRHe6RLLuro0i1umi62EhBQKabcqPdbP0brgAZRnjz7CTGy7Nzas7ONYX6rEOKWa4IbQ3L03i6W7rrC6KuHes9BgC_BTm3l92OL3xuzJMiExj52YIq27FUf3qPWcon0Ai_jscQdJclHaymvf9JfLUc7DsfV87bRDOQsTNWVJmjLCBjI8_ImLNt_ms3ouunPh0LH4reHRdYR3FO8uABtUZIPCZP_4NGuQaJW3Hzjsoq_keZ5PvONq05lxJwbu15dONOkR81gLSCnfzroFe1NiPvy0f6W8QJbn_mNAswbbLQnFMnvusXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivKrwtlbILpLX1AS8lX_BTiVEni2yuScQiaJ0RXxg8CyZV62LiPCeKnnFWv3LnqHFy927PyFLEKbrpoQU7xmBGj7mC_Dc3q6-PGLO9jGHGK1IqX5P-npLqNVVfJnshueFffYAZRtsqnJpFGBqCn-gPjAVl8dVBX7xlFOkIPd-RqHdG4x5-RtO_aQPWPTB4B_v7WcBYSUxA-iGkYuXfSYnPKSxspiTHsqOoAFFSOhtEcXZef4KkagM1vZmOUL8aDUmv1crEI92CtaEUil7yWWqMSTgFgftrsgs37o75_2-lpBHNkAXEjZa2Ut20EB9N55Xm2Lpt_jmGShoWnOoWO2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaCNyQKmRpZQRmIjPGZ7yl4myMCf3PBqaAEhvztsAbAi0oYt4dZ0WazxqGmvE3CYVtp0mU3tJp4TAyvXO5jJNZ_7nTKfnwDnnl5IWFuMff42baE20pqbv2wZTGNQL0K6zDpJENgRFI_kY8rnqHg-HyXU-eYOq7z948lFNNfhXM16mr7ZyRW4w1rtJHgwbRKOi2MW1r5UYzKf5iSjfdH8LtBkQW8UtORFSQ7AsY2xscIfwiYOydHTIl8vMgEmBsYblEZTVV9aN-8-dzDE-aCl9k4OpFFSOuS9SrZ7XFhPDcqB8LhBjlVwSZK9vGR-FLuQa0Wi9dmKpn820aLr-ZXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgDveMCsnu9oaZ-hqpPumqVjEVXmBoHvSXgip6Ro9LmV7fV6bGOJSKmNbNsm1mr0flTSB_SKgFTFaFClK9SRbGzjWsy5zJ2xAloL69AdTClC9zzHleKyQBmTAFaC8AwGNLmEZbl7iBWqqUqxnI6m3isZlHK464l3RuXFKNozgCwT8vpr4uHqnPyNdjsPf6Gv4q3wBOf0qUnKUFbQuBn3v7dsBOGsuGLPGu7DbWl5kp25c0grPT-rBhhUMI-40uEn_LOXoe0qThE_gr8X4UszKOnrRWK601mjSUv3L3h2Vyoh_ldUs_IWL9Y2d5J48nCy6C9W2leSFt_xpbHiI8qCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM73zCvRta__xd_Y-HGxaZI64X8q-idC2aCuo-H9kAWM5EqXFlRFifgOBL1xONTfif57vmng_C1lOYlZa06GBJn131z-vzh0CaAmPsPM5elGmVJ0WoVSd7zjmGnNOzhsGWsk5qdsx6NVZq4LGw7zEXB0DF6XY0A5Gt79_OOoKyWoNSCZthRG87zzrc5tyL29wXl7iwj5UZPlC0LAK9eWLC0PD_xmOoxpT-OOiySA-9STUfA6nXvE5ZX4P8MRjGTQVcqZzDJF84dGGp7pf778iZjLzbYixnoQCccxSCH-8L-1HvDlXiN3dHy2gjdjOCV-JOit8ct6GB2c_BDpK9ho7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrsGg0GD2xrr4xJGhdsSr4wqqm3xFz-rbJUSFzXQ8LCR8Neb59AItwwFMZ-HX6bZ5RGR-Hhz8WxP_prKF30KGWhtv3cAXJxW4B2WX1bgUZg9CD2NxnII9BmVUXhwdC7yETt2fP8Iom2hgrqdtke3p4Gdtn0tZrfLW07CrdI1r9b5XF6lqHy3scDd06ZVB7vP0e2vvlLODudroRZxcivG9O1V_tcf_Y8SmemUJvfGsd3M5SdBY-GHN4U5b9p2nI7AlzVb7k5HJ_Dt0VWIqvOP7dymDfLiUPWv_cclSNhfGDkYVSUkBnejEjc7ETSEEcKdt3hogzLeT22bi53dQ3US8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2fW9Ih_7AF1fy2L9R6dn1i17R-fbY7RMrtvVilrJktwyedrTLzMOPU81PX85pHZxsK9kvtR2_ZdcDAcbKV7kOQolfSTaPsI2PJ-b5g_Me-y_jd-0BhiqeHE_pEklitsFLgwT7mJKITAM4yLA358BawikTUOmdL_iM87mVeQWWrbipbRpMq1pAC88_upkYy-6_vcdymy71ZNsgnB5SkxbgSwB-28g48cb7adrpg12Sn3ASEBVjeBAzT1qj6lgqFrcGyC0Sl5RAD4rMndjdhQlOEiM2d-7u8uInhtbRPvzcrF5qHpttwtsorSiGcaefGvBhXpBdgVjvqvKPDKqTxlUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsX6YgaRyCSyhNWZmYFqfVPEYn0Qk7UM9PbbimyhgOak7JF3UQw6LVwgonnyYe7lGdqAzjQhdcFHxMIjsMkTZqXrXM0I6zb6EQXiaS7a5DU4-nJ-GJmDY-32UTZAPAWCJkE3DJzh8zE0QEfp5sl8Cms5Ahwk_uloF2UuI3086Cr6JT_TzWoMBrro3340n2MChral-x3tmRKPBqMh3MuD1D0Vcbaln-6UJapbmWzfsGmCTCBLV56KlS5DXE5Eq6WmEZ-ieuuBfw0vkqI_wO2KTzercxsrZvtApIz8ZYieA07LIRG4vXx2bgLkOdP2wMGLrczFBiQnjzLJbswAwxRMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLH4OQhePi2rb8Hm-3QkLdbXtZmwCgFX2UQbsgGaQRQ-xB6gFlM41qmaeom0CYMQbX7y_-7lrbte_whEKZTk1n1y1S3NnlV3vmJ8TvirlkFMEI_2YR0o9eUnOQd3AeHLdpYwagHta-iHDkxI5Ibe211JclhLMwmSuvz75TKYEdqFBTuguE84Jv8_EysFUo3rWR8-0YtRDMoPAV8hbXeTWR6N20u3T0DcnejGd21yLuQabAoif_sV1DsHLddNx-bJqy1GQr0Ix9X82gyFIQWsIsNGtGRdfuycrhWyg_git8dJNMoENwkSPZ31CsQ1567XNoEXS4eJOQkgOEc190cAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8AcZdAkWLWZ2h-WCUcW1L2jydAJhn4OOfvjGcDV1H3Y4Mfkg1ele7Pa0I5zX4MvsSZRiASAGVMBkdwFsm2vCv5WRAvMox_K6w7oN8MlP_coJybBeA1pRIRz5Y3VserGDQdzZk7azyCObUhs1Hl6_J8LH4vsI2zR666ORmrDV2uwdWJaNb8WTVedR1gveHkvoMJu-5tGM1QlVHuBGYGzeomOMbPpcgCYjcqMCEJNsQ7gmK9OshtBpEfdvFffRgDcOGSNymiaigqCyctgdD89vN9i0aE6AHcUdHlHz-MIwjreei3mn61mjPglgTOXuKmMUlTxYxA3SPtAO3lF5L7lQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtHTi9sXF6YsHipLEvTZPyuTBnWE_FzlKzIsehjZSEdLbxYjykIoHAqkY3I7SenXUEd7FtTAZfHAu_DT0eA75Nt9th1SMm9fp-HjNkfn8bvKJFi4dvXKCbTHArGakDN8EbFPqi1cTgxISUS36RNWLLbevGgy76sblVAfq3-qo-OsTwf-ANWiBlZgZlVh26VyTxHZMFdH8DIBWuRQmBUMMb5M8Dl2vZJDdbdLY9Vc9VRJW_Fd0z5waDRNtazeLwItdTfmXv1QFSA3q4XxqPHVJ1IXmy77n4aWJU6zfAVjTQM-BxNhUQOfLx1YpMnnXh6E4e7FcGpIbAKWG-SwZ1Tthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Dg08nVffFsMmMpYEeV02Pkyhb1kllZYcGxD6cX2gU-MP1KdPniE2F2hvsRbQGjrkKvudJTD_-WvfYVnoPMzNa5VwYNNZtgB4LZzjQZTIxyyf_7Zto_X3jfTTT1W6UFWT-xxarE8lqsR82sqnpaIUcp2czI9eVqi9DbnT3V6qGTUQ5qsNemjDdfoQjp5TgywMAE6VyBrxBlH6vQkP4Dz2tnZfoPGgsokODBuF7zagxA4TU9g7zmPNjBFLP-9PXS5EfkCoTskkrTwLTYbI_cG_6jck1ePNzwM4dX7HLENowwZMOzLHCdxHpHzItsPABAORAcNMKgyHHx1r0s5TICVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdZfJbUhyq73LFuZ8XT4gsSsL7_E5LrErzraCoHTOcoZbXf_np7kEnGorINFqIDntvW7BzjRhFNv_pYVhBFWtzqTZcEiopYK_xGQTJf67Mgd0u7a4hXlnBdnoZbt42uwWDjIoybMYOilMAuSJsPMQ1HbFYES7fLFmjexal0AHlLm3oHjEJnMeu7jFPzpt2lKDoQH1W8wtOC1rC1yO8baa77NZ-J5arIIaizqp9OoPTXD3vDOmjRwywxfR1a-OnYyiRaY3qCl-PJUUt8IMPUG4OUYft_28U_rXjOnDheSJf2_RVrCDuYKMAsLaHl14yMVAk57CW2jA_CPPqUIfLrhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpNB6TUu9YZuKR4kQr96RigUaQsGkQkYJtzH8ZcfkFrb6AphNgkXdoA5hfFOzumpw6XbuJG8j9NB8GlieQHEAuevl0g5XhNVqztMihXAkAZ_RQZzCYr5ONwZazbfserLayLsn6UDW4YATnUjjm1_leeSgzwU8b7IVuJLO1KQeRaRfl_Owwq6slkM8_31H_fXh_TpLLIBoFxGcs7ON45Mee6JhHYU6G_Onr3xYpRZbOnURwgqcxypIM3QM6zSjCL-UVMCZDxNtp4uO959npL9Kk12K6_xf-O-ZBy2fQs95No0sK2-iEIZoCbYcmHm5QDcWbrMpBwD9TkCzj0MZOArtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVdTqmXEKtOIDXYbwUdVynZmIBPkGzw54I4aclYi9eex1eaIKnWAm5dXFTZG6_EN-bLWHJ4A-pvZ2Mvp7CNoNHYtFr1LKPQVh7wH5a2PfBOdKUHu5mwansJU6zqyZWUF8dLxChdFUXXhSfLpGSt84tiYMU8F_yVEfzkRHANA0vd7g-ZwgGqNqioHrX9NcNUJw7dSA-JPc1EKAGrstE52Rp6XnRDNbTbFsJhjUxktYpWyiFgU4Uf3o2mIwr59As-n6cjJaQXY9VMmxnEXIbop08WuXH5CRyniA8nW9UPaEfpNYNStgxGOJUuF7T15P-n3_IoupAW3PktywwlrHeNjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGbVpAijObflGjA59Mn9HiNaS0bKpQTCZn8aghg4Warom-14JWIbvSmyMwAeoGudUUMvFQl9SUZTwh5tA1U8NAetk-OilAo50w30ek_JvFYuBk0nyUaid0LfMe9Evst5JGRIM5WXqTdxzYCmAOAxpjCe-WDvehotQ1VOcy9lN8bCkyFfBTYeUb8PtC2r3zJwvKiCE4VmXOCGUeqdU97HhZ1l5GNOVxa9NQHflBaTtPEc7tyS4kpgLRuaqHuCK5QbA7CGkMcWmGDASMLt7sgZlRDMaeapGoB4J4Hu1ynzuBiCVHnYh0QNsa3J0EyptlhDoxWygpQQlacOGlQSMw53vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw8VpFz8zmJr-2oZixIWyTKsYAiIY5UOtdGFmYVMq9kwMfrH1mZfsM4W__n4hHAZHRCy8tsRRuh0hfZEPZXCAH7Yf1J4diqy6cFbas9eGjbllNAr6zZ5qup3BCN8yHWdIvoZTY8JXwW42RwixY8YE_pDmR3gYiws1fv0kQ8Ola-tDAEFobjz1_bjoiOTmcQ92GpFOWa8qYrPp6LVj1XqDAVVvO50ZCm5kvy3ceXMGW8r2MYnc3AGR2AdajqL4aurGNht8dFy0L69XYa2sDD0t9IACKjnlqyk33CzPEgg5glYH6aTxXSieovBm9m3ktVet-a5g0QwvqnNnND6EFhZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHcXQr0iQrG4YwrlVP6CL6xATEaSkTWCKEM9GtULPyYTJqf5twICFZo58hVFilGZewdfTLJNA105odnjQDhZgMtWQmW6WUUZypmUjjxJlBMDK9fefMhsAi8B_W5HXhlELKItq556Hp5xywaACOXo7guZ_I4hsky7AFXBou3G3_CrnDl4AwCEU9AcVVOkQxL5ouAjuhe72QPQq68kD3nvcPkBD2uRGJ0L16l0EQXy-V_EWMAi_DHa9hJE8zS6zbyT_SkPCJDVi1IzMn_Hb_5dVXEGWYPdvoh26IR8B-f3nQycQLm2btt4SvTz9Mqw9nFxSvfepygjdhS1Ggp9vZSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJF4wfkDcSzNjgVDjO14rV9FnJWxuer413lyc6q3qehMCZav7Urs1HBG2nWY8nNW8iQ90stttfkAtWMgyC_LwLaq0GwAcD23BnGve-TPDrEe_0GpliQwYoSmgtoPL477UguIxrivUcLe96-IpI8oIVn5UWcKowDKRYQWDWEXU36cl7zNJbWRQ8VEUCCnliuD68qbkMg1A54VbeqcsuqtqaWaqdENKNTToXId_RbfvoSAUlL4E3I6VR4huPx0lx8pIAM6XgBffeSvOoBu_m8Zf9SVRs8hpmBFl7UPIoj1UaJOgPu8hKWUjqOD1BJudmt-qlSBMp44_P3aSBMEsWUltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeCpYkALsoMMfD2bKNLxrVAwWw-rp5lK6fw1wYYKzd_pfGgN48AQiOR5qURtdSH1gUJ-a4COd7lHnt_CEYC2Elz-EVd0rbaLcUOJJiEMoRZdAMAU6nb-gvKuoQS6481qs5fdR-xgHUjVvvbP8p-7rUv0ysY_UtYu6oKgBRBTV07pfcOMnLZBJ3QqrisHAx7wZBunygfEtOjO6q08aHS03moSyGkU6aCUnovceKK-5KCITqsXSl5oQGwG4LYVUgudNSfbuQAZ63-RQ1lqI2iZBTQQbE9ObSINc_9uC4RQH1qeZD8YCskT_VEbYTX14wYCjPa3ONMDQlDTn9xvj_gU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=ifJCRKvOIbx29jbxx--bR84b-lan57-ih-pYD9VqgTgmH6rB9KdUgWDAxlIAcmXzCKYf-07o-ZfJix4ER8-NIVj07CmCwxN2VkH489ad5LCCxVzNO33Gxh48DvAP3K1foQB8XZbe-G9mv3c6McKdwin4f0wpciKjLP0R4rKl9iheEVaDj8NbY6SspBMybHvTiQZ6Tf_iYV9nlXaSVokAlvf98g3Eecrb8x7OhOr4Qm0zzdqKp6op_YEgB79P6ktVtvaJDxZi-nPKsoF9gAn-eOoc_86QQWUtjXR14epmQPsudCzCroYpEW6gFEGtRxMIhCEyrw9rm4KOdzExdGVWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=ifJCRKvOIbx29jbxx--bR84b-lan57-ih-pYD9VqgTgmH6rB9KdUgWDAxlIAcmXzCKYf-07o-ZfJix4ER8-NIVj07CmCwxN2VkH489ad5LCCxVzNO33Gxh48DvAP3K1foQB8XZbe-G9mv3c6McKdwin4f0wpciKjLP0R4rKl9iheEVaDj8NbY6SspBMybHvTiQZ6Tf_iYV9nlXaSVokAlvf98g3Eecrb8x7OhOr4Qm0zzdqKp6op_YEgB79P6ktVtvaJDxZi-nPKsoF9gAn-eOoc_86QQWUtjXR14epmQPsudCzCroYpEW6gFEGtRxMIhCEyrw9rm4KOdzExdGVWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PveLc3I6aJGP4HV1UclZIKZoGmS2NA0QF0Y6Efs70qyF2DuYRYeD3ra044iXdbChws2DJODj_HnYwxb1_UcCM6-tLQ1ugB7n92tcKCcj_jNqK1iVonGs5oCzgJP1LOYJertAQmQF2bp6HPuSXYw4WoLllaA74-_0GPWpGDChBjfdXEMQ6-t2pJxDdMkgWmYS8E-peit60xY77Lb7qMxcGvPSYyPjLNUBIKs_eF9difACvih9RR2_MhJugCClEHnx6rSA6-Ky0rfjRMiJIt7K6f2KMdLAPc9XzRbC7hTEW3kpDfNM3npvcTGoEyG26-6TGhcE7KV3GwZxN1ACMNITbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psJrD-zTut9oYXyvgnDA3BZStl_cC6gMwtXszLmCM2NEx6mhro3ssRllO0R-VHQOJFBlcFldqTMrxS5FIQL81JrVvu9Xcr1ooBKXJZc_IbaDlhn8MWv5IOjXDsy0FvW5ke6UEn9P7AS2_N2r_hjo8__gd4rFVDfOVv2ib4a03ewzLZmTWwUtXeF0ySB_kLXrol2mt5QYwqEVNNX8Xl_d4_ZJAWsE0Ke1QEdvhdfbR7tZaoMWIRArFR9uALPTcZ2dhTotIJwc6-HfHXagfvCxxWGeu9yoj46cyZ_bO8fgux-_GkqbHE6w1aUPdQkGFoNI4009ThuxcS_MkMrqZaPuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0fShE1Wc0kcemlBmnsJKrRZFRzdxuJvDqqoroyVdWhxIj8HzC79K4xf0YSsenhCi9OOKjasCNEezG_mJHcUwmC5UAQWrOfFdQ_z14oOr0-YrmohXC33NjrVFxOECtTW_SQhOw1F1friW6dr4cSAhhi3jav7JHQ0sclOPb9Ae3Es-mMroMDII5JZIpB9rNJ8VAhmddc8EL_x-Hu6naOyBiwegXIKRnYdfnEku4dGrYvtNDkOs83_Hi4R9TPiwK8HjczWJ9sAYE79rHoLouy2cLnTCJwyT2onhHLsh9uf4SRY7gPuywB6MDbWWgH2T3PAdkCLYSWKzJzNc5LQHS33UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=ReJRiVzeD40rDtqGUnDu1VeROK5FaQjVjNvKi2iyNp09S651ae6T-rei0cfkAsN_AdoGVQLDkH0PqN9U12BOqWQz1sOCxY1Z0acyMMuexpkz5LRrE92g9zrnTuQ-0TpPEMLFXhDnPtNQ21uCVI_HYZ2K9BNvbsywMyLlJ-FC7DtulawQFkk5dgNmtXD2DDgFkEMNQa0o1wFN6S5YKStosEmb_saTk1x6_SMJpGE1os69WqzGMKQpLJkubGQtd-DBpzZ_9YPQcTG92lwYRZenPHpuuFBWcPpwlt8_zowGfoC5utmZj14BVy4YIj5oLeCuMEkFa78HwEds9I6EuKLhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=ReJRiVzeD40rDtqGUnDu1VeROK5FaQjVjNvKi2iyNp09S651ae6T-rei0cfkAsN_AdoGVQLDkH0PqN9U12BOqWQz1sOCxY1Z0acyMMuexpkz5LRrE92g9zrnTuQ-0TpPEMLFXhDnPtNQ21uCVI_HYZ2K9BNvbsywMyLlJ-FC7DtulawQFkk5dgNmtXD2DDgFkEMNQa0o1wFN6S5YKStosEmb_saTk1x6_SMJpGE1os69WqzGMKQpLJkubGQtd-DBpzZ_9YPQcTG92lwYRZenPHpuuFBWcPpwlt8_zowGfoC5utmZj14BVy4YIj5oLeCuMEkFa78HwEds9I6EuKLhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=hoco_lD1TQVrCnbUOo7BP7PGaFZrupApwZfZvJP7VUjnxDpsvBo3AaWU-aj1F7CzqS5ofB7nZrtw0KYvl4O7yNuLFrO07vAtd6xzMk5GB8kvRpRO2103ls188DqabHYg1yfBUuptTvAqkmf_zxZEVNFB7pgdS3dd8_R3Cgv4yssWBQkVFMhlCIYPceVPlIpeL5h5grw33qt2IodkTrV5vAnFCZHKFBUQUsOiUJl0ZdnJArwl5qId1O-q62R0jv9jWscpQLvMf_UQBm4BCqFP1j1X4jRjlk1uOazqF1_6Ol4MgBmElkpzrBEseAJzCtqzz83CTpqPv9vAs_fk_Lyh2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=hoco_lD1TQVrCnbUOo7BP7PGaFZrupApwZfZvJP7VUjnxDpsvBo3AaWU-aj1F7CzqS5ofB7nZrtw0KYvl4O7yNuLFrO07vAtd6xzMk5GB8kvRpRO2103ls188DqabHYg1yfBUuptTvAqkmf_zxZEVNFB7pgdS3dd8_R3Cgv4yssWBQkVFMhlCIYPceVPlIpeL5h5grw33qt2IodkTrV5vAnFCZHKFBUQUsOiUJl0ZdnJArwl5qId1O-q62R0jv9jWscpQLvMf_UQBm4BCqFP1j1X4jRjlk1uOazqF1_6Ol4MgBmElkpzrBEseAJzCtqzz83CTpqPv9vAs_fk_Lyh2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=jYt4Vh2oRGpCnQWrrz1HS9rMIedejdWlnjQ07OPVN6IKLRhJFGdo184bBchKZ2V5DnDIlC2VXzIdH60dp71Kf5zQWzktGGe_sH_lr9m0TtBjIolMWBTbuOPLLK490WMRxvSUxDys6lJE7_jxyDQTH7u0zA8jbFqNcdREuL40cXwtkdtfUHe3ZdBhQyLoJG5S2kKV5_LcKi5bUGWFEUUh2QUfH8IP4kbzQIy6J-OzngmYFG1uzN-2-WFkR5tot3MrP1Nglepe3TrpH-q1H0jZE9h8c634QmLIEjXmhMcpRddfaQY51oeXmrE1Dw9-fKzG2Xq0Y3gglSd794NrnaIGdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=jYt4Vh2oRGpCnQWrrz1HS9rMIedejdWlnjQ07OPVN6IKLRhJFGdo184bBchKZ2V5DnDIlC2VXzIdH60dp71Kf5zQWzktGGe_sH_lr9m0TtBjIolMWBTbuOPLLK490WMRxvSUxDys6lJE7_jxyDQTH7u0zA8jbFqNcdREuL40cXwtkdtfUHe3ZdBhQyLoJG5S2kKV5_LcKi5bUGWFEUUh2QUfH8IP4kbzQIy6J-OzngmYFG1uzN-2-WFkR5tot3MrP1Nglepe3TrpH-q1H0jZE9h8c634QmLIEjXmhMcpRddfaQY51oeXmrE1Dw9-fKzG2Xq0Y3gglSd794NrnaIGdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ39DfB2xMqyipO7LZESg_-iQW4On52gr-v0Y-HVFOnh5mMvbFwVIl8x6DYsoLr8-G7uj51dXSic1QLF1wV5pNLVBSCqM_eGir6alvrKwDfqtqBa1vASriJc1XM2STLsVpvdvrdZqApL862hzcnJkldtNwzUcya0Hz9Rj9tjlDPzcM7Eev_hlBHkRCopRMs9Ep2v92a6KNGFINgBF41wmrPbXYhYXmYAxWsC3m85eDFCEDPr0ngmjp_1IXHc_vN-yNy7WrfGQK9ESOiXfSU3J1n-a0CG5SSpVCQJdOAmKQhHw8dG09qDrVAE861l-rEwHpdI7qt5OGzFTR-N5dXDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQa2LC3GWWkoY1NpgUyd-XHksZbZq4y6p6ExB9h6QxQPCLq10stkcQNLjWEiMSt3rCWUWCF3bPfwDmjc9MgQQZ_JCQNP4nHXPz3GBaa9xcsZfaHJPpt2PKrMzDbrprXJ2FETtx-_UUDcNCZwmAoixPvWH5ijOoIOV_Swl2np00dJVLlDct3O8xUFQlkXAuZqslFdDcB79rFlFB0YBYOcOAn_4EbWOjWzSJB-AsZiUF5XfEJNFThOSFqWptaPKTkTpz5R6cwCieYbnq-uSP4dZpRSq3Em_AlDh19HMZ5EpawT7haYWBd6UmLwKpnsTp1zIdtewOQEIq501hWm_gjGjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyztu8rxUqxYpXDq234wzqK52uENZwei4bp1CXiQhuDNEqxgvRAVWAlkysZ2SEXEAo7rEG0g3vAN2ojR7oB75uJKSEa3N9ZM1qsWG2rv2C6Gr4W7DpFMwZDQg0XNf4hSoWuNRkIctmN_wO-RPJeFXp0i2e-dqyq9TlvZiOo-RUmata1poh-ZbKDDrI_y7TiSkfZttmZlqU5YJrA4ryiXHsiYlYqdM-UR43EOdrGHHAJa8NeOoXjczvU2Gua2tXZ0IcwMirjz-7GEwp8ZAXL_bHUZaKzTCVFK1500w6tek67kKYGNSEJtz0vTuQpXbBQ1slf6LSC4LyPCBtYPG3jpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hok88dw_vW_fOVRMBgrcxjlX_VL4QGwlQNABxPcGpup3K0hK3tQuJBMPGVbF49DiVYEt16Nk4uHKtQJWstIVezw61Q4VUgyKtwiglS_jgJ4oAnhqLIMJvKZh5s2zZVYSLMz1zhNXTfkqAqeK-DVEhX7S9NboBv88UHRPQQTyXFuLEQc_HIopnCYt0eCSF9A_kVCquhl-kZGj3m5UWTXqR8mQiq_D6fyorSdsSBwth2G0sByB56NVhOrTPMr6MSWk6yTfRzyGKKTpUZ6_4StvxXk959NY1jWRA3YLM9Kj_bw9BfBfshLdEwVk9_VHVEmBomzNVoECWqSrDt0wTFE_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویو توییت جنجالی وینیسیوس جونیور در سال 2024 به 490 میلیون رسید؛ وینی بعد از اینکه اون سال توپ طلا رو به رودری دادند یه‌توییت‌زد و گفت برای به دست توپ طلا 10 برابر اون سال که با رئال مادرید قهرمان لیگ قهرمانان اروپا شد تلاش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29464" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_au6chdIsEmd3nH7Pzt7kHIOVrUclx9uJ9wUeHc_dNDon1QHaAai-qtk5bXrV52quAFwdJK9ppMd-DDKINBsifpBv5m4jGjXwZ7IWdexn9sHVYhO7bk6RNup_VtuV9v_RdaOZDRdqHXL_Nm5h3-o4gNC5ortnUoqx7BCt5lIXjvks8MLYnPKfl73oOnudia3PctYXFgJYVGdml5QTL4qYmc1KhZI73oaAfRXctm3p2m2mmUo7yNWJw0FOwZ_cZjHfXT0xz8VpO12MFdAdbJZ-gixTDbKJsu4cCfSx087nrVTX2hioxuXdVA5Qb5OmR6COiFwm73VQWY5VzJfv3psQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های تیم ملی فوتبال ساحلی ایران در جام‌ملت‌های‌آسیا؛ مسابقات از 28 آبان شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29463" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ScsXota6Phno7a--HydhaT1Cqo5aOyiwPRVXylCpUH-ULUIrmBzbo_tWBEXrBKH_UD6vTgpv6Zrz29A4VF7SQ9BhDOswuCsO6Q_U_yHfx9eDhyyxkiseYPVD_zUitfSPy4W783EqqdaOm1uXD4shBYE2GHH394QL6CpPlnB7KjpSnHpiw33hsTPU9Pwq2gXKEvDXI2iPiBAga2uafmX4ZJvmG9aHsxuFytYaJ0NIwlt4guMKDHXxg_72pL4Ru3AJhLCrIg2rAT4y2yC-euB6m1gxN77AjB9S9erhkddxKvhEBiwTgYE3l1ez6NGZ-CdNfDZmq5y1AhUETBsmqaSTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ScsXota6Phno7a--HydhaT1Cqo5aOyiwPRVXylCpUH-ULUIrmBzbo_tWBEXrBKH_UD6vTgpv6Zrz29A4VF7SQ9BhDOswuCsO6Q_U_yHfx9eDhyyxkiseYPVD_zUitfSPy4W783EqqdaOm1uXD4shBYE2GHH394QL6CpPlnB7KjpSnHpiw33hsTPU9Pwq2gXKEvDXI2iPiBAga2uafmX4ZJvmG9aHsxuFytYaJ0NIwlt4guMKDHXxg_72pL4Ru3AJhLCrIg2rAT4y2yC-euB6m1gxN77AjB9S9erhkddxKvhEBiwTgYE3l1ez6NGZ-CdNfDZmq5y1AhUETBsmqaSTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
پاس تونی کروسی هافبک مس به امیر روستایی که این بازیکن قدر این پاس برگ ریزون رو ندونست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29462" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=tGs_jd-fHxO3Gx3l43U0ah-Pk-E40-8j2hL_5qyUzFNmnalmzMvdUXfSCb46TUoV3M_GoDdGU4ubjC6FqJWE2eqNGf2pjpq5zTK7UKIgj-MWaFntNbsxHA1jse76B-QkxWXDrHQz3UqlPC_jUrJDs0ZkLYa2FO5G9Y9Zm5odvrsQOrF-dkTYebV37HAsvelzYDc8gmafKqywAKWyZxUGtvBjvJ97phTE4gfmB57U6N2iNEZ6lGb40RIP0KODp27TCcTxjFhHosSjJHLw7hNBIBnT29f80WK19dGKjbZy_FQ1m6qBNqEEdO6xaeco3eT6avvHnOZLC-g6gJebSoFmyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=tGs_jd-fHxO3Gx3l43U0ah-Pk-E40-8j2hL_5qyUzFNmnalmzMvdUXfSCb46TUoV3M_GoDdGU4ubjC6FqJWE2eqNGf2pjpq5zTK7UKIgj-MWaFntNbsxHA1jse76B-QkxWXDrHQz3UqlPC_jUrJDs0ZkLYa2FO5G9Y9Zm5odvrsQOrF-dkTYebV37HAsvelzYDc8gmafKqywAKWyZxUGtvBjvJ97phTE4gfmB57U6N2iNEZ6lGb40RIP0KODp27TCcTxjFhHosSjJHLw7hNBIBnT29f80WK19dGKjbZy_FQ1m6qBNqEEdO6xaeco3eT6avvHnOZLC-g6gJebSoFmyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصر پاییزی چهارشنبه از مدرسه برمی‌گردی و تلویزیون رو باز می‌کنی و این شاهکار رو می‌شنوی. یادش بخیر واقعا اون روزها همه چی بهتر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29461" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=qsN0_G2o-u2YrqASlYX7ZIhqoA6Ig7u3LyXZs4nzuuaCzjVa3-BHDSDz8aukCtG1KvndpRNdRXoOQ8pqbrjT9DEiuPEgiVPDRcLJPoBE96qIll7hET5Upn8hfL9BKDkYDR_go_0qFEm4L0KqQ9xrMa-Vjuc-AjPTndPfvT-zmeSARvAR6t7fm0jSn8Pu7A4NbT33V8IknqZ1Mr-1Zc6lf_3CFUHXN6K9dMKu921lDd8YC5XlICp4KqmWgu2tmO3lTQrIGteMuiiYZP1fyzgXdV3Bff92Jkry5C6O_Izq5ru6wrkONWWHhTm5pmgFTjy755H0rS9cl931nzDLLyYSyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=qsN0_G2o-u2YrqASlYX7ZIhqoA6Ig7u3LyXZs4nzuuaCzjVa3-BHDSDz8aukCtG1KvndpRNdRXoOQ8pqbrjT9DEiuPEgiVPDRcLJPoBE96qIll7hET5Upn8hfL9BKDkYDR_go_0qFEm4L0KqQ9xrMa-Vjuc-AjPTndPfvT-zmeSARvAR6t7fm0jSn8Pu7A4NbT33V8IknqZ1Mr-1Zc6lf_3CFUHXN6K9dMKu921lDd8YC5XlICp4KqmWgu2tmO3lTQrIGteMuiiYZP1fyzgXdV3Bff92Jkry5C6O_Izq5ru6wrkONWWHhTm5pmgFTjy755H0rS9cl931nzDLLyYSyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=EhGbPW0jSGJ-eQ-LJVdkLXcsFBPQOcbili0ngnDoKFHI8yh-dvqr5C57rb4Ap-L91ZYFb_BEWi2TabiezF062asgDVuTU6gU1G92IxolNtdRIv7-HYe2zY3PcnMn_u1lO8X0ByZp9dNJ_O_Szpr_WlnndLQzJ4w2gbNE8CKCmXyp1mOA7eBbkinCcOFhloSkoeGbfGgDahCwSdqRts5W7lpMD55KYUDD0qc6YjPxInu0O7Ds8rNnNxb8wVLQy7SXQ3i-PQfoBEl0RYVvsEyEdVlxulPVMGsGJP5QDrR3TxMzYNO1jSR30T18ArLMU3BPR6uIvCgu49A828mzO_hQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=EhGbPW0jSGJ-eQ-LJVdkLXcsFBPQOcbili0ngnDoKFHI8yh-dvqr5C57rb4Ap-L91ZYFb_BEWi2TabiezF062asgDVuTU6gU1G92IxolNtdRIv7-HYe2zY3PcnMn_u1lO8X0ByZp9dNJ_O_Szpr_WlnndLQzJ4w2gbNE8CKCmXyp1mOA7eBbkinCcOFhloSkoeGbfGgDahCwSdqRts5W7lpMD55KYUDD0qc6YjPxInu0O7Ds8rNnNxb8wVLQy7SXQ3i-PQfoBEl0RYVvsEyEdVlxulPVMGsGJP5QDrR3TxMzYNO1jSR30T18ArLMU3BPR6uIvCgu49A828mzO_hQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=jv-6QQqgAJkx3nGMCv1GbfY5Ep9jQJoGqbx1wO5vSVwNmSyP339AIojpxeZ7LeARpzknb4_3R_nNI95Lvufs23YMM_I1Nx1z4TP5UaF6i4lkrxnuk7v_P4TZPMbytmXsN3vAuQqSWAEWd53lKZUK5Z1ClmmrJ5I5719opJbL1GTvOJrZ26VxM_mjYts-28V1kCKTCa3nteoXdC-pFIAOoRtQ15uCNZKQbjoFpW1AFYsOSGxXFxFN7CAhE4DqsUQfBGYJCbj5gIngmun8BroT4Eg9-GtH3xbzqXjOKFFIeNRx4ka7UyFCKVEPkmCcuJV4yzg-Dds1nMXQetvY5auRmHk-IFeRXC0cFiwV_mD9vWSmT_lUs8DJs9_svoFxTd8wlZdpMGvQRMHTz_ICxMXfXk0Z2lNP7GwA5RXg2IBiY4KGNTSP7DsJwRR4rUZv3Bf0arr4V7xlsxOeWg20V2mr_rNInwjGcISxVBilHoD-JUsFz8bTDFkiAX5kML-LEkjHj-3MtHufebXMlORD85zVTB2uOPJdV-hBmMw4Bf70kLgoddxK4tSevt1uza7ylr4CkyMR25zr1wYMznZT6YH9Jrph5bGP6DdD45EkIKzemsVem-9oMPn0Duw1ttCRPKnMX46TUBRaIAD5xFarSmBhWk4qAbI8_IU1597TE1ObKb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=jv-6QQqgAJkx3nGMCv1GbfY5Ep9jQJoGqbx1wO5vSVwNmSyP339AIojpxeZ7LeARpzknb4_3R_nNI95Lvufs23YMM_I1Nx1z4TP5UaF6i4lkrxnuk7v_P4TZPMbytmXsN3vAuQqSWAEWd53lKZUK5Z1ClmmrJ5I5719opJbL1GTvOJrZ26VxM_mjYts-28V1kCKTCa3nteoXdC-pFIAOoRtQ15uCNZKQbjoFpW1AFYsOSGxXFxFN7CAhE4DqsUQfBGYJCbj5gIngmun8BroT4Eg9-GtH3xbzqXjOKFFIeNRx4ka7UyFCKVEPkmCcuJV4yzg-Dds1nMXQetvY5auRmHk-IFeRXC0cFiwV_mD9vWSmT_lUs8DJs9_svoFxTd8wlZdpMGvQRMHTz_ICxMXfXk0Z2lNP7GwA5RXg2IBiY4KGNTSP7DsJwRR4rUZv3Bf0arr4V7xlsxOeWg20V2mr_rNInwjGcISxVBilHoD-JUsFz8bTDFkiAX5kML-LEkjHj-3MtHufebXMlORD85zVTB2uOPJdV-hBmMw4Bf70kLgoddxK4tSevt1uza7ylr4CkyMR25zr1wYMznZT6YH9Jrph5bGP6DdD45EkIKzemsVem-9oMPn0Duw1ttCRPKnMX46TUBRaIAD5xFarSmBhWk4qAbI8_IU1597TE1ObKb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbFr3Lq7ZUjM_ydeh4IcdxU8QXub7JCRiW8zefv5uOkJEhJToKAjLXGpiQUS5WTHKsHQZF-Kz7tOwbd1WE6xbyyWmC8NNyqTxZeHiSWhBwj7l0l-LiGNNjOcd2hrdReqfpcMuVOo_DcPXZj-bDp11efYc_7BK5iXSEaIndimO3lxyJCxEeFxKw9hS1V8VP8xFbfROrp3SZtBHtxQA7DPp1j4jbTJWBVQRJYdYAfubbao-4slpMScDQYKgBec74giOHav3K_443Cde_zvC_Bh1gPoKEBiCftjjmdGgm9myDVGXsyaEpnLEFJ9VphERcDFmoORFm6unIZwbl2GemNwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz49QC7erWh13N4-z2H_jN7RBi_sm02ZGJyjUPkmLqX4apmSEAgDXFBG1xClxBgBiN7sgd7Ac_XtMh9Id0jIf6xT7f2w6d9CyoUXchLuNa8cWuNA_-_MjMFaJ-NyncFqOlSlwHlPX18zpfCDgc_xdGyUHI-bT5X7UcHzdg8v2KVscRNnGIN8ne5xN2Ljrn1V9hGD23vbnuivw1RwxFTX7tPNMaNcWnasDwbu_F_doz2gvJBybHgCea_Wvf35wOABU7PhRtRqoiniIyv_I947alT3Fu2lKgEXsxSgQNlAthxZ3YCjuDKFWmlZfJ1RaN_dEaG67M7ADjocsU8E1rL4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSjW2RgPVGKQv2UuCX5A4LC4n-6cPG40tpiSs71g0yHfscbKX7SRj59uCoH9GrPBDqiNVMTK6oxIV6ssIos9_hXPTDbkagmcjHLwv71s2Xy17q8DTgQM1iS0BpBOLCSnPlLaoKavhBcxN9yUcOn_wJX267zz14JuBeQmvtHjEtbwB5AUr1fj1Y8MA3ERaO43FcaSq9zF2MbEQhC9OPeeN0wKN-JybJMHNBqPh9Lezj_usrNXQAd3SPREqqqPfRNj2WzbNIo_JptqLpEpaYb9dmyuHje7xnPfRZQWUP9mcM0XBze1xFsw_LsWKlBwIgn4tfu6Dm_-eJgju3a1Ncg9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BApJsNbLI9OqkCMpv4rjqa7prd8N6uIQUj-mULp07MoS0X3aVlhevok3GGnKIB2htxHBUT3oXJCmSlvZ4BzQyskHJhg8Da5xrXDknl4Qq-9iP8YPor_vIWVSvxYUQp9DGu7tgZwjVO-fKb6LB1XWWQ1ItpAb342xy4YReuIKCJHao-djiyteNWIASgZOv4T7YRUcecLPAXuiU8wtvBamoM53Bm9eK0UAr63PpFpck9dZ0zdpulcEhcfp--3xdi069ASziyj2AnzS-aAIX37HSBAYO4ZE5WAWFLDJrk-CQZMczXZgMcEG8SWM0cLcelcaHhHgFJVPoKN2WI2Niq3j1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaqdFJ-l-7Uk4Vvu4zabS9Wl-KWea8zwwxpLxSU4glNCuAkuLWW3hTDMYc8G0pV6eoiyaElU-kmQzrD94RXSPCxEX7W3yD5Yxxznw3cV79Jquq3zGkOOpyoRJ-XE-qMuxDQTd_BK6KyOxO70QVs4fElMUnYylGQehFDZw7QDCpajZpRSqPzhJVMuAo6eNNECnaWlPZEMBG0LVZu3-svBwa6Rbe4f008Lb7tVVejbhL8rqwnsho5fuN_k998xokMjk5vvUKVr35j9T4os6E-W5U4bbYtmcLiPoqSL2QyI30U5pURR9bmbRhuaSFaPGlJ0VBnQpNAQ43UGgA9rs-s5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIay2Xn8MCnMtaLXr-TrjuMGkUbbg6pOVazzrLECqARkP8wYRMXW1Gjf4c8yJvWDMFmQHiYEj_ek-rKkpBSC2pjBYBT_bmraKXEm3p-UNghSr0pVSqEqBUZl-eyjoX4xlVGbhLo42a_huodBqqVyzzYygob93aHZQwBP3DD59fmcqVedP1BtRUKxFCS3mGOOyfcImLelCpinIh3mp5E3IwUyAS6WDHJIOE97RTovREbY6pFpkSAcX_9WX1Oi13aC4pMP0cOazYMjkZkxZ-7YCmTglioHDtk67CJssA0CPtY4L0lh2LZ116jSMo_OaW2D4E3p1CVsriMr8HWXxLBGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv1JNFGQnIZaX3RNvP_GpdPPi41ouTmcbTKFwpe8O_BEWqAazqoTPC1b_OarKhfnSncqFi3yOnco5VbwZrSbRvyo73kpRZn50ml5fpfFgGst-NI_8q1Sriz0KMii_5PcYb77VBNkHxlK5a3mfGUy4tK6YiaGJFz-sbnQ7E5COEhu7P9bE5VkyiogYMtYTzKLui8AwNzbfP0C37P6LeRTV3Awtu80X95eD2V4kYjHHwuMkq72KACo4JAGs9Y9XjNVKYTcTPdOoGIEqTNALZpxXjgTJRO2d5WbYp3VEvfLWUVf4SDHoVGdwoG2gX_dXbs4mphhs5gWlbHJuqzkAY4NQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=q7IlYMkete_1nM15DPPT5RgRSI12HAQSUr0JUkJlrWb6PHAj-ld9-Iicv7OTfFRoF6qVJEDJnyG4Nkp_BkSMiBKI8JeZeVsKgyawYpv0SfUkFXBDN-lHnATCcS2U997AHZqHDWHwwYwyHF96SEXYZ_rBcfNPNVZjwnsynFPxsOaAKjCxvo1g-pqzwO47rx8-akUDQsdhcyQpJknhGGFBjKJft6vJ2AMSNyNfQIAZV9DTrFcYvT0C7wE7dNKBVTJC-nr74wjG66NosArPlEhW_hEQrQKGyMYMN3GeH1f1y1wiytcwaeNUjosvKLRXklhjNNPI-ss2OKZwWZSPkWB3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=q7IlYMkete_1nM15DPPT5RgRSI12HAQSUr0JUkJlrWb6PHAj-ld9-Iicv7OTfFRoF6qVJEDJnyG4Nkp_BkSMiBKI8JeZeVsKgyawYpv0SfUkFXBDN-lHnATCcS2U997AHZqHDWHwwYwyHF96SEXYZ_rBcfNPNVZjwnsynFPxsOaAKjCxvo1g-pqzwO47rx8-akUDQsdhcyQpJknhGGFBjKJft6vJ2AMSNyNfQIAZV9DTrFcYvT0C7wE7dNKBVTJC-nr74wjG66NosArPlEhW_hEQrQKGyMYMN3GeH1f1y1wiytcwaeNUjosvKLRXklhjNNPI-ss2OKZwWZSPkWB3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwrO7ZOZYnPVpSTkCCkT_gGPpdKqzxgZII5nEjdMZanVE2J8kYYgMVRbRO9gFaaWsG3zYGPnXSIgLZMW4vmXOBKTY8IVWExTnG--eFbwsMnyTA8gM8VjuqktYbFz04_NsNzLzpCqiGnDKmWJ6X5brbHAVQz4SAhiuapCZF4BLzMKM5toVgk9Lmy845ARS3b1yVt7XbUPwulfE3UMuof2Ww9GJrcSZdxUuQYEYAgtzDRkERc10t67jlwijIMCbke--5E0nNR4UiN_pP3EeodpVhQVYNsdvqtybiWeej7mop1DfCnkAdCHBViRJBzyjygd24VHvlNWNSPnmTuJ1KE4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
