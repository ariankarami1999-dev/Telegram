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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 11:14:09</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qk4N2d_JwRM7FtcdY4HvVvT0IyljgeSDWrTVkSFxy36gz9KCp1uQ4Afzlr1KBmlStiL1phm8s3UBXfBhKzmHKZBOiq9jowsTmmUvUMmeGWc14d-1_KQkUqWbxRMZ_2FIsVpddxzvh3A6E45p53jd77mhwOAnDx7PTdV54CE3l5VFK-7fZXD6wM74c4cZMSmk2u_7d4LOvmanPlbVY5HzEg0acz6wFweJoaOys26x-UU0LSzgsKgRFuhpNsTnXLO8eMz_dyb8EsH22Og2fNthG5lbcDr4EF-8B1JQvmOyp1B2WhamSiKRDoqBXMHKg7YMQPid8FS6I13U6STy4Lm_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHH8YhvV6ha9gefVO7KeZRW97QGD1txBDpwljLEH9fDRPstxZMNt1Y9AmSoQ-egx-vWZBuzPFbR4IC3udjBFumerq4zQ2ZHSPu0AL-eGqXAVV8sA2MZ2DuUPzRIeUr6BmSl-v1ShpQ3CBq1Skv_Q3NNXHJT-gGoIj0qikgmDHSMffRZcR1Er3FDf5Lnuv-sa_SwkX3nQ1EqkwZ5K7kzGHWkK3W5VfTD8Cbv2oBxCRRPaNvxk0i2atYH_2iOJxH34E9EeVwUzHgX3-Cmte3yCBVdrC-PK77AQ5MBQNudMaUJ9fzI9E8mQvfO-9xsZe7l8vEQuOFzGJ8QS8PLSXBAihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZBjIdJMIoA-Ccp7luzFMPVDTHBZ3VoLCL3MalkUdBJYKI2hnhlKuD454RY9DlBCMzXkp_b212Q-dPinB8R7KkdqPx5EcfdaZZYKx2ni7pK-YahMzvuXClwdA6g2EEC9UvQxc2pe93gKdwwgNbPVg7kgCd9hCQSCBa3mB-Un_gTihjU2J_eDnRI-LOggEuG__A6GUzjbs6Tp37LjtCyxh6rk3T8ng5owAcoWNsRswEVEznWxkZm1vqilMRknbxNEkA7ksfNnHQYBBfvqm5tQUbbnsIolXW9JbdjI1mZnp3ELDrZurysuxmbmypmsyIU1TEvhdllopPQ53zO5cDBNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=murRuyC74CYq-QK4-fhYVeJYBgFj56nU5jLC7XYxCYu2OvskFMtk_qGeP4qeah21_5lUowACUjn2n0JozEWYYGXKFBCTVNifCL6gXNE4O25iCqpeBQcxky7K3hdBd9AItN8sNHXz11FmoorEE26mGjGdgU1gHBAnbGjmACP0tROeoMmMbJ-cqLdPO9hLvgGk-wvE2flKrOw6vHTRLny93-ZxjRPd4JBN1dC29pwCm0ujNEfz-40gzWYiMjXR1SFyXvP_sBJ04zmqlNqqKSk9xKM1ELPlLRl0NPTQHcovzN7OjiJoQAkPeb29pu1SEpF35jRQF89IIe1D8AugJDjjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=murRuyC74CYq-QK4-fhYVeJYBgFj56nU5jLC7XYxCYu2OvskFMtk_qGeP4qeah21_5lUowACUjn2n0JozEWYYGXKFBCTVNifCL6gXNE4O25iCqpeBQcxky7K3hdBd9AItN8sNHXz11FmoorEE26mGjGdgU1gHBAnbGjmACP0tROeoMmMbJ-cqLdPO9hLvgGk-wvE2flKrOw6vHTRLny93-ZxjRPd4JBN1dC29pwCm0ujNEfz-40gzWYiMjXR1SFyXvP_sBJ04zmqlNqqKSk9xKM1ELPlLRl0NPTQHcovzN7OjiJoQAkPeb29pu1SEpF35jRQF89IIe1D8AugJDjjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRxtnQTyrlD7I9-KqGPUkacAASIPT8FOg92WHBEblHcciAbGPRVn_pAgUaeH9CgeGGLbfMolB8r8vajZvJqfTDUydi5IaBOKxoYoDozNq7wrfxFXix_i_Q8xKaU0b1hfDDXE23WWkG8anli8DQYfvAHt-MNyAu1qsc3BTNdITMc1qdXXF_Y4ZI8N6-egIQlDPRxwukQLHnRGeA6Vn0n78ieNAuD9AvkT3bawbj4ONL_5GeCDW_2f_IC1BXQS6nq8tp7Ddqn8H3PWhyOLuwibWw5ggNmWAFu_M8TqZ2eXuxkwDSVANOzLtMIOXxOyHgEqk5MYyElIXEnJN2N0xhpAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hrov2clrBy5U6cPKS5yV2bEGzdwWbEkY5uPRbA1LeQPVD_5SU-SSN_i4DxMbZOC_qPT7OvuXzYEMcqqUVTmTwJmSwCLp5Oqj54xsialf3VvL4dv6iKmwW2ML7xEElIcD_6EO6PSdr8hLdGOaV7z6KkfgNcXTNTK-a6MFylFb2selmntb5W5UNe9VQFm1AWbg2YqMd2GG8EIbBRw_wf5FgMfEjtiiiUutSkkRPtsNm7c2L99XIxGUE9Lm7R8db1EIDF3GRhxM08Pa4U8fGWv7PtryiRMnDn9eWKELutLkmxQQYvybKv-_iyzgj2KsxTIgG6EVGBbI-nAjo80-98rKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHLSV1EwCgY7KdJ9H86iQl1IzKGkyFLUlxFb-8MpjwHpatBpv8HcICKl72djSY_IGd06A4A5c2MDpTFKvRQDxuKE0jP-BmpUIfdsYcy5wefHQbzujVMVNTptbIqSqS_QAic3p1Rr6YnnsxZSdidoGYXDh8IJDmPsh9ovxC9pJFl0mQCkT0IHqVaKHdluHfIYugNZyZdLFmsB2mGa_6aWSD4tEbARXQTu_kmfDPv5kzw9oit06ZQ9IR8HXe_zBxMrzsWbq92tTa88ehZXidWayN9F2CZ0guZ4KR8u_nne5yCgVEDx9aCtAcJmtdFz4V-V-jhOvx71W2CzE4CQtfKivg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9hU3a1pnaTQxV--3-jK1DoBrou127gHOvA0jhCdi11xOfYX9kluYbaks6UeTURe4ltTFxHJLXWrK07NDeHQq8DAm3ruRf4fIPKhZs9HkabOwtGnaubjlrV1XK0piGmgzW3m5XBmnOY_a9BwzP1LvCyap0BEO2Qa-HMPH874IfBzQc8m2U-14mXNUL_qx1aM_pV0MhmtNk2_0m4WT3zZBsklxBLOp3AziB3B2coiDEmsKD9ikBHiuCSl24JisAM7plOloOvyXOUsOtc51fFTbdz2VYdV7VORB-0UEzz9DmoKIcK9MyT9mwdW9C1NQD9s-iTyCSWBs7eJaCwJ9sirLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QmAPwUxAzeagaPOmnu1F2zDkkRQXf16hEgx2j_W5_x5v3BbmlNZJ7fN43lbtf3-aiDtZMV0TsUkoFpS4GeB91AEQvQ5boPsEiS-5lMuVZUwNp4V1D_nEI8IcmVEOl8_T7MD_zijsQdBK2v9Wrcsfvvqomr20B2rICx5rvKKWBGlJVhlm2kwCzF7kJQUtWTIuaP7abNhY_IjXJVbIBZnNMijwmyoSmyFx-jb5Ja1aZ94bpwlfock7BfUykkChftO2a6M6E2kVr929PQjtOg7pQYz-neCz2yVEw_4kpYqV4-krqBdK0Ut8vbn8hvjXlVTF_OuiPr0dSN1KwCpLnNcbiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QmAPwUxAzeagaPOmnu1F2zDkkRQXf16hEgx2j_W5_x5v3BbmlNZJ7fN43lbtf3-aiDtZMV0TsUkoFpS4GeB91AEQvQ5boPsEiS-5lMuVZUwNp4V1D_nEI8IcmVEOl8_T7MD_zijsQdBK2v9Wrcsfvvqomr20B2rICx5rvKKWBGlJVhlm2kwCzF7kJQUtWTIuaP7abNhY_IjXJVbIBZnNMijwmyoSmyFx-jb5Ja1aZ94bpwlfock7BfUykkChftO2a6M6E2kVr929PQjtOg7pQYz-neCz2yVEw_4kpYqV4-krqBdK0Ut8vbn8hvjXlVTF_OuiPr0dSN1KwCpLnNcbiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=sWNtL5uDc6Ego6P-mU8uG63cZOdriKlK5TAN2oKa2q9TD3XFCiP05Sr7B5jOCPgSIJbDCu808vOVfsBtFvnKSdaqXD7dyznfo57IY3VOpo-bU_g0V_UGE5DL5KTzVumSoilSkOYZmSC-4dTLf2sDMicFscVODAp5j7yTIT_JesRqCr0ixPWxb1gadd2bTkNZn0La4jWHjq12U_t-EFd8itJoW9AdQIBYDKp3-mQKv2nI4WSTVA07NnMe-buOCV3JkSL6qpPmb8pdUIQ9F6R3MQI6HJEaCdOA4GyzqmjrDvoXaZmzRm8JPUWSh90p9s-8g9ihddSes2kOwKjCiAGy6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=sWNtL5uDc6Ego6P-mU8uG63cZOdriKlK5TAN2oKa2q9TD3XFCiP05Sr7B5jOCPgSIJbDCu808vOVfsBtFvnKSdaqXD7dyznfo57IY3VOpo-bU_g0V_UGE5DL5KTzVumSoilSkOYZmSC-4dTLf2sDMicFscVODAp5j7yTIT_JesRqCr0ixPWxb1gadd2bTkNZn0La4jWHjq12U_t-EFd8itJoW9AdQIBYDKp3-mQKv2nI4WSTVA07NnMe-buOCV3JkSL6qpPmb8pdUIQ9F6R3MQI6HJEaCdOA4GyzqmjrDvoXaZmzRm8JPUWSh90p9s-8g9ihddSes2kOwKjCiAGy6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=bK3XXY-3z1ms5Xe20-gqK3RoZELfHh25GM4BoG2ZKE0HAMHlNzwEiyFBEftJip40oMhRN_Xfj-1yy5bHk3oTb9Hkyfz8-FOiHjf4JBPKZ05xeUFC7O9dJ1zopB8wP9XCQccO2YtttgbtSpO7cJkLUjPiHFgMc4f6AlWIDELinXnilak8lH_YBZd_crBFP_5YsFTkmz-caXRXiycoZh3xseWvBcYM4U5erX9SX4C00EtcQl_LBC1czk-fMFfsYB3PqWNp9H96go1NgJ5J_b2k1yUTLItNM5vlNAcQ5D-vH7dtERzC6tEMXwPGnyRiDbnRy2IaYnqz_4moQWy6i4-q9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=bK3XXY-3z1ms5Xe20-gqK3RoZELfHh25GM4BoG2ZKE0HAMHlNzwEiyFBEftJip40oMhRN_Xfj-1yy5bHk3oTb9Hkyfz8-FOiHjf4JBPKZ05xeUFC7O9dJ1zopB8wP9XCQccO2YtttgbtSpO7cJkLUjPiHFgMc4f6AlWIDELinXnilak8lH_YBZd_crBFP_5YsFTkmz-caXRXiycoZh3xseWvBcYM4U5erX9SX4C00EtcQl_LBC1czk-fMFfsYB3PqWNp9H96go1NgJ5J_b2k1yUTLItNM5vlNAcQ5D-vH7dtERzC6tEMXwPGnyRiDbnRy2IaYnqz_4moQWy6i4-q9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXt7rWOexQ6hqv-W-WW_1kV6HSdFhv0i2UvvZM1C5IqBHEUc-pjde0ae6PmxApeAmqWEX2avn3Qk2hL8Grd5KPe1gRThu9nvyAjm2bNA8QTyWdrMOtnS18a2Mt9XukSychcPbDRM-Ry__004dexckmUyXQw16lr6KWA0sppVGSwhtJkfE5uulrFaDapf8QWfGcN9CEHlRNQffFpFOSuB4_cDN0APfL1xM9r0owVIJ2QguWvjCMVpdopYJiYU3aIhjmHfcMguhiK9yrB2tb-O6NFYjGFleO26WvSqwWQuegLexSrXnsFY7EPdTIuH0LSxzbDX2UesM5yLvxG61ZaeKQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QhXVBIv8HGbK-Sk5DH7SG2-rtspXBaSLGbqUxTu3WQRX8TxKV1m9nigvOZZf9pKkKeHAs6xyM-WGyEMpkN3o7k1cp1ww7LJkNu1oq6POcmOMnEaAujEOPjgTRPrkNZD_IeepJ50cN0EAPMKrHY254Q9IZuO1w6sBVdFhIlUG8bXmxHSPUYraCZWJm3cXjbEWhX95sUOKhCxQBM8IC3kYoFrhOzZU_t19LePheUWd97UTArfcMUoifLeGxLsa1AUQECxfHPxSAgwVHK-zRMMI9JqYNEUkAp6jmBfrnM8pU9jx0qf9s5HfgdtVwN_s49NdjbM7h27ByqUWtKzgLT0mPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QhXVBIv8HGbK-Sk5DH7SG2-rtspXBaSLGbqUxTu3WQRX8TxKV1m9nigvOZZf9pKkKeHAs6xyM-WGyEMpkN3o7k1cp1ww7LJkNu1oq6POcmOMnEaAujEOPjgTRPrkNZD_IeepJ50cN0EAPMKrHY254Q9IZuO1w6sBVdFhIlUG8bXmxHSPUYraCZWJm3cXjbEWhX95sUOKhCxQBM8IC3kYoFrhOzZU_t19LePheUWd97UTArfcMUoifLeGxLsa1AUQECxfHPxSAgwVHK-zRMMI9JqYNEUkAp6jmBfrnM8pU9jx0qf9s5HfgdtVwN_s49NdjbM7h27ByqUWtKzgLT0mPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=TkHGT2EVvotn_XsW0pChxjzo38PgvVNfLmDRun0wFaatFAtneuBPHgYY9BY77BdpLP3HdCly-nuePc4Ro3rHu1UywE_SiML8qWlFWSRW6aflyj7dnYjy1Xxg4xjl3kCnYKaWo8zbgMM_sSk2DpzkOrx7VPMn4dklnc8tIY74MNM1s_QgrCMY8pRoHPDUWEPTBy1ZWe3V9oNaAjTachhfk3x3Ujrg0g8KSZHfYevz_vsi8lbABfjzgxB7wR2gJtwwyzIWImCjQmmjXvAU6hx-knDk_xrOnJ8FSsoDOkHfPmzMvqWQAjUAojgogI0SWtye4NdVDIEHsD-5nQ6nLWQ9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=TkHGT2EVvotn_XsW0pChxjzo38PgvVNfLmDRun0wFaatFAtneuBPHgYY9BY77BdpLP3HdCly-nuePc4Ro3rHu1UywE_SiML8qWlFWSRW6aflyj7dnYjy1Xxg4xjl3kCnYKaWo8zbgMM_sSk2DpzkOrx7VPMn4dklnc8tIY74MNM1s_QgrCMY8pRoHPDUWEPTBy1ZWe3V9oNaAjTachhfk3x3Ujrg0g8KSZHfYevz_vsi8lbABfjzgxB7wR2gJtwwyzIWImCjQmmjXvAU6hx-knDk_xrOnJ8FSsoDOkHfPmzMvqWQAjUAojgogI0SWtye4NdVDIEHsD-5nQ6nLWQ9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CQ3Jtp9LZvR0Zj_VrwgikNdgR9AW8Oel-0i7bKdfq_TE175l0FTJR3PE7FmgZmYs5gm07c_1EDeNYfr_b4moPpGA_J6G2M5IreXwwgNybAiIv45KgQHZXTR7NYDh4sw7f_HcBF5sNWECOxapZgGwGqJXyGxG2V6z4t3iiuFdYYKy4cDlICIzMfrFQcofB7JEFjmvoqlGnMeNwfpZgpubae0kJG_PGlc8A3YvoreL1AyiELPE8GGFtfUAjtvsm4C1FJH1iyOPPKJDErO7FwPiHrpP5MXZ5MUaSBhE6TjhpazoqsTS2WHzsZIfOSS1wfWzEAJggtEl5LNNq06uTIvPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CQ3Jtp9LZvR0Zj_VrwgikNdgR9AW8Oel-0i7bKdfq_TE175l0FTJR3PE7FmgZmYs5gm07c_1EDeNYfr_b4moPpGA_J6G2M5IreXwwgNybAiIv45KgQHZXTR7NYDh4sw7f_HcBF5sNWECOxapZgGwGqJXyGxG2V6z4t3iiuFdYYKy4cDlICIzMfrFQcofB7JEFjmvoqlGnMeNwfpZgpubae0kJG_PGlc8A3YvoreL1AyiELPE8GGFtfUAjtvsm4C1FJH1iyOPPKJDErO7FwPiHrpP5MXZ5MUaSBhE6TjhpazoqsTS2WHzsZIfOSS1wfWzEAJggtEl5LNNq06uTIvPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=vLBjTekG-4vwQ0TjPUXlw7-4vCH0nggrRJPnm6vkd1br_PXyRPjGkrQON4BI1vDA9fzH0T3qyurf6exWL57ul1DTp11iDsDIzBi9w8xm0-rlmvAftoUGQa6KS20nl7rj289-AKmLeLoKdgqUkEyOOVuersoR9nGWGaTz0xSCN8veJCsqTK7ynZMTCCzwvHMU0-w5xfppl-t30bPkArI8UYjppC4T8_0sOUydwLBH_c7WbabdLyQfWHOiCUUTcEHqAAqbll945YMHsww3bDCFDHIK9-q0zJQBG_Php2xs_Kc5-3vc40cGb1sbkMtQGLosVIczik6p4rMyhh14ejr1hIenepAYexqi-yfqwArAHpGoWYc0AaFGVFv9Ld0GSOXOO2prQoaNX958-mV-9hPqaXY9F8-Ei1hq2NigklxGunBK7JOWm8b_-cTCOrsxs63WfE6SAUFh68C7NLAeGlznuNZZrh6iPQiIDHcmE8CRUMYEDirr-pXDZtRYQEO-v7q-Zfl8NPPLq06wMnx3XS56LyH8QZhXmfOm_UWgD4yjxnhDHmV_6KHCBYeeggETVhjHGezL1GjsRjDm0GO0g8sSs3AQlKJP2eHNPltoBs5iBEyW9aZcVMhAJL6RK9knocp6WCEBsu-pDAyxcSvmwRuDMgBBPLmyTeGKaj8GZEjyOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=vLBjTekG-4vwQ0TjPUXlw7-4vCH0nggrRJPnm6vkd1br_PXyRPjGkrQON4BI1vDA9fzH0T3qyurf6exWL57ul1DTp11iDsDIzBi9w8xm0-rlmvAftoUGQa6KS20nl7rj289-AKmLeLoKdgqUkEyOOVuersoR9nGWGaTz0xSCN8veJCsqTK7ynZMTCCzwvHMU0-w5xfppl-t30bPkArI8UYjppC4T8_0sOUydwLBH_c7WbabdLyQfWHOiCUUTcEHqAAqbll945YMHsww3bDCFDHIK9-q0zJQBG_Php2xs_Kc5-3vc40cGb1sbkMtQGLosVIczik6p4rMyhh14ejr1hIenepAYexqi-yfqwArAHpGoWYc0AaFGVFv9Ld0GSOXOO2prQoaNX958-mV-9hPqaXY9F8-Ei1hq2NigklxGunBK7JOWm8b_-cTCOrsxs63WfE6SAUFh68C7NLAeGlznuNZZrh6iPQiIDHcmE8CRUMYEDirr-pXDZtRYQEO-v7q-Zfl8NPPLq06wMnx3XS56LyH8QZhXmfOm_UWgD4yjxnhDHmV_6KHCBYeeggETVhjHGezL1GjsRjDm0GO0g8sSs3AQlKJP2eHNPltoBs5iBEyW9aZcVMhAJL6RK9knocp6WCEBsu-pDAyxcSvmwRuDMgBBPLmyTeGKaj8GZEjyOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=W5WFp0WBeXL1gXwLi_D1q0kSyZ30F3g9PD-kOpMshMRrH2hSGxlMT5bkOOXuXRwupoNfZB-nxvB9k5gccGWmSrbyqDlfgsTWQ63QKzydYKJxq-Xo5cO05PX89UjDqlBVgfFOflDL_8D_3PUwafTozPt77uonpfDc48U_paVpyXAQrLPuO3RZD1VC2tmkn3JD0vjzIAIlOCWy_U3kmmiE_WzOJ6isw9XvVFibk6mj-Rw6LlMTMen3vMOV1-Ou4PHcVUY7L09MgAoY5jjGX3lHiW29QtaiR-sq1-IS5bvDCJCqF6hS15VAs6mU4tp_2ikwjLRpjoQHY6Ct-Cglqvt3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=W5WFp0WBeXL1gXwLi_D1q0kSyZ30F3g9PD-kOpMshMRrH2hSGxlMT5bkOOXuXRwupoNfZB-nxvB9k5gccGWmSrbyqDlfgsTWQ63QKzydYKJxq-Xo5cO05PX89UjDqlBVgfFOflDL_8D_3PUwafTozPt77uonpfDc48U_paVpyXAQrLPuO3RZD1VC2tmkn3JD0vjzIAIlOCWy_U3kmmiE_WzOJ6isw9XvVFibk6mj-Rw6LlMTMen3vMOV1-Ou4PHcVUY7L09MgAoY5jjGX3lHiW29QtaiR-sq1-IS5bvDCJCqF6hS15VAs6mU4tp_2ikwjLRpjoQHY6Ct-Cglqvt3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=GD-MpYHemK_TnTY2GqX3Mk8YVdQnyrmDWPBJxcmb9HglYWlvqTSt6zvYywVk6rxPV9EWfJPcAbcLEIsz63uVshCrIlUUTaJR5kFg9Udr84oHV0I0nmWIB-_ou3QOy-MNs7IBafbk-pVCkfOgcuXbO8OMboln0QSKV8JEr6wZa2TlwsnkW1kUERTri6BmYNAx6g2jGIrXlYxDfM6Gbgcg4E8gKuJNKI3iy_6ftQP095I0b4I4FoAFiKf3NnXJY1G3mgYfFQUDBXBybes7Kske4bvhSXc9ZVSX4X8dDwMvbIeQ95Bq96P2c005GedX5pYxEfIzEk9nQMkpOvA_8KbjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=GD-MpYHemK_TnTY2GqX3Mk8YVdQnyrmDWPBJxcmb9HglYWlvqTSt6zvYywVk6rxPV9EWfJPcAbcLEIsz63uVshCrIlUUTaJR5kFg9Udr84oHV0I0nmWIB-_ou3QOy-MNs7IBafbk-pVCkfOgcuXbO8OMboln0QSKV8JEr6wZa2TlwsnkW1kUERTri6BmYNAx6g2jGIrXlYxDfM6Gbgcg4E8gKuJNKI3iy_6ftQP095I0b4I4FoAFiKf3NnXJY1G3mgYfFQUDBXBybes7Kske4bvhSXc9ZVSX4X8dDwMvbIeQ95Bq96P2c005GedX5pYxEfIzEk9nQMkpOvA_8KbjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb3nBdENJyB6dTMF-30JCAkD_DdUVR6r0zf8dJfir-NTolTZU_NxO0MnOfWO8w6nPMlWW_7zxi1ckLzhDi5_cbujHbiKfG_sG7YaWx3OuNtCqSiG4NQFLbXiiPftCpagEaA3jbG_2Ur4O-QWNLwOUgj9-lA0Rw6TzeYYGtMWvP2BHoF5ER2-T1v9NkM7aKIsyGFPb53j1IaVAHtGpzjQKyHB1o5vEIERTx__MUvk_hHtFbo1_rqLrdRDeKZfVRwN___mejImzTF-7EEeBLK5zQzcn77_lcliC8PTp9S5E5Cpxz2sZI6_DsHfHVLc7pxVhEKLxW6mPBz1cp4eVoQ34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEV7rFZJOBKV9Njx4AcD5cWh3Fq4zc0oo0ZutTScmEpfeN_lV_44iO4xQNCqyCsl16QbKd0_sstumXZDee-BIS04wb_NKcJfTC9tal-ABA1rK-zsE9y-xKpdirIkuBI-JNGWLtrCej6MARJyV_O4Lgtwz4d3e-rL_vbvfnb2-Le_tPQnOKLpDwwAQV9aisNDw4un9A42PDgMwf2MrJgeV8xOohgh_rYCC0TjXJcS6-S9Uha8YTjDuBdVqVwBMztT1cVDF5lOHY_2zevjun3BnfGIwKzfbNDeC6y1fD5zbn6dQZOec-Eee9t7wwIOVfp-j0GKmCLiJ_HiMNpvS0tTcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eyzhoTC-CvKfH7K9eX16jZ_2Z2IaC33Ve0l-lzJkML7WvUIU0HzyJcPRsrjkmJBCRv0Fbbyh2fO0862MGasM74ZvcpCMZFm7JO0kVTfY40T-QjKM9gDvvj7dEmjMox4f6Jls6xvr-1BWBGl-rRwAVMy00BaFD9UxkgWdsK9kJRF_t-HFMY4zJSb0Q9UKMB7B-xeHzCSp5wnyVkfGzH2m-PJPPQLsekzRXi2YXshkVJjXJXlWtm_Pd4Dh0gxiKRTAKhduM8nsNVMadWuK9WRBz14y6QowvKf26QOVsAHaK7mI7IhypIwUE-UJyuZYK5KRkGpFeBAD9qFGmSyEelnBgj1YUDzL-Oa-W-Gf5SuBF8tHVR_OP5XiQngc3hDl1r_aIO4NwXD-3S1N-ZBECGSzQIJcplnwvOHpRilFZK9a04Q2-kH4P5XDci-7FvaALSOQg3rtKnWxkIitl9yaSg82S4JZcqSr2qPRAJafyFPJ6Lo4J8KZp014B0hbAhK5NFJKfivrgnm5tk3Qh5iskEiBMS6wIDV9G4eGfuMxBrZYrMO8FnKrQPAXW6PJHbLrAFMSRhQijdXaLenVasRyWQAK1bqrVxlV-0ONCIpYiKqb9H9IEcGoHwbqO3JzM7fiGtVn-Xz0uzOFlmQ7yz7ECVeEWm3yfLx9EOLIhhvndXoTo_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eyzhoTC-CvKfH7K9eX16jZ_2Z2IaC33Ve0l-lzJkML7WvUIU0HzyJcPRsrjkmJBCRv0Fbbyh2fO0862MGasM74ZvcpCMZFm7JO0kVTfY40T-QjKM9gDvvj7dEmjMox4f6Jls6xvr-1BWBGl-rRwAVMy00BaFD9UxkgWdsK9kJRF_t-HFMY4zJSb0Q9UKMB7B-xeHzCSp5wnyVkfGzH2m-PJPPQLsekzRXi2YXshkVJjXJXlWtm_Pd4Dh0gxiKRTAKhduM8nsNVMadWuK9WRBz14y6QowvKf26QOVsAHaK7mI7IhypIwUE-UJyuZYK5KRkGpFeBAD9qFGmSyEelnBgj1YUDzL-Oa-W-Gf5SuBF8tHVR_OP5XiQngc3hDl1r_aIO4NwXD-3S1N-ZBECGSzQIJcplnwvOHpRilFZK9a04Q2-kH4P5XDci-7FvaALSOQg3rtKnWxkIitl9yaSg82S4JZcqSr2qPRAJafyFPJ6Lo4J8KZp014B0hbAhK5NFJKfivrgnm5tk3Qh5iskEiBMS6wIDV9G4eGfuMxBrZYrMO8FnKrQPAXW6PJHbLrAFMSRhQijdXaLenVasRyWQAK1bqrVxlV-0ONCIpYiKqb9H9IEcGoHwbqO3JzM7fiGtVn-Xz0uzOFlmQ7yz7ECVeEWm3yfLx9EOLIhhvndXoTo_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3qe1igNFKPsT1e7aT9kBy5PEOA67fdYMdpOVkgSqB4DfO69G_CLP2dzgkdsnJB5zt53gmuBqN_aDaW5Q4Z6CugSC0t1CBVJzPK7YZ-BUFoi3u2HCiC2bsNGIVWxOaBgZeqbi3yc0x5arZnturwNFvTwF7iIzaNNzYf_nRcUal7qZtfGrhFmDh15KoOvQK4l-V_pBb-KKrGkHvxXalFa5JAvCS5fHHcy36g-YAjqPp2-pmF_x0W6kjj2gmHT8WRW4mbOlQoxG9KHiio8WxzzvyqIne6jniR3NxogEG8N4LPYlgeIy1ox2C_4Za27pByOSldVrGVZd6Kev6C3LwDgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urpNLS54whb5YGYS5cyGK1CGDT2i28yLF0inN5yVeDF5_GBvd-i7SqAVitEYspr7KxX1i4ASDbxf3kOSIZCDfykGfikkpLbEzlB6bI2_5d6a-3KDvKqjznTpPKHSdZZ21ja1liuT2OPs7yKuCpK1VH-uZQjlWwYbHKgcAdzzmRzVQGpTQx8izCgDqgCWnnUFzO88u1JKRgMJqnvR-NAEGxzMU57kBhOX9tB471Xv2sEQJh8Id5gQg0Yb0pt1Dbk7n8wkBFNrgRIcPGBsNrYEORWM4v42oXjezgrn6dB10svFQ4dMlOIPCJPi04M_6-jY9jLv-HtAOYeB3JFg65PgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHXgrUVi8eg3Ho3UGPtfWGe5hpuezuLqoG8ztaMgcBwHpRWV5k4ArZSCSZOdt-u4KxTJMqAupMG4xgeL4ps-0JwOsqrd9AHI-D63E1jIkKFMelg9zV4Ow1sfyaPjzCcvZ_0RFhp8b7CguAuAZgTkKwszRvo7OJaATjGlouOpMYi1AtMpYJ-yJGKmN-JENd_mKwaArsB24tMF3JlYjtR4IquGO_4qruj04A1oQvRPczPqNRFPXUA2-vRtluu7e_5fV_-uvzyiN6StTrfk9L1PVN4YFP4lV8HBf25IQuiOXgHrs-aR2DIFCILOtSNa_ks8v0UyMursFIUyy2DMn8gHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWEw_aZRJrmu2wRiDEOirdt6psZJvbKZrYWmJFgeIZjiJed6g4970ru1kTe5wtYDJO4Pzy3ZlvD8gi_spgeBgP_YahT4ntGeRL122aiy6RmZmpEwisJf4Oe-GB5BIBUZQg3rQ2dMWfndm2oNwr5aXVqqA2UwtvMEty-QLkSrYXkswJwd1P_FZaRroGSAgref3bxo_CbJ_l4n7N_TAeTS83yGAM08DY6LWSomgl_a_44TwrCJT2-hg2sOcC7nYgBM9xSo4gA8y8y5DKW6UaJdfkoeKW6i4k0qCnCuJXzDUpTq3XS_QLAf16tZbcNh0vHkd0ZtqKcHm-RX3bil6_rmsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=YX__pDXeOxkAa0irpZHK7ANuJ5N5KmGgmdWMlL0wU5iipVBlISV15vttebvdkvHJEhCXan6z27QYH2t1DAreoavf4reX-N6lL1tni6HaFYamFdISAb9kKiF9t_cnOqIHLM5ngvF5--9eZpd6tCXrU0laBEcNMgnkZoW5CiPkxkd6b_VTqaC9abkq0dv4ecFRHEAdYIU0S5_0ur5Qhev3ppinO_nFO049z7-0ANdpM9NrCF-KHmP8bgEKzWWfJX3fsUhVj1cERI2_6xKS4AFY04mib2Ywc4I1v27n158ZE9uilLP_WVfyYXytLHhh3YYSGdcf779EK_QMLZPQYVEhhJufnir6pIWANnchyOMFlJwReCM5ZPWy2zQMzKoChooZoZ0j2lN5IqIC_6dUnNmqxLuN-vWPlav2qUyz0CSMp6sR-q0qKT0FiNpYj-clfD4pGpdmJtIqmQt-GwDQUjoTUdZ639SLe1-pJ8MMS0ycdTTG3WlkumGZnX6Evae-gBFDwU81T9ENfVoPuCc9h6V6rq2JQm18zP7oDEvkue9Amem8sRybitjCRTMPCtFUx7IoAfuR1QSwM0NFT-quGwYWLb3n3DZoX2KLfo3CzwXGhWh_7clBY7qT6R75M-_ZZsCio7__GwsZOWYNFZhRmF15VB-0-GeOmKrTKnE-00cjey0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=YX__pDXeOxkAa0irpZHK7ANuJ5N5KmGgmdWMlL0wU5iipVBlISV15vttebvdkvHJEhCXan6z27QYH2t1DAreoavf4reX-N6lL1tni6HaFYamFdISAb9kKiF9t_cnOqIHLM5ngvF5--9eZpd6tCXrU0laBEcNMgnkZoW5CiPkxkd6b_VTqaC9abkq0dv4ecFRHEAdYIU0S5_0ur5Qhev3ppinO_nFO049z7-0ANdpM9NrCF-KHmP8bgEKzWWfJX3fsUhVj1cERI2_6xKS4AFY04mib2Ywc4I1v27n158ZE9uilLP_WVfyYXytLHhh3YYSGdcf779EK_QMLZPQYVEhhJufnir6pIWANnchyOMFlJwReCM5ZPWy2zQMzKoChooZoZ0j2lN5IqIC_6dUnNmqxLuN-vWPlav2qUyz0CSMp6sR-q0qKT0FiNpYj-clfD4pGpdmJtIqmQt-GwDQUjoTUdZ639SLe1-pJ8MMS0ycdTTG3WlkumGZnX6Evae-gBFDwU81T9ENfVoPuCc9h6V6rq2JQm18zP7oDEvkue9Amem8sRybitjCRTMPCtFUx7IoAfuR1QSwM0NFT-quGwYWLb3n3DZoX2KLfo3CzwXGhWh_7clBY7qT6R75M-_ZZsCio7__GwsZOWYNFZhRmF15VB-0-GeOmKrTKnE-00cjey0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=PubaTXruhD2CrK1KYuLMDWAHIRzAkdyeasx6ijsDYIvd5TsKR-FoLmXuK3CUudcB-kkp_wvG-OqXVW9t-pG-d4M8GmU1HKMNIciKicqrxSUvSMGC-BsuktfopT5KN1l182FeFIlj4gFIqMld5jF9go_9KuVOnhu_kBz-HUeFc8TWVJdHx1gPmLo-lbhoC-AaKDW0QSQZ9aux-RCYTT-dlrGshGYsSinl8yDyrIfDVepQINQOIPicPJdA01rbYLOPAuNFu8WUCSCHuzHpOvuF0XUUijN-AWif58BqwV279__2ntles7w5Bi3YUPP6UO_QqT74fENTReaNx6I9C2wchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=PubaTXruhD2CrK1KYuLMDWAHIRzAkdyeasx6ijsDYIvd5TsKR-FoLmXuK3CUudcB-kkp_wvG-OqXVW9t-pG-d4M8GmU1HKMNIciKicqrxSUvSMGC-BsuktfopT5KN1l182FeFIlj4gFIqMld5jF9go_9KuVOnhu_kBz-HUeFc8TWVJdHx1gPmLo-lbhoC-AaKDW0QSQZ9aux-RCYTT-dlrGshGYsSinl8yDyrIfDVepQINQOIPicPJdA01rbYLOPAuNFu8WUCSCHuzHpOvuF0XUUijN-AWif58BqwV279__2ntles7w5Bi3YUPP6UO_QqT74fENTReaNx6I9C2wchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txeRP4hzSILroT9VYsXAWETgzFDFSti8r5gHRYdrV_dbw71M6r26RWtN0tYXAIImdNxVQ4N8FrE_6SEjUNBkUKIkZ-xmYJRuskqmebhHOo7ZEUvxtSetg0IV906FISiScng66ySgNVusJBIG6X6SAWQEZQJ2gl7GNIb0uAGHufYjF8oMKrjv9DJJcGXQQQ8ci-peeOWYKaA_iNvi6I2IOgWbQCPL_jNesZiIn2pXtTh7OpXNPHNEhTbTTM82fLAhe6NXitTwDxvGo8gla4XhZpKFFJhy0lGq0Ac07JBpH079Ru-f2zNFaEeSna_TzF-fo5wPT5tOvHvRW5ax6Ey5JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuCK0n25QqLC0pwPRB8JegJnLsSogsA6axS90RtvRBVw58JJa7yxHqohzRNCjKosHJblsEBtaYVKiVM0OWlTwiW2BN2MaPgYkyF68qWTrvoOqlWql-w31WuazWrF6nSXhJzBg0NHIqIOFYMVL3p9zA1bktFX5t7cMWdavXpwk8UUMrcJRK2kmmfwzsYIbNKM6eTXaX0JGkaiSPNvc_utX8FjW7tdniV89xutIYcyHgQodEUgNo0SpjE7Cv6JlaAF-HKqEOh-JjonMhrkX3exAsNvdn5MTAIWkQeBx-WFfbTQ-aAfWkpZaVnWukDiTP2qDmZ5FZkJ4T1Da95Vnhz41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJTa1ac1iZqPMnxLHgUNM5XkSZ9LoyCgl0MSPkEm_GJDCsuuAEbqiJ6KnOYIiMLulaan0npqYXsSnmiOsiR5qtzMj7MURnF7tV2qGwgEkRawxAIax3zsFy96uSWkyNuLiLqEck1oTwMP5_m8ViLhC_NFqUPLek30Y1OHSvOuoVLO1242qr2yiLcaUDVFVmU_mhNYozARSP5zbkpW03th6Cop3Z1OhWUQ2vHi-VRY8MHNP1fnDS0nTAL0BebllAtxQ5vppY6mRnuIceFLI3qqssjSRoiohyuzPb0S076xzjjzDTaze9Mo7860Bn5o_nOdK0-zLhkhJLXYZrGkfNxeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIvBNSIcgekIk2de-FvZ1FUaruJc9hWeczVHFV_mg4NZBoMs4QYszATyoW3ku0ss6ob1qklxAKvpKMeSljEmuGe8ADCsCb3qg4EekPCr1A8eb0x3U01HugjjMRg5OCy-Yu-s6mLdWsFmtHvm1cx1hsPGopJbSko6vLhOjt8anxCw71tO0EPHOaHuWVyTFQhUR9jtGQVp16LSpa4eJvbAaM31JyomgF8CTX0G9V4JwWpf1RtDCSa2gukeOdLrSCUnBYunkjpo1UJ5lbBVBj8IywiMKH8U8F7ym2w1xkl-S4IoGQ4mdkQHVAUcwQOTGjOZH0P2sSd5hELgSRLsTEET3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRLcDM4l1N0knWZ2_1tZWYCQNFJf3TwMv5xRD5hnhC1Wqs4mHVJ0lRlvkj-bfQXZuxuiak2KKZ2Dd-k2O_VOfOeF_PV_DsP4YSmBrrUQiGs0B26_tgK_jCWhh-Ua2dPAR3gVWMXbbqIevodQTuI4qBiadpF2Vu69Z03d5XR8ea_zFUzEixPpeoEuLuypSUnibj9I8FzzuhqFwtEiIHTPY56kzefKnpitLT-zUsjKpt46uMZ4FPRTDG-m50pmiNhEzBMtr8FnfF38-Egj2PldA4svNfO6zG8UNeYHSx7QzXWBisPZJlh8VSlKCLye_iN1NPtOcPB5E9zKgj8J8M0-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYI4lqWnbe6uUmq5T-bYrMIR124Qr4cVPBvTsJ94VJ-MG9N7f67KKhX79OzERUbpv-W2qlgoLXm_NqOfR13bhT-h0AFMIGUaexqeJS7iahbJjb2rf0UJyohFcepzd8hDYJ8Wlgfw1W8pwkVU79Zusgp8UFSPU3oNsSrhRSL4zdZe1R9QiaIaQ9duvi6IkrGS6mEOuGRJMyx8m-qaEpOVeMkOx0bfCxLYP7rNwp2vyAa2VFxp_cGOoltaiEaEolPYp2RO3bKKuDcm11SCr1P-0eLxZ2PJpQdYX5bCIxgE8BuzQBNg96iAvjSYPZ05GLOzHEbuuljCKmSOzxUN_NrfVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXLmRVNI1e4yD6QgEEYvaMFYJ4RW6h7YooA2m30BI6rr64AKUt8uIquhIK-nJqSeu01pDLOnWcQENfxF2wlHMRPzA_feEpXbboamcGff-373FH7RrTm387iB1zUxCyP3XwNit6wkkrnBqFFWCYE64OfVfbKM5ZUm7d2Cl5e6j7sxhuVMYgjXbb3GRd3nDDDWtnTIyOiEGXqCuiEFKOx5D5u3CBiDi4brOCLQn52XiOh7pkGnyc4l76yEPegRUIhdVA1ErQtZiZdCLUzSUwaEW7166t3PtEQVRGLIN65xuwhj4iglRX_ZI-nxfKpTq-6uTy9XQt6CetoOIPs54wkdQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=eaDmQCCrtbzEqnXhVUO2tK3nrBDxQm8NBfadh0DbhI2-bolWFfuY4W5GaanlTXP8V70UjYq7zplDQtOnSPTooEk2aXr9F22IrZ-2H2ucuI5t3iPa9CAagvRsv_tYpSNFon6j_8S0K4RiC_KJJjmi9Cx9fv2XhRFAXz7frFDvqROcAqYMVfp2PFlIc1ZWZ3qCqMjCuIKNp9HmC2C1SSpLKA5OxdTgKw22X-dOEMmmUam3YZKeqS0yMg22Rx9zkGfNOC7Rq0odTBrUqDrLZOnb63XlwdmyFr6JpS7pmPE_4AyG3PqZIEFzyTWsZT6pcqe_gnAAUq9TJhjZvMFk4uXRzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=eaDmQCCrtbzEqnXhVUO2tK3nrBDxQm8NBfadh0DbhI2-bolWFfuY4W5GaanlTXP8V70UjYq7zplDQtOnSPTooEk2aXr9F22IrZ-2H2ucuI5t3iPa9CAagvRsv_tYpSNFon6j_8S0K4RiC_KJJjmi9Cx9fv2XhRFAXz7frFDvqROcAqYMVfp2PFlIc1ZWZ3qCqMjCuIKNp9HmC2C1SSpLKA5OxdTgKw22X-dOEMmmUam3YZKeqS0yMg22Rx9zkGfNOC7Rq0odTBrUqDrLZOnb63XlwdmyFr6JpS7pmPE_4AyG3PqZIEFzyTWsZT6pcqe_gnAAUq9TJhjZvMFk4uXRzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHwhkuTVvOmQdRbcU8jslqPYmVPNlkzJZnJuCVqIBQRznsBsqDfDFWn45o44x5uaJTBcsiP2VPoMIWovT2QzrX22cnxnM2TLyyfbVKk0UEpTPspbE3LCRlrk9o-IWJxMwsqYw_QEfsIEjeBXDRIdcJu29_7FIfL9hsUi59tuKrOO80MDJ7IQ82P-BIkQxh3BcED_hTH4FmK_72J5xlfrJGxZ-jjc8Z8GjZx1n4uVTifbDRhbgMTUjcYz0yV4vppaZ2Xjs-H-2s3D_8DXSMG8lqWK9fW2qxOrM5BS-PTlyxdyZVeW0KYzsgn6H_8ZSsBWHmOWx95jlmrcHDvWMRl19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=nkcm9Hq6-loe_soWe9jubAucMICoM7NiOjRJTRPcZiIpXOmVZPIxfBZapZw5kYLCCC7bQaYDroGCVxkAuJ9ATvTamvhGF5X6kGzZsR59b4vkijI7DovAnDdUXEzo9XHugSbnovbfodRSHE_GeY57uO2tO9wHL2m4FVYVUfzy2kWLDmsMqpITWG4_y-WqADV--lLdnxxXTJOHSAABW_Qq6Ggk_PuyvJL08ZsG-Cc5eWTWtFgpG9ZjXKegdEzcitmKQRA46mOfw8I_cgD4NLbLm1hdyH7cTDWy149771sfDRbnXIjBUw9e6q1ncWbS25X6V3FOHM8whe9LsBdVzZ6_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=nkcm9Hq6-loe_soWe9jubAucMICoM7NiOjRJTRPcZiIpXOmVZPIxfBZapZw5kYLCCC7bQaYDroGCVxkAuJ9ATvTamvhGF5X6kGzZsR59b4vkijI7DovAnDdUXEzo9XHugSbnovbfodRSHE_GeY57uO2tO9wHL2m4FVYVUfzy2kWLDmsMqpITWG4_y-WqADV--lLdnxxXTJOHSAABW_Qq6Ggk_PuyvJL08ZsG-Cc5eWTWtFgpG9ZjXKegdEzcitmKQRA46mOfw8I_cgD4NLbLm1hdyH7cTDWy149771sfDRbnXIjBUw9e6q1ncWbS25X6V3FOHM8whe9LsBdVzZ6_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljG_rdTwNPwjm01pFwJtEZLKH9WigOar_AOrneGFjK6mYqs8Lzz0y-emwDr6DK7lwjPkx_9tq2ECIad5PDEoeJUMa6rgdF18SEQI669gEvn5PcmAsI8vVaubL0LuDPUUQRWeTd85Ht5XRKo4XsM4yG3YCBG_ukPpbeluwAkBXjMrRtTa0qDJSVe8cuNuSokMlqa8Yvacnz4OCQE4y7syUHrzo6AN8ZF1To_dUKPutHIqtxgk38nl0bzGF9mIYUYQ5fyzcEEmpveMNwb0vdHi9QH9zD2MvSNXMNbxvPM2q37JmWgFh8O_fu-pw2v5eR1xapxrlieM9ZaOqkIRPKhUxQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGpl1ag9pQOm4P2_4fnvgfpOS8nvzFShYC94hgZhFMeC4bfm_UoO2YfrjoblY1YsZqbpyK6byXeRWF8JdVY5KiC6YrbaA8o5q4ii1msEfXU2k-GT9oeHqa3es8c_AFBKYf-z9geuHtooKESqMaw1g8cB91NP3UgeFpR_eM_Q-HIJdy4ZLu7zpNIPGfW8PLBgzNtzku48ZiHcKa5A9W_Kb1zBGQww9VFQS7YNlZnn7mJxQAgcfJoXZoyFZxgX5TYdrFmDNVMANRHSS7OZV5QZIU7sz5qbP6etTH_wSiKz93uh8H0_OH_ryCODrT6YDZwXnHlJ0SB_BeQt7o-lfPA7B10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGpl1ag9pQOm4P2_4fnvgfpOS8nvzFShYC94hgZhFMeC4bfm_UoO2YfrjoblY1YsZqbpyK6byXeRWF8JdVY5KiC6YrbaA8o5q4ii1msEfXU2k-GT9oeHqa3es8c_AFBKYf-z9geuHtooKESqMaw1g8cB91NP3UgeFpR_eM_Q-HIJdy4ZLu7zpNIPGfW8PLBgzNtzku48ZiHcKa5A9W_Kb1zBGQww9VFQS7YNlZnn7mJxQAgcfJoXZoyFZxgX5TYdrFmDNVMANRHSS7OZV5QZIU7sz5qbP6etTH_wSiKz93uh8H0_OH_ryCODrT6YDZwXnHlJ0SB_BeQt7o-lfPA7B10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=UZ2YigmkMGRCqmgccvHs_kBAJGLEaFxN8as5bHRdNO5YGv3-za7156JGHkxHZf27FfvvLIeIkv99d094OnMIGowLKU9AAOzMK55uYsACl1woyQsqDjVu5T_ipPO0xIgRPvgf_e7PPNPP-CZnzOBDh8hR4zS-iRxHwqX5B4-jLyCULmRkJFOHN47z6rR8SqVtREpVYkvoIAq9FJyAH25ELiPVnjP3OFkTnmJqR7ylb0CQpl6Sn_1iS7Vnj1_uSZmcM1GIAaT2bg5qD-oG-3IjpkqQwMDq5zlgohd-lHN8B75MddVpdM7x8ZXjI8yJOBzr_8HJxeTk44rhC1iD78j_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=UZ2YigmkMGRCqmgccvHs_kBAJGLEaFxN8as5bHRdNO5YGv3-za7156JGHkxHZf27FfvvLIeIkv99d094OnMIGowLKU9AAOzMK55uYsACl1woyQsqDjVu5T_ipPO0xIgRPvgf_e7PPNPP-CZnzOBDh8hR4zS-iRxHwqX5B4-jLyCULmRkJFOHN47z6rR8SqVtREpVYkvoIAq9FJyAH25ELiPVnjP3OFkTnmJqR7ylb0CQpl6Sn_1iS7Vnj1_uSZmcM1GIAaT2bg5qD-oG-3IjpkqQwMDq5zlgohd-lHN8B75MddVpdM7x8ZXjI8yJOBzr_8HJxeTk44rhC1iD78j_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbLd1hLxHuO5MMGhng-oAnWu71F0KpZVCP0J4aqQs37YgU1lFTddNaXNVWu6NZPC-7mNwOzHR84DY9rKFb7WMINMTXKNzOxaw2AhQkxLWAOt0Vui-BXOWdHWn0nVLDYgPLjPN8PqR4slaB3uWZBJDY5eQ0atbiLXALTjfzQCxQ1NoIt7xRjgN4CEjn33bzF_O6W2CbYDpwaIlqcTxai152XHbFjfeJKQGuZ7hq392FZKLeFyafY68Xe9hTxTi1wi21MHHUEeFAMFvcS5P1X5tqs8IHcHdru7DXaeuNfbEDjEg99di3gl1gi9tlET0MRyFv5jdUL3R_jzGWX_gL70yCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbLd1hLxHuO5MMGhng-oAnWu71F0KpZVCP0J4aqQs37YgU1lFTddNaXNVWu6NZPC-7mNwOzHR84DY9rKFb7WMINMTXKNzOxaw2AhQkxLWAOt0Vui-BXOWdHWn0nVLDYgPLjPN8PqR4slaB3uWZBJDY5eQ0atbiLXALTjfzQCxQ1NoIt7xRjgN4CEjn33bzF_O6W2CbYDpwaIlqcTxai152XHbFjfeJKQGuZ7hq392FZKLeFyafY68Xe9hTxTi1wi21MHHUEeFAMFvcS5P1X5tqs8IHcHdru7DXaeuNfbEDjEg99di3gl1gi9tlET0MRyFv5jdUL3R_jzGWX_gL70yCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hun2Nk3WDmF_b4-JQG8viOmIM_GTCtU6aHxuzoh18EYBvTi-RnTLbLSz-6TpsCfcaJch2xJnXgpJrXZ7D0MOI4pN-WqsEvKI_eIhYZtwi-CL5ys5ehHvettDKiKkiKKHu1W7IdIFPGVSD9V48dKj3R4f9bfZp3HjphWIdbMM7BtWNUr55PCft-qEyT7sxCWCSNIsmhcs7g4BQ-NgWe4oHFnwffxmWRIqqPOnau8cmTkAWCaC5AO2g4L2c8_muFcdQbz8zysdOi-qAbGLDv_Ba7R1YTcr5TYsNG19fqIqXsMxtcoqoKcfwAQfVdVufMqmMJwpY_-d9Dv4F9mnpAMgPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIKLngg27mjWOrc2fdODD2oa0L0IhAJifhOAeZ8ekelVKeim44LYIM5z7xtdJlAljdUyGDtiftK8z69zk1ZyW4TuAAub-S1zY2kZbi3UhUp6M-El6B1MserUF0FU7zlJ8tvHbt4IfgkAOk1da406K7S8HpkNCLCaC2XDtxA5g57nFHBvGEbWIigwkKALDYpk5reau_PWPyuwnlQMANq1210NedgXFsX4p1b5jfC8BxObLldikuRZammW9wXmSbz9MMqU2os_VaEkPDL2s4v_GLC8egbrRa8VCMkb8ysadjvC_wIcHOtUDYwx2LHuDKu3TmD0A4RAtrjJ9D_O6rMCIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5cyVyY0QxvpA7Sf5zZPtDGVnWfLrAh882DEGczC7PRW-QBrAVxtiYJQJbA4S-IbT7Niie1tUPk31lJCmMTwFxT4_CJAfBlis7K--6fnZLast9s4jYGxhVmV63E90pLdrdQiwVRDN-7smt3n1FelnXF-Z4LHBOGrrMhe8CwvwtgyV7E0BTT5QKUMk-RG0lXtq2rJhKlvXTaLRrFZiTCDbCM2k2ReWdfGa72SW502DoxWdkr18wc3-kPLGcLFqWemrMN9wnDy94SHOq-0mC3DPUg2JbYq3Br-Yc7Qh14J3NI1OvfgfykLhxDHHDTZI2cpBieBJGlSzhCWdk_PNBE0Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyE806uAvyp99nHqF2cpLqBAkXE7PUjC-wiAH_Lsey0e0bKcV6dAZzEPLi_HMxgJotxvWefxuYbvr0VWEZMimo09kH4BdYVM82Qgq3E6Ji8i3Ct4gBT0LG9y31qGyTDLOvoRKAYnclu6Xv0gPs1EhceEUpQf_jCyQ-SqHxCEU9K0lxN2wMLYwGPjqlIaTxPiqK2RcM_Rgp3GCuzolO-cg27FGD2XRKWtLQm40exZHylWxgRrGkfrk88KbrMHkEserPTJWLiuBXqxqeNsgpo82XPifbLvY3d3BJbg29Qq7PSQL016HLlLMAJpshtG3cqzEyhLRjYMN3mkYm1e2UGQQA.jpg" alt="photo" loading="lazy"/></div>
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
