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
<img src="https://cdn4.telesco.pe/file/fK0MYDSoSWZ-TymrWo9Q_SS-a8_1hBXJtXZ-9rBexyPzmuLj4BlAUOeSuJH-neyBqxGgskQMU3Ff7utuCDaMchqOFXmRkuvU8gPczLmRfU7TVSGXBY4lixzRtegFewBiBn-XBIE6eKHHWTPXYccfS9lgM5z70GazGURpBXuqjGxvIdz4gEbyHg1DuNB3eGQmem7rvi0eUUeFBXd6_aeEEFHvtYGtfaYGJFSKRgcphagevrLii5A50u9_lT-oVWKUQ6ZAPruzMiwgfbYkSbwC-bLHbZCPtCvW8WW0mprsMhMwHlMN5tsrIHw3xDsQxdeQrahi8bvt65OiRRe77hdPzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 03:12:52</div>
<hr>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDtoBUvfbJ39Au6Rk7tUBj9xJ1WgC6OgSfdQSiRnwNGDwSBoONWMcOe1ZlQAla89lDB6FNpY-f_wBhzo6Q6nLf4yJEWylk261ngT6lX5NylvC6mX68GF89KvhwgY1AgEotYB6uEa2pcW4AOr2qNNzn0nHgWZJLJ75L5gf7DdEyTzUtbm1hbs790jqOZIcNCTFxDmjd57fVqY7SYfspdOd0bo2wrnXlM_g9vxRRpkRgNIHoAa58OrtRmIua6lyHrqMvvL-s7eER0o6qemgITrgMwEJrIcr8HewfAhL4qlUOsN-eZ04KvgcjOSTZO5XVZ8QVw1Lj4fqOM31dNrlpuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwk0MF1CymWQNvBspQ8qRvgCbc9OMnrwCCLvSSTmnNZG7h63TSeiBWtiMjICz44yaJh8FcDCbzEZAQrmBV-uZwz5BLiYRSq8gMvbZtzFABq742ir3Fnz48EBeSeG-EPf6pVH32S5ObLKiOmWTCPNl1wuKN6B2T09g9Q7bfvv-G-lBTFyukyL9TxmjkYB6TwNTMVSXGFJcYhgHAysEy799dAyianAAZdGsNOyLQVXCKCuthOA4kdvPxzKbtTCbGn_MFVUHfjstJ8fsr3VUoNl5ywPXjJRTMk_QEj_zesVne1WPthz_tBI_0fIXMMiubnDq-1X9wrTkke9IXGEUrNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge21nCCb68rC7OiRrhNXHZSaBmAekuVYVy-oHMedOGNqVdINDTM8aFLq9Q5Sfg9-BHiDMC7fdCHNH6Pk-pOmRJBvFbjAR_821w9FgnxgRR7-wNblk7yMN9ITc5kBIXUp4JQkv0Df_QRg7BI_mNI8IaM_foIeG5uLsAe-30y-hc71Q9m9N9VhLHULsHF2QRuULbeKlJKyfxrJhRS8JtAc7qWVZo1Usgqo4A85HY1nL8JYedcRvIN3lKJmtNoGJ8CZ2RqScQ8rpBVr0043Q5AdQtycLWZuzlI6pyXj2bh4BN3qdWy6fNTvEjRqtlirnEL9AN9xy8uHpJb1XqJ3Bsk_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1yROZXme7Jz6MtSMEqF4mPW8kOyrF5aUfl_HVrjGe-aAeWHwevXJg1d9SVFSNX68uFGRZtUi4jZ4gJLsQlk4pOXZvAto_t9O_1OUmAzvNQdAjQ2eqWCLpr1xch1XfxphnfNW51M6juJNm3k-ZOZg3xEtd6pkR9K-ez70RygzFa9cEH52a8j0IE4a8aDjO62-PACGl2FC2OH6KL8i3RuhGPAElT_AiD084WxsO3eUP4ynlXu0CBcn-Z73S9vO0bE33MKxK_BR33f6rz952x5EuQ3quYAoOJ9ipRCTeSplkDSSmmKYelZWbaOSU2YJngrqFiFN0E16Q-vdQvVkn3dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=phWqKZ9s_DOO1EVHJkH_5pDZXVbbmYOaL2EAftiA78VA3EiCbtXZV8tIPFdz1Si5bvJFAiIbX6KcbMlq6UsN_Xj1WiYvbmtl3IshjQNwxRHmiYCJz-1d9xOwkmxzBlYCtxdPtR78vSvBFjF8AyNrLA0fh4wCgl5CjxKb__6RlksFPsuf7-rRR8jgxvm3nRdoUV536HkdTbR9fyVpNTBLpwQazrGaRMzJxmZIeJglS46BLli2wOwznEPXEmkv0F0BPpYyPCcr3TkoJG5frUvpdYtbHYyiQWpFpxz_vQnYVOacUMaxdkLSVDpNcOSSFz5iZigXViM0CxsRrOwr9eQwfKdmbX-N0Xiz6yQCCh1RqQ9JNpS3mP1GW600AJCi3lfhuaHzVKe3Cj3Nkwmp6PTHZneEcuw11UWYGBgHHsWZIBEMTW01IztpsIoRNH-XHhA4wRdvJp6cMQ_D9Lp_54cSlykoO_TkY0UFLCMk_7PvbN5kCHiQPVagUItinkrJxEDtsBr0g2WAoEW_VWy2cEkIsfKDBF385e4DP4SVs_smn5BepGpaqISDYPvUpoyckVPuOO58V07zTIpFkWVRtF3UVonyumARmWlrq-zeCYBBte2eaMD5nQVVCCRTtX5TLj5ftgaF7eONxrAU3m5c3SqhyjvsZlfmlIm8Eh6pn-4fmmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=phWqKZ9s_DOO1EVHJkH_5pDZXVbbmYOaL2EAftiA78VA3EiCbtXZV8tIPFdz1Si5bvJFAiIbX6KcbMlq6UsN_Xj1WiYvbmtl3IshjQNwxRHmiYCJz-1d9xOwkmxzBlYCtxdPtR78vSvBFjF8AyNrLA0fh4wCgl5CjxKb__6RlksFPsuf7-rRR8jgxvm3nRdoUV536HkdTbR9fyVpNTBLpwQazrGaRMzJxmZIeJglS46BLli2wOwznEPXEmkv0F0BPpYyPCcr3TkoJG5frUvpdYtbHYyiQWpFpxz_vQnYVOacUMaxdkLSVDpNcOSSFz5iZigXViM0CxsRrOwr9eQwfKdmbX-N0Xiz6yQCCh1RqQ9JNpS3mP1GW600AJCi3lfhuaHzVKe3Cj3Nkwmp6PTHZneEcuw11UWYGBgHHsWZIBEMTW01IztpsIoRNH-XHhA4wRdvJp6cMQ_D9Lp_54cSlykoO_TkY0UFLCMk_7PvbN5kCHiQPVagUItinkrJxEDtsBr0g2WAoEW_VWy2cEkIsfKDBF385e4DP4SVs_smn5BepGpaqISDYPvUpoyckVPuOO58V07zTIpFkWVRtF3UVonyumARmWlrq-zeCYBBte2eaMD5nQVVCCRTtX5TLj5ftgaF7eONxrAU3m5c3SqhyjvsZlfmlIm8Eh6pn-4fmmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufUxOfeE0NJD3nZuRRpcvs5MSY6qeWocVAClBdF6L9jtlnyVuuiY40Lt3euipA1bNwAYiFD4Yf5v_Pb-LM9p6F2OEj0SybfXvbwmv4XR_PhT6RP-4c5MwbTfGVPXWLybx2jOlBhU-FEwQUjlt7416WYL7GV16ZC4GCklDPhsZxo3UcAmSXg0gUmsuBZJx95uKMt8nkZ3VbE4FdZdfvY-ofjkpomn3dIVf75zBsbUAYmNdiNZfa17TVLD9HNcZoAlV2S9gda2Nsy7Mmi2sSbkQSRz5pp4_KuRtzwUo6zLHV6zcNWmsL0_p793IbxkldA463TxFC0ihkO2IvoDyO_UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-fadso-ziuEO0QUUQtof1oEqVhB3Yumjn5Ut1_ZCQghERLw3OE3oOvjqNRoJAxHr976Hj9gfnbra71EwzIIjG-vDspimbdqF-kLhDrGX7is3se9Jx8evGm3E33t5QGqcG90cEdCM6J5y9gXgKGogDxrIEJtpGyD7pucgJ-Iskm2_xhhBVcnAuDHkqcjqRcdSwxLaEpuv3dE2HW3QgfuFgbWUC8F_wCm-OwqSL5SJRUrJCYawKIdCDKBd86XFPfM9qo3OR-ZP11v30FRCPpm5fmiWva98xR36QXrX__jI3qefGFP3faWaNGuHnMnOikRrJH60hcfIz9Vzyu4NPvo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh2IkRxGq-6-ePdNopCx9gJoqznIHYG-NCBtM75dT4d5RfDGkwdOJPtujB5oAcHN1Co5d1kemYAqd57w0oWlRRm90GBI39cHEF6De1gpt-MUc-Cr8LQlRnsularkYU1_ggigPOPsDWGtLqT5hBmmsCDgmhARfd9CAd3BfYLnAUF245d2UhUiT41V16gE7T-tioKPGGDm8NsBY1RBPLRFVVUG9PHCihsiqEV757SuzB1CWZgMBUkv2HOVvWhaEpkC9-Nca1Lcz_ZEiSpmB5i9O4DAmej5Il8OfYy7ikP1d0zb945PE3MtVEnIoyM610kXFK0LtsIt9_cI9yzH_NX9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADhGvSk7Fa91SjlTEgE3dFZpaSBPeDKZ7OOk4NsqQo_GiexsJol8DNcaCXWV98pWVc3OA1coR0XW2iWUg0tFQEU3cBEJJ3iXWnrc_Zy0ZsY1WXU2DtBuphZtC6H-9BADALq4XVGK3aV1goHYQ7LdW_7MPEkv1xCgpRifUPuD2HvF0MIp7Nh7FcFZQVqVRtTNM7kEfrJr1f3t-KHJqtdtWYoxNjJ3dIDBaAgwl2oPnmxl7aJxAzAXn9RZKdwGaZdTnQtsOROcVRyIe9hugfoNeV3RBVuW5laM6AWewEGYkLmUAYathyC1BYY4t4S6Sjzxgtcp_fv_pGQlZ4piqYhLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPERQqJURuUFa7lblYV09ezS0jugDgY-vyaLAblxb5ZDEvBIMB8GgWFKsPT1W8RE7gExd_9ep7ZuZhU_BqsUTqx27cDdougOgTT5rPBcVMO2wMYznOVY2JXM53cNkMw0_ahwEmXdDGVUCs-xuBNvmNHcT71XrtGbv8OIuisGwiCUFV14AHJS4RGRU1jfdivfksXzYbSl14jUsBXukoKnaU7HfMQ7sH7T-GtQJh1QAZWbsFCZcm6IE0T7lxc2bNsRMk04l8m20qdO0EumiTNKKyiVybG5O2og2DeeqqL9QfZxmQck1Fkx61CptlB9Ick7o4jSqRCU_bLBY8IU2L_Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3HgqRhKTTGIVodgzsxFkJCmFBswfl8b6NLFsDMB7DoicgKkCHzNUd2-tJHpW5OmGDOnNCAvXLWnlhtMOjUQ_hzhBYXXiBSkyLnDY38u6dQNh7f8zfkkyyC2BWfOGsOymJ0XViancXGNUiOrii5FBPf9rVD4LLyX4zo5XKQa_5RXeNZNPp3TULcAJK5RY3MtFv2TdEQWHVBVnrL-o9AFa9GxlQKpOc9K6u221u8p-1wg_TTmcI8Kic8E5d8OztDUkrv2BF5mlNqT5bCyl2GAayNdX8ijaTt7rPAKnKrzTLx5M1NwA-G4JtNSsrQ0-XH2ZreFoQ0Z1X0HCVPhWNM27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pkN7g1Xn-3kj3vv4QmtNL4KcNbSPFwd7pvWMgLD2bXQogdgkHIRvKfoTNwcPL33SNKYyuwJeMKs2h2qOTaXR01Q9rVIP0WWh0_hhtEKnM9erw2LmY6u9cbMqghIA1SyDibDF1EbEpXK62gJFVvjdb0MU7mhoT_-7M9qhEuAlLCt7T83ozHxwDjLhbu3MpY0CZupmNZBl1ke8uMNGuBDGTNzZnMq2pfCIc5F5ysyPXYTA2kJN5EKW5Z3mNmY5juzDiuaNc39OXmD5n9EmQkEj54oU49C_I7ZQlFzqXEaQgMWM0LpKcK8oJwF6nniPJVwCeUBv3_H0sf23NZucaSQr5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pkN7g1Xn-3kj3vv4QmtNL4KcNbSPFwd7pvWMgLD2bXQogdgkHIRvKfoTNwcPL33SNKYyuwJeMKs2h2qOTaXR01Q9rVIP0WWh0_hhtEKnM9erw2LmY6u9cbMqghIA1SyDibDF1EbEpXK62gJFVvjdb0MU7mhoT_-7M9qhEuAlLCt7T83ozHxwDjLhbu3MpY0CZupmNZBl1ke8uMNGuBDGTNzZnMq2pfCIc5F5ysyPXYTA2kJN5EKW5Z3mNmY5juzDiuaNc39OXmD5n9EmQkEj54oU49C_I7ZQlFzqXEaQgMWM0LpKcK8oJwF6nniPJVwCeUBv3_H0sf23NZucaSQr5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=tm0264_w1BAUbo648Zk8WTadMT9wNDPQrV8Ka90PPD0Na8gi7st8yoJR-uoclLPX3QkThtYMouPeXs_h6eZg4WTwLuIg7uXzMY5ft1M1ttChrlWayiuVwVDd7jPpwrZplRL9RrYcYKdrkYo6Iy9QMfKzUqEx55aOv0AmBnau1YC1ZRW7q3LDvcEmw96lWvbeO-Fn04yLrhG8rfiT476ch1fGK5Pm9giuZ6XhiuJUJcecfQZVhE1C8RpB9x9ECVIJ16QspuCvrHARIV4TTCdnBEv3_B4SSvKiyE_j7A8fBLiyR0QamFp2-Yi_jiiXQk4WOALjILhbSk74LLMkPWLj7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=tm0264_w1BAUbo648Zk8WTadMT9wNDPQrV8Ka90PPD0Na8gi7st8yoJR-uoclLPX3QkThtYMouPeXs_h6eZg4WTwLuIg7uXzMY5ft1M1ttChrlWayiuVwVDd7jPpwrZplRL9RrYcYKdrkYo6Iy9QMfKzUqEx55aOv0AmBnau1YC1ZRW7q3LDvcEmw96lWvbeO-Fn04yLrhG8rfiT476ch1fGK5Pm9giuZ6XhiuJUJcecfQZVhE1C8RpB9x9ECVIJ16QspuCvrHARIV4TTCdnBEv3_B4SSvKiyE_j7A8fBLiyR0QamFp2-Yi_jiiXQk4WOALjILhbSk74LLMkPWLj7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gq5sU_RbfRlQiQQkVY3YMkKncKj42RNHF9Zjdt-j_lvG9xnezWrXbM3gyylBszz0joCpUUFrw0ggrTtVpIjHnwpzEL8r01XewmN02VzCeVz5eXtcKOP5FZXgqIeTlru6HnLuoIqu56T8EWJlS9IizFrkHb7Nqtqe_jGSBI17YV-CI78RofsCsV78iSznoqkmRka_LP-UT1XY4xDYG3tKCBTNVDBg45weMBVt-VEN3eUEV_pO7k-6MJlTzR4yx3G7PlpQVuibCUI-FCBYkUogUZc18g5SlIzoCRySQNdo7RBbAKjsqg45aTZqbngf8C4TGxCq38yEyAu_-2S3w9Z4BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gq5sU_RbfRlQiQQkVY3YMkKncKj42RNHF9Zjdt-j_lvG9xnezWrXbM3gyylBszz0joCpUUFrw0ggrTtVpIjHnwpzEL8r01XewmN02VzCeVz5eXtcKOP5FZXgqIeTlru6HnLuoIqu56T8EWJlS9IizFrkHb7Nqtqe_jGSBI17YV-CI78RofsCsV78iSznoqkmRka_LP-UT1XY4xDYG3tKCBTNVDBg45weMBVt-VEN3eUEV_pO7k-6MJlTzR4yx3G7PlpQVuibCUI-FCBYkUogUZc18g5SlIzoCRySQNdo7RBbAKjsqg45aTZqbngf8C4TGxCq38yEyAu_-2S3w9Z4BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=iUvcxtrGq3bZsGbc3IGLQRW_7dxJMcujl7ke2Bk_8vkH1fpcr_JNbwnp9eqHAHwnOBBfcdZ4KdZdqFmX53GSqvk13JqXDWDO2b3fRZ3E8o6GyoqisWBrH02jn6WHj8VqswdtVsWx0mIZ_xsPGabEEVMYuPN7iQQ-uu5mOmFvkS5MtUghjf27vViiLD1a8sYtRORkpJenEXq4MX0BISfZSpvzFiZTDtbYW0foMr6yku3qKj3Es88ozxisx3n7y3S32qOIwfpkPReexbWivJ5JvamexaZGkHNCepknsnJOWE_G988Lvyd--1IzJMz7WP3NhZpwH_OhSEAkVGexKCTjUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=iUvcxtrGq3bZsGbc3IGLQRW_7dxJMcujl7ke2Bk_8vkH1fpcr_JNbwnp9eqHAHwnOBBfcdZ4KdZdqFmX53GSqvk13JqXDWDO2b3fRZ3E8o6GyoqisWBrH02jn6WHj8VqswdtVsWx0mIZ_xsPGabEEVMYuPN7iQQ-uu5mOmFvkS5MtUghjf27vViiLD1a8sYtRORkpJenEXq4MX0BISfZSpvzFiZTDtbYW0foMr6yku3qKj3Es88ozxisx3n7y3S32qOIwfpkPReexbWivJ5JvamexaZGkHNCepknsnJOWE_G988Lvyd--1IzJMz7WP3NhZpwH_OhSEAkVGexKCTjUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=n8tXL_S8FsEK4QnMALkKn6Ph-xO2nB_TLb-wZMi4Gvcqtm3kvXx5Mm2eHpUYNoV0rAHa-y3EcnCR-Ei-lO2k8NiY2NrV_ESXM4FjoP9hRInF8ITfwAaN3N24pIh3s3hjXiEJAuLNU9gQg2zCqe6WUaUupfctVBD6oAaqFfzb6Za99V9bqB4ilgQ6RQ1_MOd1NEKlbHYLGt2B8xC4xzS_nQZRLwP2eqkvFoD_MplRBNvyHG6rSgisymqDkmrlkVqLd1QEbt388cqP_eah9cHSaJvI_bu1wUFdyZchEgntRQ7shnWN6qIHB683aDbvroFaY2bSdR1WhMGYYU_-7CDh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=n8tXL_S8FsEK4QnMALkKn6Ph-xO2nB_TLb-wZMi4Gvcqtm3kvXx5Mm2eHpUYNoV0rAHa-y3EcnCR-Ei-lO2k8NiY2NrV_ESXM4FjoP9hRInF8ITfwAaN3N24pIh3s3hjXiEJAuLNU9gQg2zCqe6WUaUupfctVBD6oAaqFfzb6Za99V9bqB4ilgQ6RQ1_MOd1NEKlbHYLGt2B8xC4xzS_nQZRLwP2eqkvFoD_MplRBNvyHG6rSgisymqDkmrlkVqLd1QEbt388cqP_eah9cHSaJvI_bu1wUFdyZchEgntRQ7shnWN6qIHB683aDbvroFaY2bSdR1WhMGYYU_-7CDh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9prpaEYgiAoEi4NYfVurtcr1sbXUWf2wI293cLdfGQMeOFmTvNN1Th13Me6Y1vO3dDFknDbL9BXJIh8hzJ4jNomdvlbrVKH30llYw_YEwd2v3h9Dwprh2CVwOoYjhyHdzJC-0P6bFSXgTkAuGB4JC0NA4VscLzLhfLttUsylejJYld1gAO19uEGz6Y9lQqkqBV2YSi_ZiElFgdwtio4b6ZEmYOcuGkVVNNGbiTw2VwlBqOGPB3ilUyyb_b9FPKlzjUsYVOggj6UxipvPLr4Mb9_prPJt7FWMwvSfRDRXuq8ghZa0kqqxM28WrFtRJ8L8DElXwcmiX40XntrZuT8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLA0T3sHXBbUcCvs9dpE2AVqw9L9zGYNUP00TmTSG2cIdIqkx47JEpgthWiTJxdEAfe2QV3vvpRK1H_zeJQkIq3YSHLqPyZh3WbDD4ySIYMlR4z6NZiF82iI9rAgT9C7KLRnzMdmvy5SxnL0XSQ3i-FQFGV_Y1HM7chT95jbqDQwCCgOPT7sAx0pGdsDE85Nsx710M-Sw_KhN0KVvCnZMGkhjBoJz5C1aCfbxubvaJUZMtBAQg2mVZ9SWI1YJWuqSTRr3QROoLoUlSb7BiyoMtVeqaiHTqDsPCDDmpPZyxavfEiUjUFJwgnsbcgbX_IAVw8co7sZQbYWQRfNr9yNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6E921P7SOwJAoyBcFz2q3DoJMdG7ziXgWOnNo-ez3g-kPcpi7EYeyp88NJ-F5wyPciF-sj8AKLc46I-b2MR38jJBCnZgEHoP0a30jFjFFot6KzNAtiuTB9HHWj70iQtM1ON_Z3MlV7sTX-xj9Fky3HP3DXMgdhkUkltUHCm9nep3OP3qd-QPEyxn2XtaydZJeDdbd-eMhyKb85uCSrANu3INlMDrE6hmpNw8LrhQ440DzzIAaSDyHUSXppuheihHvugYNS0JfQiGOKqvPsVd0QIc4Jx1HrfddMFZspr9ShgBm9HdmhvNuYVSKtmSZ-jjcE0OOoZDNkw1G-_lHQWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=lg_dNSTClU_MUW9VYLM4TamzBM03Wl3dVXgv1RHEscwkjBaNiynssr-5bPSxruUzcQJIMrggV2bWro2OD8a2EYK8zFPgA0JzETJVhbqZbJxYIPSZ5RAtDS3G2Eoc6FXoB8J1i3pa4ou1bBSq2tMPivvnyaC2aHB6yZTxO9bcC-vPV-2Mr1I62wVjiIjaKHHD9QfHxF7aWOr-i8MOzqYu4NR_5HOc1z1GFF_koKe_ujphyl1xoyVw7oUaHL1rSHpTk6c-VVCfRw5XHCCeXNi_bLruQ3ptd6g1dlV9idaONT7RBvBUFNbOjmrlJe9VlCSJAjlA1J8TaShk6s5qbZSMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=lg_dNSTClU_MUW9VYLM4TamzBM03Wl3dVXgv1RHEscwkjBaNiynssr-5bPSxruUzcQJIMrggV2bWro2OD8a2EYK8zFPgA0JzETJVhbqZbJxYIPSZ5RAtDS3G2Eoc6FXoB8J1i3pa4ou1bBSq2tMPivvnyaC2aHB6yZTxO9bcC-vPV-2Mr1I62wVjiIjaKHHD9QfHxF7aWOr-i8MOzqYu4NR_5HOc1z1GFF_koKe_ujphyl1xoyVw7oUaHL1rSHpTk6c-VVCfRw5XHCCeXNi_bLruQ3ptd6g1dlV9idaONT7RBvBUFNbOjmrlJe9VlCSJAjlA1J8TaShk6s5qbZSMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuaXYGCVmzSoLiVfc2jgbSNDAn8O1uXCCyV-A1uzMVLsRTXM1AB78-waj8aGGfVUi2hMcO-7Ff4NlbD2VcPSKqM9brYsdlhR6eTq5g95tPHA8DpeEYZOlQaKKLQcE3HsXRDpxp9q0WB8tHZlHrfPDF7Q2nAjhyh4Kgp4TK3rNvKK6IyJggEQ8n01rAerkvOjj9VqwSnEVuWz73mzrz765vaUPI_OEPtg1i4p45aqcrs4S6phWsqjRI4D1wXbjQGrx1jjeuzV8a54MO3Bk96IIUrdyQIXh9WNd51S8aC99Qyu-pGC1yubTRMkTO9jmVVeYkauDe9lT53zusjLcO7IaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsbRXz2BJ-Ho1HmlOuJD8tIoYKZIjCXXa9Ls0KWoTmPagCvxBU-ZSyqe9uA3wvu7b-8zoBFMiHqg3dJMEfzzvOln-U5Q_QY631TsKpxowEEEWxVJ_vY6lneOhqyl26kIlzX4G8JBPXIax5Yr7rxOoP5gKdxZ7CuDJ1GMHB44o2vDmRtTpLfYHvt-N9sE17MYoOCAL-0b1cJQdwCilEWZ1kqrFD5rEkGKnnaxOX6IN_0XNJfLq0EULPtf_NQJqMsEX9U_Ot80WT9cxO94eshnvJPNX5Ijk5UIfIJ3DT5FEHLfx4i20AxVBUaWrmgqKafDuiMWlgkt_aY3roLkcsV9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGv3qGtuKORzHcxUiJCIxnR2-tVx6DjhgAqZrw7C3RO-JZY2CCne1HLHS0WfFOJkIgXTjuM76jKonkK1aIpwMNzkO8PaBfRjo3ECdx8GihkdFQe9_dPLkjRXS85M1c99ZR5smMY7AUqI0WyhNgKZGCAmZmZpg2IAhUmD7rmJeBWk3dmgS9GlKNCN3-96hOqoVLJaZp90ouZXiBHoCDcuqOJXnRR8fIbKh3YY-WI59dkX_naP0bxfaI5MTLRgdI9kbKjc5BOEIXGCt6-fn-2VveRfOrqDxxgDUBUnm9SbkAjc69bQoORE8vF3Xtz9Dv-x2LQYC6hdaTXSAT2B_oH3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGkc1v2wLSRDTYWPnpv4uT5tLkuhRsP3RP8EcnbzqpGeQh3kO9Gg4xW4PqfefYm9duW0GmjG5AgMTY-ugGuk7MZsHdZIvBwCHFvqO7hUFk7XBv85NOdfDNMiGC4NfRfUue001DFgZ4EkyZtQhLA9sc90IF9cJtVGWL4hmwIq4H1gRadNnB4S891SC2rmxv9pcLtZjyv3tbt9wnkB2229_VpmDuW32WAnSqLQ4hkcBmde5TqWUZxACVWo55xpGBINqPQ--1ra2uVOYUs1yf44NriIZuHooJ-Eu_NJNQfVA1cBuXvDAF5NFVRyRxI8D0sIJWZ-Jr-s1mtju9FDNjRznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB7gJY8dRD7LzIu1zEAacKBNEuZeZzXxodVqIDxjz5qhFOA7hWeFUON0Em1SooBKmQ8IeiLmNUKTAAN7SkZmbJ75U326SlllS5jSkFSAP05YPc9kjJtlNDqElhG_uspDr4aAl0HgFc2MUfx0mVfNfcSC2AYhu8aNA0p_cZDh-_mXm7f66IRWYticx51OoBNFIdx6xpVBSOSNFHPinFM06ooHEpXp73lJinQ3sWvNWVo5QlSOnJEvHfWdazX5L71CyTa6RXZJs1-nXn-G8sJHdVyx5OhYg-M7coGRkwZTHmJQbbCglXcLvDBmL2j83QW7NhOmqcI-moWLmaOW-b_JXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkLhRP1nyFdggwlxJnVwDPPQQW1n_5DnOQsX8Omb1XqsxXdnW67GG2yeoWfgTKvPcIAzdyPunc2XZAEc6KMThYUOEQMl2eYmFnnUX_F3EJ33Va2bLde0zUZrFvPO6mkFBEVOsBW45Cpq9d_Do5uJRrIjKbfnlKqauODLOsez7S6_nR39dMim0fSf3tF6ufMCXt6GNbnY6X5jUjq-gwAmf30Wt0vDNFt3DIgFCxbZNNg2FCl90dAJ-aVrDFAT28EgJ6BVeN5uKBCIwKwSkg-4RPd0PbXWWEyKP-5H5qkfVF4U-IYkeJBJGmiINxA7qLPWvCfCUpD9Pc65iwt1RJyBXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQiOHcfOHyKaqghcpSrqDA-Ge86t8rOEtBN77N5fudw5SGpIYb7ZaxkmHLwFh_TO-pDPbEvxILx9YV-whwrpUIy8u0wJFC4erIZq_dKnSdEHPWnlouMCoYrzpeWH-V8lFjjxdPpnK-pGGpjWX7qEIfN437ocPJ7_uH6T_7MWczQsSTpl6hJCA11ScsYh_yUqGCsSRMF7Uo9dxHr5qLUEtGO4YTNaHTVcaS_Q1xG10XMiorgjZrwtl2z6_RvEpugYev7kdociX-czd_V3IK3jQWWf9i1rspNLe9FF0HGSCOy7c0pCFg8ElSQBwangkmQyVXrLdc2o2bFUrewR4NiBbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1ncTtnsN-IPCuUva01_hLP2oEWOQrgdunQF8UIl9LFaPcg6MMZd8a1BKpUZQ7I416ycuf6TM6z788HAPkOFrUCeiIj86YT2AEjTJdP174J8dthI24JhtbOa2hdl7PZ0E3sSggE7wt5mWVaJfNQZm2vt0NXla6GiZc5dDDEccAJYrGbjHz43Oxe8oHErUoUYL1gi-F16ou5LnjB7F__-cIe22hCWdP_vLQS7GdtzgQTnoJYPsOhBtHBPGES82mfmoYiXtY78KGJI9P2t0DaKIcRRSU2jzTTxGQQHMni6KK4KOZP5xM9o0aFQpRdrdmnycJCyIlkRcBasiKSGKUEAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3sDI3W50Y3-n7tc9AjsklVCLsa5lD61XXHYIY8Im-SUxSkiZqJlfRvh2Ynew9lRwaK8E57nRGxR_IcnhEx_P06xglOzUWuutV9I3lvZbG_ywVx9_1Nok8DWJOuvyMDVPW2Aepil4nm0Lq9NfTUtuD39Z4UDIsySUn-ZJ3H0lCoEKV_bWEvxt7YLGpMRLhc0ercPYJVCiUCFhYjF2emuFY8yXOpUI9JWKaF9uib502hXeftd0HLmD48-RJH1_sk3vbGMxp6fHYfJU2cvCj6pEexs8yab9Hif4XnhuSzpMayQQhjAONRJQ5-nkXYz7xLb-mn0WsrOx0dRL22G3nXt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeQ10aVzAkcmkSxBxMs3Jr5T4DGWZt70iYg3iYT8h0Mf5-Cj4ff2zFOFtgnfeEY6ZAAHm8Mhq5OFVC_nbQQ-zOLLMGkQJOUwNw27lnsPFa0gblZA11uJX2qNSdwN3IMBHBTQ44TBR2mggTMoQcDIcDlCyYFfs8tR62jEVarbCeJ0lWN12FS-cTKDnTd2K2SUDxaFFo_s5yEhYkF4HX6G4MYY8shQf7nNcASLYgvWj_k9ZUGb57-ccbIKTEHUgAdnIw7MscgAUD1oNBatpc1AUOntHcvgMwZIkzPNlXsUK36t7BUy3xrMpnWvSK3wuwTTmsICsIHTkMBG87i5ssIXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP9c4H0bo0ViafjMF3qMODoowUdlSVTpc95n9VcdtQthqShw4y0cydXNdDg8QiwM0lT-1o_8RShl3JStD5tsV7JA2SBaRLUPc7z1KtpP5UxhTtnupya_2EdjPuFD8i4_O3mx7L1jKXyFjYhbeQ336wnzm50_OCEvHxZ_2Q6IQXcb0AMkBQtwb-d0iJjlLedfqDQ178rRp6OPCJ1JKgulV7KvhT_yC7nibRSr5gawT-vhDFHXl17npG2F3VqvrkR5370umJWe7wT_4Eyz32AXh3YtFQJqTxFEvN-vGdZzo6rOJIzzHTzOhKsme07s-BUn37uhqj5d1wJYRIfw7RA4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=urmxv_j1zjGFnWr4-VdsGbzDuKt21TbPk0zJUjADy8LHJtvIb8MmKvD5suShyyI4GJJuz4AEnBYubbG5B3z64eE6fofmADXw-IPEJwLU_T2oRP_rPxxGKafuko72GU3usbqdqHWIToETHdpicoG-VTTU0TciiFmj5RtGAL3hp9i9dzlDPOh_u5Hh4xQltkEL4Bf8dlHKc158ZXVL67NzYAYmPHtMCftXhSxydocqg1s0odddD3-ExA91HXNNAdAZ8W9Z5V8xVqc2lR_f6HLO01gRrpzLDu5VcbZpD7EAKE0KMRwfrA5KcKX1qwY_FpkzMKT4mxxY3jbpsmTGYwRvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=urmxv_j1zjGFnWr4-VdsGbzDuKt21TbPk0zJUjADy8LHJtvIb8MmKvD5suShyyI4GJJuz4AEnBYubbG5B3z64eE6fofmADXw-IPEJwLU_T2oRP_rPxxGKafuko72GU3usbqdqHWIToETHdpicoG-VTTU0TciiFmj5RtGAL3hp9i9dzlDPOh_u5Hh4xQltkEL4Bf8dlHKc158ZXVL67NzYAYmPHtMCftXhSxydocqg1s0odddD3-ExA91HXNNAdAZ8W9Z5V8xVqc2lR_f6HLO01gRrpzLDu5VcbZpD7EAKE0KMRwfrA5KcKX1qwY_FpkzMKT4mxxY3jbpsmTGYwRvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7gu339wyFMEYaxjKdflLpl8jRKzdcQs_EMz9vFNNwd9Mtk-Wh_UQF7zCF2hZjYyh3iwRRIcXIQ0SbAA0wRxMwcKBwsQqTMlsVZa31gJ-jSPz0iLIp_2doYq-GjV2MQA6dLCEF5gowswnWf6y2I_lc8Zd_93mFEwJqcrWwX4jSbe-cuGL50PEd34poDsvp93TBnM_X_pae2iU0mMTsgJiQwG04yc-sT0URawHHVI5lSo8DwL-BI22iwrsS8LxrNNZU0yBElAkstnXBxRwBHSaVXZkhn236HhyEAOGRHIO4WrnhORJ29AftMtZ5SfRXX3MM7F_9-1gEX-TRPQrcwbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=Nb4LGAEnkwXQnc3j1igyGJH1eEZp-C2xAGAhMYCGwlnxU45KOdz1VGO01ST6bmK6I64tN3UYPE1k4EzF3vu-l_YKrDMJe2cIlOk9GeWA_SLt9UeFnvx1vWTmmt2udwaG11ZLtEXy2RZrNY1DVN5ybqmVLJSX3aYP0gqB7UdCTxW59hMNf7uFydLnosbV-7AW5hMdrAIKsLL4f5Zme-EbUoO2-2nqyomDldM2PuzdNnShscEzZkeBYqf8gvgp2waq_VDfTmVp0tQ5b9RXBcXjQIhbC8tf8MeH7WCjqNdioSAwsuFyCtoPPK2jZOiUX-GkCi95F-EtqCl225hJWut9eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=Nb4LGAEnkwXQnc3j1igyGJH1eEZp-C2xAGAhMYCGwlnxU45KOdz1VGO01ST6bmK6I64tN3UYPE1k4EzF3vu-l_YKrDMJe2cIlOk9GeWA_SLt9UeFnvx1vWTmmt2udwaG11ZLtEXy2RZrNY1DVN5ybqmVLJSX3aYP0gqB7UdCTxW59hMNf7uFydLnosbV-7AW5hMdrAIKsLL4f5Zme-EbUoO2-2nqyomDldM2PuzdNnShscEzZkeBYqf8gvgp2waq_VDfTmVp0tQ5b9RXBcXjQIhbC8tf8MeH7WCjqNdioSAwsuFyCtoPPK2jZOiUX-GkCi95F-EtqCl225hJWut9eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGHCcvgWgbUOA5zn4nThx_GuIqtoXYZ_tsVG-B4sZLMNErZps15Bm28MIhoYwcjlwGRyLrBhy2gsvdnOJ_hVV73FZQumhuek9ZadAWG0DnIWho5wYQ2mr4J9sCrGj7Wnm3saNC1qG5JKloSfpAUa41jeDE6BeAFImzZbJeUqfIAoLeBTJb1NOAa2UOko4TEw8PLK7YKQJPVAwHT4FyPXtDv3GYT20iQybvH_v8JJ-LVXykUlWIezubx934rRToloGeYpu_ngW4WgZZOh8YaljZ-0BPi682irbqZgtAdHO99tYrN5FLTHr_B60cwYC9SWEqxNsjwWMD7P-ie82Icn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5hyecBh3M5HLqdOREmvrARogjQe5Xv5QrDDDme4cNHfJs1137mWjQX7HoRXHAFymWB3fXkd78BJdOGRSnpeiIVTwlk1yiX4gOdhgRUFn89jV6K30vb4vdUX34CE1PN7FHU2xRQbNjrosqFY8N2QItsLwejBjVMEFjLA7xXQGuU0sP-pAesIAVySJt60FxZAjeO2gLcj7GjQE-Fhbv3pDgR1ADe0GiwkpGwOMrUsyh4SnGe9qLbRzBBuZMiP9EvtKc7KnXAFlKywJ2iLdoPMIYC7mtwn8gVqECFSeTtMvNWmXl9oN1PZzzMbC9MGxFZQP_oujtsIGjPNy3H-dB0p1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=Mm3rgoJq41GRdgvGgx5Gi33z_EXgvEApoRk7bDuv4TJ8Rd9UnYAP6CxXlJVNFBLExZ87MO20o9hLX4SMP1k86V3zvIyPftZ4jYpAmK8vmwzfuWrCrI4fGSYo0gvZdnxc99v5p0KsffBeNvMmJopJz15aVDz_rDa0ZD01lrWTbjFRJKloTh2EL2BLB8Yzv0luzCf3ZqI4GWEPLTLZeiEXODQe41485UqdpMlOcVOhCpSr_c-ardqOiG-vCTvLPkp3V6lGpxjb2dKMYSNLhkws2QzuxpU6O9E00YdFfctoGw7-M51l_APedcGrEfoXxVtiC0nDTtfW8QzgTaehR3RXNWvS0QBvU4_16E6iIi5ecx-kFRJ9LcSzkqDaV6WTlFEgyslytBlqDkmHFJ_tA9-3A1Mfsv_bp5zGKDaXomMNs8dZGVKVRcV5aS0fDgthqUy1z7LrVZ_xV4G8T9DS2jV-cydpL9fkjU1rqkAQXU5rjYOLawNE-v18wm2SUii1OcUnUYZcTfDsmjAc7LMeBImJ-fAdT3R_Z7598U4H5qaCzEZtSJv9QOW2ahsK3pyuQp17-Ck7lUn6YuDXkIyoqgbP3RJkIxGOAI1R6Dty496A9p05zcey8-zu9sET4nFI6NMGxKaAA2Z-qDV34a9oB3CdBbou-d4_C3xyA4t4_FTMkp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=Mm3rgoJq41GRdgvGgx5Gi33z_EXgvEApoRk7bDuv4TJ8Rd9UnYAP6CxXlJVNFBLExZ87MO20o9hLX4SMP1k86V3zvIyPftZ4jYpAmK8vmwzfuWrCrI4fGSYo0gvZdnxc99v5p0KsffBeNvMmJopJz15aVDz_rDa0ZD01lrWTbjFRJKloTh2EL2BLB8Yzv0luzCf3ZqI4GWEPLTLZeiEXODQe41485UqdpMlOcVOhCpSr_c-ardqOiG-vCTvLPkp3V6lGpxjb2dKMYSNLhkws2QzuxpU6O9E00YdFfctoGw7-M51l_APedcGrEfoXxVtiC0nDTtfW8QzgTaehR3RXNWvS0QBvU4_16E6iIi5ecx-kFRJ9LcSzkqDaV6WTlFEgyslytBlqDkmHFJ_tA9-3A1Mfsv_bp5zGKDaXomMNs8dZGVKVRcV5aS0fDgthqUy1z7LrVZ_xV4G8T9DS2jV-cydpL9fkjU1rqkAQXU5rjYOLawNE-v18wm2SUii1OcUnUYZcTfDsmjAc7LMeBImJ-fAdT3R_Z7598U4H5qaCzEZtSJv9QOW2ahsK3pyuQp17-Ck7lUn6YuDXkIyoqgbP3RJkIxGOAI1R6Dty496A9p05zcey8-zu9sET4nFI6NMGxKaAA2Z-qDV34a9oB3CdBbou-d4_C3xyA4t4_FTMkp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpfGeXZYPRz-h4KdMm-Z7ViqE0UDO_JT_wZDodGmtheEiC4l3Xrbxcviz7DTg-jTxbyJ6EBaLoMSNv70V_yc0olhFsvVkHIAdGdpCOA1OFWirCjOvS0pxRtmdUQggEHmQKB8o3RwNwjaiKrfuRhjsbfWvTJiXlS3sHqQYFvj8eiLcqNu-Xh78LTvo4wv7ewo8IMPZAAVF-pS96cZBghVibqk4b2r3fSlTnTUZwjkUZR3GaYBuzHhvDcbdW6j0jvY8MdDrsPz6Wtn2I2Vx1KbQN9fXp5TNznaB1QWuhhFaspNJ7YuWoGzoLSXCmLqtsAW2zksm9Qbkn3P4uzWzuBJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igECaFS0wgnX2scUK1g0GgNpNtyFZXy1NA05AjFnRTFiM2cNn-j8vDHd99mjCvDhx5aIYpX8bIgywfpWvIEd1t72_J6lgYuSQsd3kKeI4g03ook3JXllp-aUt2dx76CP740MS28YREo4FPMGxO6FxsOLQ2wzEmysLeJJR0uAQDYP-KffADtzekTCpmJ4Dp5Vm-GlqBw1B4Gg1OzBNYj_pRygQz-17Gjc70eeJEvkp0eJcJHcSKgJafjRS_zdYCjK2nHbRz_umcMiT154tTotWtxar69YS7ytQM87-3BkD2SpFr7XIvAISoo7DGyDY9kw4Ocn5oXXZGJDTyko08EuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI5cvfSUg5lzfAUQL00SPgNmavr990fUXpo6yLb8qJLMyErnhyH28Jvsi5zQ2zMepYVV-nymImowZq-cBRI_tMF0pqcTpmR5_HL2DR-sqQBiX_hjJNtb_J7xdkoETr0282_BAzo1jf6A80ZYj2feeWPxwIhMb38bvN-DFgbw1bTGVL0NuvApm29F2Zd4cnszv4xho2unD9tYvUf-TmhvNmnTZYAZs5V3e0Lg_LIp6RhQplLDA06XNesuiqJD02gHvV8a7H5_xMs0gAC1W8dcLAzq9gFMb-8SSWe-DlTPyoMih9FT2S0KjEftde8jH58UPxVhpOSWZPL_cKZETX3q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=JNFotgU0Ye3lQ9Uuv6pGIqFbOcbQvPV4d-Vc8iALlQnaT_N9rO_t13C_Nn8xNq5_fUsx9hvPDdkK0PszxonrjFRRQYmrM4-8Wb05U00jmkBGzNPtVdEeD4inb8aWQsziK0-K0SMA2H1uTa3h-5BpSPCJhQ3DI__LPC9FjzKIDPNGe0BHjt4FNgdIlogzaPhxBNi4OyVvRmz5d-oF11rEVcmm5g7GBpEN7kYuCjFVz4fzm0xKU1rN0g2xzkZlKniRD4l9F_BwE5AAcXMTH1FgQ0xL2KZX_XcV6fo8AyMvktKEEaGbu62AKMM575a45rs4gMIV5ALXSoyHmzyutIL3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=JNFotgU0Ye3lQ9Uuv6pGIqFbOcbQvPV4d-Vc8iALlQnaT_N9rO_t13C_Nn8xNq5_fUsx9hvPDdkK0PszxonrjFRRQYmrM4-8Wb05U00jmkBGzNPtVdEeD4inb8aWQsziK0-K0SMA2H1uTa3h-5BpSPCJhQ3DI__LPC9FjzKIDPNGe0BHjt4FNgdIlogzaPhxBNi4OyVvRmz5d-oF11rEVcmm5g7GBpEN7kYuCjFVz4fzm0xKU1rN0g2xzkZlKniRD4l9F_BwE5AAcXMTH1FgQ0xL2KZX_XcV6fo8AyMvktKEEaGbu62AKMM575a45rs4gMIV5ALXSoyHmzyutIL3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEMN12xJP_WrDi612b3xGTRWvRvwTCWYCIhrIOnerE2DPdAiEFRugEIb7A2YF0C2mOSYi084q08u2BFSKJRJtNco8UcuUwRkCcwy9jheuZyDHqU82Qb5MWB1tA5qbov9NTo6x3JpcVzSlO9pERqwc9RWfdVRuu3-ZPBmGlcqrAPcOsqZNMfovsnZvNc4iuKOqqKQsa44Il2Tvb-QcW-qmXGtvntX8jeZurcu1fZ-BgER6S21q1fI5FDWggjTPZovB4QXviWW0mH9qv_93ZmM8iD2tQtRWuI12Sbm5fezmJ5WoamFXUACDSqS15dz7cWC34bQZQgO0dIMuNtVZISCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7yhsP1_J1AwUn1LHcL3l_3qVw_MnyHtqxVJOL5T7wPi9pnkLxhIFqalBXggw9VAvWVaDbmW6N_fXa9co5GiymYeJiPnx-yRWhFB1GFyrfiwxERaBkEm4FL7WH9-1IqNKtjNF-x9_9jxP6Hi0pPSwQwayNFgxlFpoyOvhVIp4Kf9c2PXKr9eqibua62dkkK7tX7F5SDX7DZp2VJoK394feBUh6KoF4fpvXfz1jXGUb0TWjY1bJ_rbixrxYGCuGFzUFvUA9CAkDgrggW1OU9Fc-ym2_U0ohgpA_iHOWEDqoaIVkiRdCERGeUX5d_xWEn9AKrhZWUra9oHa8tyA6o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
