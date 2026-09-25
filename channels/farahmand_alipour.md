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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 03:12:51</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0xQQ5psxeqFvTMrgyDmkVDUMBJxMNocfGomcmspTEPbhQQlAIyFQMipvBrToVYlnXLfBVI-PNOxMvj_G1Jm4h7QRoJRsyWTN_7sNmE1o0HiMKXZ3bBAmqQz5OXwfPi0CArOF466Qa61x-E_58YtXuupK3IEE-iS6Jvzzxqh041oIq-Hyq-QInk7_uHkFWiGR9UULYYWyOaOm2-yXlb6sBxI-LmUOB-1ajxvk_tUlu1LXL3MpSCb2xhdPwwAz1uJ35v2EKuOL8Xulv4gi69q9ISZeLJdSrgBvFdEb-Rrlw9as65y8peAaIUWeoWCbHgF2jfxWeO71sLg0uNyPY231Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW6ht1rM0z0qXldFm0P5j7hIP8Z0cHh1z3HpkOu-ZFLqPzs1TextuNY4bqgYyszVwc3cG8nv6GGXRQlnmowvJha5F3mF_ifvs5oEQxvunkiPAMjdKhFijzcYOmXPI4e9s7yYPGEyw6lJHP1WuRm-ADyOdXSy8AqtfsIyiVSyILncGJb_bavSPjBq0d43WQjQaQSrAPCKOt94nmJuiTvmnR8xfRxiKh0JrM4hdGVhQes-yW23RuMn6bDc1rMoTotvmQMnNZg4OkLO2TY8ssgfhDWrjEa64njfABOoO1FUGBeKSTAnT3p_2xdjQH2GGp6vB5iSiVgdLD-fEE0JW4ntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-dheHcdtYht02c-arrytuq_OCJi8VcLv85FGF4J4qcGzJcI1NOeOhwp3qfIhBv67sPZwYEG8qBWC4-zHMa25D4NdQg-SAZSJrVDXFWjIPgkXG_PrgurePMJayI5CJ36RaV3rP7p5O_26eItXLFS_aXRF6m5r5dykUvevjk_ZYBVTEb_An5fHJFKeUcdP_MB7NlSLL_f28lDJIlPIVDVGRAPFLEwCD1LbMT-vGdOwbX2R3Pj5HA5a7P8ftIFYK9I9ktJG9z-B4Tz2fwgmNOjcYlc6a8O74MugNZZHeO9WdjK-_nZ1FadL325HVBsfb8psEa0C4viFfjYg7UjOmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnAhhrWX8t3FMbU_GfrXbxWhLylYb6yN7jmOLPbLk73_pn6MVBNi3FhhWYUhBO3Vrlf46VNBruH0Mf-S65Hi-SqbJX-aJ6vXK4fDcegyAd12RQjN3jV21XkRPpbP_oFGv0yGPDu3teQuEld4yeZZpv0Vtn4d2nhVVtZXfnQKK6W4AlTtOAyodgxnt9jQTB2u3YvUiNYfX1soCh2A11EI0SV4EiHFX7X49Lr3daPW5ejS5UIStUqiqRG77zas1I7WZF25iaZtJEY-Qpc8z5TaIKP41u2NeEHeNbhpZ6VG73eVuC5jKkDXQOomXlRFYQh5AF2huiA533WY0JQr7NV5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JGQD50MK8Z9Jppz0vpr45BcvIQPTbyF4E6UFEgzXIQ8yNvkZaDLr38zaywfkoogZHYZGjZIM_RxjvXtbKn0aIQGJFBddZ0rmKMuCtdVasdjsVqUOWBvLrzQNrmZcAGT1CUHJAwGMDNzosNoiemdvngE4i_WBm2xwzmySREYuYqoly3rdLgS0YFylevKtUbfu8fPq6RH1VC3vJ3-Al5exQPFHlcNRekpnCfOkJcWmwWKLEW9SXzk_-V4_y8uwyqzqVyaXscQtMn-cooo40tma3CVAuBl0KD83_KI5kjckGsfTPGcR3F_J1VN7eWMvjj9dMaXedg_JOwoRZU4RIzuUGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JGQD50MK8Z9Jppz0vpr45BcvIQPTbyF4E6UFEgzXIQ8yNvkZaDLr38zaywfkoogZHYZGjZIM_RxjvXtbKn0aIQGJFBddZ0rmKMuCtdVasdjsVqUOWBvLrzQNrmZcAGT1CUHJAwGMDNzosNoiemdvngE4i_WBm2xwzmySREYuYqoly3rdLgS0YFylevKtUbfu8fPq6RH1VC3vJ3-Al5exQPFHlcNRekpnCfOkJcWmwWKLEW9SXzk_-V4_y8uwyqzqVyaXscQtMn-cooo40tma3CVAuBl0KD83_KI5kjckGsfTPGcR3F_J1VN7eWMvjj9dMaXedg_JOwoRZU4RIzuUGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC3_JxbXGqKTUz_-sOOIdPEcLtDdhvWYQydlhVg_6fTVf9gCqItna8H1L7uuRasH5zQFIXnyISzT1j8PuSCzYIvJqKTFcvmnwWS-9HnOTOJhopay2UhEQO_zwvda2SftcV2jSr0NHFEtokQOfIwwnPaQjOIh4KVWjJG-0qrfr8bqvJOUtl1vauK7DC1tqJnQ6FXoIGus4L7Co2SnT-zgs7TrijI3_TlXCtBGc5tNbROU0qoFu2L6dxZgVehSNyTgHP-Qwiy6i5m7U0uDehJqirThCDeqM4B_va4QG7_lxMGfurzo1g_QLfgXDb9vj5Jq7hnPhihMYLRjb5MJ2QQsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Fyu0I35YlBxUplJpGciXCm3FuTEISvoelEPHUJ_es64Dx7ynisIVQTcZkqXXcHhT1J0EVqhUAmBfD6VctHCLyeNwe_b0LrzidkZHManSOlyruNCkYy_R0gG1LUuILL_RI7QsMeQORcee2ZK99hXuyXcXHg6AlK4qcLkmMwhqEruNbLcF17SG_WqwojMTHJAaPxAe0u-alEe-A-4rtTo3WYFjibj0dDwlTmrqNUHToyB0JjVW3QsctO4xcanF_y4f74WYowozEzjLzZYyJH6e3whaL7UTP1Ih9JcT5zl_d5aEhjOGXx5dudhE-jElf3N-Ue5VZpiIEf95173RB6YmF5Mc9SMyLnONgeosqKuB4CabCxX71y_rq9bIzqUbm_TaIFtetkUTHD6R1CQC_Q7bFmyI5rQ13d1Oq1-8UsYTCSnZzuF8WeUvJtU5RpJHlGtSkzEENZxIWdWHk9BPxZtFJtck59W8sUbT2Pq6X90efYyNFgMff6eiP-cvut_SL7rqZ_a3dAU92tQ91CFcj_32pmJNXHOMHUHulnpJp445UyoHMtWYjct7y_7SS_-_tU1n3aZTkbydAkkU8H6FKvqSxThhMN0B2iaSq5ApzBIIuBvxJWNicwF_BbeetWqVsp_1nn9BxraJgOsaZUL8WFCs-tDH7n85bw-0ZyMSN_9AVS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Fyu0I35YlBxUplJpGciXCm3FuTEISvoelEPHUJ_es64Dx7ynisIVQTcZkqXXcHhT1J0EVqhUAmBfD6VctHCLyeNwe_b0LrzidkZHManSOlyruNCkYy_R0gG1LUuILL_RI7QsMeQORcee2ZK99hXuyXcXHg6AlK4qcLkmMwhqEruNbLcF17SG_WqwojMTHJAaPxAe0u-alEe-A-4rtTo3WYFjibj0dDwlTmrqNUHToyB0JjVW3QsctO4xcanF_y4f74WYowozEzjLzZYyJH6e3whaL7UTP1Ih9JcT5zl_d5aEhjOGXx5dudhE-jElf3N-Ue5VZpiIEf95173RB6YmF5Mc9SMyLnONgeosqKuB4CabCxX71y_rq9bIzqUbm_TaIFtetkUTHD6R1CQC_Q7bFmyI5rQ13d1Oq1-8UsYTCSnZzuF8WeUvJtU5RpJHlGtSkzEENZxIWdWHk9BPxZtFJtck59W8sUbT2Pq6X90efYyNFgMff6eiP-cvut_SL7rqZ_a3dAU92tQ91CFcj_32pmJNXHOMHUHulnpJp445UyoHMtWYjct7y_7SS_-_tU1n3aZTkbydAkkU8H6FKvqSxThhMN0B2iaSq5ApzBIIuBvxJWNicwF_BbeetWqVsp_1nn9BxraJgOsaZUL8WFCs-tDH7n85bw-0ZyMSN_9AVS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyRREGaXpfhqB640FlVL684xq3E6oIGgm5JoXEJZAsS-bxhXzIN3rJZqM-ADuA3jek4L36RVrZ76Cr6S7Vt32I9s-jOZxwNgboSZgWquG_SX8U8Nd2AD78OUZPBDUjAkBCwQvHX-R71mQIYWO8p0SlL8jt8errjEdLpwoxZks1R5AaE2iWvmpt9r530c_LUyictldAPbc0ZVVqQB6Gk2DF3ySGC2QftYTpM6IvttlJkLgNWp1y2yFiF5nfpfQ4VfKbL96oyU2Zz610tZ6WFjhw-AIDRCSDDdl7qfkZgGTNyOYUMlwsu326YkxuMy5qzSQRojObDDt_Ze0FAAYlEjZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Vtnq_9yPSJM415NwWw-HQSi9CP-g0bCnG9BmMPeXmGhfexfege8KC3q_YHiuofr7Fx3zNNB7KBdrHYVB992tpky56cfpIBz4cdutVJ3knr-11CajEJYn1NgJyW6ZGSsfgNrdDHpGKQkxADW_JiXMvOZjY2PaIqIqaeC6md-V8_tFML-knCqxO7v86AJZKU9HbmGug51LoHDpCw2OIh25LzpVwwuKUShIYwpE9Hyx8XaxbxE4dhxcV3dHENOPZrdNQse-OXqGh7z6HuOwEpMIPmRgbLRgjNJ8ocj6ce5I-_cM2YGhkoDTCnr7bJX2sKOQ9WigPDvCnHzu-2-Z7P8n8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Vtnq_9yPSJM415NwWw-HQSi9CP-g0bCnG9BmMPeXmGhfexfege8KC3q_YHiuofr7Fx3zNNB7KBdrHYVB992tpky56cfpIBz4cdutVJ3knr-11CajEJYn1NgJyW6ZGSsfgNrdDHpGKQkxADW_JiXMvOZjY2PaIqIqaeC6md-V8_tFML-knCqxO7v86AJZKU9HbmGug51LoHDpCw2OIh25LzpVwwuKUShIYwpE9Hyx8XaxbxE4dhxcV3dHENOPZrdNQse-OXqGh7z6HuOwEpMIPmRgbLRgjNJ8ocj6ce5I-_cM2YGhkoDTCnr7bJX2sKOQ9WigPDvCnHzu-2-Z7P8n8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k48l2wCNr9WUmrV-EGCBrSy_RG6gcrnyTO6Mx3WqDb1dX3eDzO9UoVDCB1QO0uQG8qn3dHHS4XWi4v_b6XmoNbsDM_bA1aHYv7C314OlfJVusJ5bbO6g475HUjj7mX8t7EBCQUZpiWZ-aD9_AL7mztY3blNAkPOKXbP9c0lrTFNs5MeStywveGtMuUHPKobv3WR5CI09rRN-3YKfjZvVrl_N2b5tMxSTifjqdimJ7-QhHVpvwRBKyTuhjyM4Wj61uZ9Ng2x45bCv65C9sKsD6QPUnkYqLl-Wt3SEoCRgQxYGeXQB0b2FglUb4McAqDyz4JFvfR3IPiX8klibZU3viA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bToJcq8j3tw4mLi3iQAoKFAg19hMQmHo9RUIJNzBzGuOunzkWZ-543OcV9kDo_m18LT9jy55DEn0t2Cu4MJDoiKALTijXLY5PJHogH2HoxPku8tIz34ycCc5Qjwb2trq0xjL9w2b7ytr2bgfT7GfEXEDJ_RUkEJjEIk2Sc0ageLec_5rKkC2um3DKQuxlEP932DQG2MDPLqRTT7rxK5qIMC0cq3JG7PmwWxItD_HfY4q98uOodIZkHouCnaKKwzeEHl1eWrr3xMwvVcyyvlZi9GX7EPTQj0zNhYtJJrpdK_ho6CcH6R0qmen7hX3nkZf3GD-qb2fdojwlPFlYgiBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAdvzIQht6RoWFkzKgWEvSO_JBg1HgPBvysEfjIuSKAnR_F_boy4i3pAK6FrOhYE7bPNhSiGBRTDQPnlcFh1jqXd1RAvZTK_feO3Dyg9R8V0_6Yxyk0DuzeMEUm6WP_9rA5p8xpznyfovJxZii9_lohgpeyjwMKxxGGp49CT-f9l7XZEp4DZgqYu3Lfc9uz12PE4-33LFiOnr5Aq2bbdU8byZ9b_ZmK0QAkZfUZUq3my6dsmANxJVrKQp0TJd28u35re_T1nPu12OIzJe7XMvf9zpPplf-fqu2mjHiOMRPPbtf9vm_XGiOMtL9dJEgqKxF7iY-X-bKbxEkNG9EjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=VXMULCT75yVR68nyiZkClnnSfQdIZ7xsIDxPrd4R15qBAXgdp_B9eSPvjkDwL694ryRvSG6u4ODLkQE9c8C-I_9UGSJXs1p69wgVVMLET5onr1ZkTxekefYV_yvZcF3U-Nvpv4NrMxfM6GhkNdrlkUqlB9-nBEnkZEG4-_fo8kaaS4ItuV2i-hiObDNT-poD1wL7AQLAWNbghrZbXK2ZaB5weNvxoAcetoo8UeBZM0lEO5_l3D5Td0gHXJYPTYEm0WTB0M1AC8bGjQJZLjxawMwiaw8OcCPpFnez84-IHIjQzzdgmd1FCDqwwg84OBGrh_aPik--yjPqO-I6pUemgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=VXMULCT75yVR68nyiZkClnnSfQdIZ7xsIDxPrd4R15qBAXgdp_B9eSPvjkDwL694ryRvSG6u4ODLkQE9c8C-I_9UGSJXs1p69wgVVMLET5onr1ZkTxekefYV_yvZcF3U-Nvpv4NrMxfM6GhkNdrlkUqlB9-nBEnkZEG4-_fo8kaaS4ItuV2i-hiObDNT-poD1wL7AQLAWNbghrZbXK2ZaB5weNvxoAcetoo8UeBZM0lEO5_l3D5Td0gHXJYPTYEm0WTB0M1AC8bGjQJZLjxawMwiaw8OcCPpFnez84-IHIjQzzdgmd1FCDqwwg84OBGrh_aPik--yjPqO-I6pUemgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkEY_MLWCtfBs0XoXQeDPO_WE1TU5QIqNstQ8nkbcu_D2wV-9yzl0wSm8-lu_eXyxJXt-4N3OyKTS_-dwD9mEnx428cF-U5gw1vbLDpuj1a5kVV4IbRo8z04dxzeQNMeOXuXGPiFayV585Zqjb9pvu8lTq62Hy8Yod1FRDk8Yi50j2Ukq3PxlwCv3_qPphyIw834g36LCieQ2J3JiirPrThO66J0x0jvtNYvLC2NFENEeI73zMtt5vuyDyh7DzlaXBva6WNj9-2nJnEY24zzrvbS2avWsBEwyze9lxrgw0Uzp6ZocUudHIMyjGMzi5FX7M0-_CEgnk58ButPD9SHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCEt0ww6TtExPWywe7JprfCynN98P-SEf7mjWL7ph8z15sHMdmsr-Y8C5y2jZhHzfwM8oPSk8UlKx-tuZBb6ZdQNgGfR7TNx93X1TfYMJ-SmKQirUJCOU6nxql5RBh5JSpBGgfjkxwkKp2Dre7GqiefwCZotsAkzMxJExxh2PMtqzCjFPqZpEkl4mDYoSYzbFBsx9I2mxQWoOCpT6AfbD1qeTt8AZergHOsBLgPJV9RWnDmEKiki9ujUingoBmcqWJ2nfPVw0IQsWdqB-eCBh5VOPEbmB3UqZDX0lh3wzmlnBuTF2oryL5yXz8Tyg8P1eJavU4gJ7NpSK8muYROwndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCEt0ww6TtExPWywe7JprfCynN98P-SEf7mjWL7ph8z15sHMdmsr-Y8C5y2jZhHzfwM8oPSk8UlKx-tuZBb6ZdQNgGfR7TNx93X1TfYMJ-SmKQirUJCOU6nxql5RBh5JSpBGgfjkxwkKp2Dre7GqiefwCZotsAkzMxJExxh2PMtqzCjFPqZpEkl4mDYoSYzbFBsx9I2mxQWoOCpT6AfbD1qeTt8AZergHOsBLgPJV9RWnDmEKiki9ujUingoBmcqWJ2nfPVw0IQsWdqB-eCBh5VOPEbmB3UqZDX0lh3wzmlnBuTF2oryL5yXz8Tyg8P1eJavU4gJ7NpSK8muYROwndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=T1xwBy7cs_EdKHwg-v-GuZ1es2FBz2NUh15tm6Tqf6z9V7LDtIMQbDMbNaI3KeQH_JJLIy42TA6BVqrOm9lVTR9C0bfRcBkxAXGBUQN_l5sDHGut5jpmrCpQR2pC4DUtM1WGbfVPYo8FWf5WZAJfbcszWi9YBJKMnDPR5cOcgKjqteM8rrg5Ztstfwj1AVEZrDQzoObdsS7kkich7saElKu28yfyGRmPMGFzYeL8UbS8Xu8CbBoEXwI-Tt6CQWeNo_Y_KQ0A7uFjAUm6JcYIz8G1e5F4C6gxXYj6DpQyHYB8-5DkKs_uydwPohrhzKY_M73xI9UtBMXDoUwR98k7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=T1xwBy7cs_EdKHwg-v-GuZ1es2FBz2NUh15tm6Tqf6z9V7LDtIMQbDMbNaI3KeQH_JJLIy42TA6BVqrOm9lVTR9C0bfRcBkxAXGBUQN_l5sDHGut5jpmrCpQR2pC4DUtM1WGbfVPYo8FWf5WZAJfbcszWi9YBJKMnDPR5cOcgKjqteM8rrg5Ztstfwj1AVEZrDQzoObdsS7kkich7saElKu28yfyGRmPMGFzYeL8UbS8Xu8CbBoEXwI-Tt6CQWeNo_Y_KQ0A7uFjAUm6JcYIz8G1e5F4C6gxXYj6DpQyHYB8-5DkKs_uydwPohrhzKY_M73xI9UtBMXDoUwR98k7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=kQUhxMkWXFbqDAHENpEfukjEaTKY9L3_hheS1FfKB5U5GqYDXLCdLpFcPie3ITuFSRtp7bnv7taM1nI1tqp8tIEU-mQxMZ0v9KTBXvdYA1QXWgnWeneJDaL2Xs26Nb3WtYW_vGKTY27PK5zCGxtB0eqcnQbzamyqQoUK8Vx3b_W6c1pUQE3Y4NANkAIUc06oN5KtPndzr8VVUXMW2ASmPsbMUswREbjfdkfuYQXQodcKBvPf7dY_YIIcfIFQs1ADRezQ21S0elgzSN85SSvEPX54UGW0sSWFMg9MAeNrdLxnosITL79JuUFVJlu0WDaoe-k4l_NoB24yqwVHVcIbKSkkF0pnpOgPOYjivOP_A9OurmCPf0rvYfOpmgUFKmFGfRg1B1lCOA7DEDbrbp-TQRz-DAqMwH58tvCjnCoAB46ZJdx267pAhV0N7Rg9C9M_5DDFYDRzxaGpmE12S-8aPPvVSoWQsUK8O1lUIq4KJRH1-G-TGLUxeDt09nK_h_eVvEiz0FRc_x8NvmU33EnkuRsbeWnEpZGVySdSWJTDRg2H0Np4gBecaxpsQJHg6dTHm2ANTBIfy-M_eo1ObduwRiO_wmjq-z_iYIhVM-wnUj4j7LQ1cU905cwc8_sLmOBWHj_4Er6109STZmglnX-kGyBCuo34ZUp1Prn1hFUrew4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=kQUhxMkWXFbqDAHENpEfukjEaTKY9L3_hheS1FfKB5U5GqYDXLCdLpFcPie3ITuFSRtp7bnv7taM1nI1tqp8tIEU-mQxMZ0v9KTBXvdYA1QXWgnWeneJDaL2Xs26Nb3WtYW_vGKTY27PK5zCGxtB0eqcnQbzamyqQoUK8Vx3b_W6c1pUQE3Y4NANkAIUc06oN5KtPndzr8VVUXMW2ASmPsbMUswREbjfdkfuYQXQodcKBvPf7dY_YIIcfIFQs1ADRezQ21S0elgzSN85SSvEPX54UGW0sSWFMg9MAeNrdLxnosITL79JuUFVJlu0WDaoe-k4l_NoB24yqwVHVcIbKSkkF0pnpOgPOYjivOP_A9OurmCPf0rvYfOpmgUFKmFGfRg1B1lCOA7DEDbrbp-TQRz-DAqMwH58tvCjnCoAB46ZJdx267pAhV0N7Rg9C9M_5DDFYDRzxaGpmE12S-8aPPvVSoWQsUK8O1lUIq4KJRH1-G-TGLUxeDt09nK_h_eVvEiz0FRc_x8NvmU33EnkuRsbeWnEpZGVySdSWJTDRg2H0Np4gBecaxpsQJHg6dTHm2ANTBIfy-M_eo1ObduwRiO_wmjq-z_iYIhVM-wnUj4j7LQ1cU905cwc8_sLmOBWHj_4Er6109STZmglnX-kGyBCuo34ZUp1Prn1hFUrew4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=amhCgUDPRzOlk0DJdfdN1TLgtH5a8SJa93l_i-bvyCn_f7aD_V_u6HjahsCJ-cE_4h3K3apxjwvydwG18Z9ub4v4dr2qrBJSRX9O-J9ayUV6oUHLO1vNXKusFRj_7BbJXzh8FALwAGBkJR1McAL6uytIENwYVqYy0aBR1GCGtKkjHb_oQdXEgaOsHQdGiuSaLW8swdoDe9stXKssNWlFtG3VTYQ8mU1_2iNqaEURfPibh-_WIxZaoZOIQblWoQi3Zis65vPD2RlKFRdq0pZvv_4B7RvUL73iRCyivYFyiD8EfgGPUJ4z7gLpHIeJmuQ4jzjfrPhADpWCGeIntEEcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=amhCgUDPRzOlk0DJdfdN1TLgtH5a8SJa93l_i-bvyCn_f7aD_V_u6HjahsCJ-cE_4h3K3apxjwvydwG18Z9ub4v4dr2qrBJSRX9O-J9ayUV6oUHLO1vNXKusFRj_7BbJXzh8FALwAGBkJR1McAL6uytIENwYVqYy0aBR1GCGtKkjHb_oQdXEgaOsHQdGiuSaLW8swdoDe9stXKssNWlFtG3VTYQ8mU1_2iNqaEURfPibh-_WIxZaoZOIQblWoQi3Zis65vPD2RlKFRdq0pZvv_4B7RvUL73iRCyivYFyiD8EfgGPUJ4z7gLpHIeJmuQ4jzjfrPhADpWCGeIntEEcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnFUI1-jwbpto9Uu40SXZYDF_S4RDgXAsDJZ5vUYAal2B_ks8WkcOlm55_-4b9XikM9zN4jppfxu20sjv1ZWNK9sPzbohxMJdY5nVzwScSSJNWN0R1TBuCirDu3m-AS1NudtkmXy64L7PoSq75fiwLfxl6DPunNpPSwv9W61-dv6k1GIlEDxgYTYB0KUUB71gYbKDXzd_sVrI6dCQxaYcJZ-UG0jE8ccjt0Wpe8n5acsxawesCLoha3UVAyCwP35MiDRnJjMvowfStX-fF1pPX7xNiH9SIyjkFcb2hE7XToG50c3_MpgAjVCxF-mOe1LciE5EUr0sTE4svN22kkDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RbKmB151dDzq1qqtN4a0f3oqMdoifIz8rjEQB-r1rUrqXxMVU-0AHjVFdyV9hvQt9UjtwgEUjAMiv0yhmnFu-GdUBD4VU7BFri9kP9Dq44BqZ3AgPDSGAn4gdUN47mJVpdEeZjz9udRfxKjo9citLVqBCA3GcE10FpjZQnUV4vPClBSMG64Q2u4d827A3YrnPZuZDw2isXemwbLRPxJwcOPOGQ5mru3C0G2YpR-u4yeXRPZMAP0SukBwNyjNAeg4gB1iijma1OZfcFKScP3ir5kwyeoShYf0BDGYb-HnT7De_KRBpu3C66WMKhPY04Zq8hPy6jSDPWcdDOCafwgv6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RbKmB151dDzq1qqtN4a0f3oqMdoifIz8rjEQB-r1rUrqXxMVU-0AHjVFdyV9hvQt9UjtwgEUjAMiv0yhmnFu-GdUBD4VU7BFri9kP9Dq44BqZ3AgPDSGAn4gdUN47mJVpdEeZjz9udRfxKjo9citLVqBCA3GcE10FpjZQnUV4vPClBSMG64Q2u4d827A3YrnPZuZDw2isXemwbLRPxJwcOPOGQ5mru3C0G2YpR-u4yeXRPZMAP0SukBwNyjNAeg4gB1iijma1OZfcFKScP3ir5kwyeoShYf0BDGYb-HnT7De_KRBpu3C66WMKhPY04Zq8hPy6jSDPWcdDOCafwgv6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=o1x_GAY8kIfEDzalKpf2ZGz-h6drhbSiMNUwm9FM6F1_mnpmmCSsF3_S9cV3JW_c-Ql6UwlUtPeHw5n3aYL6ZwMU2AeR5eLGLuXe-0Kv4BwGmRYnLQbuJyQnSQjhQP-D--0YeIKJgTbZKSwAkSd4s6YeowXlduV3pVMLQE6rGY2IDcno6H9ycGc89tlyltsznQ5kMXfd_oqQwT2gvN8kzE7QkFg1PKTvchSLOHFo1DbsP4Q6MgIX0p0kbEkuhTP7vSTTLM0q8xXcFRinzEeNCo0yljVkVuEQGiC9wvbl9EYka-vUwcxtJ9ugcNbuvin2XojjAWlrePPVPBTunbz3z5Z5NWSkzExlklPNq1uJrkwv80sK23rzamd_vQUg1fYlbceI5abSYveE_aGee5EPAoKZ2kry5ps6xs7Xqy6ahiZv_v7zZNW_B4mIfrN3177pDA-Jx8dFUHwzmdL6bJdpIVfMJoJ7CebfgzgjAQUrQDM5C-_K4pwToBLyu0xWvxXAkUo8KUiKRKHwDzMnSoFNWuurygWf4PEjj75lUhhMe3KCP_EziMAvbgI-_C8GdY2erJGi56QR1VKqMW3HIL7DzNr3AYIRUGkerIPviq3mInqNWedUy7Kzedfgw5zzrt9S_VksngrNuZxBCih5ATdGcTCy-k2B2koylLE5zNgrOZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=o1x_GAY8kIfEDzalKpf2ZGz-h6drhbSiMNUwm9FM6F1_mnpmmCSsF3_S9cV3JW_c-Ql6UwlUtPeHw5n3aYL6ZwMU2AeR5eLGLuXe-0Kv4BwGmRYnLQbuJyQnSQjhQP-D--0YeIKJgTbZKSwAkSd4s6YeowXlduV3pVMLQE6rGY2IDcno6H9ycGc89tlyltsznQ5kMXfd_oqQwT2gvN8kzE7QkFg1PKTvchSLOHFo1DbsP4Q6MgIX0p0kbEkuhTP7vSTTLM0q8xXcFRinzEeNCo0yljVkVuEQGiC9wvbl9EYka-vUwcxtJ9ugcNbuvin2XojjAWlrePPVPBTunbz3z5Z5NWSkzExlklPNq1uJrkwv80sK23rzamd_vQUg1fYlbceI5abSYveE_aGee5EPAoKZ2kry5ps6xs7Xqy6ahiZv_v7zZNW_B4mIfrN3177pDA-Jx8dFUHwzmdL6bJdpIVfMJoJ7CebfgzgjAQUrQDM5C-_K4pwToBLyu0xWvxXAkUo8KUiKRKHwDzMnSoFNWuurygWf4PEjj75lUhhMe3KCP_EziMAvbgI-_C8GdY2erJGi56QR1VKqMW3HIL7DzNr3AYIRUGkerIPviq3mInqNWedUy7Kzedfgw5zzrt9S_VksngrNuZxBCih5ATdGcTCy-k2B2koylLE5zNgrOZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlQl5th73NOmwmIQxFMysbeDhg5fwKl1-o8OScnOsE8d43T0tUoFuzgDtHk8WldBo8PvFy_VU9g3EGAc_E4eSVVFHiUdehIogfkhrPIHbOa4DhqET1k1fCd4qgiCYIiCK8vyeMFcQTp7abAhhBnhyD5a42kdis0Wva1iT2Cx_1NQs7JtEzEBkOhidfdG5ubZZuZFa__x8LuqrTyuHWyfL9EUmhrPzPKigel5dnEAW5Uw9s_M0Zk4QTNvRBnHXC-DwqkGZVlqI3HIarU8UDPxnDlRVWwmKycNhKnnshdHvUoTdDZeB-TJLb-S0PCMixEDBRSlUcf31MwT4vbJEzuPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=o2m8K0ImBViPzr1fQjQfH5e85FfcD73Ij4V6rZcK_otTnfthC--DjWJEUz5edxH82hQgG38OdwVCAlCYLPnWYd3zkdCbdhMnXa1AFAZBo62yrlUi26JrO0eCtHryXO2rcoI1PXDZQ7VzY8kS5kjhfiGd3DiE3cofgkdw2trcyhKhwdAIIeEy7Y95dkM47G3Yi-WrF1FJOfyzIuz49fz_5CCpA3O922573YjJJyV_QESMcamzNnFJuMQtadiXvLnJx1FZkALwKOGre4APj37G2DMUkMHRsFaIf-Ox4wu8M_iJJtlHzCHIggRTYzSEpwFaHCSX6lLfPV0e8ehRR62hBL_4vOCROyR1hKP_PsiHiYCeRCIkI2T3QKcgwEyZaOUm1uOq8lGxkYBR6VMqtWmzaX9Zq2hRxfeDygMI7aeknw7Tfbr3skPEj1AHkpVTQ2XDD1XILf6Gew4-hpnvaIwpIsh-58LQmF6SkAOaeE9wxiYTDJr2zZ1oCIi0xXTLWwDxmiPAyav-sQB5NtUzoB44zVw_wNfpCwcgQqd6hCxYiRnzKfPPKrUOEi-roBLXVnAp97xCJlA45qEoOuc9xgu9HjWE69Dpf1bvAxjiOc7Off_VLjKJcTuQpo6IA-suWw4ci7aeymLwvWIh4d-F4vJrF-RurDmrpNM55Vkw2fkMS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=o2m8K0ImBViPzr1fQjQfH5e85FfcD73Ij4V6rZcK_otTnfthC--DjWJEUz5edxH82hQgG38OdwVCAlCYLPnWYd3zkdCbdhMnXa1AFAZBo62yrlUi26JrO0eCtHryXO2rcoI1PXDZQ7VzY8kS5kjhfiGd3DiE3cofgkdw2trcyhKhwdAIIeEy7Y95dkM47G3Yi-WrF1FJOfyzIuz49fz_5CCpA3O922573YjJJyV_QESMcamzNnFJuMQtadiXvLnJx1FZkALwKOGre4APj37G2DMUkMHRsFaIf-Ox4wu8M_iJJtlHzCHIggRTYzSEpwFaHCSX6lLfPV0e8ehRR62hBL_4vOCROyR1hKP_PsiHiYCeRCIkI2T3QKcgwEyZaOUm1uOq8lGxkYBR6VMqtWmzaX9Zq2hRxfeDygMI7aeknw7Tfbr3skPEj1AHkpVTQ2XDD1XILf6Gew4-hpnvaIwpIsh-58LQmF6SkAOaeE9wxiYTDJr2zZ1oCIi0xXTLWwDxmiPAyav-sQB5NtUzoB44zVw_wNfpCwcgQqd6hCxYiRnzKfPPKrUOEi-roBLXVnAp97xCJlA45qEoOuc9xgu9HjWE69Dpf1bvAxjiOc7Off_VLjKJcTuQpo6IA-suWw4ci7aeymLwvWIh4d-F4vJrF-RurDmrpNM55Vkw2fkMS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=EJOnIOqhy9X4dsn2WahhPq8a_qd33S9TpBoiwtJ1vgpeOIRYiCCuHqfwyesF4SAh3oPBISaIHUn9SQRzpMkSMveirAoaOuBPhOTI9HaBIKuw_EdFtbEBi8bvsJlLLbvqa0d2vEJ6ArAwRPx7HJGNPRXKli-jKL6eyXozHqyhoCqo-RVWtDpm0vFSogh9iJqdeHBTxOGrS1sI6JDMJwWuzTZEwonfOm-4RW6PED0hw0VeJAsuESfbHSvN9rQiwtzsTFffeeLxKKDGORdcQ8zLbtyo6jTGih4Q-fZifJAHCfh__NRWZO6NgW21vDrulA6SHv9YUMtpg6a4rmvfJPdQHVF2EdjfYeEl6SoZkVEQbRIf4njYElSJz9F0QdRzwipnJzxIdEB3upKL3aIL_I4PF8Gdd33b-F1nvTU2FD_63XKNlhYTp3RQUvX6j-qjym6xzT_z4cWJnbcsUvMInFqxojFZJAr8s_oZmM2_uyLjh4ukJDf82eZEAlcrkS0LCh5FY3msjSPpJ6hw8f532rDsCiVR5xetwE_X-Kd_RfIKIfoFlY74eXIkEpO6str0K2Du1ggcg_KH5_ndkxNWSSnWvnomQnF-bi9OSWjKb1d1PbEA8zw2XBhBhyx0YNRQv-vp26q9EXVwVEDqzqOMBup0FZMldcrUvQIPRonF-WJU8K8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=EJOnIOqhy9X4dsn2WahhPq8a_qd33S9TpBoiwtJ1vgpeOIRYiCCuHqfwyesF4SAh3oPBISaIHUn9SQRzpMkSMveirAoaOuBPhOTI9HaBIKuw_EdFtbEBi8bvsJlLLbvqa0d2vEJ6ArAwRPx7HJGNPRXKli-jKL6eyXozHqyhoCqo-RVWtDpm0vFSogh9iJqdeHBTxOGrS1sI6JDMJwWuzTZEwonfOm-4RW6PED0hw0VeJAsuESfbHSvN9rQiwtzsTFffeeLxKKDGORdcQ8zLbtyo6jTGih4Q-fZifJAHCfh__NRWZO6NgW21vDrulA6SHv9YUMtpg6a4rmvfJPdQHVF2EdjfYeEl6SoZkVEQbRIf4njYElSJz9F0QdRzwipnJzxIdEB3upKL3aIL_I4PF8Gdd33b-F1nvTU2FD_63XKNlhYTp3RQUvX6j-qjym6xzT_z4cWJnbcsUvMInFqxojFZJAr8s_oZmM2_uyLjh4ukJDf82eZEAlcrkS0LCh5FY3msjSPpJ6hw8f532rDsCiVR5xetwE_X-Kd_RfIKIfoFlY74eXIkEpO6str0K2Du1ggcg_KH5_ndkxNWSSnWvnomQnF-bi9OSWjKb1d1PbEA8zw2XBhBhyx0YNRQv-vp26q9EXVwVEDqzqOMBup0FZMldcrUvQIPRonF-WJU8K8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Vd-c6-mG_RSiTDAhlu38GqjVBab5wruCzViOo28sOX1f365LYQXdsOiKXNY4Yp5tz1laDEmSXTHUM_fEwopSDIT0CF7wLEXd6BKOoIbYaJvHdoruvHaN_ZhWFgzE4R3hHhJkTQhYcdM61oq0IPwFzy_kfIbPx0aNOmeYNlV1RJskvQ58YQhB4P8zqke5ZveQVsjsW4O9J2LFF7X8LI-vJyG0YZH4w3cJfOCXZ4MPMX07Ixav7HDiscEmEBJr5pPTmDVMOy2tfoigvxIOHhZ6gK6zaHg1ebnJmvlaxP93SpwoNYBuiLM7DGkn1cGcoDQ_Wj6sANTMHO5CY0WCfHGYYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Vd-c6-mG_RSiTDAhlu38GqjVBab5wruCzViOo28sOX1f365LYQXdsOiKXNY4Yp5tz1laDEmSXTHUM_fEwopSDIT0CF7wLEXd6BKOoIbYaJvHdoruvHaN_ZhWFgzE4R3hHhJkTQhYcdM61oq0IPwFzy_kfIbPx0aNOmeYNlV1RJskvQ58YQhB4P8zqke5ZveQVsjsW4O9J2LFF7X8LI-vJyG0YZH4w3cJfOCXZ4MPMX07Ixav7HDiscEmEBJr5pPTmDVMOy2tfoigvxIOHhZ6gK6zaHg1ebnJmvlaxP93SpwoNYBuiLM7DGkn1cGcoDQ_Wj6sANTMHO5CY0WCfHGYYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=J4nAghfXnjLw9ujQ0Kq5Mu_6HlddpYzpbhRPiRIqEwHeRfSXhYYmQC0Wq18PPFlL6Ew6zmgGpJ61zJ4JndEOMh7Kb2wLnuasIirBWeh5841Ht6qplRKaNFi3znLBy5qk_zRM5kFyEHE5VrJqd0NkTSo0OEyrhLXFvGYzoCOqxkwOsk__DU4A9cs9tLEecPvD45yNhbkqgQEB3RVtLrVn2rjs69gSNIbDVL3XTZjmrDxdMshh75kvvtGPEO0Q-bDX5-CkFOCKGDmGIGmWKwp-_ibm7yY-hAanMLS4raMnKFkorjBqh2Hg_tmrtH0YhfvogHrDJil-6ZGaut2tTX7U5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=J4nAghfXnjLw9ujQ0Kq5Mu_6HlddpYzpbhRPiRIqEwHeRfSXhYYmQC0Wq18PPFlL6Ew6zmgGpJ61zJ4JndEOMh7Kb2wLnuasIirBWeh5841Ht6qplRKaNFi3znLBy5qk_zRM5kFyEHE5VrJqd0NkTSo0OEyrhLXFvGYzoCOqxkwOsk__DU4A9cs9tLEecPvD45yNhbkqgQEB3RVtLrVn2rjs69gSNIbDVL3XTZjmrDxdMshh75kvvtGPEO0Q-bDX5-CkFOCKGDmGIGmWKwp-_ibm7yY-hAanMLS4raMnKFkorjBqh2Hg_tmrtH0YhfvogHrDJil-6ZGaut2tTX7U5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jj9Koc85UOZIozMhuQtdTqByDTmfrInQ88A5sP4G55v2yQfL4KL9wwJXXIhPunMiQfj_25xyYPxwn_0sebOJbAWyCDTcGFhrloPRlr7vp0BzBLkBBu7OpmoYiyLtVR-yP4eqEMbWvC1w7adQn16IjoZWQ3ZF9tv9x9uCmnHHi2_kNPGJAJL-V4e2phtxutHs1HQ2tKqebAOHXXBMonJVo1pUUkE29EYpsIDSnz0-CuDBak29B6AUslbRe2YHnlF1o1siYEk51wb4CuVE6ZxeBDVc1XRYCq3qFhJ1wIs3BTINjV__3jveBnR4jSfxYptokSIw44fnZiuxX5nkx8gkaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jj9Koc85UOZIozMhuQtdTqByDTmfrInQ88A5sP4G55v2yQfL4KL9wwJXXIhPunMiQfj_25xyYPxwn_0sebOJbAWyCDTcGFhrloPRlr7vp0BzBLkBBu7OpmoYiyLtVR-yP4eqEMbWvC1w7adQn16IjoZWQ3ZF9tv9x9uCmnHHi2_kNPGJAJL-V4e2phtxutHs1HQ2tKqebAOHXXBMonJVo1pUUkE29EYpsIDSnz0-CuDBak29B6AUslbRe2YHnlF1o1siYEk51wb4CuVE6ZxeBDVc1XRYCq3qFhJ1wIs3BTINjV__3jveBnR4jSfxYptokSIw44fnZiuxX5nkx8gkaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=A7z4La_Qo5N-59Y2qhrynZtQ0Fj6JEj5-cnVuD83z8tr-BNuMdvBOfvY7A9O7KGZJJglAc04fbgAnHp5GVYohVWOQxc5uZwFJ5wfrJuLOhbgiUJpXt8BTtvPmtAfYkgB7_3QEZ3uJy9jjAhahncDpfEXwsoTJnw7aIK9HdfrKSr0D1XTMUy2sX8uZoIaJkk7-dqbkuX4Jw9fvMc21_Shys-NRBtM3JlosFiv3hqYFXgwts5CLIfNF6i3HhpovgVab_xs2zOWsZ23jgafGrxZMTkZTHPBnRoQhBlpSGKzECi7F-bK53RyPriRQGVYRVZTtLLzhQmVIw1H_thsNzazXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=A7z4La_Qo5N-59Y2qhrynZtQ0Fj6JEj5-cnVuD83z8tr-BNuMdvBOfvY7A9O7KGZJJglAc04fbgAnHp5GVYohVWOQxc5uZwFJ5wfrJuLOhbgiUJpXt8BTtvPmtAfYkgB7_3QEZ3uJy9jjAhahncDpfEXwsoTJnw7aIK9HdfrKSr0D1XTMUy2sX8uZoIaJkk7-dqbkuX4Jw9fvMc21_Shys-NRBtM3JlosFiv3hqYFXgwts5CLIfNF6i3HhpovgVab_xs2zOWsZ23jgafGrxZMTkZTHPBnRoQhBlpSGKzECi7F-bK53RyPriRQGVYRVZTtLLzhQmVIw1H_thsNzazXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BqUl4bEm8fSRzGLqD_W0EaPw6-6S5yNFW5yEps1DynmvzBNu2I_HAr7TjiSXQYAfGMy7N1B1ag25hRiVPGLD0_xHwrbQ2ombmAGmMONBzm4rtm9RfP6BAK7_V0JFumg3helzKN-FoAQ1felgW7lgJ4drT9UlJABpvMEvvruk67KHRH33g9EiBo2PqtQRtomqVXnrqI3t425Rrwt7TiGF3yFB3dVpwhhH3iM7kYmzX4TFIarJTRyLCUT7Booenfomf3BpK6YPCiu4EBZnkEz5U72-3KYA7q5q6sfpV_2FUwNAv3dT9j_arfvi6498yeR1oE9XZkgkdPZD90x4gPIhQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BqUl4bEm8fSRzGLqD_W0EaPw6-6S5yNFW5yEps1DynmvzBNu2I_HAr7TjiSXQYAfGMy7N1B1ag25hRiVPGLD0_xHwrbQ2ombmAGmMONBzm4rtm9RfP6BAK7_V0JFumg3helzKN-FoAQ1felgW7lgJ4drT9UlJABpvMEvvruk67KHRH33g9EiBo2PqtQRtomqVXnrqI3t425Rrwt7TiGF3yFB3dVpwhhH3iM7kYmzX4TFIarJTRyLCUT7Booenfomf3BpK6YPCiu4EBZnkEz5U72-3KYA7q5q6sfpV_2FUwNAv3dT9j_arfvi6498yeR1oE9XZkgkdPZD90x4gPIhQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=hEnnJU6RM0p2SDuTYs1okgTLGCFsvaM5xPgCxBbC-ARkpVhuqSKXkuUdbItuLsjZZBOIZzGwB9DTamHbNaR6xHR1C-nxGf5ciouiU1yn_s30MzjQgF9SLZzTKhCM2E6SgLhRobMHFRB6CdQzyO6UZP_L9y84Lp7gkJeE7czMfmLTiGxyU_kkL5vCalWZpXoyGNSuztl8y3gvhBzCJtjCsVeOyfR56W06sclSpIPaLprxF7t4eeju3963184HU4Fx03CjawDsunQi2f84B65HWsd4svKev-qm9bE_-d2rAWj9fixWrv9ZBzpjgipxMub-qwBx33DJx0uS9fCE1z9Jmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=hEnnJU6RM0p2SDuTYs1okgTLGCFsvaM5xPgCxBbC-ARkpVhuqSKXkuUdbItuLsjZZBOIZzGwB9DTamHbNaR6xHR1C-nxGf5ciouiU1yn_s30MzjQgF9SLZzTKhCM2E6SgLhRobMHFRB6CdQzyO6UZP_L9y84Lp7gkJeE7czMfmLTiGxyU_kkL5vCalWZpXoyGNSuztl8y3gvhBzCJtjCsVeOyfR56W06sclSpIPaLprxF7t4eeju3963184HU4Fx03CjawDsunQi2f84B65HWsd4svKev-qm9bE_-d2rAWj9fixWrv9ZBzpjgipxMub-qwBx33DJx0uS9fCE1z9Jmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ByQOsjoPmU161QjSLwOARrEEWO03YXwgXqrwATss9oO0XGyklmQzjk5ycHGakiFwINdhLMpTS42g5mORDUBQGy8GqIMWoix86MExrrVc8qdQmxomosnLg8PtGFV2b7KwOdAIhBlgKM8kBiuPzQ3aswI2Aa2DHVWrqb3-Gl7l-Tl8CPcessheN_YKgYqqCIr_znCaejj4GxtgZ2jOM-zBQ0yCZvW88uS-MQgUcpJOnvSWuWSsjTj7HoxdUbCwABLCdEtaD1C9zqVU5vhvMTDsVLsjlDExkbGNTeI1_Zf1_-IZQbGZCyeE67xz-mmVcBIyTOM05g0gIX38A3OOktUdaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ByQOsjoPmU161QjSLwOARrEEWO03YXwgXqrwATss9oO0XGyklmQzjk5ycHGakiFwINdhLMpTS42g5mORDUBQGy8GqIMWoix86MExrrVc8qdQmxomosnLg8PtGFV2b7KwOdAIhBlgKM8kBiuPzQ3aswI2Aa2DHVWrqb3-Gl7l-Tl8CPcessheN_YKgYqqCIr_znCaejj4GxtgZ2jOM-zBQ0yCZvW88uS-MQgUcpJOnvSWuWSsjTj7HoxdUbCwABLCdEtaD1C9zqVU5vhvMTDsVLsjlDExkbGNTeI1_Zf1_-IZQbGZCyeE67xz-mmVcBIyTOM05g0gIX38A3OOktUdaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTvXHmxL1bvwD2SOv-RPUtV3qvvNf6a70qfO-1Fc2L74vB7z3H4_5hFds2Bt4fg8UFVG4e7rXklbcBNfl_XUfxaeTRdEiUzTm1GZhVBURmvp7UWsASQugidqKrYifA2W96lYgzY82_LDygbt6ASpoQ83xz3tACyHWspfCbaKkU0sEayAgPsPRhxnsFjXfP4-PFleU6cMKs0-p40nem7L60Bo54Ho3WTlReGndpD6nFa4E164-U5RKZPmMzj_tG6ePEs29536tQ3Ko-fDo1ojFeQYSRqqe1EE6sI0HY4V14E2JiDie8R2LGikbpzkFzaihupuPfLL45F9yd_22K2kHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=NORJRKCq0O9_40vOGi7pm_HzdyxoTWAnJTdnsd_A7fMJaThKU7_DWrbG7brHtdASnkeNk-izBBa7THxZ86JvZ4g5AZCSLlPEf4u7W3R8rFkY0Id9sPRelRJF2OP2s3mBnwwL8bHsnhxgWOpXd78fYNxuzHRI5xM1IRJIGWVuwy4CSKXGFX8l4ypqRJwfQURSPvCACZPHiyz5FdNAqA5TSIRJvMTm-RVXAGXKVNtZDixwGkaIU3Awg-HdvKFRqOHQ9uNyPxT-LT-CQiXEYny0wYK38PvI9_it1i_hq3tFu0-0VcTFKNSBQpF2HP1OZyLlJKptwThVhx688yFXI2Wetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=NORJRKCq0O9_40vOGi7pm_HzdyxoTWAnJTdnsd_A7fMJaThKU7_DWrbG7brHtdASnkeNk-izBBa7THxZ86JvZ4g5AZCSLlPEf4u7W3R8rFkY0Id9sPRelRJF2OP2s3mBnwwL8bHsnhxgWOpXd78fYNxuzHRI5xM1IRJIGWVuwy4CSKXGFX8l4ypqRJwfQURSPvCACZPHiyz5FdNAqA5TSIRJvMTm-RVXAGXKVNtZDixwGkaIU3Awg-HdvKFRqOHQ9uNyPxT-LT-CQiXEYny0wYK38PvI9_it1i_hq3tFu0-0VcTFKNSBQpF2HP1OZyLlJKptwThVhx688yFXI2Wetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HT8Z4iAlYWoDKOj0-GuGvOB9uD262A9IPtwbTo12epuvTBV7daCRGxdI6HeOmq2BkRmdYbSdAOJQDyZiQGyTYiGyNf58J9cl6yJInymo8EUP5TQt-cSMuxUh5oXhnlX52Lb2K40kn9woVGbYDRAxU6TftN9R13d9j5WKdZs9SvvXTm_LvBs2WyuPBUUv9IUDFJHVEsCrLQFcVNQpy39U8jKu1B2MJt7TzIMsYniFspadrYn3cwrNSd5kjkoUYScS4Eu0oixevxQUXnJq3fkKBqMpnlirTCsClsuOb9qz5mAoikvfm06Vj5hnS4YzeIufV0qJNgW46edWYz8pGuY_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HT8Z4iAlYWoDKOj0-GuGvOB9uD262A9IPtwbTo12epuvTBV7daCRGxdI6HeOmq2BkRmdYbSdAOJQDyZiQGyTYiGyNf58J9cl6yJInymo8EUP5TQt-cSMuxUh5oXhnlX52Lb2K40kn9woVGbYDRAxU6TftN9R13d9j5WKdZs9SvvXTm_LvBs2WyuPBUUv9IUDFJHVEsCrLQFcVNQpy39U8jKu1B2MJt7TzIMsYniFspadrYn3cwrNSd5kjkoUYScS4Eu0oixevxQUXnJq3fkKBqMpnlirTCsClsuOb9qz5mAoikvfm06Vj5hnS4YzeIufV0qJNgW46edWYz8pGuY_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vooCUtCYcPHIAc_PpCQTx82QoH6tSirmv6l8rr6SjBDNRHydpKDMezSXir4IzP_F-gtOBY9YSQRkuOTlN1RE0ixcAo4qvTp9G3fS7XCyZ3m1mzvZfpyisUw29kw05JJJAXro-w4Do47vPcmRprO5bZvEN6m7-r8rb_nnKYctqu9-viUFAedBEvecc-S1RD786r7z3xHL1cJeUBCYD_mBOKtVbqiQmFuhTsSyFfx83YFyy5L-DP3PecjoFYrin3Q1H3aJSVpjfMpQOat3vYBjLbyE9UuRwLPO2ZCOE7m7vfJJQK2drcD7np_A3Pu_KWSOnskYjXpnm1bU9P4XlS3LGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vooCUtCYcPHIAc_PpCQTx82QoH6tSirmv6l8rr6SjBDNRHydpKDMezSXir4IzP_F-gtOBY9YSQRkuOTlN1RE0ixcAo4qvTp9G3fS7XCyZ3m1mzvZfpyisUw29kw05JJJAXro-w4Do47vPcmRprO5bZvEN6m7-r8rb_nnKYctqu9-viUFAedBEvecc-S1RD786r7z3xHL1cJeUBCYD_mBOKtVbqiQmFuhTsSyFfx83YFyy5L-DP3PecjoFYrin3Q1H3aJSVpjfMpQOat3vYBjLbyE9UuRwLPO2ZCOE7m7vfJJQK2drcD7np_A3Pu_KWSOnskYjXpnm1bU9P4XlS3LGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ENAIDiDbC6BU2GuAoSkMJ0L-ayfheG2zG2kM4zZJQGskP-MlMZQLOuEGVN3u27IN9txDQ8eVCgxvZEzuDHc3gxR6FQJ_rwVFxdL-kwQWAfxEM0y1dTxnD2U33yHvyZdH5Cv0ZfyFz6tvyRhw3WH7z_NjSaaEAzTkKY9gNRysWgjcxlszDwLXSigwS8NqkZW5-6ltCKEjVdP0A1EsW50uFLZU0pNbPqpCDSb2NFkGjJKsuONgc3RtdlcxF9xGCZTyzbCbyDO7dDv4Uv6y0pWxwtXnyqq3xz0BdqT-fQQU6aHxEXN5xeQRwkgRF36rJnimCzHbwO97616n0izJSWz_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ENAIDiDbC6BU2GuAoSkMJ0L-ayfheG2zG2kM4zZJQGskP-MlMZQLOuEGVN3u27IN9txDQ8eVCgxvZEzuDHc3gxR6FQJ_rwVFxdL-kwQWAfxEM0y1dTxnD2U33yHvyZdH5Cv0ZfyFz6tvyRhw3WH7z_NjSaaEAzTkKY9gNRysWgjcxlszDwLXSigwS8NqkZW5-6ltCKEjVdP0A1EsW50uFLZU0pNbPqpCDSb2NFkGjJKsuONgc3RtdlcxF9xGCZTyzbCbyDO7dDv4Uv6y0pWxwtXnyqq3xz0BdqT-fQQU6aHxEXN5xeQRwkgRF36rJnimCzHbwO97616n0izJSWz_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR-g2WT29BqnKls8tz1zH40lpMbqZnUECRLE0IpAJz_Fp4F5r82CtlQfVRjfF8Rfj44jOOvOOJcZjxLnDyf0LlP1pmxokv_GIRvoA5z9F8HIGDWF9jHmGFulGPuf7JnA59_CNTUl4pNZtbXRYHWvb_RaVQrNdWHFPm9YxN-AkO7_A4JWvUyM72UKFguF4wTd4YowPa6ORimgmeeXq0cmsHya-psfvFFxik9omuqNNIfFdQlogiGsWJEt9Q9O6mcCqNGJkIfkw7tLYOSm8f2EqE-5_f1i5VKm3u1Q1XJhuZgfZX5caJeSEz53QlS3kBp5hxgpvVgX1jwDBtglUq0-FA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Z-IjXkE0xXo0a7hh8CKoUTR1hb_6rjAoSVzvKCyGdSkb67Z3PIFmaSCdApPn5XiXqDfE9j6mXguYQA2Cbk9C-34TsViDS4QkHP_6JRNLZkeKU3M0kazARRc5pNhxu-XwcNBo-ZMU1NaDPU4ke1iwOS7nfy6NkUBIEoAcOc3yxJhPi0MxJjM1rPpaYxCUiwvrkRik5B-GZV0yJiJxjjlt-9EYVuZW9fOTr4UahbgOquyafzU4dYN1XOshorOXb65AavW0T9jBcAmhbnXumKHdqgG2CvqpLA7KeUwl0MyFh3wEBZFtgpRBrt7hN1LtC7avhwe8hHteZvnU18YaCsMH0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Z-IjXkE0xXo0a7hh8CKoUTR1hb_6rjAoSVzvKCyGdSkb67Z3PIFmaSCdApPn5XiXqDfE9j6mXguYQA2Cbk9C-34TsViDS4QkHP_6JRNLZkeKU3M0kazARRc5pNhxu-XwcNBo-ZMU1NaDPU4ke1iwOS7nfy6NkUBIEoAcOc3yxJhPi0MxJjM1rPpaYxCUiwvrkRik5B-GZV0yJiJxjjlt-9EYVuZW9fOTr4UahbgOquyafzU4dYN1XOshorOXb65AavW0T9jBcAmhbnXumKHdqgG2CvqpLA7KeUwl0MyFh3wEBZFtgpRBrt7hN1LtC7avhwe8hHteZvnU18YaCsMH0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=opwJrK5G5IFxYlhrkWtWi5cB1vTnWNvPJpqZHLTqzgejy29r04_RO8t_jvorHIhe5LQXZV970IpK4oq_xinrS4EBvhtyAYo--gCMeAj2Vc9p5pZxhhjDn1pnMBYf1HvY8f6reLwhnkOudDt1XQy3ZbCQMPnSsK8QWfaLT4atAqHdmrPS6sH2AtJV92rWyIP-gWnLZzkXZjYEH_hT4xIV0PANNtO-mKjQTly4DWt98flIeN5wdNiGfYNDm6e6yDjXLYg-tAkVwlso1U4FRkdm3_XyU4azbhr_-8M4JQ4Er0RJCrosRL8kXg6qdBFsapuO3CdVYiZAZiSVPW1gwdP03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=opwJrK5G5IFxYlhrkWtWi5cB1vTnWNvPJpqZHLTqzgejy29r04_RO8t_jvorHIhe5LQXZV970IpK4oq_xinrS4EBvhtyAYo--gCMeAj2Vc9p5pZxhhjDn1pnMBYf1HvY8f6reLwhnkOudDt1XQy3ZbCQMPnSsK8QWfaLT4atAqHdmrPS6sH2AtJV92rWyIP-gWnLZzkXZjYEH_hT4xIV0PANNtO-mKjQTly4DWt98flIeN5wdNiGfYNDm6e6yDjXLYg-tAkVwlso1U4FRkdm3_XyU4azbhr_-8M4JQ4Er0RJCrosRL8kXg6qdBFsapuO3CdVYiZAZiSVPW1gwdP03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzR2wyyCwDII5SSLU--C-ZyeRzTllNlkMJwfARkBiDoEPKcOf-CFdZ1NEc85VEZRqqLRIA2YSfxJztTwADVvQnv5eiHHxFdxMFWRabdbH46HZadTMeEH-Alj4vt3pm3a06qr0BiRgZfg3q49Cp_7TmyOZHhbKt-2NamubP9d5GClC3XgyW_F-hbX8wjSMT-AGNXoi3AioIcXEPoUXVBbxLKu4DKrEPCjUATmk62qF78JCeG6h1_3C_BBC3-DHa-rC0tG8zxwPubW04YvkCoMS7hOmMXxb1VdW0dncByAH_FfQGiR7LI_XA36vn2sgupqJxXOVLDwTUuJcduvw663EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ql3UUwvf3KYMazZkGKy5p_szk6gc_m7TAWysLQBbvzAF-_CcMDB4zaAKrEvt0Z9cf5H71i8mDjYLiGph3LvWX5_CnfcFMUPFgWD0h0Yhpy9s639gVmWn9jzUxhlFZ5rhQ3HqVOXzwo5UNZwydbJPsNwEgPExv5ydfW9SNBX8TmIB90WB9I6xE1i6kWtXGnaC7VaWY9JMPmddP1bmrWzIyRbDwdg9SemLw0rfI8zl_jt43ojSMogpfcJDp-liwbI6YsJc3Es_FtJGMIRt3Pm54YgXuDbm80JNohNCcRA_y1e7XeTpGVJma7O4xll0MtKrGhSAKmMOGDQET-zVURY6lw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=QVMFmjmxyM4uhsCl6Sm_pzzNQ7R6ZzgUIh8f58G2XwuXRZV57DFl90NGx4I50xouiPm8cZnEyKjCIrNJ_j6jnuRL0eGub_rAW9tni81BwNDxXt0Fuvnzf7BbCnFFHNbykbumnCTPXvDOigX1rS3wbvMpjEGPc16FXJLqneWI509Th8eadu52r69R19jv_0SUZqaRNXltLkVMvRF-b_TVKd-zeXl4kRSo61jT2PmDk7RxbNZW_0D8z6_tC3CpAjajtCF_tCbY97-h7_B72isxjC5nXHUVbO3S704z0VWpB_fyqUsQuLjlIm6tEF5mLkxCa1EeO40m5Wr2Zt-iPRv1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=QVMFmjmxyM4uhsCl6Sm_pzzNQ7R6ZzgUIh8f58G2XwuXRZV57DFl90NGx4I50xouiPm8cZnEyKjCIrNJ_j6jnuRL0eGub_rAW9tni81BwNDxXt0Fuvnzf7BbCnFFHNbykbumnCTPXvDOigX1rS3wbvMpjEGPc16FXJLqneWI509Th8eadu52r69R19jv_0SUZqaRNXltLkVMvRF-b_TVKd-zeXl4kRSo61jT2PmDk7RxbNZW_0D8z6_tC3CpAjajtCF_tCbY97-h7_B72isxjC5nXHUVbO3S704z0VWpB_fyqUsQuLjlIm6tEF5mLkxCa1EeO40m5Wr2Zt-iPRv1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYsy8yG42mTTbP75vkGoYNp3EIaaJehw4Hn6TNc-Ua5LgJJvUnXSW78KIX6Z5ESFM4WLG6gceYBkjYHn7EAzK3qgARQHTUkzO9dc-F7ExnHVxQWfCGwt2Wus4dY9ikFkqKQNqAtYNZ26eQnEH65qCmIgoaYK4_fyTOYYYXczpXW54Z2KSutp3o9xctlKG0X5lsJA0vs4P_MsK7r1x0kXi8ebc8TbcSehIiy9vQooKcSZ57iuaichf1CjhbUxYbbY9JVgs5TTgAjGXhnKIncTZVcyhg7dlSSVXWDsho145qb_FUsg25qiLJ_Z6pHwgtPATVtSpzuMvwTnQk3tooKY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgPxukQ2OywdJkTEh9JKl7uZDj4D-qfHLNT4reorfoTU3jNOlh84Or7TjI9PtfJJuuHgnbKQ2PsuG-bFPICuYYbJi8EICECCHMNLeWV0r6MS6KGBcwBNA2sxE2-iLosa7DQk5kfOE-zIiL7uenVwzYAewfkXr3pUQQFFEd34oiwEuS8EiLyaQQOtBBQwtYtReX-ISCRTJkPJTrn3yBUi163_duhtIfZNI-LiLCKc8knPUcF4cPFH9gfx9BPtUnL1qDjKRNDHq-Av4xHWcoVHwM9kcejHhRTgsWBmmPKlna8V281oUPdnX3kpBBax-fANgJsUGZXvGHYLVzX40Z0UuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-2o3ZXa1TFFsbX_KTKg0z7S-TnpcIaBlwy4gjjzk8wba2SF-HQ3Ompq8g_Q__iJCQkv-fmOJgmhZEa4hpVoZDjf9zhgPT711Nli4kqKhRdIj7zapTYvNKOMDE8WpYzzjoFg8oyyDatmWNPDDfOhQceBFVInHb9pjNWlOolIB6-lqeEZfbJNDdtZ_OXx60v35rlt7PJIAJlz9q0pNZGQcDAMBuniQcomFRmJMU6tW-Mi2OWk2SK5YFN-5eQHcj3dx6qfzp70AKT1XhfzUpzDoI3Qi8h2BlNuH-RPtrhIpJ0HKt3wcCUOPazQQo8nStaWNVkiYyI3lwVfcwcTdUfsAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VZ7CSnbpGUrpq3l5wrgQPeofvt6zjZYAZjOdcAS4H6QGenyv7fIUqD6XxSwNXZ91KgJw5mhIvd1wPK1LJBLaAsiB0k8BNAlh1YugwMhJp40N4mlTiPoxL_5SyM9uQKGRE7Tbf4-hjTuChpyTaiTtMjf-Ue8daHnTnxmaSwerFkCkQttQeMZBZBxscHjt2k62ghdxtBg0GaRLeOGRnWgtfqNdFDe7dAc3GYVNJ1cwDSELhziXM8yQAot-0jkS_AZFF4Lu8FYymyESLRwGe82-QiwFGXe2oW-MEmoQz2K0exowZooLZn3ysygBwlieUmcJk-GOnkCVwOVyndjxMpE9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VZ7CSnbpGUrpq3l5wrgQPeofvt6zjZYAZjOdcAS4H6QGenyv7fIUqD6XxSwNXZ91KgJw5mhIvd1wPK1LJBLaAsiB0k8BNAlh1YugwMhJp40N4mlTiPoxL_5SyM9uQKGRE7Tbf4-hjTuChpyTaiTtMjf-Ue8daHnTnxmaSwerFkCkQttQeMZBZBxscHjt2k62ghdxtBg0GaRLeOGRnWgtfqNdFDe7dAc3GYVNJ1cwDSELhziXM8yQAot-0jkS_AZFF4Lu8FYymyESLRwGe82-QiwFGXe2oW-MEmoQz2K0exowZooLZn3ysygBwlieUmcJk-GOnkCVwOVyndjxMpE9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TlqJE475fmwJB8gEEoaISiBePe1bMprQv0BK6aVdln7C_aQeNohHOdAlejW5dTljGOz7Pxo_HmrsX8wVLDfrq_1bP-vMctp8urbK58D3ueBFH0I6FkB8ghq2fNY5jtI3NhN0TpcNEjuauOMViyqQXE480kRTUCk4_ruc9_GSTQ7AKfL7pnolGnKfLXKpSTM1rFbT_K6TDLOJ35kQcKa8tqaoKTnf4Sb43ZuG-tqj_Yi99rs6_mVYSNlxISQ2dSuI77bl4Mi6_jvft212IIBYkvMAMfZZBG9XLci97p-5jEOVTb_wEA4_y_8h2c4O_ywmgmHJGbI53tSrD-6JyFQSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TlqJE475fmwJB8gEEoaISiBePe1bMprQv0BK6aVdln7C_aQeNohHOdAlejW5dTljGOz7Pxo_HmrsX8wVLDfrq_1bP-vMctp8urbK58D3ueBFH0I6FkB8ghq2fNY5jtI3NhN0TpcNEjuauOMViyqQXE480kRTUCk4_ruc9_GSTQ7AKfL7pnolGnKfLXKpSTM1rFbT_K6TDLOJ35kQcKa8tqaoKTnf4Sb43ZuG-tqj_Yi99rs6_mVYSNlxISQ2dSuI77bl4Mi6_jvft212IIBYkvMAMfZZBG9XLci97p-5jEOVTb_wEA4_y_8h2c4O_ywmgmHJGbI53tSrD-6JyFQSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bXfbVAuCXIsbvuXJjV7Z7oH_Ackpg9G462fDcus84qU5P3cUYX1o8UJsGbCsD1u7IoKGt_n6ZIWgJhUjSts0h4HVkHDey34dQaOQcoDChkA-p1OIVkXuVghYj583rTXxyJqFjjEzHo8baBi9Ug_gpb8sZu88qWQLhDFDO4x1LSwfyhaliB9kQQHvXtffydDqNOI7Db2eTvYuoVQvGww9McjbI0T4fSffxyAFd_btvhgVRgpfmZL8AvQgPrySJQglZtGNniGglA0xYtff8Ojhfbom0amq2jJ7am3jymJTzfAREB2od9k47c2IeLOolmCeu9cjcw9-N5DKkrcG4PXwiAcmSjm0CO7LLF0-99ZIMtoFK6WvFJKoJ8mnfKK2u9cNzFvXdxCxAiihprWzYUzdpGqk2Vf-mdBVD10jwtLMpo7jVCIsWES0zzJaZWUNgo8nNaB76txT47QrarJNTlimThxdAFe8qlk1wHmUySSaoRcZvXm7qOZ-jhfLnyZQZ_9gWDjEsNvZj8g214EreAuHlyAaaFMSKDwpzG5uExCpL8YRPXTUMSbnn6xwgs5UnhI-TVSzAA53WgqO16HcrVMJhvmzcOeRkCucanCz6KriwZZpOmHbyo5uIgNvPqEB7y4tHvkUKy_aqek2N-hq_x3E3kcNgGEl00ecXEg3_rsbFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bXfbVAuCXIsbvuXJjV7Z7oH_Ackpg9G462fDcus84qU5P3cUYX1o8UJsGbCsD1u7IoKGt_n6ZIWgJhUjSts0h4HVkHDey34dQaOQcoDChkA-p1OIVkXuVghYj583rTXxyJqFjjEzHo8baBi9Ug_gpb8sZu88qWQLhDFDO4x1LSwfyhaliB9kQQHvXtffydDqNOI7Db2eTvYuoVQvGww9McjbI0T4fSffxyAFd_btvhgVRgpfmZL8AvQgPrySJQglZtGNniGglA0xYtff8Ojhfbom0amq2jJ7am3jymJTzfAREB2od9k47c2IeLOolmCeu9cjcw9-N5DKkrcG4PXwiAcmSjm0CO7LLF0-99ZIMtoFK6WvFJKoJ8mnfKK2u9cNzFvXdxCxAiihprWzYUzdpGqk2Vf-mdBVD10jwtLMpo7jVCIsWES0zzJaZWUNgo8nNaB76txT47QrarJNTlimThxdAFe8qlk1wHmUySSaoRcZvXm7qOZ-jhfLnyZQZ_9gWDjEsNvZj8g214EreAuHlyAaaFMSKDwpzG5uExCpL8YRPXTUMSbnn6xwgs5UnhI-TVSzAA53WgqO16HcrVMJhvmzcOeRkCucanCz6KriwZZpOmHbyo5uIgNvPqEB7y4tHvkUKy_aqek2N-hq_x3E3kcNgGEl00ecXEg3_rsbFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sTErzzssaJJiK56yMhmJhFpV5mq0sMQaeUvysrxuH29AlM0Kv2NQF9L6Z40x5_ipSKH99LgGzgXLhNNVD9GlSF6PWEvPT_47WbXfWcUw46ix8VHD4k-TWk-Ts4qKlaNYh0eRPJQCfQWxl5XZg6PECsZqEWL3u0mS598Z1BXg0WwleR9Rz6NvU1j-NCMZCbh8EcUU856YFag9b9s06SenaDhMRJne1u7PdA66mUmSo9kkRcj8GLhTtGxDGMEEEFH7RiKZTc4eR0b4pWzE_2qvYu2IMvGgkuSCHvDn63qxM5PSf-Z7Fc5n_xkPuzg6w18UPemxzjVDwGahCEA1yFNNJ0PEDCK702Sn44_WpxxDjZgKXzaUXb5zJcRQJ_ZRkz4X3JvD4NhyMAHo75ewVeT0f_whp5tLLMdnVQ_TESrXEKur-20o3JmLNAMwAcL1JL9LE850QnL_ednzl35r172Yu4lNljupL5C9BGmWGXjRS2Vn-xWCE2oGjGxrKeqWlj9rhQoiMOR2iEXYA0Ekj7pVHRT5aBustQnpRqYAbLXtyBRcZzalP2k2PbfxhoRLX6eN88Sza16tih-vNz3zhmsXqooRn7dObGkTZyvOn6SqzO1xOGm6J8H2cGnblObEHK5pmT-KIjGwOQwO8KpiTWOX_Qvq1MVUipD6mnezk5FHAAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sTErzzssaJJiK56yMhmJhFpV5mq0sMQaeUvysrxuH29AlM0Kv2NQF9L6Z40x5_ipSKH99LgGzgXLhNNVD9GlSF6PWEvPT_47WbXfWcUw46ix8VHD4k-TWk-Ts4qKlaNYh0eRPJQCfQWxl5XZg6PECsZqEWL3u0mS598Z1BXg0WwleR9Rz6NvU1j-NCMZCbh8EcUU856YFag9b9s06SenaDhMRJne1u7PdA66mUmSo9kkRcj8GLhTtGxDGMEEEFH7RiKZTc4eR0b4pWzE_2qvYu2IMvGgkuSCHvDn63qxM5PSf-Z7Fc5n_xkPuzg6w18UPemxzjVDwGahCEA1yFNNJ0PEDCK702Sn44_WpxxDjZgKXzaUXb5zJcRQJ_ZRkz4X3JvD4NhyMAHo75ewVeT0f_whp5tLLMdnVQ_TESrXEKur-20o3JmLNAMwAcL1JL9LE850QnL_ednzl35r172Yu4lNljupL5C9BGmWGXjRS2Vn-xWCE2oGjGxrKeqWlj9rhQoiMOR2iEXYA0Ekj7pVHRT5aBustQnpRqYAbLXtyBRcZzalP2k2PbfxhoRLX6eN88Sza16tih-vNz3zhmsXqooRn7dObGkTZyvOn6SqzO1xOGm6J8H2cGnblObEHK5pmT-KIjGwOQwO8KpiTWOX_Qvq1MVUipD6mnezk5FHAAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vRWJshoIgZ8DgWpJsbVf4_yyGSD4YM1ISK1zEbdW1t_Zvctb0uBBHiUelIOM7RTNRNef2x_wtLedLug64AU4DXBVN_vN3dcMX0VFhQxLPML18VaC4dEBbwKQih1F4j7mEkHrFEbJD-vWNZcMeeJ7hQToqeAhoKwjAAdoDEG-u2dXG-1-wxbGjzfav4swMlIcQCkGrpKpUCASECPcXU55OnjpeoF3MYJnyAin0C3M56KNCSro5PY7zQYj7TlT8b0d0h3ll-xVwsx3oV_wL75Y9PkceldR4_1slxnvz2fESn6xtPv6-_zuaR0bNWOoLTLwcPi7lfYA3hTVBXcZqEhnDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vRWJshoIgZ8DgWpJsbVf4_yyGSD4YM1ISK1zEbdW1t_Zvctb0uBBHiUelIOM7RTNRNef2x_wtLedLug64AU4DXBVN_vN3dcMX0VFhQxLPML18VaC4dEBbwKQih1F4j7mEkHrFEbJD-vWNZcMeeJ7hQToqeAhoKwjAAdoDEG-u2dXG-1-wxbGjzfav4swMlIcQCkGrpKpUCASECPcXU55OnjpeoF3MYJnyAin0C3M56KNCSro5PY7zQYj7TlT8b0d0h3ll-xVwsx3oV_wL75Y9PkceldR4_1slxnvz2fESn6xtPv6-_zuaR0bNWOoLTLwcPi7lfYA3hTVBXcZqEhnDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgeiG9DLVPolWHXZswhuTJ8xhn1AEDG02DyqmKrItQAxHoBiqaodSyiBgPcBStW4qTkoHmZgYnkzneKsrgR3VMW78csY_KGqhQJp4UI_Ipt21WdShDuLkFSFFXsHx12STAOCCqdUSA04Nv93Pgp6MQsM0jQ6kZjzrWreHve6xXqZi7JYw5tBy9xHx_SkRIxTayXX-YOZC-vDrPu-VBeAFovKFwi_DvSOg_Msr27IUWGeu0k2inQl0hQ1fm1M0JZ7qvt4esCReD2VmpKvngne6aDpgzoyHfXWCXastcysDoIyze4rGblrS9zCIS1kDmcuBZ6sQGDzUjdHyz9UlIxqFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=II1-F1TWNiwAeUp3stlShJGMRbk_9DhQmYZCfgK5Zd-SMQLg757d1zVxVHy9_QAabryF7jE1w16e12ok18ml35gndycsTzUGSdWdAMnsxyWaefPyj8cbTKXpEpCJjt53rPycBjr_moCI03T95uf7Wd0OgGFQKNsPLO6W0-xWPb7rPeNHkR4CM8sPzN0opSwTnWM8wnfdkyLyp3bb_R-6HQayUkpHRTWzNnDdQ1H7v18Hz9rsq-VpPGrA-HEAPE-3ohTUHc4P-utKgRk4nMfaSV4coR85qMuNsWTd0dyBdzxUVuqjAGV13yWda9zqx7odjHfrUxnQ6vyJHbT3p3zIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=II1-F1TWNiwAeUp3stlShJGMRbk_9DhQmYZCfgK5Zd-SMQLg757d1zVxVHy9_QAabryF7jE1w16e12ok18ml35gndycsTzUGSdWdAMnsxyWaefPyj8cbTKXpEpCJjt53rPycBjr_moCI03T95uf7Wd0OgGFQKNsPLO6W0-xWPb7rPeNHkR4CM8sPzN0opSwTnWM8wnfdkyLyp3bb_R-6HQayUkpHRTWzNnDdQ1H7v18Hz9rsq-VpPGrA-HEAPE-3ohTUHc4P-utKgRk4nMfaSV4coR85qMuNsWTd0dyBdzxUVuqjAGV13yWda9zqx7odjHfrUxnQ6vyJHbT3p3zIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=IbPxERhQvX-svrZg2Zez6TVRXS1B8F8ygGiy0G0KSuAw1xy8qGt4ZwYksn4mb_hc7nMm-Xg1eprNDolzLdT_vJbLcIs2aKNZiOwJKW3XJPQ-5amAMXTUauJPI9ebololgQt4JA_yHXVTm5DqlUl_v_xl4dZ-w_BK_7leFtYGSQBFSxgpjKEcg4rYToDSibx8iVmclzqUwgfDD7TEjijMS4UDSx8oKBvTc0XWUBNQNNi8UispMnS4zD8uqjrDm06OgyDmmv_qh_fEj4zvXYHJW0ntZfdrWgbzbHFZ6yEqmKZMcwMJbbxNq1koMgUpunOBeemtVFGLS9lN2bLxejjMPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=IbPxERhQvX-svrZg2Zez6TVRXS1B8F8ygGiy0G0KSuAw1xy8qGt4ZwYksn4mb_hc7nMm-Xg1eprNDolzLdT_vJbLcIs2aKNZiOwJKW3XJPQ-5amAMXTUauJPI9ebololgQt4JA_yHXVTm5DqlUl_v_xl4dZ-w_BK_7leFtYGSQBFSxgpjKEcg4rYToDSibx8iVmclzqUwgfDD7TEjijMS4UDSx8oKBvTc0XWUBNQNNi8UispMnS4zD8uqjrDm06OgyDmmv_qh_fEj4zvXYHJW0ntZfdrWgbzbHFZ6yEqmKZMcwMJbbxNq1koMgUpunOBeemtVFGLS9lN2bLxejjMPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHbBeAME15lcwsNfLqd6gFHvZ63-ACRz25swcCB9xHSpoYEvMsQr4Bj6IGZPD9-mKZ9XRVuxsSn1rwCpwRgMu1V9tfxUOKJkfEzTJSPlWyaedK3d0e_4R450HfLEJAzi-txP_f0Z5zACYO9cqN0a7792KZL4pFd1Y15qGEBA8AaPd_-A9DsoWNhwFhlghsQ9En-gALvDxB7tsZb_shHwZPhXPBx1wCM7_3E3mJNk9dZgYhO9Cdru18p-FFHVXrPlEYXwiXjbd7jBDFzlEjd4w8iExz-I6M3Vq0OI7YmFlrHfAoxCU6u7-0QjsKzotAgGPc0hQ9RIbs5yTCanjJTt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBbQNNXwrRLM2sQmx9cFL7jXUzwsMvMoztH5Bo_YJgEGDNDLxWKpfVXzXzwa_RSYVtnzHWb5cnIo_1K_2MkOE4Oz4xxVxfCTIl3qCurTA4Jbf3vWTiaDqltYZAJx4kEiSyv37C9PO7EGnYzUMLnudJZHl0qs6Oo0Nmzqe9o-mYhVilstXOxsYBBWu03759CCh3CLXwsoks5Ki6KmjkSmxWrYuLP5wZzYD-Nn3Id2Lplge9pqG8sprbNqjz4Ts82Inap1GGY5huArBEe2HmwhnjmCSYMx50dhgSRqIylEEiEX0_f5lVHt6LGMUA_a2C0lppMl8e-AIWPmILCcjYYKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3VtJF3Rh5hTa5tI9wltH4EoHMLZMigjaVgecozFjvF2WgscP1JBdK5yPHHQDtNbVYv4RNr6EuL0TRtqx3bAdaiCr7SshiUCfQg5fs1PnzZo1c95JmOJWdrara44ICQ--m-BIadyTmDVmEOb_sgxmLvIXwcitMG1-tevH1GRRc01SVwSeAJWPea5rYq60QQ-1MD1KKNCyIRmTPHYIKoe-ahEnpgbmIDdHOiBRtjktCTkqv0-pCZyjMiFmQw2yFD2kKfgDW6EQgcf4H3kto6A7of4B3kQNZNwMDa7shDubmvuuYq0RCuQS1TnNWR8ykMS5sQeMVXl0mb4MrU1PvdDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtQCbkXMJKz5Y6-GWgNxkSvOuhMakXYQOjRCZtgjoHgQRc8Ql7d1WoHXSgpt4YV6li3lrZ2kOl1SEngwbMKSV_rPAF7-xQwwTy5p33pzp4rbHkLSAWJGEOeloGhhTprlHp1xK9Fl65eb7EdoGaGZ21zMuv_v78OB6Qkam5yWPTSFhKwhTBEvWsE4WNhei0JkJky84f7X4ufQMVHiAnmpKc5bZINnWyhNWzPo5BC2_Hqeekv1B7idMTnvLLVM_rzNEJg4bpZa8S1m2N-quydyzE1M2FaL9qE1eZUu4j0kaWfhl52LORAySstG9SCfDivNrKs-bwbFvo7pkCydTHDh0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH85JyuKlp-_ZVtwZ344gsqrwXbOIcGgXVep1EDbz2pHbjzGBLyORhP235BgWFwyJ2qKj-rV6zxXZpoaADIoEqs7tSC7R5rdYP87Y2TNBciykVAXWqelHSHSyuQbirnre2sTvxhO6BdgK6zJzxo7dYqFtCl1x3Ii7t-f_78kyVXmDmZDpLXmkL0q1i6ktc0aant6Nu_a34JkZzf6D9MH1YNzxCoKcvlJ9qKkNtPyA02lp6_ubnG8XW1r1osT69PygrjC0b9OoZXAdPLQBi8UBE1_Zxsdb-2-OwIhR0GdHFC7apPILvrdAPyjlKBl78WIKwt-psbwZ9cPkR_3-WYOvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U015YdVbZJm7EG9kTW8AZWHAp6Vrt1j4I32r7QLVabxJIRj-KaMb2kJJ8avK_q4fuMxPbalEj-jeTLhVSN3uM8Ev0-COQFkT_6TjdlUkoL5eIk-uaNPMVPy039CAM0bgmmfUVZ_K1rEmaPdfotHlN7XQ08VukCnfrcCIV8MhcJItX4WFTmKnvZUFpy79bwwvwub-eQAz3mWUIikl_KGutN2ZurF2bbu0o7CbzrajhxEnuWqp8S9uzy683WxwcYgxG7XTIVw62y67p0XsYQk4xYVZ91bp0uEl2xKTD4SSFwaDhmuaJEy0i_W_8sMV7Ap35vzS6ljIpc_DmkPwVQ1jQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikU0MKvI_jOwWfYV3SK0l5X6G9Vj1YGSW0TEdlvTu9xrwXk1fVCH9pZc3rjsl153K7N_C0-kHuYfJLCeThIXakh35ir4_Fvk3AWftZ5EqugRyki6Dt1AVekRLv_6S_sgDUd75lhOV9eP9rP1rrzTc3H2WL-aRgU-0nfZgOwZ8zEtk-4MCy9pH84zZXsrnmPKsK4zAIqBQ2MKsOVhpNA00bYiGIjwAgKft0cAjfDW2V7XdQFB9vo1KweWGKMAw6ytE7yfi6t5lksmXcnJ8m7TEejbeLza79xf8GXPoNjEmCxgxIqTATNxO63W4Dh8AcTEQkZ3Zb1zGH1L4RCRxMwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rue4WAMNQHmwraZeXRMKbrriSanebEUTdhPyNVNqwnT2KRNVeRlLdVvFX3N7CkOW_R7PG9zM8iTZmrjVtyyaVnw3awilzULGWdlWuZm8sJJRBnsaetontFpjtG9TPi-OYA1oTF0U1hdlM-LtP5Byids4dQGTm6BeWU3sXGU2o7TKOlqlUpP2L4xvv2Jcu-AVsga97rlqJ2lyFmopbJz_kjbKMX5BpsWAzJyy3OytVwf5ktojoZyD5izVm8woNmPqOzr9dflYck45YP-LCKmhlvVPmJeX7dTCJ5oInjEEH4Wj7VnAuPoTv3QYLymMtCKJFrXX0PDjS5iYsGwJ6uxXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EF8gMAmU-gkCu3GUZ57xkXxUCHMEBnwip0fBJCfT7HHT58NB0CCata4dOXu6DCyouGcaKETlyRclYdZTgkSVzrCMqFrZVxI92OLhxJ3e-F-VOQ47KhyNnNKNC5i3ZHbvcyDMsorpk4AT_qJWZYH-A39WZ7AuTi7LfQHgVjmOT1nNudLdyj3DbVs4e9BgEtiFf0JcIC-IB9tH1m2gAuwqGChf1cJw6US4alviwQOz-EPKfCrL-mQ2lBbSwrMrRIuG3L9F4H9XFG_0dT0SDU1LhqISUmHrg0w6-S7q12IYpfkawXbUaQXd2_6cwN6qEdcKnMAw-n_K6yDj78MgIpNruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIgenTe3jNL-dB_T2Ylw92XlhGJ6Q9BP4K9Tp-DA0Cwn-wWYjDLBGTfK4RIHze7emX7yqjNaDRhCk2tw6JvcS2XQoHPtUeevM21ZVHiTbRRPym20oXNOeV_-4axSPAAJ6QgfwtBJDQ35e0DupMlNiNm_1oa67QvXBbnK43qcmJEtsU_H7qPBZNWrvPxPs-nlRQovb-_xmgbd6w3ElXl342mOSglOtgk76WfF5HZ07kNPdNbDh511VAtR9BzWhqsmU4AQ5y4srrh1wnI9GYV5gCdj_E7G-B_2OQEFwyUfvUUz2ItU92qgrjmHapSUU719g6UDyX1tXJdZ-ZB4YmPqjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=MGwE8ry9SdbKN_snm_K0i3Wwqtp56xcDZm-NOyWZ0WcZr-h98i1o4XVFpSXdS_lwJ-cVqyYjfuBkvQTCGc3ltSTwOCd2S0421QI30dNy5c0Y0rmP_req8TDj9n2y0AigMrL3EzhB8N6D7UAgpNpuQulZpyXzlmW97DeaYSIoCMN-4QIwCdEwehxK7j9Cqv1e1k7Mr_b_RBUSCDnrsHP8497txxlJ3Kthdow289T7taSHd9UGSxO_5sKK6h4w0DIpjFeM2GJaV7Aw-Q0EBRgDdbHj5JXvJtKBKMeah9WTLMJpsxI_1wKxbX0Id-gM73Q4MeE83OAAO5iRAI0HfkHnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=MGwE8ry9SdbKN_snm_K0i3Wwqtp56xcDZm-NOyWZ0WcZr-h98i1o4XVFpSXdS_lwJ-cVqyYjfuBkvQTCGc3ltSTwOCd2S0421QI30dNy5c0Y0rmP_req8TDj9n2y0AigMrL3EzhB8N6D7UAgpNpuQulZpyXzlmW97DeaYSIoCMN-4QIwCdEwehxK7j9Cqv1e1k7Mr_b_RBUSCDnrsHP8497txxlJ3Kthdow289T7taSHd9UGSxO_5sKK6h4w0DIpjFeM2GJaV7Aw-Q0EBRgDdbHj5JXvJtKBKMeah9WTLMJpsxI_1wKxbX0Id-gM73Q4MeE83OAAO5iRAI0HfkHnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA8EtNSOZoszx9XkqI2jQCexJy5AHm9v_kWMPTiXPFuokroDL8c7xVoXMa3hYVh71QP6shh2ns6zLsY-T9K3E72cOgODPJZ_luQIMXhqWVCvZOwYYPEKm5gzAFH7Nj26YGzEaMtL8R0usLiJJYLj2f-U4-TsIBbbQlCJtRNpENEp7M9fk7-j61EHGswWrs9gOpcw2Pcnl58TK2w1msvPomcIl_qFOh20KpjEbM5ys_OCDqs0juy0bOyNB2u5A0KWQn1eZnnOCYWdZ4oguJeLNH4pGsmt5-_tQbGMcRK-tMu1iF83hWMoz3knDuyODvfvYnPCT9PrQxdhya0dBk8z2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKmBXKvuCRG7vbfIbF2QTvmXHLzKTBcnHJfwRJJj7A3Ply9m_Rlk4HpjjVuLIRziJcdT1gpQ_buiU2_UflmpnZKNELAj8SIgi3elhzKMAGCa15nb4fNBBRs5s_15Ll81FwKDOfSn04lJ2EvylEEFN1dIbZL3xyTXTNU0fyTP_8q67r8v8MyIAUFaIcbz6ViH7IPirbSez8Ca8k6T0yjzbkEt4OEwtnHYJCk4N8gMd3DMzDNqKRj2orR_tHAuBX6T---UJ56c-fqiqVxzX16jiRa1wGRxwTZmhekL0l2DOLUhbWn2aUFQalq1DRrVJVJeEcQOI64HhdiF6246fpvScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
