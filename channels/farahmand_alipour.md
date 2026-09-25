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
<img src="https://cdn4.telesco.pe/file/b9s-RN8kRvW2RVoF1QoeuwceXtl7CZItLZb9Wb3h4ESIhgY-m25D8oAx56M3RRAv2w0qo_XjuYFkt_gyqELFmkmf_ainJUQ6FAsuYACNQ_KIXk1HevwSedC4IR91bOLorpDoC9r3XX1ljl-dngP2BYgwyATi5_PcboQQgS7yffHR4RgZcosNmWZ2JqzSv6cshEOvucud1Ezw4eXmiAOkmiefQ--JvEBflNmoh1FlfnZvg7rXIzGpAt1ks1Ei8aW0-sbV4NpOZPi2dwgpdJ66X54QpiJbTSzwhj8QHto8I-QSEHzSP6qAE4vVS_AQNYCWdLuzKMrJudc7w7wI7m5y1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 00:06:01</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0xQQ5psxeqFvTMrgyDmkVDUMBJxMNocfGomcmspTEPbhQQlAIyFQMipvBrToVYlnXLfBVI-PNOxMvj_G1Jm4h7QRoJRsyWTN_7sNmE1o0HiMKXZ3bBAmqQz5OXwfPi0CArOF466Qa61x-E_58YtXuupK3IEE-iS6Jvzzxqh041oIq-Hyq-QInk7_uHkFWiGR9UULYYWyOaOm2-yXlb6sBxI-LmUOB-1ajxvk_tUlu1LXL3MpSCb2xhdPwwAz1uJ35v2EKuOL8Xulv4gi69q9ISZeLJdSrgBvFdEb-Rrlw9as65y8peAaIUWeoWCbHgF2jfxWeO71sLg0uNyPY231Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW6ht1rM0z0qXldFm0P5j7hIP8Z0cHh1z3HpkOu-ZFLqPzs1TextuNY4bqgYyszVwc3cG8nv6GGXRQlnmowvJha5F3mF_ifvs5oEQxvunkiPAMjdKhFijzcYOmXPI4e9s7yYPGEyw6lJHP1WuRm-ADyOdXSy8AqtfsIyiVSyILncGJb_bavSPjBq0d43WQjQaQSrAPCKOt94nmJuiTvmnR8xfRxiKh0JrM4hdGVhQes-yW23RuMn6bDc1rMoTotvmQMnNZg4OkLO2TY8ssgfhDWrjEa64njfABOoO1FUGBeKSTAnT3p_2xdjQH2GGp6vB5iSiVgdLD-fEE0JW4ntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-dheHcdtYht02c-arrytuq_OCJi8VcLv85FGF4J4qcGzJcI1NOeOhwp3qfIhBv67sPZwYEG8qBWC4-zHMa25D4NdQg-SAZSJrVDXFWjIPgkXG_PrgurePMJayI5CJ36RaV3rP7p5O_26eItXLFS_aXRF6m5r5dykUvevjk_ZYBVTEb_An5fHJFKeUcdP_MB7NlSLL_f28lDJIlPIVDVGRAPFLEwCD1LbMT-vGdOwbX2R3Pj5HA5a7P8ftIFYK9I9ktJG9z-B4Tz2fwgmNOjcYlc6a8O74MugNZZHeO9WdjK-_nZ1FadL325HVBsfb8psEa0C4viFfjYg7UjOmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnAhhrWX8t3FMbU_GfrXbxWhLylYb6yN7jmOLPbLk73_pn6MVBNi3FhhWYUhBO3Vrlf46VNBruH0Mf-S65Hi-SqbJX-aJ6vXK4fDcegyAd12RQjN3jV21XkRPpbP_oFGv0yGPDu3teQuEld4yeZZpv0Vtn4d2nhVVtZXfnQKK6W4AlTtOAyodgxnt9jQTB2u3YvUiNYfX1soCh2A11EI0SV4EiHFX7X49Lr3daPW5ejS5UIStUqiqRG77zas1I7WZF25iaZtJEY-Qpc8z5TaIKP41u2NeEHeNbhpZ6VG73eVuC5jKkDXQOomXlRFYQh5AF2huiA533WY0JQr7NV5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av-evXXpTzoGtnm26vJgdujpiQ7boD82rJ78OoRrxjATLKzNU515ylj0CDyJsyFQsAaN2ShMXHNUojIESXB37q4AErKFgRA_jtu7-udzRfhc2K0wpfJNb5qCwQd7YoFc4CsflFA0451GWDdr9ehfoD7uxCy-fjxjIoFwvYVJFxghPFI2gIEWIiBKst-qJHYeacP1hTIieIeVJV7XZonSCyKkiltYT41d89CYI3epiTNHfdcT1NLTncvQ_Xn9_odu_BrEqhOzKLp--Cza7yDJyJhUG1NDfnHzsC9bug1jO8X91j4McKphnDjav17vls7DXUYNgBKYuHOY1t0yldl2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go0hU-GSGTARIZUm0o0W30geHg923mNN-G9KB9c8_CiYZgCGhiPwvdBRQXMFmOfDlj3jF2-dCf460wbqzks5I6T3WarXXHzle5rGPrhb_w3eaPxvVO9YE_d8HUHi4LcxKk9OWvdroUpilFNKP5IGeAzeezmWrmmtg66l5iootBqWEoBsIXOd8xuluvk6dGhFpbUiRw6Yu6Zt68RQGQYBi86xEVoFY8lLkfQU2XPJremQfjSXlCglvD3kppTr0Jk8reEm1OWt8iuOS-e1U8-H4EAtZNH5D-ve7V5XqYYJLm6YS65se1AMXHHN9kgH-2IJMjhbHNE3CYG9-pYNDgXi0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuzCNAxqP1yBV9rw5ieu47gcakLbNdxtRF0rtE_U3PHiIx0k6OoE-9XFZVL7fkg6Rpb2sziRpmiUrfy02ZK0Wt2wdTRSPvEhujpdcUBGpH9rQ_Eh6fC2jlZ2gtjFhUJThF5r42nGVlcwlwV6BLLSriMv4O3bDzcllXvKhFSwpovvTWKZQVWgY5aLZpd7bcqMnVDZJqrSR0V71SrNgAsbV3U8NIP1GdMkU2L4SRYolcgmiwHPjWXdnApdh7vwOJcOi94Ja1Yu01v_DD0cP6qI7m346qBsfC3G5qtNJwItVEMiuYHIJQVNZC7NvtFW-__jP76R136TAl__M3spZBS4Tbp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuzCNAxqP1yBV9rw5ieu47gcakLbNdxtRF0rtE_U3PHiIx0k6OoE-9XFZVL7fkg6Rpb2sziRpmiUrfy02ZK0Wt2wdTRSPvEhujpdcUBGpH9rQ_Eh6fC2jlZ2gtjFhUJThF5r42nGVlcwlwV6BLLSriMv4O3bDzcllXvKhFSwpovvTWKZQVWgY5aLZpd7bcqMnVDZJqrSR0V71SrNgAsbV3U8NIP1GdMkU2L4SRYolcgmiwHPjWXdnApdh7vwOJcOi94Ja1Yu01v_DD0cP6qI7m346qBsfC3G5qtNJwItVEMiuYHIJQVNZC7NvtFW-__jP76R136TAl__M3spZBS4Tbp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4MflA5OIJsCCbeEixBL2wwtkYI0GRF7Rf0KHYgFg59c8JEvHDcF6Equm29egCSIzxxRzeq8KGRsC2xVvgFV5qge3SjmEpHq8Y2NTNlyz1cnrkjOamcn0DDVEYQtjDj6lhihNZ_ibeMi168b-ctrkAXmeYhknKQC9YGvNCzBp7_ygc_WEKgdtmhrJHQUjF9vXAQIHaj-gH8GuuT1bLmlmw5NWv8OD-JH23REH0VRlEUitXgGK2AHaXKvy0_0e1NwXaiyXV0oQf8TZzG5PIPC6Stw17stg3XCRDliLpzjlDBmbvytpRWI6N5yshPy-DEy_YOzRdVuNFrMQwmTbcGVYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ew0RuiKRFRk2xk4ibqNGDQ4k4mLYbTlPI6lPgEjCXUXl2e29Z5M_7AjkYBwkOXBXUy97dRXyVZVL9bmFOJID5SLqcv32YUs-k7_u6M16XHMXMdeQ4W_SZWlciX04YOmslXULftuTPDziltrQO_DerIUlqkacgk9iBTpKxhUn84nfKuOarIgJXofTbXF2eDOZfbQXU6U7lnz8vfTFqQUNitG9ZENNGyWlObKoL1h1IiQKJfcaRaLj-7VUniq8xvNJ4AqjSTcQ0tjNqHguHNASO3YwG6RebjVJo8qeOBLFjNFx89Se23ngCKToeBiahZlq5LvhIX6RWaeHjQ3gBEfFKZlNmFUNyEaXUe9Z9VTcaFghukH7iBsFZ1-WMfBn3FmcB5sAhPrBdfbVXRzEfbdhzjuM1ZkY0-gFVKhzId4x4UgEMJqiOJSsAnpGH-EIk4JVuxCa9bTgeRHLjeFgkTziIoaVcSJNGC6rZqDX-PMzrInOsE6H75MnJ2G0zBqzN3W5MMxTFZ6hVnobEsbd4b0vfHRpkttlgYhMmORU8yxrRRskjf1m3HWX1mmrxmovZoJGrLyAx-HCQehEifNRm3z5ACpBOIK8iFEa3sZIDy8siv4AfefN104JhXZwNW3S_6r9-RNmgji7Lhyux8YvR5WXTDdoKXgQdNh9-T9a63xjA4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ew0RuiKRFRk2xk4ibqNGDQ4k4mLYbTlPI6lPgEjCXUXl2e29Z5M_7AjkYBwkOXBXUy97dRXyVZVL9bmFOJID5SLqcv32YUs-k7_u6M16XHMXMdeQ4W_SZWlciX04YOmslXULftuTPDziltrQO_DerIUlqkacgk9iBTpKxhUn84nfKuOarIgJXofTbXF2eDOZfbQXU6U7lnz8vfTFqQUNitG9ZENNGyWlObKoL1h1IiQKJfcaRaLj-7VUniq8xvNJ4AqjSTcQ0tjNqHguHNASO3YwG6RebjVJo8qeOBLFjNFx89Se23ngCKToeBiahZlq5LvhIX6RWaeHjQ3gBEfFKZlNmFUNyEaXUe9Z9VTcaFghukH7iBsFZ1-WMfBn3FmcB5sAhPrBdfbVXRzEfbdhzjuM1ZkY0-gFVKhzId4x4UgEMJqiOJSsAnpGH-EIk4JVuxCa9bTgeRHLjeFgkTziIoaVcSJNGC6rZqDX-PMzrInOsE6H75MnJ2G0zBqzN3W5MMxTFZ6hVnobEsbd4b0vfHRpkttlgYhMmORU8yxrRRskjf1m3HWX1mmrxmovZoJGrLyAx-HCQehEifNRm3z5ACpBOIK8iFEa3sZIDy8siv4AfefN104JhXZwNW3S_6r9-RNmgji7Lhyux8YvR5WXTDdoKXgQdNh9-T9a63xjA4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bxm07zZBc4D4PXFc1KIMd8LdrA3y4f1kx-nPAb1AwitZuvtYD3DJytSK-PTLhQbTEIDVWJSEoA08r_J14wYpDg35nnNlJS2ba8wu6-CIXQ8FnDoRBdy72W5P2btz0IDRfkUD0XK-tH884Trz9W2YkoLbJG6gGPkTIvM6yLkcxVcNuo4fUyA-7REZE7a8bRxflRyLHYImepGqu8yINKjH0fM6yYogWRfJmCm850p6Iq2c4TsZoozE7culiUnuOq2wPn1uWnFvJ_CabNL2zkBtWd1IQMyVLBBFBjbOJUJk3CVvvU1XjfCR-i1Nhfo4Gvq7fRGS7P8dTpwfXun9WvjIKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bxm07zZBc4D4PXFc1KIMd8LdrA3y4f1kx-nPAb1AwitZuvtYD3DJytSK-PTLhQbTEIDVWJSEoA08r_J14wYpDg35nnNlJS2ba8wu6-CIXQ8FnDoRBdy72W5P2btz0IDRfkUD0XK-tH884Trz9W2YkoLbJG6gGPkTIvM6yLkcxVcNuo4fUyA-7REZE7a8bRxflRyLHYImepGqu8yINKjH0fM6yYogWRfJmCm850p6Iq2c4TsZoozE7culiUnuOq2wPn1uWnFvJ_CabNL2zkBtWd1IQMyVLBBFBjbOJUJk3CVvvU1XjfCR-i1Nhfo4Gvq7fRGS7P8dTpwfXun9WvjIKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=XQiwY8t0Cqn6-lN2TvhPs_mRxTXxIF0E9K6cQ-rAKKyKgkiyargNr_8AL66kQfr8c7F3fWWu-QMXnvHNcCkBml7ygxleQtBkG0AWBHXp6iKvkV4VxeKTkfj10kvosz0vtfP5UHSMW96qIA8Q2z33g2KFwxN61dcdtgIdiLn7_Nn8yrNemqWb0iahcM8pdcdSZeH5Z0GNxghWFCsv9LqrEbIuNiRBJBC6V0kYDQUs7kbhwT-vpB42AUlY9K7B-rpn_Z5Uu8x1ESy9GI5WBIKydevcP3TBvP1fMm2dCrYK2Ez3_JOFnfUUJq09frnKId2BexhOWQn_H2p0-Q2dX1AsAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=XQiwY8t0Cqn6-lN2TvhPs_mRxTXxIF0E9K6cQ-rAKKyKgkiyargNr_8AL66kQfr8c7F3fWWu-QMXnvHNcCkBml7ygxleQtBkG0AWBHXp6iKvkV4VxeKTkfj10kvosz0vtfP5UHSMW96qIA8Q2z33g2KFwxN61dcdtgIdiLn7_Nn8yrNemqWb0iahcM8pdcdSZeH5Z0GNxghWFCsv9LqrEbIuNiRBJBC6V0kYDQUs7kbhwT-vpB42AUlY9K7B-rpn_Z5Uu8x1ESy9GI5WBIKydevcP3TBvP1fMm2dCrYK2Ez3_JOFnfUUJq09frnKId2BexhOWQn_H2p0-Q2dX1AsAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=HAnMYYQtU0_z_7aknHcVfIDLQYW_hZmpn9rUq21symrm_jF6ipXabZZPrOZYsKadEqHb-hooYZURG8n9F0Yl7Dt6f0IjQJttEF0TXrMjKIyt5KbYdfFQvPRUoTgdo1A6XOEgs7YJnhTfccRD2qO-GZ2z_2wo-zFQZcJfAeaxH4oLy_bdb19A2eaH0cchQa2Wu3YmGyhxlXAM35ELWRa0Clug21XBjMu_kMkbwot5lju_7QkWnog7K0uQ61bgvwcDkj4e3_chKNOzhJD5MMTlvWyahU4mHZ-EaYsrkKGS9zu99BllBlOURnjQZsnR5hMXf9Ls6CO5-BbvXkjaO7aQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=HAnMYYQtU0_z_7aknHcVfIDLQYW_hZmpn9rUq21symrm_jF6ipXabZZPrOZYsKadEqHb-hooYZURG8n9F0Yl7Dt6f0IjQJttEF0TXrMjKIyt5KbYdfFQvPRUoTgdo1A6XOEgs7YJnhTfccRD2qO-GZ2z_2wo-zFQZcJfAeaxH4oLy_bdb19A2eaH0cchQa2Wu3YmGyhxlXAM35ELWRa0Clug21XBjMu_kMkbwot5lju_7QkWnog7K0uQ61bgvwcDkj4e3_chKNOzhJD5MMTlvWyahU4mHZ-EaYsrkKGS9zu99BllBlOURnjQZsnR5hMXf9Ls6CO5-BbvXkjaO7aQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kWFSSB0DZew-BpCNmTwaQ8WnJDRxRpFHK_CBgWqGMnA0izo_7IHBX9GnJhQSmffoTr4_186XFf09J3KRYMpHSN8GWSCUkhGEDsSbEdI_LUfgqkxBH4b6c72z-I0HbSULH81iF7VxdtCQTobGn7p0_5xQ4SCeUq6WLpOx-dcJjNcrcUxnKhJsqg6ykdz6DymJRXZGz4snrHmraw-cPOC16oaimjVxv0Zwsk5sEE3rEL78aO1u7iLosAHnu30EXWFexSW_ZLRqeMrh1HVJSCHU1pWcPVOWZUEdfC2KL62RlOMq2u8Q7CDbG-BGq18RNIRmROeIDf_vcl1Qbons8I5s4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kWFSSB0DZew-BpCNmTwaQ8WnJDRxRpFHK_CBgWqGMnA0izo_7IHBX9GnJhQSmffoTr4_186XFf09J3KRYMpHSN8GWSCUkhGEDsSbEdI_LUfgqkxBH4b6c72z-I0HbSULH81iF7VxdtCQTobGn7p0_5xQ4SCeUq6WLpOx-dcJjNcrcUxnKhJsqg6ykdz6DymJRXZGz4snrHmraw-cPOC16oaimjVxv0Zwsk5sEE3rEL78aO1u7iLosAHnu30EXWFexSW_ZLRqeMrh1HVJSCHU1pWcPVOWZUEdfC2KL62RlOMq2u8Q7CDbG-BGq18RNIRmROeIDf_vcl1Qbons8I5s4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=CNwX5RGm9aOUkpCyw9ds2MeCWE6mZAwoBnEMGQsdFZFC024GvAk9uRYxAdF2qwWS1PpssH26upQ2FvteCTU4BAWyEDwZKRLxtAHgI-JvAUPFfDDlEjHPF7_9eH0w0zjtB_EL7NMvnA8LKZceRkNPYoevoYt2JPCqSuExeHQYixko4o0Ub-dX5HQX9zCIbrL4sDSKhjoDyXbvcLVRdBLQfvkHLXmen58v0RG8oBKv4xBcKB7D80P6_22vp6Fukf0FpxmXU7e3aQWrXTt6xFnDubpbY31phf6pCxu1loGDy5ZvTTanLKPvfI-ETpuRZtyA1y5F2LcygcdxSRa71vq-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=CNwX5RGm9aOUkpCyw9ds2MeCWE6mZAwoBnEMGQsdFZFC024GvAk9uRYxAdF2qwWS1PpssH26upQ2FvteCTU4BAWyEDwZKRLxtAHgI-JvAUPFfDDlEjHPF7_9eH0w0zjtB_EL7NMvnA8LKZceRkNPYoevoYt2JPCqSuExeHQYixko4o0Ub-dX5HQX9zCIbrL4sDSKhjoDyXbvcLVRdBLQfvkHLXmen58v0RG8oBKv4xBcKB7D80P6_22vp6Fukf0FpxmXU7e3aQWrXTt6xFnDubpbY31phf6pCxu1loGDy5ZvTTanLKPvfI-ETpuRZtyA1y5F2LcygcdxSRa71vq-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=a8BbO0_gWGLZAGxngL76pGIxAhrHscA1c968elegmDQL4EdVhQHXOB95GoOko7wgecWyoIcp_mTLVtOEdtcyfNKMk8RTDopBihIYDJYPwWVk0pa3NcPZJD78QPvCormL3-NGn4PG-T-lry82lZ7Fn-Ushyi3mXRlVyWi9cjwF4HV0nuiINKiL9ym9uvHT1fJzd9yBHwrwYk8mmBuXiLo96jyBaMGo4luODmQWyM9Wek6TvebjpvXt9FxvsRWfUB8bX-IUZ3Tk2C30bv6FJgKYsQ-HEtNOxWHB2odkS_aWYM1qccFQpqXPe0W7Ztx-jrl-cAVoINeAbWTGQ2xLQpUtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=a8BbO0_gWGLZAGxngL76pGIxAhrHscA1c968elegmDQL4EdVhQHXOB95GoOko7wgecWyoIcp_mTLVtOEdtcyfNKMk8RTDopBihIYDJYPwWVk0pa3NcPZJD78QPvCormL3-NGn4PG-T-lry82lZ7Fn-Ushyi3mXRlVyWi9cjwF4HV0nuiINKiL9ym9uvHT1fJzd9yBHwrwYk8mmBuXiLo96jyBaMGo4luODmQWyM9Wek6TvebjpvXt9FxvsRWfUB8bX-IUZ3Tk2C30bv6FJgKYsQ-HEtNOxWHB2odkS_aWYM1qccFQpqXPe0W7Ztx-jrl-cAVoINeAbWTGQ2xLQpUtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=R9nsSIYDgQDVG7R3P9U-eqiwByzMtdt9olTVbYkzoiufwgd0uwb-bNM-PTAK8gw_u2AvWTJADTUvkltRSveubMpSsB_Ez6Y53L0o7VcXVtpkilPPiCJi1F77Ty6B7RnQ9X9BIiVCpFgMRlliTl17X7am9N7x7HWVqZcIoQPDkNYCyi5jbL1Pxk-EPwSPx5w1dAl5-mE60GQ37Fna95zSeZUk-oah85sEdKn9l-MMBH0s-fC__DMSZO34S-In9N7G3hivse2T3wFdawaYN8CDqXax6joikZ8lyya8oZtvLW5RyRruoJkTocQ4F1EoWhOZvCjBAQpldSJ_zLdPQN_fLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=R9nsSIYDgQDVG7R3P9U-eqiwByzMtdt9olTVbYkzoiufwgd0uwb-bNM-PTAK8gw_u2AvWTJADTUvkltRSveubMpSsB_Ez6Y53L0o7VcXVtpkilPPiCJi1F77Ty6B7RnQ9X9BIiVCpFgMRlliTl17X7am9N7x7HWVqZcIoQPDkNYCyi5jbL1Pxk-EPwSPx5w1dAl5-mE60GQ37Fna95zSeZUk-oah85sEdKn9l-MMBH0s-fC__DMSZO34S-In9N7G3hivse2T3wFdawaYN8CDqXax6joikZ8lyya8oZtvLW5RyRruoJkTocQ4F1EoWhOZvCjBAQpldSJ_zLdPQN_fLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoZJUaqdhEQj127tv7m6V49op28FPrSZuXNSV0uFvNHtCKmzwDiCOtk-hQhSZ2aY5MqLm1yRGGs9zD7VVsKrZrdaMGDE2J3bihnOL9Y4NkmcnRToIGqxk9WAUWZamuyb4Q1XaY_AdsUev2FWClvXtoaqD5RgoQhNwyAlVRToZGWh3GCH6dOOqkZQdhvVwEJEWqE_s1gNimKCNoLM_AH8PrqWULzIVUVQuwc1l5Yzu2olGLaewXHqcfJxIvoZkvNbKXxRSThoS8ykZBC4g-RTUpakc2jPDLe2LbMMaYMGauu68CI_RHS6ZYQ5XC4W7XvE4Jt6eNjkTG6h-l-hW8AvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f42mrbHntCR4HD8RnvfMUDjLYmriHXSGv_v8Th3T6v0IFbXf8Zo_DRUq5vyI6-VFjyIQShPYAw-I3KEZPLpWcdknFBeTIUbkX94GaS09gyfaUrd_mgmuWv4BzsTu4uaruJIu3jlt24L7_i0PbGJvM2TQTz5oT-ooRcEsEeLJzf-E8M1I9A8oeKn-_lMnqZeXeeD5BOagGkVPTUyKUvVG2iv63B5QEQnMCWWiYW-GuikOrBMi6Vaaqp2p5ckK9A2iaabr527S_GXS_bFV0hMlqOW8sIa-p4HpFL3O-pJAfXxa_ml43JkgHszImlr1N3FsInv9e9fBUbZh2OrO61S2QQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=g1r9JI14rhlLqgX6F2GQqMNZR-gWPdOmIZpS__xQsFKVIZiRUvRoyj8ygTj-cllIrYCMlXUy8eL96P06VZx3tcsQp5BaA0vYZxHdbKeNKDoWKdYZw3FveTMiKeXLoHitOgyiwQzP_ks9LoFGu2L8infGGgP5UirZ1-4QCxGZzkUeQD-0k8mwyzpC0hCRlhR-RmiY-QZ0cMoQGKBOlRJ0XMENo1eGHyXr44ZdZeSgsbEV5I8aNpdgTVJT_m_ga_nzAuD_JDMShl8a7EnMH5erx8khch7akGq9w67UJgSX_XuEoJgDJzK6j56f-iUlQ2QTGzf3xy1s9zjFFVNaXoPNCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=g1r9JI14rhlLqgX6F2GQqMNZR-gWPdOmIZpS__xQsFKVIZiRUvRoyj8ygTj-cllIrYCMlXUy8eL96P06VZx3tcsQp5BaA0vYZxHdbKeNKDoWKdYZw3FveTMiKeXLoHitOgyiwQzP_ks9LoFGu2L8infGGgP5UirZ1-4QCxGZzkUeQD-0k8mwyzpC0hCRlhR-RmiY-QZ0cMoQGKBOlRJ0XMENo1eGHyXr44ZdZeSgsbEV5I8aNpdgTVJT_m_ga_nzAuD_JDMShl8a7EnMH5erx8khch7akGq9w67UJgSX_XuEoJgDJzK6j56f-iUlQ2QTGzf3xy1s9zjFFVNaXoPNCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmIHAkTZm6peE17LFCLJhcgguU06aX4bTkLUbA2EN1eW5gTXruQUfQ_Q6f8xoQeOI4kA-7tVaZ9KFgvuP3VU-X3KyQEzkSfTCCgwJNuFcoY_szbLuLNsGG153Ab4_N4KqPPJaOVxOnKyOyziuYqwjhUY1UVx83BXFnk0fCF5s_FkxWayVfk-m13ZHwOHszzuLl5j4Oj37n_wDw-IrqsEN7APMCGXw787EEAZtRUm6EIPtbDiHYh1T3R6RGZVrWbQsdz6A9usGmsgZGnAUbwO_GcuBTrK5hBUNF9OF8gNYvoGXaPccr_3x7Bc33tJ-O6eODWYA3KKaOXCh4LVmSLXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYQIns5ykVWqTCaCQDosNBmmh2yRNSrJiN9g-g22ctWzTKYuwfoT1qTeGzLQo4IL1s-rOStYyPrvm076H-uVCX-lEMiI5o1H8tKbn1Z78TFfYVUn4KkqJS1gvv51zJJWLtF2n7gyH3jvFTFkmIhMs_PDuPlRt0cu99H5B7FYjK-kQ6fkWcHZyWgo0EzgJ0IihAcBNJ-RpJeAjy3z2_cBZpYReSJR6i1H-crSBhk0PXO4al5Ts0tgyc68IgCb47l0mMY4AiHOsDtNuG2vhf_NMoFwPnJOILo0aQxSdn9eZDPJegANvqNIcOhnYW6OqYrRsyD18rClL1ZTxfHVdmQ6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQgf_Q_KOqleccq8kWTneZsaNZpFYH4jwR0BUa_VDc5jjPEpOZv_ywHe8Fe3j1WANjb0k5IZpVWGSDo2l1TdCkgwqXb2_aAIeRSpWhHraS5GrjzSDHIyi9IvuXn93IrB4IaOJaDBhqPTbpcVQUy9nn3zqHvhc7__2oasON7r4os-A3SJ9geVOjkNQMr67JNjPnsK3ufUQ5LGU_hL7PJljAjid87IGIkbYCZkMYPmqvB5oqG0tb2JYoYdX6z7THdmpL-28dtq8Tl265_ssODaCUpLcU4Sif-adfB5gOJACOeB-wP0tBQ0LLyfflLOd4QSTR3UvioXKg6_TK08bwTFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=K4nygp28SjF-ILH7VWjRSH_ntqvNoZso9yvx-EVGBgaIs313WEJ_aPpilN9F2ww66fUk-F1KimkM-e4MlAwWeW0Kyzdm_iIDBE35n7lrDjPTppAkJ81fDbM7YecCr7gOk0GXzBOywQAmaIqIvtULVLIhQJsl-bAQ51S0_uPP97im9y2ZR7MqdNhoT2OwbwxT8bheEMOkmW70sS8H7SlPK8MocNzhfJbAYGmlFFf3yawYQcr6Z5BshpPRP7Jem1tX2Yd5hjCkEUAdr4CL5XlRUaabPYUNtV5duRBBRCukyMe7NYenjOa1sScuMNTJUnqeatzVFYp8RNFH_vnZAiV5Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=K4nygp28SjF-ILH7VWjRSH_ntqvNoZso9yvx-EVGBgaIs313WEJ_aPpilN9F2ww66fUk-F1KimkM-e4MlAwWeW0Kyzdm_iIDBE35n7lrDjPTppAkJ81fDbM7YecCr7gOk0GXzBOywQAmaIqIvtULVLIhQJsl-bAQ51S0_uPP97im9y2ZR7MqdNhoT2OwbwxT8bheEMOkmW70sS8H7SlPK8MocNzhfJbAYGmlFFf3yawYQcr6Z5BshpPRP7Jem1tX2Yd5hjCkEUAdr4CL5XlRUaabPYUNtV5duRBBRCukyMe7NYenjOa1sScuMNTJUnqeatzVFYp8RNFH_vnZAiV5Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=tRj5U5rdZjatoklndPVoBjPGiZsl2_vYeoJtQSrX0ciUJlD9Pk4SLquUkmHxOC9fzrWnYq9SOFaUK2LvNkIa1VWRlAsHA_IOJN7QR8HtzDJyAiBzwa8wwwDVnx-UencmNnSsyIeCgPzSixDiDFAVbVuNE8Yp9RUSQx7GRt1EiZEqyyiyObZNtiY0pYWZkOU6Fi7b0u5nX498hWt-jhTobBlJb1AGRGOw-q-2YT5W_lzK027cgQZqeo4uLzPWbixhwf3TMTsqjq0wlBDpNpLmOsP_3goXwPOYxXgOepgsN_gKkxdjYCpO0PUzDu6azmczVr3-fHqywDoUzId4vpO1CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=tRj5U5rdZjatoklndPVoBjPGiZsl2_vYeoJtQSrX0ciUJlD9Pk4SLquUkmHxOC9fzrWnYq9SOFaUK2LvNkIa1VWRlAsHA_IOJN7QR8HtzDJyAiBzwa8wwwDVnx-UencmNnSsyIeCgPzSixDiDFAVbVuNE8Yp9RUSQx7GRt1EiZEqyyiyObZNtiY0pYWZkOU6Fi7b0u5nX498hWt-jhTobBlJb1AGRGOw-q-2YT5W_lzK027cgQZqeo4uLzPWbixhwf3TMTsqjq0wlBDpNpLmOsP_3goXwPOYxXgOepgsN_gKkxdjYCpO0PUzDu6azmczVr3-fHqywDoUzId4vpO1CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jVc6vLvv7nn-rTCtkdADAZx6m4Prc02sRgz5gXdIxpSuEtFqi_DT5RW_Kb_bRXQsoIZpJaEBwBfYFCGC5Mt1hWQJGDkag3OEWFxd-ZTG8wth4JJoR6LyoIrCFefrS5oiC-duGvkdmeP7vT863VVs_GtIHlLWUnFclLff3FdpJezvs5ScSL1TPhKNGhLQ-bqiiPV9bLza2JDJ7FsqcUCaBylTLC1XE0S6dEkv3hQ5KDBGx0PLtC37YL3Rso0ZLEhOlfD_gUs3G148uG274c9X-sECf5Jjli9Q7pavhPsxo2ynyf5jxSaVcw-79nOWrcx3EgF6_c2zxMliIILwJ-1FXBjV1KzkXiFa6fZ8xNsyHtGtCJ7bqhksgbcixXDsqSR3a26Ex7mEnIZGgfRDY7nBD9St4OL-9MzVTmmnfQahT18kc2HiZb2VvnjMBJtYfgmTza9wCFc4Z2VtCMH9FtBGbqGyLjFz4UOjw8G-9PPap1Efp3epQUf9aVTfCqL8pPH1to3qNvQ1ek1R217Qrn3E24tb5Yh447ZrTcrisI3uI-dIddqRYEGg3PFsRW9CAKC2cRCKLRTRzGIScMIIIZlJiYYnjjt7trZp1P9p1yCnN1SZbwSiia1KAmN9s-vXkohySircRYNB5B8YVAL2cVz36xMRt6s8n3XSp41HE74VR9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jVc6vLvv7nn-rTCtkdADAZx6m4Prc02sRgz5gXdIxpSuEtFqi_DT5RW_Kb_bRXQsoIZpJaEBwBfYFCGC5Mt1hWQJGDkag3OEWFxd-ZTG8wth4JJoR6LyoIrCFefrS5oiC-duGvkdmeP7vT863VVs_GtIHlLWUnFclLff3FdpJezvs5ScSL1TPhKNGhLQ-bqiiPV9bLza2JDJ7FsqcUCaBylTLC1XE0S6dEkv3hQ5KDBGx0PLtC37YL3Rso0ZLEhOlfD_gUs3G148uG274c9X-sECf5Jjli9Q7pavhPsxo2ynyf5jxSaVcw-79nOWrcx3EgF6_c2zxMliIILwJ-1FXBjV1KzkXiFa6fZ8xNsyHtGtCJ7bqhksgbcixXDsqSR3a26Ex7mEnIZGgfRDY7nBD9St4OL-9MzVTmmnfQahT18kc2HiZb2VvnjMBJtYfgmTza9wCFc4Z2VtCMH9FtBGbqGyLjFz4UOjw8G-9PPap1Efp3epQUf9aVTfCqL8pPH1to3qNvQ1ek1R217Qrn3E24tb5Yh447ZrTcrisI3uI-dIddqRYEGg3PFsRW9CAKC2cRCKLRTRzGIScMIIIZlJiYYnjjt7trZp1P9p1yCnN1SZbwSiia1KAmN9s-vXkohySircRYNB5B8YVAL2cVz36xMRt6s8n3XSp41HE74VR9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=GtZr9jWBzd6YyR8GAXVtyLVHG9n6vnkK1p6SMID2I6CgevxcR20sf3ynLEouHvQfWwN6tb_ApbkLwY4-7NxU9VuWDVMaHqmiZshIGKXtmpiaoiP7K-Ffo--V6NAwq4NKIvNbpoI8DnoSZfKSm14XHvYVMH4hvspnvi3MQytUoirCIg8KET54DkVOP0yD66675C3AfRzUf4fSn1P1pjo5SNPshRJMZ2_xtXXp_ccQxJrrONU14myRwoPrK8XiZ74Qpg0kF9pM-czZtaJWax28q0ym5nMulWu8xbYYaNlmAjF82O1g-gmJLKD7X37pkPHp3pPh5Wc3vlHWd87ly_v9M2bmIGd1KQnvrrp6HCiRSi6qeGORQiika8aF4nKvAxUZTjykf5j0K3TTOaQAIoMlqQOQCQFnGBdsCZbk6zcwl211Bj2nRW8yDyohBHK1sQRY8sZzIdy3UvM5-urWFVPBFF3zKEXjcZqmTP3FdmNBf6qYif6pzSD223__vLt5QeCgS-yMZmZ5gM4Nw7eBQDGV_nRgztR7wI4IFgvhlScBecoGj_tUuMdbU8XbDMUbnj2kap3SYoCD0kDf9RWr4arVNjJjcJtIbo5-CRD9co3BPqLbuupr3epjOhRLzDB8Ll6Rd7eIJMxGZJJNVtlnkqGtRGBat2KwyysA2u91N8Gut9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=GtZr9jWBzd6YyR8GAXVtyLVHG9n6vnkK1p6SMID2I6CgevxcR20sf3ynLEouHvQfWwN6tb_ApbkLwY4-7NxU9VuWDVMaHqmiZshIGKXtmpiaoiP7K-Ffo--V6NAwq4NKIvNbpoI8DnoSZfKSm14XHvYVMH4hvspnvi3MQytUoirCIg8KET54DkVOP0yD66675C3AfRzUf4fSn1P1pjo5SNPshRJMZ2_xtXXp_ccQxJrrONU14myRwoPrK8XiZ74Qpg0kF9pM-czZtaJWax28q0ym5nMulWu8xbYYaNlmAjF82O1g-gmJLKD7X37pkPHp3pPh5Wc3vlHWd87ly_v9M2bmIGd1KQnvrrp6HCiRSi6qeGORQiika8aF4nKvAxUZTjykf5j0K3TTOaQAIoMlqQOQCQFnGBdsCZbk6zcwl211Bj2nRW8yDyohBHK1sQRY8sZzIdy3UvM5-urWFVPBFF3zKEXjcZqmTP3FdmNBf6qYif6pzSD223__vLt5QeCgS-yMZmZ5gM4Nw7eBQDGV_nRgztR7wI4IFgvhlScBecoGj_tUuMdbU8XbDMUbnj2kap3SYoCD0kDf9RWr4arVNjJjcJtIbo5-CRD9co3BPqLbuupr3epjOhRLzDB8Ll6Rd7eIJMxGZJJNVtlnkqGtRGBat2KwyysA2u91N8Gut9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Y3JVRKeNTuxU7An34CycIG_bO8faU21SBigKZ6do6hS7CxgY1Osl8lNGGaTTItXK2gVt34etvehO2p_UuhzEk0MSzzWu3XwCWeww7KCETNrvntk0J8kU2pfpdI--5AchBkFm76Pn3aho_eWcXCixzfcGQFzPNcRKwVncb4-pCd8MFA1Tvbb-BuSpTSZ2O6aF59BIPgaDq_Uu9YrtlpLJUh5FUcdvKeGaSTV36IBldEYwa_vajNOJUeq4LuiHU-NZCIE9s-jok3WG9plKmIW74SjT6Buq899A_LiEY-ONyHlJGqbTzSUcypUSs_ANBR7OeQaqaSyw5cIO4clkrngAhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Y3JVRKeNTuxU7An34CycIG_bO8faU21SBigKZ6do6hS7CxgY1Osl8lNGGaTTItXK2gVt34etvehO2p_UuhzEk0MSzzWu3XwCWeww7KCETNrvntk0J8kU2pfpdI--5AchBkFm76Pn3aho_eWcXCixzfcGQFzPNcRKwVncb4-pCd8MFA1Tvbb-BuSpTSZ2O6aF59BIPgaDq_Uu9YrtlpLJUh5FUcdvKeGaSTV36IBldEYwa_vajNOJUeq4LuiHU-NZCIE9s-jok3WG9plKmIW74SjT6Buq899A_LiEY-ONyHlJGqbTzSUcypUSs_ANBR7OeQaqaSyw5cIO4clkrngAhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usOGXmsY0LMDEQLOMyyNJfrnuSK4SDdaa6blu4G5l4QQQtQN-rVaURmrYZp4wx_IXw4lkvWMrBEh_jKVcjTMMc6BvF-xjw7QvDpzcRKrhIYdnMIvQs3A78lgAmEjrqpNKipQRCjcqBiIbaMG4VFs7h8_GigU7wz8Tzg2GllXtNpfevtllFo56gXUxztgJSyPwYC7-ZJxyz--KmKpWkD3-9RSnggsvNaQNbjPshunmwn_brpH3jVep_Gb_tLpAFfXeI-m68w9HjMNG3_9_Zkbhzjap5lUYCZjs5Xc-DhMmoMk0VBFQk0ib-wxeraqG2bUqPmpmjDxEklBRn8HZUql0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RRI0bBdqicwf6ztIAa8lx3X_c1Mj-iBxZmGUiVDseaid0iWjPGiHLRRJJ-B_LxFHJwMNuBckxZO81HFj-oIcokKuBCMTckMiH_1VABcor3ssrO3ghad1jHsNvZWCaxySqSr643_G-q_w22CbXmw3aWparNhTzXqjntH8pIutmoJcQ5faCGn76Mn85PFzZrpNGVYnYpBo6ehoy0F4clGMRsE-ewmAtRr088ntS8BAffsskibnsVCBIpcMIbvBFL0jf2VSJEtbX73-uzrc9hiCvO5BgDHZBxL50gXsPvICRx_NKg8n4Ldl9I4SR8LiB8I11Kj7QXoeYNuPPdweBZ8bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RRI0bBdqicwf6ztIAa8lx3X_c1Mj-iBxZmGUiVDseaid0iWjPGiHLRRJJ-B_LxFHJwMNuBckxZO81HFj-oIcokKuBCMTckMiH_1VABcor3ssrO3ghad1jHsNvZWCaxySqSr643_G-q_w22CbXmw3aWparNhTzXqjntH8pIutmoJcQ5faCGn76Mn85PFzZrpNGVYnYpBo6ehoy0F4clGMRsE-ewmAtRr088ntS8BAffsskibnsVCBIpcMIbvBFL0jf2VSJEtbX73-uzrc9hiCvO5BgDHZBxL50gXsPvICRx_NKg8n4Ldl9I4SR8LiB8I11Kj7QXoeYNuPPdweBZ8bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LGH6r2o8yXnM-nd7zd5SXugGkv6bvRG__nb7SS_NBmeScHKYAa98E-NytuLI2PvyaYTEDRCPE4lBeCPxJ7gMtK9_M4sx6FU0AHsRnkH24vlAhv27ZpQz5JWJQVfzga9X7Q672UX9wOegnPSh8fVsHZXpOrOAvAocbr7nuFHzgPUBto30ovC6aFekdfXqYdQqQflKF7zJsH4JrqBE2tUqeqIY8FlOzHdAtdJWeoXYJu3I0fveBGa-tqr-AgjZcxpN7iVQXGENNMUp-Ksk8OvmqaWoZd4wtfCggq5T-1IBQNx8WPbNmgu4h5HUqMzAbHpaNx1MtEZ2eVSWh8JJwA05Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LGH6r2o8yXnM-nd7zd5SXugGkv6bvRG__nb7SS_NBmeScHKYAa98E-NytuLI2PvyaYTEDRCPE4lBeCPxJ7gMtK9_M4sx6FU0AHsRnkH24vlAhv27ZpQz5JWJQVfzga9X7Q672UX9wOegnPSh8fVsHZXpOrOAvAocbr7nuFHzgPUBto30ovC6aFekdfXqYdQqQflKF7zJsH4JrqBE2tUqeqIY8FlOzHdAtdJWeoXYJu3I0fveBGa-tqr-AgjZcxpN7iVQXGENNMUp-Ksk8OvmqaWoZd4wtfCggq5T-1IBQNx8WPbNmgu4h5HUqMzAbHpaNx1MtEZ2eVSWh8JJwA05Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcBoubT59W4uBnES7J-RK1i9KSztX4_mI2f5-gGIIzF0Gu7tu-IxnsJerZB7S-n4nZMOvri57jBqQp31YWOi8Weqf7Mevi9OgZNheVCJjg7uNH5vEAvOnCUfzGYmXId_iUy78BCzCUZFFqEvN01ehIFbWlTDQVt7tieTP26RsvN9-jNidtvHB_PDn6IESA7MhVL4XUtM31C68Qp0AW8FTOAfJUwFhmOejXSQTQ93SUgbFcssVNdIfPUW50lvTLwWAC5MT2Bwu4G4a7PhGPRKxr-qGnhOtGPumOKImbrtfY-yUyYbOtDhC8BDCrEjBa027hbjXmacfaUQNIJtfZ5UCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-GxOfm4N0qBRcFpO7UcdHmdc8pw1GryagDxc6tnQr0igSjqtM2rztvc4HVgMzyC9J8_oCydFAOis4DFQj9ChfcjU8-BUe9FuReLGh9wLZYkONz5QEmcCtkHJ3qAkxb2A8Nhxs9TYl5VoM9_ynuAaW4Wd_BqDAkZHC0dqjPcswCMlyEuUZ_STF2iu_Mb7FjwvzacoYsIy981y2_uLqpCXGaHvCozIPPvNF02KOOOUTwXG4WaCKlHL6cGoqbr9LO3pu4eqIdP3MUEJxfBML_EVlRasH0P_x_FwVIeeAtxOi6dmlZcpmSwCh-oE7xpJTXyi-QmuRVrcVrX6MibzKyqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoQWPNWKB0CzLcvBVQvBjI7vyKDdmVVTqESdTy1_46lh9-ZTTlyIvxdpxybV8FE-teovXdHkSqaTdeDXRlYiXNsS-JxL1KC6rjZ95nOltUV-rl5IujUSFyBBDqqQdADT9YAXMyhzL5opmdGcD8PbTAqRubkk5hcf__M2j4mNJ7zwgb6_RV8FAwB2YZwB95UXTbqsTEBMEsuS4QKsy48A1bMg2d-8YU7OYfO91UlRFz6y3BElkUceByc0rJCs5-iRojCLTwYkWcoElkXjE9WZlJ15KjfD4vElIFPpoqucex24tlbHmFq_eV1VvNjExHeAJJbj9DzxPqf2SICMtjJFJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEJnzsK6v76f9TdcreRPekptyYYXNsffPz7BMpBr8ZoEGzZmJJ7jUarEd4Vjn5U9b9InKZuso2tfOgD0OVQiYL25xy_mp8i9PdLmD7dZSrEK5eOrsk7kuQ4TP5jTLvriXXLXkgeq5qRp0vSuX9Uix-xcZKJcrTH4CurDwGuu51Pcxh_7RfBF_GnLgUT9-Z0xtlX4qRRzE2pvGQXHXxeIG85jcWE126UFWfD31gNR81O5-fquYYLYpQOC-vyXg6r574OzRHUXjuFf0UMYJkh2JKiT_fETvceVzh_fbwBwPUvU2AsmwAm1MQhUUxamXvs5uj8RevCGtJ61XcBUzMZgkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc-80Rsg99siRwmPJ7mjtTWBQg7d299KmqGk93Pwie3BmxlOAtM2mWpeBjo36EGbF--a62QFEkZmZjh9lfru86QMf2AW5G4QbexrOJVBvNFes7FEMwETGuhAsNgLPRu1eYyMBqiPGHzb8G605BOFZLuTwwE02cuRyA4tYZBdaBJj4r5kJ0axWVPLNSD8sgYc1oEHGxUgoVdIHBpg1YwniZ-1Zwo1sIUgnYypxzos2Jb6aTeQIj3u5PS4N3V3G7h0uJ7Fd5wmsdR48DAMbq683dhbyqYhyH6MR6fZYh2ZcZ-IoXVqpF1rEC9easMA5LYmFzz5NHxgm_BfjzljpRxauw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkMGTD15AmF1uayEcklj91TdNdoEnH5T5nMnVhwoI1tpiPF5Dx3yfcx7OdFF5FNxI2dF8QYQ_TlxBLkC9SJPTzqm-EYMkeUrYTJxv1TzfIr36o3agRGvlCB_ijeIATtDNio3wU7JzPGVNQKUi1fXi18tcCz2-yuSqDYYtm7l2cZkSkDS8apXb13u9BelzGOO8JcXQo19zwOAF2JwaQ-MjcMzgU5Ffm1mKVJkIk8eRkgz1vRktI024fV1D7enbfYHVD9bWrjwZK0u27-dnr4sHOa2q06t1fVI8fNh57JjTUnaMj2OKTTG1rAU6q-4PNK6a_trEq6VFPq_ZU9-HzQdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvfa9JL81WRDMu7r7b5_9AHIpw-SpsMapAAu2yjp-KgS5zdbLSankKMwRWZZQ1vfas_GEKob6WyTgwT84VrqyzapQtDWo6rFufad9mM4TEd0HE5ukJckzroeIvRtUaHy6wV3iXAF5psMGERqTg_r-2VPSLE8Gga9LCArQEeGuQscQoaMEkWbxPT6vR23Tvb6yZQLyjS67M36Hvz_3I_TZHawkCJhJoobjsZsQCR3SYJdSjr-oUuysjXTz2F6VggiN9BJDApjQHy3QUWOgafmokuG8BDK8vqUhToGfmtNKfk-MIQT8_pytfDp9kiAAEezAL7oPUnDRgyL8ytmmiZzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdSZAdW9hLUOIoEtf2hia9ncNGwSN1kUyWbnyZxF8y5vh4iOidUx4FITMIY5h3kVAJEugQTxVgUgpEzWKu1l7wYJjHCs4HPOwPjRxv1ChMbB9EM9BOpS4p_NHPurEXtPMcIk1h3u24qYXoWrawHneDRDtyfvbX7PxslnT9ezXi_GU_yqdJaQ_mc9vyqmFDWjU_yBCj86t_SfNxzwGFCp_pGrBVgCJ3wyNbd8jMRlc_TvL1XAwWJx6MRA0ffiaoGvaCSLQnRh6jftO-09si8l7RfDLpHXEnRJiNQm2_QKAf163rZoeOb3kIF8Zs9QA3bRkHDCkW54OLxV8VnpZ845Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVBGKzlbba6V42sj0Pps-eSWTDCru-_9kycKa4fF3jxXSW5aZHhRE3GsP0CdqXjsoGp69lOma_K5s3_-SCpZK4lyOHLMBWUytJk9XXpxruNl59RdV1bqv7hbKTlmml48vqnHAJp3xMlkxkL0_UvfLzfHYrkp6VNkGaYcYkxCF4H-ro3O-TXDuUu0OPc_PPrPhCYto0bI02f-wXNMc2wWVe8x62PKCK0MlBmg5FzsYhCNNsN_evMwH87L0ehfqYBgOxz9iw79qIPeLQvYC7BU5yFvrmnEn1f1XYcqAOwy3-yHjMgNXrjaFhmw-hGLN9AwpeFf25qTWeEnNXWX1jOB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFSl4XJNGNkFiH7nD7W8UYSD7H1riP4TMe3O1i1cMslQ_CxBGvU-_FwYYsWHFlrfpsOGO-Axh2nI9LcGBQ9h_FP9ZB2BYmGrim-_WqqoKU_ivpn9pO42VA_0khfEfrI9t83gGlVjG-1HD1qC2TYBhfEwpISoIXiGWy53iHiImjh6fJSguKS4xyXA6-g09RfbhhxthK6GjgiWqBFsFn-R_CtIkH-9IwvrWsvXkaYlGwWB7fICTJIv2URlMDccDtlg_x7R3Bp3MKKmFa57VShkvrqLK2TagF7EAmIqQWUwbCMw5G4QPrMK2NH55bEHOvahempxIfINsxJinY-q2w-k-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dUGsacy-K4A4lk1KkUkYj9WzSQO0gQq_Pl4gIFn_CeIM-bHhBIARt-aSSCmzIz_fOTrCGmE-AZPhfKZ0UjNIxOT2HEI5p0QPCuxHokkLE__87doEyRNEbllHodk16VLcz4Go9hYgZXK2ep0RRipHlI_haCzK4jAVyNYQcOfcj5rRVuA_dF0ValMCbEWzBaCDaMI2YAe71vo1bY9Op2NT1vpkjJjbvR9j8LS9ickoNPOf0sm3hdks2q1QlCe68R4Xg7AaAfJkjouAA1wrvyJxQ5ylJ79giWyNBdu1JNeATkwlyxlkIHAdmVqfwFgLrlvqSIawlvZBRPfzchsAh9UQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dUGsacy-K4A4lk1KkUkYj9WzSQO0gQq_Pl4gIFn_CeIM-bHhBIARt-aSSCmzIz_fOTrCGmE-AZPhfKZ0UjNIxOT2HEI5p0QPCuxHokkLE__87doEyRNEbllHodk16VLcz4Go9hYgZXK2ep0RRipHlI_haCzK4jAVyNYQcOfcj5rRVuA_dF0ValMCbEWzBaCDaMI2YAe71vo1bY9Op2NT1vpkjJjbvR9j8LS9ickoNPOf0sm3hdks2q1QlCe68R4Xg7AaAfJkjouAA1wrvyJxQ5ylJ79giWyNBdu1JNeATkwlyxlkIHAdmVqfwFgLrlvqSIawlvZBRPfzchsAh9UQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_t2nuS6e8KC3rh1vwieNTKEY8ND_vSDH7TTReLYCkfUxrWU5Ut1rzsBJ4oZ6DACR71ytOv7610JB6v0LLN2EQ24g9mj4wtT2wttMvFftY2ITfRQDTQMBA5dYe-bLfgWKdR3OekTihVHCe6tCLO2HHJ3NzQEGniL-zoaHDk9f0O1x-WFDCfnmuRJh_IzSL-eDmUb2sjx-YEKI7j_RCpPQ_xsjIZGWbZJjizJwut4mpaOR7BmQogeDvgEQQtgl0HlcGLIlBsTuWDXF0ghcbam_lDBWFGwLjPRYrAeqYg4yBq2HChKnDMG2fVTvH0zKJuEd9DMRLmFG2C-mLnqqO6zeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B265Ss30sD6IS3LA5hPZyTduprxLLGi1aAfOdzNY0rhMi-D5ZEcEq5E92PLRXqD7wViUOStHlMbwH7SHLSJuFtt3_HBvwsXhKLE0KFVn2zMdPWCZSxwofyr_EPMIw0C4otl8FD8A09a0pr5R7ge9U6gsEIPx4bRVp6hqRJeLjDulcNN4TwW1S1pf_5o1bmIqIJnzy5svMOhHAJsFC4o8sbYARftGbUU6wAx-jYsT60K4kSlT5Je2VGj1SlVgRX_Ct2AndeMZYubvhRYiEReB1XJYZvx7lD80qFODtp7nT3nd80HfNgzboqEZCyxSJ-6goNyhRTUXm1m95aNuiEB-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
