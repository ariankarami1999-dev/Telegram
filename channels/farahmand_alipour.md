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
<img src="https://cdn4.telesco.pe/file/a6mL2sy2jo6wlKXsUQ5nOIQaG0FskIDaWqd2KBJueFiif-h4Y5Lp1HPG3XRURX1edTFUPPmOZDEGcdzkSEqY1K8xYK7Iijvyjhh2tRhmVfwGjYTSOHwBcu_pQ9Ofz_a6IRzvdfXzfcggaYEXAmG0VwvZoheOVpv9qMTRGktlPjHbWD0u0cqejhRm4_h8iVaanCXLAorsGAIDPvTTzqKtkpLe1cTd0DonRMrp_6ABCktyqqm6lBMmrEoqzN1VpjAYnNt1ogYMIYXu1OZPYFFsjKcS9wCqrQ3awRHztK3lNg98a5C54jV5w2Sd4icgZPxdQzBPcHBtdeDIbjhhtqL_ZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SPoBo8hg3l-YY22p1vXygXI_QxeEPfH9rp1iir-W9twoD-4StLDUzlbRWBUqhRA5zdif17SDqn5mmdDmykltX2Cm1PiY1oO5mCqLnqqZkXVAps-QvbGGa0uZ_UTQq0W9_-SyhZFKx2MSkTTUOhw5ba5QFazfgIyWk3sH9fw62ExV8RHtalc_8RH_hX_LDVKpgAZiFX17HauuhLCCUkI9SRJxssEzmqxoYJzd7Lj0NZZzN_td9Iv30TIiuz_vVcfdNoubwz0RedlXaq-eLh56QeZPs2p9GDLPsSIE1r1fzBjJPfE4L6HabM1Ba04t_tBrh1FcUvpl2dAKMshM7BFAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SPoBo8hg3l-YY22p1vXygXI_QxeEPfH9rp1iir-W9twoD-4StLDUzlbRWBUqhRA5zdif17SDqn5mmdDmykltX2Cm1PiY1oO5mCqLnqqZkXVAps-QvbGGa0uZ_UTQq0W9_-SyhZFKx2MSkTTUOhw5ba5QFazfgIyWk3sH9fw62ExV8RHtalc_8RH_hX_LDVKpgAZiFX17HauuhLCCUkI9SRJxssEzmqxoYJzd7Lj0NZZzN_td9Iv30TIiuz_vVcfdNoubwz0RedlXaq-eLh56QeZPs2p9GDLPsSIE1r1fzBjJPfE4L6HabM1Ba04t_tBrh1FcUvpl2dAKMshM7BFAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0xQQ5psxeqFvTMrgyDmkVDUMBJxMNocfGomcmspTEPbhQQlAIyFQMipvBrToVYlnXLfBVI-PNOxMvj_G1Jm4h7QRoJRsyWTN_7sNmE1o0HiMKXZ3bBAmqQz5OXwfPi0CArOF466Qa61x-E_58YtXuupK3IEE-iS6Jvzzxqh041oIq-Hyq-QInk7_uHkFWiGR9UULYYWyOaOm2-yXlb6sBxI-LmUOB-1ajxvk_tUlu1LXL3MpSCb2xhdPwwAz1uJ35v2EKuOL8Xulv4gi69q9ISZeLJdSrgBvFdEb-Rrlw9as65y8peAaIUWeoWCbHgF2jfxWeO71sLg0uNyPY231Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mKhnO-P0WfZswCirHiPHCiwSLIlM1zA5MkYhDUzKtdjLHpqQ7eeTNb4cqnZlXlkIS1_5elacOVvdTJkvFJkbdJKgtlzgn2XoJF0tXr9iZO9xpaoB3IUQga8O6d656DZkk1te5qL4yn25xtZANYBtIBUoy-dKHNQza1aphWLyjFZzcxGfjB6s31a1BNS7M2u-A6q-vGiB2HEuzcmRmulxHas9nY4XJIHDp70YzerAi7tMdv62nf2d0CywwwLpaVlXPrAX3E1qKrWEZjxjXxTBr01ouHO-trZ-g0CbXINZGXSh_E6d3SMuT0LjXGcbF7I-LplgY4OWCZT98_TpSaFZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mKhnO-P0WfZswCirHiPHCiwSLIlM1zA5MkYhDUzKtdjLHpqQ7eeTNb4cqnZlXlkIS1_5elacOVvdTJkvFJkbdJKgtlzgn2XoJF0tXr9iZO9xpaoB3IUQga8O6d656DZkk1te5qL4yn25xtZANYBtIBUoy-dKHNQza1aphWLyjFZzcxGfjB6s31a1BNS7M2u-A6q-vGiB2HEuzcmRmulxHas9nY4XJIHDp70YzerAi7tMdv62nf2d0CywwwLpaVlXPrAX3E1qKrWEZjxjXxTBr01ouHO-trZ-g0CbXINZGXSh_E6d3SMuT0LjXGcbF7I-LplgY4OWCZT98_TpSaFZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW6ht1rM0z0qXldFm0P5j7hIP8Z0cHh1z3HpkOu-ZFLqPzs1TextuNY4bqgYyszVwc3cG8nv6GGXRQlnmowvJha5F3mF_ifvs5oEQxvunkiPAMjdKhFijzcYOmXPI4e9s7yYPGEyw6lJHP1WuRm-ADyOdXSy8AqtfsIyiVSyILncGJb_bavSPjBq0d43WQjQaQSrAPCKOt94nmJuiTvmnR8xfRxiKh0JrM4hdGVhQes-yW23RuMn6bDc1rMoTotvmQMnNZg4OkLO2TY8ssgfhDWrjEa64njfABOoO1FUGBeKSTAnT3p_2xdjQH2GGp6vB5iSiVgdLD-fEE0JW4ntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dryqg5dzwce35UWuXMd-L7cxlkB5-d8QhO59xSWLD4wXvjZz-IzLQNrb3K6lZBnznnIqtS8xpxtp8Cbfetnq8lqWlX2SNCMlmlSQxFvs-by3xcwVXfaeCF5k2U8TENuIxB518DVj3B8y54Vax8k1-4r9Aru-dtMu0pCzHIirIt6bjT8OXINoek8QCP9w8Elw8xgmHaNKBd5d4TF0Kf-M9y3oW3rmTktJGBRP0vt9OTI8uNr8sLwEnIsLw89QkU_CMBq3eJvWE0ZJD_5JU8WDBN-y9IB9HNu5IU81eFbxkHAO7yTq0ATkRrX_wBGpCZRxS5dr1CSR0uT2Emj_saiEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=gyjn5QvcuIjSoX_UwijiRUhG8Iqp7iXp_4cmSCXoEBBCV2FFE_opoBU67KB0s9vjKLtCAUFZsMcws8QrwyoKPtq_56vO2PPDIsNh-1-gYKA3S1fvb7fctFxUal5hSn88cjv-U5ePnUq3lICL4zsiJmGctf2EskrMZCY7AimCOYABzMyteu49t1aXsPxBIGed-Y35RLxOKqshvQZe2MvR43bYmDDyIldenRS49qEroZuelXTK7_EyIT-tV1JH1g_wKylw7jMNO_rMt35Of45Njf-1W8V_tQ5B81kM9ctRthDINm-AkT1OdffltppzxwATrEdernGErTTEDrmH24pCzYv91VtPgbMAoDpQXo117HwxZfR6xSxqpi9E6vh7-evwjDHzjHYijnZwZjsokCiwJJMrX8HzwgYpSKum6vr7TaVZNHvHhAVK0_Fgc0DXMsY3EFRHtPnew0o02v-pKbrbaS9BK50BaA30WornYviDzn9jZ2049hq_8bpbDEdcT1WKVFGrOFfTs8kVq6iIA2Vs-MZfXVwiRqgNdigUqzGV8-BCz5Cm97GsQEbOaHD_l76TRcB4MNy25ChSRci7Xs9skwm7s7cT22pgjINxbE1Y8JJLpwbvLh59uURMsIpO1mKGfVu-KQq4FHW6qH5ep2ErnHUmMkrwazwcwnxcGg2BgwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=gyjn5QvcuIjSoX_UwijiRUhG8Iqp7iXp_4cmSCXoEBBCV2FFE_opoBU67KB0s9vjKLtCAUFZsMcws8QrwyoKPtq_56vO2PPDIsNh-1-gYKA3S1fvb7fctFxUal5hSn88cjv-U5ePnUq3lICL4zsiJmGctf2EskrMZCY7AimCOYABzMyteu49t1aXsPxBIGed-Y35RLxOKqshvQZe2MvR43bYmDDyIldenRS49qEroZuelXTK7_EyIT-tV1JH1g_wKylw7jMNO_rMt35Of45Njf-1W8V_tQ5B81kM9ctRthDINm-AkT1OdffltppzxwATrEdernGErTTEDrmH24pCzYv91VtPgbMAoDpQXo117HwxZfR6xSxqpi9E6vh7-evwjDHzjHYijnZwZjsokCiwJJMrX8HzwgYpSKum6vr7TaVZNHvHhAVK0_Fgc0DXMsY3EFRHtPnew0o02v-pKbrbaS9BK50BaA30WornYviDzn9jZ2049hq_8bpbDEdcT1WKVFGrOFfTs8kVq6iIA2Vs-MZfXVwiRqgNdigUqzGV8-BCz5Cm97GsQEbOaHD_l76TRcB4MNy25ChSRci7Xs9skwm7s7cT22pgjINxbE1Y8JJLpwbvLh59uURMsIpO1mKGfVu-KQq4FHW6qH5ep2ErnHUmMkrwazwcwnxcGg2BgwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-dheHcdtYht02c-arrytuq_OCJi8VcLv85FGF4J4qcGzJcI1NOeOhwp3qfIhBv67sPZwYEG8qBWC4-zHMa25D4NdQg-SAZSJrVDXFWjIPgkXG_PrgurePMJayI5CJ36RaV3rP7p5O_26eItXLFS_aXRF6m5r5dykUvevjk_ZYBVTEb_An5fHJFKeUcdP_MB7NlSLL_f28lDJIlPIVDVGRAPFLEwCD1LbMT-vGdOwbX2R3Pj5HA5a7P8ftIFYK9I9ktJG9z-B4Tz2fwgmNOjcYlc6a8O74MugNZZHeO9WdjK-_nZ1FadL325HVBsfb8psEa0C4viFfjYg7UjOmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnAhhrWX8t3FMbU_GfrXbxWhLylYb6yN7jmOLPbLk73_pn6MVBNi3FhhWYUhBO3Vrlf46VNBruH0Mf-S65Hi-SqbJX-aJ6vXK4fDcegyAd12RQjN3jV21XkRPpbP_oFGv0yGPDu3teQuEld4yeZZpv0Vtn4d2nhVVtZXfnQKK6W4AlTtOAyodgxnt9jQTB2u3YvUiNYfX1soCh2A11EI0SV4EiHFX7X49Lr3daPW5ejS5UIStUqiqRG77zas1I7WZF25iaZtJEY-Qpc8z5TaIKP41u2NeEHeNbhpZ6VG73eVuC5jKkDXQOomXlRFYQh5AF2huiA533WY0JQr7NV5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=pnYYOFK4y9NRx_dATbU2AoMAPJdFj8nPm3Zs5XRJQhGDkFYI7UGV9JtLgjBT6RKDXcrAvNkZzF1pGo3zuMEevA2Em_ktvieFGLMk5TiH0a3Kf8ZwE6C6GPhQEc6ZQkNQX51LU3byoBX6vzDretl5NfDYj9srREuVB1j9AMNIKoYdBAUn8o7K6A4f0eFayaFL1_GddKmv8uB24ynJ8SBjoFUUCq6Aa14VvJ9_r-n0A4BLbq9G5a0vhX1NWZYi1_2KMYTDf4LiqNm3ZgzwN0h2ld_p67HBdvJfMs88iAurlfVJJj3Q3KUcWsZifHSWLNtCBYt74OwIza5mZ0ATa9GP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=pnYYOFK4y9NRx_dATbU2AoMAPJdFj8nPm3Zs5XRJQhGDkFYI7UGV9JtLgjBT6RKDXcrAvNkZzF1pGo3zuMEevA2Em_ktvieFGLMk5TiH0a3Kf8ZwE6C6GPhQEc6ZQkNQX51LU3byoBX6vzDretl5NfDYj9srREuVB1j9AMNIKoYdBAUn8o7K6A4f0eFayaFL1_GddKmv8uB24ynJ8SBjoFUUCq6Aa14VvJ9_r-n0A4BLbq9G5a0vhX1NWZYi1_2KMYTDf4LiqNm3ZgzwN0h2ld_p67HBdvJfMs88iAurlfVJJj3Q3KUcWsZifHSWLNtCBYt74OwIza5mZ0ATa9GP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=iSPd0K-xBr_hin5snjZEfSjIgOpRS1sZmneVAbf2rqC0knCRfHLllRfWaneqtTImIIWNVWbiS8QfIGQ63pdIOjIPo1Rrvm_O1cmiZy_LcvaJ7pMSoFht_LwHkN3LKKch3E3g9XQhfHBzwxzQZ2P3EydsGtmrZaSCQho2OyqfC_7EdHNtUjzqX-Vys6XbTO354qVwpSYDy9dhV3mtLIZ7n57kN9lO1vz6Alpm5BZA-1NQNs_F4665qW-rVMBszndRtHvJT68SohA_ODWCVDpz371c1_rXU5kJe8CEs1t6FgMhvodcrRIwVOTudbqKe4lnAFSonpGajPGnoDT0d21H1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=iSPd0K-xBr_hin5snjZEfSjIgOpRS1sZmneVAbf2rqC0knCRfHLllRfWaneqtTImIIWNVWbiS8QfIGQ63pdIOjIPo1Rrvm_O1cmiZy_LcvaJ7pMSoFht_LwHkN3LKKch3E3g9XQhfHBzwxzQZ2P3EydsGtmrZaSCQho2OyqfC_7EdHNtUjzqX-Vys6XbTO354qVwpSYDy9dhV3mtLIZ7n57kN9lO1vz6Alpm5BZA-1NQNs_F4665qW-rVMBszndRtHvJT68SohA_ODWCVDpz371c1_rXU5kJe8CEs1t6FgMhvodcrRIwVOTudbqKe4lnAFSonpGajPGnoDT0d21H1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=t7NrXgUd34IgNm4sRvA463VAdceqBWdAN3rhxcLe-yHWcnkf87nTyRl0bxLYnPHETYhDvBngvaeoimCE2gyCxCy71_fqSIbmHrimrqAvx_FnsPhipRYAIEOT52c_teu4C2a-qFx3Vw6btHkF91mk0gnB4NQSwCNhsr8YTWpyF_hOmhOH4qkXrSpvSw_uA3BqlS-Q3aSfpvdg1rEdJ-8dpgh3v3tJTku8k7ni_qDVNuUt40wl3hqlnAg5QVUr2HqpSOUanQuJwkpcf-YvCrz91nBy8I-x7h24169u2EPBxCwnEcMfTTikeIYl1PUhCYkNIkZ1ij2AlfzWdIJmRQ0d4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=t7NrXgUd34IgNm4sRvA463VAdceqBWdAN3rhxcLe-yHWcnkf87nTyRl0bxLYnPHETYhDvBngvaeoimCE2gyCxCy71_fqSIbmHrimrqAvx_FnsPhipRYAIEOT52c_teu4C2a-qFx3Vw6btHkF91mk0gnB4NQSwCNhsr8YTWpyF_hOmhOH4qkXrSpvSw_uA3BqlS-Q3aSfpvdg1rEdJ-8dpgh3v3tJTku8k7ni_qDVNuUt40wl3hqlnAg5QVUr2HqpSOUanQuJwkpcf-YvCrz91nBy8I-x7h24169u2EPBxCwnEcMfTTikeIYl1PUhCYkNIkZ1ij2AlfzWdIJmRQ0d4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av-evXXpTzoGtnm26vJgdujpiQ7boD82rJ78OoRrxjATLKzNU515ylj0CDyJsyFQsAaN2ShMXHNUojIESXB37q4AErKFgRA_jtu7-udzRfhc2K0wpfJNb5qCwQd7YoFc4CsflFA0451GWDdr9ehfoD7uxCy-fjxjIoFwvYVJFxghPFI2gIEWIiBKst-qJHYeacP1hTIieIeVJV7XZonSCyKkiltYT41d89CYI3epiTNHfdcT1NLTncvQ_Xn9_odu_BrEqhOzKLp--Cza7yDJyJhUG1NDfnHzsC9bug1jO8X91j4McKphnDjav17vls7DXUYNgBKYuHOY1t0yldl2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IVM-Tz_nPZY0CRX2B0mUZqNc_f6KIzaqanysqO-sS9iKmbWeZ4F7OXnNVM5H5A3-0uMazZ-18IuTkOR7qMtu8w2QkkNnkoDZUhlCj4ORUFaZfm2OqpWUd-6xtO4aYlwYlXblisC_gyz9jPEhPUhdrNNxITm1TWVTibBadxN7yCRpOLWl3beMBU05tSyjhJVTIYGH9hWjMJwbKis8k_NHkqCvhoJ0WLbw5PxDcFjDjEWxPncCAZQlOpzSJ5FsU0FGLfUH6Gf50MmxCqlNEhA_r4xVGU69OAAd5pECW7B9KI-5Jmy2AB3jJenvb6arxynTkWGkpARQj3MPZ_6sHMcLtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IVM-Tz_nPZY0CRX2B0mUZqNc_f6KIzaqanysqO-sS9iKmbWeZ4F7OXnNVM5H5A3-0uMazZ-18IuTkOR7qMtu8w2QkkNnkoDZUhlCj4ORUFaZfm2OqpWUd-6xtO4aYlwYlXblisC_gyz9jPEhPUhdrNNxITm1TWVTibBadxN7yCRpOLWl3beMBU05tSyjhJVTIYGH9hWjMJwbKis8k_NHkqCvhoJ0WLbw5PxDcFjDjEWxPncCAZQlOpzSJ5FsU0FGLfUH6Gf50MmxCqlNEhA_r4xVGU69OAAd5pECW7B9KI-5Jmy2AB3jJenvb6arxynTkWGkpARQj3MPZ_6sHMcLtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=iVVc5sGXBeFQzX5y9yqR1eXnI687gS4mET0gHPqltHHnOujaG49awrGRbWHBuXZq_dYfQ76-Lk38bZLjYwTcOeucJLlm2gEFJEvW5_nAqs-6mP7JR5s8Rf7oqHaU_CI95QQKwpWo6wmFX-_AcMDM3rXZ63QzaVpq_ud0ehsi8zDlRvMIBa_szJ60pfuYMCTXzttlNVtKBLKR8MdbzM5zaYX1n8fraCMlNf1F4yGndJCG_RDq8p4iGyI49Xw-cYIhSDxiX7l8RuYN83odCY3wW9f1tQQLSP4w2dAvR701wPAst1sYjXfF_jrQ5-adAMaUY_zTTWe95ZBkKAjYV-Rd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=iVVc5sGXBeFQzX5y9yqR1eXnI687gS4mET0gHPqltHHnOujaG49awrGRbWHBuXZq_dYfQ76-Lk38bZLjYwTcOeucJLlm2gEFJEvW5_nAqs-6mP7JR5s8Rf7oqHaU_CI95QQKwpWo6wmFX-_AcMDM3rXZ63QzaVpq_ud0ehsi8zDlRvMIBa_szJ60pfuYMCTXzttlNVtKBLKR8MdbzM5zaYX1n8fraCMlNf1F4yGndJCG_RDq8p4iGyI49Xw-cYIhSDxiX7l8RuYN83odCY3wW9f1tQQLSP4w2dAvR701wPAst1sYjXfF_jrQ5-adAMaUY_zTTWe95ZBkKAjYV-Rd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSw__rW-AWNMFjqVgUq-XYjHyQoChaYZ65kOqKk4l_0Ips6AePgFZemNONSHDCiaXRawg-LoTG2zekcwZUtxQBDd0kL_dgGX6friKzdDlVoRzqCRboSXZcNOzzIrw1lzXVHVtBpXDBiw4a7KD95rPinzS9kHthgg7X_KMV3QqC1rT3cLENE7YKwEQpYlrwODdFMwCQR0hA2C3QlJaJd6Xx95DB9Wg33djRxC2Orh_HC9x1IilgAJvQniHaJwnFOGPS5uf7gizkI5Tsh2oRV-vPIJSvWn3gZj0OsHG7utu7OZ2KiOeBq0fat_h5vBohIuJvQzdKXEFNvFlYOSkY0Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=LCHK85dcc8WgR7tEBcMivbadK04KzJoHQnenHlej-SAmRL2Bf6w2bwf9dL7IF3t9dl7UIyC5485FRWpLqmg-VSnEc5btqf3oTsZE8tORvR3LlNJ3U8Gm_rWf5QvJeBsG-hVl0R7X6eM3-A9TqIUCT7Z3LkUFZOf9aoGfsZ83tQTac8sp4vV3yhCLJYL3pN9Gv42lAHhJqTj_2EMddjp7Yhu2E_tudECObY29jA60V_lzOtiru3cL9EqmP7ZDO54udggv9Jru_QGFNm_sB6M8zcTCb_4lO57JQ01Tua3Yc3tGxSshsATG5uTUZZh09_OvySMkOf6lyv3VwaS8roXDZpF9prpfeCnrTmlD3RPsLhVsJwoAJQKz82MvPSKioqD1DYjbtJlaBTkdRMBpYdWlD92BBQiEugpdFrhlWxeXJl8EiFEjSyGHPeFC1Op7W5_SPBwIfnLVGJGmzm73pMkfnl4fZFAgbBMYjhg0030DEDtRBMKMYkMzjlw9pYdfJ9ArRvneysWO8uVeaoB9I2gX_fXFUgXbertVNulIycOx8Pv5EMIu5sg9TBNsESXuuUQm2rExeA0xd44nIyJpLX5BQ7rDvB8AQkrlpaG52daKGE8Ahj-_hndRNh6htAuWNiZ6uTRQda6O9FHL0WZZ2XkmkE1M3RNgu5DW9zwc9zEyuN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=LCHK85dcc8WgR7tEBcMivbadK04KzJoHQnenHlej-SAmRL2Bf6w2bwf9dL7IF3t9dl7UIyC5485FRWpLqmg-VSnEc5btqf3oTsZE8tORvR3LlNJ3U8Gm_rWf5QvJeBsG-hVl0R7X6eM3-A9TqIUCT7Z3LkUFZOf9aoGfsZ83tQTac8sp4vV3yhCLJYL3pN9Gv42lAHhJqTj_2EMddjp7Yhu2E_tudECObY29jA60V_lzOtiru3cL9EqmP7ZDO54udggv9Jru_QGFNm_sB6M8zcTCb_4lO57JQ01Tua3Yc3tGxSshsATG5uTUZZh09_OvySMkOf6lyv3VwaS8roXDZpF9prpfeCnrTmlD3RPsLhVsJwoAJQKz82MvPSKioqD1DYjbtJlaBTkdRMBpYdWlD92BBQiEugpdFrhlWxeXJl8EiFEjSyGHPeFC1Op7W5_SPBwIfnLVGJGmzm73pMkfnl4fZFAgbBMYjhg0030DEDtRBMKMYkMzjlw9pYdfJ9ArRvneysWO8uVeaoB9I2gX_fXFUgXbertVNulIycOx8Pv5EMIu5sg9TBNsESXuuUQm2rExeA0xd44nIyJpLX5BQ7rDvB8AQkrlpaG52daKGE8Ahj-_hndRNh6htAuWNiZ6uTRQda6O9FHL0WZZ2XkmkE1M3RNgu5DW9zwc9zEyuN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyYy9Cuw_RCkPn7mPxkgwIjIsWwZUUr1we-s3J_kG2PVlEKp5xIdG3W9UVvNdnsi1YFXE4fLz3XYD0SyJWLvtze3GtUZm-mx6J829LZ3SGNkwxB_82G1BNACH5kpK6TzW-EuCSZOCU5EsbUTABmyS7qDLC4kJw2zl20xkiWLlC9KSXqD1z96r4s0ZF5zkyIpzTWGL4dP3Wxmq9pc2s411bnjzeRTZSJ7FxG-nX5eDM7aOcr4lcgIzpARGh3fMCPPT5tojckJFPegE-0NbavEspW5rq1ThnHFU35scqNv5rOXCb_46d5dpxt9ixdPPi7qmnw1iGRGM3sJtInr1j97Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LZsX_of0zE4xTHqp3JzqlsMp9BsO-z13_CEw3qo-wKWEBhvoEzPLJObQXWeLC8p3InsN-4qiXm-CZL4RXPNJR3k60tnjNcg6e0EdNO55_OW-ElJyP-DeyvpGoQHGO0laEptYELKmuMGeXpc6DLRgxV1AP6iPnzi8S_uPnE9wF-d4yahSMD4ZZPSxF-3J4Ly7nqPfEACFsvxpEdYPel2efrqW20Dsbn-3cS3JwxhIFu5FLnwD_B7vb2JRxyFVQGX7GIXlH_c5DeJHIEl0i6Kkfs6zZTvICHv6J-K1ABOysKIC_QFwTg3PsXppWgavaaDZTdMBToxtMUkipIF0k3aFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LZsX_of0zE4xTHqp3JzqlsMp9BsO-z13_CEw3qo-wKWEBhvoEzPLJObQXWeLC8p3InsN-4qiXm-CZL4RXPNJR3k60tnjNcg6e0EdNO55_OW-ElJyP-DeyvpGoQHGO0laEptYELKmuMGeXpc6DLRgxV1AP6iPnzi8S_uPnE9wF-d4yahSMD4ZZPSxF-3J4Ly7nqPfEACFsvxpEdYPel2efrqW20Dsbn-3cS3JwxhIFu5FLnwD_B7vb2JRxyFVQGX7GIXlH_c5DeJHIEl0i6Kkfs6zZTvICHv6J-K1ABOysKIC_QFwTg3PsXppWgavaaDZTdMBToxtMUkipIF0k3aFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atcOf5htmkqb-YTq1EjLzxzlgrNOhqWG3il_iCR5dqoGRX1EAE9I6wFBv4UJbc52p9ESV4uRpR9-zWArpqoBTbmUO79-UfK3gsLcCWYsT9DFiaaH58kLAqhNDcC2lLWjqtqbsogf0XpXKV_0b28N4NMkirIJTM8A2sf-stcmVc6QFmyepg6XJOf-3agRtHEUd7-OR4DU_HvnMGJPqEATV9k0wxXQYAZMLCKeawTbdcMkBIyDkl484qDXgihpZHAI0XYGZNH4w-daf1pCm989QlvTzcYtuzonVcKMMhpu-fV81KjHOKCoh-6C4hq4ew6tGSeQ7xce8ZQZAJLsT4IWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdphQprnEhHjAnGwRhI7PEthr3OFGsEyZfqNd9hcpd2Ji9b_D4blkcEIcFXpnnZE26isMJHrBinbIRByVtrf_OoU5POkehVKcLpTAvVzTZgICrE06wDIhuLugfRJ-uTda-Wz7Xmb6JURheajihu3rEtTYvw72Y4iat1x0evI8R-tMa8oY8MSYXg1FC0Rur1GZq5yrATDYUvNykgsAfD8wRO62e0czCtLF1pyHyD1XdC9XuuMQTnJXyCmMTQbP3EA-GZSLkHlTiBdUCk0Ise9-heMqcFhX-FAhQFi7KB7VbYrfevWEMMZHHov99M7L-DJLNdR4tbBBm7pNXvXKTERaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOHDCOdhJg0gML3sqMWS4QewWVYLW5bO96lX1-2jHTCdaVipRREvRb5C8xdgSctPOncnkOiJU6axUOG627eZ_wVD3ciYQ_zDLSGb4KwE3rZEDYc39RwfNLEEgbF5ncTE4SKuiRWE0ZJFMouT3sbd-roLDxoN1YqfD0JN89g5CKI5yKtJR-pyDDS3nFcLL7N87hd6QeZMKxy_q0hta-03A5vbEy_YY694kQcQss09ubs-GuogGXfT0m_eElP9wcddeYlS80EwlVUzfaHIY-K9Z41yDciHir2AEe7zWr-SGYONKNzbbsYdcEYOmJB66BnPp-5i4l4Uhw9YClELY-dzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=oGIGrJ1syAP92L8ezq23ZtR1pyJrfYBmBAuliFDJOuvoMlT_g9T5KLpLnFD0J2Q1UM6h9qEN99Uxco5E3UjRl4DcoYaUkq9JuKFlZRTRLQLOFg8aLd10g3KD1N6WccW5F3cpWXbpUDXlvENljar2a9uaUoQTJujx1zv4owS7jy5HaWVzjFEuwdc_3MZTsCcwSEo8htKMBVdprg7hmZY0gJ_UIPN9fLjrx_3awNXe3aZf8Iq3AFqAAItHAC9CCj0CqIbCbUwa7EnEsSOsq-1XfmiU4yYmiIVvZSqubEfDH9ncNB41nX1fRaUb4NHPmW1tLiIg4X5dPiX79l_plxlMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=oGIGrJ1syAP92L8ezq23ZtR1pyJrfYBmBAuliFDJOuvoMlT_g9T5KLpLnFD0J2Q1UM6h9qEN99Uxco5E3UjRl4DcoYaUkq9JuKFlZRTRLQLOFg8aLd10g3KD1N6WccW5F3cpWXbpUDXlvENljar2a9uaUoQTJujx1zv4owS7jy5HaWVzjFEuwdc_3MZTsCcwSEo8htKMBVdprg7hmZY0gJ_UIPN9fLjrx_3awNXe3aZf8Iq3AFqAAItHAC9CCj0CqIbCbUwa7EnEsSOsq-1XfmiU4yYmiIVvZSqubEfDH9ncNB41nX1fRaUb4NHPmW1tLiIg4X5dPiX79l_plxlMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWGZY62Dsan0_YSby2fCLWmqS5ZLCrpo3oA-_DT5SLwbk568DGIPd4vE0Xuxm9UI14gQLZanN3CLEDQ9odPXCMQhFfCj8rKVSy9O023nOrzX7eAWF6Bwt6BjU-HzkfJFpvYiFEFhmwpADvgUGEqjNw19DBS_xIq-8eBudz67fRaNPquEhOClyVHAjVsT4H7fEwh39B46gUfr5nI-j3XV4TXAMBe4ArFfTCo4ngHmUH21CUSTUSLxW1s2yYznnEVtvpOpKKh7nhWskCWtq7PLnYDXCYB2YOmTpMI3FPGaHpvUCEAx5Au005_RQMya-nDxP-B2p1uU33WF831CqO_rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5Kely9lunW9uktW9MCO66Cd_sHN5g3OZPlumV13_K_lLL1NB-pJ_UjgMeySqYXP-gUKdcYW2aNhPqTqOsJ9NLPfoaHLcLjocwkkN0RYc_k9u63seDI4r8R8UpVvzIxy10c99YZQYLJqnW5hhuuqwQBqeCWU0VYGP3BAZuLON17hKvjyiubfZ_i-mdOI4wZ_EokM4thGJrDLZgFvn9cNUwSHoHN7znhjyMEOtjAp60EPPOhJwfEtKzzOXulDdXN93UWlCEBvH8V4_PdqpOWdb-o-X0QF6VZbKLPR1QBsY6248dQ0AQD2ABTHAsXzJ-gVai-XenETdxGbUyyEjdxxpEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5Kely9lunW9uktW9MCO66Cd_sHN5g3OZPlumV13_K_lLL1NB-pJ_UjgMeySqYXP-gUKdcYW2aNhPqTqOsJ9NLPfoaHLcLjocwkkN0RYc_k9u63seDI4r8R8UpVvzIxy10c99YZQYLJqnW5hhuuqwQBqeCWU0VYGP3BAZuLON17hKvjyiubfZ_i-mdOI4wZ_EokM4thGJrDLZgFvn9cNUwSHoHN7znhjyMEOtjAp60EPPOhJwfEtKzzOXulDdXN93UWlCEBvH8V4_PdqpOWdb-o-X0QF6VZbKLPR1QBsY6248dQ0AQD2ABTHAsXzJ-gVai-XenETdxGbUyyEjdxxpEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=lFnLeILXmgGd_sxlhd640DXYvTowDlFvFzIg94mHwKN6NpS67h0TtPAyqDOBdf5pl5jP6yctIBAXamfisTxRlM1_EvIuRs4a9IjQABQSPbC8rWwq8JAQBdlgIdVQTMIX8syKnbSeNTF1qD0dYlnzex8sfY4A0vi6M_YAGQGLXXhokTjwHMj6Zt60QOrXucmi427U5GHuQ65ZZMlZ44ffRUS-h0Ydeg32VlaA1GnDDfU_WtlUOb4zbnq5YB75kdcCwY_wipEJ2Xv15LNKCGmCs_hrVQrtmMOQD_r9pYUwJEPp31EMUeMFGmbbWYlVkuQaD7ufSu5J8tGlds06_KGf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=lFnLeILXmgGd_sxlhd640DXYvTowDlFvFzIg94mHwKN6NpS67h0TtPAyqDOBdf5pl5jP6yctIBAXamfisTxRlM1_EvIuRs4a9IjQABQSPbC8rWwq8JAQBdlgIdVQTMIX8syKnbSeNTF1qD0dYlnzex8sfY4A0vi6M_YAGQGLXXhokTjwHMj6Zt60QOrXucmi427U5GHuQ65ZZMlZ44ffRUS-h0Ydeg32VlaA1GnDDfU_WtlUOb4zbnq5YB75kdcCwY_wipEJ2Xv15LNKCGmCs_hrVQrtmMOQD_r9pYUwJEPp31EMUeMFGmbbWYlVkuQaD7ufSu5J8tGlds06_KGf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=nC-U9zb-QiErm0JY4m51K3r4J1LS-uQnfJojPuotc7QxuSGKxDgZEq6vmnUb6wnkfboKxIfJYs-oB5LRbIz1NqENPRhxwoGoskchVdZ1KWuLKY-WVV_gmgFA4axMXSom4prO0FjAeSph4RGBKHqK7D_jZWH1rBeJQ2wIMWw8RH_9rNtfp4cjf0Kb6KNabV2twJHxmN1934JZFqdch_-rS3F7gCA4a6R2GaupUryolqSxB3ft_ZBAXksMMrX4CGnjp9cbq4XNiV0VBEOQmI8bmFc_Hs7OZPouyuOWOlOtXd6sk3xJ2S9fLG_yXgjsvU-PxI7pQwdDzyAg5e7QHnXmMZBbbWlXlDQ88q_W25Pi22CKe1CjlXcGN6JRrTtKtNnc8JeEHqI5CNHrpPdhahwS9FY1kwBCDXsQOZrFi_vAZE6ts4enkUkCQVA4dWwXPWyNP0dWS0vftkcpZQ1oOyRzQAQEaW142AAe6qjCPPzgqKlsmg8nfJD3z0hB4hWhGHPRTT0L5sPrXF8cIg9J9Rpd2yFJtw4HnrX3SZ7AaojhUHWhoJhivGNDUJY6yomA8JyT858fn2GcR1V7oEy6WW-bfx2mFxs7x6eOE8arO4GzXkYLzqt-WzcHS6hx9IBP_VtnaPJIn_V8pOtn9eLbiEEdqd_QPl7BcYCL7FlkDlqulcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=nC-U9zb-QiErm0JY4m51K3r4J1LS-uQnfJojPuotc7QxuSGKxDgZEq6vmnUb6wnkfboKxIfJYs-oB5LRbIz1NqENPRhxwoGoskchVdZ1KWuLKY-WVV_gmgFA4axMXSom4prO0FjAeSph4RGBKHqK7D_jZWH1rBeJQ2wIMWw8RH_9rNtfp4cjf0Kb6KNabV2twJHxmN1934JZFqdch_-rS3F7gCA4a6R2GaupUryolqSxB3ft_ZBAXksMMrX4CGnjp9cbq4XNiV0VBEOQmI8bmFc_Hs7OZPouyuOWOlOtXd6sk3xJ2S9fLG_yXgjsvU-PxI7pQwdDzyAg5e7QHnXmMZBbbWlXlDQ88q_W25Pi22CKe1CjlXcGN6JRrTtKtNnc8JeEHqI5CNHrpPdhahwS9FY1kwBCDXsQOZrFi_vAZE6ts4enkUkCQVA4dWwXPWyNP0dWS0vftkcpZQ1oOyRzQAQEaW142AAe6qjCPPzgqKlsmg8nfJD3z0hB4hWhGHPRTT0L5sPrXF8cIg9J9Rpd2yFJtw4HnrX3SZ7AaojhUHWhoJhivGNDUJY6yomA8JyT858fn2GcR1V7oEy6WW-bfx2mFxs7x6eOE8arO4GzXkYLzqt-WzcHS6hx9IBP_VtnaPJIn_V8pOtn9eLbiEEdqd_QPl7BcYCL7FlkDlqulcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=M7YYfAz_8qmI4ffXokQD4bod6ouGMowXdk6zK7I_s6DVgQSxxPVg9OnmucmB5hZHoWvPZUpVzECgjjpXk68XCszINJ_9V8lpil23jyjoWDlNa9Jw44iZ9lVq9q2t3lHLQ8Y_wSN0kQPc77xWS2AKdUzstlgdW2ccaEzloFfOVcY3wDQV5Y37-sn67hcIxZ9C_gYP_FFCbP3bSg3Gg1ahFmgM9D3Xc3c6Dhz4bNCUGToDS6hUrJxl7qOsNnhpbfOAu-jpCeJAH16Ul9fHyIgBjkiitTo4Sz7FGebIHRaovaMThCTlaOUwHpCcIcciSvVNHt4-RR9bZvBfM_YSWRsP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=M7YYfAz_8qmI4ffXokQD4bod6ouGMowXdk6zK7I_s6DVgQSxxPVg9OnmucmB5hZHoWvPZUpVzECgjjpXk68XCszINJ_9V8lpil23jyjoWDlNa9Jw44iZ9lVq9q2t3lHLQ8Y_wSN0kQPc77xWS2AKdUzstlgdW2ccaEzloFfOVcY3wDQV5Y37-sn67hcIxZ9C_gYP_FFCbP3bSg3Gg1ahFmgM9D3Xc3c6Dhz4bNCUGToDS6hUrJxl7qOsNnhpbfOAu-jpCeJAH16Ul9fHyIgBjkiitTo4Sz7FGebIHRaovaMThCTlaOUwHpCcIcciSvVNHt4-RR9bZvBfM_YSWRsP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCZVzUwZJ84E3oWwukb_pzVB-YcuY0xVF8Gnlo-5UbZfsUqiIXDChan5iDReJ-Fc4FjNZo2k8BFJlGPEy_tqcNmKCVf-jKSQa5O4aYi-4Qiu85UVQqvZY_ilzEXcEmwJ5icnqMfybWv0GJRW0tLjYMdDgjdrhudu6CnsoKIFj6wJPkGNBn_vi827U1FgGq-U_lVyLjKP7dnfUkK4iZJcnzy7XCX08ZUM7q_xLjYxkjtyz9WcvO2hVBbi3uMTHxHwv8CMg84e7kOUk-U6RrONENjAcEiPpnd9zrEisSRJqEsd9SvTqhd0SHju7Bb8sw89uimP0Bxkt2WIF2_iHKNl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=NrTG_xhLOST3MD2uenYt7y1WRybIlj_AFbguU2-s8baM-g0XcK06Zz7W9oCW0YrwMQQ8aOuuHD-RmDqwki7FHjAsVqz_SLZ05qpR29voUoNKpgwAKbDOhmzwvGg8hBLguWD7qEEgcOUqmDtHCg9Z2cMkLjcmdCo2-Sq3kRrPqitsrZUQjOlEnj5HY8OUjyVPR55wGOQm0q9qIGhAOtK50JelAaQGf_WLO15Oy3L7WbARWaxb-F31CyjvFRuarrZkX2-NsGHoxiu32tcuPUGuUqyzdAuxOu1c_7aMauwMp5uJ84c3QHZJl79H9FmpJGZgYEghGu-wKpSK6Hqvl6pOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=NrTG_xhLOST3MD2uenYt7y1WRybIlj_AFbguU2-s8baM-g0XcK06Zz7W9oCW0YrwMQQ8aOuuHD-RmDqwki7FHjAsVqz_SLZ05qpR29voUoNKpgwAKbDOhmzwvGg8hBLguWD7qEEgcOUqmDtHCg9Z2cMkLjcmdCo2-Sq3kRrPqitsrZUQjOlEnj5HY8OUjyVPR55wGOQm0q9qIGhAOtK50JelAaQGf_WLO15Oy3L7WbARWaxb-F31CyjvFRuarrZkX2-NsGHoxiu32tcuPUGuUqyzdAuxOu1c_7aMauwMp5uJ84c3QHZJl79H9FmpJGZgYEghGu-wKpSK6Hqvl6pOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=DAL107_MsWqJ25sEr4LZR47L1rcE7gcayPUpA8qAhgeXFljCL0wEPJ46-9cXAFJXrjvnr9hqiFKmVkhOv-N7pJ5uhLOJyzWTIm1K48tCueWMANCt6KNYILbKjknsirGZ9m1BvJeljOo6m0FbCwWmMFcbAWiYdArzzroO-52r7z08S-rsJjMOpctMamVeqREenLQZqwBMoWRrxV6Cfo6pw4_4E9yreQwUPqzon6Hh7J7MBrZ4bcFGPRpeOehStyyOVTz3-O4GKy-nCvz4Kd7ri6nYWpu_WIqPuOdZfHmBdGV7iBlV1db7TvtLbDdC-JWq_X8g3Xg5vJiSduiDaLJc_wUKewyEPc6Hu7XWVq2k6qfW0rdK69SlorUinS1Tx8is2DeD5hhV-eosVjdRUeqcMZSb1kvpUnVrcZt8jQ7o68nB2jcsCmRxQru2QykyD2zkZIP9lJO_LOa0z2SzcqI6GNj19bzvfY9sN0SdSefWkWT3Upb2dQlhQJ5p_VrQLvL3KD-NhlUwHYcJR2Xk4-HU15MkaScBBRt5zW6QiUr7_vinZpxQhzLZwvlQF4sJsBcI1DFpYGtP9_7fPlYchDb_bcgLeUZXrPZT268SRWaydCMozmk38UgHoiLrf43snptVIY6eB8lmOOOCbhyQseXv198Y3E3J5RebcPOBLDiH20E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=DAL107_MsWqJ25sEr4LZR47L1rcE7gcayPUpA8qAhgeXFljCL0wEPJ46-9cXAFJXrjvnr9hqiFKmVkhOv-N7pJ5uhLOJyzWTIm1K48tCueWMANCt6KNYILbKjknsirGZ9m1BvJeljOo6m0FbCwWmMFcbAWiYdArzzroO-52r7z08S-rsJjMOpctMamVeqREenLQZqwBMoWRrxV6Cfo6pw4_4E9yreQwUPqzon6Hh7J7MBrZ4bcFGPRpeOehStyyOVTz3-O4GKy-nCvz4Kd7ri6nYWpu_WIqPuOdZfHmBdGV7iBlV1db7TvtLbDdC-JWq_X8g3Xg5vJiSduiDaLJc_wUKewyEPc6Hu7XWVq2k6qfW0rdK69SlorUinS1Tx8is2DeD5hhV-eosVjdRUeqcMZSb1kvpUnVrcZt8jQ7o68nB2jcsCmRxQru2QykyD2zkZIP9lJO_LOa0z2SzcqI6GNj19bzvfY9sN0SdSefWkWT3Upb2dQlhQJ5p_VrQLvL3KD-NhlUwHYcJR2Xk4-HU15MkaScBBRt5zW6QiUr7_vinZpxQhzLZwvlQF4sJsBcI1DFpYGtP9_7fPlYchDb_bcgLeUZXrPZT268SRWaydCMozmk38UgHoiLrf43snptVIY6eB8lmOOOCbhyQseXv198Y3E3J5RebcPOBLDiH20E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdMX0QVDHhCSeAfcXfGtws0W2hdEknW9YUNWuzYD7TbQYqO9KdXI5PleeCXBwKhi94FSiPFWZMTDhcGNzBSBSGk8nlVFuG11gnyjC1h1sGjrUsM2msDLTOWeHCcxRDgmKRmOzeGay5sA2vwKfxWtEJ6qnco7G_mvI4IKT0uYqGjlVOU8voLjOJCBy1qXjdxiMjUHSJ7KLitSYDidSNjWMh_8ofCqdGyc85wVQSUjyA_cRAe2v6wvveH1AB59cLaEyKIHzsTP8pS3FxcFLP9GIWa4kMZ6dmlpmKQacyuXza4nUowmNK5QSWb61wY83Wytd0RpoI6A5smjpK1AO-hvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=EdokKn5Uvp0IuBDIkFqoxqX6GFct2LZR41XeG49BcqMeepdQzgd-3-5UBnyRhWIub_6aCsrnbIWIDkstZk4r-3dDg-jtrFGTIe0BA91hOorWQrhRnbudYjHe1dICaGi2dlTby_Lu_AmS_e2nLY_qQ9kUxRcApmE7K_8FBfdpmi_AdkZfq6wpcKnrH8nbJiYWqGArkRYtiv8z4oGiA8-76NQWugf_zqoak-gRcPpkCbGjN3DwmchZ4YVYRzr-IB-7xsipG1WUHFPEqnOe4LbgGoHEaEdygRBykuKfOS9GXA8bNbarKbLXwoocLnwlkvKXOle3XB0mg49fX8CIvB_-cjtI8Uk4u3EMVnRwRhf2a7w4iyd6OmfiU758sJ3urCowrM0c5_GlW55OEARCT0kkVpfxlVA5zwq8jgtN_jKL5WWM6YzjQgz6fuztv3e3IXxlY2vAASH5aTLktteQCueWmtgVsv7jDlKJWLRxMKAGIE7P5ILnvgqL0PcXidTM-rphilFn0uYdcWy1bgIZdEyNu1d4MRDzPUNJuWIsgaglKQAlqgIKw6dWLVISOM_vbQrN25-WoSUlZMPy61y1RFtzQYnDF4DJ6Zoff9IUjX1WOyYGFC5_M-j96BwbQcqGrLkhCY7xdbrcmrdaIGkCRLdtEneQmrqXyEWl3-aln7IX3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=EdokKn5Uvp0IuBDIkFqoxqX6GFct2LZR41XeG49BcqMeepdQzgd-3-5UBnyRhWIub_6aCsrnbIWIDkstZk4r-3dDg-jtrFGTIe0BA91hOorWQrhRnbudYjHe1dICaGi2dlTby_Lu_AmS_e2nLY_qQ9kUxRcApmE7K_8FBfdpmi_AdkZfq6wpcKnrH8nbJiYWqGArkRYtiv8z4oGiA8-76NQWugf_zqoak-gRcPpkCbGjN3DwmchZ4YVYRzr-IB-7xsipG1WUHFPEqnOe4LbgGoHEaEdygRBykuKfOS9GXA8bNbarKbLXwoocLnwlkvKXOle3XB0mg49fX8CIvB_-cjtI8Uk4u3EMVnRwRhf2a7w4iyd6OmfiU758sJ3urCowrM0c5_GlW55OEARCT0kkVpfxlVA5zwq8jgtN_jKL5WWM6YzjQgz6fuztv3e3IXxlY2vAASH5aTLktteQCueWmtgVsv7jDlKJWLRxMKAGIE7P5ILnvgqL0PcXidTM-rphilFn0uYdcWy1bgIZdEyNu1d4MRDzPUNJuWIsgaglKQAlqgIKw6dWLVISOM_vbQrN25-WoSUlZMPy61y1RFtzQYnDF4DJ6Zoff9IUjX1WOyYGFC5_M-j96BwbQcqGrLkhCY7xdbrcmrdaIGkCRLdtEneQmrqXyEWl3-aln7IX3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=D0Ns-i3febSvTFSJ2XxSj_5_G7yBRhC4sCYWa7VUUc6UnKE5y9L4fFdsqbGiwvr8m8oHChuRK6iWPl3gUWrbG6-_aqJgqZI4Bn9ThhCN8uiipRFOHozsUkubDZRn8u-tElGwJaCAuXEL78p2aAavJhohHNMF3u88M1J5vcihVaSUCa5lwZADbXtI3TFTnYeU4zPoqVOZKXOdRPj0guwVTLf1QB4PwyxDSzau5ql4CWS-UzW9d2BcK9Gq6YmwH45xcsC5HJ8sqQ575Fazx6bP7kh9q1_GGRcWnv2L3rmOAgb8iJO7tbI51bHVM4LQM6YJEpsymZf6RBcNyGpKg3L9GrKyEz7_hHc1qp7Z2_zSrXL-lE2twdTFv701C1c0rL0-wynAIkh1z9iYNOlBIE3K-YPASaBfuV8XJu8Ax98bFLF3jsUv1IVT5cJgrGJceZRs9CqIWGIAZGwXvyYx9TULkJMOmQ4gdHpVgZnkTTDWseSsyfJi6cbd5hWkbVs298LhZpoTjQwvrJSsC48lFE0U7nWIjX3YmW3Di2JaOkTkpqOGNX1AW0YiWuV3dlqR7BUnHt-p59nwCBqEYXtRWJBoBnAbpYos_wyjJIEhuDvY6lowGcMvM7G7-86ofQK3hGgIbWQKDFlrLntYqPaFvj5-mjgS1-h8fT7EQkpRyH9Tvs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=D0Ns-i3febSvTFSJ2XxSj_5_G7yBRhC4sCYWa7VUUc6UnKE5y9L4fFdsqbGiwvr8m8oHChuRK6iWPl3gUWrbG6-_aqJgqZI4Bn9ThhCN8uiipRFOHozsUkubDZRn8u-tElGwJaCAuXEL78p2aAavJhohHNMF3u88M1J5vcihVaSUCa5lwZADbXtI3TFTnYeU4zPoqVOZKXOdRPj0guwVTLf1QB4PwyxDSzau5ql4CWS-UzW9d2BcK9Gq6YmwH45xcsC5HJ8sqQ575Fazx6bP7kh9q1_GGRcWnv2L3rmOAgb8iJO7tbI51bHVM4LQM6YJEpsymZf6RBcNyGpKg3L9GrKyEz7_hHc1qp7Z2_zSrXL-lE2twdTFv701C1c0rL0-wynAIkh1z9iYNOlBIE3K-YPASaBfuV8XJu8Ax98bFLF3jsUv1IVT5cJgrGJceZRs9CqIWGIAZGwXvyYx9TULkJMOmQ4gdHpVgZnkTTDWseSsyfJi6cbd5hWkbVs298LhZpoTjQwvrJSsC48lFE0U7nWIjX3YmW3Di2JaOkTkpqOGNX1AW0YiWuV3dlqR7BUnHt-p59nwCBqEYXtRWJBoBnAbpYos_wyjJIEhuDvY6lowGcMvM7G7-86ofQK3hGgIbWQKDFlrLntYqPaFvj5-mjgS1-h8fT7EQkpRyH9Tvs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bkuu7hwsC8FqZsx7Hb-dCG7JHM6Epva6VJlMjdnVBF0UcmUfoL6RbfaOepXyfns_F36kRkmSxscavjgw-aXyUtwmkwfXPi8AuK-pkwTwBhXzt4xtjTUHGf8o9aUPz2OaxiwiL5rhZagqAUQHVggXrdCp2U5o68A0VV_4MuUW96kXx2vrZ2WwjCQDKTKZe9LGT97ct5UMsPkVUofyZzBn8Rxel_Mj8nMg_Pp7eirkxXQwEX35onzq6VWlIq3OPIyMABjx315-lZJmf6-auvI_sQ2v8nHIkPxkXWfRtrYhuDAnAl7ZwwRMGETbA2_qDwZ8RE4M0ClWRk5ufEzbdnmHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bkuu7hwsC8FqZsx7Hb-dCG7JHM6Epva6VJlMjdnVBF0UcmUfoL6RbfaOepXyfns_F36kRkmSxscavjgw-aXyUtwmkwfXPi8AuK-pkwTwBhXzt4xtjTUHGf8o9aUPz2OaxiwiL5rhZagqAUQHVggXrdCp2U5o68A0VV_4MuUW96kXx2vrZ2WwjCQDKTKZe9LGT97ct5UMsPkVUofyZzBn8Rxel_Mj8nMg_Pp7eirkxXQwEX35onzq6VWlIq3OPIyMABjx315-lZJmf6-auvI_sQ2v8nHIkPxkXWfRtrYhuDAnAl7ZwwRMGETbA2_qDwZ8RE4M0ClWRk5ufEzbdnmHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=K17de2VoRZ-ptzpecdXGmzbxyRaV3T1UosYkORQja9pmU8iCO2O_9cT_N8CVVbQ5j0QmW6barBNmj5KgPrYIg8wsTGeYZ25vZEf4360SgDlx2vRKIblr8FDQJiv0IU6PqdmoKbSgLdLrihj1OKvlmQwU5W1xn2euRRR2TBzPQetP3OolzkhhYvH1s1mH5NaCiJz4B7qAvqOohT92eIkmZ7BCIIcnWESBeXZ7TUAbH5nbmy2nct0jd1w71NaKPZPa3exPqw3hik_jshsHHFDln-DQPq-VdYpA7sQAaljWMEarRETW36feKUTJ60hzmrgEfXn0pnFmKqRC6_VDiPpB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=K17de2VoRZ-ptzpecdXGmzbxyRaV3T1UosYkORQja9pmU8iCO2O_9cT_N8CVVbQ5j0QmW6barBNmj5KgPrYIg8wsTGeYZ25vZEf4360SgDlx2vRKIblr8FDQJiv0IU6PqdmoKbSgLdLrihj1OKvlmQwU5W1xn2euRRR2TBzPQetP3OolzkhhYvH1s1mH5NaCiJz4B7qAvqOohT92eIkmZ7BCIIcnWESBeXZ7TUAbH5nbmy2nct0jd1w71NaKPZPa3exPqw3hik_jshsHHFDln-DQPq-VdYpA7sQAaljWMEarRETW36feKUTJ60hzmrgEfXn0pnFmKqRC6_VDiPpB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Kennydb_A_K6W-Nt1zn4EvWl4HBGrIt_dvC0T21bYu9Y60B122a8u_PQlxCZqN-75wRc-GoRBNw6dAWd5i8X6Q46tPGlH7PddEr9wwYMt_GGrBcnKkaYVjbq5w6YzxKwatw1wWkH6Ldhcw9ZPJYYzzOcy0k_zwMTPzlcKLbLwsBvS65lSamTrQiqdjMMlG9uzBfyFEhy8yzVRAZVSK2emCFn_oo-0A0lmvMTOYJtSJflhjRewqBAqzV7A6OtIGUjlpprqlHJQhxDk2O6kLOMjP6vtKh7OjQ9vvYOqqiOtpCX4By7mvua33Vr8FFZ7KgahzRrqQ30IBI8ej5E1aNb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Kennydb_A_K6W-Nt1zn4EvWl4HBGrIt_dvC0T21bYu9Y60B122a8u_PQlxCZqN-75wRc-GoRBNw6dAWd5i8X6Q46tPGlH7PddEr9wwYMt_GGrBcnKkaYVjbq5w6YzxKwatw1wWkH6Ldhcw9ZPJYYzzOcy0k_zwMTPzlcKLbLwsBvS65lSamTrQiqdjMMlG9uzBfyFEhy8yzVRAZVSK2emCFn_oo-0A0lmvMTOYJtSJflhjRewqBAqzV7A6OtIGUjlpprqlHJQhxDk2O6kLOMjP6vtKh7OjQ9vvYOqqiOtpCX4By7mvua33Vr8FFZ7KgahzRrqQ30IBI8ej5E1aNb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=E4i9iCA5gRQkrLZJ3oyTOof5NHwLt0PS5dZrlR97WftQXATgwSASwkQz7M3FkOqfqwcWATptD_dKLJEsSnmiFfA6omixPAyP0rVFp9OltKUNkkeqxUvUDwBSOZr2PUEbChGVHWil__33zzIbIZ1Dh4Q0I_J1-zuL15iFwkyif__ZwCQH3AO7LPMYtbynjdcU1s8i2toxqMlD4VZrMt6t9bAviSJQBTHRU11AXVH7FELGt1znPltFk-Iwm95-uf9w62IP-jntZRpDPaOXvSl54pShQ44kkiLZkkh3BTqhOYbIvjiTrf1Mi5q44_9-Jf0Xcsu25a7C9iQdZgUpVn7yfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=E4i9iCA5gRQkrLZJ3oyTOof5NHwLt0PS5dZrlR97WftQXATgwSASwkQz7M3FkOqfqwcWATptD_dKLJEsSnmiFfA6omixPAyP0rVFp9OltKUNkkeqxUvUDwBSOZr2PUEbChGVHWil__33zzIbIZ1Dh4Q0I_J1-zuL15iFwkyif__ZwCQH3AO7LPMYtbynjdcU1s8i2toxqMlD4VZrMt6t9bAviSJQBTHRU11AXVH7FELGt1znPltFk-Iwm95-uf9w62IP-jntZRpDPaOXvSl54pShQ44kkiLZkkh3BTqhOYbIvjiTrf1Mi5q44_9-Jf0Xcsu25a7C9iQdZgUpVn7yfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TnfIS5wDEfA69_kXCtmHItm8qHuOAmwEjvwbw3TeezdeW_g6sOkgLb5TvnSNtvo4ipBPNIfBPB3XvHzmxEdrfN3vv9kVLhlt6qBZ-PbV_4tptpNEN5liFWPZbqndMF4zv4LjjK2cJ_DNADKLAGRb25AmQRlw1TS3dwhQ20uWH37Pm-v_W7SsuHdpfwkW6V9wVsAiuojAigxgaqmJ8Gf0asKy0ZSkyrwH9aC8yGjUyQD6GgofyAIx5RTBgEJKBvd9g-OI-MYsFohvHyxvgxfij7Mf-fEOOb8aXvuwsiJ0w3cnekesmUe-VbrrYCiS2bIeFluWnEn2e2IJEE9MXeAmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TnfIS5wDEfA69_kXCtmHItm8qHuOAmwEjvwbw3TeezdeW_g6sOkgLb5TvnSNtvo4ipBPNIfBPB3XvHzmxEdrfN3vv9kVLhlt6qBZ-PbV_4tptpNEN5liFWPZbqndMF4zv4LjjK2cJ_DNADKLAGRb25AmQRlw1TS3dwhQ20uWH37Pm-v_W7SsuHdpfwkW6V9wVsAiuojAigxgaqmJ8Gf0asKy0ZSkyrwH9aC8yGjUyQD6GgofyAIx5RTBgEJKBvd9g-OI-MYsFohvHyxvgxfij7Mf-fEOOb8aXvuwsiJ0w3cnekesmUe-VbrrYCiS2bIeFluWnEn2e2IJEE9MXeAmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=R8LTiOpwW6KVe1Haykdic0URvJZnr-HmEyJKKoE2xrh3ViKOOkXg1M6uQ7u7V_ZC9EsDO4wwIXwulZewmdmHl34nJkwF989D8JTnLw091npm5u9GBtA23uzIIn6Ac1sJgs4VqqILtSNEqBNes7EYSHAAVz1rfW3Zlw8XqdA0hNYjsLLt554Z132q5UFZdWxFtqXsrGAx8S2OhPHghgVNietHBrpHrO0U6LqE678hCcPI1p2NR75hQg-46cPmMKdtGVGiMjsu0qzhWv0i4irLWPJ9m16yZo0ciOWp1NHVzWrhmy6zTbBdMCdIcgFujqPwgs7wxJIcw9Yx_otGV0ja3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=R8LTiOpwW6KVe1Haykdic0URvJZnr-HmEyJKKoE2xrh3ViKOOkXg1M6uQ7u7V_ZC9EsDO4wwIXwulZewmdmHl34nJkwF989D8JTnLw091npm5u9GBtA23uzIIn6Ac1sJgs4VqqILtSNEqBNes7EYSHAAVz1rfW3Zlw8XqdA0hNYjsLLt554Z132q5UFZdWxFtqXsrGAx8S2OhPHghgVNietHBrpHrO0U6LqE678hCcPI1p2NR75hQg-46cPmMKdtGVGiMjsu0qzhWv0i4irLWPJ9m16yZo0ciOWp1NHVzWrhmy6zTbBdMCdIcgFujqPwgs7wxJIcw9Yx_otGV0ja3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=C47O46KhlHt2wJ3DvXIomYftdZyhd8VUmYzHt-gsNQGf7lCH8MYs0pVwHMPKIqAZgHsMfpABg5TCrDFU4GljocDGfmM1jQR_LR5lXV4aXUUhwySzM0X3nhC4S2-txdP7rJTgY4aXp3tNzZxOEcVPAV4gkjHd276vuVO_gegQnXScSNjfoUU0n9kNtio55j3ACWUBJJyGfrOoe-yDv-qwCP51itb_FrOHFETJcE58cgw1MK9gGGCt2p2nWfYPzASHYmUXJWJu2jb5g_Y65n3MwKW4-V9b4eTjlb8MOmvx3UvDDraa-xWsi_QQA_P-Wur5jr4gImQkT0snjSnvvcQ4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=C47O46KhlHt2wJ3DvXIomYftdZyhd8VUmYzHt-gsNQGf7lCH8MYs0pVwHMPKIqAZgHsMfpABg5TCrDFU4GljocDGfmM1jQR_LR5lXV4aXUUhwySzM0X3nhC4S2-txdP7rJTgY4aXp3tNzZxOEcVPAV4gkjHd276vuVO_gegQnXScSNjfoUU0n9kNtio55j3ACWUBJJyGfrOoe-yDv-qwCP51itb_FrOHFETJcE58cgw1MK9gGGCt2p2nWfYPzASHYmUXJWJu2jb5g_Y65n3MwKW4-V9b4eTjlb8MOmvx3UvDDraa-xWsi_QQA_P-Wur5jr4gImQkT0snjSnvvcQ4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btdx7kiemTTDQKKKIuCPBIRxxpZA6h5mK25LYjh8Et95saHQSf24oFuNXSXwfzHaDwVFLk3fVx_jhwbbpPBjFGKiUpn2wqyN-9rYKPZmHIaD_xsSg6mQubLIhh-VQCmEpBnAhZb9OFvajtzWvzAszi1dwG7gHhp76wuPmSKE0VL7QHLsPA5pYZd3FJ_vkgY-U-7WReCv-0nkb_qOpmk9IlmgduCBOym13C0qSGyzLBYcyeM37-kmO0BkPlFAZBjnL71H4jOvV6bOZDZ1gfXSlNIR7Z2eAU2T9ebxXcLvXeaReBExFSwWzw0P07g638ynq_SH6gxlWw3O4ZC6EErjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=IEHzcWLsZaa4Fh2ew-7bUcaRvJh_liU-x6lRGRg_Kz2liBwamfOUl-98xGEc-gO2mNIRTm_Gal1FcFft50tg54D-lGi9yForDgpFAwlvKRGxGnTJijZQ5FMsWQxL_v0fOeGRJAaxaSyUVilfeACEvpxeTpg9SUefHKCvF5bgrXfhsDxJpvge8ZUJjmtygBbrpMbmosYqCuOUD1P9CaXKWhxyezV5KT9gqa-CBa3ISp5g2I2SRlvlBZDRzbVGgfMBkmvR_mO5WbcsJ3fyn8M8i3HFgIoFSlbmlnNQijZL46g3N_PIt2w0Kus2yy2tAWkAsqcTgMWPTaZIC8SGR1_-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=IEHzcWLsZaa4Fh2ew-7bUcaRvJh_liU-x6lRGRg_Kz2liBwamfOUl-98xGEc-gO2mNIRTm_Gal1FcFft50tg54D-lGi9yForDgpFAwlvKRGxGnTJijZQ5FMsWQxL_v0fOeGRJAaxaSyUVilfeACEvpxeTpg9SUefHKCvF5bgrXfhsDxJpvge8ZUJjmtygBbrpMbmosYqCuOUD1P9CaXKWhxyezV5KT9gqa-CBa3ISp5g2I2SRlvlBZDRzbVGgfMBkmvR_mO5WbcsJ3fyn8M8i3HFgIoFSlbmlnNQijZL46g3N_PIt2w0Kus2yy2tAWkAsqcTgMWPTaZIC8SGR1_-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=vEpI_2pnvp-v0a8laJxQ2HRKG--bK_AN8dJKjHVNaY12zW9jHAmYw1QsmSqCNpu_ojUsEq461q9sNeTUFzXGulRVV96PgHnoIqtVzgpMuwU3_z7li8q78BqkpRFzbTGO_rwuZ-8ibmSF59xFKuOpCWKw2WZdWkGMZ_Wbhjb8O-lHdEWCdQUZmDIPQey9qLIArWd6EJsXZ4dPJSbl3pbXT2euCRj28PnWW5vHV8TgJH5WujvFosgl6jGEfr6CZxyqeH5xSVsXSekb-_duP4EeEGrDUWPhFKukbpv7QXhJ4-y614nAQmcPjvdSNGp9dz89FkRwcvhx2_WC5AuN3t48Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=vEpI_2pnvp-v0a8laJxQ2HRKG--bK_AN8dJKjHVNaY12zW9jHAmYw1QsmSqCNpu_ojUsEq461q9sNeTUFzXGulRVV96PgHnoIqtVzgpMuwU3_z7li8q78BqkpRFzbTGO_rwuZ-8ibmSF59xFKuOpCWKw2WZdWkGMZ_Wbhjb8O-lHdEWCdQUZmDIPQey9qLIArWd6EJsXZ4dPJSbl3pbXT2euCRj28PnWW5vHV8TgJH5WujvFosgl6jGEfr6CZxyqeH5xSVsXSekb-_duP4EeEGrDUWPhFKukbpv7QXhJ4-y614nAQmcPjvdSNGp9dz89FkRwcvhx2_WC5AuN3t48Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=bqt741Y6QmgjyJC8Jv0ZKQqHknaXWvN7UUHQxB-QM3AOtWV2n2-PGFoKgRrIM161UXKkUOcZbtuKcnL2hj4SB34T4Gg666UZ0OLMbvOHEwZLH1IvOa1Tky9Q3Xgn5OFdE2nV0q76IPKu1yGBw0Ui3ryxZcUZJduV1vIlsNPbtawuv7mix_3lymUAiAKThDMbitU9CxoiAh2Tg5K3r7IIxzclkI7wEMtgV_fUsVGjqtxb-eFu19C5J8o6EuS_rPSv4xxgKJj7QcYfwYq3x6j5LG6Asnx8Rhq_24yipZuOoaEI0Ukqzm1sQ7QxY1Edt7lcSU8DmHc5RVGLMuzyVMer9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=bqt741Y6QmgjyJC8Jv0ZKQqHknaXWvN7UUHQxB-QM3AOtWV2n2-PGFoKgRrIM161UXKkUOcZbtuKcnL2hj4SB34T4Gg666UZ0OLMbvOHEwZLH1IvOa1Tky9Q3Xgn5OFdE2nV0q76IPKu1yGBw0Ui3ryxZcUZJduV1vIlsNPbtawuv7mix_3lymUAiAKThDMbitU9CxoiAh2Tg5K3r7IIxzclkI7wEMtgV_fUsVGjqtxb-eFu19C5J8o6EuS_rPSv4xxgKJj7QcYfwYq3x6j5LG6Asnx8Rhq_24yipZuOoaEI0Ukqzm1sQ7QxY1Edt7lcSU8DmHc5RVGLMuzyVMer9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rR_XiPDAr79NTqXlNLZzRdJFrjYEKoae7p4ozw5NrOPIO34u_Kt_LW0TMwEWJNQyWTP0yPCGyStcXZdRpA9zbwNeV-dSulAaZOQzJTalwiHRA-tpmQN3h7DdNJIRg9gXSdFnsO6SgWmmREiUArdFnUEUzTFiBWTVAKxDQVqZhnj9e3r4WdIDqOky9pG5TQ7FyQc690s6CML285PGVUkn9OZFDRNEmAWAYcI_kmb1TNeExOwR7mOvukDNBPmUQlYD4aJzLIPsqNOxdRqMbWlusmx7fx-TXV2r6lkYJT6K_geCf2tC1rkIN-9zBxKYI7PODx79HPGRDmSE3IGhna-95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rR_XiPDAr79NTqXlNLZzRdJFrjYEKoae7p4ozw5NrOPIO34u_Kt_LW0TMwEWJNQyWTP0yPCGyStcXZdRpA9zbwNeV-dSulAaZOQzJTalwiHRA-tpmQN3h7DdNJIRg9gXSdFnsO6SgWmmREiUArdFnUEUzTFiBWTVAKxDQVqZhnj9e3r4WdIDqOky9pG5TQ7FyQc690s6CML285PGVUkn9OZFDRNEmAWAYcI_kmb1TNeExOwR7mOvukDNBPmUQlYD4aJzLIPsqNOxdRqMbWlusmx7fx-TXV2r6lkYJT6K_geCf2tC1rkIN-9zBxKYI7PODx79HPGRDmSE3IGhna-95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5uhe0_e3nIDoV0mqtHbvZkOFbrJqybj9glGm79hWuZWTkKaIg9im3GWzO9tXh-9dri_zlD0M6UE2suB20ygLIZYnjcLDgK9rmnGWKC53Ex81ccSZS-GVxx4cyzY-ZknNoIxHNgfkJ6pbeEV2k2FzOSnwCV_pUlpTyFmNoJNerR-5-4j393M7WQNTCv0SI5wRxqd9C0he-lWuCXcc9RW6HCX-nuTUhWi_xbSaHBOgOJXBxO0gFCNSGd3uCWgV3s1ito46Xprgyyq0GfFzl6DZMXJ6G5m_lGAuFbRbcpJ3ZX32FuNDzqkeQWHXAdWNDR4GFORWukzOd4Dvw8ePzIrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MQuM58jLJ9xI4PoS3TEy9M46_hwA3s2mbplShfPNYjdJkUKA0fU6jxsyWBNaE0eXaX382GumPua7wGDcA0y7pMAsdyjjAepASU2BDIivH6GyN-6KVdSKn5qEZg0yHIwcnbjVljn3H2TErZKeClLY4yCcLbO-w4_r0wtI_WxHKd0CAPZv0Q31z4dE6rY1Y9Bo0U_-hARvr1WTxfDdNeGW-HTgw6IEnKp-vDBLM1YhAzYjxBfjlxjma_ts4Mxp9mIrtt3eO0xR5krSswbU_hHbTDVsg_HHWoH9nLi2i48jec1oF7aR8wLUlyAcf0Isy5VKgHDGCRPpdybB2ATVuV0kTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MQuM58jLJ9xI4PoS3TEy9M46_hwA3s2mbplShfPNYjdJkUKA0fU6jxsyWBNaE0eXaX382GumPua7wGDcA0y7pMAsdyjjAepASU2BDIivH6GyN-6KVdSKn5qEZg0yHIwcnbjVljn3H2TErZKeClLY4yCcLbO-w4_r0wtI_WxHKd0CAPZv0Q31z4dE6rY1Y9Bo0U_-hARvr1WTxfDdNeGW-HTgw6IEnKp-vDBLM1YhAzYjxBfjlxjma_ts4Mxp9mIrtt3eO0xR5krSswbU_hHbTDVsg_HHWoH9nLi2i48jec1oF7aR8wLUlyAcf0Isy5VKgHDGCRPpdybB2ATVuV0kTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=er7l_WEr9H5TNLLbFoz9TQiebXrTmz9gTGLV0UzPN-IWJwfl1hcWeA4ESZLwRQcvwbWo3MVAmBehit2vS1jbljbJOZQITzNVg1i8OBVcu85XYyuc_HL-OAoik000bPVcB19uxkN-DRFSC596YTzM7lZGTHCM0FXyQXU7upxFFHxg_GPyhYUV4xB5FYDH_70cEg829UeyOmZzc_I3QbWOEmhCn02E_PaO41pWdhyJc98GqKGXsToIJtez3dnfrg5O8wBcM1NvfgYxmjhLiL07vDq8p41--DgOwGf6ZADnuvXrFA4M6B6DCl4PEOJDngKjSpPGNmDyf0PFcGYKKfNglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=er7l_WEr9H5TNLLbFoz9TQiebXrTmz9gTGLV0UzPN-IWJwfl1hcWeA4ESZLwRQcvwbWo3MVAmBehit2vS1jbljbJOZQITzNVg1i8OBVcu85XYyuc_HL-OAoik000bPVcB19uxkN-DRFSC596YTzM7lZGTHCM0FXyQXU7upxFFHxg_GPyhYUV4xB5FYDH_70cEg829UeyOmZzc_I3QbWOEmhCn02E_PaO41pWdhyJc98GqKGXsToIJtez3dnfrg5O8wBcM1NvfgYxmjhLiL07vDq8p41--DgOwGf6ZADnuvXrFA4M6B6DCl4PEOJDngKjSpPGNmDyf0PFcGYKKfNglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1ctnDZunmqpb8qV14q8nvWDCKtM5zvNNuHlaMk1azfz0Jud3jQUvYE-jrcuZkBa-KRg9diUDmSJZJqoG8zTaPrZJbWAnwRwZOFrDJDt0ruvpIAfypHKzTwFwa-z1DAkcadeeKi_zNCuXypLT_tv-Q2FV3OdtE6wLMdn9G8_pI87xjB8C3FsOnfnZ-f4Wbyg05nE98sRaNFtMwrt8qwyZARvnoOnnyoWUQdKk77yUSUZ2I0DNgsMYjc4Mjm8klP_5XKsjzEXEeQ4naGp2TIsds4_TSg81wS03nSMFl1DEoU_t5K7p1B_Y_WCtSgTKVn4ptVIag7DhBEFb78Rsjb4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxoP1GXWou748ulLk07fDwxdkjChnlSwlO-urfbaoGncjtFn1lL9wZ_foDkKdWNpF8h1IR7hJMrxG937Wx8XxK7yaWSfjGanCRj3s1FC6ADuw_4n9oKEmw3j-Mb86RxuRmAwrMUaTvXIjNkX0PO4J6zClKcHYv_fFhv5IH5EmIgMrH8wCzFgVAOA8q8PMhraNImTSirLhAwEVtEICt4zb3WCYEY7Eidr-KXM1QxGgg0jCv900Z8fYIcSKgRMUmA0gujBeOztcBvpzdRPvv2DGZm0Ch7yWnuAiHunmuhifgyRNrXilRoXI_LD7dYHF1UDveIijw482OTVtRspfA4PAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=IAEk74VdLlkY1V9c5YOZGiQQcNEHbcp6A2sEWMcxnDp5WfD4K6bFHTDhp6lkn3Hql_dUZMwEZKIjEnT5mZCPpBkyJKkkQyblX95gV6fQPkVZJaHkOiRqkZ5PjtzCZ6y799k7zlOEjtbgcaOUeRTlrlF3C5DPGogsBUBb4trUXXMqtRga71GghqF31TSTh0cGzTmfgF_ZmPNB3kPiWLNp2hKfP2H5VieOtrEXJT-E6OaZ-Uzl-S1cyvMGkndkc4m9qAh2AUwpQgCkJX9ulrmXJwQ1c8-YrYeAwbq1LZO67YYHH_qLNCNScK5q1Bdcn7V1-wAHAwKcHLWcCojjFkvQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=IAEk74VdLlkY1V9c5YOZGiQQcNEHbcp6A2sEWMcxnDp5WfD4K6bFHTDhp6lkn3Hql_dUZMwEZKIjEnT5mZCPpBkyJKkkQyblX95gV6fQPkVZJaHkOiRqkZ5PjtzCZ6y799k7zlOEjtbgcaOUeRTlrlF3C5DPGogsBUBb4trUXXMqtRga71GghqF31TSTh0cGzTmfgF_ZmPNB3kPiWLNp2hKfP2H5VieOtrEXJT-E6OaZ-Uzl-S1cyvMGkndkc4m9qAh2AUwpQgCkJX9ulrmXJwQ1c8-YrYeAwbq1LZO67YYHH_qLNCNScK5q1Bdcn7V1-wAHAwKcHLWcCojjFkvQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTi9OfBRiWi6ICfM-ibwc8n8Ogjd3CN8-K2gFr1tLk7rguR4bOl4VfpyMOcwDAieE-AqIZO1LEfAoxe7YgX5A5GwMkrvmcmrWmMAtUMcZl9FVVKSAomVeZGEe1UkRUWyBhqZSM860Yrs1uIXujefTn1delpq0ONFYtwH4yohFd9VonK4bmC1xhgQMHLNtqkaGFyGX9dUtvyEKj6mBE6TU8VjPHJWtg_BcpoDQrMv6QapCwAWrW3zPTih483iQO8QJibfi-Tgxj-GRnp08HM5uQAcapuBobapf4ZE_obtuhKYornHIk9fhzdCQ3Tm2ikTstfjY46qSxk7q_KuVnDJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1YZ4wplhlKOx0fyMnL9TebXklOAFrE5Uf565Rhkc-GLFMZwhMYq30jOJv-ltK6Ibyju6cSZCYl0payTfwf50mpKMY51cwtzYgdXW475Yt4Cgf-pyv8ZSfiAFjay0mH_BQZ_-pge8sdjPFAAxOExHPuzOaCwMOSUpXHQd7rg88EK675xZX0vw75K6BtUa9mQxb71dw0G1ZVFHdfdFGKZneymVrNuE-xJXu5wvDZomaBFUNxVwFpQoFo4cMF8nzgJbbnD1i0RrT3-O2IQEZJN76ejpkXtE27_k6vNVC1ct7GqLj9pCDmmu7UZtEeTg8Di_Xf56wDu2IJCMuF67US-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVozOqADd6x5mm9NuXLb3kAOyX61hu4WxGKJiHxu7p1LK_Fej1QotG0p7Z6qpjrrTZhvS2rbOOE-zE4M0U2o3OOLtX20wbU34IftOr6QKsDsKZ1uaKhd0T__zat0JktqDO3XHVFq8L_bXCFBdIkqOgCo9T2fr1_eKiCxMDZxB_bcFZVIPDagQaUXg1iwh40B-FeynVzNl4Mqqf1N8iGYeKnN0mgX9W8LNCszgjXiAoBi7-quIWce3shFtSizgi_MigHJvoHMWjulJn-rxNRuri4xraDFJM49PpKz6tlGLq_reYlReWSRFLgob9WLzzbG1Jg5CnD6UiatH6Ctf8KXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rPaff4URtCWe6XitABEBW6o57nVQ0UmvXnxAS6DvHJgYfWps69j35uV2TiN1Wwm_ZHv8uqUXVtspENW8SWeniWZFiNvtFkp6JODlH_qpUgBFHOzwlLLBU17JJHq4REDIXArYvLd80XKOCwe0yTgU3LCjr5OnawlRUWoJl74ULnPA_s1Mcvv_JgWp-rUuTVzc5HeEuE9343rGDy1Kvw6ylPwk1v9el4L3vHNLfmPswkSNaHPTFtSaycnPmNPU3ted94uFGRZC_bioOfihjSJhvjt0z7ltk7rgTU9r7x-9b76ZSaifJSzgQZCYFdZlXKqXQmuE59gWl2_AjEdooq2vvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rPaff4URtCWe6XitABEBW6o57nVQ0UmvXnxAS6DvHJgYfWps69j35uV2TiN1Wwm_ZHv8uqUXVtspENW8SWeniWZFiNvtFkp6JODlH_qpUgBFHOzwlLLBU17JJHq4REDIXArYvLd80XKOCwe0yTgU3LCjr5OnawlRUWoJl74ULnPA_s1Mcvv_JgWp-rUuTVzc5HeEuE9343rGDy1Kvw6ylPwk1v9el4L3vHNLfmPswkSNaHPTFtSaycnPmNPU3ted94uFGRZC_bioOfihjSJhvjt0z7ltk7rgTU9r7x-9b76ZSaifJSzgQZCYFdZlXKqXQmuE59gWl2_AjEdooq2vvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=uul1ueI3AxN_OMpaSyk4eag5GxmwHcAucAPVUG6v0eh_f2L24SolVVj15YMq4Vid09bJjCRKhAwNi6kCC_ngRhQiR7TxLmr51iH1V6kbIBxl_oPR7ewLAWbdC9KtS8NSsFkf3Hy0OeEiIFmsY_5bVaGwQUumVtgcQi_1EYTNHSXq1fKo1ek1oOAi3u3vCAB8JFixqA7IWJbLsOdWRivKtRl78ek_KE7I5yuLXTruAT1CAPmNAumCgzEbQjdDvQC3EUZHpm0PSY3hYbKxmhEebDs7MfIYx2oS4WEODbjjakaHFs1ucwV6STYN28WxkDJGjEF2SFmo2axeaNKpy0XaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=uul1ueI3AxN_OMpaSyk4eag5GxmwHcAucAPVUG6v0eh_f2L24SolVVj15YMq4Vid09bJjCRKhAwNi6kCC_ngRhQiR7TxLmr51iH1V6kbIBxl_oPR7ewLAWbdC9KtS8NSsFkf3Hy0OeEiIFmsY_5bVaGwQUumVtgcQi_1EYTNHSXq1fKo1ek1oOAi3u3vCAB8JFixqA7IWJbLsOdWRivKtRl78ek_KE7I5yuLXTruAT1CAPmNAumCgzEbQjdDvQC3EUZHpm0PSY3hYbKxmhEebDs7MfIYx2oS4WEODbjjakaHFs1ucwV6STYN28WxkDJGjEF2SFmo2axeaNKpy0XaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BBgjRCDB02_lI7r_AgqHvdyU96BD7Jqoda9ycQVrOebkAT4cnatreTocuIZ3IvU01TtyI64Nzj1ZLTUEPivt1Ya-i-fWfnic8oml9o0TgDGKs--CISucHupeyqTzSjiyMBgZo6GFGbtO4ZEmHpObp4bYZvByymbq8Uc_Q1GrTe8S8HiEVGmrASefgtYVX9Zo0TA0_SEXZGptWjFmMQqjvem8_AYaYUnPU0odZ5czR27NZHOW6e8w1kJ8gOY__eLdGy2JG3rCKpoDWswZS8FKvoVutnWgvBYpY0k2oigD0e9MfmNP8iMnuyNDvjX8EBzqKSe67cx01rcF7xIAElhT-I7I9j2YCFVFTPM_zVCIULg0SLYG_ncD8u1by53VNzL_JjAafxQC56c6_eRLcFeoGNNzAKxWpIo31HB5qQd9l5gl6NY62RSieYN9L0Arm5CbjbWOd2PlE2ZUXjlTMUKjIvelSyxXpbwSHXOdYJdSg2Afhk7UXl3r7Jt2i1I4PLmpm8qltlUwVGQjzyo3F_GAlAPPj4G6xyx8AkFb6tw156_Es7IaHN8zfYKKVVkQKdAgZrZdnTmSD2oWecpOXz7DFvh2dVmY6cojOcDpvZ3qmQjo09Rtn6lEi04LIhCanxcfrDqW0QYQ1K6_680lAXNS6HlmDIXAOQuR78my_j0F_os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BBgjRCDB02_lI7r_AgqHvdyU96BD7Jqoda9ycQVrOebkAT4cnatreTocuIZ3IvU01TtyI64Nzj1ZLTUEPivt1Ya-i-fWfnic8oml9o0TgDGKs--CISucHupeyqTzSjiyMBgZo6GFGbtO4ZEmHpObp4bYZvByymbq8Uc_Q1GrTe8S8HiEVGmrASefgtYVX9Zo0TA0_SEXZGptWjFmMQqjvem8_AYaYUnPU0odZ5czR27NZHOW6e8w1kJ8gOY__eLdGy2JG3rCKpoDWswZS8FKvoVutnWgvBYpY0k2oigD0e9MfmNP8iMnuyNDvjX8EBzqKSe67cx01rcF7xIAElhT-I7I9j2YCFVFTPM_zVCIULg0SLYG_ncD8u1by53VNzL_JjAafxQC56c6_eRLcFeoGNNzAKxWpIo31HB5qQd9l5gl6NY62RSieYN9L0Arm5CbjbWOd2PlE2ZUXjlTMUKjIvelSyxXpbwSHXOdYJdSg2Afhk7UXl3r7Jt2i1I4PLmpm8qltlUwVGQjzyo3F_GAlAPPj4G6xyx8AkFb6tw156_Es7IaHN8zfYKKVVkQKdAgZrZdnTmSD2oWecpOXz7DFvh2dVmY6cojOcDpvZ3qmQjo09Rtn6lEi04LIhCanxcfrDqW0QYQ1K6_680lAXNS6HlmDIXAOQuR78my_j0F_os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=lmNBpO13PKp-obfUAaln53v3kl8f0sMggTBowRiBCPOK9XS0K_a0EkeWRKTZ1flZyr1h88HuUGgcsJk6Lq1X_QjdD42-d8Z9dOWPEXxm9tKUUkRJ6Nlnn3qvIVgz05Hfb8InyJDErwOA31qz9rzialsfdNnkINFk-3YkUjqt12_HRYyQIk2sgNFT9HWtXiAkk5dursncaX3F8XL--RofawijwlneM5uKmDSJ1qzmQK3xsMN3poCIOeAxTPJ5iBjyhAJ0QAeFT_p-Y-GJvzN2KbtFs6NUCWlBPo1NG2YSTnk0g6r3wkKLlgtitXS-EwD3JjmjONGANKiS07C5H-toEXLEes2vSjdV9vNybJDfZL0VKIXGqmyAMMZNcFZVzyknJ45HP7cLe2Kp3hox90lDMg7DIMX0E1tQtD6feZOqjrwxqg9TNUuprzopIfQrLWdLNR9DvOpcld1uHgSPk3DBSZE921HTadtSxZIq5u4g1QV0RQHgotlfs6nZc6NQKUf784rAVTwwNKI2HNMhSOpU9Bbkj0dRwf_ErWXw9Xx8bEPIipbLz3WnpuS_zlfDQktzv3ih8y7xkElpYDfWiSeayRsMFtKLMNC1BH3XkJQhOS4oKQtbfxqMLLMr5flnzIOZn27tlOaeEWvNRQTeI8leO2ihizqhdWkKwXKK5tcWxrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=lmNBpO13PKp-obfUAaln53v3kl8f0sMggTBowRiBCPOK9XS0K_a0EkeWRKTZ1flZyr1h88HuUGgcsJk6Lq1X_QjdD42-d8Z9dOWPEXxm9tKUUkRJ6Nlnn3qvIVgz05Hfb8InyJDErwOA31qz9rzialsfdNnkINFk-3YkUjqt12_HRYyQIk2sgNFT9HWtXiAkk5dursncaX3F8XL--RofawijwlneM5uKmDSJ1qzmQK3xsMN3poCIOeAxTPJ5iBjyhAJ0QAeFT_p-Y-GJvzN2KbtFs6NUCWlBPo1NG2YSTnk0g6r3wkKLlgtitXS-EwD3JjmjONGANKiS07C5H-toEXLEes2vSjdV9vNybJDfZL0VKIXGqmyAMMZNcFZVzyknJ45HP7cLe2Kp3hox90lDMg7DIMX0E1tQtD6feZOqjrwxqg9TNUuprzopIfQrLWdLNR9DvOpcld1uHgSPk3DBSZE921HTadtSxZIq5u4g1QV0RQHgotlfs6nZc6NQKUf784rAVTwwNKI2HNMhSOpU9Bbkj0dRwf_ErWXw9Xx8bEPIipbLz3WnpuS_zlfDQktzv3ih8y7xkElpYDfWiSeayRsMFtKLMNC1BH3XkJQhOS4oKQtbfxqMLLMr5flnzIOZn27tlOaeEWvNRQTeI8leO2ihizqhdWkKwXKK5tcWxrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XxACop15xsNraGYp0sP7kH6Z0IhBPu4HfI-wQxtFeA6XzixT2M-_Ari4s7rjUeGOd-i3hbhkhx9QkMMKXFmh7KpZ_RnCGX-Oa4S9sjCeW0-fdgGbd9oOcc1o8_93BLCCS_PYugSzjz46jSYAt7NU4luKbe4ojFL_O0tGZe50gQTl1b2adiAWZpVEJRTdW1wv5gM1Ksd3BIUj_ufkP57-q6fnU9OMIw2vbtsoCc5Eg0fVstjPOYar3R1TxLEZothiJsoWn5YhmVga49Z5qwYVVRl1_EsKBwmEecLe3Qq8FQpFtRfrYh08jxnm3EEZnJAKXAQkeRhHzclpnejdspswCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XxACop15xsNraGYp0sP7kH6Z0IhBPu4HfI-wQxtFeA6XzixT2M-_Ari4s7rjUeGOd-i3hbhkhx9QkMMKXFmh7KpZ_RnCGX-Oa4S9sjCeW0-fdgGbd9oOcc1o8_93BLCCS_PYugSzjz46jSYAt7NU4luKbe4ojFL_O0tGZe50gQTl1b2adiAWZpVEJRTdW1wv5gM1Ksd3BIUj_ufkP57-q6fnU9OMIw2vbtsoCc5Eg0fVstjPOYar3R1TxLEZothiJsoWn5YhmVga49Z5qwYVVRl1_EsKBwmEecLe3Qq8FQpFtRfrYh08jxnm3EEZnJAKXAQkeRhHzclpnejdspswCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-lPSAmq0M_wWvAOvCKspxDXei4oDw4vbblzA3Y-DAubzuZJL-DXKilQ46eirEUs2TXv1TjqOrl9j2Z9l2uFyaXr7tQubEaqFDoyT0kdSRHqu6Iw2LnGPRpb6SxvyRhoOqwJLi7zNB5-7vmXngr4TEtcbzaiUya-fI0a8sZvKvNZnw5KOPjW8SlDrPxAUKDLGYAh2cWvsZNrktxelFn_hNDPOmhwL8KLg1nTb5WUEmhnbsn8GzyVX0g1IwJvBL9MpqvSNPIXAlwuTx2A-5Y8XTSzPbSl9h9g3kOmO5Dx6b51sHFOsIDzQAsQqaoerMh1quq4O9b9cIxB_YmrThvfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RJbwVukz-Pkx91PHrOKmCsGzUAefzcWcXOaPva-SwWAkxMICvqLL7UrrA9zaCZeOz-3l3m_azv-q7bUzDYVoRFbl-yXBsSIP3250JDcztALI29EmYRfvN7JzVUK6mgvdV4dZa_WtaKOoPFsOYvGSbKvBB83sUlsuF2LxgeEN6C0NKPJUBvYow6Sd5C69drrjf5WN9FCoCKJP-WqRIrwPLOVf1EienoJQKXp3YN-VBfn_OElb6xSRwUbP578jmKFdv9VcQfpKqnsRg2Qq7PIBCLqmCxkfGtVV7MrprGZuLIAN5TxCRVjeJJ_Rnf_T7Upf_bVglGjc5byrhIXTnthhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RJbwVukz-Pkx91PHrOKmCsGzUAefzcWcXOaPva-SwWAkxMICvqLL7UrrA9zaCZeOz-3l3m_azv-q7bUzDYVoRFbl-yXBsSIP3250JDcztALI29EmYRfvN7JzVUK6mgvdV4dZa_WtaKOoPFsOYvGSbKvBB83sUlsuF2LxgeEN6C0NKPJUBvYow6Sd5C69drrjf5WN9FCoCKJP-WqRIrwPLOVf1EienoJQKXp3YN-VBfn_OElb6xSRwUbP578jmKFdv9VcQfpKqnsRg2Qq7PIBCLqmCxkfGtVV7MrprGZuLIAN5TxCRVjeJJ_Rnf_T7Upf_bVglGjc5byrhIXTnthhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=KqoWz7U-A12JTDLnWEB-JXevjnlbPuIsLGCH9AgPRTUyy5A2xLuvdUyOZ--OK8tfqcihfFodqxVDJcAG11EubdYijn4rD_S7fWOBQl19gUlycrndKy-rMEwCiSp0JFGRIRnpL6iiIBb97c4XGnocIA8Y1E5kg_gXjtnhX9GMEIihKkIPYz1rzSeKBFmhSPazoM_4_SUwWrouAfptCcxUs7Ar_ZdBbCaO93ntP1npGyge3_YShG8_8ylcJAX-xgWBNE5bp-P0VjIwBhSVmt9rHXfCBWZDzDtyHr8aGl_ewQianY--nJ1AAvERhiG_JIZTVRFYzpojGNQsk-T9mBXT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=KqoWz7U-A12JTDLnWEB-JXevjnlbPuIsLGCH9AgPRTUyy5A2xLuvdUyOZ--OK8tfqcihfFodqxVDJcAG11EubdYijn4rD_S7fWOBQl19gUlycrndKy-rMEwCiSp0JFGRIRnpL6iiIBb97c4XGnocIA8Y1E5kg_gXjtnhX9GMEIihKkIPYz1rzSeKBFmhSPazoM_4_SUwWrouAfptCcxUs7Ar_ZdBbCaO93ntP1npGyge3_YShG8_8ylcJAX-xgWBNE5bp-P0VjIwBhSVmt9rHXfCBWZDzDtyHr8aGl_ewQianY--nJ1AAvERhiG_JIZTVRFYzpojGNQsk-T9mBXT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_kah8xXpxmXotVWnhWqS66VJAWmt_JhmYG84WsSN0keo9JfBHELc-1hPCoBPx4Q-M7G9CsCSJGpUh6zpYgb5jUl1G1y0Ji2uVT98tM88tL3UkAAicoUqRb_dNNGLzEFDHhONwjdR7xwlrvKIi9cVG_J547e0hj6UCX8jlH7S_5ZTOYseqeHOfXQnrCHu_viB7_rZ6Q8IME_BqCmbXiYF48YEIFSjZ7m-DRGmPI7SBsuTe1cudUwC-cZILdAELxzA9c0YJLqTrkvamdjn5h-TZ4dFofqQ3qcuj60JZ06HBrrFfq0R_bBg4SCOmiGUtxV8n8RxMLUK2TVMztZtM0A2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxYlBUR9u1lBU9cjBbwY9vUxguic36AGzNKGjM59zUutrPlhXLlIOtnp1pRY09oqNUOqRknMmWjJk0StxueMdrGnn_v19fM_VVaO5nFZ7JY6PILvNbcnVpKM1ylwJQ1MheWD_W9qDYj8znWvxDe-T8OkHkeAcqXN5Ru7MGmXNjGT8XhMADGMoF3EZAANPpmIT7uHbDVSO7CF1KmsDIl1_z3uMV_tw3XgcsCFVZ1TEJtG_OYZo7ZP6I77zvzK7gniCAtcwPhg7XOQXOzalW5Bd37OJYX8tmyEmudIqBkoyxfzxNfxOK2HwuEZ3ioBsiu_R1GjUHox1vEgA0l-LddoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2hJ4D8WN2hbyI-sGwWouK09mnNBgZhYpgJ1oVCHb9-cMiriIP9B8HJN5xbUS4XKHzSTlA0v-3Ys6FApCBKJPIfn9vXPzfh9Dt1Nwj9aqjknTtUbumfoJvAqgLJjpBLVvRTTZNjG95afaYzOnN542_6YPIfJi5jWsPYL9BPen5KQJsGrTE6bZCBGiJMP4XL1B1QN3gBbtJLGlb1GWCfB444BMIwJ21mE2JZBKxd5u0T2TZbY4Y4xhTbzsu6bJ3P8XyWds1WssboHbqCSMhP3etnaenswP6hXZxWb1uZm_dhqVtNGaW2qNelaFv1RUNoTL_0ffHQyPE8FSF6M1XzvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny4zNAd2CXH0wLGMKEzYheB3lDo63cD_yV9wzSLvZkWEPwO_GfqOpmL4x8Mp7ARt3pms1NdTwnYF3fdY_Mamx9ARcvLB98FK-vxOXhiMU566Aa8e8P3ff5K2V9rpuAzB5LRWPossQGAVLYTrRam1QHDcve_rUB3hv8iWh24JunWPKklqB6bn2_Yylj-hJwA25AR_Lu-WZ9ncb7WB0coKvZrLw-J3MyGqFxY7OZusp81wUYynoM0HrcBrXEtvbuBVbU_ng5XjDa1KO5jLM3xsl50QkV0iyUJR0vYSY6h8RTvd-m51y7wrnprC_tuigYb45fHxyxmJtWD7KSfQLajiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGoAtuH_i8guxrGavcTdOunDqovaFUJ9YxdRKO4Qf_Ut9soxHxVoD6ZKvXEVJpyVHjPxPV-qtKiSJTkl1-cB5v35vo9hFUP5iG-6ZqkyuKppfouSNcC1U_KaSDFmOBio9OOx1rj6jgg4H2rxpQkECp97Azoev1Phe5CNOT3MsDMEo3PJC-vaoL5a2FFc1q5VswL9i4WsKojRm56P_MJN6AB5aDna-u5b_CBpb3kIaNnlnDVZgbCUT-aYU5SaeKdy2wilE6og0xLDZrX3sIkMcjJTWPn4SnMyCb4Pv9ubOfAbGjYMlJUdVnRU4LYEUHkxIZrmNfJeaW7SFOiXTOHXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPQUg29-Q9e9l3wO07y5gmt26P0_8urq9C5rmpUx-AAcc-G95AIAVCpqAkuZyUzu-jFHeO16MltNNkSYpStYX5jojLPdoqXj7qpglDpxB-FfgZHBJ52wkpr1TF9mpIvaxaBBN5RZi4FaDS6OfhZPcf2cZZ3d0fi03_wXBUlCxBtPS0RozvL1SilCpn53XkWcUnzXeGBgKTKjl24PTJjFdra8Bx6E9PG-KzT19wfQ_uZOXFyJdtuDqqHgLNCdC1nzJDII1N89I7oMT8YNTyFGVPoLgm7sTgoqOy9XnsnEHXY8P2PEF8l-yBjfwSvHd7B4m156kVTwFG6cVPXC8fBPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmS1qQXvOrkvKNgaHE_HKmdD8Maxhls536SqIUSQViOy3j8NY8SJYRpPTpl0dfYZ_KYdR4cq_Okp4pQ_dC8COaKM-PuonuL3UEvc-oEcy9Rdo5UqnF7waDOmWb9I3uzvn9hBNLizrhTo-YZ6fRD2R9x8l3DsfBDWdzlVPAcA6xDzmewi8YaUy82oR9YT9ZBF5Ss3kTR1tUkj4mf8dyQthnnJiMjqI9-I4SSb4A6gzlPOxzTYeAN4vjEiwp0dxDFEmC1rTZ4wy501ZbJyRXWK3hYn3pYRXpFs89XS0AjlF5KBUOvtbx7ZxGt7HJ2c7XBkiQmhOStQXCh-qpeQSELvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUd_LxozSt__TktOq9zz1HnFpblb0TgP2p6bjnGo7mKTc7Cu8eGiKQ2RNW9FZLVvEbvHBPnpt7huy6mAhwkd9-HWcjIcp7SNF2BPovJ0lqZ2N-JxPKNyi2hVMPft1yCgnqMJbEdU0nZFhANGsJSoexJU7XNfhwEIorZFAVRppHXHmB_B7qH9z6yuDFj8IgGRBVBqTQrunhP_6Nl61jXwfJAyfAQ9sv60XBVCw7LRwLIZXk-zsn3d6jeRcvTxr2OVxthjbqy_qs98v7FqFe8lM1ztHcon52mzwEZYpT9bm6aBp_yzy5R8la6m8cIaVQB33i9cctFpH84rktQU8euGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkWM8wfZZbqI3C2ylvgh5RFMpZHydRwYW4SON_V_FAAhawxo0Si32aTST8YzqTNy9nbLjEYMhyiKhwmxfiyplFfdo9SjrIZMagppXXyIIGSB5VBKsk0zL3dLMGlo-efe1eAdYY4TIKIPNQm4RjWrWQzI87cpxgxQmsEVvyZhVlJoh7fQ5kd4l0fU1u55P9y8qTZy0NzOmdCq8uKWkMxTJctQt8Fkxv6mLBvezHqxPOGKtW_t28CS68Qmwj3vQYTwA9KI3YhGO7DcK8etpr5zCx9KL9ySkyuyWP2kz35E6cruAvPcQMqnP7wsaiB_eCK9IyfALkFkaJ5ek_v1aIsCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJVv9l0lzg-4fMU5Fds_SEuYupwql22ZdTa_96ikEmEzb-fz3gtPj7MHs_xKnu2_8VupmbXg1OJr4FrpFqRZqgib0aQLfJRM_xx2wyCN2nM9RrAlAIz7Azt6MDoHmxqufJU03_cR23NCMCPSqsTnOoD9L3iXCyLH9o9l-KhvC89jm5j4CFGQ2cyCDpuza0LwQVQjdgddY9LtJgeydkycORqXNwxzeSqb1hWCZUMYJ83L-VBYedIqilqs4QZCRlgIUjHxiSS3VQRlYdzZDU5yqjSkE-YhpQ3fuL7NeU0UcK_ahSTLcX4DHHh4lcqC5l3qhEgsBFyH06nJWpnzq67KYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=nSmCKZA8pVSj_Gc4UDw6PjAekYTGoc3AuqMRybCFBVYwCuaGB_IWcvlBga3J7maPohBzRJ7gra9ZcXBwwyhAtVlztRB32JEsy9yaJmdFywEMzkSkvhm7jY0R-lo8E057EdW1XRM9mpfPDTzgecMYKdN0cY6bhV9o-JNz2TArkNk7xV0JaZW2V0jkNej4rknoQGkdeoyqgIDbE4c04SlffC_xokpqle85YGf0O106EYPfPA5nS-j5UUKdsRssCbsnXpik_POskLy8hKScZ8mV0_n8ztXW0CszyKH5GM09skg2OWtHpEJJuvVf917Z2MhwA47wYVATiTU12WG6HUchXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=nSmCKZA8pVSj_Gc4UDw6PjAekYTGoc3AuqMRybCFBVYwCuaGB_IWcvlBga3J7maPohBzRJ7gra9ZcXBwwyhAtVlztRB32JEsy9yaJmdFywEMzkSkvhm7jY0R-lo8E057EdW1XRM9mpfPDTzgecMYKdN0cY6bhV9o-JNz2TArkNk7xV0JaZW2V0jkNej4rknoQGkdeoyqgIDbE4c04SlffC_xokpqle85YGf0O106EYPfPA5nS-j5UUKdsRssCbsnXpik_POskLy8hKScZ8mV0_n8ztXW0CszyKH5GM09skg2OWtHpEJJuvVf917Z2MhwA47wYVATiTU12WG6HUchXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9s24a8gwpShUzxlgOgPKIiALg5O6MhbkM_Vu5gO-PidyOEq-XIFS_njs19zMLh2pkM7Yfgrj6uk8KVfpKMvJMRX-hbOJYmwsdiM4C-RtaFhSJZl7Sla2ku9zoZ8VEfZ4nSFRgKpBLnYjiMhRFy2JeX7IbCzvX7dEJzlrtFknw585sgErq68i8oyShMdwAQk0p1ESQxefmcZuRY3Bl_E7ECaJTMG0cRQxMOJdf2QNIFTwTkzVckaxNnzQlqp1ZOLGPfOKizwmko6xkzJdE56HokvL_92GR7YmXUtaCxqI2iGu1P1YK9Zc0BgqoCTF7MbHQn9LQzSqSJKOLBOLfhO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6TwJeY0vGvWExLmhkvIyP9fVt7VuFwQpjGRn-wX791VnNculkGiuodaQG2e75lVK7RSoCIJgZmNCsjFPdFc4LjGVCogTI_Vq3OCP63_ZdO8J6JqEvCeXVpkVXCPGr5xocG1eeI747_C3xWzg8QPu-fynam3JnK_REGctjCOGuWGR2vAH6bnVG7N4CHUij9VMTixFuZKw-lNfSyMQecKr2k0BS2BzNj_PqmeUmo1SlTluGitY6yuu8zxc_CSAoTmvInB0wQD2mSYeiT-L65saodY8KOjJT0UOMajfauOazOk4-3BHGeinxAPSt2ais4u2ShsFtO2vK4o5mJO-m22Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
