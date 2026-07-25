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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 578K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 15:26:42</div>
<hr>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTgbXyh4McUZxwdUtiV1erqQTVGDgM8BK07xBDhJ_kZWmwKhia5mt3lfMHhItXU7c1jcz-SICBtI3kUHv-FTQ-7t_nA5GmCVi8JaBMF0fuwnk20YlLlUdOnBH85Q-d6g1lR7itftdZX0SNqo3ITj239g3ywca8y5xoZSdcR3qu1YlwyIhvg-mMIMDd-bEFrJADNOBV-oBKLJwTjlbG2VwCLbSKEl-xRCsfNAtUy7x0FXoBvNNu1GMoccP1J0mflt1HjRb9PF-lGhiOjY_2iZjLTaWq_bZB_bj8yAtXf6Cau6DJDG3drY_D5CX3mlxtDMy7sGU0eG1mNZkWo9jG4aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUYfEkWxnUQHGMD04LFPT8jOyn6n5Hk7solEEoaHOE_4PzpNMOKQ6fakciqHmvNTGSOrgLAgLyi9HFPEnDYMK-3PpgKle4OlvTG30FU0XwTE8TCGHqip4FMI_BYxdj_189rk8TToWskJQAR9QAyWC_F5OHUgDLe4c4hxWxqs88XP2maWjejoebE4xRtwMKXXZJPGS-nB7_G_r3HAgzmRBHO3tt4HdUJQQ59KbUR1BRd34AYz-Nvo04Wr6mz6LmAYfBvzsfXH7Js2JwV8ytJnWPo3cgFfGz1n6C_jBRL3wBtkyqTt5L0X-0YDA9yNobM-1D4m_RO0-JHh4EVd9yB4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrlnVviZUO5-hDgEniXVnLwSoeT2GiL7x9KhN9bnY5SXs1FaXYsk4smpqQmRIE1YfqAsEh5NdGEI_0RIOTytTqBUwdEgbLfRtg2_4U3vyXLVkA3jI8Fe7a0aXNrmOPU0JfAEHiQcFPUgxVlE39rGFL11wGiLyk5Zo45UeedAHfPHRshD3qq-2wLrDAWi-zm-6CHPeci9emvQS0HSF-qqRRfQqooehx88G_OTS3sVUonl2u_XouO4GWHGtVOZkre_lLPfkaLYiXhllR1UqwpHUQfuIaNOiRrLtQyxvJM7OCimLqHHR-M1q8jQWeT5D-V4PCFdSylGIozJYUi1dakERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUYEmSfCaVfShvj7MY4lzM3MNMlhNawqrHMYq852nAChqa5_AGT-LTin22OXYCA_lczTaruOcZzWIHnIjZpqSuHeRADS85BJJZJYMgNepBRv37GgmM0Cy_J53BcScznmA1yYyxy4WCDG46fJwIhNFwL190NFeEifLDEYwy6aUMr3Lu4pqJiMUa0dRreOQX4-k5F2TrvjZDRFe2i3mNyv2LJZHZ087_9vHVgjiUJ7r-cYwbJQIJhYIPuE2n77ZPj3lwYOX77Xmu1Jyi5O3-mBlvGWnN8ToLfn-YSqvbKwxU4bQsePlcNecyu4JFEAqW20dkgDTc5gGBWieJLMXLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzwrVS5N1D0zkmqsFYaCT1kCdo1-yDMPX9PBpYs2YllicPT4otye9aWm8yComBYLpvscvFhm9Ng3pgjfFVPK3CWTVoEPNdaGN9RrVtteWCZC7sRC_H1Zc4sogyiPBVIhMh_2HTdxKT-FUx8kB-TVqCIL9MPHQ7J-LJ2CeKOlJ8VK1bTzrhar1D5DiPOWqgMu0-m0NbhCYXcWYlu5-RP5xZYZRd0JfdSt2j_m1XYZqhJJXZCU7r--zx4IvTYNWN_jy1Oe6ADMtfQwruZy7w47kp7MYF5qezLXPzIM16hZLON69MuIuCkWUuMv6V9Dbb9W0QnWsWstiwKRqDVuwlUQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIudNl8W9BqEaVz9ho9w62MBe4hIDS4umtz3IvOJ7a9Cwe4d6DCCv5ffiiNPYubJm8l5LSib0cWgl8G-ZfVVweKf85IhrnpX1yw4B9OvwLA5JNQqBC5fhCOfdt4s3mu-HoHeRQva5gv2P3hmOmGd9jB21TQ-pmk6GudXA9NcfIbsnIafmHWAtGC3of6QCBVsI6-CxluT9GXQB9Lz7bTWXAR91-YCo2UZFtU8ho744SE1tgkrAg-kxxf7tuXQB2qreX1ErTvUCewqVDGlXOUZfHPsiUFFF6_2uE86DoGy866Kh4chaNOC3w5uquC_Po0qsM3AwEMciR-4D1jUnF74ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQ-b2P8x_sm_wp-etQcdMJuPH6o49YVvh2wcQpSTtu7PygTBm3YtZ5fGZNyxMXI23o1Z4nKqsZoyg7lPP33XXr6GuXQ3TJ6JgR-5rARrmxXy6J2AlvDy6o4yAGg_p0s_gT3yOTvk166MmfKtz5n2vWs7sVR9y6YPVBU9RAwJI9Nc4z0WXwUP8aVUv5Zwg7V3K_hNe2UxNRg7dyKVzNzAox_RWuYhLkWVKGMrjhzjyDINg5AdR3s5tAw3y_mJACtBB1WQ88FVEM5Ys2s1W3Twe6aLyjiHKuzKP2ILyBz7Ln6FNo-9BOhI1P_e2aJTu9xyoq_aHmnmKYcb3alQtUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnPZsOixQe1vgqMH1-dv2moHeQjDB1Sh1yIoKvf9Z05leal180sVW7D5FQWpJUHkcwfzTWBMnW7o7A2jCVIFtbCFI5yQ-DlwIcMl8wqndkMrnNoLytQQA8EKIqJ1w_wxUBvI7pcWXkjNqF8V2f4hicZAgS8ANkDXSP0MZgqYQq6PDdJgYzBvOkqpBBTrOfT7dzViaK78u466uLIxHfKg80HmPqctiM2bUSLnpIlTHnbo4kR2P5fCCYw0f7hQ_Yo_h4GoMzfIHPUiWc2Qhiz5LhcD64CKxb4eWSoAjrAwdbIenjvXS8klWnpXAjBJkDQgm3-gVznssnrv-AfvNV15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8YNcZOhsfs9aYlvmAzjEvhJX2xLrXmTkfGS35MvJQbetYu9DBFhWBbzVUaMtx6pEJHOoEZ0EHdi5j7ajbe7QTYoC5hhSIyKRv_iY2gUvaPsi_dRemOtPJ4Sg6yVEniMLvVWwcfhDaqNYkHdPon94wLfO-vUnYcvb1_uyJLAPp1JRXujc9duiWao3jVcSIqn9gsfZ3lGwcmVDUqs_kT3STy3hKlie3Fk2CWVlkcaWD5BK5O7_ygaKZCWB93A5quaLUoSBk6CSr6sCuvzsDYCh5q6LdoNhYiNEDv_vs-F2m0WTGHh-wyvn7E1TAy1_Yn-xzOSMcgayQLwywcuGoUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cWZ3aNvKTovdK5wlJEtcUFMnFti411znMhfubyNZ0rmv5KltvMUj7AZ2Pomn8ziYfO47amy664yeClYtRNZ7jVzEu-vPmZ3bhhsD5PcCS5IOSfkjSgA9N8We6nuJ-IuXg1N61bmEZOtdESyh869RQSdi3EIDc_HdYh0Wc6bB2GoKTjt-hihZZxzbvc-gHj3rcn84Kmr1rzcyrnpEEn-dLYXi1m_8WudHYq1qA0uvN-SOSNsbzYYLIbpMcWxFrOeMulfG6LoBhD46iC2KZgSbiZN24UqYvb323f5CFHR3_7cB346wZoCJEJXKqbbA7ECt4g2WAyJXrGBl1g667Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhu32fQUsqr3aaTbqNhoxlZTBfE1NEh4i23a5uec7YFls1k_rpaSGAhrOsDiMzwkOBUcGS9m-gDG34zKBUE9cFXWRGjqjlExwBH0ChnCtHZDrsq2ljbWWTJQ7Gy7FlzHv7wpG52gbBrbPZEX2bl7UQhKPMeEwO-YvTeIXISORO6nyy8gSW2FOwxBm_1yK5XKAWCCm8N6U8m841h1eTVN3VOlqf-Xvk00DAbStpO5iyaBbip6T5CaVg7LJQUWbjFnX2dP97LW5-34gdm_L0cBo_pNdnpewcj0iqa_l0UWAjc5ypu-lcckdDv64I5wFNFv2MlXuQju4euS5QqhUwrQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwn37v3DdiJDyOkrVEzE7DZE9vGhIUi4kHMUgOIHA11nTAf2VpuBzdvo5T0Mu4Wj2JZwUcl0W4UTSYWqGwhvMRmYhOtLOUUMg81NIXAQwh9BwOpJMxmtZRYAqnaz0NMxNw2v0fzCw_YG4Of83-xCPoGmula7_ZKT50YJxP2R2Qv04E_I54yEuY1FmQFaCvJRBuiB_g1m28Aq2KfnsLlYcOECiGC6YjWJwnh3SZy6AHmXP2Dm9qzmU_VJ94ABAnBRJVRaEv8QjVMEznUNokwq8iDdY3Q3zeAYoecKEDbarQi8o8O4WBPreoi5tWpsb5b8fwRfhgV1hjQb3sDw3nFtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe2lWaQ_JE_LuZKxw3SCFSg6-lNNG72W6Lxx7jF8jsGXA-JkxiLC_vegZaEsn0UfTbQ2AqxKO8VKs0tsy4S91lNcLEppagjEdCDx9gE-eOFVooAijNVDgPtG44u_KAI23ATDzLVAVJTBHVpXWr33h_Ezdrhn2PFRMMXt7vN-5p5VorbpTN7t4glVKKIEzXwOBJWRDzJWxxhjDoCev-Z2nr9IcwqouXCvL_NhQ73S0z_E2aLXWy0qKekuIsbuD3BW5Go8Uiisjn2Mc8a6XyIl_9ypJZozPdsiXWgB49qWtys3JenGlrTPrRBnhjYNrvXdL2uQWQMGA1v7vfFDVeHU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6BRmJzHYlamC7mTb4Jf2wjhavujf0jc6PXyQMvgH74ne2JqKQHCrH-cAcna8nH16BWdz8jPlsveLEKH69vSc6fdqlGGp_EoZMQtnbTwOOrY3myaetXOP5G8LErQ7PoBDfUIky9nfg1sBHOsDw8A4T9YQm1aYHfgSZYCnhRA3775ShiwEEt5_xB0fHQc3M1orK1mnxVgbEs0mQVgL1-EHw-fTjhm70UZX3YMsRuKL3yKHaCsZDZCfXNDdKnVoXGpSDEeDKse9LEfYvF51Pv1vDmV1pHANjHJUR9HjOpTgBndtVBoNyOlMZotmYZp33AO17Yzst6VxqAREamGInG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls3SXx8BBSPcU7ijYCAWZePjtV6vDbm7XKbCqRTXRwAZhDqhnkTWNqMdfpfSuxc0HcWTvajby__I09g81YghWpZcC2G47684je1Lrwxn2kvA4RDiOcbrXQCKuasqO2wMGUIGqqvt1yNmrXKqNhtYQi8t9p4ar5cEhNCXLOG34sND4YuwtljOspMGtXp5O44QulS47cjYsdHxnTGQBS45NNFjYyuFVbdaLc3MjtKsTfr1AgwRf8LjLwttAr1FP4uKFrJe9f36OVsLoyGLixU4H0_N1EdJj4jvVD9qvjBUUmpiPDbP8dC4HFweIpCj4pwJ-FeS0pAZgWYfEtTDhJXzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7k1QKQag2XjTp4ulLno-FuLd6V-b1uUbJNOBKpAsZSwZ1q3TH7rmV_MBnoMIZBgrOtUjJm5WkJ-yj3neK99PN6Z7kwXS_Cutt-Q7aRw797m3V-ijDGwnNFakrWqEpqzPMOKxUd9Sh6tCcCJ2c-NeyShNEQGMKvFuLOha35qJHn6BAJTxcz3TZP4xzMDo2ARC1tiPR7Biw8XPTrzQvkmgqoNjcFlQzpNOSnlsIwL70C7kBwoWW_Q8gONQ1wPz2Va9oIaQJeqBTkf6ZZePqIYMQN6kiLGQE8M1Bnbs8HqvHvOSXWFMlWcDQPOITTec7HbrMuW-eN3bYmTqTK6A4nQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBRE-0BRoIkjX-llOnkD-WeoHo9lC_nmCHPUi2kM6uSjU9UDkzrgcNR1vKurfokZun9y6wP583WP0qIwEk1UMapusjvn9XixJ8MGHpTQY9MsSa7kiv-ImspkyXvVo_st22-7UUdk53ycFikKV7CQBxCrkaJhRXW9PETvDok3Gb85yKcyP0mvz4LSbpk-is1mV4dItWpQDMUuQFpCD9uMR2T0kym-dTcTNGfh_4wLR8Eb5ViGUwCtIb4B-7ZmeZC9fvrWeQHcmfOSrYFoYGE3aLUL2NJ_sW7xTIE3mNAUI56dPQcTiz7moqgK1TyGlIK5WAXYGitA06sFHhdYRUw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2S3GZcxR-w0g-b8osdVFAN4CcEjKaNQ2kal2ShdZQzVa-g0DRxzyAVYfIOPF-O4OMI6l7C5hKGu-Ct7t9mhP0Fduj-7-6PcHcfDAEEniBUIXS2i9s2f6SwOhNdjIK2R5y-UkIGHGgVQ13GaF0ntxDLSYe8GRWfBXgTdWESvnHr0pr1P0cwMU6kO-UWqcJFzITHVXkESbrzF2JNZVz_MYvPWv9zeLSXe-Fb_VY9y3K1Z7OWpGqqKai8e5y_bXBOSo2pDTWuq2m_wXT3dpAynPcpZ0ccQ5vdEBw4XqzEdWMDkU1yUVxhiF4Q9ExDlu6xhpKhfnI0iDsl0ZUxdFyA_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWjq8WKNYY3xXBJek5u6R2iobYnGTKKBpDczD5Sj4zOajZkVcEtI7JZWfKiR5aVAAG0jMibg9tTah51GVSZfBjd1gwtVUpFG-BhkQltV4508uZFUlHsKx4lpGfkRmDhuxKFzpSglWIU0TR57UyF5Wb3VyDPvHy8LPaCSsmnsYOM573SRvGKRhgJX0-v1fFyZR39ySupa7Bbm8hpWBuQOhz9nf7aJk24uIZPF9KWUAvAA1fG1IOTy2XgQHf0aEoQaCiHv9AjBYh03FEAa0lkWUbZGYJEGUuWJWJeLSdL9wxI7qhy8vlYaI1qcL-KPgUnC0qVPcMoodC4GhlpLC7OEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKJWF_HDlWx-SwpskxQPaK4CihyARFex0xfoypA4LDAN1PqTgN291KbU8-kFC8WPhg64beDiySPSVTRN_A2tCo2w2C7kmwyWYPYkJ7U6VFzUYC7FgliJhdSZm_fqQ_mxCc5lnZrpgVhcwOorH3-MgyvJAc4ziWMCn42beFUxoN0LiJqc3nZeUhPQSINmPYPB9giMmXO3DTg2JS-6fc0FtEsLmp9qvtvqn3FiAOQW9Sf2ZHknDsLG2f3qXUi12ygAZxPUhywlIJJcofqzhcQkXnz0Kn2U4hvzIhnWVHmHP40-PPP737DabBhmeDO9BORsaCVXGh86VhCsctf2G-qLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7zZnaAr9g7Ycu69lPNJ3fJUBrwlPOTFvWbTuWakA8rY3EyJKetykK-vm8_WMEiXRJRYKivsHFhQsVxNE2f38QujvO9dqxknLpa9eaGZ_I-TH3Ft3hJo9sL9n7ec68rgPVuDF1tA_kZox7x3iejsa7wjyJhtva_e5vLibcCfwAaduJH5ObWViUlpTlXS2X6XI3u6Y-vw6S2vRw9OsMTHSzNVhSa2GF6-iEV8_c_U383bpVHJ0oTJQZ_y6xSwOh8fT5hbK5_wz2Wv4VoxgiX8hGjT_rZkq-iUrzKPxghaaB99DM7YckPCxEPXB4h4VVbNz1rEKz-dJFVot2BsnFLQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2U5IC4vptHbU4ZKyHeMEsVnJ_6jNbDLMuMz4kc8WSXa8qn00i80sSvUO2_uNKfx7DYmS4bqhylXizJel8P3VA8EQWwYSMgyPEvZL_9wAOYcTa76x_zhdLnr8lNTJtnee2e5qVcRnotxNL0qD4Pq_ZbJwqF5WHy0eiTNFX6GKoNMYCUBKIVNaHF8JF8LjU-TGJnPdC24qGafvdRZWDYDiaH-6a4s_M2w5CzBi8hH90JY_kFWxzudGv1AzZ6GkuI8nv_IDZVh75GUJdDV5fc915ZTWT8LuK4V-EGtlTAHv6X3BliHJjln60R9QmJAWBp81xXBhHmkZH7XaZknURrLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUhS6wW7-2uX0mtywnStCdo1ugt2XLzP1gYghT-N1ti4agIwPgxZGhzkXYD08UfjArhoU3XELygIK4-AKWb4aqWNdjFl-oYpqgxt6lffgR7aBKId_2rDSls_z8ShNWCw_grPdwRHdK8-WwRvUQQ2XyNqS4chYCFnQbjvlM9m7ZsIZIe6eQ9AVRz_WyYZHD-u4CSGlC4tle7prJoVnzs6drSgmwo3xW_YPvgREFbZJvekDjQCCCSkN1xQ49_9NGxIWHP8OXApNODlzKy08g8klCTCHAW47_oS7KlawKAtohSM9cY2blFyw_rIKwRRiPKaiWcIed33GYZG_KUhtJwe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBtwApWpUYrWbumcLJDEItlPo1mpZEwhIhfNLkxA94ZzeLwl-pAwxha4AdaiZqNQhCas_e7lJSCG5OkLE_L4HJGKfnpmPwmbjJaKWpeiI1StZy4J68rrnhHoKsmV6kNXNKZJez43Uf-NSkKTc-dr25Rj8-2bbLrS7em1OUcp_7Io7RQ63H8FK2JFin_Sm6yPQoz_qpzAK0FBR4QF91hbJlx3IS4fob7PpYiblK1aWRBV2Sy7iBFCiBhE2XambeW3C-wOmNDyZsdShUN2Mo_HdRIl76f_nf5OYnc5wR_vXSHVOuIuYHPPDWwOegZX7E-1ujeCUhHt131OAh30l3TCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W479HxBEI7GfbfsC5Dgr84EKFX2hbjai2BPZ1TKoG6jecECt3dWV6MF0vcusFYhfvSLbgh8YDCHA_ciLuqWmdCvPWe49gy64_wX7zoVsg69rG5iXeZBk0m92qHEy3j0Ip9sgw_72-eweZn7VnLbGpIk2UDxNIxMOTAcZ7gr2IsbIMAQBvzY4KP42ElJ0cBtJJuUfrM3YxinAHbgEXcbpCB5Pd3s3NgrSX5yTocradpj5TYOSUV2QgJk6tkKwqJr6H_4u7-n9oYa1kSIhbm1jCQaV5mTu4bhlPScHAStV4I5kHxWPI9JhxuUmOYEJbvkXOhe-MSAKhFeKOsdbzmEV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbrAnElVO0YaqY2xM7q9LnwGdgXAHzdQLAAQMv-1Bm9HctQg0xgIRHOT9eefgC3VoZSN51r_CdlMsJV_wdTQoc4du3FIkQzyVNkiU60x-87eO6WEBm8XOb3goaIjLqDGqTsIAZWz_l562dz78H6dZhXWtOrAN2oUsnj0e9_8nwlBUrrtjbVxbz48_7BHprRjtG_6J_wF0mZ3OiCPmxqXgsUBxGaNEEQaQa7iNbdx3ZrykvIYWsULKDwribwgisXnyN4tL-7qxn3GysigCDs8LxbYcyPc96YF4xfFSnYAlBm24nnlrZETsT8--5lcUbgH4CPOrAAjHrL3-wbG1a_Z2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiE60YKv4IVRUI0IYUr6eMRv06hemRlwaiROLMT1WQw1MyV2LutmyJLbibrURNlEP6wOFYAC8aHd_2khFEZDPtPt2xjHZEwZSaaI-uygIxuKVC0vSrYy0zVm1qt0WA-fWGDlQoejuvEtHkFco2GnDwaCpoNkoI9tWsi9T7B3GpcPprWezBWQjGrn9zcwHu9END13S1VMj5Qs40Az0k67TJNbMBk-prwx-dVKMP_Y9bP8UEtt1GCD5fYAIg5m-OcanRPcJnl-lSKGOOmo8v4XMWyqqslcZ__Za63oDu_btCthB9hJaviJPhS2KOSSmJI8rPt2Hb7jVECauhoXgt3zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q904tjBUQ9v_gVbcoiG0WCUn-CNp7tLcMAWbtb9q6fwfNMyc7W4WwLPmUzAeiuUu9sA1n7QjihukafrWaeUv1nLssOIek90LF_Rq-x_KyfQit0aKBps9S28f9oc0nuH_1oK8kn9TWjJcjdOTWnkZ_VpIkGhi_En-IoH7SN9yUbxPxTrNfxHugF1ChPISfKw64trg4iUOtC4mT79jARhkz3CJB84bFS-Rx-gdo7RBnMPmGUoVosRlpMtC6Xi4Ei5oQNdJN3xEq5zQNIAlLif_3rXnRzsynKRm0LyLPNkWZMDCnEdMwvxJG9QlX8bKExrmSo9ckWPooc5dvbb9-IQYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYRQiySISr2HJnhD0aPBmG6zgOpO2ZM9ICPo4g_u7JWCbow4Z2PkueS3pVU06g3texMImVDoA4RFoiUn1xxZGSlDrvdUZCiwrZrlC9bmQfnkVKlPycWEwdmkemNmTdqqZRJMDhYHYMihUtC_8VmhpB17pOcZBAqibqy67WVk9G8_Qkq96nXsPJWQAEvCU4BPmZPawosAO-d87WDiRHKYzcQ7i3kRebAIrXhK14IJBm4ci9Xugma8fzJvF3NJGC2Gzu6_Z0QZOfHco-KzQRDKxq_5-czmhV0nWj5YRNpK4QgE-T-vLEsUpMOuUObK2n52UOZ1OhFB222GDWfx8zoNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibvidd55m62PaiVxF9bpR8YzqQzGHyhG3hXNnQAIsMkeUTgY7diZd7dI_JSWFkUvOwNSwOkTZM_GaRAVI4g49-3ku3GJ_qdru-o_fxqWMYVXqsCen0wsi1aus0eI3SLbcjFwxGv8_3wcXlMBHhzdkAvh_rCepVJGjDtaA-mgwHEg77pVUJ4q85i0PvZlCmY4ns0votCfRDej7ZpbzNiQPrtHDRd14sCK8LwScqyJzghyJpGlBdX9--Oktxo2I-n4Mqn0vG78wt5_kHglVVThPciCfRf4CQnycSMGXXnKB7FXtjBXbPD1lvYxC5y3BjMcwK2ja47QYl2Mdt7IvH2lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHdgMX852qF5AQLYly8d6Bvvsz3iCgI9dS25BHjL4fSTIMEfL0E11W4v-Ryxk4WSNEVzr4qy_xEDRDZNRBQRLDasIJYEB8vWT3N7xdveKLGafvEkRFhcaoj_UDZ3gy1Pa6qS6trpydn0DVLy4bBDav6NKnqAEOqHgrZMxSMzwJswT_hhg7XAXNjRUy0Gf6dEX8ps3Bt4KgIuSf3iKFy5AVwtCv2kkdugGcxg507MGwJ7ffPtL-h-dsb0fE1d02WVSS5ZUEPNGtIeSqlVhjsUa3_Pq54jP1G9qoWHrfbTCliJXKhNMP1iU-IQJESLo7Px8EK_W27zPmK-IliuXsl5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob8zGgEGMq43O3VS6iq_6SHBC2f2bv0EWSH1YNXD8Xzodj2b463_UsMc81Nj_SSs7uEfojlZsui49LzlGaLdoavUITSAQqLxDgSUrEkHK-YQRg5CKTCkiQLtMolLhyknQ8vZwq6m62kaMKrkmQUZr27FITpD1uqfk_AIFFnb0kIWbxJtRT_5nz1KEqt_A9pGJVlAEMh49-KtWnF3yPPNzztCQRB_H-dPSqOX5IeQ4cW3N4fRd3srJNrrr2r1bPPGlifbqXkRmjM-vAHOqoTUEMlBZHwKbbAOh-5CCYO6Rr-k3FadJmuOUGMMDgD8IEalDZRzS4kfczz7rnqCEwWeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=olXqStZhnXsvjQJu_w_sqzPQyxp6DLYFFzNdjRX0WiBssH_SmNVsn42C4yeIypw0hGs20p53QEKJolIvzGmqUxMJNbMauMIdCj7EFI6BP_kNSzcXfk5QjsvjQN5_uipe4vrn1lIke7xca6800-jx0vzuT8JS4MBn_ektY2Yd1JQ6SJiOJFNSe23gV2114q0iGhiNN3FvNLRRXA4-be5tTp8y05sS7pzmXd0WH3_bjT2CuwlheCm-RhbQ1m4xQo70sVjXJA52X-hRdwQvRzbbdjUgBOPAP-haeTTF5hCOB133Qi-ARkcF1xuisZokAK9BsPvoLJ2kvxex8ygwwgkSvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=olXqStZhnXsvjQJu_w_sqzPQyxp6DLYFFzNdjRX0WiBssH_SmNVsn42C4yeIypw0hGs20p53QEKJolIvzGmqUxMJNbMauMIdCj7EFI6BP_kNSzcXfk5QjsvjQN5_uipe4vrn1lIke7xca6800-jx0vzuT8JS4MBn_ektY2Yd1JQ6SJiOJFNSe23gV2114q0iGhiNN3FvNLRRXA4-be5tTp8y05sS7pzmXd0WH3_bjT2CuwlheCm-RhbQ1m4xQo70sVjXJA52X-hRdwQvRzbbdjUgBOPAP-haeTTF5hCOB133Qi-ARkcF1xuisZokAK9BsPvoLJ2kvxex8ygwwgkSvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvDXuvlOxv3aik51DVviCIdQJMnG0O7ghjfdf2pYcFT2wB94FE6BoLzWkBH23rObd3QehWNE7mLJK6qn6ntCtB2-jTmbP9xGCfvthrwYtKDaAJ2kI4Cl_h07NdY2M0gqrVZ7uUOQbBNWQYuDa26rvFzankGh8UOAcpKRbf52OIOOtkRrv9_UzkMU52V8THvqe2andQ4XxLRMKi713C9hbShuRvYtOmkeDCG_LqTHx7DgdHa6qDLHG8Zj8bT0ea9u0w-HrZ6HVH6p1cF42ib0wsOIoYDfm6RfR8S33AbESTjp7koUqSCwV81MXDZ-1leg60vwsPIwyEdnzZxnHJXC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTS0TakeVm2bsyolbr0E0_VsPltyi6s8cBzRkALtv6WlMEE1SQSTS00NFNAdKRZRrtGmUcuUa-NuWyifnhQ_XlbX4ZsvNzuuy55BD6PGrHqA2ZgzzSGzXt4ho7GgoUMMX_EeWicEw2hLM6XXkG-m0fOVaO88p3bJHBkL6yz3hy4puXgW1WeHUDVGywSVcsxJUgIYcmXtSl5qCFki6PqAarmXjgIDOwV9S-l_b28P2FVVradWvXKeiSCMqx9AIdVW5PIPIJDa--xzSWmRkcuaPT3aJRnmxJ-UcHmtrGVA-Fs1YepMg_0BcwShifNyZ14mSwp5_Vgd5r-XUHuH8Hvrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLjNMt9OWSoGmkJ_rBBYfkDjru1lGov7GZmnI3sYS99Q676mt0SqnTAua9MP5SJd9atzsj5vEtz2WtNzMdRH3WjO-vGgz9auCn2b62LQINb5Ifq45F8b0a5_WwlJ60okuzJQtADpri055LFO5-XQWMB_yZ5t3mzqk5pRUrHUorRZO8RVNzl49bUI7mklwbwe0jgVyHcqw0H2FhXqvyuJbid7f97t9zkqHdG5OKgY3LWv8oBwnfxlVwMXH_uo7EZXenfbSwLYvFyEpSF90Nxx-GfIUqdCZp-ObTF6jmlfpGUvagfTb6XniOggW_-sOfea-XsT_yrQNj1SxityN4fbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm2yIyUMP0ZfUywo9xdm0OEgHw08omeh8spdXlGIodm6u50anLpaRAX6TZHfzZk5YCrR54VQHoU-XY_c9ZV6R3FGKxB6gvBEK52OPwE1Oc4wWDWvsNoh8OPLrOTUDbL09edzjYNWXkEb02RdpHi-1vR6twuaiUB09NKL0kPZ2xhuqxZR1TFsVh9s7yT-6WgTYdgLS_rUnaZUD9gRKRuX8FDcL_8mYcp4Ej4u6pLjzwR7zNAeYuMkr6HyqJJkIXTAyUZ10ZRFXmAqaJgY8rxGPLRJ0P_nAuAY7PJO5eRxzfG_XpF6qpwT-SV4iyHqwWxCmwDNfpyD9vewFhA2YjzcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=MM0RmedkAI5WrHyGOaj_YBsThz0If4Xi1u6CbPsCyGM8X2k7TjTnqf8870x8AtieuTAERdV26Ok4Grl4p6I3CmLGn1dgnIDYoqEO38aQWXlpg9i5YwDl-VkHmeiRCqzLr06T--itdgaCAKz3djpHV31vvrwTvU9Is7nFU98wyBOHKGudbyRDhLRs_BMVEkS4Y-63lKKIpgFcxN-ObGCzBlrdMl7_4C3SMUzD8b2_gWUz0wp7dlvE3ZOGKgEkNX7vq55M6pWcSRrNOiGJcdfMDaVmZhOG_B626eL3jf2VJ0h5FKv2VeSGnoiojq6Ci0hqAtKBbJqdev0OQzTDW-arKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=MM0RmedkAI5WrHyGOaj_YBsThz0If4Xi1u6CbPsCyGM8X2k7TjTnqf8870x8AtieuTAERdV26Ok4Grl4p6I3CmLGn1dgnIDYoqEO38aQWXlpg9i5YwDl-VkHmeiRCqzLr06T--itdgaCAKz3djpHV31vvrwTvU9Is7nFU98wyBOHKGudbyRDhLRs_BMVEkS4Y-63lKKIpgFcxN-ObGCzBlrdMl7_4C3SMUzD8b2_gWUz0wp7dlvE3ZOGKgEkNX7vq55M6pWcSRrNOiGJcdfMDaVmZhOG_B626eL3jf2VJ0h5FKv2VeSGnoiojq6Ci0hqAtKBbJqdev0OQzTDW-arKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqYEXyu_z81wgxaeHDe4tzbT_VmnufPA0_2sKlrbtBGVmb3BDcSI54U69GNV139bZbzVCEC1UeZ30cS31lYnlJoT3X9-fobWIz9ll4Et0IbrQBH1W9VHyblDrcCEW605t_G7_13OEGORa30HVybtWP0MXe1iqp0RNRY0pLgqWy9AAGSwjsMbp82Adwg6GK2KRaynSv_2sl4sYbh73EY5_kqNeniB2Wq9CMmnXSM2LayphCmd6WRwpf1kbDs6B21AnCa02Kc3e4ZGlUMMAvNjWAXrspaMVN6uu0k1QFdjt9eVtGR3zgtA0Qbuudsn5leUTr55HkGItuX8mM-xAZyQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N660qT-YV___6-NEH3hxVSBkr9A21L9Dzc1QC9y-1T6F2zpu1srvEkxi1OVa2dEAwdw5S-VX4SZuG3MY5O06eAf4zLUoKS3ALvqSJIaF6UArKDB29pjO9MumOR0b0l3FvElsrydzr2WvIWhBBrEsicHZIUucsIm7xhRHOb4DHLe17hOfeOQOlsmT_J384lQh53vr6ELyIzQaQ_k3sYF4alrAIfoJhAYsNjx9C1-N366xCkcBgv2y-YvUFqoeX6SgEHHVIEifv0MQRnmiPaCwxBo7q8tFed444QH-gNyv61YXGHd178iiiisP0GOgJxGkNNONEcjxMhGRHXDC4brwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by_ErKQ1ixffWm8xoo5TqFghQFjOkyriwRj8E-ABAuWxhxatqhqlzQ1soJcUQPi2JjrD3ItrsEPsXo4kQePhwett23O4IZrnbahKbJaLkca1whECT56W9mGzMktN8rF5v-7_Bxkr4Xhg-8eGYRiSM8nw0ezGoRZM7tEQBfPkKklRoEDmG435WUM58rw8iUOGDkafJ0-Tvs6Pn7Q2S13Edx8MOzq1sb98JnmEbPa8713LdNbOiLdc44NsJ6c7EI3FMB6nQ6gSvQyYL-GPFmKTLm_otPB-R4-cqPUMWxa5cgOAcuVzmdvEqBwJhWBh8CjIwTOe-mmSanzRjxbllWNMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8o-2-wNGMRQcT-HaqISpysUOrZWQpwlCQEFD7DF0V_eCGiGqm5PW3--XXHKp8C_M-DH5OLf8nOFejZrD0dTnpamZpexepxXrZaNy91_S4AmWjrxk3aPVnPUu4iOrTUq7GMNO0a7B-JtJWqkOCBNRmsBZ3PzmSsoupL12czbDkPURyriXBGSuEhKXnMk2I82O1RJb8Juudm0-S9mhxFLFyoGiHlKjl-gaud9bGa_6qrNy8xODUMPV-EJJvgbhAGJ291z6ePUd-0QMxGnI3jRna5xSLzGwgBVt1fiP-9tVIToSIyvI6Igk_SPyKbz7yQsidFntmHturfw3Mx46l9MLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7a4zbbTffs6sqU92ZsiALQm5PiqtAxHOp3ckv3f4vXIWZA9l081nPoXAjnIWXYVyDNzX26krRJ9WB0fkR_7e7guVF843LuBUIoNa-eCS1klW8-Op7A6oczw1wG_8qLBz_wdUEBvyXvYgwhsrWaxll3n4oadMXp6N-zzVFLh4TFffSSwQ0B98X1eDz5sJhLuaHCPjOXlW1zUFE2TY1FMddfQxXP0xoC05VFmB-xL2JUIw7648VjkclBFCWzEPZY8SWDm04HE_0ErxE0-ScW8uYAUOosxq4Or2P2Sh6G6d2B4EzYRXMcrGJdUNpSTJ2deJUm_-bpCPXpom2E_yLMXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6mt8bqjeSXdB7gqGC-4FlxtPSBIwkPV3DJw7HZ7CDrWl1bT9HNfDPv_kHl30skq1XARX_mxFNNatWDgHBeL5LGSVDTzzOQE4ZwSlds1RDsreVFYoKQlFz_0lkgcWJeleP7cAm83Wu8kMvwN_0wK4LFEJZDkAe6-_hc6gFXZsNsjcoj5EUnqfGuhIajKTXaWFS8PE0iewjlXIaknGgm5RxGJpoZSXfc0oOD8wDgxTTXGfaNzCx1h3C_ZGAKcS04Dx4AHONfv2tMyrc6lUDdQ9tq3VCyqfZkrgqbLvmKUE03FNia_aDtHr4eDpYxxR7uQHQyAmCtg9GjxJz9ysEkKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlFJvo-ysFwp8CMtK3EpvbSP1WehteAVB_H-5_nx45xXwApyY-u1SOD1pq9LJ7l74asAK90MS1vR-yPe78_zYTnoTwV-jtFoeAkmuVsvS6W5Pi_fjhJGz2_KAjRfK5zOYwlhRVE0JkrSq2fCgq16d2MXQ7h4-RedF_Ceq4K-Go2JTEabR5jZ6FHycmE2sftzHRHdzzJ0jhSJFr-nzh5h1l6hLF9ftiKyk6LmgHiAiLUHGnSJWdRuiSGqpOopxyoF0WBAe4_Fp5eyiw2umCN5_y7SMDboJ5HuIzgY4oz8JKoaK-bs6UaCOlNW_ed8zMi-fxWCHLHMuHMrDuXZTpC1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izmCZQgeVOmMSeSq9HJiN1wtS34rMAewHOup73XF_4aOoPzpIShQ_fMmXHaarA1z5raChVItrKrRjBLexQx1k0UzXRdJPboO2RP7vOPp6Ave43KUMqG3P0i6EiDPCnQv1nRZGUJvj2laILuIFp1J-4fePRHC8sQIRrWWUFDJ4ZlRzX2IEEk2S3Yw057dcspPEeyvlYEUIa2RaycaRjbMJd0U8phcbcYVG43SOXgBqz5AVH8DMiTekngDKftQpeS9hPatm-nwBis_0CCrskSZYlQtf8W0paBriXqLWUQZx4PB06MH3AzCY8RdLrkOcTkRX_52vEyZVAnT_7YeC3nuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEvH1nbJ9BjDERtXKQcFhSfNe6Cj3GkMAPAoyde90QduFBUQsZh4G0XFCwuD55QAowsSCo5WvtmS1eS4WkSmoVFLqSfAdBpUsz8MDO7Ua09DnwQAGMBZGZVwK-ogGW9Ux6I_SQqFpNomxfxXfKiwyl_zsx4fy2TfbboKgHxZowcmCtEQOtssL4IWhhPG0S8vc8-oFeQJitC9MvjMfHV1sp9vsvHu5P-uMtcM0b_DHcLCzDQPUtN9nSNQd3SwbS6o0zyEj0hnEK5mtj2ge1Y689-401b-KiYCx03c3uTP-ZzKFbgrplW-FrYU2WO-PbietryoYFKZXCdB-BNxz3UTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj1HCShN5orcbEWoFQL1fEU1pvg6qlnAgSVCvbOhDFnO5bzJSv1Pk7ZbkdYmRKPC9xKvYgGXyY3dq7r_GPAPbqOYbmwp2O-pPwrtAKQOn83ELX1LNnPKT6tR2m7YnBWbieHlAcII6odPWSOOsQy3or0RH9klyvL4TK1WD204xIEgjEMJ7xE-7Ij6NMg8ld8baiZj3GWSPcWYLJxmhrZv46xduk4v53yw4Tox1zDlrAxeJ2tCUQghh3LUgklBg69jum13AJwgPoysCtFiFEE7lBtW5xq4lG84I4N9InEEeKoG8j4WhPm3sMN02oN2GkpYZ1SYTypPKfi9p8BT4gug_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd20J8H5Z9dfs5TXyxabnVOOCeezEKxDkK8mbr5vT4yZKD9xNuHmwTH6a2hlmiVQTpdCaEGVHBbAO1SGQciVDAoAtpJDWA_e__cczKmwC9koZ8a_z0CbbfAUMp08_qVbuFYZ0YQFo8WYIeWapP_dQC4VLI7WA1h0Mg7r1YTcs6IWpZYrDIqnD1ZsDpZIycyOuolCr0pnJ5d2CD5rTL8gsKKw9oyU2fkmuj1y7mCRYWi6VoJkXnB7LZx6SHSMsvsHNktB305pevzjIvo0NfZVv3FfED-aKUFQpT1IzralgsbVsEmR9vH7zB4jZYlKAgN4pjlt3jP9AWkt4nSvBsLONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlS-1-SDDFERlLzkd19WBgUNn4_TVY7oDN_BJJG0DjhFHqca9QaCBay3OgIgRi5SMBTtYTzHli8MB4aJ78E6n6b0HC1w41jyGLumSgBzGUtF8PiHeU-EoXvPr1ucv1plgUFs0EkxXBxRLK2z9yhjkiczFkx58q6ajopZCxmhs4NnVKoKhMZ86GuAfhjqILB2-xJOrU5uk4EVGel32bfNFbql2wXF8S5jokIu2grxLTYw0f5wDtTZoMVGV0l8qjNXhfCHFcNYt48huCOoOVzDBRdx6FIxKX6YMr44ozzGe8INX_J-HTo1VL8w2C0eTMHzMOJJlyHPg1cJRffVdABnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNGgdPoe_MxhEH6RBdmpvp7e2SjwDbwok6Sk7FZ-scxjtTrTuKKu4yHHwksZw7ZwFpSLnDFULRX_2vj0UniPRuXwXUltgOYir7ihQhhtEovBSZRS0iEq5GITJCKyt45XxnnB_1k34KSH4Bq2KbCW9FGzos23mPtpB0bVbCf3tyoXOC3S2iOQUyfShL8j4sq0CLF0-Y3A6Mz6wCHpIGlT3LN-h-_uBYNQcZF4R-OJdJI6AwZUatjcCYQcsBHl44RObPTdr722prTD4a5Pqp6g7MdF8pjQhd19NEmxCd9gJAOJjXm9YDJ7awPo73Y9zDVgJ8N33YjU9LbHL_ib1PBtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK4KrxgSow8N6MHbwnaF81Z9O-fYuxy_uGJ1F9QNcr8VKWKe4ssy-dYHLCqBLyHY4AjArr4p5jO5nl8QQwDWOBlQ-PYPmZNvuUEL1XWW6RqC2HGRmDIQC9ySvJ86pN9S_Wz8l19tY5bRdGkYv59FdAs5x-W7mnieavRFKTLx3u2zafEL1KVdut0Qlcv3XQTSeNco-OsDMS3eUwPaVOueQcSztZF-QA8wPoeFNTWNCS8iCFw2E5LaRjx2w5qQ7iniOKI9sHdTe-lsydLEnO_SPiEQGqMGzRYUA-AnPpuNLfFvv_gPxPiJyi84K0f6Rbfrb-UrXAocgouw5PkzhEtGvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-pK1IqZRFldsgNjEhtKWNdfw4LSRePqgUXv6KoyG1iGfb8tydkAmp7jUxsHHKLV-1BlxDzqa2ataIqStHmI3EFDpw-Q6UXMfwajh6Mh1215bzSAvhkx5MG3wE-k91oSKviqYsj6ld4z2Ll6o8TTG5pUzp72wYaLfXzs8Vc4DB9PiSePEmEjIa1fz5wz4fOaKEEeFNhtQIE-cLyp7Ok_4Jvb0F-nfsKSqCOB2ERnVavcYpO6DL7DfksQFcI3zBh2g1FhUhlJIrAm7mIxp6NVi7toXSNgWzi2I7tXcP-bSdDcJtnB8oF0URyWlYkWBsSqVRTjH_HWRfiMmh5XFgyMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sclDdPoivtf18Bo-g1w4U-0PZNG12oftEvS-BESdhUBFZooJrd6HIwfavO7n3RSyrjzjr9y-oalLLZ7oS1yqdHzU4di7_gb6YvCsoBErEvR3ZDWzi54esrkCUwADn-0vbSxEn58j7vNfYXHI144V-i43eawxEtjCkB7_9O-Rg2GHMsNhPgpBQQMeddQXwCCzOmgYUIbyuemM7-uQWRgDPbKNux2dSB5e7Ke8wF2CH1qzRqs0F_KPiA6EKKt1nPDipRl11vOojEgxnBh2MlDBkb7Q5GHDrqj5s2U7SBrIoA70zVcPkTDpqb1EkpOAWGOjCZVusrgZGVZDeNyeFt2srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v34g2QSVk_nxIFbjDG2Jgl2daXs7SveqPcS7eW7tGPGhG9zUJvhQJO7M7PtZS89HG4Oh1E1UwLXmkpaDViBFS4WVJcoqVVmOV49KM9zhpG9IRg9TmzTXrBNEKJr-FvdTRvE2hEJ3cHugPjWUz5fhBRjC8NC1mzjmHpWstk20vzIdNq4Ysgar4TLZ90TbAnVzSjGy7pekFB3r5VNFrYKkXMU1N3XhlrKVEc-9GauCSFH-yBGX6zNZxG889cnFoSZh204sZExDL2AbQ8qufyoGPGqDYgK_BoYp7MoHnRGvntRXafBVzgW2ieT-mktQDUFBs8cJZhVY1SFAwPltQOOYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG2oALZ4KxNZFIQQp8bh5-diJL41QD_a4O2eIVbxwVCKT6yeZcXBjb19AOUsbtC8EF9fFO8i3ZYL7XQkEhZ5b7DFkQpSc-2LvDXJO0kkG0rSuQpdbOzk8Hlt6NIn_4tHq5nsTZFrjoy8F3B0DSJjcYmp-X_3bu4lutJw3C0YEeb0sONvaVOfX-GjMYL659-48y8-PwBlOenmqOSUqmHMTrlsG5fB2xxwVNNdauhyU8y1fM_pEXhI6wv52Cr4IzCKsDcc9qqSEU2LSEAyzK5ZNKZCLKHht0Z8k8AZZZb3awtHS_0KYgyJGYiW4aG-eGHe72IJml1oQ3m3F0QU2PICRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htfzp27aX3Ybx_cuv2M2JeM0N_q1hUWyHI6k2TGJ7Oo3krkKuJtwCVb1FGt_FvlVCeZ4mh70hPzcoy8-3qeEYTtWCTWFqmij1sKjTNrvU7pBj_ImtzNElVMYtO7r8z9Fini1R_wdCHP8z5Qf604XmFeVfAzBnRrnpzkX9MAcRpy2-HG5FrHgueoKEnry12rsfo5PLrVBY9TdOJxIsQqMYrNKj6SooiwRb4vhdOdckUgSEWFV3jr5vs8FKSOhjG1mpRUh6B76BjmRDHvwPIyZxm-xJrAwWHO0I7TqJQPl6YgHSVnYyN0AAkz3gj-nKz3vXy9oSEgHfTMQ9cmOCiBpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfr3bPmNIMNS-ZKLZTUD-sW6yjXMkCq3r_gInRn_bzIwR13ict5GczpA5kNjcpX-Zs6mhh9JLWKDrZXI4dkmd_vjpysLQdSZ0trxXmrmrm6qIQ-ethyw24PzAbsLsGkS_H0hCRLUMezUZBghn6sRbXORRRAN5EH8Vxm2WYSs4r1c-UH1j2NrACZTZONBvFkVfMOJwLvKYWzQzDtVqM2min0dqYVKXBmFnxcle2LFQm4aoyYnJDjyDmOjHd6Oo8Wbuop2Ipe1np1xMRSAXwC9UUyEtpruv1XfLzm7EGSqhWVpgwbgq2kfWsgIVPULNDYPJtUUU--6z9Yt5vamn7xsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk6WaJ1Kp676CZbeS9BWuZKKs6M-Lh_dVD-uv9aNmeK6NrasAo4_RY9el9Cnbd5UbTul5LSWokplBsv3PzaI9tyKo4pjaveAUmO07Jpmc0tBPt4da38I_8ksYbLnWfF7Hd31O_-Yjtd8W7bIoQMdx7fvuXC9ZA73zR4KoYa2OB3xvOOQizrCzWclpZ2NfoCihpnQ_XrSeo4SifHuyvORJhtzNcUrrAQioa-wwDknXqsY5L-GcujgXfgK_GV2mEE3mYAw31QrRb8OFR04_9YpKhv3Ie9L4Q1ICp5OmxE73wYZZJWj9Lyl1kOgGGoYuNAUknhihTsc4xD4AzuuZU0HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU8qVKaKnCig6X9isN06sAJaS1CpcOpp23hhkr2ZcQ0rsslQ48Nn2No3YS31Bszcxp_61mj78uadFrCLZragPJoUlVt92edCxy0QkCMwDFxNqlkenlsS8C5n-zZ76yz_-2cfIyBbXSbrZ9Kz2LLO3hp49d_yRAwZvxugxuziMOboMMNF7YGXOJ_7VilB4iFf7i2sJ4joSeUnYD50LmvY6bp8p2IxE4TC0bXL7rayv7-Vrz_YYDbWFpac3AB2xQqBEO118MpbN5O61VvI51chDUOX3_TPUY3JGf-lYj-BSTKGY0CKK7np0o4YqwzScwlrfuXXi1eYqa_xHiFWDDtE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNtiVL1j8VBsjlMPUR8gGm8SBW3sJA_PT0KqECi50Z23p4ICkWuuWYZsl8ioV7kQiE1sikqXCEB4Wd892ZBx_DLwoYPMKOeObVQgGOmRV3V8iCMtoT7AT9SQ8v4I9fkfN-dKUR-loFAnnevzlKyUUNouE36yxHVk5tna6jQJIwoIoOKMhaTFkAzaKrXFlE7Yv0_l43Ok8OXCOsgliuDtX9Cpk8n1pf76eInabMvK-Wc0QXqgMQSlx-vE1Bbya23_--TdriKf7-60jx5DTktHObPvRIm_gDR6W2sY2KhiIUMRnaGoPLxM8sE1Cw2vXiOc6arfG04lNG-AROm9hSGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2Vc86TGGpZuGX1meTFq3bA7U03rzGnhMek-SPr8W4t7tjD3Vnu3RzDHCKZOpn8yfHgbLQ7rACprOfacVkE6NTHTJWoSbAusTWs6f3Al5bRB4jCIV7nylH0vHsNyHIyBEt_x3RGmz45fIM7UO25ClFbjF6HL-OJ2Sxrz_iGzQ6y-VnSNVqNYx7win37Utdnb6hFRdrqccLtNw3mTx8wFI2HwYt7SFn-n9yotbsDV5IxxYFGm3zr1T6kWQCmPtrlUVDCkNrJSsZ7Oy-n81S089Vtvd09QP_6IDqErEznFsYBI4jsPQLHtqI86Lu8ZKEkVf3axxqn7Q3XR7ZMvRaO75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=g8dsM1cCO_NxTMQx8XLLpJwZ2bBU8SImVBgLWpf2OfN_y-tVxQFg2HUYSvHEqYWF1XGSeKnq2CjpA5W5jKLssyg6IAmyczkUBTdksLyFxtuJJHCkvna8s8GML1dybaJyPUB2P3maX_s5SH3oSrkq2PTNVl-Rrq5w0YS202tf8YMZlqCGY4Nv0XcXxzYyKNf73gIs2FIGTf5MpAVI20G6pk4kVcPdsYfvtOwYbCjuopnHKCBdIGhTLu1nev3AnzxcHr8QMV0NWQT9exQzrAAd-S9aCKrNKgUoaZMCDdlflRGuBYe538SLkNGrxtjW4l0_pGa1hMUnTrS-oQoWkmUX2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=g8dsM1cCO_NxTMQx8XLLpJwZ2bBU8SImVBgLWpf2OfN_y-tVxQFg2HUYSvHEqYWF1XGSeKnq2CjpA5W5jKLssyg6IAmyczkUBTdksLyFxtuJJHCkvna8s8GML1dybaJyPUB2P3maX_s5SH3oSrkq2PTNVl-Rrq5w0YS202tf8YMZlqCGY4Nv0XcXxzYyKNf73gIs2FIGTf5MpAVI20G6pk4kVcPdsYfvtOwYbCjuopnHKCBdIGhTLu1nev3AnzxcHr8QMV0NWQT9exQzrAAd-S9aCKrNKgUoaZMCDdlflRGuBYe538SLkNGrxtjW4l0_pGa1hMUnTrS-oQoWkmUX2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haZjXM8bKzUnMxtyL9iQfLjmgU620WxjHtVuWLe13UQAaqzUsiydEjU4WdXzIXNbwi4IU9nVMhDMhPynbPhASOvL9TLtxZWhDdEz6APjOQDgEzAUl11Yh3Z_Bh7q1fPPJwGAQg6yTksb3yG1T0U8JVGpC1MYErEKgYlN5S9nKgvMo5gUUCizgQErFZkirSQFfwPHsUcYm3G-aa7MsawPRJZMi9158ge_G7SojbqHQKi58qNe2Y1O_QTI2SqpsqZDTkKaXzDPCJEZ_uvm8DYFebsNHOPZ4ezwhKIKIUSuNFtgD5Lujuik4aYwRenr1ffit6PRxHSzijbDvyPHED9z5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs2v4MIwCfiS_Hhc12IvUc15kq_VRkG_WRQJL84TBGj19uKS3HGfUzVZfEyOsmzIwAVS2fyLwcpiWvYnYV3K_QRVccQ4vcui4RyKxesty8Sdcp4m00hBhrJtuUT_IRWR3tojSgyydA8vli5OMpaXvqL7NGeyqBr-pf-f0d7rMJ-fDm1o0MU_Ewpc91gEplWSaX94ccPCHNgd05Lu78NOf-u_D4dAwMVYL8MlSt3bJryHuWKT_G-fWRyrFhtr9JL7EJoTOJbn0D5C8puEBi_ZzQJqEcR-zjU1zkmo834uJ9LNlnwlqqWSnNCGO6eh9mM4p9zVob4ycSJQA45ZsNvY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdJIJvl82kIKQt8K-nYHQpqXWizD6lsOvPNKRRJrjpnB9uCNPi6Ds31wRepa7stRDPw0ituV9Q_rlNIiIzVU2RFoianDcwKpUtlIoCWJvco0yMSdJaUIK2P1zlVakcj9BEUNYCFWS52SRt_xKAb9a22j16_9XuUyJDWjBjmOecqFSi_maBRHTZrwvMnv4f4s35UwHhfGnbN5GUSBfNQoyHYO_m14oYMnYjD_c9hxqU0obclgp75kpLx0aKSEt26PKmm4RjaRxUz4ndZBe9yVru-xV48ZDXqHBgwr_bcuDqeJYImu5yPALD9LHn1p3ZFTVZWd950vOpWhnQB5cl11Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=a0PCYLrKXRcqhPpZx-8aSuUWcgHGw9KuSnzRNCN1TsurjXEp7MROMPAIjo_9yH5OdCvmv9sARG9YFLRO_CRxEJbPZFhc509w2xSp6eFinkOMBl4cvxreejPQqo_fQbj2Wlj9nE9yvqab92ogLQu0vWepFooSpJ71bZEr2nsgJAr1_1OVidHN49Uum_tM6Md-M1D1ZdJG6dP2AmmOucR2O_e8jwXDYxP05ahnCpkYo63F2B4DnH3RcO5Pju5_17ziVXUziHRNbHhSGykrTy0-8BBXNrtoHziUDvx1xU7ulHvFZyMxmNtbygdCAfr3G-JnpjX6DUNvP6sV1IgWYkAUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=a0PCYLrKXRcqhPpZx-8aSuUWcgHGw9KuSnzRNCN1TsurjXEp7MROMPAIjo_9yH5OdCvmv9sARG9YFLRO_CRxEJbPZFhc509w2xSp6eFinkOMBl4cvxreejPQqo_fQbj2Wlj9nE9yvqab92ogLQu0vWepFooSpJ71bZEr2nsgJAr1_1OVidHN49Uum_tM6Md-M1D1ZdJG6dP2AmmOucR2O_e8jwXDYxP05ahnCpkYo63F2B4DnH3RcO5Pju5_17ziVXUziHRNbHhSGykrTy0-8BBXNrtoHziUDvx1xU7ulHvFZyMxmNtbygdCAfr3G-JnpjX6DUNvP6sV1IgWYkAUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTFhkQaH1Bm7CH7ADHg0DJVo-qTEbJwcHbwMTv8DEHNDclJ89VS7rdo0_Leu8fz-QDdF0Vyau1GY7B82abRbZKy4KvFsRGelI16hTqG45_UiGc4cfnjuO0fmVU0yNC3YkXre8D7qTbKKCksF47efbv4eERO_9uL7jFt65b7SKj6u-4WrQ0XVflKZduq8Q9ImKi4VSQo1sK_E3H3tPreIAP4DLQeTdvCsjyZSKxjdwQyRGP48x1sWwaak42wY3DWjD-3cqSVOrYDrw6d34-u3oNgvIVunn_utL2UKq5hzkhfdiIrVdxIlXaVX3AnCb8IbUvJPPRsiZnghF_B2KX3-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neD8uxNjmNScAmxJ9T81KHwTU7GdznZK1YtSV_viLV5q-M-iHWzWehCccbnF1VmvYHblZYcjYolGVGv9C25DJz7rmbG1BuR6b5cGCkzHbtS7V2Id1o0QBaY-uDdGCUpCqO2VA0Uf_H63Fgj4ooT0DQ5XBFxvswekXsEhdMqGtjWLrusHaQF0QEW5V5n6clyNpSWn3Y0tYyiT6wjdWcw9U4Y48adFl_DzMusK7xGNnL2hbu7V1BLPkQ8jd7iJiZ_5WjSVrWk5RgbJtLA_PhCKPC0oTRXIbSnFme0nxl-nXtz9n4Zsj0UCs_d8xnZG-T24T1YknKxUIrpRuQqc09x3QB9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neD8uxNjmNScAmxJ9T81KHwTU7GdznZK1YtSV_viLV5q-M-iHWzWehCccbnF1VmvYHblZYcjYolGVGv9C25DJz7rmbG1BuR6b5cGCkzHbtS7V2Id1o0QBaY-uDdGCUpCqO2VA0Uf_H63Fgj4ooT0DQ5XBFxvswekXsEhdMqGtjWLrusHaQF0QEW5V5n6clyNpSWn3Y0tYyiT6wjdWcw9U4Y48adFl_DzMusK7xGNnL2hbu7V1BLPkQ8jd7iJiZ_5WjSVrWk5RgbJtLA_PhCKPC0oTRXIbSnFme0nxl-nXtz9n4Zsj0UCs_d8xnZG-T24T1YknKxUIrpRuQqc09x3QB9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0xy5O3TW0P0Fm7hTM4saP2CjJgMd0dYQ6AhZdprFFJLiJwWvqduH6LfNEZaEaOFmSpNNToFEAXR6Jn8urNw1lDEI0ZTe_t2em2wwRdklIPspxMlMokneZwq2XEZWm21wS03gloxf1QmISS-rZiyna6OlQe2rLgyzCWZoRpFJj7P44EqGq_9r0KnqITxpsvOO9BUXRZ6XXz3NyLS0eUghFF2ETpcTK-iihg3gy46y1JowHAbcjM-1t0KdbdU2rAFoT_VLxVj_XfIPG_sODD26Ew6Z8eU11KcQBaijjWEUyt9KGsa49uLn0ZOf1V9Uy5l7dAVQkHXR1fa5BTu3VvYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePl97v5A-A8-ezd9dQQ3zkUXfQnpcNcDn1ulzyGDA52_UhLtfjQfnJtBFZFlfO9UtpQsuq7s5Pk3HDB1gqiXF5bgbM1IbWS2_9HnW5LWo1Iy7hr7drsXorkFW_JF_n3_m6zyTMebJpw2s8FYeDNXgcUPbgKe8z4BKTY_CWLOI9VbWkSUYnnLkm9nY8k_SHhrg0e6oxU8BhUO_DUtubbXD6C2byy0f85gDx550uWX4HZfE-BAbZElTWhCfGHw2q6LDi8uO2hQfT3iGGxCoJgctx6uPBxhDSABvNBRE9H0MPEP6dtaNO9-gfqQDClULl6ZUtDSBJt5_fGCfAv7QyQHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXYCcZXhUAGDT15dax9xXPevLGv82O9dfTTEP2tvBmSt2g1zTy-KFwepReicuf823TZ5S6uF2XtN-dxZ32ig4xXUp8xwmR00QgVE736djSymTcc_pVO05OjPyEVplG3hlXDITm-eBTeKFymrLgFgTBHRJduCdJZpC6vnvrE6em11otRcb3x7EcD-YGtQxpa9u1KrLci-OKFzwkTqjyvOrUynPo6V9Wbi1uAXttT3noDWseXz5i2bdqPJ3qqdWjnzk1aJMSGVhZqI26JyCJQTWwt9bOWYOinF1MrOcxnZgP-zisjX9sdTzU-wO0LEKOt-wqDiwdyjHHzn2ybTnSZ5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJuMPGfO0duuQ_eLjuUepgeBcwizmEPFBX_JVW-cTJ_33XyrezTZtCYCX2le1cA13Vnhxm7vAZlHU7on7sD-1kR8iT6o2Dsb6Ephaij-ryVhQ0uPtekqF_4NknMcWeMF6fNIOz8OjsPJdcKAte2BotVVa2v-k9FADBhWAg_COIYRmOAvqDhiBRaebyMQhHgBnGGYEG_Qz0F6n-RHMYZ4M9Py3NE44XWeqNaLi3YGXYV62OeN8Z7MRDZxJz6g6NcWrEq31gZjnGuH6xkA0zCQy8ZRIOKy0oDgeGxYPhxs9hoClM1ZYChbscUawXCpiKfLlhNTOZ1PIdpIQexP_IW33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFxEw9tq1WIvdYv1zCZ-xaJGPZUiCj0P0yqJscY8A8ETEKAuMwTgxWXX5NvgSJVKZlC6f0SCxZeqHjrsrQQQR4fDd48ljTlhH_lphOCHOShsQmD9Wd2jyCnBLIgJgj47-YiL_Q89wXXagN-99wobWuGODFdFttvpZ7qGh6VsBZr79d0CXswuqJ2Bk9QDObIYqfGmTyWrgzKtxP2AIOO8b8fBHGwRwblPCu8BlW2Xozmsv9bZxUGA9IieGQzTop-TWCk89cQLc51BHjl8h_iQtXRhSJpK4j6SXQbydAAa-Ki4QjR53X6dyWVZpgda072Yvv3jgWUWulnbst7VAyxcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jStIWRHwdr7nPzSFn5FTgEhiGH8OIMfsfwVTLWaPlU_oHHFa66oXBBvvbZdF2FLcWjL-vUCG3w0kaJr_SDqTyXTr1GBvvmC_izPOWGdJMyjIY8l_r4CSpLTvndB-Aov4YKF3103KwSVpVb2RlK_n4ekt5J3x3HkS40IBHdFDTMciyrka5gbIzvg_IBvufPPT60PsLcRCpSx6q-QF4-TBQZOBHw-xjf80IYpfkULaUuj41etgoZ71paEN5whP3j2_9a2cKtKckvW-2NmVxzEJqRKq0r0EVtCxSn-D4dmL0LJRsVZ9kluql0dJFjN8vcP2VjVUAMURyC6R82bLlkVDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLJAxZuh3VjpsjxDO41UyAgKY4Q2_gpuDdkZW9OgoXrOYtaTf8IYfF7iiOJ34I26mkhNowucXmHdjEaRPrsSvYlIJfnjNDEkimExqxntkRTCZws54GG-ern-E1qV_r5akJ4-Us3Q3cy_lBxH2WXH1kbctYL7RDo2mmegiKuy93cr4H8q-eoPUi7myOs2l3qQSq0ul33c3j7VvE06oz1NjmnhMwDsICKJyLF_8dmYUmbUCfypv5JcmgQc6UeruRfE49qPsK_ptN0GIJd_RdBYVdhREeeFICU8g0Vy7Sh8NLH34Sa7Xfjxii7UM8ufgGpb4v7lAWUso1Qc6V9UX4npNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7GzlMR4caxAV-ztjw7ItLY8Qt_nsGWfE5b1NWBFpFdhxGEU7uKGiJK3tAWv6t3rXRpA3B5GnLHvkf6rBwt7niRJAmhoZMwOgGETkMuSbIpDREL6fI8M_BMml3vY_tLcjhVm7lbqbqsNQyLTgpvvuEnQQA8w8dP9MPsVrxR5I03on9N4AvJ0bYM-s4UKC6Zd6vQO6EDSrQ60y4hG_rQ8cp_DQfSVJ2wffJ78EI8YrdSs9RR3DZb5h80TPl6NEFfsoDeTmXV3BXDMKA9EQO51QyrTTTzuYPAPI7P4sU7UEApuodjjb0pZrCQp2cUDqaUPjSHSExjg7hVeioQ3sacDdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez355pr0JCrrKz1a76Tb6CKc_SuoCPcAkujnGTSioamRyZkb99udidwSpocN8melGU075ORSVLXQUYI_c-mVs94JEBEio4O8q25kuQa8iBc_RKpk1N84GYx5bI8AsG2SUG6MmR5V-H7edUPIeka-cNnP0gP_JX3lmbXMSGWUI2j39JxzD7kEcNzZqpiVMmFd5x_i_10jVo7dVsXtCZBPtKKbv-rUde8SbDPrMfjeGzKqk7dkr7RvKUrPwmMUnIiRV-bI48hBlH0FcvdDvYhK8VHE_CerG7jZRgTfUZxs3n2crXFy5oboYs1XRwHdin_E7dzya6O2zsZkhSQodTFpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxJ09F8DS7KEU6bmIzS5aBPGFjQeW0XhsPur6X6vTLFoQ1XLST2i6h7kloqDIi9hNpF9lGUzE0Z-prLpNp1Iwkd_kcqygK6Kx4qoJBjFaNAz96MkMKhrV8Or81jaJksmG6jMCYIaff5YrHUZvuWew0Ll_0k9E1CpTa9IhnnEED0XONrGZCdS7hWfK-4kPJ3Y9p1kTPtO8nP5ZinBzsRBIPXIaME7VOmR14Y_YQnuB03Ve6q8RQASGqQPLVPjjqQ91aGAVzZVLnRfuiEaHxm0h30TucJwebV_I4csnOB1umKCZlXEmBP5htD95QF3U7oh58TMGuLQUYRm81E_iicrGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHWOhpowoVynzc99j2dX2kHZQpKyHVjOmyAP1uvBhX0tZmlvzjnBM4RgiLNWe-Eazc9t38UdqypZGaucijVYYebEQNKeiKssv8FDdwgT8CovxBRT6UQg3xFVuVLp8dAULrt8i2EmJa1TkLDEp6moiBrgSlJN_WhUCjWNoMy-NXs1pUe7FkaTi1M6OTTThiKG_z809StqDBQ0_HAaRC9crmjgos6HRNvIpAchGoBvR5DeIT4U0Ps0AorEJHMUp5KJBd_Ac9Z6WNUOgTgnSuUXhtkq3HvfGWRz07tLNWnHtPHwlZ2fu5tV_uKh62_gvj02mqjlQXUmLalf_9JzVCj2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYUOxL73Kwgca8S32cZpdUDk9Llg79z8dZmCr21KSD7LtLyiFzT76aGOwrFXrPI8ilFtB64PwkKBMwdWrH6BfgjZ2YS2Mq8xRMpTY1bi_U5SFxaeEXmY92FIqkdDqHKEKZrtkqc20yTVTHD_-2hgCuLnF4yZrelvS9oDPI2W7tWKpLwR58dVSPV7W6m00oEzy7tAgPHVfzCHK9jySNXoqtkDUsUYt69MKVd-9jZReI1Z0kaD3UciDb6XbVhxDE4ogsV-pNWkyXpWF4YQ908LK86ng71npZSbedvlSMsOZCKKVrRzCVBqr9N45a96yPVdh2QYcqolPo-DyIZfjRVzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8CFboyOGUkuSKBRPD6R-Dmp4xsZUjk8Zm8RwyO6c8YuBkkRuI7i3uzBX6kmkZPbRKvsL5zwXT9ftZAgPMOEldTkYshMycnBsChckRTkE5PtkxeHI3D-9BkPvrR8IwNOirkRAkJ2HDnFhLqV-NMbkx3nxYvWBbE0mBBIipMtKHs-lAt4pCPCyoJGuU9abF37o6sgUFfDKso5BVYgYDYictPg6D168eVO86aXnyNvM6TeP5_Gh8AsOLWad7wHmMhgwLCuewZKRtnL8sFsh9dglRsn7VcYA7P7CBRLjTlaea34_JS94rWqjERUvulyckfe4d2b_i8BsMUUWkvg0uIzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0i9SGxG2dzB3Maav-8wzV07miugb6c8UgaAFbFMue4nDkyfkp0wmTJ3CAXfqg7TmEXH2_ITZiJ2sblqQr648jJYO29Hb7QgWrowqlLFDUP23AEL9C76PVnaLsPhoT-GwRpwiEsAAUTZJwDIIhHn0vd6-9gkAhrms29fzx2LvPxXD_Ihbo_xZKpNWWi2KHI6AwqX-x3Cbgt9nMNDsX50gbfYRUMFUdcNjFqZpFWn23HlAaFllX_cm_-dLju3M7DKPIhO6g4T_yr__SGopwCRWZw_MQXOrLvwigfbX3Dq_hKWrEXhMlojLBEf1oHKEzBA17nxFJTEx8ciwSv6WZIH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=JPMYj1eHj2IUo3tNAZ2787fKCTciHbOWszsshGeIS8CnqzjUD4P9wZZXDlOSyC6L5VZnGAXInj4X3MTS1mnK3Q6Dc-jqOX_oYYSewGsOOAa7XMUMZpAjMKle05-yvlp4BsdifSfClLP47Q5LDzDhQuW8Y_btiVTXvGNm2xxVx2OkenXadAIJSyHgM8VUCG5NdDFSkhgEbLf-C7MyQ5oVpSWIUZk4r2OexBSxrSb37ELQFdiunYBanY0_pvjYJmvDOfopfXYZqTntLCKm8q-JuPl26Ut6f3TcatLad7ANo5RBMWU3-Ea234ghOG8s7xsMNejrBNdq2qJRGhePiCJvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=JPMYj1eHj2IUo3tNAZ2787fKCTciHbOWszsshGeIS8CnqzjUD4P9wZZXDlOSyC6L5VZnGAXInj4X3MTS1mnK3Q6Dc-jqOX_oYYSewGsOOAa7XMUMZpAjMKle05-yvlp4BsdifSfClLP47Q5LDzDhQuW8Y_btiVTXvGNm2xxVx2OkenXadAIJSyHgM8VUCG5NdDFSkhgEbLf-C7MyQ5oVpSWIUZk4r2OexBSxrSb37ELQFdiunYBanY0_pvjYJmvDOfopfXYZqTntLCKm8q-JuPl26Ut6f3TcatLad7ANo5RBMWU3-Ea234ghOG8s7xsMNejrBNdq2qJRGhePiCJvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRb3BcrckhAkP-6FhcsVf5Ow5aBL4KIcdKrui71SiBL7Gocie06l755A9AiPP73Pgt4IRjcWLPUfIkhkhegr_fhZ0Ywcpr_c8-pJXdevY01GOgJH91RP_WUSIGcK0ysJRYEhPCmrcZMs_Qk0fHUHdw8AwClEMMpxnexsIVxzRGe5y13e2MObP26F8ui8X-_Em6fi4N11SIyxzOiyCxmjuhPcv8m2CWLL1VMMnzR9nElByQagDwJFHt3gxCONxVigiBou7-GgRxkIyd31fOWMwG_mwRwNKHe5LpGz3xcROooYUIfv7rbZ-wqAnBsIVe3lqCFUub3eeztYFFhYKpuUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXH4cpZ4b8SvzD4Vye41ukSx_xGFoJjZ5WUbawCFypplKWaSXFe9SXJyB4G7whMchAZBrVH5RBYyVJjCqlZuOsD8i9xYgffF35AhN3rcls_LQ5puy6s3beoOfqclhpFU28MjlkAdd4ObqLKjryqJluso6XG7kH-jMEOg_l-yVtx1IeHVENgkkCIq6b1FwAIcnpp1UdLJRs1tB5WeEcXbJWOCf5bCoRhyGgs9ZgdnyupjuyfuHQYDYW3G5xkkc60VRKgdeKCzAsQ8gadiuoW3BJ-E5bbed-FX8w1msMlgqXV-Owd-Zsrr8hrMUtp67l43wKTcUXThePBVVTsNgfSH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZtotjIBe6Fh-WhNYacDP56HkUJhtDcWRq1iQhuoQkmc3S5FGolzPvk7NyX9TkguWuvmJLH-2vPNPk7amMwZG2f7grCj23J3gopSjSYBvNTQ8x8CB48_p2Wx8p6pHTF1RIHu_6feRiAXSirUaHVTUsVioFQlYlAMCLsKedWkDLrog_syrGDx3c_QzXBDg_deYrrITgSeuQAoviqd2LrLoxphkSWynV_ahH9NUqCQI4UOVf2CqCq9sBymgvBifxRNd7R6X8QHHDYLXNkYRDKNfgi1hFnWs4hhaDRJHVlombAoF5hocovURCH-cnoch447DpskS96Fu2Pyz2Tx-_0xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTuuTXWMRj4sgOJm5wQitPwiVXnjft-mzHLXscl8ZuoWwrd-IipkA6srXxYC4lHiyBtGVQY_V7atIR2ELJFhnzZsC_JIQZ6JpgKFNV7u0lF89LgYgsfG92x8BHRucCoBeIlCPdLGz3fSKEJSwrrFY7OWy1XcYEwfCngCJpEiRz0EcK9wLH9QCAXQeSgi6ddvahyUZkMamU8Y0IraqiDt5c9Pg9kAVgyJsl2kCh835EeECOmPfIqjXoGEq5dfGACXfFnZYll0aFjfq38lur6Ucr4IR5GCq0MHMwVq_FhCbKwf9-1AlupG5NGI1vFi8t_c0qcgxc9CqCSAej_A1YTqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=eHFMVnt8LFCtzleRXEb5vt4fKQVSKA6YPsIX_otJvKKon1ikz6cHH-tOwmSVmMudsbMyLbgYfua0lCYdtd5pEEtNAA5bd4Lqpno_V-4MpNnwfDLBDRA-gWypsvbLscKrVrldcXh6B4gnF8XAWBzgxhpBFBLtNDea-2JZ0cj-KQ2e6MgHDk0McVGHXhXFFhWaZMZ9vFmJ9PQ628A5SUMz_TSZAAizx4Zl93i7oj4Gw2GyEEeyWYXnogGP-HijOuO60lv7zHgaXrzOtvz86UUES-ORDYbYEFcpF9S30Zb8iOnJ3byUbz4lPOx7mz0G0XjAYxPZJaChtBhXZId25WIfVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=eHFMVnt8LFCtzleRXEb5vt4fKQVSKA6YPsIX_otJvKKon1ikz6cHH-tOwmSVmMudsbMyLbgYfua0lCYdtd5pEEtNAA5bd4Lqpno_V-4MpNnwfDLBDRA-gWypsvbLscKrVrldcXh6B4gnF8XAWBzgxhpBFBLtNDea-2JZ0cj-KQ2e6MgHDk0McVGHXhXFFhWaZMZ9vFmJ9PQ628A5SUMz_TSZAAizx4Zl93i7oj4Gw2GyEEeyWYXnogGP-HijOuO60lv7zHgaXrzOtvz86UUES-ORDYbYEFcpF9S30Zb8iOnJ3byUbz4lPOx7mz0G0XjAYxPZJaChtBhXZId25WIfVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ekSeYmRACPudYX0kFFO6E5Po1jE81FOS0wXOoqGAX8kFPeSR1pGr_8zwGqsUkfbzx5RP36Xe_DZijoH-kjIiB1hksDR43whdXdH26_kScm6-1n2Dm5JnhzLT94iEKDf8bMwRoCYND_DWF63l3HZezDIVgQxHBm1AMs9JJERf5AZyJKcsovQztVpxO8Rdqm9Ln7oLaMds4yHEfsXe1otRLb-shQrLYWvpVLsH-PpZAf4Y7NWMZ_wgSH3QAOPrQPG5vZNYZFIpFoI9rXPq_DvEEkeGaeh82NiL6bGjsu0DWikbz9u-8gfpeEJxJPz4vJoudKn78RWL8ABFmtqdX-TXgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ekSeYmRACPudYX0kFFO6E5Po1jE81FOS0wXOoqGAX8kFPeSR1pGr_8zwGqsUkfbzx5RP36Xe_DZijoH-kjIiB1hksDR43whdXdH26_kScm6-1n2Dm5JnhzLT94iEKDf8bMwRoCYND_DWF63l3HZezDIVgQxHBm1AMs9JJERf5AZyJKcsovQztVpxO8Rdqm9Ln7oLaMds4yHEfsXe1otRLb-shQrLYWvpVLsH-PpZAf4Y7NWMZ_wgSH3QAOPrQPG5vZNYZFIpFoI9rXPq_DvEEkeGaeh82NiL6bGjsu0DWikbz9u-8gfpeEJxJPz4vJoudKn78RWL8ABFmtqdX-TXgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPUrFDFCCxxWwMJqFsWOVDK0sTMN9zttSrhHxzsfqMgsEA_pmA7qa44XVX23zjsGE2rvm4CzkQLDxa3FLwm2f4GD83bEcs1N5fjR56GaNhqqV9uxtSEP3RP1Q9CQc58sKyZG2pdMJYphpsY0IW0vYCSjTLRO9xfAvYBZ8KYFJXUZsEfMSezT8EgpW4M1JArIYfptDoH4XpK8TmN2gSQUjOkiUhgsG-wWi45cb3UCszTFwED5NJ-mUjXHsfLITX6rKbBzaBNpCO2HmlGzT-EOM7hBLaq6Iu03PlNL9BOz3_4C4HNUFxSHUFlpJud43p7xSUC3UY3gupFP5odfeJJw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSB0MIrLDkLrYyP645YTK2K1H_bry7M9OCVFQKTHNiE9g9rVfE4DsgS3zgdzi_7oB8SlbCLm4_dDDplnKZDb9BkqKxL1-SZpRa7th4hiNGYCidJCsHunqyFBFk8U613B_QvnwcmWblZuwMPK3_3j30RrMzHOGnxcs-88tm_YAn2uGhaQ9tM0vK2f3d_NW5Q5xqanIWNKuzlQDju79cjhkVbeqMOnR9olDKsyb0hpOgf_J8IaS7LWxjvGWbld24M78mI2Xs-8GkKg7Id65Oj8AAYwxuRrJjP1ig14-Z2HZ3yFx_PHM-E3IO8R4Z81J2xYvBTkymynWSCquFI2P3cbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrPMMvlN4zLsoMWuk4DuQUMPKyMK7w1bz1mIRMs2UDJyAR0uSZK58AADq9NnX6hfsCkolR19uLoTUjCLrdNHN6EgA-hzk_GCeAtUCiabaMCVhGQ0zFUH-tT7fR7Y4quk1-MThuyn-va-urs1aylmtIKuO8YA-RLtdbsE5sD83QbcCH5HYEWjM4RpGJzLK4bIIUIJBAqoz9TzaJcZL3OWiO6Nv8mI5pbbI2jZLXKVVQ4FGJNiUzKyf3ojFi7w3irvFZjpwWFnaWfM6Bvu-6qWcylfNj9v_nP08dpY6GTva0_ujiYWjgF_NpiKVwM6rspeNMlDE5juHrhXDVoVuG5mWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
