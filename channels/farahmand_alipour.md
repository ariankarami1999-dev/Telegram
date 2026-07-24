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
<img src="https://cdn4.telesco.pe/file/oG5WN3DumIyYO2OzQsTg9uzPIveG2NN82nUPehypSDe7gISpQSNe3TuJ76BFTHNb7fKwnhcGlw1QJw48of9NQwERO1rGMMp98FuSPE_81nYlcC2FNfdVeS9CsILDNgyQ-vSw0wfvyWKbqcLWdM3CwxUlrwoRwlj11rj2vGVmSY3CC2As58x5rNo8w-M5MdtvKu4yfXPA69bllcSne9ds6eZ4qh0dj0lK2_F_DgKDiROuYvwmw1Igg3FAQDXKUj6a6-W_tH2DiKsHaLL0sitllotWzymx4U2Ga4hnON2gw12qYUoJPMkyLiwqvfI56RJqDccqVQlgOOiqLyELySSt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 08:43:31</div>
<hr>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=YyfB1BxdxwYTvWWAQsWmNcfDtjEVd1cdIIvljNlTGaqZy2kuXXRLymzxY-h8PFb4vjUiLx26otYTsaTTQ0DXJmUYGV188zIKh6_iXaQhIHbmAme8ZFt88tT7iUIpSuvzh6IMmjovdZBt79-t3JLiBU-TDPemCCaItQ6wAeKk0xlIXbl60AfFcYulZpIL78of4MiNXxhUike7w5hG_cCmkqvksp6Hm6Ql1X-fjg_7RivbEkpXC2adLwck0eRhl0qW-l9ydALb-xt3srlrkR5zRexqYMWqfS4Gu4GZnZQLsmKGS4VPatYvx3I3EgwqKYjeN4cqjrSWKSOT33YqDf427Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=YyfB1BxdxwYTvWWAQsWmNcfDtjEVd1cdIIvljNlTGaqZy2kuXXRLymzxY-h8PFb4vjUiLx26otYTsaTTQ0DXJmUYGV188zIKh6_iXaQhIHbmAme8ZFt88tT7iUIpSuvzh6IMmjovdZBt79-t3JLiBU-TDPemCCaItQ6wAeKk0xlIXbl60AfFcYulZpIL78of4MiNXxhUike7w5hG_cCmkqvksp6Hm6Ql1X-fjg_7RivbEkpXC2adLwck0eRhl0qW-l9ydALb-xt3srlrkR5zRexqYMWqfS4Gu4GZnZQLsmKGS4VPatYvx3I3EgwqKYjeN4cqjrSWKSOT33YqDf427Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgUt_qdKOzEwfnChLmAwdMcVnVxbr0vnnUZ4_fjEuuc7KieRrF3SrrENxb2bQPx73SJpMgHXz39ZlDwQZg3sctjRmVLd1Npv4Toe4mFXfOfKqYTLvR5TTI7PcqnavafrfILV67NsQw2AfCOLdtZXxsJJAShk6SG7uP8nt8ssxlzvFwTRdvx7BT62P_B8r3gdRUxCwry49T0fCFnwYvbdMjq9jj9URSKQBiQDQ1yhq6r3FUYp458xncQH9LRNDxiAAfGJ_zMBRYRgTnIQIZxdyLTYwsFgkFODuLPwxP4J4LQOPULGDRYvKlGsld8Be7E1tkqgufucBADMjwk-Yj9-bpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgUt_qdKOzEwfnChLmAwdMcVnVxbr0vnnUZ4_fjEuuc7KieRrF3SrrENxb2bQPx73SJpMgHXz39ZlDwQZg3sctjRmVLd1Npv4Toe4mFXfOfKqYTLvR5TTI7PcqnavafrfILV67NsQw2AfCOLdtZXxsJJAShk6SG7uP8nt8ssxlzvFwTRdvx7BT62P_B8r3gdRUxCwry49T0fCFnwYvbdMjq9jj9URSKQBiQDQ1yhq6r3FUYp458xncQH9LRNDxiAAfGJ_zMBRYRgTnIQIZxdyLTYwsFgkFODuLPwxP4J4LQOPULGDRYvKlGsld8Be7E1tkqgufucBADMjwk-Yj9-bpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4e6B8cLTHOFZLC_QYWCJylwSJy9W0ogC1kkRdY6btQuH9H8CxCgaa_B10O5ewXYUxmKpJiOTN0Ok1jOwJzi0kgotaQ_2jf9b_Y5lklIwH1mMX9jIZqCs-epIINGw6Yx4PIe39KvGuERRpop0rMJzGtI_xUPz0gFzFQcBAm60EllibNy4qfoms-3jmaAXpr3mODgfU-TkPoqkbeC_wKoaxzAUUJpquRW9VB3eEMGor6OxrZmO2GWGGsilZJVFP8KpTQ60nU37QY7iTkzNHw0mzJ925GZBZ8_gLXhUxvi0Rb0kUsZY6BSvIAEyxdJzyaFGbTkYYq8rukWUxmT8i05hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keSpQgncHjfmhqCX6qpAZ4A9VjB9ySuJMYVgBycn7zFJA2BmcGlrNoGTIdZuj2aBoZXbwefb7qSaehyPAD_UzvyOb6vohFGf-Fr6xGavOU1Bf2oJccItFnnO0omJCsLoYxo1zMUmmSqUVZ5y18NFcTCMU-ZJT8cmrLDhbRmMEVsk0d3fLlqUligvfGoMwquIzHfhGlOIimp_N7EiVhn_u9U4KXs59XU4fVoSYTwTMrXnPfBQ2iJdrOl7-Plkix2r5oEM_N_zmieYWH13zvejD5KWiUEw3gPuV3MoVBRi_6ULRRGEc0U41m6vzujoo9QH7xa0H-qnsFnD2C53SfjNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjX8xrLSUc6BcsHQe-m1nHeFCL8tPZ5K8poigeSQhR1Iq_Blb6UEoz4635zFg4hlwgIa7O1j0_BR10Do12PZI-xcmXgPxj0YNm1ESIhy5lJbgCM31V0lgeA1r19J4Cu0yfThSq3hBz6CwFNhquFnMPJCEiIlHfITOJl5ZXUJwFZbpgF1KDwjB18d9RIld_KBP-XvjHPRSJ0wC3S-SgPmLQ5QgyQT7Fr2Bn2c1pRxgXI1dMfhar8Teogp9TnqGEwV7169C9fclN2A4KBecimGHYtgAQuuqcPynyB9dc2gtVisyEA_ofOhmnXKjbHQWjFRLD03h7FOD6lnjisdfAnFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=PP8VmMHsG9fxKgCLnxi88Pe8jLeH3NVH6Y86MEMVQSVQUDwOpEjOVFmCRzbuxfB3QfDrhpy_1FNiQGqJ9_ITz3QAA1X6UvcggQOMyZ9m0pOyuY6IFGfEeD-gsjaBdKukLHmAI6LmJyX9TA3NMK8sxEktuoomShzWz_du74BEORSSHibkphzrbrq6I-wSP_yT4XYBLx39fyXIW2wpEkCl9hjJcSEgR9Mp33m6n_W9AVIa8fv2rYVRUF9LQS7GrgO5thUwkxq9J1ao7ydzI24G0yTx07QsX5llu9y-n-LJDacrl2NtTOqxHEebQNg-EbHlGvmSL8KipiFS9hSHGKgkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=PP8VmMHsG9fxKgCLnxi88Pe8jLeH3NVH6Y86MEMVQSVQUDwOpEjOVFmCRzbuxfB3QfDrhpy_1FNiQGqJ9_ITz3QAA1X6UvcggQOMyZ9m0pOyuY6IFGfEeD-gsjaBdKukLHmAI6LmJyX9TA3NMK8sxEktuoomShzWz_du74BEORSSHibkphzrbrq6I-wSP_yT4XYBLx39fyXIW2wpEkCl9hjJcSEgR9Mp33m6n_W9AVIa8fv2rYVRUF9LQS7GrgO5thUwkxq9J1ao7ydzI24G0yTx07QsX5llu9y-n-LJDacrl2NtTOqxHEebQNg-EbHlGvmSL8KipiFS9hSHGKgkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHA4llW-TxOQnULV04EQKz4HoQD9Sh7MJMapN8ufI3rFnFhN-rIlodt46pWFs6lskoPQ6PSGLpDHpkGSERTHs1qOCQFOYOpUfF_YM_0Bob8VPMWy5A6758CNsEEbL87hQI-rFpqIvmR2Gn8mdjKeX93To5HiBA4TyvPZAu79ItfuuAfqsQyqhA7mnkqI0GFtr3adxFwIxD6emaTYdsg3OlQteXu51uoZFRgdJWyZrJ1yhx2DQj5dEV1Z3fu4f3lABr7DJ69KxxwoYCFggN0E0p8iO9vy0IHjr3I3lrkvJL1foaDgXb-lFyQ0Pi7X1N9P8tzWmU9AyK0yY3VIvDvWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGevfE6-l3x5M5w-cy7CU8TxGLAQMzzlr2xgsBkBEOfh71AYa1kCZS-up5Gj9123UZVuPHxtU93V3vUY363A02q2hiM8VvpUMaZl549jvxE6hct0Po2SZWmu6GEPH51-X1KtXHduu8542YpOshBIY_I7WGEhI3DWCCOZ17j9-2w3Z4mej7FIt1K5ptQWmjHvDSy4BVCqbx22tF2b05tvIzv5TzP8BJ5ufJ5PeYPDFjTY0_9UBsDiI56tDibxHMavUI3Y-paTi1aH1B9OvyxZ5AIemDPi_Z7CqLdCn6UylAc5llRxspKS0CnWv2McMs8FBcFttZzPfyIwRdbn7WSgOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANxrTMw3OZoAS2X_woEQCVZJDurkyHpFamcWvK4t_23jbkoG1WViSosshP9LyPLlrRKAJT8L-uUnbkcu7QchysqYJA0AxLno2ldXvdNmh-Hw342kSxMn-Xk2tP92310lbuKXNOq1MM1W5duoT9_qG3QJ6ZVgFoY6bWMRD3cCl5dr8LV12e6Re0YW9EWHB6ZUWADHmMExS80uAPhOgfFcBmH4jABg1DIw1Je3tDwR3Ybpi51nXmjcPL0LvqlHGk3c3MidnqlPiTuE4UAIb1SrZGCS7OONjd1nGvwIleSTI7-FJKEzWtZeYQsGZgRwBP0WLnzc-qTotRZahZWTyGeABw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESTMrqTQLs293uQ-qpIQXv57SeXHvL-8tkaTB8Z8x_RGejHC-T2ltcqx-Fx62E4AMrrwHL1ZApMg5kUeVyYVMyz_AqzVHm2zZNZ2YQyXDfkjI-ojWtSGsj5CRMfY6G52a1m-6WGDCm-tTW9gih532-7mh0ZFq9UUSjFTwDDrFVXChBpeyKGfM8O-5ph_vx5EiSlCqKhQ0Xj09uOFYY0qJLVZ4Z94x6-wHGq8AWhmSZB1dQZp11uXk_M6GMPxt4PxF7JDH1WeF1aiObeA3tgheMtQcESrCuUzcIZqswiEKkCRv69RBYxDy5Z22DtDr_EL6SzbG5jbFF3I8N2DV-q_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=SkPj5BY6EeZ50ZFDoc9sUN2byEFBisGxSitoJxadOyIAcKHzhCU74VGGI8ixKv8kI3IBL7WfxS-a5VYZd8ANCVGCgo-8rKpP7_RGE67DrOx794brvD2gOIkU8ivxB_yhekb0l5nj5yb_87f-fQ1_BOgfvTQcNeVuWZN9aeTbG1TQ5ilkKtcuMuquupZ_eBZBQUSq2UuP-AS9mAaroHu6iEcWHqA8EpxQhwlGrI9u7mLwnlBIJxNSX5fR0I8kj5MrMX90dBPn-J2nLJpI-hn4TSGsMDBq_ENv0_KssnjUCVCNkcO6V9IWZL9ZUHQkGIvwxOqC5hdZVjHjffGuYM5ecDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=SkPj5BY6EeZ50ZFDoc9sUN2byEFBisGxSitoJxadOyIAcKHzhCU74VGGI8ixKv8kI3IBL7WfxS-a5VYZd8ANCVGCgo-8rKpP7_RGE67DrOx794brvD2gOIkU8ivxB_yhekb0l5nj5yb_87f-fQ1_BOgfvTQcNeVuWZN9aeTbG1TQ5ilkKtcuMuquupZ_eBZBQUSq2UuP-AS9mAaroHu6iEcWHqA8EpxQhwlGrI9u7mLwnlBIJxNSX5fR0I8kj5MrMX90dBPn-J2nLJpI-hn4TSGsMDBq_ENv0_KssnjUCVCNkcO6V9IWZL9ZUHQkGIvwxOqC5hdZVjHjffGuYM5ecDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=E4e3w75Pj67TydO7H5EmoYj7KAHYMN_uuBxdej4trL3GkJ4N6YoxTIL00AhZeU2FccKYROhgI8PaBl990-VVHogB4Wm0CQenkKQ8E0SFn7hPbFWdc8vKLlvxEgbnnmDwyZx3E3TWTQHX4bMxJe0R6uSoTtsmRdMO5MbUt7nhcVDQLI0tVS_rzKwP4aJ_O6g7QAWurJsgqCB5Lz2OXb8Ln9ecIU1RS-H3FP_JWH8fer_jTUoxwOl7Qhlb0HshNVlPbXsLSPa3tT_Z6a93VYBkfhBmg9HCLlByCFaGdyaNw3NW0Jh525Xf7ZsnCYsmJLoxj6s0EHrDX4eSeEqErGuKmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=E4e3w75Pj67TydO7H5EmoYj7KAHYMN_uuBxdej4trL3GkJ4N6YoxTIL00AhZeU2FccKYROhgI8PaBl990-VVHogB4Wm0CQenkKQ8E0SFn7hPbFWdc8vKLlvxEgbnnmDwyZx3E3TWTQHX4bMxJe0R6uSoTtsmRdMO5MbUt7nhcVDQLI0tVS_rzKwP4aJ_O6g7QAWurJsgqCB5Lz2OXb8Ln9ecIU1RS-H3FP_JWH8fer_jTUoxwOl7Qhlb0HshNVlPbXsLSPa3tT_Z6a93VYBkfhBmg9HCLlByCFaGdyaNw3NW0Jh525Xf7ZsnCYsmJLoxj6s0EHrDX4eSeEqErGuKmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=JwUaRP1F9cjSijhfFz_K7AfK6Wv8x7i9qKXGv6uJImKJRlPMLSrtLhN1oH6qNkTLAWj1zLFwCqumanMLisuKc96CmurzG98tO4mtZzgKwKBjkWkdaO_cAPPvvxljwYMOleUE8K8o63psfBDbumnKajTdOBCiR63FgQf1vZOT0EyZADuABowsQdTjgkP9abqGGRsQx3WtHeBYBBSpBbFKUn-b7kI-Yld4Ne2bDPotS5xShqnXrTmutnVmda23e3sLMWsqihQ1RVCmbPEz_AN1D1BDsqmAzOsu_xFQBWdEID5-rc50ccRUj3aiHEDMUr9Pct34pOleN2c1D7o9tR4dHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=JwUaRP1F9cjSijhfFz_K7AfK6Wv8x7i9qKXGv6uJImKJRlPMLSrtLhN1oH6qNkTLAWj1zLFwCqumanMLisuKc96CmurzG98tO4mtZzgKwKBjkWkdaO_cAPPvvxljwYMOleUE8K8o63psfBDbumnKajTdOBCiR63FgQf1vZOT0EyZADuABowsQdTjgkP9abqGGRsQx3WtHeBYBBSpBbFKUn-b7kI-Yld4Ne2bDPotS5xShqnXrTmutnVmda23e3sLMWsqihQ1RVCmbPEz_AN1D1BDsqmAzOsu_xFQBWdEID5-rc50ccRUj3aiHEDMUr9Pct34pOleN2c1D7o9tR4dHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvE6Kl9FEM14OnGJDoyxL_8EE3_Qhl6PKOFbtYnZ-yQb0ZYMge-Deva2LFOmyUzkXnqM-qcEGcWHA47Jvn3bkUSXlnL0Lt2gj5cRB1Jby3i_k34PZefWGbQJ_YDFeFaTnoRIkRBfdN8w8vBV5zY-295tFICxztPmkUIBDQqqOvBrJqQbZFu3-PZoLC_WxMudcYjXwZquUfeI1a2c9II11wSrfaRl5Z9YmSUys3Tq03QzPHLGH8Sg4hNktLMj2ZWTyaZV2_shajF7C0NA_hd5eeLJsiwBgDSpSA6Fcac0bYTMCrdJnA8kuvCHqlwqZQ0AiBIp-aX46t7d9ChX-_hCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h0foODxro6uCCMVnrQqI3RPcwT4N0B22a4_8GMWFp609Q8-yo8E-EIL44A98FEV82WczR22EbZ6qy8smKHsfjhcSAsxPNpexxQf0nHBUbM2Azsqu_7svqRyjMHBCOXJsBvr2Tvg_fh9NGKL9mysvoCeJR24z2i-R7rj6fNE4_FqEeXpBUI_NQ1Q52vzgBo8wBpOFm8zcLoIL_1QlNDpgrFRT9VIMbhuGEFB7Socf3AtjBO5Lio_CLZD1l92xxT-ERxWgswlkk0DajySwtMOIKY2YvZ-VVRomml9pefvc7bMYirZbVeaHlIqcIE0brAbr2ULZLOqZ3OldOHdLUJtVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h0foODxro6uCCMVnrQqI3RPcwT4N0B22a4_8GMWFp609Q8-yo8E-EIL44A98FEV82WczR22EbZ6qy8smKHsfjhcSAsxPNpexxQf0nHBUbM2Azsqu_7svqRyjMHBCOXJsBvr2Tvg_fh9NGKL9mysvoCeJR24z2i-R7rj6fNE4_FqEeXpBUI_NQ1Q52vzgBo8wBpOFm8zcLoIL_1QlNDpgrFRT9VIMbhuGEFB7Socf3AtjBO5Lio_CLZD1l92xxT-ERxWgswlkk0DajySwtMOIKY2YvZ-VVRomml9pefvc7bMYirZbVeaHlIqcIE0brAbr2ULZLOqZ3OldOHdLUJtVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JmwY0QSip_pyUZnKB46H8Tkv-AmI4O9c4IAPM216ZLhcQyaenGkAJhRMSRwRHkoZaURtPN1RNIxMqCLuw9C0BQwaMlmBkgNn7lrVXslG8n2XhFrjLsF-H2U-lCWOTLIqxFf-WAQCC9S8cbe14sPXPJzqJrHoTN6VB8_bDObHOxxn0pfSOYxt9qwYbzKjMHOkIC5DlxjIoZVJ5Mip1r3HxjCphLH1UVdGRzr-ZNBM2AbyUiLcZs2vZ7TDUMWNSi-CO-Kcj_Aq6gq3v_WURl4Pax1j-rTnNbhGSDkM0lHvRfEqfOfvtdJwRwo5fikxi7VxVe6l0ZzbHvm7DoXazP98xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JmwY0QSip_pyUZnKB46H8Tkv-AmI4O9c4IAPM216ZLhcQyaenGkAJhRMSRwRHkoZaURtPN1RNIxMqCLuw9C0BQwaMlmBkgNn7lrVXslG8n2XhFrjLsF-H2U-lCWOTLIqxFf-WAQCC9S8cbe14sPXPJzqJrHoTN6VB8_bDObHOxxn0pfSOYxt9qwYbzKjMHOkIC5DlxjIoZVJ5Mip1r3HxjCphLH1UVdGRzr-ZNBM2AbyUiLcZs2vZ7TDUMWNSi-CO-Kcj_Aq6gq3v_WURl4Pax1j-rTnNbhGSDkM0lHvRfEqfOfvtdJwRwo5fikxi7VxVe6l0ZzbHvm7DoXazP98xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OdT-CLYeBwVgbdBc2IaWaK2dB1F7PSItssubgsQE1P1z02X5YQ6Fke1gyW6CtKJlZIVBYPb5_LDCz0hRY4z9ZwfeEth11vVDqVlyx_OevJKjBNmAivDJJwfkcEgIihmBvFTX0ZKKXmQnI6UyKQqyW2_cIP9iSxfc7c1ojx5rfZsJcqbphgAvdCb57HreJtNJvMLr7qfIkicOwhM1cBuNoADXY8tQz_hQDRE7qD72IlAmPd86y2bYqSWOFGG-d9TRSuqTKwFxt_hFvAMYfqT90lJJA3zpFLzHPpb9DvZWqYqovw1PDanBQXkR6ITaf5Q4oJ9mMjXrLGyMHyM8bib7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OdT-CLYeBwVgbdBc2IaWaK2dB1F7PSItssubgsQE1P1z02X5YQ6Fke1gyW6CtKJlZIVBYPb5_LDCz0hRY4z9ZwfeEth11vVDqVlyx_OevJKjBNmAivDJJwfkcEgIihmBvFTX0ZKKXmQnI6UyKQqyW2_cIP9iSxfc7c1ojx5rfZsJcqbphgAvdCb57HreJtNJvMLr7qfIkicOwhM1cBuNoADXY8tQz_hQDRE7qD72IlAmPd86y2bYqSWOFGG-d9TRSuqTKwFxt_hFvAMYfqT90lJJA3zpFLzHPpb9DvZWqYqovw1PDanBQXkR6ITaf5Q4oJ9mMjXrLGyMHyM8bib7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=drfCGdzQ9Xxwx4uPChMf1DI3eCxgiCJkM1M5eAw_lANJjWsshX-m__RxATmcmxH2Z2o9FzREvnJ3DmEWpscQV75Ew1kRZHJbCcPjQstct3GOHGPahh45_JK3IJLJu-Vw_WEnJlWVyTzUwm_bLPjsZbsdZaIGKsjNp5VJwI8Y9i7BdHPPTQPp6_zVQySJHowr8TshVjNx_Nkhib3RhTc8GgfJNfqwmZsc7sdzSKpeG6suCXtxL9mVEGxCHPQ0yABjn-9eHACA678D_ZaORgmX9WnAb6vKWX-DOmY9k_wBfHS9exkj9EsR4qru1jHruNEvdcGj0u6y_0EDANbUskG-PUZzzmEam0acKj0FFH-ntEXXaMUB0mbLVIOm-K7tE5MaroExL_ZahQRlYKxOmReCYVsmi_ZrXaA-D-uhQUaGcgItVMOqq-reBQnA739NAFaVBHoD_Wu5Y4GIQwGPZCCJP3ngl65938bbOqSJ0HkO9dKVmlxnPRZnkWfFHhc5v418bEtNWmyU4SzUQksdn9YFkl_5IWbgM4O5jqdCqpjM0-h1skJQpXCSquPJR64qfj79rpRqjMXWTlviRGC9Vg5HvrMmwDzksZOAoMc5j5JqhXdJwjks5Qpf0DJXPwp3Sj3zfyln_dNdqRJv3iABwtuVPkJExgmD3z7evF0LaQaRjs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=drfCGdzQ9Xxwx4uPChMf1DI3eCxgiCJkM1M5eAw_lANJjWsshX-m__RxATmcmxH2Z2o9FzREvnJ3DmEWpscQV75Ew1kRZHJbCcPjQstct3GOHGPahh45_JK3IJLJu-Vw_WEnJlWVyTzUwm_bLPjsZbsdZaIGKsjNp5VJwI8Y9i7BdHPPTQPp6_zVQySJHowr8TshVjNx_Nkhib3RhTc8GgfJNfqwmZsc7sdzSKpeG6suCXtxL9mVEGxCHPQ0yABjn-9eHACA678D_ZaORgmX9WnAb6vKWX-DOmY9k_wBfHS9exkj9EsR4qru1jHruNEvdcGj0u6y_0EDANbUskG-PUZzzmEam0acKj0FFH-ntEXXaMUB0mbLVIOm-K7tE5MaroExL_ZahQRlYKxOmReCYVsmi_ZrXaA-D-uhQUaGcgItVMOqq-reBQnA739NAFaVBHoD_Wu5Y4GIQwGPZCCJP3ngl65938bbOqSJ0HkO9dKVmlxnPRZnkWfFHhc5v418bEtNWmyU4SzUQksdn9YFkl_5IWbgM4O5jqdCqpjM0-h1skJQpXCSquPJR64qfj79rpRqjMXWTlviRGC9Vg5HvrMmwDzksZOAoMc5j5JqhXdJwjks5Qpf0DJXPwp3Sj3zfyln_dNdqRJv3iABwtuVPkJExgmD3z7evF0LaQaRjs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jSKRQL_WvyPntT-eyXdd7kJEeyva9Mab4esS9lWjPrQeFtG2HRb_oj7X1zT8lmj6cDoO7I1e0sOcb5ybUPCEM9C6pPkrsbYEu9A4GbhtRMFSfboetRcsxeRcQWlw17-WtZdGBblF8IFPY5qEha1AYYW3TcQeKwmZB5R8MhuG_uXE7lFF7oBHvmPzkDt5y1qzoJkFm2YYpeQ-9OkuO4jd75yqRtOw6foltY1Hzyw8XgPlc0_rlap8xhVtUbwAgVTVUHQnmkbnLVzbZg-MeH8lfnfaDN2CbCrNznQ-RbYIPtcRe0RKeVTnFjteAuvM6Nxg2m1Xna_epwmhf0rK32dGuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jSKRQL_WvyPntT-eyXdd7kJEeyva9Mab4esS9lWjPrQeFtG2HRb_oj7X1zT8lmj6cDoO7I1e0sOcb5ybUPCEM9C6pPkrsbYEu9A4GbhtRMFSfboetRcsxeRcQWlw17-WtZdGBblF8IFPY5qEha1AYYW3TcQeKwmZB5R8MhuG_uXE7lFF7oBHvmPzkDt5y1qzoJkFm2YYpeQ-9OkuO4jd75yqRtOw6foltY1Hzyw8XgPlc0_rlap8xhVtUbwAgVTVUHQnmkbnLVzbZg-MeH8lfnfaDN2CbCrNznQ-RbYIPtcRe0RKeVTnFjteAuvM6Nxg2m1Xna_epwmhf0rK32dGuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=B6u7bEFU4YZ84LPiVL8MuTgH9B-8ElwrdEXx4XXrLpJ5VSHrDKZFUn8VJIJVjPQHhVCPp8zBcbn7RGC3z-g3l-FWHsdiKDZMJJl4yAFmGAwlFzLaNw8mtQZYVzdhXtTTyFhpD0cBW2A3KqK1NBj7MP15R-UgaA9dZqNGoZ5f_7ePeOkrSmumBqqugLrSFU_MUi9kPKFZL7hnbnLSvv5SoU9MfqjErQumzSOibfpXICw2u-YoOKONtwA196TAiSo6SDZNY1DFhpmF5S4R5QEcEP13XsPdcObjceRcGSk5S-FywI13lodSDlnhlux0I2tMS3XDAWvvpfFVURzBlu-E0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=B6u7bEFU4YZ84LPiVL8MuTgH9B-8ElwrdEXx4XXrLpJ5VSHrDKZFUn8VJIJVjPQHhVCPp8zBcbn7RGC3z-g3l-FWHsdiKDZMJJl4yAFmGAwlFzLaNw8mtQZYVzdhXtTTyFhpD0cBW2A3KqK1NBj7MP15R-UgaA9dZqNGoZ5f_7ePeOkrSmumBqqugLrSFU_MUi9kPKFZL7hnbnLSvv5SoU9MfqjErQumzSOibfpXICw2u-YoOKONtwA196TAiSo6SDZNY1DFhpmF5S4R5QEcEP13XsPdcObjceRcGSk5S-FywI13lodSDlnhlux0I2tMS3XDAWvvpfFVURzBlu-E0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stvbk4w3g8Ix0Xw8UNunz8PVNOynL0WXfDlNyaQT3GvMPipgNASlCj4CB9LjtYKKZt2D0LACch5N5uyntpKXvAMF-MTtia_8XnYNjJNj8FpMwn4qw_AgA0b3MW9eJSamJzPf2KI1wik_Su7kAaAwZytPsduMHMPCykQmQmZgN6N-O-dYv2qarjdd8KIL2ZK-QGXs_skbrVRLWfMhaC9yO4HUaIv8zVu5WjXGt5Gr0b6f2_mDAkWm0aI7S_LuTEPPChjEaTmAp3ndfKjmGqQfTKNWEJr2pfV1pFh8xJX0Dg72Vti-X1pbEQGAM_i5J4qnLhTpfyWHDDtEkNSbSJNKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7iqvjZUvB2a4Iw5KIivVTo3g4nIjmAEGQvXXxmb8YNeNaoV7mT9f46tFZU7kMQyS827NIfAF5Zi0fokuNSdTA6bDmIal35JvqE4_bAkosmP0ZPfr9j2QhsL4y1ovO7JSABF5dXW83OVOOOOk_gAdJle-dAWQgk1YthIV1s8besCtStOQ_KTaUknN-VdiJIaeiLa21udUoEHCGDbI-8gcSFuwV-EYCbQptC7umh0a7wW1AcwQ6UEcrMTmIUhPha3ft9SHzUZPJ01w-__31OWlgywtGZeDEXUO5DT2AHil7lAuihsDa9X8DmwiIQjZfNwoY3LBRK6FjSR3yGuv-gidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=mbZeIhVgT22wGgMKJIa2P1s7ScPNagNUStP5bvkSW_Irhb3RnwTTUMwmEGyE1lgfh3DH-45jZpVsnTkAZ1c2GVoOUGudx5OlYpzN2bG3tISpc2BsXXFEkg9hJ5hnVSpRc9grLHWNw3sc-XF2KiHlb33aE6-IHxWMq4LXaT8QQ97VpFbb4WrR6CLx1fcYre554EfYx073AeZnNev4oRJTVF2I5t5SVedOHZkFZsb6T8oQNbBvaaaG5l9T9ZthGyj_Tfhai1ohrlVwYbJw3CfAQHH6WvHpiDA2aBP5AFHqW-sGCCshBg4or49q9m7M-GwPyAaTKYz0vrMX0g0Nn0UdcraJko1cD_L0HWFbX9px3uW1Zxizyrv-OCdgM2UHtFJvK3p3VzHiUxTdYXnYQcYC7yjSxTvJ5PR4n2VmMKlgTNXA9QIxyW0lZ72kllJ0Sx3Ph7DO0t9-Fw0VMJe-SsgqSGlLx2vwemuyR3nGF7VDC11ov8sjeLdI5b8d0kNlg_2ImSV9F656V7jgMEE18MiLh2fp6D4NRS0hYWRTIODIh5nacduPkSk74L8e1jHCbJkKw51VpYl4e54fWNR3l8QdsgC4DlEaZUv0DX_Rn0IlS-XEIvnRCCrathVghABePwGGnBWkqNzyn9CucLDAoFo7gdvxN251nCj7msWkEe722r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=mbZeIhVgT22wGgMKJIa2P1s7ScPNagNUStP5bvkSW_Irhb3RnwTTUMwmEGyE1lgfh3DH-45jZpVsnTkAZ1c2GVoOUGudx5OlYpzN2bG3tISpc2BsXXFEkg9hJ5hnVSpRc9grLHWNw3sc-XF2KiHlb33aE6-IHxWMq4LXaT8QQ97VpFbb4WrR6CLx1fcYre554EfYx073AeZnNev4oRJTVF2I5t5SVedOHZkFZsb6T8oQNbBvaaaG5l9T9ZthGyj_Tfhai1ohrlVwYbJw3CfAQHH6WvHpiDA2aBP5AFHqW-sGCCshBg4or49q9m7M-GwPyAaTKYz0vrMX0g0Nn0UdcraJko1cD_L0HWFbX9px3uW1Zxizyrv-OCdgM2UHtFJvK3p3VzHiUxTdYXnYQcYC7yjSxTvJ5PR4n2VmMKlgTNXA9QIxyW0lZ72kllJ0Sx3Ph7DO0t9-Fw0VMJe-SsgqSGlLx2vwemuyR3nGF7VDC11ov8sjeLdI5b8d0kNlg_2ImSV9F656V7jgMEE18MiLh2fp6D4NRS0hYWRTIODIh5nacduPkSk74L8e1jHCbJkKw51VpYl4e54fWNR3l8QdsgC4DlEaZUv0DX_Rn0IlS-XEIvnRCCrathVghABePwGGnBWkqNzyn9CucLDAoFo7gdvxN251nCj7msWkEe722r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzjHS2_Wrpi2cVP9SN8Kiml1aswAY0AVaQ93uSqcE7vpm7I_NMuI2SwvqSFVWAp56O4vjahj_YjMylrwfD1l8iShNt_Ci30agA3PDdzFvZkbwfSnu1NQ44pSQEGjH0pk3o50Hn1fcaY-VfVlOccGDq9J5WdjQROxQKpMtu5oSZRMMUOuzw_SlbMbyhkfaUTOmLFLI65JzLDy6fcdA0kA1jT_WDj5PhYXA733TwsIHn5oxpR0fqDfCxViIAn-e9BxGwDVSjHptn8CQSWIzJNadomjJvUR-qt1QXFyHVPkfZ8CtWL_Y8S-OPVf0bNrz0BomkJLrJWvcfFABL_56Q9KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY7GniX8ELG5ZZpCLbjLwjtxBuiIjsENwMoZSoGNzHlT15KkKjbjW864m2jigYlkjaoOxeSltLCXqQij2OVjA3PMBQdbo_iAEIy4jrS-ESjwuFvLzbEY_JJm6Xp3HUm25uaZrMYPuJN598dj-P8d_1WKuxgwGLxZQXFWF_DgOHysbax6FVeHYO2rqKSG0E_POdxrvpaYAwRaYBRfMfRIK65T_tSzVPx8xeBab-wej_rXYbXMs9_MqKPI_tkOJ_Ocs9uzK2OTCbiHSQoTP9SLjkSI85Ndl9MswctYBGNp_NS3gY0kWIlohUSXa-ymSOkP1Ts8q5Gd_eVhOqczmx2i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXtanNtDJtLvt2VpWzmfZ01_nNK-83Kxy7-O0f9oLetIZmFubDlGryXkhMEKetVodSH7x_y2ib_x4PQYv2Pvuvnov9nYrEk6P7gpsKC4CJF0DZjMirr2_GljZaMaxKcSopxbnAjnIcVOX-cKx97bYRxkqCptBSij0R_AHow2zOI8XH5yt2XypBc7AhmJdf7jaXuPUgUI5bVJ_WBT_YJEVuDvKmb3tXlYml2veFaUPFrBksZFQA5cJ0oGxTU2slyey2KK50XGrWEZpMvimkU9b3BlA9OOlbI7viUZZ9CgFAcMTx1OP7qHsUdVn9iKK_ADn44vNfG7EVcNMBRLk_HmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxXCB3cnXi6kK2bLUPzR6zqt591QuDyWgBIStW9lT5zU8FipOMU_bnxM_Z6B3N6hQaMvm5tQHAH4pVoUkZzjHKlH3zn3JcUJRvKW7AvNp2BfqWj3tb8jbdFC330b3uYy6cUs5m0SvGL2SeS1sTPBtGd8JQUr0CKT-aXDwl7ua7FQc-CByFH9CQMHljUK-voa4SLU8xj9oWAvs3D54oUVX68wbvJ3xGQmvU9lwjxe1VF1avPSedS9vTGpbVJE3b1kM3SRsFatqqqH8kF5Hiy-KMr6P_bhFiVEHLee1keeTMlFRwvR8Iwzi55ocuV1-VMO7EZJkcK1QwjKl0y5GwGqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=cUcpgfy7fOPZA5Zvq5IMt3thbbQd09f-bBfOkhzD4V9PyJVF4ZohoDSN9LJry-kMvsZQKwATYs0jqnOHDtpxdYXLIZCvowbPCq7y4R0TJQVdYzEYhAX496dGsRRw9t3K2ljB-4A6mTRhckFZ4bf1sUXeGzeRn3qKMAu2q6kTRGSMBaLC0JrY1Oi49iEwSdAsq1wGY7wDDoUkhneV0gYAIlz-fG_9ycAaQUA_mlgAMhZ87E9c7sHweapCB-Qo92d-ZP8CzQ_uUgaFSrGdMi6cOWk8DrYr2Rceq6URFTRnLGSYX0-HA3q0QoqJ2xWa38HqSsIgaTblgywVXYY-6AimXUOJ5-qubNx_ZlIz0Pzp0BSOKhNYozIF1hIv-PZFUNDchYjVxNIExbKp-CdkOw6NLbs3UuRwiYKedrMDouttIWngVc9IS0blK1DjTy2x7lS9qwVKSiCSxjiBwf9HWdtzndT5sqZEIA9hGeNjsSN3Usm9-yUUsGIbfWQf7YKLV0QaDupMJbyy0fs9EqsoCHc7LaEEfdQ_GHtrAgwKstLYDsR_Qax5Z2WHlsQCkC7fwvi_rn5e8JGMM0r4etD2o8-BxCb5fEgb0Y2PpwRuXNCf02ejFYxKACHWorjPoj9fK05z7y5UkEn9MbcaVHZuuptPTkafaE-IHBeRGb9Px4ggUfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=cUcpgfy7fOPZA5Zvq5IMt3thbbQd09f-bBfOkhzD4V9PyJVF4ZohoDSN9LJry-kMvsZQKwATYs0jqnOHDtpxdYXLIZCvowbPCq7y4R0TJQVdYzEYhAX496dGsRRw9t3K2ljB-4A6mTRhckFZ4bf1sUXeGzeRn3qKMAu2q6kTRGSMBaLC0JrY1Oi49iEwSdAsq1wGY7wDDoUkhneV0gYAIlz-fG_9ycAaQUA_mlgAMhZ87E9c7sHweapCB-Qo92d-ZP8CzQ_uUgaFSrGdMi6cOWk8DrYr2Rceq6URFTRnLGSYX0-HA3q0QoqJ2xWa38HqSsIgaTblgywVXYY-6AimXUOJ5-qubNx_ZlIz0Pzp0BSOKhNYozIF1hIv-PZFUNDchYjVxNIExbKp-CdkOw6NLbs3UuRwiYKedrMDouttIWngVc9IS0blK1DjTy2x7lS9qwVKSiCSxjiBwf9HWdtzndT5sqZEIA9hGeNjsSN3Usm9-yUUsGIbfWQf7YKLV0QaDupMJbyy0fs9EqsoCHc7LaEEfdQ_GHtrAgwKstLYDsR_Qax5Z2WHlsQCkC7fwvi_rn5e8JGMM0r4etD2o8-BxCb5fEgb0Y2PpwRuXNCf02ejFYxKACHWorjPoj9fK05z7y5UkEn9MbcaVHZuuptPTkafaE-IHBeRGb9Px4ggUfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=WgWzIPRLunCKC8-8RNWcEq0QteZiNO3amFIvS1eMy2RM1TreT3Ama0jAs-BRCnIwbQr3OXoOCiyyvwcvo2PodyeRuPJSHi7Q7LfD3j1HozhhZDuhOPx0CoyDs6qla0syMxuNGvIIH3XqE-ZB4MAgGvPfxMNWp_-pxNLG4GYWWOP5ejFIux1o6qWwLMLJjS4OZSiiNOfenLGN0a2LQfjlI3VBUISqAIpqZs4kfCQqqr0EUgyisxkV_RfGe2uS4fsINHxcJZZl4KvhpO_84WU_CqIa_zxl5lvgZmr40YnDt9NumFiJuorw1F3WHL5Y2_wpdZOjdAlEuVuFBLKdcOr62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=WgWzIPRLunCKC8-8RNWcEq0QteZiNO3amFIvS1eMy2RM1TreT3Ama0jAs-BRCnIwbQr3OXoOCiyyvwcvo2PodyeRuPJSHi7Q7LfD3j1HozhhZDuhOPx0CoyDs6qla0syMxuNGvIIH3XqE-ZB4MAgGvPfxMNWp_-pxNLG4GYWWOP5ejFIux1o6qWwLMLJjS4OZSiiNOfenLGN0a2LQfjlI3VBUISqAIpqZs4kfCQqqr0EUgyisxkV_RfGe2uS4fsINHxcJZZl4KvhpO_84WU_CqIa_zxl5lvgZmr40YnDt9NumFiJuorw1F3WHL5Y2_wpdZOjdAlEuVuFBLKdcOr62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS77uCGY_01iPp6kc9X3F4_XQBTadGGZOFe2TYI1mWkLGvywMheWvvYCndqHwGkE8YNadlUQ1RofOWrIxSnqeEl-55ua2WCGdVCjA17HkuSo2JrVyiF9Tc9vTqVj71qFgiOIbCw54pbN4F_cs9c1RztEAYTD08R-aEzRfNXZbSCphjRZu57r4NN4A9dOGDlW0opWW8oHqEiProTher_Q5FZVaOiuk0T5cR3DgDGQ4tLYsAqR5UlOvXeOcU2k0mFpqVMWGGIyHbohYFzbz-3W79zGf1ytlp_Jj9PJGpgopWtILSUcS71Dx3LQwpNAwOKrGr6DAR_kgCwacDLFWUUXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1TDJs7gC3E38bEGPZqESU5kk-x3s01-KbRGKftas29oHVuXTnDzLqw8lQMYa3ypyTOTd_MyB6tCxLi-nJ5CmVcmHw_CEELkgb_ewvWA535k9U4KEkh32NhoByHYpB0GDsE4WEcb3-ilwOiDhcg0tz7t9YLzEFi1z48gSiC0XxbYBGuHV3GaMQsiH8DmDPQk3WrNFWtNopwl_PJ0kYVekdk26-gzDTGeEf2EO7ldpr2c96wdtyb1opnE3o8Aum4OwKW_vRAzD6DXMkBS4lLfck82SosI89NPRsf2idSBGoGonqKi8GoemSDi1tKay5T3YPAIAJj0lxJiilmu1hX0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5x0d6H5v6xcI01Br5bz0eDxgE3rHDgqH5U2t_xr6xxgep6UKuu-L2V8V9DOsg2kNzQu1reTWv4DApJAY6X4xsf7k_b5kc6c5ncAOJYLs76bCP6rL8lMVPlykJTsXcGzutVIT_Rsgr3ZjRL5wzS0XOy2WmvA3qnuRZwOQO-Px4ILk5Ww3bcf9ORIHXjUdEKMdSh7tiZVVV3nu1B7wOeD4HMdfwCQ3wdHoXq5Xgxc30d7rSdYcTTYsh5t_B3ttfQbx1Y7DEyX_Q_NoEldZ_H23_9fXtGeu4IKxC4iGagEm4V5jBMef3dZnmYK99gW-xtY73b44gMfQdSm_Le3ChMelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQ9hmo-cde5-J3Gs3bQzCUXvqZWts_xLbqyhKRVW8pf4eXCTpeNUelhfyStbF5dejafZjXATC1R2B-HB9BItWazAPQOTqOipZ1BHkgcSyJdvQqenFqvlVOWajyDminrwaHhx5Z_bLwUa80uS5JhLnxgGjTpL2Bmyzu91Vi5xW3wJCj2d8HBhmt25KhmqoEn0e-jFKUkjhkhbwMgCvFfn3sD848WTIKPYmdgYhuQylX8lQ1d8uyYiPnha71Xy1gpuLwEWSFbjoIC5w6GGOYvBo0Ktk4ryFSTg7HN3gRFv-ogwFl_bHknVnKA8R7ImuhnJI5STlUBDZkJiYgzdALtD9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTFu4AicdOuKUec--V7A0hA4chFt5h972qfp-Qyj2x2gfDT3l4umBMBP1YBNwl0b7FmsZUUSRWCI_IN3CnumcxOgdGRInkv6c0QCKsgVF35w9T-aKgHjTgsfYWe3KBb30gI2EEuJtTVdRhWYlR840dyJzFrX_aGdE-YZjShqUeyloFVrCdP1jPVct3UHCk1xCTJ0E_bR54RPwwMR8NUQlzI2bP3pUAeVdXutExi7VoCSS0hc08n2c8i3oLiW1n9rFmen5_FsBXaLz-NwBbSHmMHoHzfq425atAcwsoY3Vo5lP5V0JeYRzf-CAZOrvZC6Z0-tAjd_rfhRfTvG1E8ZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va85a18DB9yifDV6tw7ncRRAJS304xIV_VTLgtQw_bE1xxZmXu6JJBuDP3t1rQaBjFijoG-rpA-u9EaJugdRJAuXL3IcyLB6Dj_3ehLvKQ32F_XkoqBGhDhiEQ3pwwjHHfT06VfjVBXWhV3Rtq57y0ql2LPP0kQvdWQQd0JdXV5ozHxpvfFjfjtgVN1G0uRl5lORkTEZZ1fFiFU8OBMWMMbvQlpCuX1yHMPeye77B0xfOg-BCTiJe36J3tTlgTwhqd5HqBDiOtYRbGlvbeCl4Z2A3fd5vJvgah049N35OVeE8nGBY9Kpob1zVh1qkE6rT-UntJjzvRY8QFgbA1sCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5OOVDqZ1rwQgcqncVEQFZXrzfkEs-8OyOtRGBPSk5Gx8sijJ7ribXNtTX4mszj1j-s5qP33GxaMXcxqj7HPIQQy-LAJf6Hhaq60rBaoM09o1fSRUrSBtlW_AL81xtzG4pBwOqKkkH9GDSewpQIJx74WOlVFpDXrIiqa0tY3cGUqF7H1mmuwDiRZvTt8G1cbgsd7VKO6l3uKdQfT5PEaWnG9onRhWxtX9q90zSdg6IlM-IlzXqmoUxdjRlnh5nr0gv5L2d7KwSkJbx6bI08R6_reGoWhjjVFjOyexO67hHJifX7vXLreRdMWN-U6ya84QOw-zw6WBd8DqtGAivEpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=OHBMrBZ-pOpF3qkH1e5ZBDP3It9uRVCdQK_98bfRsvGwqlixYeXRoMTMMzGEWB6dFanFx1yE5u1O_XhKHN6G-t8xXb1AquFta7fS_VPdIKcHN8hceAb45nwCG1dMQiR-fK6EwEJCohRdq9GzRkTRKnpMG2xTJ_bAPTs7ulQ-S-fn4uVl5sLtNkQSRbB1u0j0TBjTX5AgSLga3H4bT0wFqiP-Kvcqj98UYS9kQqispws68Dls1qR9Vra9J_W7tKWooSYsPEHaDe_ot5UCQ0xFbv38BZkQDikW4ZWZERsQIf8EURmNJnGxXwAB8VVu8oYNAQ0mrwwAgoZwScBfp0pA7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=OHBMrBZ-pOpF3qkH1e5ZBDP3It9uRVCdQK_98bfRsvGwqlixYeXRoMTMMzGEWB6dFanFx1yE5u1O_XhKHN6G-t8xXb1AquFta7fS_VPdIKcHN8hceAb45nwCG1dMQiR-fK6EwEJCohRdq9GzRkTRKnpMG2xTJ_bAPTs7ulQ-S-fn4uVl5sLtNkQSRbB1u0j0TBjTX5AgSLga3H4bT0wFqiP-Kvcqj98UYS9kQqispws68Dls1qR9Vra9J_W7tKWooSYsPEHaDe_ot5UCQ0xFbv38BZkQDikW4ZWZERsQIf8EURmNJnGxXwAB8VVu8oYNAQ0mrwwAgoZwScBfp0pA7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv5TYJLUxzkzoL_lSnS-DO5J4XdQxt43mN9-B93m70ZBlAepPuz7wBh_yrLlqTq5dXV9ZBDszeOM4-8D1oz9-2xKYv0nEDdaf2hMGI9f3DNcJFjIVQWbzEBVEv74AGwAhrVYRYZDe0SP17tRUaOlers9KI6pP1Pq0TcuP9jNeoPJjRvrT_-TgVVyXtF5WJJDNYxhiHXo-Fr076d3TGyeygMaSxzSjWXkzdm1uZJ1_zHqPh2w4Xn6b9nWP1Gc8h_RpD-OGs4soqsp3NWl-7hfI4OiXGgScezJ4yHz2haVEFUltwZE4PkZ-eai69b13oAm1JYEhXyIazfB1kYbUXSEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=aPyLo6hmkwhn8l1BmOcWzdbELFru7B1n5YDD2ESGOxPw7yYD32K5RvYvHBP8k1FKuoCGhm4p1Pf4380GNKDhYRladDHobDQfqTkNXdDh7uNUS41lKrP2jw0kbh2p4mlBGFoQUtdtwjVaR3AMjiEQiFteFbCh6vXCNFnAKwxcHaB0uXYR9DcWmyLYKIscVhJzprHFo4eEPqAYWFaflMfWGYJNCmumc8MhCASwi8yVpIMfy5pyKH329AGgaq6DF9-JilrTba32LPJaBE4c9wG-b0-dIK8j0S53yw95qIh0g7lvw50EfP0tmae00n9hFBO5dFu2FdM-9vDQxIoGZn9GOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=aPyLo6hmkwhn8l1BmOcWzdbELFru7B1n5YDD2ESGOxPw7yYD32K5RvYvHBP8k1FKuoCGhm4p1Pf4380GNKDhYRladDHobDQfqTkNXdDh7uNUS41lKrP2jw0kbh2p4mlBGFoQUtdtwjVaR3AMjiEQiFteFbCh6vXCNFnAKwxcHaB0uXYR9DcWmyLYKIscVhJzprHFo4eEPqAYWFaflMfWGYJNCmumc8MhCASwi8yVpIMfy5pyKH329AGgaq6DF9-JilrTba32LPJaBE4c9wG-b0-dIK8j0S53yw95qIh0g7lvw50EfP0tmae00n9hFBO5dFu2FdM-9vDQxIoGZn9GOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkWAI5Qjujm6XRa9tLEAxX-GTgGRGsvWfmKzThn3RgoXvfoNJIfoMptHRdMy3Asv3a96Z8R2IqTRlj6BV7Zn3_30mCrcN1SPMzVSwrcXQC-UHkDYlqrll3Wjn0UjwXFrtXOzy3gpChQNmRdyye8n_X9F5lQF08UeP8zxE1Q-VFMcWb9ka5SCQSXlsG5hjD95ASeyvNPk82gHQiLBlLZSZhPwMeHFn72NXniO9rUrsGZtJLiWW3683K61BGKRHDQGNI8P4FGS2ltBq8hq99Oic2A-dyUUX8ZiDeAyuMcC8oP4B4sfqf_MPlE5q4dpSUvf4eVouDHNMKd1LPTeHjN4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHNzsDpZyPgFM8_rxVOB_sqf0EdODNC82NTKuEAmZ15tEvMWvalz_ppcM_jFPmC3pV1uu6d2lnvUBxP0kpRqgpheQV2Ei5c-ACyX_y5YcFAw8ddyaurAe8TaG3sVoO3WPpHEq6Y79dgmk-_0qfatbiPTMZW5I2tM-7J-NwqJrnSN0X2UIgEwp6liBWp8kB7ExKyhytbloa1ziLMWnE3pWeT2hPjwBMZrB1kZn8v49gUvS5fqol6Y-FpfR5nKgAAAQjlSdCA0l6InCQcwpwZ_XlOJdya1e_YYyNBmgxNWj4RAKm8frfz8Zu8aVejsDSSomwaT8juAKisbfWeVwkNXKVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHNzsDpZyPgFM8_rxVOB_sqf0EdODNC82NTKuEAmZ15tEvMWvalz_ppcM_jFPmC3pV1uu6d2lnvUBxP0kpRqgpheQV2Ei5c-ACyX_y5YcFAw8ddyaurAe8TaG3sVoO3WPpHEq6Y79dgmk-_0qfatbiPTMZW5I2tM-7J-NwqJrnSN0X2UIgEwp6liBWp8kB7ExKyhytbloa1ziLMWnE3pWeT2hPjwBMZrB1kZn8v49gUvS5fqol6Y-FpfR5nKgAAAQjlSdCA0l6InCQcwpwZ_XlOJdya1e_YYyNBmgxNWj4RAKm8frfz8Zu8aVejsDSSomwaT8juAKisbfWeVwkNXKVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=LMmeXHrz8tYulemv29x0DJ2XNqTuofRnYoDmp1JHAujabwRRY2e6_3UTgNxdNTD_0w8HngJGETKOWKGIO6sghYVNwDWur-3xiwPI4yPX-OBjdMiMlqbYBQ9ceTgCQzIZyOY6FObOAEwiCbw9dMAGfdIoWHE0BnWOArOQ14nDcnFPG5vFXl0R5fOFIoxBPAV-fM4iQNCPfVoYR4uIVjhqfa2GNffji_rrdS_XO27MPCG0mmuaNH_yP4HKxzdBrV-3rdYsm386qmLhqZU4eCAyxl5pikvyLU5eVk5m0JJZQxlvuD6nINW7igLgHvidZlmDKxk262zZEIyxtKUarmEjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=LMmeXHrz8tYulemv29x0DJ2XNqTuofRnYoDmp1JHAujabwRRY2e6_3UTgNxdNTD_0w8HngJGETKOWKGIO6sghYVNwDWur-3xiwPI4yPX-OBjdMiMlqbYBQ9ceTgCQzIZyOY6FObOAEwiCbw9dMAGfdIoWHE0BnWOArOQ14nDcnFPG5vFXl0R5fOFIoxBPAV-fM4iQNCPfVoYR4uIVjhqfa2GNffji_rrdS_XO27MPCG0mmuaNH_yP4HKxzdBrV-3rdYsm386qmLhqZU4eCAyxl5pikvyLU5eVk5m0JJZQxlvuD6nINW7igLgHvidZlmDKxk262zZEIyxtKUarmEjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUWC-cfo0zKYYIAePGYVs6swI82Gc2fcIN0MWyaqu91RRTyI5OD3RXZJdTOW_6lwD6VPuHUgjAlU1EG4090ezUZsfAvy4fWyzbMenGtF8Y8bJ8nz3AJoqTwOrwurnXqHFRJ0xVzEqG5jiBdvcyKAzkc9XEZCHGAMZfVWq10S6PynnO4zIpmTz97FhfQOp23CUB7UqfhchEZMnHi-34VsogkyWB5HH5kHWuaYcITFddNIIP9vVUHVM2Mx2iYfo6NG_4Ur-FHsAa7rv2Wp3yAHs3CbO4QKW8g6S-dNe_qGrdhbkSf1z_gxstLtjBBsaJtU7ZOLfxG5ktpCkR_tMLw-ZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUWC-cfo0zKYYIAePGYVs6swI82Gc2fcIN0MWyaqu91RRTyI5OD3RXZJdTOW_6lwD6VPuHUgjAlU1EG4090ezUZsfAvy4fWyzbMenGtF8Y8bJ8nz3AJoqTwOrwurnXqHFRJ0xVzEqG5jiBdvcyKAzkc9XEZCHGAMZfVWq10S6PynnO4zIpmTz97FhfQOp23CUB7UqfhchEZMnHi-34VsogkyWB5HH5kHWuaYcITFddNIIP9vVUHVM2Mx2iYfo6NG_4Ur-FHsAa7rv2Wp3yAHs3CbO4QKW8g6S-dNe_qGrdhbkSf1z_gxstLtjBBsaJtU7ZOLfxG5ktpCkR_tMLw-ZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atU4nOo1eFtFeW566DhZb96YModvJftCSOyBQF_jc052scV048nKcRNMyESQHY2VoeiEpJAcUMxe6WXJmJR1DYfErAqUOsjta-4CbdEIBSW1k6GOynGcSPP45q84EaijOs9hKb0V1pQLBsev5mg2OWuTHnWlkx1mbvpYAfe4nRVWTDKyaSWYZHf2WVDI6G7s_D2ZXd1CX22yLESUnsc2-HWbde2XnNbLK0TYq_aHg9wIYAHHoghTlW6Uss4gQWnQb-bJyJAnu9uLylImr-Si1qUMDtL9oqzyli4cuVfQUsR0hbMzT-DmDsIcBfSpLmA_LcIWgjdpy3ei2iIB3ylftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZu7DTCxbeEGA70_k4V_v-ZgDFaZ8iaefUax7E1vqbyo_xu03qDis0ZuZeGlTADWBZbf6imdrgPh31P8sNO44uVE5SW6C5V-wyywEFLI2SI82P5zsgWcyV_TTw2KrdzRt6cYDuduHzCs4K6981xNu0n_zZPFlNDBG9wayWsKiN1aI_xu3jxbpfG1tbpxF_qoKTxZdCYntllZ6B9Jb1r0mDDnYePMMLyeSPYBbJ0gH6nd0RAnHV7t-p5gn1rBp85ztVENdicR6AYDEgOWCUAyfmfU38qP5H7R07V2EeJrFhl5aqBXrdI4VDWHPmYwYBikZgc1uLqceyRO7ptAK33_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyipPFGRbs-2o-tju9K-b1iZctnnhJKqPwfhlzQ5Wjz2eKxLywSG7a-zPguzLkhjBoYAFe1R2YhjiqnN_GZBQ90Ifdl6Gj8InRBDNhjqknLMpCkyCArziW1cCAwDeYQfcWZwUa8mh6v4U77De08hyZv_UNN0zi4QbmD-W8D3FyTIdkbRsVhReaV-nX27sFPiWpMj9Iw3B12tuRncNE45w_fnx0JfFLhbiSUBhySavhpWZTNZuIZu2eTUJiKQuRSS5AzypppJuZDjDg9vYBfK17uzfxQF3BS6ulwH8vQLwAsFhir9no_Ia3xKw63wdxNZ_oFQ9hT5Up9-KhLlznBU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcyC9vcwzZ8At2J2nb4vVrXYqPlG3_riJgBiJfW7hHF0UYHCZPUoJEjc2dFAO28ChwBvWw72RmWzyjqsiv3SqvVfNbw7eV0hyKqLsB_MPODTMrJ2tyoIUWJYFI7tl7IPw5iG_K6Re6izrO6NsCxoY16QmxNpPVE9fsRleTa7vZl93mn9VuLt4GxRQzFQnoIIp6oxuN9QH3MIu3mKymMz8CHNj-t8031DV7N01ovqGOP4hrEfe3GL38Z6Vnl8JO3es-y1CgIyySago3dh_FoHfExmpC32eQJNNGyPuql1LdxiTc3hcQqMtyQQABdTMZdFcmg0PrJRXpgJfN4JIVFP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
