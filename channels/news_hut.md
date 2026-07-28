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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 145K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSKXfixdPdfbk5i_O0GyVU-5T7VCFSQsA6DvBBqiNGD39IecTWLgYg5ZERMMgGJdBVWTgoX87REh1SQXFOm346cVPDkbhGGW9p-8fI3AZHeCXy54ytRrSHIpkkABCM_Npn2wNAG1vqPXUY6EuRHNrtSg2fmASiPcsIZIm4zhNAFazd7P2MuoIa7iQFN75nRNxrWv5s5IBCSr5eN4NuZxFGCGThPDY1CkpJPh-kZ0QW1TukC600s0cxAE2FsIw4OTjkfi_l03TtDZQeZMCYONs-Z3TjEEPv4wFPg8t7aLFhcg1n4-bRT6egr3C24PKnKpkCfxYUyebS0dbdoMFjkvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwq1AWS12VTaiz_uaHQUU-Nk8zNEps31Kl-OP6E5suYJlflBGquvMmzwvJ4-JhZFKsnVi9IiwgbXatG7P6HRf7N8K1hd8MJM6jybae2yRmvANjAGcUJkggWUtUaoCZ-OIZGu0dLzyyb7ztcyl6TYyix6XjugkbCH9OP8qKgcPU-e3RSld1U0QP9j1SVuaMBHhq_RBKEkfCmLtLkb_44CYTgejEfQUZ11aix0r2UJrJI6ulZTQXAp1uQ9T7zp2KFjPJ77QtcICmwkDvOXO2QsX55R1EK2_v6cwtF6RfcL2vo9kJQLRuJNWjNvk1q5bmvDXfU6Z5xp5uH_kOA4hCyGfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUV1bjPxGEc9pqIGg-5elzi4ghvuC9FDziNz_MTfWHN3qEe74xZNyCyFaNKzjo30XwRy8f4vxOUqC_T7eeQhJxdjFAi1BCV1yRVo4jwS4Eh2m_P5OIwDsobrF_Wv3IsGpwKZutPvNRNSKBZTPImopzi8XRnKaI21jfWnPIYJFVwvPxNUJdp69UXhFz3LmgA-R0QLbaxnRUKTJ7JJiSiKPU_ZbO21PMaGHjge86Zb-ZUGtLATN5BGenvwdWo9touG_YYTqvWWRTMGmAEYrQ-fDqCgztlQciMhIQd8yqrgkJTYxgjRiolydRvh4NjMYalCKWGwtqppEqro1_oC44fgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuTsAa_5IKnvSpKWmhS3iYcWs6W8Nxk-Zm2IBu6rX6lPA0ElL-ra_APo9C44m75YTdxZUv_Lge1UwKVsCmshMSam7spnmdBlv4-jZw6YMI2qeFU5T-PfF1bI8bHniqC_HX4YprSbNn9RN3hxHd1KSNjS4wExIga36bwrDFIkWnfcGNrU5k65pkh4SSas3qtIDN_bMVa6oDkx1lvyYeJkGi-U-mpziCium9sLiqmy2Pzvk5oIrXG00giCQnDqxpR_v6OdcMSTFAb63ZQjXCVspRvLNNw8bo_iaqEGJ-qgTsqRrA0PJ-wa3FBUEimaBKJhIkUygCbNk4DaUA1pd-aNcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=LYXfPsOW4j0gjYmJDkCd1UWYA0PXD4vemDh1KXosD8Vgfjp0MY6NyiYF79Ds1lqi9wVU1WscufsmQzrjBf4-LgYjPVFAlyjc9f97sESlvzFygjrDNfyVarR1ol7-cOa7NKW_CYeKW63qX63ByZ9DHYn1t-aFMCChflVKFiuW02KdhgXnGd6YALcvejFiSnubEAdlQgDwWN7AY5KRxiLbqPFcj9tyCZG4AOknt5XZ__U3YYa84hLydKN2jUMbJa5xgzpDTlx3suzR_kHfeb0Yqw7dhwrQG0V2lPd9o9rMswAHcFnf5LLqiB8FSy5C3v3c1bEI60mv0fNbfLXzXzf8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=LYXfPsOW4j0gjYmJDkCd1UWYA0PXD4vemDh1KXosD8Vgfjp0MY6NyiYF79Ds1lqi9wVU1WscufsmQzrjBf4-LgYjPVFAlyjc9f97sESlvzFygjrDNfyVarR1ol7-cOa7NKW_CYeKW63qX63ByZ9DHYn1t-aFMCChflVKFiuW02KdhgXnGd6YALcvejFiSnubEAdlQgDwWN7AY5KRxiLbqPFcj9tyCZG4AOknt5XZ__U3YYa84hLydKN2jUMbJa5xgzpDTlx3suzR_kHfeb0Yqw7dhwrQG0V2lPd9o9rMswAHcFnf5LLqiB8FSy5C3v3c1bEI60mv0fNbfLXzXzf8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPPkJYHp8jZKvyFtj7TxI0PtZyykrS9ZNPWvWETM7gUg6UTVGZwxNucBp_rDpPGjCIRpguTlmKgElISegB9YeZHlGDqexcttn-p4vyNM8Rx1YamwxEhEnPOS4z3nZ2NKK3DTS8CtpUohArXb8wrp5BQeXtG14YW92CXHd5PB6kIDbsAlaBben8p5a9LnuqZjiQtdILCsXl6-4Hj2KxbjujOaFjbuUfZSaAAFABNO4RzPBHuL6BPH4VRX2FhnKNpamApdfGZV5uuDsQkyP-tgEVWxHFZEorUVQKQarmex5jRFre5a6ZxUjoZDHJmyxkF-09puHzNBbF8uHtR9pk8spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-TZ9gQFEfQuiJlQrb6k8Ytn9G_9cg8jneKyGtJKvL-7nwRRG7IliSoCYtQzKsh6hiTb9K_N9U7fRxNDYydGR3g6JE8iSKD65hyewIFS1qK3rKlj_quGKJ-hg_POcCh3Aiy2iObe8uKKkQVX7PbSIjiW7uWpj9edjlRRLgyq3UgIybHu4JOBbqvUDK5sOSo188Qtioy582oIm6VWz-0kpLrmQfdkBDWOwI8CpREHS1yk4XNPMobpe_eA76Ty5zlcDGT-JrTDJ4K1D-8_keIIrM54Zp1iT7YD92NsRlE2zGirmC6pUXT7yxjXV3f51CT9fXNCHS_lV8pCyMIcrE9uWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0H_-BgNqYJZOoca3H1Of4mL0042G3V_AqCFTuQMf91-PPifWQxxlXhgziHRyU6SYGqPwjpvbpM1b623Gnr3l_0-5yKFWWjWJ0YuROjnIiko4xv3DT4J8RiVC2Wy2--LHX8z9GVJbFgqHlKJ5CkzKUrkjfgg-IqNSHgKm4Q5QJ2lzFiyS6hgdVGh6x4K8WmeK8AgquJFcZrhq9WYPE5EqbZ4ftwdCb6ZcXFiOu3YKsDgCK9em93lCM0x3KpzSjxgDCLbpKuxG0J4j5wWqjooLwcDtiUaARZhx0cRhZx1S6Glu2GunYvVc1SF92d_e6yIgCs_vuCkLcouy6G6tB5_Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=N9VNP5qJXFsf94CMigW4pGCfeRVV-7VoPA7d5wqvatMpJNwLrGxYfWfLQpPero3rDqXu0feRSAh6NW5R65mKT2TUBWTDESGtnGUbr6wMB0EnFMlK2_P8EqrfDUjt6wJbylSXkT9OL-FrSZU-bp9V9ZRYsgvzzUu5ct_q9VfXx0p8nfaWtW-nWkWnPMR00IAzcunXgv5Nf08vR1FDN84YP775bYJhRMiLG4TzLUKH6V-Emz2nbxbD4MNHCTBXSfZWYOW7FLDrYmNkGq-6-T-kSmbQGD82oeZeuFmLCAe5xnOccWkGbJIkx3BIwSdzIWIuRaMzZyqmCP0H_5WC8puBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=N9VNP5qJXFsf94CMigW4pGCfeRVV-7VoPA7d5wqvatMpJNwLrGxYfWfLQpPero3rDqXu0feRSAh6NW5R65mKT2TUBWTDESGtnGUbr6wMB0EnFMlK2_P8EqrfDUjt6wJbylSXkT9OL-FrSZU-bp9V9ZRYsgvzzUu5ct_q9VfXx0p8nfaWtW-nWkWnPMR00IAzcunXgv5Nf08vR1FDN84YP775bYJhRMiLG4TzLUKH6V-Emz2nbxbD4MNHCTBXSfZWYOW7FLDrYmNkGq-6-T-kSmbQGD82oeZeuFmLCAe5xnOccWkGbJIkx3BIwSdzIWIuRaMzZyqmCP0H_5WC8puBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=ctxpmsibjiIMneQdmKKbon0pqhIoH9cRoRJS3k16fbdBcPWQlAfDfi4lwmXE3Ou-8CD8VdpkpJbcd0pdJKprJyPW2jb-sMuWcHkOjLpM_fvLESvu_28TOe68yQ2QnCWzLbWo0BwmvYlbdEVLnXE5F9Hxew_V6tjxh5S8lnU50Hskmg1L03d0orTZUZ-Wyw5_R5-kAbp5-IulXc4bR4wgKIMYQwVBPdwXoLVrNdgSjTEidxVVm-V7Dob89eQxLws9BVFxsU68wHQ6C_lYPhCXjx9iqADnQggBjYxJ0mj8_ZrcNFlFFwyZs297YzarN1mN5B4dGgURfqjtR1hjT6lBXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=ctxpmsibjiIMneQdmKKbon0pqhIoH9cRoRJS3k16fbdBcPWQlAfDfi4lwmXE3Ou-8CD8VdpkpJbcd0pdJKprJyPW2jb-sMuWcHkOjLpM_fvLESvu_28TOe68yQ2QnCWzLbWo0BwmvYlbdEVLnXE5F9Hxew_V6tjxh5S8lnU50Hskmg1L03d0orTZUZ-Wyw5_R5-kAbp5-IulXc4bR4wgKIMYQwVBPdwXoLVrNdgSjTEidxVVm-V7Dob89eQxLws9BVFxsU68wHQ6C_lYPhCXjx9iqADnQggBjYxJ0mj8_ZrcNFlFFwyZs297YzarN1mN5B4dGgURfqjtR1hjT6lBXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=R5PZsk4JWW35fRih34Q8twjwm1PrFxlKIt8s3N9s8d04wJY_JPdT0qqrpSeu40ANhmiWtzGoAXXFvd9A5iNPrTvpYM6l3hB46qVP1k3ryTwQLOWchzV9Z1oNiJIriw85JFC43j2Ca5h9NFSTVPsFkwxaCR29WF_MiFtY79tn4fovG46f64Lwo_Sb9szNqLvCXwG8CDbyR8fDJGE89zRfHpBJ_xBJTWrdXm_Oh2lG9xzgnU3R4Wd2FD6WSuCwOPN8URvy7dX3gcO4nLTZCQXIAAL11eyJGvpTgV54JjnWpmmOhA-RW49g15A8eDjS5b7keeTNlZBdNWX_V2eiN6V1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=R5PZsk4JWW35fRih34Q8twjwm1PrFxlKIt8s3N9s8d04wJY_JPdT0qqrpSeu40ANhmiWtzGoAXXFvd9A5iNPrTvpYM6l3hB46qVP1k3ryTwQLOWchzV9Z1oNiJIriw85JFC43j2Ca5h9NFSTVPsFkwxaCR29WF_MiFtY79tn4fovG46f64Lwo_Sb9szNqLvCXwG8CDbyR8fDJGE89zRfHpBJ_xBJTWrdXm_Oh2lG9xzgnU3R4Wd2FD6WSuCwOPN8URvy7dX3gcO4nLTZCQXIAAL11eyJGvpTgV54JjnWpmmOhA-RW49g15A8eDjS5b7keeTNlZBdNWX_V2eiN6V1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcySbzpQcscjjl-85GyKvLDhQQ2onBJsqZMERbBiYnLSdSP4r0fbK7rcVnS6YSVnLp5l9ETmlXFcPX900gUqnN65WtBqpvX_qZQtcJBVZ5ls-g69cLXB1EfiJrAttXYWfUbJ26WfrHjDYIElVJ9u5kYqi--UF6GGIxXJZ0bM3IWNSwJOtexprBSze7a-HxnhHXWT64o3DEYw0Posr1IDsF4PVNy-Y_d62NSq98ulRKRt3Ge3k2yg-CfwGstoEmctvpk9tTJPXG1tG6XnmH1wOWzRnT_Ff5stH9RUAc70UIlEqUjTIhCnZAYtVF9RH12xjPBlEsmUnj9xhIzDF3NWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5sALdGxpyNRIYAZ0MrCsUKFK6ZbGOaPDbbpx8cfFDRtCdpygsXH1BFOiRRvbe3ovYwAw4c6XqWZntH-tE2_u-ofAcjZznCwEss2x8FxH5ZgxM2JSp2yrVz4rsdINuAmjt1ZzhQOZndSEx2SraMo9vn5NSgLnUjuvgqZpK-elpj7y31V2vYjyJHGu5N1hhQnr8L2q4U0r3Ku_ydkqDQyimn9grMMLa5i8bO4GYF_qhsTZCjtEcSiWKbMhDWbgIjT9BYqt6ATOao7dCBCpVk_SuapZ9ogZY-TuFSz7cWjVBeLw1ydfboQuA3jSbVDEp5w5nZMZ84Te5qnwncp4Sq78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T38spLSmEU3UspSRUXrUOBegG5M5rfG0zUxkdOAm9FqGcbNkeHbDwo2M4HMqHa79QCaU2d7Zsa2SkiqXxPN4VOdZKm9dZ6eRPZqLykUN0eZlYDeLZUJ651OH8jyAnCACEyXqtXuIVqq6P_U3CL7TsmE3WRYXLWZva66p7QydB_Pt6uSYESnptlIRPjJt1Erc3dgSKRhBjRmVlDPc84dH4khC1F2yudWtnoQpUzsWmIoeFjcTjvBLfYtZeyjexX3W3A-dad8m9dzjCq1ufD1m8JfdsYkcagpHiJl2vQ1Zr8YinNq3lAWMbUlgOjObzD7dGlHcFWxMwC3CspUt99mXuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=nMDhaObg9pRFVL74QUw4p8XbnAS8KHcOppfLLB_tsaqjfRC77X_MXpqMRWGzZeO7hH9EDCb8oF5nhhg5XtlLeplL7nqSXJAemY2CaLGBygJZ6UaDIaznvzUhxOO07B_dLgYDpE-IpZn9Bl3Moti_L7Iwdc35VGHtOeX46EWz9ha7TwGmBIdoCx6wM0yfg1OdPdPC7kv7igAZTcHU5n-pozNLDPycT4Uedxyafzy3e1LdVobGq5vYojV5UKIIbn-1Lk1wGjV2DPfWSSk7g4FEgD_kklp_Zi8aokTLo14AqTpUvbFM10gIb_NOA_Srkh_BWVTs_5WMbZfbHSrR_d6jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=nMDhaObg9pRFVL74QUw4p8XbnAS8KHcOppfLLB_tsaqjfRC77X_MXpqMRWGzZeO7hH9EDCb8oF5nhhg5XtlLeplL7nqSXJAemY2CaLGBygJZ6UaDIaznvzUhxOO07B_dLgYDpE-IpZn9Bl3Moti_L7Iwdc35VGHtOeX46EWz9ha7TwGmBIdoCx6wM0yfg1OdPdPC7kv7igAZTcHU5n-pozNLDPycT4Uedxyafzy3e1LdVobGq5vYojV5UKIIbn-1Lk1wGjV2DPfWSSk7g4FEgD_kklp_Zi8aokTLo14AqTpUvbFM10gIb_NOA_Srkh_BWVTs_5WMbZfbHSrR_d6jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC5nGkfSJJKk6PkZCmr95uzMszIUziDEsFg6Sk28soje77NCqVNw7drF6-ElKQspTO65NvERiBVmrha5R3lnvtZjO-0tr2gtB9h4nS52605XhzyB6Gtr4yEOMldi0w5b4Ul7Ko_g3liQgGZEN_1qyM80rzEaecgnhuuk6NNthiHInpyLl7XJNrV3q1Nz2eX8LeqYOmCrD-qJVOzHQ9G08Ho5AA2P4ScA0v9xVQ3uFQDb9WA8RS4PaUro5nOxq1B3H_jMwHR99f5vf2flpr_qssgMKXkRa0OF-RTvUUwimG5aNuixfxOf2zNlLmQ_nHWtZdP9f0w8kJH59JqqO-OZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=QpmOqPYI8k0FGhBgWesxGnjCId_AFp2zUviNGekK9-cfAfSUrzssiDkgQHe6kTbqJG4QqcxcGQ9S9cborl9QC75K3og1Y0CI5B4lFWGEXvACw-wBBu5_-FPeTr65aDVwEtJEQu1o3pHwXTSCpny7-0Y8s91LPMNiPtxrI0WEDdb5sDaK7DUKliaYGWS3PSyGVDQcQgGiXrRD1pWBCy31RaWyUabc9HE8m2eWB3umh3OarjH5_CMmKbj3lmssezh56muncKmL37gBqKfi80-a79mfbAznp-oW7ERjsC_t0ynWUjCp_huXBFqRJD73O5HA_QcvIeEc1zXz6X5oN69yroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=QpmOqPYI8k0FGhBgWesxGnjCId_AFp2zUviNGekK9-cfAfSUrzssiDkgQHe6kTbqJG4QqcxcGQ9S9cborl9QC75K3og1Y0CI5B4lFWGEXvACw-wBBu5_-FPeTr65aDVwEtJEQu1o3pHwXTSCpny7-0Y8s91LPMNiPtxrI0WEDdb5sDaK7DUKliaYGWS3PSyGVDQcQgGiXrRD1pWBCy31RaWyUabc9HE8m2eWB3umh3OarjH5_CMmKbj3lmssezh56muncKmL37gBqKfi80-a79mfbAznp-oW7ERjsC_t0ynWUjCp_huXBFqRJD73O5HA_QcvIeEc1zXz6X5oN69yroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSIaE4X3a48rYXArfluy4ike2VTwTpGTlTz-IBtdtnchhPDU_T0tbdXFHFIUDUDCHfbsmD8Q4if8USsQjLd14fWqn4wD2-TuKMQm6DqDhl4gPAin_Q98tMmW09Z6vnXzdHy8p4u_VmsKfUycTHu-PkzaNleQAhT-59UxNyZoZY0LWaO2EYg4RiOsYoG1CgXsfkdYR6JzpMfI17GtGKkL1Xrg-Hr66m33mkmxLuUCUcyRnT8Nyx1T9mJ5na-pUzEvGcf71EVNOELCn-s4mFCoPTcV-Fyz5vv5impgKbqBLOG8G4SAqUp-LZCN7rUuDdf1MfNPvUNHGzysVsIWFNY1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=b-5IwWO1fm1s0Z5vTqYayafvr95ba48QUF4-GJZn_cqrDNkmfOgTIpZ18LMiNinPhy4KpHfWrPyJiBMVevSxG9KCGtY65ltisozjcbrYFzfTPLNEImwC8jdzSK68i5VIqMJIHWX-arWJcjT01_floQ6An7-26FbR9_Pz1r_caC6EIv9MPMUexX3RjyDnsPR3PftlOKmRv9XKiItx9KIwhGMw913GJzSaWu9A4WuvQAJUGgiVRmqCvfpCcNnsgzIwtjz3Q7RVjKvA2VF3FWKXRddfUHDShJwqOzLKo-zPehfpBXXEOnN_MTIT4bmC3-9jTHsQBqLAiSWHbdB3kT7iVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=b-5IwWO1fm1s0Z5vTqYayafvr95ba48QUF4-GJZn_cqrDNkmfOgTIpZ18LMiNinPhy4KpHfWrPyJiBMVevSxG9KCGtY65ltisozjcbrYFzfTPLNEImwC8jdzSK68i5VIqMJIHWX-arWJcjT01_floQ6An7-26FbR9_Pz1r_caC6EIv9MPMUexX3RjyDnsPR3PftlOKmRv9XKiItx9KIwhGMw913GJzSaWu9A4WuvQAJUGgiVRmqCvfpCcNnsgzIwtjz3Q7RVjKvA2VF3FWKXRddfUHDShJwqOzLKo-zPehfpBXXEOnN_MTIT4bmC3-9jTHsQBqLAiSWHbdB3kT7iVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7Z2gzLV7CHMQDaPjoVYAKz7fBC9mUbVvl92vrncKWa64nN99k5UU_fet59-BdRorWq5HD6rYOPemM_8RGgUJD_t45g2JxA3UzOACC0N3pJT0HZsEq92BUD4Pv4g75GN1ZwkBw05jyDOnhpMZwEMSfdXJNLutnzTB5dtk_UuNjvX91N--Nk0Chjo4UkPq7do6TJYoBguci1T0m8sasC2b76b4gYNOzdNFcuWrVsJ4VrUx7S4kTDDe1KBWtZUii7NPWTUSyAlHXfW9q-jcmxqKHIN3E7u3AMkSqpzm82B6nJaHagnRi8fwzEfl88BxLO6-y2VBso0W0cmBZPw3BbgxvBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7Z2gzLV7CHMQDaPjoVYAKz7fBC9mUbVvl92vrncKWa64nN99k5UU_fet59-BdRorWq5HD6rYOPemM_8RGgUJD_t45g2JxA3UzOACC0N3pJT0HZsEq92BUD4Pv4g75GN1ZwkBw05jyDOnhpMZwEMSfdXJNLutnzTB5dtk_UuNjvX91N--Nk0Chjo4UkPq7do6TJYoBguci1T0m8sasC2b76b4gYNOzdNFcuWrVsJ4VrUx7S4kTDDe1KBWtZUii7NPWTUSyAlHXfW9q-jcmxqKHIN3E7u3AMkSqpzm82B6nJaHagnRi8fwzEfl88BxLO6-y2VBso0W0cmBZPw3BbgxvBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=q-FSSX-PbnGnBH2J57MUEEU9xOAuDUH9uotb-7l_NOhpDZEQwbPBdX6UOzGQlVi2R-aJ_tmNqbjb5fEE3x-ywhM9hkJwcudtKGMKGVQk_H1IbN5fb-VdlXxGWXorfyQW67Rdt3hvdcQNcJX0xVGvEWhGNdTnP9NkQyISnZh_AzF--5lqbZdRyp-F1tWD06fHvuteVME7PG7xPBkf69wpt8cJa6kEw_A3UduzffXHjkCan8lRe8Xkf98rGraduSfyTLRE3ii7pxn9DC46yDP2fN8vqM4St6TyW9Sf3JQULJOmeftTT6cZxlYTwFr5GMu71toiW84I-fwA6FrX6_Fp9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=q-FSSX-PbnGnBH2J57MUEEU9xOAuDUH9uotb-7l_NOhpDZEQwbPBdX6UOzGQlVi2R-aJ_tmNqbjb5fEE3x-ywhM9hkJwcudtKGMKGVQk_H1IbN5fb-VdlXxGWXorfyQW67Rdt3hvdcQNcJX0xVGvEWhGNdTnP9NkQyISnZh_AzF--5lqbZdRyp-F1tWD06fHvuteVME7PG7xPBkf69wpt8cJa6kEw_A3UduzffXHjkCan8lRe8Xkf98rGraduSfyTLRE3ii7pxn9DC46yDP2fN8vqM4St6TyW9Sf3JQULJOmeftTT6cZxlYTwFr5GMu71toiW84I-fwA6FrX6_Fp9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=SlDNSVt_9y7Kh3dNoGBnY6hdX-L6i5QloQ0H6dmsgvJtOH4QMuvR8cvM2VtccgA5jMrlAi3ElJOhQQgp0woQwR4oj1KyFda84zOZhvY-UhGBcPgBOB9MVrmS2Z8lmu9gfzd-FPXxzQygckMezwnFuXTtj1T6mViQk4H84zjokFyvx3puS0AwJuOZ-_b5CM9KK3-qgHZYNjkNrdKQvExQex8eT012XNaM_cEwJe0whk_vq1W4VcuMN-s0kPdFdM2xVin9NZrITKr_PpRYr9D2YtYoxLMmIf-MInba55j9rScSR4Pds_jdaWuCejm8i6IG1PFQ17Uq0WnHIvi2BC0owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=SlDNSVt_9y7Kh3dNoGBnY6hdX-L6i5QloQ0H6dmsgvJtOH4QMuvR8cvM2VtccgA5jMrlAi3ElJOhQQgp0woQwR4oj1KyFda84zOZhvY-UhGBcPgBOB9MVrmS2Z8lmu9gfzd-FPXxzQygckMezwnFuXTtj1T6mViQk4H84zjokFyvx3puS0AwJuOZ-_b5CM9KK3-qgHZYNjkNrdKQvExQex8eT012XNaM_cEwJe0whk_vq1W4VcuMN-s0kPdFdM2xVin9NZrITKr_PpRYr9D2YtYoxLMmIf-MInba55j9rScSR4Pds_jdaWuCejm8i6IG1PFQ17Uq0WnHIvi2BC0owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c356qU9HBadLIA7Ov1Nv8xjK0rpuDZZAl0dXQZSBKfprk8uye7niFIRwa9M4VqXmWYHJNGcuXCFfARDqCVPuxFXRdLXMXhYeFcZn_mIhtJHFgLTJRYMdFqmJHkhCnNd1dhfiIiCIE20awuxbPzLH0BLRX68ysUkRxy6OAOUlqJyyteHO8k_Q3HqFfgzz3klgumTjDPMQePdLhar9jTCNDFqgqal8LwnA2W84H3aO7OzKrP82vQoMzqVWN5XZwR7Tof5q1eW7Oiwz6btZeR1Rmi1EkkvFQmOX-CCCDFkubuKp9J6MGe0U7Fx5GH3X6L77nWlniXfSkTt45sabEwgD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=FhbZYWhUa4Yr2Qkg5WHelXUPCctfK9213yWjsMnm_Gxvfvx56HhFk3S6xcSF8ttB5yorPysAYBAODjUG26xIzEfdYEcscCSYzRFdYs0uXBzi-lf_ZvuBrF4FXmskVacBaCr4LJrVyp0whL_eOC8B5_GcOYQBPhQxYxMuL8YYxYdLnp4k38nYP6qT_l0CXSs8ziSIqCO9zDpLUe4jnT-jTI-npUu85Gqov2Ted-DGKR7Ejocm0EC-MLstDSTtZ2CvwIFECotPP4VenbM_N3JYjStnU46r2Us5e-tbh6F_80NSe3yXk3VRPEHCsFWaHIhmM9pIdXGiH3Qo5jLsJnNDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=FhbZYWhUa4Yr2Qkg5WHelXUPCctfK9213yWjsMnm_Gxvfvx56HhFk3S6xcSF8ttB5yorPysAYBAODjUG26xIzEfdYEcscCSYzRFdYs0uXBzi-lf_ZvuBrF4FXmskVacBaCr4LJrVyp0whL_eOC8B5_GcOYQBPhQxYxMuL8YYxYdLnp4k38nYP6qT_l0CXSs8ziSIqCO9zDpLUe4jnT-jTI-npUu85Gqov2Ted-DGKR7Ejocm0EC-MLstDSTtZ2CvwIFECotPP4VenbM_N3JYjStnU46r2Us5e-tbh6F_80NSe3yXk3VRPEHCsFWaHIhmM9pIdXGiH3Qo5jLsJnNDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=AoZc-Hn_hdY7loZtEFMc3OutypyMvBzcwNTGYkB3LWa3mzUW0kjU3XOl53vnJHRPCviGsoVI_79d6YjP0NOF58kZezVkTKWUS1869v9SBsoxwKSrw4wlQaLvsJOyAAFoVam8LoZQ_4VOKpTeLB-qnIK2uUa7XLa_Ekj30e9D0P7wV96D9BHnbXzuwQrsRNE64LO79eTJsQIQgaedEmqJruQUMM2Y3JU40aIqpi0ZsI238NX62LLN7f-Ku5HhufE-iuKpEQq6md9XU462jzgfSRrKVV9-FMirQPw8rJBUePcMtd5sxKPrIIzrgNskFvciMlQOWTE5OgE9WhyOUR_jx1FFPJEdJaVgLxxV8-mIq_w0nl_ff6whjHNIB5rAs4MSG13FxhP7VIFjPRrM50HLVELNost-590NVYC4xsYUf71Kg3MUQgyEw8M6Gekm2qako6GBQvMezQ4idDvJhhcKANfF3P2szixJS-pvDkHxNu1xDpFcmkHyZKiPLUUrTVHEtRPdvLcbvpQd7jiHjcN1FxlwtACIXH5okNgP3zlKgbYPfFVSt8TkYdEpGqpfbHKJ4I18S-iEBslOOzqWNysDv0nwd8HfQx1W28SHKxRofOMbui2N1t607hfNweg2G-oVU280KX_IIMa7_emC1IF-HC9CLoyK-HKJpHb8KBNsjiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=AoZc-Hn_hdY7loZtEFMc3OutypyMvBzcwNTGYkB3LWa3mzUW0kjU3XOl53vnJHRPCviGsoVI_79d6YjP0NOF58kZezVkTKWUS1869v9SBsoxwKSrw4wlQaLvsJOyAAFoVam8LoZQ_4VOKpTeLB-qnIK2uUa7XLa_Ekj30e9D0P7wV96D9BHnbXzuwQrsRNE64LO79eTJsQIQgaedEmqJruQUMM2Y3JU40aIqpi0ZsI238NX62LLN7f-Ku5HhufE-iuKpEQq6md9XU462jzgfSRrKVV9-FMirQPw8rJBUePcMtd5sxKPrIIzrgNskFvciMlQOWTE5OgE9WhyOUR_jx1FFPJEdJaVgLxxV8-mIq_w0nl_ff6whjHNIB5rAs4MSG13FxhP7VIFjPRrM50HLVELNost-590NVYC4xsYUf71Kg3MUQgyEw8M6Gekm2qako6GBQvMezQ4idDvJhhcKANfF3P2szixJS-pvDkHxNu1xDpFcmkHyZKiPLUUrTVHEtRPdvLcbvpQd7jiHjcN1FxlwtACIXH5okNgP3zlKgbYPfFVSt8TkYdEpGqpfbHKJ4I18S-iEBslOOzqWNysDv0nwd8HfQx1W28SHKxRofOMbui2N1t607hfNweg2G-oVU280KX_IIMa7_emC1IF-HC9CLoyK-HKJpHb8KBNsjiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=XjQgcFW-JpalQL525YNilrEaBk0qDURXDqEQqxpmKooE-c60Ur7AxNraJG45FaCzS2lJcCXeDrWpZqMsG_hZsGoC1uu33cUUE_5y-j2RnOw18FSV5fGwW8dOBa6Q45NYCt3UMndKH4HXvdJu72l0JBG0uhysZchW_D6CmEKEY2FIeKo4MGqIAho9lSNviB-Sz7PlURXmc4Jb2ifYhc1yIHK-voYE9z4dzAL_pQc3s_UqangJJl3w8OrT_B9C2pp82dOMyLGHfXsxOwC94rdK7-Wr2LtdVB3LzIdEGtiM4aeEXXf3_uEUDeyXr6znftDo41pMmQNfq9ysV3Dtl_TqXX2ODKcR5EAxzmJ9slZj9gH0s1eKIsbHUAnGYIuz-L_16SEMNkdKHFLxlIc5-IoBjZfj9pIQOYL4oiDpn2AV8Oj9QERo9bMqxIg9BInrzBORPV0mzM0h0dsuatOI3xMl2Doz-FeUEo_uSGS9VPDbu3JO8_aMS-yX-rBOBZ9gKTm9azuFUyPAiK9iR9zHk5fvBrZEUioiq7UqdnZ00xKsWZio8rupVdMgf3BqZM1AVdTfWjISMjSg-HT4Zrp2IjEm51MRLtgpYndalIqnJofZducwTmFnq1AwgJzQPFRorzBPdXBqzWkucBblgjits5LEN6gg_BJ14hjuuyK6rGp5Qh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=XjQgcFW-JpalQL525YNilrEaBk0qDURXDqEQqxpmKooE-c60Ur7AxNraJG45FaCzS2lJcCXeDrWpZqMsG_hZsGoC1uu33cUUE_5y-j2RnOw18FSV5fGwW8dOBa6Q45NYCt3UMndKH4HXvdJu72l0JBG0uhysZchW_D6CmEKEY2FIeKo4MGqIAho9lSNviB-Sz7PlURXmc4Jb2ifYhc1yIHK-voYE9z4dzAL_pQc3s_UqangJJl3w8OrT_B9C2pp82dOMyLGHfXsxOwC94rdK7-Wr2LtdVB3LzIdEGtiM4aeEXXf3_uEUDeyXr6znftDo41pMmQNfq9ysV3Dtl_TqXX2ODKcR5EAxzmJ9slZj9gH0s1eKIsbHUAnGYIuz-L_16SEMNkdKHFLxlIc5-IoBjZfj9pIQOYL4oiDpn2AV8Oj9QERo9bMqxIg9BInrzBORPV0mzM0h0dsuatOI3xMl2Doz-FeUEo_uSGS9VPDbu3JO8_aMS-yX-rBOBZ9gKTm9azuFUyPAiK9iR9zHk5fvBrZEUioiq7UqdnZ00xKsWZio8rupVdMgf3BqZM1AVdTfWjISMjSg-HT4Zrp2IjEm51MRLtgpYndalIqnJofZducwTmFnq1AwgJzQPFRorzBPdXBqzWkucBblgjits5LEN6gg_BJ14hjuuyK6rGp5Qh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdOFtJbl_2L7BkDwzoj9ETs2Nc6-O3RK2vxTn9c7ZlIDU_X7NfzF7I5gxaeg6SSeff8AkGt96pPX11ligVQUp-LdIZFUCUXwZsYzLJSQ0sZOJyeGDpL3oDFw98Lf5l7GWjwzPEhEMOpTKTiNhOz-1LJ8hSSEtNDjjHSvTXLnrvCRxBf2DKDHu70ASjDYG6VPub_vvr8Wi8AYqMOykZBJjCmviSEeaFW3a7exvev_BJDHoLhQsKvmVTFpKKWlCPEyb1a-gkSE1h_9_3zX5zrSitgWX05Z9OmBPwz2rXJV2syw_cgAC99RY_Qdo07DGiE6OPSMx9rqV9il7jwX7xlM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq_dOW1Y8OYOll-yOhuMeUFBnuMJ89COYTP_VobcdCs5j6FQJAtHfj3XF3oaX8kYG1xdGJfy4Lp10B4oXIuZ9JHR0oiOwQ43ye5Po6xpcRc6biexx0FaqyGZM6KrVCswZK8_kxfG8eKlPb07vxoc39FdELEoVhvPpxDWlivMc-ycqR7AnErRVdmC1HvmiYf-gMRNwVQtq_toPlfaitbqFr3v9VfP-mkop5wl8V7YUwqr7gLXfS4PQTE-hCam31_mrPyZBCe-vbl_BMHkrboR3g-QDkpygJbXtlpGOoWUlxL_iNvVFVv6Q0ynN12kZnPbT1ceFXu_ED-iEBsvoCS3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN6ceS_sQV1KQr-stsZZ4BNBDCpEwor0M-QrhjQkZRQEtaInJl0iVZYPLQWImxMrsSaWcZFuLQSVg3G5UOusiYK1nGnVnxr8fHAW751Cb2hP05NP9IP_PpTpkbJ7VNSgD0dxvMaHvuqHpIcr8Ngt6zUtv43IfJo6u63R_f9VKMrmJxMCJv2fNioTPDAc78l0CarSExwt8K4f_8uTxQ4-B6BIHAekd1GmLb-prBJJRpqP-ifa6Zk7uOsHhOLQtY01CZ3NA-1T1qcEUQc01JVwiYPO4UfGf3fajYOaOAE9tT2lUo5re-cqS0iEIpe34DSbhlRy7M0CPARaxqOMjKRs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=AIiIN2G0cNIEBbpzvTQf21K0RZBvt4ycfsS85tU-KaEFQOD5yQNqpRq2qi1njquj-4v2gqVwwmmSeCwvhhrMPdif-Y1E2s8svHpaNI7smLFueEmDB5KZAM5Xt7E8zRjcUd8PP1jYxwFdE8re0ivypRTqraD2IrWsdz3GelTF_bRCcv36hN2xGf1TO6VH-k_ctwNzHduHrQTHQX_OTVUYEG0Ov0BMkyy5PNHo5aVZ6ZyZSZjJ51Jdt4JpB7cPZ-vU1Gt_AO1te9MskvP8KpmVzBIJ8NEh751r0cwAI-AGuFpB3S6H3987Z_KURS_s2o1u5trfxyP4abPDrbTiZIHe_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=AIiIN2G0cNIEBbpzvTQf21K0RZBvt4ycfsS85tU-KaEFQOD5yQNqpRq2qi1njquj-4v2gqVwwmmSeCwvhhrMPdif-Y1E2s8svHpaNI7smLFueEmDB5KZAM5Xt7E8zRjcUd8PP1jYxwFdE8re0ivypRTqraD2IrWsdz3GelTF_bRCcv36hN2xGf1TO6VH-k_ctwNzHduHrQTHQX_OTVUYEG0Ov0BMkyy5PNHo5aVZ6ZyZSZjJ51Jdt4JpB7cPZ-vU1Gt_AO1te9MskvP8KpmVzBIJ8NEh751r0cwAI-AGuFpB3S6H3987Z_KURS_s2o1u5trfxyP4abPDrbTiZIHe_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=EzyuMAkt6Z8NFi0TfJugofe1eFJbXjK84ZUu7Z2nsI0wPd8fN7KeWeYdtMJPgZPtNktgaEcotHgofeKJU4bHlV0KxvJQKBS7GBcOrzL66fCnlAI8wqPqJOzgOb9nyQbfCw74NiKcbVnEIUCk4biH6zEcWGqCa7yPNr8eYW_ViaCZS9ObKZj_pxLZVcNnEoY9E6GikBGn2K1M20-l0NOoNYsn4Sk36VuBtI0EtyLOAoi5jJC6eQofRNY7cNxm83C2ZKU4m1sW_wcWnoMohe0idfVVjkTL_1UGR4QAIZomUUk2dOO4grTqelaT5MYmAhrxySHi07bwCLs5jzHLU0Q7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=EzyuMAkt6Z8NFi0TfJugofe1eFJbXjK84ZUu7Z2nsI0wPd8fN7KeWeYdtMJPgZPtNktgaEcotHgofeKJU4bHlV0KxvJQKBS7GBcOrzL66fCnlAI8wqPqJOzgOb9nyQbfCw74NiKcbVnEIUCk4biH6zEcWGqCa7yPNr8eYW_ViaCZS9ObKZj_pxLZVcNnEoY9E6GikBGn2K1M20-l0NOoNYsn4Sk36VuBtI0EtyLOAoi5jJC6eQofRNY7cNxm83C2ZKU4m1sW_wcWnoMohe0idfVVjkTL_1UGR4QAIZomUUk2dOO4grTqelaT5MYmAhrxySHi07bwCLs5jzHLU0Q7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0DEUXHtznffEWXyPgBbRyvculHExv-nyVp5YNHco8ttw4MSar3eMcmH6CLQh1Dyyi20l6y3w09cWCBHbSth3a-yqKXjG96zUS0QgH0bQduhhTBMJaSGNm7POWudL_ODFQ70ivwCYPyxhGOsrk1icT1i4ChMwV7MKW--PGXBCC7Ld47iy2BWsf23obbgV53Zlk2HBPCC-QR5GoKC1HWAuv3Eb95LTVrbAwH8kNAogV1YDktO0s9gJIsLaKHdt4eQ-y5MqeChB6j6TQXvWJGbyie3jJvNDqKdxPOFw9bOS-FZ3kElAkZ9URwcUx3Me7ZRQ-SoP_LD_Y4pe1NBxUpIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtGyUdLZwO6iVEHzn7yfeANQVNqbl5Xg_VFmbwsjZVO7Y9pdkvi4oMYr30XVP-6Gl0pBr2Rqd163aYfMEZATrBKz9z4W8KS6pPsTXUqjGsV1MJTdqofDCfG_NrioKnsc4cdscAAsj6HVvmVDZbjrQLIQem_HUtMZYpvGmkwwtUsqazNP8eltJjoi5D76cOUl-0e4F1kBuig3Hol1djnTBUbH7ZbKkEmZKaqEvkKtWblJWei_nhEKJiFn3UUEd5bmg0wcSoDcIC9qL8_ahNleric-KYMyrRrB5sz4YcpZFFvnItAfsALQCjkCFcazjVYw_IS_v24SwCx6burKOpoBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKbA5IRkGRm_2mCUtP6wuBF-t9HP25kvfZ-y_26tMtL2jFUaaRXZsGYNrKtA5atrhN4YTV0LoOyNXTqZkME8LOasmT1J0uW5PX0hX73AL0m8srexAi_kWHq_vt4S6z8kSa9s0ybP3KDjLr7oi5B_0FW1yTHpWidlnESjCuzxnJ1qXvcf5hBQndTfBBTHuw8gumkuYPIOr00mZjFeQPBncrsIuRG6f1M-DFFEtF7y2FT-vHcUCCFxvNQky_FyfP7iaHQa3Na7ofFxdfY5VUfWa6dB9djY5f7BZ85vQ6jPcWXCcxCzqa2HnuLg-1Ewhf_Je-AD9sJ9yxAbNK0LkilqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Wek_gQ2tEBU-46W0P2DtDWdKSAayxeDQeumXVTu4OEytNMJ2HEpkrUt-a-oqdtWXxXPPycGjm8XzlWGy8w97UjKwpXuvzd59a34bVt0DyD237ynLc1uEw-wzBufnZCnHkG0fUZDxwBpQoAEvKBvqr-15BYnxXvRVIDKF76GC9c78nCUkcmvn49SIxa_CdKy98MnXslD61cF_TuO4Y2XQ5wOo9FL21igFHiChWTmHgnE5fTpyHmmBe9mcv0p1F8Lj0WLr-3K7EgtrSvaTOQeGFD5sor2np2icJQ4-PY-9OapX7s-LUoEl1x6gVnMgYjB7D17xkxfkB617TE0eG8OQfHqfVxgyQ_ynC8Z51q1txVCHziMoOPYy9y9uiTgphtqiOEa9F4F3Tlh0pxM3vbYNan3kV1soWV_qPTchs5UUUyC5WRBSRtNfIrqw7PXzAjRU6YRKNKe7Rm6PyBj9uwE0Iu868eqXRJtvoQImZyM1Iu_gOOuqEEVxaEqv_1UalFSWppHNR-IUuiRIM8pOCy0ymlhn_5Gw7W9q6Mu-QDRscP-XhVq9QPVVtpZUOnhl9voSYswODF2irU6ImoonaGi8sPsB0KOBLf7HT_XnH8CsvFWVC2ws74e5VMoXQSLKnAptRtO1UvAN0WiRXSCVu8rz8MaXKCoa_smx6A8UjzZaJyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Wek_gQ2tEBU-46W0P2DtDWdKSAayxeDQeumXVTu4OEytNMJ2HEpkrUt-a-oqdtWXxXPPycGjm8XzlWGy8w97UjKwpXuvzd59a34bVt0DyD237ynLc1uEw-wzBufnZCnHkG0fUZDxwBpQoAEvKBvqr-15BYnxXvRVIDKF76GC9c78nCUkcmvn49SIxa_CdKy98MnXslD61cF_TuO4Y2XQ5wOo9FL21igFHiChWTmHgnE5fTpyHmmBe9mcv0p1F8Lj0WLr-3K7EgtrSvaTOQeGFD5sor2np2icJQ4-PY-9OapX7s-LUoEl1x6gVnMgYjB7D17xkxfkB617TE0eG8OQfHqfVxgyQ_ynC8Z51q1txVCHziMoOPYy9y9uiTgphtqiOEa9F4F3Tlh0pxM3vbYNan3kV1soWV_qPTchs5UUUyC5WRBSRtNfIrqw7PXzAjRU6YRKNKe7Rm6PyBj9uwE0Iu868eqXRJtvoQImZyM1Iu_gOOuqEEVxaEqv_1UalFSWppHNR-IUuiRIM8pOCy0ymlhn_5Gw7W9q6Mu-QDRscP-XhVq9QPVVtpZUOnhl9voSYswODF2irU6ImoonaGi8sPsB0KOBLf7HT_XnH8CsvFWVC2ws74e5VMoXQSLKnAptRtO1UvAN0WiRXSCVu8rz8MaXKCoa_smx6A8UjzZaJyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NonyTJ-Iy_yiaKdh3mUzBxnHfZDYPuMOrDABcQDNX-zU2x9R9cCqAlkdXn-q-dUN3eCXlGNcIC7P_03Hnd4zvwVxNb7k4WDIQ9gOpM9vNNjalkpI8h_Fsa7h7x4HlAM9m7XXq1PEKUX6WNgJRutkO3zTbV-LZ4s1TC7JOFwYS2sYbr9fV10fmsBAwBm2fNzhFHAEjO7ZW_6Df9HdwJ4b_bSwM2DByt4a9JhTVHFeX1zLKedWkMfbJbdB6gR2h9jsH_xu5YXkfaueNZ1W7w44VBkJHigaUjsVRyOzXkIG73eRMKVLt7996ZY5o_3vGmeA5L7gigiK6XntkNrcy5Q1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=CW-BFsDXUiviSvymVFJxs6XcNpQShcE6__F1e2Q0i7WZtSFxQ8SXfBqIe2jjkmjE7ARvqy4gNcUV_4_XAl3CKgJUy3lfr0RzWCG8p6V7rz4lDjR_gj2LkIDDOMWx-YhjQVKhPTMjbvDkJ2EkKaV8-uZYN4koEmPsF-glap9n1uctMFJ_pLXWYIkKr5uRmy8zsx9YzZongKVA5TeaVRF2zkKT2FKaGp_p1-GQ6VZ42Ks7c1pe5A0D1OGgT8n4AEBpmZSig9JlyA55fKYoar_YMlaq-CHRontOd2uAJXkPvoP2NEM8QGcm28L8HjvW4uFQM3qOUeA-buflhW-tFYtU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=CW-BFsDXUiviSvymVFJxs6XcNpQShcE6__F1e2Q0i7WZtSFxQ8SXfBqIe2jjkmjE7ARvqy4gNcUV_4_XAl3CKgJUy3lfr0RzWCG8p6V7rz4lDjR_gj2LkIDDOMWx-YhjQVKhPTMjbvDkJ2EkKaV8-uZYN4koEmPsF-glap9n1uctMFJ_pLXWYIkKr5uRmy8zsx9YzZongKVA5TeaVRF2zkKT2FKaGp_p1-GQ6VZ42Ks7c1pe5A0D1OGgT8n4AEBpmZSig9JlyA55fKYoar_YMlaq-CHRontOd2uAJXkPvoP2NEM8QGcm28L8HjvW4uFQM3qOUeA-buflhW-tFYtU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwFPE0ztbDvjTvnXMbQFCQuYi9TGkTzV7BEbVVpDj_RyQ__7EBjR36Gi6NYf6A9N-v0EktfKdCvnve7lNZ0Te5xtb3QowofF3y_Eq8bDZyC3fEMAkG2S34bGoAMSRspHNxCxbekgGc3LbIECjL1H6tVR_ICYcN2nzNTzLsgPFFCOZ3WyvoPFbOWZJRjoKVeixb5XM13RzYrvDRd6HRc2nPY_qBBMbNFNX62lJ1q8UOrH8HXwHd2hFTwP-LVQKjT6DiEoYZ8GwzXbM4EQOXkuIut16-m6Zwg6nLrlhfutVTD4gLbM80NUbF1ZzVD3TLFf6_DntTVM9QvHj03IMWRirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HzqKTp5Vo7Ql0P0Hn5njZoPsW6jLWJPiSlD-Jze0DWpyrGaPi79NCNJ5BQ2K5q541tU1PPdIpmJd53fzGB3cRKTGlztIN0LeOFs-DgSYOoEtKSYHKQogLVH_EczK-cQyXwHrZ7Rh1s7pVd4fZYhRDQT_1KR3Q94o3ZI7yeuNLr-KuDaZekhroOA7iLhLdnQxqI2fGBmfow6kttDFSk_fQRJHFY5aREURZ3nt59d-oB-AM8zcjJHwePpE7WpwZMGQqv9wTqwQrWCaIMaIrtD27-08DNETP3VXVDaTNyUKFVyy5Txw-iG8sK9Wdw6vQwP9RFAnPd5NWkW447Hx6Uts5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Op3CDtRR1oO0I-czhYO0AWxu28FwVR2oKuoD3CC0VLrZ3wfGt916m456fzDfrg3jPuWWqk7I8g-8wVG8AwmdJuTyAaXvIoMT7RStw2BHn7-dYbRhT_t1NWfN0mWkA2N7vhOG49qAwq9RlaBrfOr0uMltTIwyH7UMUWgl4DYPlZlPjBUYP1sFvEsh6hVaA65cfLvibyRCDU15WBNm-KAXCkVWGLipt_HWGfJAJjqDqDUA_GeIGRP3Rta6ytPLXtuLjpN2Lj5DSyKMeLBxrQv9XOdyxPSJiF1hEhvw-JbFDZ3HtgHlmsDRTpRXepnZhX1DCRyKa2iustJCTbGDyOApYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=uwMRiHq5oecX1v4-IuLtSgq1_enf453g6saguIIYBGneMNDmK1hHvTdr1s7ytIrhnoehUsbs94Fc_kvm7WVu6SEMzCWeB02oQuccTP8zAyKJ_SG5ZJg4FhJvJaHO4S8SxM4J0OaViEV37FT3EE_OihtV37EcYzksT1HLyEaDTR-nqxGDte5ojV3slmtpMuizLIRo7jAoiLL48Y7ZquAAn5EekO8AvuMV7N-8bRX6aJlwADJ2NHZ7cG8-vsTrWU6O7i51B961Z1buE3KWkl5M-jVTTGV1V9cab4MkN12K14Hk4FZ8aRmGg4If4Tc6nHhZz7SDwIOf6nkh3rzsRdcfww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=uwMRiHq5oecX1v4-IuLtSgq1_enf453g6saguIIYBGneMNDmK1hHvTdr1s7ytIrhnoehUsbs94Fc_kvm7WVu6SEMzCWeB02oQuccTP8zAyKJ_SG5ZJg4FhJvJaHO4S8SxM4J0OaViEV37FT3EE_OihtV37EcYzksT1HLyEaDTR-nqxGDte5ojV3slmtpMuizLIRo7jAoiLL48Y7ZquAAn5EekO8AvuMV7N-8bRX6aJlwADJ2NHZ7cG8-vsTrWU6O7i51B961Z1buE3KWkl5M-jVTTGV1V9cab4MkN12K14Hk4FZ8aRmGg4If4Tc6nHhZz7SDwIOf6nkh3rzsRdcfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYAZuwKMfMGASGO84jbj-FEs2GEzdHTcZTF1pTIJbKRzzC4_xxUJOpnVIIKwsseoIANazqtlBmrnaV7ScxhMJs-WRlWD_VCx9S-Qbt5aiA2HdNWzL_6PUvqMYGyl3q96u4A1W8is1bbHs-8UFCHhfBR8k3MNIjbaZNPhZS9FtF7PUsMRlNn8hwF7f_ZjQjHaCbxGJ5tbK7IXX-CbS5jZh5o0nzXT5bcW5YyU93m6EK3G1v3WJ2391DJNHsAuo6X4TBD6g1HF4MSXPboNe09w7ilDR5yo8Bg9qsybyW-rq7FtOfjEXOXU__T2NAEFYiSufFKzsvFxR5IdUDr-uPjwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2zdI8opR2591gZk99WvUJcJ2IAGKMqBXQOU3_gFZ1SsjAAABLAB4CQReP50Z5FMKl2art5YpP9iFaP3mJNkknq4N7yHYqTrbjy0XRnAVNRwSa2r780zmxEP7OC5vBdkvhSJC8JOzU5i40GVzLK9LIiFMoU5PZiuaOSQvUtkjj0rt0h6OZtllEEPOKbz8xaCdzQf1BMekZDLNUAwOVXMd36dBYbMHOH9xFTDMbzVsxCiO-acdUn9MeGrks3LZSBOoeEGy7XdGJ_Ohhkc0LQhm9YAvDTqRIdrMGWcK_uFz7CeMK0XSuF-jWxRYJU73KW3E7IDz_DviKVCPQh5wDv8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaCwobe48N0I-Q-v8waBr7hPoXGZcnLpaEtDbVMyS9kyNqgCMPtJ7YvgVVGqzIBPYkACfKdjzJHDFLbYyAQzKH5B7U9HOWF710SoYgNy35UND5ly69uMT481FXf6RjXheD2sam7lDBjJYR_453XM-Pp2TTwOxMm4fOlSXWPso1d1acgVmCxfKp-0F39VYY24rTOam18vYmcoCAbRIrMIfoYQ91eWX9MfmQptZ5NoXoEVQVC3RRTPTXlz_7Rd9L3PW-fcor5W-WW_6v3eFZN_zeuOB3HWCZIgzyRFGlnBI4nH4hL-PesYm4wKHkkNNbskD2b4QNl3mbhYmZYc3vqb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPpdCVijlQ_VVA3UAnhAoK-X6XFAboSfCBYvzDf1KhJQgc-5Bip6j3i1-URP5GPwGzaysDH3rKfQxXgjIf4seuGc-EU7bbNNR9rTgbbfFqov58O1qaS-DlQbHfZ9F0sM3KbY2tH4WpenfGZpSnl9IP2fDfVbTvtJmyDrSRHPkxpU7WzGa4otJI7lKRNhY3MvIKi7Xyzl9U833l1VrkaILVv6UHFV6z2JBjxhlD2lUM4ZsdtR7uOdpZRWnraSnlR1s11NpFkDyf8fYQbdcOLTplZ_WbJRWnIKn7MyxENQrFQAM92TAEul-RKzyXXBG8C5e9hyUKJNgZ42YHY9rOJuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqfQ6riF0vlz3XzT8DnTFxCtK5gkOpNcA601Rj1sy_4fM6c61WVyzlejg0pdWcJXogtGmXUd8kLWhnsXT6-ZQU46lmpHmheUumeejP2qSKBsu1UWSWHNIm1v_fOtuNQUIbvrkqHqKC24_UDkzJ1XZnctZSRYClRAl0FN_7qKM6pxZVJBD_xJcmWzxedtDmjwrx54onwX2dyvJZw6kblsNH-JlZN_ZkLduVVtgTnYu_5oXRkP6HaFj6gq0Tqj2npO9abkvMeDgPOujLTcTAuOQt3DBvaDx3QaWGFao1-VHQOq2hs34sH7nMsa7S03Qet0FX7653E9fbqmQ57vQm2NuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM1PxM1wXjETrGUz2_KHH-8o5YcD_0FUTMa66umbAvEMCKnS0o75z61sPqJ7GaFlM66U3qkbQpDFw1BEGy1zsoZ3zUP3F_VHTtXdqa7Ui_a_5jvH47QUf_V3yIiGxzc41g_kYlhmXpDse0lof-MEz-fM7hjdG3S9Zyv4EicW1YD_gBWojVxiAGhl5aeJHEFnzftMQYPZkLNOfgux_HR43olS52bCkxmi4Y3upcvfLId9JWqBd7nobz0cG2Ga2vp_QcYkqTrI8Z-uQ8mhAV3DwGQG2tqSp9oaYB3vdy5y-4oDlLLMYF2JaBrfVRuHPCWSvFDgjUVit61_ku1XZtSDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1ZNukNncwJTYyIEKwLouee9KXSwPivPzs0TcjvZGi0ll5E5JJPnZq9BSWfHSjJPH1d1Dsl1HpdBH59BOQ_HbWxkXSTjvLjD6loTTKBDqbt0j2m7gQLYJ-_6Qdo5aG-sh8ViZrrcbUb2lPQ7Ch9nnkbYSb5uVeiQTw3j5LNmDTzsP1WE62BlmpopfyBzio2W-Edegk1W65h_iEt7VkOXW7-d9lyDMDsq3ovFyumJHCK8EaTiLsWAMWmdSoisAv_VZdYDzNHBzGsjOxEtJSWjEM3jl2qNXPzJkhuiQhhROZ-1akhaDp6ovCGMWWzYSOjReOc79FOaU3E48v414ig0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8gzhgPzqwT9e1JpiVby-oJiJ2g3Zim28HQPOmdyyRArLx2FxmYNX7w5nUKfR7gFn8ll1wiSrXRi4wRxvnTyT2dT01ACMPBs7eNeadREIKle-If-pmK1-b3tZdUC5T9DQK682Uxxf9GOOO6aLKo49dq3NigT0aBXHk8Tk9QRXCNnRFASSe524AkERnlOB6Z9tZV53GqH33WcgErNAswHF0Mc_7S0ATgAk_3ipRjKt6NSRSP9vXnfQpF8OhFApI95khC0rx0Z5ae2giR8cHwG9sv-7HtDMb2xaSLHYKH0vjpog1YJuS3S2MTX2mS50HNws0C_DHXyskVosq7Osu4gGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNA_sYuy9w6KgZrpl6faO8qgadpe6mwT81qD5f1-IlzeqFp2TnrJqNd1usA5F9MdUgMZLjf0khPv4RznCRn2bbziFs6iRRUGasB6xlKjzbNaDE_PHWKBCTroUcBx_4y0f2vrprTmnHDy_JD0B7Ask2tIPBXShX9KkSkBpqmcV-pvucZYbIMaGfGFY4uL7-0n9uWfUXtTd25-DLJ6NobYwnBtNbyFlmLT6Toc1Nyi1-LMBQO1vHMNVC4tg2l_2X8dmKEI7TSKtx8iBOIV4sHQLF9aChq_Jks9OWkwpIOi40vlHCIzqcvdAov07nnkcPCG6ARKZncLpddDxsisVl8-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFwy4s3ugPf2hQlh6q8uje_vOgQPfiCkned2Lqi6ha8YNbCSE9bUxSoph951z4Et_k6W9xoNMnsVHMOvtGOR6V3HtNULLI4CitCFSOUVabyKN0xOVtCtPBiXQwvi8VrqPch001gbUUtOUoiOZtd2loCN_3_YD2L6y9iC9b1jRGr6gy_LHKzNpFr88s-9lDVjzpppOhpRg_Zmknn0IK1CCsUx_aC6cpeRVI-mqSq6tgEA8RGgLk9qwORMPyuRfEkEBS0lJhF2JbjeyejR4lxMGSx5ipk-WqyAB6gBiCHe5QWMeCGmA_pHv2YtoNT1DnNeeYzP1gRT5OdQ27mpN02eKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPtJipPUiRruBheCQUbFJyavgDdyENEi4iKY1XBY-S24H-JmPnuKd6ejGuOZPY96aJfnYwedsX3yUV8kTBaeJ0lcJJ0e9-hZe0oWFBpGrG0aHyN06IT2_DCR16ZgoEmpfJP39poEt_PiEAEwb5NYLACc9ax9ZzkWVtfWoUIOzFLnjou3qxPvOz89T35ICBeTusqMGY1o_AFiSfTs5i86BGJBY15T93HjYu8j6Knr0IV0C82T4tjJjqs5_SIxwXE5umxSzmndlOJgOYIWJEP3N9eJD4-J51Lbb0bsY1pzug_iiHpQtoYcPy54ZxYpFpWeZe9SFTSq55qC9mGKLQvxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkSGFCv8r1LXrP3qUtXO1_oTWS_Xk5BCLL9KerOQE-X7hcGV9yLFnrPyrPUHQxNRjgN4uJf-6cKr5wTWWX60aFatPqo4UZI6n7nY7zXXofC4RlZApGTbtuJwwSw8P-N6TuqD8NlPUjFJ2CC7nAZi4ATzsnV6yh8IKebKD0sdZZzRCRfcLRS6F1UU3_H4KZZ8qnz254vhw_LEmfg1qgbuBu8d4dN_yAT5soL67P-eyBltlQCi3eurMyqi8v-Q3SjLwIprDy9MtnSk4TTX4zYljZyr4Qml5HZME_AfcSWGS3tsfmCW4IvestX3UTgp4Bw5wwZqs3B_LzLZVnjtNlokzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GttHjs-G1gEn7MUcOD2pRH6MBt8DJUgOBVProGESA4AlLZBEpqpUtnmp7au5SHAMnwIZtvsbH3RVbf9Vr-TRDEiknR61xUjf5alfmFFHzqWdTUQdr6UTQGWr6GAZlCED9HeUdLEyCPU6ScG5CSal5APOIxdLdsw15nHfMVzWXHA47ESJf8bJfQPGAhQei-u4PIM2n50KXNM5clECgKtLRcARQHFSykFAXPfKfu05kSXg2abFUZJLD2qICu-nGeAVRx6Cez2bcjA04RLTM7B7QCOFF8J8f_H__g2-BvAjLj6PcWvJB15iVGZa4MWWkaXViVziHKQn58WGvN4oqQgfOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnNRpwLAgBAr3CsWU2VWm1ky7O3UCYa621vcJig40UhAnbchZvDVMZQr5pvzcZ7g8XzJuyn9dyP9mTIWU0L3GAnSNBmBBSniwwb-_SpuJS1cGwKE2Z-VBNVPn_Va3eP16dmYYU6rx-thprNfa9CoL85hPJaJdfDiX8iBBPbcIeskND68tvosfzhmyPCzHHfWt92joyV45f3x6ybjF5WqXf8HicCkNdvE4W95Ahho58yb-5-It9dhJAo8G2YzQAINREQlcm4SHxXyNX2GH1VlhyozpaAKMWN-uBekVcP8wi86rKuqDDB3M1-Ga9H8riilhZYe65IRi_jcTg3ULN_Y0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=T4nKF80hbkC7SCKTKAbmGmbRRXIhfCBUNSv9g97F-X36CVKEu90RVsCndFQtZ0z8asBrL4if1LPcjqrdN2vCiSWauQHYEWT9UqwfeyA5YXWhpGVlMMaPRp-aSilytN7W9Y6WhwBP_xRlbJ8inp8reLDgENLX2kkOFY99LjUHrfuygu7kqx0IqVGqgspqkpu9vEqlVabJRLqsJ4W6jfwhVNOU4AdYNal7J7UM0BJ4F0WWJlhc14r7CCMlsrmN2nEvgGu6k5Be9FErbJPH4WA36fzYFcuIM9UpqcR4BNYSC-tRoKa-nnBFDhtXSscn9BsZsbr2H-TRiNLtK4yhh5kiqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=T4nKF80hbkC7SCKTKAbmGmbRRXIhfCBUNSv9g97F-X36CVKEu90RVsCndFQtZ0z8asBrL4if1LPcjqrdN2vCiSWauQHYEWT9UqwfeyA5YXWhpGVlMMaPRp-aSilytN7W9Y6WhwBP_xRlbJ8inp8reLDgENLX2kkOFY99LjUHrfuygu7kqx0IqVGqgspqkpu9vEqlVabJRLqsJ4W6jfwhVNOU4AdYNal7J7UM0BJ4F0WWJlhc14r7CCMlsrmN2nEvgGu6k5Be9FErbJPH4WA36fzYFcuIM9UpqcR4BNYSC-tRoKa-nnBFDhtXSscn9BsZsbr2H-TRiNLtK4yhh5kiqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muwpZy3XJHbzTnmDAsUrRch_sY0_lHchrJ0IL4OezYmI_Vf5HY8u_xltri3G9Az_fqq2GmQJGV8wqMyZnL02NezsfVsV624FbQFYkePZZ67xDEg6Ttb9rfVOmWngfZ5saZ1VS7fe7O52lDWwo9ZkyHLVkbzzQsvyVdPKB0JEk9x7LZ5fTDbsXv6-WIon5NK4KLu2eTeB0m20Asw8jzCk26XPNlp1sWVpaWpKUDA0NacwxwwOkEEHtbGz4vvmiyN5ApyAoEynh7dbhnBk_MuBn7cciXnKOV-wE_BXvsARNZ1DqAW9DuOB6gYKFeSa72wjkzHh0b3m2C8DkZbNLJIe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBQr2mDwBfIA7BVhuJGvbi6rRs-y8aTr4ZFAc3XJyrrH_PMq9_PNstITCbh5Qpt8ZjY0I9eUATy1G2_wyWK5Ekpl6onqXCISnospe_KPMOFyra4NgAV0Hay_zHWwsDWdRdn1wpbKxMk0oF7AE8w_W8No1jLAqnIF5QdHj0QV4mUqlOTYHZshpkJHCGNKKx_v_PZ9Nhb62_AJnqxOqGYtAsW_MVMKO-k1Tp0OWuh7X6Mohd8feRXHw1YGyUCS4C7xWrvz1uJIgGx4WuEJiy4DbaoYKdNISu2jffCerD9WZ7tIM9rvcl3Q-upPafZO_YHVwm7VqD8XxVE-GBSiOg2_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjQo3jL5UPmajwASva1G1sVFc1VrfY1g0wL4pbZafO9MMjfkDch_cwde-i9Idtq0LUqw_M6_jO7kKFr4Yy4M2QTbDVue1vTn7ojQyLXKmhFXM9HOkmjWIMc2gxGGiWPJP2dQtakYdZarJB4TQhbM0AWMV_gnEf3-L0qZVZ7qQ7poZS2gziAoFdnPSDH7D4ITsRwExZHJktFjQZfLFlYWMlttxNTKEetpUeGtiiIvTEfESwyLkR3mq3eZmxkS6MrEtKje2iLsSk2Z9pohu-KP2HLBo1vJbD6tC192z0P_rZnwGmu6NySk0456SuOk3DyJMeCo808gaGohzn6NZG6IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0b__Pyn-tRYEsPAUTt3V7z25tWRTT0LDHFQCMQ-ivcyDuyqpPLrFy8aC7Uo0Nvb2DBhya5eT6-F8p3Zfvmspdfs5KKsLE0ynEz1_svszSvdA6L_XRg4zGMC8PhxbTfTNOQep90Q12iphQEQEQT6_w2vbeUuum-iW4-rnwACSeaSwfs7fk6sVxppCqrHg2o5HjprQlYygiFTjRvu_X7h_NW0mwyRDx4czun31VnggeuSjB9-h1ti5Opi2w2MvJBPFDq36nV5Thg4sj-iSoO3Agx2nSULa3F2Y1j43PP23ntGMeHPYohFhpuEWqgcgoCr2yHJ00fomdvjCjWoY3U4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=VjxqrfEk4m9k3oPjUWRAtHL31n3kx4xXWYGdps548rcYIR75QhKVOhSzH3ua7Fg2swEile0bf8q5qiOJI3eEamUKtm1VDmAh8mWd4Oo2HUlKq-_IQVc4nYZikeuKkDMsAUK5uUCgXzzbRrJqnaZtWnoSkTKTCIfJHrqSz5Fro-p9tA1joRBV17nYeWg6rK3I0AFvIhQ9fpHj6DKpmtn-3xv45GcuvJGYtSBAsnLrRlJNQ0Wn9AM41dlDWr3P6GGRUY6VhPICn9Z-oJzYZ4SbGElYOUVQrLVsWduzvcYG5AtujeGKIwHKL8bHZmjJAtAsQ4bQ2QKblPcpPOjH84HmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=VjxqrfEk4m9k3oPjUWRAtHL31n3kx4xXWYGdps548rcYIR75QhKVOhSzH3ua7Fg2swEile0bf8q5qiOJI3eEamUKtm1VDmAh8mWd4Oo2HUlKq-_IQVc4nYZikeuKkDMsAUK5uUCgXzzbRrJqnaZtWnoSkTKTCIfJHrqSz5Fro-p9tA1joRBV17nYeWg6rK3I0AFvIhQ9fpHj6DKpmtn-3xv45GcuvJGYtSBAsnLrRlJNQ0Wn9AM41dlDWr3P6GGRUY6VhPICn9Z-oJzYZ4SbGElYOUVQrLVsWduzvcYG5AtujeGKIwHKL8bHZmjJAtAsQ4bQ2QKblPcpPOjH84HmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=V2zmQOOaTengLgU4d-37SMuXylF21UC6P-z7gDD835hnX-dMgShJUJG6JkwX6enJXPcHxuIHK4XcDsmwuOMv0-QUdghGbwUxN7ysPkYGDX8taPdBKUZDjLSp3f2jRxrmrqctA8w-8bDr-FoltYwdtWIswl-rn-FddBcmW52p92B4OcpcfDSvMZVzO2M0uKjpqi2s_gf1TKD8hx020FdeCJvsMTzmI9lLkp3na4pkxywZrsHP-DZn5uRK7-faaCY88TE4qeSNqtzyl-ltVuMG8v9ZA7gzYWLT6TBZY86r21bZCBc8nbzVN1hsfylh_nYYa6eAwyHeTozYLe7NPOd5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=V2zmQOOaTengLgU4d-37SMuXylF21UC6P-z7gDD835hnX-dMgShJUJG6JkwX6enJXPcHxuIHK4XcDsmwuOMv0-QUdghGbwUxN7ysPkYGDX8taPdBKUZDjLSp3f2jRxrmrqctA8w-8bDr-FoltYwdtWIswl-rn-FddBcmW52p92B4OcpcfDSvMZVzO2M0uKjpqi2s_gf1TKD8hx020FdeCJvsMTzmI9lLkp3na4pkxywZrsHP-DZn5uRK7-faaCY88TE4qeSNqtzyl-ltVuMG8v9ZA7gzYWLT6TBZY86r21bZCBc8nbzVN1hsfylh_nYYa6eAwyHeTozYLe7NPOd5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Y8lyhufddOiYX7iMMaSm0QKDm7vvTCWREilWJCxVHsKTzMlN84FAXsD4cbF2eRNPxT6aqm1KLMWjWon6bRDNcMqtDW3eGIyfVBFAeKxZIPcvbh-ZVMUQY_iHdYADezSjTilja5lhCpQRdrX2zfVz_etYW200W4s3NaI7c9YrS2XNMAQrdn5pcq4OBnoIe1pKADj0MbSx7Zh9fllmO1xVam_UyHBZVsSkZFFlxmvOmxGyVhKJGjmKCaEVzI6bDtygtEQP578yJoA1CRh5TgNv62DtlgDJtxNDopzffb_SAbcpALiWxWXJzOPPRq3gH97cQnfcVthQ9yPO8Ebm-Sx-vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Y8lyhufddOiYX7iMMaSm0QKDm7vvTCWREilWJCxVHsKTzMlN84FAXsD4cbF2eRNPxT6aqm1KLMWjWon6bRDNcMqtDW3eGIyfVBFAeKxZIPcvbh-ZVMUQY_iHdYADezSjTilja5lhCpQRdrX2zfVz_etYW200W4s3NaI7c9YrS2XNMAQrdn5pcq4OBnoIe1pKADj0MbSx7Zh9fllmO1xVam_UyHBZVsSkZFFlxmvOmxGyVhKJGjmKCaEVzI6bDtygtEQP578yJoA1CRh5TgNv62DtlgDJtxNDopzffb_SAbcpALiWxWXJzOPPRq3gH97cQnfcVthQ9yPO8Ebm-Sx-vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2tQAL1fXYlOUhoFHTkqsE4MNP0roSU5VHCudOXh82B63p4A0GNLfN5kJ-iSF4SmiRUDVn1aaa9nhqMGpjXw6_h_rQ4Bn1OHtnT_iSDd2m7dSfjWcJgVImQBIIHZsKsozR5tImWGCbBqCtw_syhLUVY6rsST96Arfj_PcuKYUPCxSRbylXf7_of31FSaXWK1ol598j7dDdZsJOCakVEkUNEroLlrDYVnGQK_YkeJPwghOxqui15wLhNrjRJiFWxKa6og71iM3c_hazCGcV-W_32dBkgrF9Gb3s8jXWyXcU4LgFQ12dWbLw-T1HySLevC6iP2p02tPXEEGTXeZ1z1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=aX3-2XtdGIQJ9AMH3FypZ1ZpgbcMM2uvOii7yDpZ1ylMquVmbzzrLAZtAds8lMBDiLnYYOShEMb7XhJhQuYgwT5myOM-nGqVf0CGeDjL6JOx6UzI8SDWqvKJ72rr0l0jNnv_GxudD84ZMZQA3CfMG5vUcor6gWbsQHpNmuLFVGtMpQw3NlTtLaIGWyXZ3ApR-4MdUgJwaiajKHbmS5rTfVdMMJHTD6SnSMg-gI0DLIHAY-eJ0CIBf2VKowDiJhKJ3A-hzaD57YXzDxo4m-7yh94P2r2vIlU9cG7mcxgBI7Pf2-AHBMWzkRyDR05kHbGfh9WrVOxa7-MI8MK_zyWeq20GeFCuRlhn1L4EGIMtwTYBw-QXOvocrYJ0RyZqkQFQ7SffE1P8zE7_aqOQEMPMyhE9KIDDFy1oADspNUb5iWSsunSBUC7cBz_3VCyv-ZDH7hBdg56hO-mV5MQNLUEX6yG6aj130T1of9gAVvfadmCxfNwGWI5KEHaqJFaeu0EfH99XgO0T_RIEpSnx4VE1KP4f3igRxKsnVYwahZPLjasNb03PH8A9twsYCchJD8hb6falbn2FjfsZh5N6rXpNXDpwNLGLPpMUSzdV9aDJkoSvXbVlu6hQn5NvXs8O2v43s-jteGoVnstwe9Zv1cWW9GCdVBrW9vkE7Mr45vg5OuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=aX3-2XtdGIQJ9AMH3FypZ1ZpgbcMM2uvOii7yDpZ1ylMquVmbzzrLAZtAds8lMBDiLnYYOShEMb7XhJhQuYgwT5myOM-nGqVf0CGeDjL6JOx6UzI8SDWqvKJ72rr0l0jNnv_GxudD84ZMZQA3CfMG5vUcor6gWbsQHpNmuLFVGtMpQw3NlTtLaIGWyXZ3ApR-4MdUgJwaiajKHbmS5rTfVdMMJHTD6SnSMg-gI0DLIHAY-eJ0CIBf2VKowDiJhKJ3A-hzaD57YXzDxo4m-7yh94P2r2vIlU9cG7mcxgBI7Pf2-AHBMWzkRyDR05kHbGfh9WrVOxa7-MI8MK_zyWeq20GeFCuRlhn1L4EGIMtwTYBw-QXOvocrYJ0RyZqkQFQ7SffE1P8zE7_aqOQEMPMyhE9KIDDFy1oADspNUb5iWSsunSBUC7cBz_3VCyv-ZDH7hBdg56hO-mV5MQNLUEX6yG6aj130T1of9gAVvfadmCxfNwGWI5KEHaqJFaeu0EfH99XgO0T_RIEpSnx4VE1KP4f3igRxKsnVYwahZPLjasNb03PH8A9twsYCchJD8hb6falbn2FjfsZh5N6rXpNXDpwNLGLPpMUSzdV9aDJkoSvXbVlu6hQn5NvXs8O2v43s-jteGoVnstwe9Zv1cWW9GCdVBrW9vkE7Mr45vg5OuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=TD7FvMhYXHoy0bl-Z-9Q9Pzj7GIEFtGD8PGmCo3SjhJPW10RfEWL_YloUIoTpIWJ7kHw2KUE8uDW5BbNAs6vfbBg5PvzNmL9g06EokVJQ9WZ_GAg85226L26sK6MQNmiqPPise4NRa9VYppRBvaBD_7rDLXDGNDHYN0ua3EM67sATU9NMBrvtbPoNFBWFT7FVrCxp6nNeUUNtpr3N4zyprrTICDEULErSb6YQi9KimN2XgxZ_SIK91zjOI4w_4Ozth894Vu6_qalIT2BTb79VQsr1p_CZZ5SY5gYiSQfVqb5Zl_a0OTHTCJj15C73Kf8x6Qu7CLVbRx-c_xjOOVX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=TD7FvMhYXHoy0bl-Z-9Q9Pzj7GIEFtGD8PGmCo3SjhJPW10RfEWL_YloUIoTpIWJ7kHw2KUE8uDW5BbNAs6vfbBg5PvzNmL9g06EokVJQ9WZ_GAg85226L26sK6MQNmiqPPise4NRa9VYppRBvaBD_7rDLXDGNDHYN0ua3EM67sATU9NMBrvtbPoNFBWFT7FVrCxp6nNeUUNtpr3N4zyprrTICDEULErSb6YQi9KimN2XgxZ_SIK91zjOI4w_4Ozth894Vu6_qalIT2BTb79VQsr1p_CZZ5SY5gYiSQfVqb5Zl_a0OTHTCJj15C73Kf8x6Qu7CLVbRx-c_xjOOVX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfI5gCVjHkKAcsADlR-cvdarC5lXjHXl9DRZIik5bhp7z0dlaaieD4DQCzuYgEbdmKCVu4kPTijnavhrUTa8uRsOmaquFThn9KTiuTWkgXQSl9-9di527hEg8cyqQBVy0SfG0qqtdIsU65lExUq4DehzEqPn8odp5QJ81-nbbCmRFRlict90jaBxo_DAT6_0p2ClKJkdzhuN0Lj7WkJiaCT_j4n6jrLpL9eEQBnzmftsLjKuz8MDeUX52V8_1TbVwptUr39nVaqcdfITz9rCShmKaEfFZXqnfODf36TFouwhUmJjNrsEEsPf3m7PiqCFhJexKOybXMqsBHLXwNOc0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvmI3t3GUHphr7MA-CwCYlR1W3S14O_FuSWFPfrmG3oo_e5TXdQnRrlhIbDjA1T5LYVQ8JAriGMyb62yU2RgPxYZC-k7V6I901TdSGWD-KnBd8n5GTSBmHUxoZEDqghYR1mGyLrHdEuVQ0KUHNNAyDbjgnEUPObSpmhn8tRLVBO7sfQ6FKNZDNVwPTwC2gP-5QfkawOcn9RVgU_XoPfEPb9l-A50XgrYGj2pnQg1VP85gP-9565afd-TFqyjvBkz8cfM0Dh5ltwjkqqpqltFrPJxbpjCKzCG_4lrXSBuDLq3WImXSGEk6l1QbhFs5RmKZf7JDIsrzdxhhOYiYsYbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=MW_HCX6T3BD9euRKIcDE6GWQHuxoK--sXtO7RqFmfOhpGFeQ2qVtGxDmWaXhYMKwKEMa70JpaYXjW80suHPQIhzEosTsHdLpyfqEzm31oSukX5Y4DYLj1OPdixU6LtIjUIzrhWN5-SlSJJwAgYP1vPGpa_YyCBELqPjUPc0wRqq0MNzk6UGLpbQXj5JfOpnVGFteIkYyFHGEUR3BKknqKZMZPXjS86Ynahl-qWglkcthlTJxStXnDll3dDJ5XMzva9aurX09PTdnhjJ9DO4Pkk8Q2pceR0XRyRbxE_CSr8W4hXd-OUojqTRXZij-AOeRujc_iTZTywlsbQJNT9VvCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=MW_HCX6T3BD9euRKIcDE6GWQHuxoK--sXtO7RqFmfOhpGFeQ2qVtGxDmWaXhYMKwKEMa70JpaYXjW80suHPQIhzEosTsHdLpyfqEzm31oSukX5Y4DYLj1OPdixU6LtIjUIzrhWN5-SlSJJwAgYP1vPGpa_YyCBELqPjUPc0wRqq0MNzk6UGLpbQXj5JfOpnVGFteIkYyFHGEUR3BKknqKZMZPXjS86Ynahl-qWglkcthlTJxStXnDll3dDJ5XMzva9aurX09PTdnhjJ9DO4Pkk8Q2pceR0XRyRbxE_CSr8W4hXd-OUojqTRXZij-AOeRujc_iTZTywlsbQJNT9VvCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qDh1SrKc3GNpiQNWvc-Ufl7isfxK_eynp47P5eOzUH8wWNgN64n0U1V0ZsiNv2s_MlI3R5W98ruXlIf7V3VNnxJ-ORnO9SOHI65JgQPcyCat8n8zrWaGT172GK_cvA0QXKVGRQcMHP11FGN8Yn-In0oux0imwoDbhT8knndamGO9pCszoW7KGnCdbKtK7ta3j7b1a5w79H9BemL4Q1BPgEygj-cjnrNprnzm94WtS4rfQrw5JVbhMpCaZzfivB81JN54hJrSXRvdfKgpTwj1VAtVYbOkmyNOyodjp8rWYH_5cPhgVOIT4QL9fH9Pgy-WRfMb_rmmKAhKH-9mV3lLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AENRzkii2wwRbEjJ61kO6FICn-mWlkZWe7ISGA-a91GbfaUqEtXfaa2qAS4-VBJq8NyRhTkB3Meph87181Si5AJHY_oq58KwA6eo4LzmVYEpAl_jjaXKirevWPfGeAW9vI0eoi5s-PiJhLhHCjExxHO9F1pBruOWiF61D0p72yVYrOR7t5DRjVeQO8IYhFnqDDQ_FD5q-RQyRUK4E7ZlZXikDdTIOGpxCsuENwkKgFetiFGOQdyIBNPNgjH96ou4ommqrf8gQAiucxpjnd9y52Zxl_Asf48E7L0Uo4oAGE_UIl4wBLFfw8nZhucJtxdCU5ezzp3qr4QSEDz4AyUODg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=QxRkKSRBPIlyINVeuPtHG2fl4Le42nGz5DTonUk30PhgOG4P7OuEcNewjjNiraHQ0eBBAKOfdbWaoqLlLO3XtiR1ognAvGbIcl6kwIfmt6u24jw7Nm0EO5TT8wmCd6GmbdH6Ts9leQTWZpo6WAwf5GNwkgbZOsvDaYjLi47V-8UpSUZjJUpELtzLB7Nfv8yVBByOq4Y_FghBiHQWauJIwdrD3PR0DQoWfXKdqA-8rCe5NvYXBueDRdXzo6RU_jE77GSz69GJ8g9iPS3jKtleDtE__2z7uwQnN1T2xvy0w7NY4-ytsqjuWn1fcZmxRur-6Y5N73Rcp4zSAnLCBm_keg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=QxRkKSRBPIlyINVeuPtHG2fl4Le42nGz5DTonUk30PhgOG4P7OuEcNewjjNiraHQ0eBBAKOfdbWaoqLlLO3XtiR1ognAvGbIcl6kwIfmt6u24jw7Nm0EO5TT8wmCd6GmbdH6Ts9leQTWZpo6WAwf5GNwkgbZOsvDaYjLi47V-8UpSUZjJUpELtzLB7Nfv8yVBByOq4Y_FghBiHQWauJIwdrD3PR0DQoWfXKdqA-8rCe5NvYXBueDRdXzo6RU_jE77GSz69GJ8g9iPS3jKtleDtE__2z7uwQnN1T2xvy0w7NY4-ytsqjuWn1fcZmxRur-6Y5N73Rcp4zSAnLCBm_keg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=hY7SXeHLskF_7AKswJ4RrVhU4zBVIZyVZItOsD9Y5tCJawPy056bCBElxhkxFYma5dYuCnDVgevvrOue80FEVOeBTqlIhjKU9faZQzxo97P2yIKMW--j7BrAua8k33F3XpgvQT_k-a6k6vz-Hmr9xTQpBYuiuE3eGMSoLFwsPUTZnG58neI6qfWzj8Buc4nC0qIgm3_JOkt5-xB--7b_L6C8SzyH_xjf3CWFIreoQs70TvMaRLaZLt3YFhIgmGMpRSp-VEDhjgLTjNGIOpivUlLU0cP1hqh4Cg50laYWHeH9cJ9SOtbaX6VGeF-LiFAOxcOqgUvchXDmHe0pFE0DxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=hY7SXeHLskF_7AKswJ4RrVhU4zBVIZyVZItOsD9Y5tCJawPy056bCBElxhkxFYma5dYuCnDVgevvrOue80FEVOeBTqlIhjKU9faZQzxo97P2yIKMW--j7BrAua8k33F3XpgvQT_k-a6k6vz-Hmr9xTQpBYuiuE3eGMSoLFwsPUTZnG58neI6qfWzj8Buc4nC0qIgm3_JOkt5-xB--7b_L6C8SzyH_xjf3CWFIreoQs70TvMaRLaZLt3YFhIgmGMpRSp-VEDhjgLTjNGIOpivUlLU0cP1hqh4Cg50laYWHeH9cJ9SOtbaX6VGeF-LiFAOxcOqgUvchXDmHe0pFE0DxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=iyKthlQXwFuSvWVnajMlO17Au-SeXfbnHuR0cYrs4rK8nhkmR9L1--kmT_Q2Ue90ofEt1kYvdli5hzb5MdrdhawfU5ZKv95wLGs2XwYsaE898mc0O2YUGHEKyMQjB5NKTotjoh87VjNTiuu9Gq6KG6_48TAjodnBk6JKpWV_mEi9EfDnX_qSahG-2RMQOeLp1NGRhOmuBJnTcHnA5wM6Rr1buT2kNTjMUoNKdqqu3gZ_r-kpfolBKo6W8H78-6ZmvgSALTo82k17NGDpNxCNFOWR-T7aFqQWo8Vc5ivInsQG7yPpwNU42WnaaSKg-bS82Nd51pTornFmIH-oLMQKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=iyKthlQXwFuSvWVnajMlO17Au-SeXfbnHuR0cYrs4rK8nhkmR9L1--kmT_Q2Ue90ofEt1kYvdli5hzb5MdrdhawfU5ZKv95wLGs2XwYsaE898mc0O2YUGHEKyMQjB5NKTotjoh87VjNTiuu9Gq6KG6_48TAjodnBk6JKpWV_mEi9EfDnX_qSahG-2RMQOeLp1NGRhOmuBJnTcHnA5wM6Rr1buT2kNTjMUoNKdqqu3gZ_r-kpfolBKo6W8H78-6ZmvgSALTo82k17NGDpNxCNFOWR-T7aFqQWo8Vc5ivInsQG7yPpwNU42WnaaSKg-bS82Nd51pTornFmIH-oLMQKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiNERDMjZZ_MZX0xqqEXeVXPKok9CoOg_8wacVn6vh2UkGUzheY0Iif0nrP5E3HkUE9M8LXHoM6HA8vS5KDtvpIj1d1xf5GxJs5KTHO8fJ_WadWn8Aftqfhe_9HvsDZt5owKalY-UbZNHSIn13IzUZ8IiHKknh7qxOHjiBcNDUIRwXPzr4TccRAbQ0m8xYzYdRf2SEreuDpSMmP8M8oHXGtlARFe8VyHimwtb-t-epAej-lBWAwQgSi40ZK5xSf9PW27NqzIM-HnUGGxkhj7HZ13OLe9m0agCLjYHit1LkcLcxBUMRlZ57CzCglc1ujkNh-UCg5ajEf_i7euGItXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeAzbGdkG0IEIHRCm-l4rDNgW3pGASohxzPYU0H34tFb10Y6mcDE0CSVP2nPqTroEY0q4Kbr_6OqdKPrTskPejVjuK8ytdaLzNQPBUQ8YhJOOSMpmI49Plf_JExMi__v-rn3vPNbOtEAICfowAESaYh7Ynp3fUuzxH04kjACC36iQCOy5400tedWZLWgc2esKLzUsiUmQDR3SuQYDu_8UnQD5ka6V3yE4p82EU_-4l0stAAFEYroXfOFYywOEOKrhs8EuPKX9TaULMhylMO8reYH-JsL9fLWoPhWAY-ixlrndIJPXNx6a4GDxTBnJQVW7X7d2DdMpLK647QUXGYIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=Yi3Aj3cXh32nDY6ST357UpXNWHsS4fYYdcGLFbywNAu157se8UXa982PA3ZQ5R72g3XxGvRDLUBszBUQC8RlrASq2VB0wvYcvzKvpuDELy8DJ5_tHzmt6hIpqUwf7-fN5C-zyElnA1FS1rkebnqDNjJh899b7rF8e9AFJhJcnztGXEHgwO_0WEn22qwSQcsBJHrAW_vM5jgNlDW859X4NdbLPox2pycFi8dk4iEkxTX2SlhiDTT6KYZFsWfjZ42-Ub5cXSs3jCAqa7Zxclr8wDIc5xj20twL_UJLECaggJcD4NcFi8SgLzKKriDkVSuBiHJlFsIDmZALG95VswzBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=Yi3Aj3cXh32nDY6ST357UpXNWHsS4fYYdcGLFbywNAu157se8UXa982PA3ZQ5R72g3XxGvRDLUBszBUQC8RlrASq2VB0wvYcvzKvpuDELy8DJ5_tHzmt6hIpqUwf7-fN5C-zyElnA1FS1rkebnqDNjJh899b7rF8e9AFJhJcnztGXEHgwO_0WEn22qwSQcsBJHrAW_vM5jgNlDW859X4NdbLPox2pycFi8dk4iEkxTX2SlhiDTT6KYZFsWfjZ42-Ub5cXSs3jCAqa7Zxclr8wDIc5xj20twL_UJLECaggJcD4NcFi8SgLzKKriDkVSuBiHJlFsIDmZALG95VswzBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=JKb52LwCzEFaXqRjqSPdWBwJ1YrMOzKfyyYJAoQ_EGcuTuknOFNRhiwRnxDPOKveYEjGuCYbrMeWTN-l7VjcCRiJgvuS39vZIGsDCpy-51na9Nd-7o0Aqil4FH706bg4jpDgQkVFQHHbniw2VAAVQ_OCr-PN574DMlDZZsXz6_MmVe78ZWSxG0ve-pKyDeVlqUHmYTv249zArtJFPkNFDtoHm3o4uUwaoL1r5461pMkdfbGhBLHLMMURnm-1f1ojXGIvZlh8lM6uKIKYZW9AM4MigvEtMbVy1so6x18KeUWyb7pkv-YWWmX3cQPUdaz01IUJ5dhPgCsyzI-LB40VJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=JKb52LwCzEFaXqRjqSPdWBwJ1YrMOzKfyyYJAoQ_EGcuTuknOFNRhiwRnxDPOKveYEjGuCYbrMeWTN-l7VjcCRiJgvuS39vZIGsDCpy-51na9Nd-7o0Aqil4FH706bg4jpDgQkVFQHHbniw2VAAVQ_OCr-PN574DMlDZZsXz6_MmVe78ZWSxG0ve-pKyDeVlqUHmYTv249zArtJFPkNFDtoHm3o4uUwaoL1r5461pMkdfbGhBLHLMMURnm-1f1ojXGIvZlh8lM6uKIKYZW9AM4MigvEtMbVy1so6x18KeUWyb7pkv-YWWmX3cQPUdaz01IUJ5dhPgCsyzI-LB40VJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTc0wIVsXjSiPr29nxRhAVb4u06nuF4VqDHq_dMVtG78GqKhx9sxd96y488NqhSLaBcA2SdqTh6210lGowi8ZY_GsLb65GHfBz-M_UGHkeN_M22oAhxTQICTKq7yE1n9TlSf8rm_qVEmUTS80X1YpEj779oPM9QF5dHyDoRPXVhu6Q5l9eUqAMNA6PB1wRyIRhjZb5wgHS1n1PKQS7FFzA0rRbExio0LBX13KnWxBGlCDKzaz4VjGk-UsowlhUmDPdik9_BAMhi4AOGkskFs2orbnLpYPijKcThTQ4--CxRf0zqRugFUxLlY9FVhLnbcl5hqqiH6c77gVi0pPUhzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=lcWbm7KV7uSFavl_X8JIdt2kdoJJLVTbeUaFVMm7T3P3w5UVWdoTr0I6tQd2yNFauLad4x8KbHOYNvrG9CJfPKDqEJFFpwFx0C_4I3hRytr_FQlmxb-iqnB1doE066Ap1OwtC7xiyLUJ00MUDYTdUxZRPEvcqerLker3lnvjnwzhiQmHb1_tV_JBFsx9kURxniIJ5EwKBiIdIsSIl3gHS8U-avsqZqSIN8M2QZSPIowFfzU7U5JMsqi9-8FLz723Mb8eTHEzAm9jLc85czPb_hKjQdGQP34Um8Uflrn7HNNoP2mfj9k4mtrJ0dGrwNMrYOXDi8HED-tk3IcWsRfpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=lcWbm7KV7uSFavl_X8JIdt2kdoJJLVTbeUaFVMm7T3P3w5UVWdoTr0I6tQd2yNFauLad4x8KbHOYNvrG9CJfPKDqEJFFpwFx0C_4I3hRytr_FQlmxb-iqnB1doE066Ap1OwtC7xiyLUJ00MUDYTdUxZRPEvcqerLker3lnvjnwzhiQmHb1_tV_JBFsx9kURxniIJ5EwKBiIdIsSIl3gHS8U-avsqZqSIN8M2QZSPIowFfzU7U5JMsqi9-8FLz723Mb8eTHEzAm9jLc85czPb_hKjQdGQP34Um8Uflrn7HNNoP2mfj9k4mtrJ0dGrwNMrYOXDi8HED-tk3IcWsRfpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn77RJRdLpVjyGcBpbnxyKczD0noSmKYtSAh10Iijyyf6QZijKcUAn8wIvrPTJYdP_q0nunfLgwhQ042w3ENUXBynxHmUOye-MsK3U_4YOQl8hYEZUtUm3OztmXwtZpuUWY578ngjNpXlJwBdJXLvTuInDptFoqByanVJHI6XgedxCSKj-LU-wM9JKcj-9bf0mYOdWnGxzFi00plKZtdS2kXhxZ3S-p_z5SBh1iCdp_cWAX0CIJYDWj-f8RTHjYr6SGFR2YJz7W_oZp6NmpMqWmVpQaCWWXWHzBql0ctUmuEkqZTU8gKz-7wcoonoeTekqw1kLh_L26P5o3FJxx85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_R3aG6P4zVk2N7W3BzJSV7D9iJ67gjdOSZOGDJ67AhAIgv7S8tEepiPSCS_qF63eauxdOBqSPVOSMmYhVe6G5yH9s01u2h_zdBoQlCRWO29Bcm7O2-pgHseq6nsERIDjgSWpxdhvV8XmnqWBlkiwYqV8wMyRNq6Fmf3x8YzXZtSDsucbi_B0lNaTchLjrVn9rzI_uZbEaUMs78B_z8pnXfk0vdEyulICRJA4XCiygsDzsoCbuG5Wh6jG7Ias2vkKq9VA3NK3Fto8PKC11ko3oi9N6NAk02OGj2SfYCg3GoHOPwVuKZcxJQ_1qGolUenerjtUUcl1xYmbKe4xUnQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_gnnHriQh30WWmZI3Ngs5cc_f74tUFBJznwMtabjsHC8Dso2AW6fs3pbPwaveI6UJ6meJJI-axsk6S5hqn1ZnrS8BDKDBtN1QJ115Z8XB_xXSXUeS4mShbyaOuplxwa239DDRe647ciAs5aMSZVzC9BNYbQTfEAwOXOt90t_WGDl3SIFOTtzYoocx4AsZOhBiKZ4BT7ZYoyvnonN5BKkYBZe0rHEvrhz8_hK6W9bOwGq4FZ7mN_7z9haS-iIjUjKe8y2uN8SfRaGf4gw7m-fm5ebI-drb57zXhfTzahR_iSt4_ZcBUsX0YXtITvgm9uGGLRLaa7-pb1PX2XmH37QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HdskBfqT8kmaIkbPwq_f7ndy3ZEZL2g6a8ESICOJfwCJlib-rZjGIlZ9fVJRM3-E2lB8mJ7dgt_dgkVNfZCn1ykLMrj5gYPaP8Zkg-jUf-t5qKTdGz2KHjt6l46UF8cqRt1buEtdmxMEC61LSzAsjNOTLlEeQrqXX1_pjQNewQCZ7nEDT7vagVqfAZJqbnJPRNrLqQTtKP4GH2JYReecLyhoE3Xya4SGCATCr1bnV-wMlLAmVutdFvKczTG_7FqueWMZOPRz-mb-RVoKBszOcfSVCJEUKsdOCvE10qBbrva1ZpNhfTcidEnFVBCUP06zTEglrHccG6jtCnYID_7hlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HdskBfqT8kmaIkbPwq_f7ndy3ZEZL2g6a8ESICOJfwCJlib-rZjGIlZ9fVJRM3-E2lB8mJ7dgt_dgkVNfZCn1ykLMrj5gYPaP8Zkg-jUf-t5qKTdGz2KHjt6l46UF8cqRt1buEtdmxMEC61LSzAsjNOTLlEeQrqXX1_pjQNewQCZ7nEDT7vagVqfAZJqbnJPRNrLqQTtKP4GH2JYReecLyhoE3Xya4SGCATCr1bnV-wMlLAmVutdFvKczTG_7FqueWMZOPRz-mb-RVoKBszOcfSVCJEUKsdOCvE10qBbrva1ZpNhfTcidEnFVBCUP06zTEglrHccG6jtCnYID_7hlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2wsMj6QH-G3L-bH8pxS-NygVyUHeJcek0SNc2QObuQ5BPdjoCLiD7SEew57YKAtpdmnPOC-UuQlpxp0bjdaFSzFabpH6vEOUH5_LmvyWGKgmBz5DWMmsGnVtLqofiw60e1noWZbHIhl5K5YRp2ZONsf6GheatoZy0UJ3SaPTsAwfaXudQlvay5QMPEhE77PjRBkprw04sFN2ZAVpDffDOJgzHtLOTTQLtLt-OSTcIWPhM5HfaKnmO0xdH7WzSFmQl4-3xc7Qt5h4-jCOxGlSdxuu1oYhOm4ZYtwa8IzvN-iaDRreZgMcWdsxZyRcl6Qx-O4rgSo94SeWzu4H8Jq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nUD53kFlKECOuJ4bd1aZ3HqU-DxiJFx7tZjXtfKcDx7gMO1xO7cQEVk51PoQza3r79YbI4ek8H48a0-TTkSzBQH5FSFW73cPeex8uCS-_jwoTuTw0BadMIqiS6E-4YaGYz2bC_867X823pKwBj9CtW-FLvOLfDXrfQyyQ0bF8TdJVrSszSjZRtN8v6d74FNA-D0wuGpZMv3fzQBhJ5IV_1mKWK3P9ea4gIiMHBKRZt4IYK6nj5xeaV4C-Xu286Anm0FsDJfwQ0qbnBpAGCmFQZ7sMmvBm8tg-DZ983ZXjL16CFWDqGlkZQvW_F8imdDy3EGbgbHaja5gBraVWKgB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nUD53kFlKECOuJ4bd1aZ3HqU-DxiJFx7tZjXtfKcDx7gMO1xO7cQEVk51PoQza3r79YbI4ek8H48a0-TTkSzBQH5FSFW73cPeex8uCS-_jwoTuTw0BadMIqiS6E-4YaGYz2bC_867X823pKwBj9CtW-FLvOLfDXrfQyyQ0bF8TdJVrSszSjZRtN8v6d74FNA-D0wuGpZMv3fzQBhJ5IV_1mKWK3P9ea4gIiMHBKRZt4IYK6nj5xeaV4C-Xu286Anm0FsDJfwQ0qbnBpAGCmFQZ7sMmvBm8tg-DZ983ZXjL16CFWDqGlkZQvW_F8imdDy3EGbgbHaja5gBraVWKgB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=k9kkmUgkUq2O8z7mlUWVUYY17Je_uu6Ea1KQWR1yXd6puH5CHhiigYxl_IlTvU1OKuO3hyCgRvhnot7vZ2oPpq-ufJ9vI3jgXZeOAASkED_3AL7SH0pGDWQGmqcUVr3KX6MoFUOYEhuTCDyYQUDqxXPaSrNcEK8oaqueqlW7faJBNlRpAOM_GAf5O_OLEJjYYzJEthT9fuybY2IWei75xDY7bX7xxEJrWYz-xouAiZvuYOl31GTH9Q71xSjuBmBA7n8eFFSY8k_7p4yBNJLGzLW_ODIzNRqkB0k_Lq_99vaVE49eBxMVkyPO_zq1LQxOX6uujHzgVKOkHyA5pDAciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=k9kkmUgkUq2O8z7mlUWVUYY17Je_uu6Ea1KQWR1yXd6puH5CHhiigYxl_IlTvU1OKuO3hyCgRvhnot7vZ2oPpq-ufJ9vI3jgXZeOAASkED_3AL7SH0pGDWQGmqcUVr3KX6MoFUOYEhuTCDyYQUDqxXPaSrNcEK8oaqueqlW7faJBNlRpAOM_GAf5O_OLEJjYYzJEthT9fuybY2IWei75xDY7bX7xxEJrWYz-xouAiZvuYOl31GTH9Q71xSjuBmBA7n8eFFSY8k_7p4yBNJLGzLW_ODIzNRqkB0k_Lq_99vaVE49eBxMVkyPO_zq1LQxOX6uujHzgVKOkHyA5pDAciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHAkS9F95U8WOx6GKI1zxB9povOo2YJ4krQfgijeO0x1qJ9DKcXDOeuQAAlCF5M9zQA1DzCF_hwHeSIOW-hKQ89cNsqF1Y-S8hkAYxzB6bZb_BHg9CMdeeg1WlHQwVYxeeGFHP78q5EXCg6tKbWY5_wGt9-l4g9O0sLYk_yoZCm_J19_GFG3Psfwjq3WtkJBnca-cpqgDPQJGabjYMRlXnonFhqakDBKHLZcFK9DWmcFI51glRCJi-YU4RdqzjIDkD_ED6-sPAgalQWvkY7bGMCCu_IyRmmP2KYgPGsPglmnBmlJ68whsIb2MdLU8QAmtxRA0toMA0mpNiIEE3QTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
