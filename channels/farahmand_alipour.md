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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
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
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0xQQ5psxeqFvTMrgyDmkVDUMBJxMNocfGomcmspTEPbhQQlAIyFQMipvBrToVYlnXLfBVI-PNOxMvj_G1Jm4h7QRoJRsyWTN_7sNmE1o0HiMKXZ3bBAmqQz5OXwfPi0CArOF466Qa61x-E_58YtXuupK3IEE-iS6Jvzzxqh041oIq-Hyq-QInk7_uHkFWiGR9UULYYWyOaOm2-yXlb6sBxI-LmUOB-1ajxvk_tUlu1LXL3MpSCb2xhdPwwAz1uJ35v2EKuOL8Xulv4gi69q9ISZeLJdSrgBvFdEb-Rrlw9as65y8peAaIUWeoWCbHgF2jfxWeO71sLg0uNyPY231Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW6ht1rM0z0qXldFm0P5j7hIP8Z0cHh1z3HpkOu-ZFLqPzs1TextuNY4bqgYyszVwc3cG8nv6GGXRQlnmowvJha5F3mF_ifvs5oEQxvunkiPAMjdKhFijzcYOmXPI4e9s7yYPGEyw6lJHP1WuRm-ADyOdXSy8AqtfsIyiVSyILncGJb_bavSPjBq0d43WQjQaQSrAPCKOt94nmJuiTvmnR8xfRxiKh0JrM4hdGVhQes-yW23RuMn6bDc1rMoTotvmQMnNZg4OkLO2TY8ssgfhDWrjEa64njfABOoO1FUGBeKSTAnT3p_2xdjQH2GGp6vB5iSiVgdLD-fEE0JW4ntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAP2_SuzT4o8HAjzuGT6aEAmtk1kifKUrGw4E5Rlb5gle6YAcvxoGOhRwYyM21PS5Y3P8eM_TKmZ1P0jeV4tisVvGxspPn9MiRWTB0DhY7sYw6Top_6WKFu9opVPpxRXcNflmF6-8EfhqJHXVJN8BJk8WqQ825J0ZcCzB5yuq_O6eq9iuXx_yc4wvISCFqQ_NnKP9JkjV-rHP7nmsm05_4thJdow8pMBjPC3zQmjJmkdQ0S0Cxkw9qS_nOC_eUs0PqQthzfDlon7iOnn3EySDnPZ0ydbtb1Qs1k5ayN120wL5lysQVIf7k0X4IYY_CSKh1kKLTPNxHjTu-J9T7ChhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnAhhrWX8t3FMbU_GfrXbxWhLylYb6yN7jmOLPbLk73_pn6MVBNi3FhhWYUhBO3Vrlf46VNBruH0Mf-S65Hi-SqbJX-aJ6vXK4fDcegyAd12RQjN3jV21XkRPpbP_oFGv0yGPDu3teQuEld4yeZZpv0Vtn4d2nhVVtZXfnQKK6W4AlTtOAyodgxnt9jQTB2u3YvUiNYfX1soCh2A11EI0SV4EiHFX7X49Lr3daPW5ejS5UIStUqiqRG77zas1I7WZF25iaZtJEY-Qpc8z5TaIKP41u2NeEHeNbhpZ6VG73eVuC5jKkDXQOomXlRFYQh5AF2huiA533WY0JQr7NV5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av-evXXpTzoGtnm26vJgdujpiQ7boD82rJ78OoRrxjATLKzNU515ylj0CDyJsyFQsAaN2ShMXHNUojIESXB37q4AErKFgRA_jtu7-udzRfhc2K0wpfJNb5qCwQd7YoFc4CsflFA0451GWDdr9ehfoD7uxCy-fjxjIoFwvYVJFxghPFI2gIEWIiBKst-qJHYeacP1hTIieIeVJV7XZonSCyKkiltYT41d89CYI3epiTNHfdcT1NLTncvQ_Xn9_odu_BrEqhOzKLp--Cza7yDJyJhUG1NDfnHzsC9bug1jO8X91j4McKphnDjav17vls7DXUYNgBKYuHOY1t0yldl2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC3_JxbXGqKTUz_-sOOIdPEcLtDdhvWYQydlhVg_6fTVf9gCqItna8H1L7uuRasH5zQFIXnyISzT1j8PuSCzYIvJqKTFcvmnwWS-9HnOTOJhopay2UhEQO_zwvda2SftcV2jSr0NHFEtokQOfIwwnPaQjOIh4KVWjJG-0qrfr8bqvJOUtl1vauK7DC1tqJnQ6FXoIGus4L7Co2SnT-zgs7TrijI3_TlXCtBGc5tNbROU0qoFu2L6dxZgVehSNyTgHP-Qwiy6i5m7U0uDehJqirThCDeqM4B_va4QG7_lxMGfurzo1g_QLfgXDb9vj5Jq7hnPhihMYLRjb5MJ2QQsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=aduM2YFOT4jjA784u1nkoSAaxAhGuQzEInzCsjCsL3ZxMC6w8A6ptTmj1KmybMMkp_YGMFgGhFX1y9xo0BxNpgfb0sjmKPrTEe1kDk28Aj7lzLmm3bZ8eoCjx9r5roYkPw7UhYnEpqjBlZGXdqFpjxHBeax7UJjPiCOL8d8wd9cmpJlGm7T5HfUX-HUwm-5ik6cmOC74Gfuw8yzCpjmADakosOtfxYeEnguyYzK9KJczZMl2LKaXglqEHtD_2JHZKEDAj04U3RJjes9SuCBbceQmItV-9nfl3NBKS1QMQ7hauelIGAjbsWy6PXslExQ0ZKQotPiHLWSaGAnBX6lcfWWg8LCQn5B2kBW2Mj-cDdfq8Sm8tfurQUBOBuZJ-oFRcWdRWScciLXIWeUU9KMCDrj98s6vr1h5MMGu1advdRX3mUQ6BG-AKfniKx_bpDfLXempjTWOzWPSGww1daIlfIbBCsY2JCs5hIfqwS6aBJ6qjml1NARCQ9_ZR5mV84NO1unTQjSKW3iBMo9KdCfGbKiFEfS-20K0lxq2_WRV9ADWnZPGhuzGmp0AOjJ44QjgiuqIBxmRzJAveZ6fh-9j8gWi-kZivYkxhIIW_3UwvhwLz_FJ8W8iOaYzfO8NnVyAowSKJF1vS8ktnbcC6h5WuNrLuIgp1dvhkOwf8m7QAmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=aduM2YFOT4jjA784u1nkoSAaxAhGuQzEInzCsjCsL3ZxMC6w8A6ptTmj1KmybMMkp_YGMFgGhFX1y9xo0BxNpgfb0sjmKPrTEe1kDk28Aj7lzLmm3bZ8eoCjx9r5roYkPw7UhYnEpqjBlZGXdqFpjxHBeax7UJjPiCOL8d8wd9cmpJlGm7T5HfUX-HUwm-5ik6cmOC74Gfuw8yzCpjmADakosOtfxYeEnguyYzK9KJczZMl2LKaXglqEHtD_2JHZKEDAj04U3RJjes9SuCBbceQmItV-9nfl3NBKS1QMQ7hauelIGAjbsWy6PXslExQ0ZKQotPiHLWSaGAnBX6lcfWWg8LCQn5B2kBW2Mj-cDdfq8Sm8tfurQUBOBuZJ-oFRcWdRWScciLXIWeUU9KMCDrj98s6vr1h5MMGu1advdRX3mUQ6BG-AKfniKx_bpDfLXempjTWOzWPSGww1daIlfIbBCsY2JCs5hIfqwS6aBJ6qjml1NARCQ9_ZR5mV84NO1unTQjSKW3iBMo9KdCfGbKiFEfS-20K0lxq2_WRV9ADWnZPGhuzGmp0AOjJ44QjgiuqIBxmRzJAveZ6fh-9j8gWi-kZivYkxhIIW_3UwvhwLz_FJ8W8iOaYzfO8NnVyAowSKJF1vS8ktnbcC6h5WuNrLuIgp1dvhkOwf8m7QAmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVaVpGZufiRbbikkPWbuJNSigVIW0IyN6Ga4cICjEYFi3HHMuKFCeRhly-LvOYXwINyAA6GUG144BMGnivTZFhMAED52NbwzB8DXTVpe0HEh4yuNQMivR0JgRzZKH-mOXUebEiZd_yDdxgAJHuqHkDstaCpUwqN3geeccg1aB-zyqxVvyRUT2DlmkULfalVWk0N8ayTbxRLVRJ3JF3T9YBuITns7PkzxaSt9Hg39mRRQUxBw4BnshQaTqGuSh8AVXhN3GsDRkDn5tM_8hUnIiVZ5JGfTKHiKDP3DN_W5xD7BcgsxontPUblvV8WMEznIlFGczRN0IPtwXe1MXwZglg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ZhkJIO9RnMJCRgXw-0DDw23aYHIrk3sS0ygH0_iwKa1G5J5Ih0ba-cqUFJGEmD5ramBgQkv6M7-F4wByLKVPrMzKeg5McRjbhmDJxiFkmU5m5P-UVIH5xswp-NWTc55M_TOIN-OZF-5siKkOpNCAD9hspsUs6agqC4fElj6FNIZU2XNJ9uFwdZbVR-e7AjRuMH82CDuxKr3PMgitLZllrpw5cUkbPhspFrS6U8lXDgppwY1nA5r91_a0IKGnxYJZm0b5OuNrq2eiKsUTPyjBBXd37b98nHCXMrUR0AZu2WgFiDdIqlnH6zhEiTimSBarfQFmiTp93KTVuGmlNg-tdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ZhkJIO9RnMJCRgXw-0DDw23aYHIrk3sS0ygH0_iwKa1G5J5Ih0ba-cqUFJGEmD5ramBgQkv6M7-F4wByLKVPrMzKeg5McRjbhmDJxiFkmU5m5P-UVIH5xswp-NWTc55M_TOIN-OZF-5siKkOpNCAD9hspsUs6agqC4fElj6FNIZU2XNJ9uFwdZbVR-e7AjRuMH82CDuxKr3PMgitLZllrpw5cUkbPhspFrS6U8lXDgppwY1nA5r91_a0IKGnxYJZm0b5OuNrq2eiKsUTPyjBBXd37b98nHCXMrUR0AZu2WgFiDdIqlnH6zhEiTimSBarfQFmiTp93KTVuGmlNg-tdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO8rEQnn1s2IEJr8eIWqkM9CfxSngqZlTvKF2_43SgxezbyM2VpN9eowErFcWF1jES9X_CL5wBy1-tqx8rCil_FSIMbmxU2K2ZBqJBGpcUgKTb90HMMIlnWRTacVoPpY9-0xts4zdH7InDN2ryt5TsS0vZdluafAxxVrFMZK-J3qP6ec_1-9O6xqzA9P6Tsu4aTZo8-q4oUwJy1OeHlLn54uJIXBKhLnqTLcB7g50gEnDWQadBtSwzIMWS5z3TnRAV3-IJgh9La5EzyXZ7yFn7xRKvw5SqV-WuxC7IVNbn7wEoFSx97uApHyd83178aT_hHnUxaXjKi659nCBd5Kiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APWimCRNJrsTQHlAlfwJ0KUyVlQgmx0_Zrio9VtAAYlSq-uVhjjYL2pFb_jIDt7F3-cIB2SmvIf05HeZkTSGCByHJWzDyc7Ax1pV8na69sMFJ9IPHpewW1OuO0B53Ld8v7E4CFCcH8CGM7fcN-uh2Rze0mg2HCtLzAPtXtRnMOoTk3OprSUGz8ZPq7hcoIvnvPzDvs8NNwFhoLfI-FPQAIpWNfx0TipSO20cvrqRZqlNjBRIenwAWXfkvB_WHrJo9IThZx_MKzZzP3rLiOrAEcCxX7yUJjjw6ytrFscWKs6h6VAAUL9qp0i5oTch28UeuJnYT1NdpqITKfLGteSjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzuTBNzsZCIbWGa5eL_9PUjF7UjiIV28MJDN-GmFQHs6LW1kvwAjhaKeRKPj9JmC68oJrDPS88-sp95HUczqh_pVlf4asYXk4UsAOC0gV1hfPCSh7_jnS01X-rNcH-Ld-s3Idc5N1r8imF4R1K94U2mLAJ-H0fRuikV5NMQiqH2gqf9hXmOdaHbFJDmocFhXMbX-aO1ekVCqbmnZ_SZLkllmmmIO1ujRWLQ5S-4QTRw3cRC-Y-twpu0Ma7OJkMAo3NYltZ5-QWUKdNNb3xnw5eEGqUWbOHBkJsEeWBtpc0-zdoS7hiij_32luPbjC21FPaf58Q0dsK7xPQ0ggF13lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ewsRRS9t2ONfW9bqvsbmBlr7M27usp-604XpLGhSI8KYaUArQUNulSPfMsqzNnnVgieAAFKOqCoiYxZHModaRt4yYj7mFpjXoz4hRegji_GtnTH519BbLXi2se1RclAKjhzt0l-2GnVx6QLQeafjTFUkMKpjLskD28sLPmn4ohJ4Cxc4bLkbmPMkK50e-EQ7LlKVgx37bzG7hpfKYPR75vOHnvaC00pvxl1HgHt5v179Rk7lNw1RT-1TjiVxIuZCvMi2bltAOrtnlfXvwLSWQ0fg8mBGWqwEGYIBSxlw_dZiorE9HnzNN4DPRAeZE37TFhNGlFF7Nq6Ojjut6A9YEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ewsRRS9t2ONfW9bqvsbmBlr7M27usp-604XpLGhSI8KYaUArQUNulSPfMsqzNnnVgieAAFKOqCoiYxZHModaRt4yYj7mFpjXoz4hRegji_GtnTH519BbLXi2se1RclAKjhzt0l-2GnVx6QLQeafjTFUkMKpjLskD28sLPmn4ohJ4Cxc4bLkbmPMkK50e-EQ7LlKVgx37bzG7hpfKYPR75vOHnvaC00pvxl1HgHt5v179Rk7lNw1RT-1TjiVxIuZCvMi2bltAOrtnlfXvwLSWQ0fg8mBGWqwEGYIBSxlw_dZiorE9HnzNN4DPRAeZE37TFhNGlFF7Nq6Ojjut6A9YEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9OP890YSWRhnFEkwiEbiEhu3f4BXwVqIKTMv2wnJwNZUF9jkrBLBKdCsegSExSDxq5lgYm_SxPkR9dXGa05g2WEgVRP2hzXp18aWwOjEt5z6i2bLKSfF2dXTqsNPRSgoEZcraJCaiOlJ6voAtEATxSNGm67t57um3kt0vH3ra0OvjTFEwPyqD8jcfYhK9IU6AgK7snp6vGwuQMbhATiqssXB77pwqyNuNkD7hrRSeKyZ0J1ul2eah1lFBS08aUBV7XWlsLXX-lEIPNl2fjia7xe_0JLcE1_PingnxgJHbHWRzEwj8XUEMc2SHMUk9vaNOxwdhMvC-EyvHpke45YVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0mKQD7s8vBpwfFtG6yJuOzd30JpN6yTGMVTmC2xVo7NGM80MQIDvjnuXx3wtWTPQoZkFyiT2LulaBYaf_EXBZ0RH3hXqyElhNp4ysO8ACVOVT_lu3VM5yKmZH-MSLRVHR9UXdHUhOliCPMomnqTKEiyXIHHPskz3t8KyVWXO2M8hIqPw_4Y5HrooXwMzeS6zz_Fz-xiSpa2dQ8G4p73xemSza9sHJh4gKtroZxCoU3TyZFteWUPrA8bc2OnuvFZC6VvlElK7GDTQp_KEvVQakKiLapA04sKpNdWHky_8ttFskgkRh_lWhVzlPCgK6shanW6yxME3uV-fndL_PVLYvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0mKQD7s8vBpwfFtG6yJuOzd30JpN6yTGMVTmC2xVo7NGM80MQIDvjnuXx3wtWTPQoZkFyiT2LulaBYaf_EXBZ0RH3hXqyElhNp4ysO8ACVOVT_lu3VM5yKmZH-MSLRVHR9UXdHUhOliCPMomnqTKEiyXIHHPskz3t8KyVWXO2M8hIqPw_4Y5HrooXwMzeS6zz_Fz-xiSpa2dQ8G4p73xemSza9sHJh4gKtroZxCoU3TyZFteWUPrA8bc2OnuvFZC6VvlElK7GDTQp_KEvVQakKiLapA04sKpNdWHky_8ttFskgkRh_lWhVzlPCgK6shanW6yxME3uV-fndL_PVLYvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Q3BgNTVzViqUgd-z342Tms1dyUwNyCyjssIfHWpVXr4bofVVWgERyaqHwi85h3yuec3aHYpWLded71Ii1-4hTnUNVIikSua8Byu4nTvgGLtMKwLBVe3HATuGI6bnb435l6HRYAWYZG0YZ5Z8u0jsm_mYxas2LafgPnoHdVrsskBy_1f_ks23rosFRD6urrw2-5wqu5s5q3dn4JXT2oegAen3m7WVzbF9xo6fe5aKv-sQViOgIcwVj0AooiZYhI0RAY48Uc5EJ9ltjGzAwl2IXyfhikLmVuMs6m-tEF6qSl6nHaQUTqVouDnc-9EQ15S1e53ps6gowwTqdKaNAGCDkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Q3BgNTVzViqUgd-z342Tms1dyUwNyCyjssIfHWpVXr4bofVVWgERyaqHwi85h3yuec3aHYpWLded71Ii1-4hTnUNVIikSua8Byu4nTvgGLtMKwLBVe3HATuGI6bnb435l6HRYAWYZG0YZ5Z8u0jsm_mYxas2LafgPnoHdVrsskBy_1f_ks23rosFRD6urrw2-5wqu5s5q3dn4JXT2oegAen3m7WVzbF9xo6fe5aKv-sQViOgIcwVj0AooiZYhI0RAY48Uc5EJ9ltjGzAwl2IXyfhikLmVuMs6m-tEF6qSl6nHaQUTqVouDnc-9EQ15S1e53ps6gowwTqdKaNAGCDkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HQcO2zhLYV7ZGMRGTZvEPvY2aek2Ntt7JEGMyVV0k70LxvMJYg20mxQ5uiEJQzx5SlL2XWF8gv0W41f9-rQQA6Z31UK0MRHX3qHFAppq8u-XsoKg7ry_XvZ34h7PXbXyGdBbIh1HrqaCS0uKHQpRBYhopekWSXnEbId7wSI31pCv_hknq14PYPb99XZ08qb-kek9oB_t2m5mAbgdCCA3sdZJj_bsDBoaWyn_Xt07d9cCITBmEEXh-DA-s9uUF21-yPFanmC9KkBxM_ZbHyv-oLFZRt2P2a4Ml1lEFT6anKMKqHPyY7KSrwv0A8YuzNhp65mE4zByUehRfGkiHvQSNIrz6mbnQGl87pupVHXDcgD3UvXzHAmw_dcHl8-GJXcDXt_vtvMvlNLeAJN1B6pIaoCwFao5PMOJ8n2bB36-6X5VHmYZyfKxj2_mRlLWoH7oi3JS7t01fJI2ZOoPVBsJVikkm9zIXKCiQFNNzA-PcQpchgp4sTXtG6Z_mC2hV3eZCRSeOkt6VetYlAEEwNzXxOe__0S-nYeAuDUeWy_CYAQcZiqstySp3d86Ts5AHT77Aek5txpcQFnIr5cCRtx-YNyEJSc92RKq0eAxNFQ1Az1pBZXBCfQGo0ug0KvAgAz7uyzxMQbh7M5qLD7ru5myOxTeyyHfP4zfYt-3ooHj5Is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HQcO2zhLYV7ZGMRGTZvEPvY2aek2Ntt7JEGMyVV0k70LxvMJYg20mxQ5uiEJQzx5SlL2XWF8gv0W41f9-rQQA6Z31UK0MRHX3qHFAppq8u-XsoKg7ry_XvZ34h7PXbXyGdBbIh1HrqaCS0uKHQpRBYhopekWSXnEbId7wSI31pCv_hknq14PYPb99XZ08qb-kek9oB_t2m5mAbgdCCA3sdZJj_bsDBoaWyn_Xt07d9cCITBmEEXh-DA-s9uUF21-yPFanmC9KkBxM_ZbHyv-oLFZRt2P2a4Ml1lEFT6anKMKqHPyY7KSrwv0A8YuzNhp65mE4zByUehRfGkiHvQSNIrz6mbnQGl87pupVHXDcgD3UvXzHAmw_dcHl8-GJXcDXt_vtvMvlNLeAJN1B6pIaoCwFao5PMOJ8n2bB36-6X5VHmYZyfKxj2_mRlLWoH7oi3JS7t01fJI2ZOoPVBsJVikkm9zIXKCiQFNNzA-PcQpchgp4sTXtG6Z_mC2hV3eZCRSeOkt6VetYlAEEwNzXxOe__0S-nYeAuDUeWy_CYAQcZiqstySp3d86Ts5AHT77Aek5txpcQFnIr5cCRtx-YNyEJSc92RKq0eAxNFQ1Az1pBZXBCfQGo0ug0KvAgAz7uyzxMQbh7M5qLD7ru5myOxTeyyHfP4zfYt-3ooHj5Is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=I9uoKWf_PewGi2sQ9PsLdTGpVD9A-g9oocVWEh8HD4867M4I-RJtczZn1GTYj9RZaAf9uOc-fzeTB-tk0U6Elho4cmvjpODYw8wxbcY08fKKApsYV0YhlQLjKZ-dRWH1T3D1AQdQVtgsu5WrFnArWJKc93a222EYmG2cPg_wCzDxsxB96gIswkO5auYQHFFFZvKPjVceANBsMEthWrVI_ZvVHCm1AicoD3E2opX2x4orSyxMnvYVIpjorSPobYWse3jbhpu-btuQfzimpBGfpjh07Z_B7yvDwtGh4OXgIhaZy5JOaaMlnXN7AfKL2Hn3YqV88QNnZfuVINAw1ybn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=I9uoKWf_PewGi2sQ9PsLdTGpVD9A-g9oocVWEh8HD4867M4I-RJtczZn1GTYj9RZaAf9uOc-fzeTB-tk0U6Elho4cmvjpODYw8wxbcY08fKKApsYV0YhlQLjKZ-dRWH1T3D1AQdQVtgsu5WrFnArWJKc93a222EYmG2cPg_wCzDxsxB96gIswkO5auYQHFFFZvKPjVceANBsMEthWrVI_ZvVHCm1AicoD3E2opX2x4orSyxMnvYVIpjorSPobYWse3jbhpu-btuQfzimpBGfpjh07Z_B7yvDwtGh4OXgIhaZy5JOaaMlnXN7AfKL2Hn3YqV88QNnZfuVINAw1ybn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg3W-iyLWqkvD24P8BY2f41FFcW06xovgiHI5pfOrxsAIxGebc8zlfGEKOgkYEhen5qddQV1Ip91MuU1_XyT6ZxMAKmmLCA80sB9HOcsqiAdq_YNbyziFglqYwN_TiJrJZHhfmhu1_O0s28C-GDyqRu9RAvdQBRk8JVyOfE_tLrLG259Rs77n7TRrlPumOLXpA1M6d4vhqucVLMk3rD1wFSz2WWXoI5AXpqzS2ejXvWc8MuQgDRLrISzj68xhCPMen0vcH39lekiatzPW2OfQokgSJ3aN4OCibej9okKAY9p7TjTkJNjWKuEYrTsP2h-gkXyS_lihpGlBUf2eJIQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=nD0nptcSgeMm65P0fFOnGey0LuwzlO-71dScBCneWrR7BVhSTM3uyEdhaLgI0kp5BId2-Z9ktvbiP2GWV0OHN8Ej-BRHxlxuJ_El2QYPzJqnlPubiSAc7Sbr-RZGlfCD_JY6xnIiRmHt5Lpe8tMLcJ-wmPJKAELA1M1un-UAiezUKSjcuWajaInFz-VzCPZFZOO8sSlwZA-mna62ZFSAXmbHRGgchpsQI_fpKEkw40xLqbIMNJyHpCMq6vSjsqZVewHKWTgGUKfhHVfUf5i7rw2ejyaqKfkhNyrXdX5DW-nzs2fvyJ3NakStliBye-uPjIT9GXsyzhIM4imysJTueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=nD0nptcSgeMm65P0fFOnGey0LuwzlO-71dScBCneWrR7BVhSTM3uyEdhaLgI0kp5BId2-Z9ktvbiP2GWV0OHN8Ej-BRHxlxuJ_El2QYPzJqnlPubiSAc7Sbr-RZGlfCD_JY6xnIiRmHt5Lpe8tMLcJ-wmPJKAELA1M1un-UAiezUKSjcuWajaInFz-VzCPZFZOO8sSlwZA-mna62ZFSAXmbHRGgchpsQI_fpKEkw40xLqbIMNJyHpCMq6vSjsqZVewHKWTgGUKfhHVfUf5i7rw2ejyaqKfkhNyrXdX5DW-nzs2fvyJ3NakStliBye-uPjIT9GXsyzhIM4imysJTueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=OMu5tjMjTD_F2SQM4eqlHsnytF2v8C-QqjiWKKJeQfCsRRJhsI__wSW5znuEO0vCdDFTK797v30EL4_uy7_30x5P09wG2wEFFIDF_AF5zQGpcW10tNuZN2QCz5OqNw_usr8xBIhQW3LMLd4Vdnh4fiSCDn2XgFoV-0yjDgFZnv0LcwEJ-yMSt_czTXbEOwigE5f9Dckcg1H5mNY670EgKq4aueAAqwkawejpRaekduF-bzFqhNM2QH5zmtvfiGKg9GMD0ZlclTRifEQOW5wSIJZNm4UYyclhACkZDrxUmpSC47HY7tiH--ofvnn1gn2UGMPfJnUMdvFoqZQnQcmW8oJwacCXTOLYWPkSd7CaPlQay2zkPCTjW3zp7BnuMWlQRL5wexVEQmQOd082l285hgZRZ1K9JJu--YAOQqgnegVParXyVQgnmvNcj6faBe6XBuooJ6GR0fa_xreEpoovDK_A3iXalNcxubRyBSr95kojwCiHZbs5ksuZp5Okmn1CzTF1E6Vrkol-UFSPmB6ELL001kbOB8W1gHHq2l-5hr9USKiwibAnhb4d28Bh-d6jazSUKAsmIY_BiTM6ug_GBVcsHan8elgP3NwZWSDvwfZScfRa06SkMzMBEs9iQYXZWJh-xoSROVzlr9NwL6Ddfmxf1HVy5dUhdeJRmdKPuKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=OMu5tjMjTD_F2SQM4eqlHsnytF2v8C-QqjiWKKJeQfCsRRJhsI__wSW5znuEO0vCdDFTK797v30EL4_uy7_30x5P09wG2wEFFIDF_AF5zQGpcW10tNuZN2QCz5OqNw_usr8xBIhQW3LMLd4Vdnh4fiSCDn2XgFoV-0yjDgFZnv0LcwEJ-yMSt_czTXbEOwigE5f9Dckcg1H5mNY670EgKq4aueAAqwkawejpRaekduF-bzFqhNM2QH5zmtvfiGKg9GMD0ZlclTRifEQOW5wSIJZNm4UYyclhACkZDrxUmpSC47HY7tiH--ofvnn1gn2UGMPfJnUMdvFoqZQnQcmW8oJwacCXTOLYWPkSd7CaPlQay2zkPCTjW3zp7BnuMWlQRL5wexVEQmQOd082l285hgZRZ1K9JJu--YAOQqgnegVParXyVQgnmvNcj6faBe6XBuooJ6GR0fa_xreEpoovDK_A3iXalNcxubRyBSr95kojwCiHZbs5ksuZp5Okmn1CzTF1E6Vrkol-UFSPmB6ELL001kbOB8W1gHHq2l-5hr9USKiwibAnhb4d28Bh-d6jazSUKAsmIY_BiTM6ug_GBVcsHan8elgP3NwZWSDvwfZScfRa06SkMzMBEs9iQYXZWJh-xoSROVzlr9NwL6Ddfmxf1HVy5dUhdeJRmdKPuKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqaSeGwyAA2V6_gGRxnNS7cwTXPxVCyP_AHMacjAj1l51FZFXKeVLlQ20VhPbQTs-jT-p273ni43xJvsChKG1yhqCsQEnZoerRAJobmdUapsw2xvxGJfIvlHtu5w8LnSCi6pTW8jh5r93fsufWee8q6oOuyj0SUNR1SnKTNuy1rp8OS0XCUHqm_RCXcA8IG5LkXzLRgiahrtRfdXVmvb7yDhTmeKB5uhCHQULkIOhxpjDRHm5n1JW8H8f7BLbeR8JKfiAZe1yGDda9hM9W_9LkuPjEG6CI_GH6VzcfNMZrU-5TPqHoH0lDOdo-9so34YV6rEq7wEwIwMrEfGTQzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Fg4cH23FgWQePsXlwUQIiJev-_Th2nQSTJr9jaSZXDNyqiHzlxtD0FERTF4skcDag6Xl5rmbTvC1me14d_GXjQBIkb0UWwbvBKOBqAUQJ5DZYUm4iwiAtx-VLxQlD7Tm9g5IYkayr0-qBoG_KlsjRD0x_9JvT6Uvx3pzzMAxrh_3MbR6uOaD0E5pbJfj1KMTVDskWks_FBDQ_kB43W9zSpR7jzZfcSa1xcEEYvd5KAzMCRj60TCHBOnUnJ8N6qQWon3qOjt8HViWynV6WOIxlwVofAKSYKlP7a78I8a6TZZIT1iRTa0qiemHXo4zZ8wg0WfCcZ8QlT_TVo1QJGTb87bX9DyGkVcGyQg7T4oLV7Fm1sVxl8Joiw3FOJWymgqiGGf4R-bGCoiXVDYaZ7BjVPoqe4aovFSh4jpleuLYxfpeNWjBWir_75MH473VVHEgIHYvYQQupQo3d7Fz85WxPNSZwpImg4Yt1P0O_V3B9JM2yZ6gaX4Gr1Y-Ts-q1lB0hKshfEoDqdOdesa072bJosgMpwXylgkUuu5TzS0npKPU5avghksjmMkEu-Lact65r5M8cC69Vlxj5otG5MKWlGWkqS_sy6f2GU9y9L7aDX4jPYTuACEMiiyOLLh7YLUKR4bTNvB4aggRuyIDtdV4WrQvKxG-hpKeUGxGRYK9dXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Fg4cH23FgWQePsXlwUQIiJev-_Th2nQSTJr9jaSZXDNyqiHzlxtD0FERTF4skcDag6Xl5rmbTvC1me14d_GXjQBIkb0UWwbvBKOBqAUQJ5DZYUm4iwiAtx-VLxQlD7Tm9g5IYkayr0-qBoG_KlsjRD0x_9JvT6Uvx3pzzMAxrh_3MbR6uOaD0E5pbJfj1KMTVDskWks_FBDQ_kB43W9zSpR7jzZfcSa1xcEEYvd5KAzMCRj60TCHBOnUnJ8N6qQWon3qOjt8HViWynV6WOIxlwVofAKSYKlP7a78I8a6TZZIT1iRTa0qiemHXo4zZ8wg0WfCcZ8QlT_TVo1QJGTb87bX9DyGkVcGyQg7T4oLV7Fm1sVxl8Joiw3FOJWymgqiGGf4R-bGCoiXVDYaZ7BjVPoqe4aovFSh4jpleuLYxfpeNWjBWir_75MH473VVHEgIHYvYQQupQo3d7Fz85WxPNSZwpImg4Yt1P0O_V3B9JM2yZ6gaX4Gr1Y-Ts-q1lB0hKshfEoDqdOdesa072bJosgMpwXylgkUuu5TzS0npKPU5avghksjmMkEu-Lact65r5M8cC69Vlxj5otG5MKWlGWkqS_sy6f2GU9y9L7aDX4jPYTuACEMiiyOLLh7YLUKR4bTNvB4aggRuyIDtdV4WrQvKxG-hpKeUGxGRYK9dXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=R232RCcr4qJ62FZXvdv5ElO8qPCfHWeGSfW4Ay7zbj4E_UjldHMmKCZZ7MteMQn8KYSkkPWxN_1vwUnMRPObo5Npyijmpm6mdkjYo9SSGqIT992IcZx0E4H1nsZGOKMV4DuTmSNHD_Sn6Up_ZvK4sgilqPVKe45wiifQo0k3S6cfQfaLpdjCZioSivFWSZR3Izg3WxYMFBfLqSL5UjGIhal6ZXTL3KXHZAeafEJggg-LG0TpPZ7p4YF_ZXY60rQyrCDIGGYNyCfAayezOuzbBOo-OwSnr1pcO5KiCAhR7J1ewmIqca70B8QPCP_u-wi6iUs9NwD1dMhcam4JlD8rpXojOgSjNFvvlPUnjATQ16U2u9HzvjZcMCg_egK0dZm8ah6ZZBC55d4Olj9J54UjLqTW1F54mpQt8snxJ_WWBubC_MTg-8BOjpAjS1-I26XOPMCaMMFVu7aZi6ukbd4ffM4pxmgrLwZghPOZw0uIQ3udtbmEp_wdDe96n1gjLFWCNw4Gqj_jO0vMJDpt5RvH599BnCT2U2uEeChFrjMSQuuF1kj19UdIDA_bsyPtFO6_dmrzNneFXcv9zTqUbZ5tNCF1xeEQLV3A7PrLPji0nJ7IujBtin5ilazC59JaIAOnJkfOCE74O7KTxfKNORoFzO6lK8O9zJiC7CEdgu_MqJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=R232RCcr4qJ62FZXvdv5ElO8qPCfHWeGSfW4Ay7zbj4E_UjldHMmKCZZ7MteMQn8KYSkkPWxN_1vwUnMRPObo5Npyijmpm6mdkjYo9SSGqIT992IcZx0E4H1nsZGOKMV4DuTmSNHD_Sn6Up_ZvK4sgilqPVKe45wiifQo0k3S6cfQfaLpdjCZioSivFWSZR3Izg3WxYMFBfLqSL5UjGIhal6ZXTL3KXHZAeafEJggg-LG0TpPZ7p4YF_ZXY60rQyrCDIGGYNyCfAayezOuzbBOo-OwSnr1pcO5KiCAhR7J1ewmIqca70B8QPCP_u-wi6iUs9NwD1dMhcam4JlD8rpXojOgSjNFvvlPUnjATQ16U2u9HzvjZcMCg_egK0dZm8ah6ZZBC55d4Olj9J54UjLqTW1F54mpQt8snxJ_WWBubC_MTg-8BOjpAjS1-I26XOPMCaMMFVu7aZi6ukbd4ffM4pxmgrLwZghPOZw0uIQ3udtbmEp_wdDe96n1gjLFWCNw4Gqj_jO0vMJDpt5RvH599BnCT2U2uEeChFrjMSQuuF1kj19UdIDA_bsyPtFO6_dmrzNneFXcv9zTqUbZ5tNCF1xeEQLV3A7PrLPji0nJ7IujBtin5ilazC59JaIAOnJkfOCE74O7KTxfKNORoFzO6lK8O9zJiC7CEdgu_MqJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Qwsby72As5almjVfgiRoRzNiUkreMEkVrxXcRaJ2odO6Dmn-6NkP6El2J2wA9g4fQ0mUkPCuQVbkZECVlbd7hAupJL1dijeiNkF2OBOV-v3UUA85dp2ovxLBTl60K47BXHGQtCtTdZrUzR2AX6VKWMvUce8A7a3qoALdfD_M49vRX2bBuOgx3FH5fVX22DYvJ3sSjHcJ1deeSp05B1nDFfH_XXC5gJNjfEBNLurbCk0sqgk3I7sTAgPiwZiFXkSv1XWGfDEx8nQGRE7C8oXPwymG47H93Yx5pGYyfoCc0a2-HW7b39g5d6m7vy86xAYlPigbcW9I8OYFwuYjUm0SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Qwsby72As5almjVfgiRoRzNiUkreMEkVrxXcRaJ2odO6Dmn-6NkP6El2J2wA9g4fQ0mUkPCuQVbkZECVlbd7hAupJL1dijeiNkF2OBOV-v3UUA85dp2ovxLBTl60K47BXHGQtCtTdZrUzR2AX6VKWMvUce8A7a3qoALdfD_M49vRX2bBuOgx3FH5fVX22DYvJ3sSjHcJ1deeSp05B1nDFfH_XXC5gJNjfEBNLurbCk0sqgk3I7sTAgPiwZiFXkSv1XWGfDEx8nQGRE7C8oXPwymG47H93Yx5pGYyfoCc0a2-HW7b39g5d6m7vy86xAYlPigbcW9I8OYFwuYjUm0SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=XaoIpFKqgis83H9VG79uifUYjGL5SC7kvcB4FTaobbo22S8273NWVclH5tELZr2w4_MFBcvUsflHMrZ0kCo5eciqUb1wy66g5ZakcRUxdUjJB6QrWyfgCE8u8ZKBaWTzODD5HYD2gvUVw8Y3CX18sW2qeXKS1qEHFCs4K_p8WxPYOoJxRCEupWhWj_2dldTN3Ti1dT2kpBHspksu6sEW3fPPSOsilo33eObPfV5ATnCSSgZGFwLYtPrDi9GFRisuK9KKXsnfsb4RUXmgXEom--DAHk23zqoE3Q5hBkXNNAweTlFj1nBHMz4oMWUXVLOYDlysonszNu5Piy1bb2ofrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=XaoIpFKqgis83H9VG79uifUYjGL5SC7kvcB4FTaobbo22S8273NWVclH5tELZr2w4_MFBcvUsflHMrZ0kCo5eciqUb1wy66g5ZakcRUxdUjJB6QrWyfgCE8u8ZKBaWTzODD5HYD2gvUVw8Y3CX18sW2qeXKS1qEHFCs4K_p8WxPYOoJxRCEupWhWj_2dldTN3Ti1dT2kpBHspksu6sEW3fPPSOsilo33eObPfV5ATnCSSgZGFwLYtPrDi9GFRisuK9KKXsnfsb4RUXmgXEom--DAHk23zqoE3Q5hBkXNNAweTlFj1nBHMz4oMWUXVLOYDlysonszNu5Piy1bb2ofrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=WBVgWE6SHyZH8pK9vCgWDT8AIiThA9krlCIhGbPfN0bGhUUmLrMcNR8RkowXcK6mno4CzBOLu8ACy_urV7R0xeVVBVv_RY-tVH6vTgVM8dOvS3xUlPR7ZvNpVgkBpeKTZfuphAtLSEj9on3xPFhGfrb8_LmwODA27HfZu2LMKErxEDiu2tWnqcJO-Go0x9vgInzR-e_qg6YnehH8VHB33oQE6TZ9-EHPeOQmbNg66WovTX3CmSkVhgnTc0A1a8pHnYhDQq2C2GLmFhOPjDd2-VULqrq62CKGsc_iZ54R6V1e-uUw5c25CmrLmJLcYFrTDn1GfrfK1UR8RVasGEcrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=WBVgWE6SHyZH8pK9vCgWDT8AIiThA9krlCIhGbPfN0bGhUUmLrMcNR8RkowXcK6mno4CzBOLu8ACy_urV7R0xeVVBVv_RY-tVH6vTgVM8dOvS3xUlPR7ZvNpVgkBpeKTZfuphAtLSEj9on3xPFhGfrb8_LmwODA27HfZu2LMKErxEDiu2tWnqcJO-Go0x9vgInzR-e_qg6YnehH8VHB33oQE6TZ9-EHPeOQmbNg66WovTX3CmSkVhgnTc0A1a8pHnYhDQq2C2GLmFhOPjDd2-VULqrq62CKGsc_iZ54R6V1e-uUw5c25CmrLmJLcYFrTDn1GfrfK1UR8RVasGEcrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JdakNNGJC-rm7SqTyXWhUsk7u5hncKyXQgf3m0PowebWZjl7Uh_MKFuYK7nRY1AsvPMa-exPbLmOpOl77Ry-G4NsRFNr5BKOKJpCAEzaJkRAD-FEFf-GOZlyBWNR_yg9Kz4PcaZyilDRHVnESEXhRJd_XnzKOadzBZOXMeODMA5VSDHQGG_TcDlt15snOokNPHiRmySuh4jovTbuWncMWxggtidehzK_afnw1_hHFNsqlUYIIgMRPH0GPEFU0GfnbXSA_UX0LDeh6fU9TSnxBceafllLq4PNg-liNF6dm6AHRw59dgCrfNMnzSP9k1V-QlbBMe1-Fi2m_60El1-vgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JdakNNGJC-rm7SqTyXWhUsk7u5hncKyXQgf3m0PowebWZjl7Uh_MKFuYK7nRY1AsvPMa-exPbLmOpOl77Ry-G4NsRFNr5BKOKJpCAEzaJkRAD-FEFf-GOZlyBWNR_yg9Kz4PcaZyilDRHVnESEXhRJd_XnzKOadzBZOXMeODMA5VSDHQGG_TcDlt15snOokNPHiRmySuh4jovTbuWncMWxggtidehzK_afnw1_hHFNsqlUYIIgMRPH0GPEFU0GfnbXSA_UX0LDeh6fU9TSnxBceafllLq4PNg-liNF6dm6AHRw59dgCrfNMnzSP9k1V-QlbBMe1-Fi2m_60El1-vgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gcHbNcGss8M1Y7a1uG9Mr258eYlrA4Ex9TwMqLYrLncRQpZAxzhyXM9GnJ1f2ZCH-6OaJFjPXWccLTQMKliuM5ZfmU-lN3TK2uq0fu1IxbfPIllXBRE1qhC6X3x9weczcTOo-Z4tMVjrqeq5JO3Kxt7rVh4LiKsqW6ERT5b9G_02Rpn1G5JBBfsK4QJlxfTWKVIk3mkER-nj5w0xejVcPcQy96Oy2qaIV7ldLadZkLVqeXYNTCTTRfc2NBjiRzKcWX7fF6P87PYRE1vRfMFWPuY206fYAPRkP2GawNQv8Sy7Vr_d7UFHa0Lt-TA8WJGllfjDJbX3EtorFug_WSGoyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gcHbNcGss8M1Y7a1uG9Mr258eYlrA4Ex9TwMqLYrLncRQpZAxzhyXM9GnJ1f2ZCH-6OaJFjPXWccLTQMKliuM5ZfmU-lN3TK2uq0fu1IxbfPIllXBRE1qhC6X3x9weczcTOo-Z4tMVjrqeq5JO3Kxt7rVh4LiKsqW6ERT5b9G_02Rpn1G5JBBfsK4QJlxfTWKVIk3mkER-nj5w0xejVcPcQy96Oy2qaIV7ldLadZkLVqeXYNTCTTRfc2NBjiRzKcWX7fF6P87PYRE1vRfMFWPuY206fYAPRkP2GawNQv8Sy7Vr_d7UFHa0Lt-TA8WJGllfjDJbX3EtorFug_WSGoyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=clAbl22gz4sApaKkMuhlup8N_rAXQMWv41zSlrES90jBh_DK5k7TVksHVFr4Qrorj2KoeuMgtPMJMCVPDw36tHtSizKfkqWL_RPGBqu_Y2YNRM_vv7A4jS8actufb7V3kF5H_jucN1LFSNuBAWeeCuBPkyev3R2DET-91yMu6jL5G0nQPl6GsUZWHOhYf0Hgt0U3V7ZpFyq9-4EcbTU-ukMByFaO8egKwdCaM4yVxhW33lRL0q9_9ecqNACQwWd2JC_VXBksc3870-O7XYqycS5sjsOKKQSr9nbxt8tAkS5o6qsztOTRS9H0anlQxXUAuJbNVKxCVGUdRMwI2LO9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=clAbl22gz4sApaKkMuhlup8N_rAXQMWv41zSlrES90jBh_DK5k7TVksHVFr4Qrorj2KoeuMgtPMJMCVPDw36tHtSizKfkqWL_RPGBqu_Y2YNRM_vv7A4jS8actufb7V3kF5H_jucN1LFSNuBAWeeCuBPkyev3R2DET-91yMu6jL5G0nQPl6GsUZWHOhYf0Hgt0U3V7ZpFyq9-4EcbTU-ukMByFaO8egKwdCaM4yVxhW33lRL0q9_9ecqNACQwWd2JC_VXBksc3870-O7XYqycS5sjsOKKQSr9nbxt8tAkS5o6qsztOTRS9H0anlQxXUAuJbNVKxCVGUdRMwI2LO9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=omGVREPWvH5WGOZ-0bayPMrw3yPDxBcx2u8Q_aV6nO4oFyAIWnpf-iZBbfF95Sxy1OBgOsd7Mp-_jVo-uDGpscZN_5k5pu0voS1iR5ObWHASpmTLc_hn2WLrLZZuPIxEzJmUp9FF2M1QTVhQ8-WnmQXYEcQ1TmKfL8KFYhk4yY7M9eaZdBb5xev9Yd1qHeswnHIk0eeOf9eXH3Dka24hY9uxtgi7GpKDRe2hvCWphIVEfKELmOT6FEmAvyYr4NsXmzBocAz6Kd-wwHj6lquZwl0Rl5wyqB0GiIvG2CLa70en4bvPKI6Mewbg-PrZaSnQz2oj9wG4S1ZIU2U9m0Lx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=omGVREPWvH5WGOZ-0bayPMrw3yPDxBcx2u8Q_aV6nO4oFyAIWnpf-iZBbfF95Sxy1OBgOsd7Mp-_jVo-uDGpscZN_5k5pu0voS1iR5ObWHASpmTLc_hn2WLrLZZuPIxEzJmUp9FF2M1QTVhQ8-WnmQXYEcQ1TmKfL8KFYhk4yY7M9eaZdBb5xev9Yd1qHeswnHIk0eeOf9eXH3Dka24hY9uxtgi7GpKDRe2hvCWphIVEfKELmOT6FEmAvyYr4NsXmzBocAz6Kd-wwHj6lquZwl0Rl5wyqB0GiIvG2CLa70en4bvPKI6Mewbg-PrZaSnQz2oj9wG4S1ZIU2U9m0Lx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN0WNZaLCTQK_bQwlLNdFX31NXzL1YnH1LljpUy28oEIh21Vuct43NvLRI6yXQ9WqImxUISkH1z9SgyEVatKg2_RjT9rAfe5WQBPp5HiaODJj-Az6N7I7rNKrJsw2sKKmqNg-pSMY3oKwozWSH5mxfSHgxH36GIQ6VBNNu_2W4qwKbNpOl1y3zQmf6J-Jbzel3AYAursa2WONnBkV5LaQvMO7CPk-64fS9FEEg3hLZX_Q7tsS664Y4Rxh2pEAA7XWNZD84uEPFaNJuHJfa5GGe4ZaMs6Qc1RJ0XsdBPlTtFpEJ21LuGwf0ugpjBgFWJRzta79C4wOiqc5bYz7S6HXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=LUDzBFvVv4DRS27A-mlrVqqCGF23_pOHTj_Gb8x28TOvlTFJXYU6AkgpNQu5BloypYO6LPfmzZ58PfIGY2q3ayZ3X9R8bX1GWmlzkcmUDKYjt_n5n9H0KnyxI2lXH_mMLsfRb5iDsjBwEt4s_EuTRjfu7FGYbLTpJhkRyvgH0-imX6WjfwHSIbydNdkmVj7Tu707G9ivX68uxIvOGz_YD6JUNSjrvRaSKt7ww-_snC1nw7g8D0ykDYfMOZudQsDACR7n3UO9oUecg4A1m-8h2egPeMMXTmr1cuVie41GsC0Kw_wZCAG_iTt9aBNi9KbOpc-vIVKYCYk5YNxBfqyahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=LUDzBFvVv4DRS27A-mlrVqqCGF23_pOHTj_Gb8x28TOvlTFJXYU6AkgpNQu5BloypYO6LPfmzZ58PfIGY2q3ayZ3X9R8bX1GWmlzkcmUDKYjt_n5n9H0KnyxI2lXH_mMLsfRb5iDsjBwEt4s_EuTRjfu7FGYbLTpJhkRyvgH0-imX6WjfwHSIbydNdkmVj7Tu707G9ivX68uxIvOGz_YD6JUNSjrvRaSKt7ww-_snC1nw7g8D0ykDYfMOZudQsDACR7n3UO9oUecg4A1m-8h2egPeMMXTmr1cuVie41GsC0Kw_wZCAG_iTt9aBNi9KbOpc-vIVKYCYk5YNxBfqyahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tjrZkYBNG63mXVc0704pr4ngpBFgOls3fOxbE4PwoGhizYGdgeelVtHLNJ7Gg1FPR7zstbYNFN-1qn6lYKvE_7ntGTiIUgm4dTsfbChX3EYoInieBZvu7FoU-FK-2fsT86Of5jJGqa69gnL2z-smnk9afT2kj5-N60u44WBjqEwcprX8Qd9IUQ7O6jiLmg67ubYNUI28A8NqSdFoCDMOyvNrpSF9aWC1bKS0reK8oHITmXrvKiiceI8KwkZbw7tpV3ame--U43mbX8lq_8hdPmyKzyGhbUi4wZIYEz3_LUMhuAZxxgExDHn8JNUV5HnahXnAkovmk8gZbPeCO8_3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tjrZkYBNG63mXVc0704pr4ngpBFgOls3fOxbE4PwoGhizYGdgeelVtHLNJ7Gg1FPR7zstbYNFN-1qn6lYKvE_7ntGTiIUgm4dTsfbChX3EYoInieBZvu7FoU-FK-2fsT86Of5jJGqa69gnL2z-smnk9afT2kj5-N60u44WBjqEwcprX8Qd9IUQ7O6jiLmg67ubYNUI28A8NqSdFoCDMOyvNrpSF9aWC1bKS0reK8oHITmXrvKiiceI8KwkZbw7tpV3ame--U43mbX8lq_8hdPmyKzyGhbUi4wZIYEz3_LUMhuAZxxgExDHn8JNUV5HnahXnAkovmk8gZbPeCO8_3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nhDDEKXVUtYdHZez3_qHz0k2EXlc9RqEUZvUdcc3AfLdXI4Z15qEG-BS40n2uqesII-6n5rWwAfa0NshBVis-lctOIdb8_QMOtZjCmLxjIRgsXJHfaux9M3n4R1LM3i4l6Tlv2ob4uM6hOSFeXjYlN7drbXPnY33vfXF6vH0gh1BFfCsSCJvYd4YA2vkr5Qw4uCnHiacOKjAHwsFVulg6nhPAMDUPWpaa9lA_G2f9KdfuZVprnSIPArLn9qA0cMDBEyNKwZhlirdaHQgTOHu01fewhF4dFqZ0vE6jCk5oDTAPor6_zqYD8KsW4EiH3pfY__mzUhH1UlSQVZAJd6IyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nhDDEKXVUtYdHZez3_qHz0k2EXlc9RqEUZvUdcc3AfLdXI4Z15qEG-BS40n2uqesII-6n5rWwAfa0NshBVis-lctOIdb8_QMOtZjCmLxjIRgsXJHfaux9M3n4R1LM3i4l6Tlv2ob4uM6hOSFeXjYlN7drbXPnY33vfXF6vH0gh1BFfCsSCJvYd4YA2vkr5Qw4uCnHiacOKjAHwsFVulg6nhPAMDUPWpaa9lA_G2f9KdfuZVprnSIPArLn9qA0cMDBEyNKwZhlirdaHQgTOHu01fewhF4dFqZ0vE6jCk5oDTAPor6_zqYD8KsW4EiH3pfY__mzUhH1UlSQVZAJd6IyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=RocScbe5jfFabBhlINZAQEbXjgletGt44IjdpY_BRbtdxBYwSnUvN3k5btvi5IGBf2HaR95ztct9l85jZpjS-TMJdvvtIoRGPKzsU9FAlAFo9ZrB319Cirvz7F9RWwaKD0fEvKZAfLch4AgpeBqiW6M9mbqMVVVAicOlh2bDe-VAM32F0N3dA7RBnghs3u2x8kqiXvSvpfkxZ5G3gT6jN3lgcM9nDX2YTu53MGjTRFOgFH_n55wpuGVT3aAosfVIBZrRsXWZePjQaK5bJVJixFVNfQBlULVaFXwgXq6vxjO2RagdoP-0K-Vf9WTOX2OKPaZP4QpYO642uGoxhtWD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=RocScbe5jfFabBhlINZAQEbXjgletGt44IjdpY_BRbtdxBYwSnUvN3k5btvi5IGBf2HaR95ztct9l85jZpjS-TMJdvvtIoRGPKzsU9FAlAFo9ZrB319Cirvz7F9RWwaKD0fEvKZAfLch4AgpeBqiW6M9mbqMVVVAicOlh2bDe-VAM32F0N3dA7RBnghs3u2x8kqiXvSvpfkxZ5G3gT6jN3lgcM9nDX2YTu53MGjTRFOgFH_n55wpuGVT3aAosfVIBZrRsXWZePjQaK5bJVJixFVNfQBlULVaFXwgXq6vxjO2RagdoP-0K-Vf9WTOX2OKPaZP4QpYO642uGoxhtWD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBJOQJsebZbRP97JM4QJbAlZ4Pan7qixwPfD6LP82p26kQhwGhqpqBnR93UzL4d8Z4urJed3CKMshUI_pERms03KaodHGAIXZSPnq2m1GnLF_t6aa5w2vrBvR16Uddo321FS2ZSfQdLIy0033jHbSfwkC8SQ5n3v-TrTzvaYr11ddON0krGAQ0ddZKuMydzfvKQVZBVPxxJRbUsVRfuix5ieLItUJphW5w7ULImw85jzvPZ1jDQHF2FwwxeqVpcpeeAO4Rp8S84Z3q15zrlICQH7WpnRV5iB39Y0UzFQYHHsJl7Bl4FpET8oH0Up0kD79JxTPnI0ALrMu41LkvJFCg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=q-rbToASag7a0WT6o7XqmfA-A7-irn7KHJwG2yfFQ925INX_dLsDgOVcW75MgWTKcwJTv6_XVsduPvckYiGh8n0rb4are2uHD93zbwVtcwxn5v9J8SbWh-9ljAQjaG901ptYktfObptGsvEZ-i09IBl2S0arPrZ11XnFpSZ8wiYgBTr3MasfSjkdVZEXDT_8ty3YTbwbt3_OMsBNmg3QAiopaTryoGQ_nOG9bLoaZrnpGDzH31tBDWF-dJGDImkukyZOqcXuLX_zT6ogXy6n9Jj9ku1oHkTKKcRs4ElDAp9ZR3wE1U2ALj4cHW22W9ZiMoajZjH-9asED20v7XmmHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=q-rbToASag7a0WT6o7XqmfA-A7-irn7KHJwG2yfFQ925INX_dLsDgOVcW75MgWTKcwJTv6_XVsduPvckYiGh8n0rb4are2uHD93zbwVtcwxn5v9J8SbWh-9ljAQjaG901ptYktfObptGsvEZ-i09IBl2S0arPrZ11XnFpSZ8wiYgBTr3MasfSjkdVZEXDT_8ty3YTbwbt3_OMsBNmg3QAiopaTryoGQ_nOG9bLoaZrnpGDzH31tBDWF-dJGDImkukyZOqcXuLX_zT6ogXy6n9Jj9ku1oHkTKKcRs4ElDAp9ZR3wE1U2ALj4cHW22W9ZiMoajZjH-9asED20v7XmmHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=UvFbx-w0Ta-ZObQ7MqWlnQJP9KjpzKgyZd4xq4geW8ZCaflp-wboq8kp1HP5JQdbQ9WJhvsmBRORspdSuHZDZTJK-P4Wjgw9zNhpgYIDjDvPYpt47sTALbUnQ5Y1oPR5zOFfsUaTV9-HEWv10630oDp6Xw7k46yQT01ktlt1VqQ-HLV1Lys_lvg4rsZdj1sqEQzv6obpcBDKXiAqOGj2kvnwjnhRDl5dDDWZ-bRs3xGW_aWn5Ihkyx68s5B9RwJclOHFAHCJe3sBXbMp7HWqA6xK5f62DmLvru-OAYU79Q16IcwguS3ejh5vJOUl7rrG5MTZ40hR67qusu8hOOScbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=UvFbx-w0Ta-ZObQ7MqWlnQJP9KjpzKgyZd4xq4geW8ZCaflp-wboq8kp1HP5JQdbQ9WJhvsmBRORspdSuHZDZTJK-P4Wjgw9zNhpgYIDjDvPYpt47sTALbUnQ5Y1oPR5zOFfsUaTV9-HEWv10630oDp6Xw7k46yQT01ktlt1VqQ-HLV1Lys_lvg4rsZdj1sqEQzv6obpcBDKXiAqOGj2kvnwjnhRDl5dDDWZ-bRs3xGW_aWn5Ihkyx68s5B9RwJclOHFAHCJe3sBXbMp7HWqA6xK5f62DmLvru-OAYU79Q16IcwguS3ejh5vJOUl7rrG5MTZ40hR67qusu8hOOScbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxHBMBeFJ3GLJbwrbo0gcoGnmASTXB1JWUbfM5sA1mIXH_r9veMSa1NIhw9Jfc7uLoqTmJEenKIuLVOXRlofvpMHZUhiiNRbrpd-MqmCdhgjosa0GQvexlkk9zqKYN04bAeWBt01kLZMMu_uNBsE0HrFnDi78ckUMKwJRAP4MOzGoq8Kf6IrIm_uMUCNIzUEQEzx1f1_THp9k7ZdrSV8rNsYoSGTxnpF8PFDQ4rMvhUl_sVXgZgofpE1beewlpC19Ae_hZGYtq0rasI4cYXjsXiTgnqn2UWK-vP-rEZQDKuJyWuNpM5t36kV_TWvinQ8-sC27anUycTwa53u5ZuoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1ilfYkpTwO4rvtDLUHDgP1Q1GUQVGS9pFmOPpdaHRVCmX4oAUdKWZ7EZaMozfg55SyJ0TLcV6rE3lwnG-3HCRCXWhv9j7fuR7vBAb1cNsjA3JJ2fq6zfiypbR5z9L4tKGfLc0vVqzDN5cOgyCpOfV_F7k6owbTCsjR2oLtt52xRL-1vjdK4tX4m_6Uhnw4whElLWQeHBy-SI7c_LoThZGCPwoIGPcIIsly0l43bM0hf4X0Y2HZLiv_8XXr9L-VZgfOE1PGxn0eF27-fqSJSkQWri-z5jxVsEesxW6X53yMDNrfx-uDRjyLJMmEd_MNIddPk1AETO9Jy3ZrZP_jLtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YcTW1iZlt2TqeyEpdzyiJRvvryA-3BLx2up1SgX-ZLLCWEDvTUHMuIvohiU2QS3oyWeKOm5awHkcj1KhERg10jr7YjjPoO74Lcs2OCUYeONZL1w23xMuvOWkTxy48ACXL95l7MBCVEAohmqwSPJYPZhRdbCK3kh8sTNk829kLeIyux36vn1yH7bPmYZEzT5m_yXXV6EsCPEYEsMXf52TWocvHN75TrtlMH1N9jvFbWUdLO8V-SH4QaES7p8SdO0Eal9z5ToVgUuLHj9LWMUpWqaGinhMn4VLkxNhTP-8MrP0dpg9AwdY3crceNUJZbdChwwaAB-pwSOcZJyJ82EhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YcTW1iZlt2TqeyEpdzyiJRvvryA-3BLx2up1SgX-ZLLCWEDvTUHMuIvohiU2QS3oyWeKOm5awHkcj1KhERg10jr7YjjPoO74Lcs2OCUYeONZL1w23xMuvOWkTxy48ACXL95l7MBCVEAohmqwSPJYPZhRdbCK3kh8sTNk829kLeIyux36vn1yH7bPmYZEzT5m_yXXV6EsCPEYEsMXf52TWocvHN75TrtlMH1N9jvFbWUdLO8V-SH4QaES7p8SdO0Eal9z5ToVgUuLHj9LWMUpWqaGinhMn4VLkxNhTP-8MrP0dpg9AwdY3crceNUJZbdChwwaAB-pwSOcZJyJ82EhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGuRAPRPaNT3p7ozn7UYpaBX_ltJUs_M4DiWoiW8pkgR-jKiAX8CkoE6rKhUwzhay5luvAcliWBgNSsmPZUSVsQNVFiZZF0iBUFdQ68_WUtJuYfw5XNwwUzV1EIgnD_u6-_VPY69R3NYAoL0J3Bc7MEqgFyrKnidJfPfQgCBATP76tBvl9PcTUAX0wgWpfr1ONVkIok3IqI5gi1H1YYa9eJUx7tgASgB152H5RfubY11AlwQGy5eXKp1W51Rm5h1zx2fdQqyl0jbYT9yUbZEHMyXhYwlB_-TSosqxrUDWf8XuU0zVYsXr-uOjVE4VlEVeEwXiEgrVZ1xAWMGH9Z5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7L7X_aHLSgp3ZL8SrTEQ-f3lfK2Kqk-FiRvkFEkkhKp3KeyWpWiXrEZ565NCQj1YA5F-gP60aOmabzAahMwcLnzmNN2nvmgDrUqKvg_mUmEYqpsXmV5s_HRaJt5EJE6nZ2LXfTtWWsvbirMgV7vYrCeI72k5VoTCOue5937-aQwfkpW7euVpJ5OfwofOYx7BW4b-RXPgwzXoJvO4TnfKkj6cZ_Q4gXst8jtgoaqGMVQAXrXO2fSiikhRkDp4cnReEu_fs2rnBxi5LxZDcdWXEmX6bAPeUrJfbUatjjo9DsETXbagEMo7NrzKYaSPZbjJIAin6J0lqd_DwEoWY3TkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsaNPsp-imBsYVm-2k63OmPIvvVQUim388RtNgs4RYwB9MNlrp5DGsJ_qebDIiGUUH3_kkOERwTI3QvqWAjNZSvVXUuRyxVomExR6SbN4_ddofX70ekfPIiyvduSCncSAgsqBW3FzI0K2jpugj2ChFQJnS67qRwfY98dyLtagSlXdkb04CBV_UTzsg1x-D4gzemZfjLV-OYpX3KNell0rPUKjbxVfN-ke5I7fuUxebgjg1oSZd-ZPnoTyYGn3m9-UL6pFJsdVZ_B1UN2HXHawIoK5zID9RwB_DbxHBAy6Rh9HxvlyuANo8RkSMA8o-e0pFWKyiVQ5N_8bFVA5iMYhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZKbG_mQ1ka8B6jSjTf4qE-d730ONVT5SzXY_2LtthBPS27Hcu4hyJe8zUId9852e2VvbAueyQmtr1HnxDvYAQefbBApaVHZderM6fjWrM1jXH4aBQGtr4XS_CCiGqABOeAK9nCjRZnw9wONYxC0MaXhW48TX6xekFAUu8X9uJVfnCMRBfUk3oHlbQqEnvT7WkmoWjjp0F4ygyWJdUFYSq2f-zi1bMYpkW_zT4aY9SKE4zioEygmd5E31fQLYixVHMaeiD1p2_tnla1D2fuaUW8zg1XolSrj6q24D77n-t_oY0PQNtodq0nmIC8WZS20p51LWZ9lvtdJgyq_-Ht1Jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZKbG_mQ1ka8B6jSjTf4qE-d730ONVT5SzXY_2LtthBPS27Hcu4hyJe8zUId9852e2VvbAueyQmtr1HnxDvYAQefbBApaVHZderM6fjWrM1jXH4aBQGtr4XS_CCiGqABOeAK9nCjRZnw9wONYxC0MaXhW48TX6xekFAUu8X9uJVfnCMRBfUk3oHlbQqEnvT7WkmoWjjp0F4ygyWJdUFYSq2f-zi1bMYpkW_zT4aY9SKE4zioEygmd5E31fQLYixVHMaeiD1p2_tnla1D2fuaUW8zg1XolSrj6q24D77n-t_oY0PQNtodq0nmIC8WZS20p51LWZ9lvtdJgyq_-Ht1Jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Gsgh8ElZ6H-k5lahrWbNnEWfW3tPxaPqFHSjhou5Btds57xu0PAAJmpiOI6X92b0D-spW4ypQcldqtgVRwZJkHfJM_RP1-a7f7_J1cEHcxt8O_N1c4r_Sn1enyH-e_Fvx7E1rTRWHtms_XdPgbsRXKM7P18B1YtV7UOuULi3VtxMTas-IeylpUJ1PRLcsPwvQVHIx7QN2Y42XDdUJdy8rx3hugXp0nA0HqR1o6Dt92SBG6hkjl0hemWlFOaiTUagvWe6xP5a4MSKexZ7vVUrPsN7qU0oB9w7OQ8q_SrfR20UROibSDCHF9DQWPeF687wLkJSui7qPv1y4gxUWWc8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Gsgh8ElZ6H-k5lahrWbNnEWfW3tPxaPqFHSjhou5Btds57xu0PAAJmpiOI6X92b0D-spW4ypQcldqtgVRwZJkHfJM_RP1-a7f7_J1cEHcxt8O_N1c4r_Sn1enyH-e_Fvx7E1rTRWHtms_XdPgbsRXKM7P18B1YtV7UOuULi3VtxMTas-IeylpUJ1PRLcsPwvQVHIx7QN2Y42XDdUJdy8rx3hugXp0nA0HqR1o6Dt92SBG6hkjl0hemWlFOaiTUagvWe6xP5a4MSKexZ7vVUrPsN7qU0oB9w7OQ8q_SrfR20UROibSDCHF9DQWPeF687wLkJSui7qPv1y4gxUWWc8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=dyfkRee5Ba_mdE42WoPuvo_LzS9LB78jNq2rBnCmDHmfUHJuCK2N133ZDfaIgyMdLXKwzlJENKTh6jTStSbz7TlopvOlIG1_v-f2WpoI2SEJbvx5s_jtbjaCjocsMh2jApUD28hbwKAxKsZTF3BW-jz_-1TFRlmVvyVIR65hEY1Npag6IeyrvrCMwIKdnzwP_55RC18MqSJn4ipf3V9OfYXbKcoqmQ7TmhtmEgCuvtLSCkzK10DAzBuObe58LxOyXHY0cr8vhx51iEvY54e3atd6IWGEQTC2F7scXqdKt42uafPBN9GrQHp7SBsemLgyJCHK11ocXRkHUtn-GmNiGo561PXDWFlimPnOfjTFZkwcuVAEfiMSo5-M1TDgkbz6YsQFbq4VYzsvL179nlDCzKFuot5sxZ1HYuXG15eDnaGEjvD9NcntnSEp4l2dgfBPwEyy0LzOglRrs6oFjCeAtZRsyFS5_eksC3RjBuPMOYmxK_QycA7YJmNYEus1JWriyXyYoMPWcpK_C2_Y4fbKLi5jkbTRivnF_o6uZpgDIQu6-xgiYqlRFdzTmVnWqB6URAboCdKqAvx72joaHNuQJCWDeeycB_BahfTMRc_UpO9lJY7nQCtU41RMEOFL4sDeHZtwZIdfP0kfJelrYj-F_KH_-Au3G8nj8LPud3j1S6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=dyfkRee5Ba_mdE42WoPuvo_LzS9LB78jNq2rBnCmDHmfUHJuCK2N133ZDfaIgyMdLXKwzlJENKTh6jTStSbz7TlopvOlIG1_v-f2WpoI2SEJbvx5s_jtbjaCjocsMh2jApUD28hbwKAxKsZTF3BW-jz_-1TFRlmVvyVIR65hEY1Npag6IeyrvrCMwIKdnzwP_55RC18MqSJn4ipf3V9OfYXbKcoqmQ7TmhtmEgCuvtLSCkzK10DAzBuObe58LxOyXHY0cr8vhx51iEvY54e3atd6IWGEQTC2F7scXqdKt42uafPBN9GrQHp7SBsemLgyJCHK11ocXRkHUtn-GmNiGo561PXDWFlimPnOfjTFZkwcuVAEfiMSo5-M1TDgkbz6YsQFbq4VYzsvL179nlDCzKFuot5sxZ1HYuXG15eDnaGEjvD9NcntnSEp4l2dgfBPwEyy0LzOglRrs6oFjCeAtZRsyFS5_eksC3RjBuPMOYmxK_QycA7YJmNYEus1JWriyXyYoMPWcpK_C2_Y4fbKLi5jkbTRivnF_o6uZpgDIQu6-xgiYqlRFdzTmVnWqB6URAboCdKqAvx72joaHNuQJCWDeeycB_BahfTMRc_UpO9lJY7nQCtU41RMEOFL4sDeHZtwZIdfP0kfJelrYj-F_KH_-Au3G8nj8LPud3j1S6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UdHlBds-7g6Tw56Bj3klgVWZm-tXUQICQ5OG7Ml03Q2rcQDqVjFbHqNZeLjpG0EiBYOcLmRHfdODq-1-FuI1sPpPIwvE3jff16xyX0M5Zs9pc4AuaTsz8uCwg8WfYk9ps13JEOloQRmJAMoHg662QBFqrFcvAB0NKjlsxxgSGo9gTxWAYWyconwXV84SCoS5E7sH4L8pHUJlEh8HJr6Vlt8EKwsMvMuuIdMh0Sv__XmxmPSxsXHjxXNVfFCE4DRpYNYQv7lHH4YIsXEg1KEFLFWVXvf2fn17vDFmqLHfeFQ07YWahYfEI7M-uz3g1sSUDTYtzyYnMn7K-hN9XOc0sD3iO3_HfYLtMJOQrvgBVg2DucXKptCpzke5ri0uvZENAF4xMaNJsKa_-FqrViqjnlRyD82BBctqP_HdsY8bKQaBPbMzH9WoKb6UcLMe2XmngFLdunpxk4uLQgf0HzF-4JBpQMXC4_R-7lR7aJuyhiskDjaW5JmHBBZOry6m5abRd1U8mOTOfG4P3642vpxYWlJxQZq9JmrI3d27ZX-dl50mdH6V_UK4QnJookicBGv2uRkiTgVLs8m_y2IpSWrY0Ac5ZWvjwoTPwjmR5FNyqGUGesyBoaiecVACy-oe4l04NHp9LNwSrlPkB7ToNZ8cSq2uhH9A9Czsxy7hIgDOzJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UdHlBds-7g6Tw56Bj3klgVWZm-tXUQICQ5OG7Ml03Q2rcQDqVjFbHqNZeLjpG0EiBYOcLmRHfdODq-1-FuI1sPpPIwvE3jff16xyX0M5Zs9pc4AuaTsz8uCwg8WfYk9ps13JEOloQRmJAMoHg662QBFqrFcvAB0NKjlsxxgSGo9gTxWAYWyconwXV84SCoS5E7sH4L8pHUJlEh8HJr6Vlt8EKwsMvMuuIdMh0Sv__XmxmPSxsXHjxXNVfFCE4DRpYNYQv7lHH4YIsXEg1KEFLFWVXvf2fn17vDFmqLHfeFQ07YWahYfEI7M-uz3g1sSUDTYtzyYnMn7K-hN9XOc0sD3iO3_HfYLtMJOQrvgBVg2DucXKptCpzke5ri0uvZENAF4xMaNJsKa_-FqrViqjnlRyD82BBctqP_HdsY8bKQaBPbMzH9WoKb6UcLMe2XmngFLdunpxk4uLQgf0HzF-4JBpQMXC4_R-7lR7aJuyhiskDjaW5JmHBBZOry6m5abRd1U8mOTOfG4P3642vpxYWlJxQZq9JmrI3d27ZX-dl50mdH6V_UK4QnJookicBGv2uRkiTgVLs8m_y2IpSWrY0Ac5ZWvjwoTPwjmR5FNyqGUGesyBoaiecVACy-oe4l04NHp9LNwSrlPkB7ToNZ8cSq2uhH9A9Czsxy7hIgDOzJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IhrDHUvzTC8jhDPo47IabHec_y39DKEpNmnkdcSgmtLkFTsUpxz8g5aq62h2bjduEoC4GGMiKRkHkL966GAcAy7tYws9hLXX403DDOsOahtDcrQTVtG_FK9USWaZONpujmCWrmnEonGRmC2mwqS7udHQ3_j1vNQZtcQ1xDgdCtMFjWHgr5_ail7qDC1QzS9C0QEFnvOfTSpnoR1mYlLgtKikaVZ3s3o06BCnws8tqzNkKgXULJNY0n_7xIhFD4F5GZXuUKOk8IecW6L2_ykWMgsecH7ZPUXcQ0rBKT4_-r_v8HwtxRAF6EQ4SrIK6990ZxJWUy_cbNc45Foqcf7Mtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IhrDHUvzTC8jhDPo47IabHec_y39DKEpNmnkdcSgmtLkFTsUpxz8g5aq62h2bjduEoC4GGMiKRkHkL966GAcAy7tYws9hLXX403DDOsOahtDcrQTVtG_FK9USWaZONpujmCWrmnEonGRmC2mwqS7udHQ3_j1vNQZtcQ1xDgdCtMFjWHgr5_ail7qDC1QzS9C0QEFnvOfTSpnoR1mYlLgtKikaVZ3s3o06BCnws8tqzNkKgXULJNY0n_7xIhFD4F5GZXuUKOk8IecW6L2_ykWMgsecH7ZPUXcQ0rBKT4_-r_v8HwtxRAF6EQ4SrIK6990ZxJWUy_cbNc45Foqcf7Mtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mimA6sA7Oo0SzkxTX3SiQeaU51pon7iclFkPPSq-TbyDD6IUB4RhHZnTaTeCXdIKWQIcf6jQuW7CUcTONVIgJHD53xWIT7csuqXepqeNN5-CKayNuO6mdON3OBNMHlXCc61aqo6zof8rA3tfcpipILOa8zScCMUjeL1_jYQr_zXpSUZKDC3ZV8JsHwZqTR3WZsl0cS_v9fnhAlTm_fSTdCJW24OVvPqfag7UgSLFP8I2NPFl11WiVb4brQ_niyIub9iPTkvHP3vrKYoMIglCoDqMDbJd6v3priXwYxejU2ku-M6wYXip_IVxCHKu4t69AiR3w_4O68XbH9vq-1YxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=tFRbFH79j-S5w3p2cvETSWu9em6f4yWcMgoUwiGpzV6eP4HOLX45QjgyJlb_FRYtBBnqkFyI9Jj72Y0RDDRBpN7zuOcIUNPOG5OxO7t2hH3jGpfM_Bw4OxoZenxR1T0DzvNTwTNjB1mYcB2xoQGGnCexyhrL1577oEv7EoaD6OdNbaqCy5yNJaOwg6HQ5G3Lqu0oVcr_x1HkykVbEmslgQ_6TeNpqHcCtoB1qjE8R7FBeVDL1IDVpYvP2y1kGvWP4HYDWu7oizJpmtVfVw2gNzn-6dAJm9pSdfQLoPoU_R5rJrQxDvnYKt7DqADou7z_2YUEMKidnvvnAr23ZQZTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=tFRbFH79j-S5w3p2cvETSWu9em6f4yWcMgoUwiGpzV6eP4HOLX45QjgyJlb_FRYtBBnqkFyI9Jj72Y0RDDRBpN7zuOcIUNPOG5OxO7t2hH3jGpfM_Bw4OxoZenxR1T0DzvNTwTNjB1mYcB2xoQGGnCexyhrL1577oEv7EoaD6OdNbaqCy5yNJaOwg6HQ5G3Lqu0oVcr_x1HkykVbEmslgQ_6TeNpqHcCtoB1qjE8R7FBeVDL1IDVpYvP2y1kGvWP4HYDWu7oizJpmtVfVw2gNzn-6dAJm9pSdfQLoPoU_R5rJrQxDvnYKt7DqADou7z_2YUEMKidnvvnAr23ZQZTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H_iyBs3tp2BdHKIBBGBUCHOM1KzIxJ-zoj3qQ_y6BWMfQRFs0G3q9cu5iOEiQ19sZKSe1EO9RTzwJ8O4QPyYdgCl9a6RL9WRPs7igFVFJVZDXYzsUJN8OV2BZcpup7qJQLr3QlYyWe5Md0d_OdHj_-Vi1nC_LKCU0CILnX6_YoIZeokgNn1W9sfdG9Xlt62I9K8RhYnT5kwGdY599Vp8HeUMwzeEFgmMi9-a4_zTe8LHkQ7e-ZzNX9tQnX49lv7apyx-FqQIFDXwdf-1J6S1AvJSe_rUr1jpIHIe1uXjRfxMHsorN4gH2KsdBJMf3wEcISCIuLuWGLFf_GPup5ewNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H_iyBs3tp2BdHKIBBGBUCHOM1KzIxJ-zoj3qQ_y6BWMfQRFs0G3q9cu5iOEiQ19sZKSe1EO9RTzwJ8O4QPyYdgCl9a6RL9WRPs7igFVFJVZDXYzsUJN8OV2BZcpup7qJQLr3QlYyWe5Md0d_OdHj_-Vi1nC_LKCU0CILnX6_YoIZeokgNn1W9sfdG9Xlt62I9K8RhYnT5kwGdY599Vp8HeUMwzeEFgmMi9-a4_zTe8LHkQ7e-ZzNX9tQnX49lv7apyx-FqQIFDXwdf-1J6S1AvJSe_rUr1jpIHIe1uXjRfxMHsorN4gH2KsdBJMf3wEcISCIuLuWGLFf_GPup5ewNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu57nCwo1Dd_MHQaOuDndLJi-xlrBpdznuiiO6CIRHqdYE2o_Ws6vQ1abU1OB8M8vSLVEBKupHirhpzCJlHf5TTQjT8Ub9R__Wc5PhFx7AwAjDsHCYT0nXADpAeymWzqO86UMlxKFqtCikdXU0OEYbRQHV4CCzHUsQWdOvBmnUdAboaj8knQwoMStVlYsQucBP8V3gSjEHmWK0nn6tKF8WjIMrO5AJB9L6MzdSy9M8K9A2AFHO3sLGJcuyBgnBEioncheEmGO-eJtgFuWB2d-7juStlutMULVQMotYSW0wQbl6OwqYm_Uhln3hRTiM2yxyIK-gaGhaXD5AZA6WaE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcd4MYUWP_GhgkAxwiFFEjVgqV5CsJAAMwGuDn-oUVWMM5d0_lr3PwtdERz5utR2nutlkWn6Hf6Uc9HStMKn2qBwtFTksCJi1Mj7V_XdGFMKofjLhNrichx7Cl-dpzHsf77VT_fcgECPXryXhHSjgQfA_8tpIAaZJ_dv7SzVHNX6u1m-uopXdCsatSxqOxu04CulHuIrQQwF_qoYVZCDE1F6C-9cEMBWkUrj6XF9uNx5eSORInc3M4q8CO8kVWu61KV8uSprbAYmuqU1C_YtD8rm7LAKNv_Qk2ryKfS9xITOrJYk9V2p3Iy-J9U0mrQbZawRwb2yBHIhiLrpc7Yq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXr-jC5XzRMGyjEg0WYvWKh9Ewd_LAyJqDP64dvZt67JtBHGfzUY2VGI8XqdIyb6jbDEEGcVIR3lDlFa62U6qteMh1q253GwuNQZ_NxQ82iVCbT7pSBoue6rximqQbGPs_qe0WgLphWg1L-TYKQimMjunUw1hKNCDWpxfGt2NR3SrhH6PkuRBGNVEvVW-gbxOXExkC1gKbKAI2JLFQspRu3l-OGbBsjYOq6h1lSlXZS-7WFAbedXtJj66BubTgjKU3IBqC8vKORTY5Vq2jxRSIaRrPowDw_TWcP975nyDE1Rfek2WbEMJ1EIcQ7Y_K-Kpk6nA1Bxru9Q7FRDnfBN8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os0zzx-sZWPsGu6dLbu5UQBABeVqIsnnNudvj14LpKa0LikwTwRVUyfKwsxHG7PZHLPC4VatNgNIP_hxK7hoAuTrIszJeuskvi-VRsVJAi1EZV_LHGuDslSFrABhhoh-dgNbX27OUJLMNkRhmSKnLQc33OLFLry2xz9Zgks0RIefuTI1dIBmeTuTSLJP17FVpJMJumb6HzPzD0CYdkdXPcdz2lVPQA-DMiD5g88HV8QJPIyIG-yhkv9VP2G3VlUnAtCj64ffLZdLRgue4vYymDkaWuEBJyK5BlIphJmH9FQRuhwCO7ve7AIu0Ul-qssFLaywDgNb9_Fjp6Fcp2cg2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNmZQ6oqbXHYOhB-LlxrlDlhhL2TB3mzsYjJ39rs5eggvGE6ZsBadXWDpxpdFqn0T3i6mCrZ7rlX4f1Pr7unue_n9A4LG7uNlYV3Mfs8vJxdx-vlCi3i1izTsCzRkVOzVq3PVr1NpdtThBv2em04-6Y4ih7GLDHXLbPnlbiu4fkWp4KrvFbRZFhNJQ-a8nPgrTBH88zE4Tt_lv9-cytG9y9Jb3-oa-9qEGhp5nFLoDaR1FTaOOn2DqrO6WxLuvLoCMKv6HIeZwwPh5G0OcDF6WZeg94DrOHI4ECW484rHh4sijaZcUhr3oRETGFgrvSTVYoHvEfxBnNyZ0A4nn-yrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYoqr1ziUNFY9SHZmxakltmMiHU49evqWJWPzBhJKB590Ve0l0gd1AzUmhSW5PUqxKMS13oymh-g4Ea56I1qzQLJPdQf_y9wbqizL1-uGlSh3I2vaRS1Auqbl6yHs5vZwTYPUsTcly3FqFyGKtbnQFodODJUPNIMt47ES2adm7UiSXR8wp7K6-9Wc2KeQnQP39UDz0BrTtZRAnm1v4YVbfLr4kHR6TqHJlUvfbbMlEejWU6hYB7M7LJsrbpW24_JfmIH2DNk5_Yf0euhxa9h8Kdsjvw6Di79CkkB4H_055QJQBSGy7tWvNNGYePz-RsaWAi3co6oC5j6l1coFeHJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giuwtS-P3qCZzHSkRW4INTtM4xalkUag8GUhmYmALL7X272quwv6JTooyjf2jDCA6hRz520n4k-u23sTZ_N5rOL7pokwugZyXjroz2aAvLWGtXjdoE2_sm9MtYgmQwpiNI2rkw51HYHXDjbUctkKdSWSwnfK4jGx2ZMNRtEdyHT4J5s7SahNEijvNq09L12PvuH2-zmOtjy0rAy0hDVVg5lVlGb35-6zLL7ryiKzat-M5yA6s_T62wuzgYHOL2_dI7ToJiDpm1_5tSMcfkl5p4GGunuN7jP8H5X67E0wjicOuu1Q9WROnUyYT0Xkqgk3ZLwYGCWGlC419k_eCOt3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrHdMturmPsCzpsBARFkMHMzVVpSswuxYLYWGnHdWSSxzXccRA7VtlmcIdZ3KuXTG1oRRIhZqo_zRHy13u16RT4g1wC5AQT9k0qAC6vIpkYAPPxyKIn8kwawuwijgn9stsC0kFjDnAtfkgoL4wqx1ocpPhuk5BCjJBzXHka3Fc8Wl6iFSEWuXEl4X859936cXxcTfzQcmYJ-iNyKCu-0RwCfDj9n5gkO9zi_gSPmDgmhrS9CHKYTgKjWApa19wn1LZgr1zpyRMoP3TDeCklXKUQcKOzT5nwuA1nfgHSe_xZZJqfktNkYSJmtPVmFUhMlVxXfsfsjjGm15itQWF2wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUfe-qIeKhaAM5BVUfgUmblCPt6IO1iDqGjd5lO4bd5CX97ru2oAv88KMq9j7rCWc6-4N9_MAPwsAwSD-RjJnvZ8iZ-NtaifABdUbX8XHmR5jLdSgQh17wab3XKYpozItzu7WQBQfLbuntmWp2RD1FzFdqTrRf2GerLXeuPI9XQGqgVNKg0ZviN7pOYiVj0HUrnTBssYIspzypLdSDALlN3Vrd2lC-dre67CiNRvP_qsDMLWf3oJK6ZO1CkG75ChLaPqM0J-KfY_yttXAT6URgjo42f6C_h60o8mdaJUfakeBoV5S0KbyB1Y8FTeY6-uiuaLmbJaihAf_mhTfDUi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxq4n94Meu1eha4sjqPCADLy9Lmy9Yt_LvNZRu65leaIi5LFGL6W3lprcz_V-I8gPb8w6GMosvFU4xXJm2UFmj7BflXhGxASSPzqpadGjJX2Zxkk_gGOJ17Hzkw3TKRhIa0oUDPnVzsl0JUhBq6namB67QQDgSh2OZKSMkbbdpMNe0QElBDSHOlj_K-Es6Z2wUcOdlb9QYmwu4qIflQfHDk9i7Iex-96_F4fkA0sK6q-3OAZjYOUDq8EHkazYkNryCmlFKGhWIhbZfAJYdlV7EgSGJvSpQiCgIp5-2Wg36VHcygUusgjhwR0VZd7G8vWmNazx-X8Zu6j41afO1l2lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=iu8iZLwkQFllGeXoNx--aGpHDUGjbyGeJCMYGIdk4FJLPnIa2wLQe-tcde4nsjc_B-5NsNQYz-FvHBBdPldH21OwpHIfdu024R8h3Lx4DmjHbEQ_86HXcReqpHWRPzogE7oO_gT4CPmO7JRl0sV4qVdhARd2AVH5d42ythryrDPnX0XUYQ41F0O4O1lxfUk9XdwT7j_U9xcQ3vujgDvosX1uOIGHhHOHo7_buBNkArLkHaI5KwRBexLcJBfFKFvIlo4wqFNcWIGfm0zv7OH0_HRVKmnUKRO5SX_0xFznMPgYVkthBefkOLPL75VryEGC7GO_dQodhRDONDKbCXDWIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=iu8iZLwkQFllGeXoNx--aGpHDUGjbyGeJCMYGIdk4FJLPnIa2wLQe-tcde4nsjc_B-5NsNQYz-FvHBBdPldH21OwpHIfdu024R8h3Lx4DmjHbEQ_86HXcReqpHWRPzogE7oO_gT4CPmO7JRl0sV4qVdhARd2AVH5d42ythryrDPnX0XUYQ41F0O4O1lxfUk9XdwT7j_U9xcQ3vujgDvosX1uOIGHhHOHo7_buBNkArLkHaI5KwRBexLcJBfFKFvIlo4wqFNcWIGfm0zv7OH0_HRVKmnUKRO5SX_0xFznMPgYVkthBefkOLPL75VryEGC7GO_dQodhRDONDKbCXDWIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oydc48TDUJzf6-w5qAAlQxPcGrXonTi6eHziMGChj9O59zNtywih5uVzfzjfbLt2KuuGguCxSIFWdbUoyuAbPUIae00I6ZTo3Vgu1PpKzFshNuDOwuwPmrS0tavBcAza_SrcgKXUseqXxSBbUBDDxBxm2hfDZIgy9j3SrH-tkYN-IbA8ozV1niq285qlEcqbOh0f8fqrGvpFLFuqsqjmEwBZWVCLNoyXmHUVq4D5dW79QPwa_QcXqa1MYolIoKQVs1uhZnLt6JlGCnDzxTvTYxOTR5oRWlfGI4gYbrPTZHO2WBzTEMVH2ovgcKndLbXsA72vuegKgeOWYKH9A8jvDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poWF3ihvFj57dp1XScpYapvycm4gKJ868TsmhAtgwDA2UJga_hqBU546s_02EIFiBs3CeWm5VmCiYw5cVY5UHXbiP1UdYBwmApYY97l55SOl_4U1seCATJLCfSNinW4ZDyvZDB0dA5E6IP329xRh6N2_khnIGUXRSMi7VWoQ6Y71P-hcp7BL9_c_cB7_QFEhU84D3zGpjuh3BSg6l6SnzLRGkSpUfCTDPtTooODHUghmWZDVarM9AXA5sfXCRsi5yTrFtSTvnvvoSRbpV0i8oHcjTwEUzUbTcnLAQXFd7XH5UQqdSO7YiR4Ag_TbevHXfXAibLEMMFxPjd0HVoeNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
