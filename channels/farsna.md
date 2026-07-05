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
<img src="https://cdn4.telesco.pe/file/QB2CxLwPBFIUgX9LU8AuAHjfVE4ZUugFVRPKJ2lLpZz0PWdrsbC9_fBaYuIB6cXXTAsaZRIoh271hOhyqzeiyZAPymb-v4FKLVdxF630qou_-apPfZuTFTesCccIfSnpSBwtFvLQeFsW6pkHfjPnKz2d7VQoaBpwutT83YBnjssCDUjjWlC0uVgvQSRnAVU4WxC_SIvVJlHtiPQa2qAq-flMU-NJHgei2BDnxzHaEebjwWb2BE-Qs9ka-ZNcORnDdDwDW7N9RhXa8vVSDPMad-HijIqBx8rim5rWgh5_JC45YSiRj8V_tYSsqNXD8RKVTHoTVA1n6tDHOEfIYccbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-447073">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d975d4917.mp4?token=top2XncKAawPE4WzvgiJcDfBvwk_15TVXU4oE0kSqrd4WVIWg6YGLTob1H79coyM_gzfE5N6KNpiR_1DJQQ41UOu94JoOAwVO8GbjGi9WvbeJAknJiOgRj9wE1BpNTs11ir9e3PU60-fZGGDwI1JjpNMsX6LpvuwMnQvRvolMNiQE_WFa0jjv7umcW-tbEX4d-bvskF7ZIGGqG0eT_bhq_O31Jd2wApnmJlela7u7RUiakGGI-Nc_5tk7IGOXFQUtUVimj2PpO-CiaM9sIbGBGn8vYyzFUddXaEG8gRqlkXVv6TRRY42WRL4Kka6dWuSOf7H-rEFN6LKTS75CcCwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d975d4917.mp4?token=top2XncKAawPE4WzvgiJcDfBvwk_15TVXU4oE0kSqrd4WVIWg6YGLTob1H79coyM_gzfE5N6KNpiR_1DJQQ41UOu94JoOAwVO8GbjGi9WvbeJAknJiOgRj9wE1BpNTs11ir9e3PU60-fZGGDwI1JjpNMsX6LpvuwMnQvRvolMNiQE_WFa0jjv7umcW-tbEX4d-bvskF7ZIGGqG0eT_bhq_O31Jd2wApnmJlela7u7RUiakGGI-Nc_5tk7IGOXFQUtUVimj2PpO-CiaM9sIbGBGn8vYyzFUddXaEG8gRqlkXVv6TRRY42WRL4Kka6dWuSOf7H-rEFN6LKTS75CcCwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سبحانی: آیت الله خامنه‌ای با خون خود درخت انقلاب را سیراب کرد
@Farsna</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/farsna/447073" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5i-bYXBt5uM8LlYhp-Ru-O8U9huv4-LpxOOqBZZjiKPQbkeBxbYhwPcS6h4uNBXVpZMQXd6I2gZa0pl5vMq7DeniLNqPj1MaSQAxyan_bb7HXhMiuubC6O8RottSOoYQg2CcZ0yGDvl21xrQx3YojZBA5TxnCeqcIoFq5PzQ8bYJhVmnWz_2c3PoiqU4L_YZNopLtU4E_Do14TnsNNiTDmgZadIZhaiFpIEZ2YsTUZpwSanou8SxLRO7C_zLgBDjj2omiErNgIvnaiyyoZAxR1VkKa_HmwdkjLTIVm-QygnaRemgMYuSZf692d-a6VFP1Q5OEVh870fBCGoCPFN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پویش ملی «آخرین دیدار»
🔹
جهت ثبتِ تاریخی وداع با رهبر شهیدمان، از کلیۀ علاقمندان دعوت می‌شود روایت‌های خود (عکس، فیلم و دلنوشته) را به شناسه زیر ارسال نمایند.
🔹
شناسه ارسال آثار:
@akharindidar_admin
🔹
هدایا: شرکت در قرعه‌کشی ۲۰۰ جایزه نقدی + بازنشر آثار منتخب در صفحات رسمی پویش.
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/447072" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzb_oIHtDKJK0aH4_u4NSQWcea6v2FSxbAkwoOfyWNoWbh1v3RH0CREkGeepdcVnNGpiL8b6OztAtNitU7aQCChTwxJLlR4U3PXbECuRgKd8CW71zR8D2MZMT8znqQCFeodLUyuwno9bwRXZ8zZiZU-XD1pzzHDSEstaskY9n-5-DbfCTjAOhCthcvGdlZJy210BM7IKqXSztbtYxdXyQu8yd6S-NAMrLq504h-qmj97WXRhabniIxD_ncRQl38EOa-SRU_YdK9dzyQKUZx7wRkDWuaENhib2gPzH7WOyri4NUrV8oHxB8KQMhPt3yhJMEIcKLUi5OiR977mNKM47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ملت شکست‌ناپذیر ایران امروز یکپارچه فریاد یا لَثاراتِ الحسین(ع) سر داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447070" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59349603d.mp4?token=L-7frFWr8aC_vD6nwLqJXakRw4tUj60mvCHrfzD5JoHZr7R-ZES1FIeRVu9p9uLRCLkRhTtD5Afh7Ol31loo0xQnmlsDTqDU0z0KHWrkiEbMPBF1ofFGMOVkBRqnj0MKC4xM0_VNvrMO4gqNtumg59UCPKPz-CIqWFD7p6Sv_b-NkWN1QsCHcAYaVJa7vMQn9I74A9uetHW3FWvLLl5hKlkxi-FBq13Z50KYl9twjtn04sUwhunCBrEgx7bqpR1s0_r65CRxvDYxeRFxBjScVAdHqgIljJgw4qsAQjBMNLHI0bTaalP_DC3Aafd8fBkhC_WNPhKeG_83Ru8oZVi8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59349603d.mp4?token=L-7frFWr8aC_vD6nwLqJXakRw4tUj60mvCHrfzD5JoHZr7R-ZES1FIeRVu9p9uLRCLkRhTtD5Afh7Ol31loo0xQnmlsDTqDU0z0KHWrkiEbMPBF1ofFGMOVkBRqnj0MKC4xM0_VNvrMO4gqNtumg59UCPKPz-CIqWFD7p6Sv_b-NkWN1QsCHcAYaVJa7vMQn9I74A9uetHW3FWvLLl5hKlkxi-FBq13Z50KYl9twjtn04sUwhunCBrEgx7bqpR1s0_r65CRxvDYxeRFxBjScVAdHqgIljJgw4qsAQjBMNLHI0bTaalP_DC3Aafd8fBkhC_WNPhKeG_83Ru8oZVi8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از نماز بر پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/447069" target="_blank">📅 13:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53e7bf830.mp4?token=MAiDpzqM-w_82Jb1j4_k4VZ4RI5XqhnpeGeNNWQeRHqkFWGVZtCNZjBLv59hRI8-rMQvt754MNwvHrO_jXInElmt83On17tBAxjjzHP-wjO0b9PeHKFnwQcmvP9p85rvxKbSPHlCPxxrWl3DLxP-U9CjKXutde7J9ZiVSvoyPAdI7XtZ9xT_H6ipeTnPdXa-bFk0tQXgQsWDrSB52djbAIFjfXA92nv3Lhm5qK79CGxCkz7PlYa-tw7p0NdpQo5vNAi5WsQ_pTUZ6PhcvXT-K3pBTpuxafMNZJ9f_f8EsqkqCehPj4N9VdNSBzKtlUKUXZj145bCYTFjofIJ1JdC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53e7bf830.mp4?token=MAiDpzqM-w_82Jb1j4_k4VZ4RI5XqhnpeGeNNWQeRHqkFWGVZtCNZjBLv59hRI8-rMQvt754MNwvHrO_jXInElmt83On17tBAxjjzHP-wjO0b9PeHKFnwQcmvP9p85rvxKbSPHlCPxxrWl3DLxP-U9CjKXutde7J9ZiVSvoyPAdI7XtZ9xT_H6ipeTnPdXa-bFk0tQXgQsWDrSB52djbAIFjfXA92nv3Lhm5qK79CGxCkz7PlYa-tw7p0NdpQo5vNAi5WsQ_pTUZ6PhcvXT-K3pBTpuxafMNZJ9f_f8EsqkqCehPj4N9VdNSBzKtlUKUXZj145bCYTFjofIJ1JdC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم نماز خواندیم هم گریه را به آغوش گرفتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/447068" target="_blank">📅 13:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uncg4hasd6Iv765-yZtvfJ99NNsuMmhD6ItmwgBVg1ZrPYL8DAjGGh8JNF_jhQjB7dJ54Ap6RJRmcJWlYCRw798hsxowrn2rBaVU-QbTYb1FEBi7u1aQNJYbObctAbdn8OBGvsw6h_vfjDgi2RloQbh441T7kbQGcspPj5U30X44K268ncAwml7QlvWyvyPPCFP7MykX8PyJQOmpPPp9KPPkJAZQcSLahsQwDreGjPNvAXpnwS9MZIbZ78uRbilGc3aT3d59b5lKBxIoWjRhBluocQEQI8AiC-_h9pPCIjLj5FyjJrChFdSERydzrkjERMsyW06YHn1e4Pesk4l_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای‌عالی امنیت ملی: مردم در وداع رهبرشان دو شعار را فریاد می‌زنند: مقاومت در برابر دشمنان و انتقام خون رهبر شهید ایران
🔹
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید.
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/447067" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89bddb803f.mp4?token=tcLtiX5M_Fz13AFiXFTgDjXfb5fqV7BJVF6ya8ho4UfA473C2ZkY7fdy0fM5PPwR0soXolULDBFSPo2kHykjTBRNT-52dQ6sv54pcxASKikOsQJLM7U3O5LEVAS1HjpOQB4fy66p_KRP4bwIqbu1XJ1YKU42lupoU-ewX49witi4TF88mS9hcWEqU_rzNxmmkIioEt81HEIpVjSiDvHanD9xzy-rD8h233CZhDd4NoXNX2BJlEBfgVesK5nFF0LrMgvswDT_27uF-rC8K2VK2WY_MZ6pQ9BWGEPhZ6F1Jmy0wd9vhUlfCyS70cOROmVhE95Y-ahYt1N1i7ED6Ae30w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89bddb803f.mp4?token=tcLtiX5M_Fz13AFiXFTgDjXfb5fqV7BJVF6ya8ho4UfA473C2ZkY7fdy0fM5PPwR0soXolULDBFSPo2kHykjTBRNT-52dQ6sv54pcxASKikOsQJLM7U3O5LEVAS1HjpOQB4fy66p_KRP4bwIqbu1XJ1YKU42lupoU-ewX49witi4TF88mS9hcWEqU_rzNxmmkIioEt81HEIpVjSiDvHanD9xzy-rD8h233CZhDd4NoXNX2BJlEBfgVesK5nFF0LrMgvswDT_27uF-rC8K2VK2WY_MZ6pQ9BWGEPhZ6F1Jmy0wd9vhUlfCyS70cOROmVhE95Y-ahYt1N1i7ED6Ae30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هموطن بختیاری در وداع با رهبر شهید: انتقامت را می‌گیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/447066" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_4qQFfAFxm-jIqm014jTsY5Hq8XzfItO23Mt00yLInwbN4ib7psGqWVGvMeEtf6hYJjpEmX6rmD_ACmKP3lJwrnZHR20SpZGxXT-9W2hxUm70HXmvif0slsZBo0R0s6vzVXNll04h7ts7SRzSnSuzRZlyakLrsu-Xn5LMdbhPIpK_4nvrPFARktpwEmTrV7dBLZDFh8lCh52E-AcFBP0QUOA_fsbNZKX_TNdvVcSWdN_IzgUbFojKUTeGUZq0Gjt_C_5irRHS9ctYzk4Y1_IYp_75tSkvbWrfGwFD3Mr_mB1lu0UfdybGSuIdq-l5SdNbR-AOKeyimMiqmbNUpI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار اعمال قدرت سپاه در تنگۀ هرمز
🔹
نقشه‌های منتشرشده از تردد شناورها در تنگۀ هرمز هم‌زمان با حضور نیروی دریایی سپاه، نشان می‌دهد ۸ کشتی از ادامۀ مسیر موسوم به «کریدور عمانی» منصرف شده، یا مسیر خود را به سمت آب‌های تحت مدیریت ایران تغییر داده‌ و یا به‌طور…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/447065" target="_blank">📅 13:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447064">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b338e712.mp4?token=I1MHlw688Iw0YeloaED_cpkwaMtPztKrP8lvy5ZTQKQT3py7T8J81ZIwF6dxn86y3SQ0zagWLYHoMZzWncwuBxWjViLnRinTIp-4KMbHbLtoD0qBaS9qnfGJkDopJuLZuaQLIhxkN0DsirhvAC7rS_o1HctZrefBWxdOPj_-0AxUynHOQ5vpc0gL1b7hIMRG8fUBa0vC6aW1R39pHMSZ1I-BVaIDk700SzQ7BZn3u85mQN2EokW8a5_8D4LpnF30rimSkUuxjLTLSQcZEGCp7wS06bntSQh0TLX15UuAKY8RM4xv8LjDOr3GV_cEbb7VwtA3SQHfSaz70HpOV2tSjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b338e712.mp4?token=I1MHlw688Iw0YeloaED_cpkwaMtPztKrP8lvy5ZTQKQT3py7T8J81ZIwF6dxn86y3SQ0zagWLYHoMZzWncwuBxWjViLnRinTIp-4KMbHbLtoD0qBaS9qnfGJkDopJuLZuaQLIhxkN0DsirhvAC7rS_o1HctZrefBWxdOPj_-0AxUynHOQ5vpc0gL1b7hIMRG8fUBa0vC6aW1R39pHMSZ1I-BVaIDk700SzQ7BZn3u85mQN2EokW8a5_8D4LpnF30rimSkUuxjLTLSQcZEGCp7wS06bntSQh0TLX15UuAKY8RM4xv8LjDOr3GV_cEbb7VwtA3SQHfSaz70HpOV2tSjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف‌های ناگفتۀ مردم در آخرین دیدار با رهبر شهیدشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/447064" target="_blank">📅 13:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447063">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXB7oXHLoRkCsoN1AAGoeFoX8_usAIiYYloh34QmdMgsip5ES3XMAiQ-LYRiZPHd2a7FNApaeOcV8Cp9jBeEvR0bAknlN4foNZQMMr2dyWlATQaRFzOaM7WNAIL8g2N3JaizSeXRd5xmcFwRCW9am1tCAv5QYddd49TghGEFM5q8QlFULEqb7yH3oKu9UE3j0eQaSCmuaG9huIsBFjCl1g-DhIjp9LqEEWI9-3coxzB-gXTrKpUnpihlF2wFk4lFokLWJcKX1JQUR0uBRa1Hs_i0zeD7eu7v6nqBEd19PQaYOqeVako-iET1kSqiz5pjmd8DEotLOpKD9jsGfo5wLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واگن‌های مملو از جمعیت در خط سه مترو تهران به‌سمت مصلی
🔹
به‌علت ازدحام جمعیت در اطراف مصلای تهران قطارهای مترو در ایستگاه سهروردی هم توقف ندارند.   @Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/447063" target="_blank">📅 13:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447062">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lySB_lCaAhGrpYFF26V53dfbb9KCV_5_Ku3lF_3HzLlwlxF0q28LMxh1ndO6QSIo1OhPzKPtoU8ku_6Th-8kboS8z109dmuDf4_-o955SiRm0tL8IcF9oczh82p4GRwiYPsr83ozOdV_RvTbZ4g9Ah3IRETLIn6xqho8QmRr2P808A27VnemDFtLFEBwtwcAtbQSEpkhzChSFlYn6OJDHsSYEZtY__oFjBv6yTKjvRu6PBSJTy07682_2tirNzrFtQI-0z-AoW8vBn2v_XkQJz58UHr31Ns1yWW1obBxal63iBwD_WeaTaF-xRhDxx6v0NOYK49MiOl1Rja4lgNexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله مکارم شیرازی: امت اسلامی وظیفۀ خود را در خونخواهی شهیدان دنبال خواهد کرد
🔹
هم‌زمان با وداع و تشییع پیکر مطهر رهبر شهید انقلاب، داغ جانسوز فقدان آن مجاهد فرزانه بار دیگر تازه گردید. بی‌تردید، حضور گسترده مردم در این مراسم، جلوه‌ای از اقتدار و وفاداری به آرمان‌های والای انقلاب اسلامی و نشانه استقامت ملت بزرگ ایران و امت اسلامی و تداوم راه نورانی شهیدان خواهد بود.
در این شرایط، توجه به چند نکته ضروری است:
🔹
اول: نباید چنین پنداشت که این جنگ پایان یافته است؛ بلکه مقابله با جبهه استکبار همچنان ادامه دارد. ازاین‌رو، هرگونه القای یأس، سستی، بن‌بست و تضعیف روحیه مردم، مسئولان و نیروهای مسلح، در جهت خواست دشمن و برخلاف مصالح کشور و امت اسلامی است. البته امید و استقامت، هرگز به معنای نادیده گرفتن واقعیت های میدان نیست؛ بلکه صبر و پایداری، از مهم‌ترین عوامل پیروزی در آزمون‌های الهی است.
🔹
دوم: قاتلان و عاملان این جنایت بزرگ که دستشان به خون آن شهید عزیز، فرماندهان، مسئولان، مردم بی‌دفاع و کودکان مظلوم آلوده شده، از کیفر الهی و مجازات عادلانه مصون نخواهند ماند و این خون‌های پاک هرگز فراموش نخواهد شد و امت اسلامی، در چارچوب موازین شرع و قانون وظیفه خود را در خونخواهی این شهیدان دنبال خواهد کرد.
🔹
سوم: مسئولان، نیروهای مسلح و همه تصمیم‌گیران باید با توکل بر خداوند متعال، اعتماد به وعده‌های الهی، بهره‌گیری از همه ظرفیت‌های کشور و اتکا به ایمان، صبر و استقامت مردم، با تدبیر، اقتدار و هوشیاری چه در عرصه نظامی، دیپلماسی، و عرصه های دیگر در برابر دشمن ایستادگی کنند؛ چراکه تجربه نشان داده است هرگونه عقب‌نشینی در برابر دشمن متجاوز، او را بر ادامه تجاوز و زیاده‌خواهی جسورتر خواهد کرد.
🔹
چهارم: انقلاب اسلامی بر پایه اصل مترقی ولایت فقیه استوار است و به برکت همین اصل، از گردنه‌های دشوار و توطئه‌های فراوان دشمنان عبور کرده است. ولایت فقیه در نظام اسلامی، محور وحدت، حافظ مصالح امت و رکن استواری نظام است و التزام به آن، وظیفه‌ای همگانی و مایه صیانت از اسلام و کشور است.
🔹
پنجم: امروز بیش از هر زمان، حفظ وحدت و همبستگی ملی ضرورتی انکارناپذیر است و نباید اختلاف‌نظرها، هرچند برخاسته از انگیزه‌های صحیح باشد، زمینه تفرقه و تضعیف جبهه داخلی را فراهم آورد. در عین حال، مسئولان محترم نیز باید با اهتمامی مضاعف در رفع مشکلات مردم و خدمت صادقانه به آنان بکوشند.
🔹
اینجانب، بار دیگر شهادت جانسوز آن عزیز و دیگر شهدای این جنگ تحمیلی را به پیشگاه مقدس حضرت بقیةالله الأعظم (ارواحنا فداه)، رهبر بزرگوار انقلاب، خاندان معزز شهدا، ملت شریف ایران و عموم مسلمانان جهان تسلیت عرض نموده، از درگاه خداوند متعال علو درجات آنان را مسئلت می‌نمایم و امیدوارم در پرتو عنایات حضرت ولی‌عصر (عجل الله تعالی فرجه الشریف)، عزت و پیروزی اسلام و مسلمین و دفع شر دشمنان هرچه زودتر محقق گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/447062" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447061">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ee4e0494.mp4?token=m7kqx_z-iBN2rt0CEovdtbxx7kg1YjXJlASqIk9ERMtV1SYdVergjIqAoGhmq-gwnANWQyBn9ZlKmgPNWoQkqx-Z_Jr4ZCl30NUYw1NkePv9MwdU0Bh-x-8U3L0reOAfjsJHXBxeDL0ffYp5RkfcX2DQWpMI_mDIovkY2KcQNAE-sFakfN9cZcKX-2TWk4IN3KLS7SsB_usoBseLz1fdSW43yBnN8_c891r2NBhEwoStFzmwXRgAN8Nc3KeqBtcm-k-udQ2Qvqejreb4WbJEvgYlnfISuVHkNho2b1hqy24eGfsWnS2k3ibZy08VATq6_AnsSIKdjwmnYQleKTsTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ee4e0494.mp4?token=m7kqx_z-iBN2rt0CEovdtbxx7kg1YjXJlASqIk9ERMtV1SYdVergjIqAoGhmq-gwnANWQyBn9ZlKmgPNWoQkqx-Z_Jr4ZCl30NUYw1NkePv9MwdU0Bh-x-8U3L0reOAfjsJHXBxeDL0ffYp5RkfcX2DQWpMI_mDIovkY2KcQNAE-sFakfN9cZcKX-2TWk4IN3KLS7SsB_usoBseLz1fdSW43yBnN8_c891r2NBhEwoStFzmwXRgAN8Nc3KeqBtcm-k-udQ2Qvqejreb4WbJEvgYlnfISuVHkNho2b1hqy24eGfsWnS2k3ibZy08VATq6_AnsSIKdjwmnYQleKTsTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مراسم نماز بر پیکرهای مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/447061" target="_blank">📅 12:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj4m_VOH0OWqZOoK2Z6USr9Sl69Bv-EZuXNmEw8nYoZymBHrHb2XjTlS2Qgc7T2ZGXZHPk90uv_BuqTC4Ai3Lt-j_sQa_jZFVEycK_DlWb1yjK7g7NM541HNjT5gW1tMchQSc5LdiykxBb5gPgsJ2_4UfGC6wxwQN4o3TqSVz_Y3Hh2p0N4CzdcYuLu8QDCGB6eAnQRpu0pSDnNJWtYCgHYhintARxnND0ikuAgnUb29sH2yELlSs3_H2kR-4CO3zKoh9goI1FeLSJbA9fAha1SchnvXp9-R-0sK2RCIDo0TwcSK-QZ2VF8Tg4TkH_hXsng-KE4TKI7PR5vgWNSZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در نزدیکی یمن
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثه در فاصلۀ ۳۰ مایلی جنوب‌غربی الحدیده در یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/447060" target="_blank">📅 12:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/447059" target="_blank">📅 12:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf96c87d26.mp4?token=trf5YFbZUs_RKrsXO90ZKApg273MVeOxP_YSnGdFBwXchrXnfSWADRfpLSTSUotU-PX220BYoPjKXWmHP1gqBO9AwijEVgYj_PuMcG7Gw8v3B8wLgjntRrgnImB5OcA9Fzdti0MWyIcAVnOK3Je3ysp3b5jHRfCfmCZGBNz-_uOANEk1NU31k431qBPrJmjM4FQSe56LKkWefZ_BgfCG-31h8UG_4ja2BUmk-D2F-f1bUfMTbW8-NTxZkh0PMU1bU16it65A9Sb0GagBukxc4_36QAPiV5abcyfHfsqjmbzW3h1SGVOeYk2DBAuwGP1dVkJxdr7L7Cxnbmo15p7SWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf96c87d26.mp4?token=trf5YFbZUs_RKrsXO90ZKApg273MVeOxP_YSnGdFBwXchrXnfSWADRfpLSTSUotU-PX220BYoPjKXWmHP1gqBO9AwijEVgYj_PuMcG7Gw8v3B8wLgjntRrgnImB5OcA9Fzdti0MWyIcAVnOK3Je3ysp3b5jHRfCfmCZGBNz-_uOANEk1NU31k431qBPrJmjM4FQSe56LKkWefZ_BgfCG-31h8UG_4ja2BUmk-D2F-f1bUfMTbW8-NTxZkh0PMU1bU16it65A9Sb0GagBukxc4_36QAPiV5abcyfHfsqjmbzW3h1SGVOeYk2DBAuwGP1dVkJxdr7L7Cxnbmo15p7SWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی ارتش: آمادهٔ پذیرایی از ۱.۵ میلیون زائر را در ارتش داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447058" target="_blank">📅 11:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447056">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
حرف ما عهد ما والسلام؛ انتقام انتقام انتقام
🔹
مداحی حنیف طاهری در مراسم وداع با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447056" target="_blank">📅 11:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447049">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcOFOE20gcQRsYunLL0DJNxE0mVO3ONBxg3U5of-ONsM5FqmjwT5I3vX5gFuc6eBem45JhkMcZ_qPfVr8ZvFHSTINuVuOsDH11oPzD2YMNiAMUXtX5Sag4MZ82pNFF97_9gGZDTJG8y_Qiyq42kiDHkURoAkpIPoEsVJ5LObDFGvoF__ve7kbcrBUH_0cwggRQZD2lVyiu_AxHmLDbTsNb4AgBNJCNoBa2TdbY3nSWWX56a6Kk_VR7mQPECLQfnilM0UuotgzWZNtPQg1W5v2gRXN6CFZs_YfUc6MFj4gNIYWOxGziobqlGsN4OGLZSsOmHwcjvDzX63hXkWKXbQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQxBSvb0wRTOf7_u6_jkkxME7ZSgIomxq57dIn-CnKCdJMb8tFN2UQZAHvgsSRcTP7_l36WCd1nD-hS_aOpe3nkUIHZXq7PG0h-Hbt9er2NZ2C1gTpXQFk83VQVmM5c6ytxtq_CUUGFq_YkmZHazHrCbl-RyGv3OmcFa57akpRCPKHaBtQC9ydP21KAlQAJfnfCOBf7PSC4hX6y8NeZL5q-t06Anc4hCvbA0M6yJPVJ5nNjCTSNRGj_5mf2q4vwaonxcrp9UK-X5zRxkhtz4hqMzHItuyCL66WTkP1viayWooN74OV3WUAkgTmO0nEWS1UqBBdhJg7-afy1QUn2GnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzXwBJH_hQUVBIgSDcXRJ9FY8a2i258auhAP4WEXoitkVFecOwXbkoyRr0YSrciibS3OBo_NZLfKeKyVxlGBV4v8xv3c5eF9G4Jp6CI2HPjpanh5Fkd5_HlXmGX6PcJc-9zReIHzPznEoF_ArBCiM7_9IPhCHjI776fyeNrxdJ8DBmVJKlf0GLoQUR4dDd-pwsqLr6F0QfJVhXWgWhltlvo_NOgmM6cnrvqTrdaDK6uUGvU6UzoCmv2eKnmZkNPePXjBTrdkHgAhEM2YFCyHhimCMjYNP402PJAwmROhZXYH7aoMiI3zlPxlv1yFOlKIVwBcyg-npHDY9vUYJ8xGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHi6A926GmS5yVI2umXMo__yC8gVBbIeHyiXtwe_tvkLV0YNVFD1p1FOV5I03DTINGNafjB1Brz0RNCdTiZPckTnAsAh_3Sncdw6QKy875rXyJgl-1i96RQfsSWOCnGadxEzxAFmUCUYnUYbDQT9bb7-a1eAZVQLeLrtjbHELIWbi1_dE_CPQhR_Yjn6qJVrDq1UCOZl1pr_8M61kosD8TKudJMbrg6IPIGgkVxI6_JIcpGX6RkNb8_qB7jJvO6tm4T5w0Qj_a2AyijNnTLa8z7fGLLQ9x48BfKKsDHCd7_3-fP6lOy2aDGhuLAElsnzI2-Oby8Hb0eE_K6_ZDkerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJd4P9WQXJ8H9LroAMNJ0Xt848m22aIS_0DBNtG2q90EKL0I4anN0Ee5gBvBoqVaCMdiKgkpQ6ebZVuTlnig2Y-lF1JHY6Czts3gMmLjJL0byO18KBwWO_EwBy0gFp6fcnfayTzuy_naJwlAPIzjGAbFO33ZbMSC53CQTyb1s9v9yu8n47KxwHZO9k-WGr8OWHMTHP3rkgY13UbTewfmefkjVBp0S_FnCn6LZ6sMMoBb_QcCsYoyfsABpknSLNrhFkgWnZ7elgvta6dc_AA9mrUGYZFPmpiEHonjzmYZAnaEbTuXSo19Nd1eqbWTvaz5hDmEaE3W6evPaa3fBgSiyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-FjDbzKEMbWoCLzyA6BDJctc8sIA82jas7wODAruHadSupjVRjWJZNMUxG7xdtP2ba_aKU2CRl1H6s9XDnGJXQ0HhC5aMD3k9ahdl4gmIqk6e7b-o5hDuo4GEAPNVx3XaOO53RJ5jLyslEv0EABbYeJEsfSyaBU2kogHDszRPmBXeWHEcOJ5LTVHjzjybCj6JT1RtwJ_25RON79K68_r5sMoAMatMOsrL5WDXDcx4KCsQRSJK84dkoCSNcHmc-g4whr9DsyHaiar_XY7MQUzRl7x3WLViKsZG8P6bjvQdJ7eYrB2FilqksD3-rJUj5285tI1_kM38XIv6cC2oFDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYL4G8mAYPb2O2RA32EO0AubbAJK-jaUNLsHSOcWNTBozl9pJZjCt_5a6HqFe6GThBqpWL_gFV9QtA3-AqDsMPAp7Na-lBsr_2vpeP9jlC4QZg9gg7iWR6WvHGOzgEEIScwzg1cbXecwfbTcDVjna1nAE4RzAfiKgyUjYIa4_blMlSAMDBdnyIawSFJQskNJF3tQ3SJki5iHwjM8F52B0mVgDB5JdVHQ5vrdB2DxZktbTl3vv3uAGtKb_X3TXUOyDxyGXmhbXBI1YhRZIF9JUIKsTNAS9IqSMkk9eIqAALdhpAQz79dD6eoGzAJZLVcU4s0vKVyxKhVfT7W7uGNR2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عکس‌های دیده‌نشده از رهبر شهید انقلاب
عکس:
مجید مردانیان
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447049" target="_blank">📅 11:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68393ae383.mp4?token=Hr7u40fAkNNZgggHAURvn4MzIV4JiMQHEVTJ7LbJpfT9Y-R3J56IOFN-1wxAZs445na1uNrkr_rOJ57ee5TR3-FuK3eVU9jgHUF_E4zFr_S84uDCaBz9g5s8h1mIluDNWYvs5cxaRzihbj6Q77WvvHTxdV-IZhNnH0_OiSxe9S_C4_sFV_dUHrjBlpj4uWmaiqqbmYRSubaJYIpfqFWFjWsTgFR1iDVgj_fIRg91FOmkdw6CAlA4tmoJjy00rbpBAiXqRPupuddwCpqzjU4op9rGW9rTFMWd3QIUBN51cxaYR1DduRCVgFlHkp2ndAG1vTaSCIBARPXXIC0t-Pbzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68393ae383.mp4?token=Hr7u40fAkNNZgggHAURvn4MzIV4JiMQHEVTJ7LbJpfT9Y-R3J56IOFN-1wxAZs445na1uNrkr_rOJ57ee5TR3-FuK3eVU9jgHUF_E4zFr_S84uDCaBz9g5s8h1mIluDNWYvs5cxaRzihbj6Q77WvvHTxdV-IZhNnH0_OiSxe9S_C4_sFV_dUHrjBlpj4uWmaiqqbmYRSubaJYIpfqFWFjWsTgFR1iDVgj_fIRg91FOmkdw6CAlA4tmoJjy00rbpBAiXqRPupuddwCpqzjU4op9rGW9rTFMWd3QIUBN51cxaYR1DduRCVgFlHkp2ndAG1vTaSCIBARPXXIC0t-Pbzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اقامهٔ نماز بر پیکر آقای شهید ایران  عکس:‌ زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/447048" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e7fb3583.mp4?token=OJQlyF7tpVt424hxFe_Own4GupC7drhRECTjCNUnz0cCup885_xEu6VaptyyLh0jtmtYIfhvs-cUd7CgGxincKHwAw7Lz7zjbhag5v_bIlN4AYR9BDUiH3D84bYATq6A75AQq8kaHP7ptsTc4SHIWtiDIl56A7bfdm7xTyFHqYvS8v97ohbdMR5e10xhzeXKuL6fu7fnK5FjlStLeHvgBiasqjLoVQfjb2-CiOcD-aC-Uvf3ITIjh9GXVbxkGJuUd1JO_HYJ-iPuCn4V1Pc2nfSNVK1ymI79X0ct4rpeVKCeMcz_XD5eEMlcwN3BbQpbHdEAzgV696h8T1PThbZmm0fdYKzvrrj5OWcSO1E7TY3AWfGDnyfE5NvD7qPHl70mZtHffEBGILrWi1Y7OXb4zNoklH9Reym3GiSm9gPiUK1qO5-uZJwYOb26m6soHQnIXLdXC_FON9vHo_ZTwPg_MJS3S4Y-myF81i5htbebWdEzK6FSMBjEfrzDykXJfSgzADovdxLZHi_ywGgQRXp97qKW4S_lK7URfGH3EuBJoC0-eKVPGbuBcw60jjpcRb-qBWQzoZmMqxmCrGkDrQ4TnFKNavXVeYZ3QcvixTXND6JbyfggzT97VnoMIvMuOfdusz6fZrdtUYpgS0Dl40eqavdgQ0FnA4x6IZVQgCxhF_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e7fb3583.mp4?token=OJQlyF7tpVt424hxFe_Own4GupC7drhRECTjCNUnz0cCup885_xEu6VaptyyLh0jtmtYIfhvs-cUd7CgGxincKHwAw7Lz7zjbhag5v_bIlN4AYR9BDUiH3D84bYATq6A75AQq8kaHP7ptsTc4SHIWtiDIl56A7bfdm7xTyFHqYvS8v97ohbdMR5e10xhzeXKuL6fu7fnK5FjlStLeHvgBiasqjLoVQfjb2-CiOcD-aC-Uvf3ITIjh9GXVbxkGJuUd1JO_HYJ-iPuCn4V1Pc2nfSNVK1ymI79X0ct4rpeVKCeMcz_XD5eEMlcwN3BbQpbHdEAzgV696h8T1PThbZmm0fdYKzvrrj5OWcSO1E7TY3AWfGDnyfE5NvD7qPHl70mZtHffEBGILrWi1Y7OXb4zNoklH9Reym3GiSm9gPiUK1qO5-uZJwYOb26m6soHQnIXLdXC_FON9vHo_ZTwPg_MJS3S4Y-myF81i5htbebWdEzK6FSMBjEfrzDykXJfSgzADovdxLZHi_ywGgQRXp97qKW4S_lK7URfGH3EuBJoC0-eKVPGbuBcw60jjpcRb-qBWQzoZmMqxmCrGkDrQ4TnFKNavXVeYZ3QcvixTXND6JbyfggzT97VnoMIvMuOfdusz6fZrdtUYpgS0Dl40eqavdgQ0FnA4x6IZVQgCxhF_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سعید جلیلی بین نمازگزاران امروز بر پیکر امام شهید در خیابان شهید بهشتی تهران  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447046" target="_blank">📅 11:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336805f5f0.mp4?token=VuLdfOKsfmRda5gvEEUi-USH3oC4Z7kthUs1HdYJY-jQIxWDZSFqimpJkrXpiVsJb-UZsfT5l1jZnL_JkA1vVry5jP6qK2flwTnBckKwwM86Oh_hTIw3SvZGERyEaUT7HZ6s8LVJYfJFAq7TXzEHMaEuTbGmq3ZbV364mYK-QraubF4p9OxZklf5XFbP8i1ETiesBMgditspVjVO8l__e6X8DAqmXK3Mvs8M5bTCZ0AwRfpTQYuiM-3ntbRBAKO6n6f_8Z3LXi1Ft_RcKlUomwJDhMZFpJ6904NkiU-H2oRrvamHMZGFb58O5zo9Iok_qb3g39Xhkn26erkLgKCvdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336805f5f0.mp4?token=VuLdfOKsfmRda5gvEEUi-USH3oC4Z7kthUs1HdYJY-jQIxWDZSFqimpJkrXpiVsJb-UZsfT5l1jZnL_JkA1vVry5jP6qK2flwTnBckKwwM86Oh_hTIw3SvZGERyEaUT7HZ6s8LVJYfJFAq7TXzEHMaEuTbGmq3ZbV364mYK-QraubF4p9OxZklf5XFbP8i1ETiesBMgditspVjVO8l__e6X8DAqmXK3Mvs8M5bTCZ0AwRfpTQYuiM-3ntbRBAKO6n6f_8Z3LXi1Ft_RcKlUomwJDhMZFpJ6904NkiU-H2oRrvamHMZGFb58O5zo9Iok_qb3g39Xhkn26erkLgKCvdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نریمان پناهی، مداح: اشک‌های مردم در مصلی روضه‌ای به وسعت کربلا بود
🔹
این اجتماع عظیم، مشت محکمی بر دهان دشمنانی است که تاب دیدن اتحاد و عظمت این ملت را ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447045" target="_blank">📅 11:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRuapXrTjsB6Yq4YFQz_iNRAFRIlq73vVOKsj2kBFj074fpkfy0r1lfJc6rYmQZicniSCM3EYzF3mvPuhWHGwG1gOq6yzc492VtW_Iyw_kN-kmu93O-9d9y3AtgG9odVwLBeemDBY6YK-sHK0OzbfMJneKTbzrBUgIIHhul6F_17PwCX0jimJCYWvmdz2Gqvc4nHswWUE0S_N2GzuKKJ4hc9zt_hLc7BiI4J-eEMTP71ab-uzE3m8Trv5Sfss-uRpCWsz_DHFyAXXJVenfI9sVq8kQYqIrAxxTNEYQ5uUhLoo8I6e6JEbkknBqil_kYoJfVSXbo5iiiM_QMjSdJwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۲۴۰ اتوبوس در ۱۷ نقطهٔ پایتخت برای مراسم تشییع رهبر شهید مستقر شده است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447044" target="_blank">📅 10:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne_2v5eMz6tdQ8OrmitMKT3EEgStdKpRRMuFQ944y5DgzjuYZ0uQ4h_Q8thCBva6YJHtxfiJvgHGCWvIeYjwU4NtIRRlx0zJhVUOBY-sfK9sJxFGAOpUnrOMtc7CJ2sgJHi3L70gnFJdUFYfQLlpLYro0Zjm5bnX0kn9W5YS5W4W0RftM5p5fRh-Kanx23byBp7rvO5eaYN1RQbuXRS62kV3WKG8eKkM2K7979NxiHpOW6n2JFALUBNPb67FbjNvizCH3wVkgpSxbvBNcl3I5Wwt9NPmfwcpjQbl0_LFl_Wwxh1rymydwjKXayGVv0LiYzihKUB_pUX3_p0KyEdYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eICRSAx-8I-x0q013bEVCg9TfGxLYPT4U_tcqFZBsvxFosq76VWLPgwIh6xsLK-WhQDsU2Chj-aQj7fSuvoYyQ3DEUvTd5NYJCsUN35LMQrrqB7lLSymsDlB7Sy0_jaztZpR7qHy6Y7MmavhDakFPbNObf5WijiOHqEoe61rKLqiUUpbHcSP610dbVfHnppIlR_uZEcbNmniNuHcpfDKGOLawQvidAdS8S7uDhtYhB4NFfd8--r4wTTehLHy0swVYdID6bHwrkXWKKWlsTcfcbRzQHc58PTiEfnva_PhGOJLwzzqVxCc_pDiVPVSQLcEb22C_vPE2BsGIYUX6hP-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rneJOFsrtNTRbITMNzpmsSQw-yr8bAsEfWup4BkQOlbR2fuHbLCxP5oUwyzTcpD34UoVkzaX0wDquqQQZ5Xx6Z-gWPlckjac4NM_1ZIrMo6ZfvICkYT5PuWNoklphcHnrI91K9Wyg2iYFTDwCGohHsAYG-KgvEe8ENTMSvfCsmtjkXeC431FE-_fvf61-7hZC0QOv9aihoRbFahpPincyllxjtSOqFo5xC0Dvg1ohRyWQb-D_agIU0WmWGRFNJhrFSC9GQrz5tXgUl1YkiPxKthjfxKbF0GOeLyHROGxi941Id2bTiVYzEIKBuv2M8j71lm6QUQk0wtKd_Z2nXHYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N585g-koP-De2FVVzNRrl0uuYvIZDrD_f0WKToGpzCiul3tqnm6DKwoJOc-5q5ICMfHAMAm0ZCcWTRcpyjjNw88TheP29JQfikDZ437og2AdyJCyKk2SZxkoDYvCP_HK938GC7t4dYU3TXLpBGJt9kCTOQ8BtGSSjloscn1FYZqgrnjR38FIirdw6tsT9nVuUMh6ga2W9xjgoQEQHHb3eq-mZjr7aSgCGOHtsFphz0H4h7ZzIsvq-v0sWASfiqRRfHvGv3aYhMtW4Eb9tRGfMMbOUL-Lz5hpr5TF4AI4SUxCG9q3wu6FaeGQ43LonDU9UPCZAdX4yb0KjItQX4XOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWkzLf3cZKwzz2Kta-vmuV3kSvcbzlMGaclTpEMVhN_dOjWQ9BXo7SO2iAlTwSOam0wdk0-5TgbXQm9IDd8bw_P8L1Kk85tWZb4I0gGihXa6iV7wvXigTHoaK_9ozMpzIDCa9Pl8uvEgIsNQaI817xRgdbI9gftvtaPLHhz01ne-Enwz95BUAcOCe3Hu8bEhgrTeefnC7aBASzS-qTl7yDJVXxppB6mKlEg6i5FnZFeWniBEs2zYuqoH1LUDIc7LEY7eq0glTOIc9pBqbD1vnIoDIA05XObJnQn-9Q9vkzKWuEJ7GBAdnuAVA8uj0kWfnCEd_ySkjZQhFMPIZQgmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czjW3fByoSGZoQBwsWx1meEvRUg-29oEvo0pZ0mlf1tfSYs2y0HPEfTi_JdewEaWfpoY_IV3VoMn5DAMuDN2zwa-sQ2SxmqEH2UdkOniwxCY7HvyJJD74amHPqc9ESJ_SFwOsByPeEvWlcMOXP-MUC-Kbs7irL8NPl2hGfXC_eglHuILSubJk220tiEjdtq7iFkL3FsYOEBKCMBtSmgZ8IMR-5jYNR74zxFMGoVlk3YEYpzbRu_R6n8iinfc29TjvY8kuBKbIzn0h2t1clAtl3E5Ls-OVeK4sLaUq4ft5_uuY6o33RxfTWivNgWeov-wjqEcDvfwNakfPJ8Knojxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfNZtZuNVShbQqfFTtBr5vTdh_NZM6lGkmmcow3yo308DJpLi1nr5un3zCiVNc63i08qVE33uYYs319MB3n2OEhdgDldROP8WfDZDa6_tAKyhDwH0CcxaeFNi3j8Vpp1SbVIzCrI8UZlVtzRtozfHE7mvQpsRD9bOHnrfDL51_LUek1-ocDPwuQnpL2IYziSbkU_aY7pB0oMeU4BIExcfQ0LUGf7DgMTOggV7hivSq3Om9SfUg8dwpN-uoHVb0hrMg-yH6ycNsldjeVmeVlRJIVl5tHtEP8nKyih8DtnzT4DnkpEwjM-qmT_dK2PN6TDSDzPNBhVFsYLvSp_j6x1FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر امام مجاهد شهید حضرت آیت‌الله سیّدعلی خامنه‌ای و شهدای خانوادۀ ایشان  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447037" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">◾️
لشکر ما بقیه‌اللهی است
◾️
بیرق ما بیرق خون‌خواهی است
🔹
شعار عزاداران در وداع با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447036" target="_blank">📅 10:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqJvYTnsM8y64hoNb3pdVdFC6luQ18DWTCKsBjtsMphsigZKJmxmMoPKNFK4hm18IRmY_ePX4qlWYHJIBfMj0vnwfCtfhbEuwQSIsvyWmcWkjYVEVT4CgCvyeX7VaIo_4-Jt1_-ZNaKMGmvmrdEtg_WI21GQgYVGqhYfECH2KqGahAkLntIQ0gahOOS_XukdtQS1i4hL6cd8Mi1k4s9c_wmkZBxc-2cGNH4mGGslxFXIPEucBGaDf-VSlDFrKaBH9MYOtTmBorFXoWqa8YRxsnBkmFvUjYrl6kXa0zjqj_hhj5B-c4MPpoYEs0TLWkNrHjXC7nmBGju3TwfiKzNZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447035" target="_blank">📅 10:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760aae9bc5.mp4?token=q1LY9dnEbiVEd3sznrZ-bJtikG-_-LhWQ41sHnPGTeS2eLuyvVrqCKpzNwPfQ8K2wpzK8F2cmLFjgJrIdJMZ-6HLXhqmGJ-QgRnMvjOIfC1oxRVqUZLF8c0mHhA6FsIUMr7W2nEAEtOvBvRGmTD1J4IIuW9Yu28GzeEzN4gMRYmtYbkxSwfP32V5SZYMKnOoTubgMvxZmvCU9mBlshXUXlsfp3237JNU_MuMQW9N4DDRnAVaU0E5doVwQpiAlITg6ITu6Ek8tB3rFLEbQJ1YbXjLYScyzfcDOISqjrpsuXWx9RxpjBfOJUsc0Y5JlTPSRcRcGXZ3iBsz_GWZBvBjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760aae9bc5.mp4?token=q1LY9dnEbiVEd3sznrZ-bJtikG-_-LhWQ41sHnPGTeS2eLuyvVrqCKpzNwPfQ8K2wpzK8F2cmLFjgJrIdJMZ-6HLXhqmGJ-QgRnMvjOIfC1oxRVqUZLF8c0mHhA6FsIUMr7W2nEAEtOvBvRGmTD1J4IIuW9Yu28GzeEzN4gMRYmtYbkxSwfP32V5SZYMKnOoTubgMvxZmvCU9mBlshXUXlsfp3237JNU_MuMQW9N4DDRnAVaU0E5doVwQpiAlITg6ITu6Ek8tB3rFLEbQJ1YbXjLYScyzfcDOISqjrpsuXWx9RxpjBfOJUsc0Y5JlTPSRcRcGXZ3iBsz_GWZBvBjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار برای اولین بار/پشت صحنه آماده ‌سازی مراسم تشییع به ‌روایت سلام آخر
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447034" target="_blank">📅 10:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447033" target="_blank">📅 10:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
قسم به خون تو؛ قتل ترامپ گردن ماست
🔹
شعرخوانی محمد رسولی در مراسم وداع با قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447032" target="_blank">📅 10:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b4c7264.mp4?token=hv5o0UKmf2lD41rKPcadxAaLNhcxtn1vStf4ZOonFm61rJhjCCCwLjodYxdrqhfyoryjHyCvfDfRHs_kdcOSfZ7VTaObHo8eORbsgmxWv_4jYW_3-rpfMMH4Yp0O_X7SeroyUhZTdAWaGKsP-FRvors6gQxeQIYS6gmJFum4qMZ9bNQBpGZmEdKome8cfNCnpBKpEvrH3mbbsvITN0LDYKybJsUze3d6DrwaaacW1gTAgYecE_Pcy6tIAyyR7a5cDb3gesmH6rPhmEyAxUS4BILx_7OBvRL1nQWgwPieN0jwu91EB0e79x8KQxzGfku9AmPz5jfiHiUgAQmelLbzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b4c7264.mp4?token=hv5o0UKmf2lD41rKPcadxAaLNhcxtn1vStf4ZOonFm61rJhjCCCwLjodYxdrqhfyoryjHyCvfDfRHs_kdcOSfZ7VTaObHo8eORbsgmxWv_4jYW_3-rpfMMH4Yp0O_X7SeroyUhZTdAWaGKsP-FRvors6gQxeQIYS6gmJFum4qMZ9bNQBpGZmEdKome8cfNCnpBKpEvrH3mbbsvITN0LDYKybJsUze3d6DrwaaacW1gTAgYecE_Pcy6tIAyyR7a5cDb3gesmH6rPhmEyAxUS4BILx_7OBvRL1nQWgwPieN0jwu91EB0e79x8KQxzGfku9AmPz5jfiHiUgAQmelLbzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سعید جلیلی بین نمازگزاران امروز بر پیکر امام شهید در خیابان شهید بهشتی تهران
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447031" target="_blank">📅 10:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
همونی که براش نمردیم، آخر سر فدای ما شد
🔹
همخوانی محمدحسین پویانفر و حسین طاهری در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447030" target="_blank">📅 10:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqGCDdVeL1OGutYoQKSIlTcgfrdpQC1IyF6LP7DnNFIsliY93_dhLnncXJSqSJbfpqmxN7JryOB9HwDdu-hkZ4vii-dg8M5DPc1lAWXU8eWGisbuj3fBytUK06QDfpT7yQuYx6dbIiMJa522Nx5nN2T5xjULJE5VqmdTjM5PVzlBWcoMU0Ch2XZ1mLX2Z1dxE1OKvsE1WaddbciGp4zPhFlTvyFlrpBNgRYxDeOkeeR8tjT1zp8m8hHHgDygWhK-oXpcbvPtBb2Ie2_UVKemYpf6H__3JxSGNQjz9FW2nEAkwjIiDzCMfvOJd12vLNSyQxLVT1UbyFVDqJYJPEZ4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghq6_3lnyidRQpKYW4q1ANdCUVqVVWBhOtoBhq6S1me-TTVTb22WmndQwgFmN2I23QTnyjRLwKhpF_pst0PF7fCpkDNz5tTAZGcuJ5Ypnj0fVP2gkGgDYCW1zGyiPkdWN_FZCBuyc6pcYqDYurDwzbJcE16PF_Y723N1TXsMptNLatLq3itOPcblOmFuJZObMIsXLYKK5v2W6MnRpzva7wIxf_FqgJqY0Pkzwyu8X3G2nXgQkckytKUZfzX4XBs89U4zw0RX9XnUa_rNIz7287pAHlmgwDiGsgkpbfU6qtnB9yWDhcPbwyMTdCX3WEu0yb1_mqO3_-9p1jjYFaMVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-WtCi2dOSJ19jR-J2thPFg_A3ZUhA-Wc4paqfAlgferpYBJlD6p9ATE2th6Rb9sicz2v4I35itNnwHdUqEnTfNQEW4l1wEK1wcHZlxGl55EXun8WVz5KoaLDvqRtN8-zMNBplPh5_3CAx4ZzP4e4qoNCGTZka4d3Yf-G2qdUyBxzrYc570zCBmMR75zENl-Z0BtAEG81FvCE35OUC3fxAnXS0LnKyM5JhU9tHwgc_GxAhztgOU2tDGoqLzWENNuNv9ZCk0EU1W0JRfNL_phaio1I2r-wK4jueWlaJTN4C49o0Yn2ZxqO6xqWIEx0MGmtGZzXMIGur7ciJmYY0Xf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiHpReYX2eCRoa-jpRYMdieQb3BJ_NTvzgT0IB3OE4-o-nB-8zSP07L5ZBPr1_Y4TU8xCG6iMos2Y_g7OYVrS7pKnjs-ZSohKtzRBLiWGyOdK5UHnC2zkEy0_yOnTKRmSgLFPgROg7GflvrCp06pcAQbrTBB85oDAeHF70sZ9ZckRnwQpb2xS6lTGspH3Wseht36bXUH7nBthBVULPTxo7593DVqbu6VeFP83qqifSxmXiFfBAby8psepyeW6eIVTRcTpES6H20eh0buOPXwYI5iN50m1rAOkZ-kSY_cUbauUNlf8mnJBR8x6acu7WRNRvnnEdDsrt0LoHlDfdBzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RR8MIv62l_cSgMaABKPlDdnvL4rCpC6yvV7vYk4WqxznlJYPjlUMb6zkw8clNeUpKwW-sZxlkZdbuy81QUgc2ngF9nVS7QkPVdPZ_lhMw1GQeIA79RAC6KlPYXRj20Ej6rpKSujxbBhgQRRlji4cbYgx_AbsITTx83qkhLBMz3aiPcCVlVe3G-1jwU223g5PwPAxUSsqVhtvJfwZ7iE19kKBauMSGW9ia2uEzHHbBHYuTvjbgyTcr1yMp1d4IxonYt7TPIzNha9-ZEg31193m83HU83UKGdKBn_Frj0YumFlDraw8d3frVBMC-69ddD956PEmFQZ72P-BZP7jigK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eE-LRwj2PWmnQqnhJgnAy5A8fQgWdHr3NwKbZ4Kr1ZCrGcSg2JWR5TQEZEbo_5rluvOCmihcFFwg41qGdOcck9d8-p8lNj3y1fQH3dou-us-7arQxRI3jjtbZmvr-9k6HSsJZSIAk63UUwUezfh_xv3UapeL_7vXM3XD9GUpunr_GFXqnezvwHwL-aGknqyIzGwU26cKLDU0XJJOgySadJXm0cjPV8SzY5yyEyPGj4zlpqv_nQ0X9VIBsTtrfOWN_NeiaqiuwEjSCDkFJAN2NsTlIOa3SKo94H4lCEWRF9f1zKIUbCoWR5JIUdnJG3u4GcSuu7OdehU9w5vaR_MT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P29NzXkfb1FJC381_3HuZj4eTrwVyMB-v0sXqGRJvaxPeDLz6TpMrBcE5bku7iOHanu0Paan-iv8RiUisIoCvvHinsiEXmMLGLRV3P_w2Ouc2qXXiRSdvXBE242J0o9dfdBtAE2b_qMnE3XNEMqIVpxm-ZYHDlEfN5lB2_lJegMvge0E36k-cZvlNcCECHsDCaHDfMZufiiLpBkmEQ2UeD3Fp7-kbE-xKotmGtEa0Bh2eiw42A1U_mckaApg4AprLsNrZRRCPkeIUQI3ZCzNsvkNxyQf_Y4nm_VWLkN78lO3LvpzLRbho47uPhDFc4BZ7W4AhGv1FYuCNFn8T2LWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3O-a5ZU2uIRnklJCUVoy_jsE-I4Lisl8-WQSK7aZ4v_pOS9oqUOnEvKj6SQWl5wFWsMSiTICir1eiBZBjgBHoqyyOtC_6oiTuHnb-lWYNOz2ZD1L43l91-YvNDnfF5Yb9BHNV0ZfANSPwA42cC3n95jF_xZ_TFye1W_HwGP4Ca9otUnz69992cNNtgmdu7RWi4rZ8n9HmpvXpmEHmzGALDp1ZkPPeAx0cCVJdMHzWSpD9fMiP_whWLWeRYVZbGkThDVOui_URbPNS6MKUmV0N5ZdPjzli9rVly2NM7_3ZmXOcR3cM8gA0d1sFQQW6_RAuEJ3A-TGhAEugIJBIZAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic5CnfkUXfKHvijlEEwGaWGA3zS4Mqrv0etWmPQ_LaOxgnsJ0gcwb1LOVzpetMEIUUo66mPswSmrkbFr4FPyTkHR1oKWhmlectWyZ1BUdA5IOfJAAyHbL2sh1Iqnucil_AkJx09I5O76S8Yk_YgZKEv_cKQrqLt67177W8SsWc8fNwIhwclFqQX1T1ONnBIr-GUuqz6WecD0MwURb3dq3y519X9ApNn041VOK2hWvcPcopZYBMmPGeu0H0gb9Gx1KiIsxjkzi1HYVnb_v1TdA8LeEGzPeCTijBuIqdXTQpPBWs22-l231sqzrN2C_CKXzmy0ALo8L8InNHLg5dnzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vfj7mr22qn5WeGdh1DIefroD5Ey702uF8jvI-LiIinKXjaCECOols3podYP3LTC9DXBktFTiZu19UDviuMX5NZ_o0v3GqlA44sPM6_cXRpqytxxmhTTEHLoLqfoV2xPz7YKp4QRNMMTOd0nGCHvFMpvc-tTkarXoLx5sGZSU-vFeN_eiZrq5Q7Qj8m3hH4KTk3GS69NHZeIfQH6eBhI-k0COODpxpei6Obh5n5j8iQqajTe-Z4OzYOAqjQUpMDygF9wN71hq9c1Tw1LLfv-lgPh_3J57M4O4hH9_1t8WxoBHLcBLqqf6EuIlwqCtnYzGqb4ygEjjb132A4kYhV9MpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر امام مجاهد شهید حضرت آیت‌الله سیّدعلی خامنه‌ای و شهدای خانوادۀ ایشان
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/447020" target="_blank">📅 09:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPrlBOFTSvf11CS0aw2ASbas3HvIeS0BLIOhEuWow20TZ3kdafTxnb980Cs2GnGPSjwD4xLIxezJ2KQMjv7QZuiPNGXDdHoGPj6VXlgH6XJ9B086epc9lQPe6UOeNQHlCQ_j0f4zeg2CGSTePGDoTH785VTIGZMxLdwRtnJ6Txl7piivK5y0S7NhVrL99xFI3EHAwRGOEPy3uiRc1y5pZZJw5O2WHC7ri8r3K5Ir1immDyKp5-HB4tk4gXjiCbEMopVy7gtmKhtPK2Qpo0D7dKH-wLFUFbDcOACLusOpeyUljfzp5YvTte3LFwTjwG-QUR-WkW2jREBzl5oGZ5Lz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از خیابان‌های اطراف مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/447019" target="_blank">📅 09:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447018">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3409f584cd.mp4?token=ntgn7KMqgxBxxW1CrJX9hrBut2-wT8FD5yX6Lju3cqafnLrdkYtqlNGBqzxUKcIgQ3L4HqY9PCNE2hvl0cNs2XvvTKHyi7rSTO8_1hvYD9dJK1zexXEMKvrr5jUtOy5w76tuFuC2PupEO3MAgk9gaQX3XU_IwlD1w1HPaZcWxBcvW4vFejU6Dp-uxt3w-0V1i0TGiVylxi5laKdXfcb1187iJOpVe6QzlO1wRh8AAVGlGsGUCv6N9l7mJp96ud6Kcw5XnlsxC0Dnf1Q1a0cIurWqR6Zlv76fcwrtL33TZiQdZTNP39Je9HH-g25_tqsAcJ6kG5Jm7LHjXo8RVttREw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3409f584cd.mp4?token=ntgn7KMqgxBxxW1CrJX9hrBut2-wT8FD5yX6Lju3cqafnLrdkYtqlNGBqzxUKcIgQ3L4HqY9PCNE2hvl0cNs2XvvTKHyi7rSTO8_1hvYD9dJK1zexXEMKvrr5jUtOy5w76tuFuC2PupEO3MAgk9gaQX3XU_IwlD1w1HPaZcWxBcvW4vFejU6Dp-uxt3w-0V1i0TGiVylxi5laKdXfcb1187iJOpVe6QzlO1wRh8AAVGlGsGUCv6N9l7mJp96ud6Kcw5XnlsxC0Dnf1Q1a0cIurWqR6Zlv76fcwrtL33TZiQdZTNP39Je9HH-g25_tqsAcJ6kG5Jm7LHjXo8RVttREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثبت بیش از ۷ میلیون تردد مترویی برای مراسم وداع
🔹
همزمان با برگزاری مراسم وداع با رهبر شهید انقلاب، از ساعت ۵:۳۰ صبح دیروز تا ساعت ۷ صبح امروز، ۷ میلیون و ۱۴۱ هزار و ۲۱۲ سفر در شبکه متروی تهران به ثبت رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/447018" target="_blank">📅 09:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447017">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=l1QSy_7MHat8bY03JiT2dt8W5JtqptDmS5awn16fPsVsU8Zum4ao0XP-8MrHDtRUpVXqQ4t9V1Z4rI1Lo-lJK9Hrny2AAwI4JniR8jVcSt5K0p1BOUb6TdNZG7Az2g3S5lecrDLuqqf9p4ZuR40JJeVTxgJG46ibSxzGHz-D5YXhXqdzQhLxDo-XBu0s43DzA-DX8XNRpPFodD5pbHiq_CwP5-vv4lnV-iImWeHGsT0MOZ6bUTQj8C0BzHinHgoJL4VzjdQRC2kw0AmM57yfdjmz9GONQzmiTCGZGnlu3FbXKvwqI2GevhZlmzVapFM-kNqtlZveFU6qzGE0YYYZbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=l1QSy_7MHat8bY03JiT2dt8W5JtqptDmS5awn16fPsVsU8Zum4ao0XP-8MrHDtRUpVXqQ4t9V1Z4rI1Lo-lJK9Hrny2AAwI4JniR8jVcSt5K0p1BOUb6TdNZG7Az2g3S5lecrDLuqqf9p4ZuR40JJeVTxgJG46ibSxzGHz-D5YXhXqdzQhLxDo-XBu0s43DzA-DX8XNRpPFodD5pbHiq_CwP5-vv4lnV-iImWeHGsT0MOZ6bUTQj8C0BzHinHgoJL4VzjdQRC2kw0AmM57yfdjmz9GONQzmiTCGZGnlu3FbXKvwqI2GevhZlmzVapFM-kNqtlZveFU6qzGE0YYYZbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای غیور ما، سید علی صبور ما، خدانگهدار
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/447017" target="_blank">📅 08:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447016">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwL-LoT0OWZmeRYVFVtpLxXUVLG1q24V0FRavAiBCbrlivUUn5v6CBtO6C5ydBgw14geBMFSjfWVNNaW1LDKOUMJPF8R72scbUBWzcCT_fwCrKE9PCpyjW7VdpfPmPI5yYkPWQdPdH8qJh4vbagNr2byzDSgX8FHj0cHsFG-jG2574gwjn4hInn3Jtg__KPA9IC4FSFOb_kMVi3v8Oxb1SdwtTQCvAodUX-3WUqa6Hifakfp3vIpJv-SafO8I6mamyo9OmvTJhFXexPKWZnooLd6z1Jt_56Lo-Ya2e24WzQEscUD4d9dTAGqQuQalTbcKIxAx5mmTG4y9xVaaI_ZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور سردار وحیدی در صف نماز بر پیکر امام مجاهد و شهید انقلاب اسلامی
عکس: زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/447016" target="_blank">📅 08:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447011">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1AZMBCqXw3zvTj6yPiTH-L-aIHLPWXwL9jUKOj2XYYt4i-ZK0uOGqTNUqS9aKt0CMbnbGo7kpwDhSIt0FCEhkGZazaaJ5Xy8vqZRCdHrs2E1j4NdLKqDGWsN4w4-bLGRpEY2bc2NRV5T4MO7omelZf49-D2Eeujj-ivJowDB4cQO27wep6HeOV4jJ5UYJMGPBqdaIjnpXy7FqOUCqgz7CssXtH8OsbuvWuzkg5ZvVvbxS9ZXKzOL8SuLvES2OwEc3BVvVH-sRlQFfD2yP4I043Iv4maAqT5T2DvXfVYHmWxhvSKt9y4nhQJnPQno0eiDku44FMN_bMFVW5MudrJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLF5Sx4WaRL4IBR_24wcmoFQtxkFi95NB1yferpbVJ8ScE5khdhZK0fuMv6Muc7hdRKeNiI6su2S-Z5MSNSVpwY4Vw2xOuAA6ZDzsnZFGNwUf9pCCocjil5uHy2N7LC1MT06LgZolOoUQ6bISzLkCAxQlyaEjjrZQoiT4v-Qf0mmpawYR0X2n1AsFFfV3ngj-rZQO1hkEu8chQHTKfiHI3N-u3HI0He7s8r_fCNVRioKjtWNJA6JliqiIwG3hnEjgj11AknZY8irFBxtuWe2X9KW6P85EFbXSk26DyJOxqAh2oMf-oy471z31Y8ztriy4YWI2aKvm2jXU0rAhgWBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGJg1UfalFEvJZVbCmYG-tVVHIgUN-droRB8z4c1XmawlKo_JZQplCPcdIoZwt9mL1l8kDfGgyoEwfTuWRw_t65m4h9qEO7SwaJcHYRUn3alHKB2V9rtg5vaGThYjnEU1OyezXdCoT8K1jNZjFPHQzfjef1rz4o3Gu3KyxUH-iPPrjZAwNzjURwQHIJMtaVHtQEOYJP9mvwC6FYenoPEDZ-sNYZdn0F6Qx2RJ6n-GmqyZrxKhGfop7M95wfhrMnqMigGxx_RDi5ddfj7tb0jmGlXJkqKOW1hfOlf8KBk8WY2dOCtLtXpPH7jPWkEs8eFEdmgwvCmKYN5un8PWowfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmY7_fZsvme0EFDLPsnxRdGMAnrAYrqfp3oAas2HrlUhfk08n4vQipQzEUDqIk65BruAelrWYTXUsYqp1Agpe87fMULxMrRe7xZLBP11sJfTydPVGOHpn7ljQDG6_TscAPmLq78Deb3y8xApNMWaCVqvpDiMUqg92uTKsQygR-zLy6ZW56ZwRvAITlh5-KT_U8NFU_dixrt7p2MYWE2bU60ShGcrXLiU52GMpkoN0sdFGNH0tYTdDQGSCUazWF3g2fW6Nqjdr3J_3x1_BFcQWhb6BX_vPvPWONLI6suZw33wPgRQxEk2FgewwXrpA0uxr5Mde6tck0UwHCIbLKPdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTlgdtk1ub9ksjbzot8QLRQ3gwtsEcVBI0N8tpJ8v90jwsx7CrnxseaLHXKAk7bphsjn1bZybgahkScqak0GVA2UQScZhVkOJTOyPVkMBjyVLHm56nOQh_UdiwX8xVM9SEqHu0HKRF-Wzvq607BDPS4ve_WHgWG0BxJEAp9lfbFHnPUdiGG5fy33nqcf1YCxoaZ0s0Lub_QgX28WkwQUrrgX3iWduPAwMNDcf0gtfGrEwMsw5ksfE9oAnKzwg5dl_Dv73wupohlPHThy6bDLONyQyvv7UtXsoyQxO5tlw0BTX5YZKjvOF0R5qAhFnFZA-nBSm4zAPoh74c2paY-XIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
صفوف متراکم مردم عزادار ایران در اقامه نماز بر پیکر مطهر امام مجاهد شهید
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/447011" target="_blank">📅 08:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447010">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دعوت بزرگان، علما و نخبگان طوایف سیستان‌وبلوچستان برای حضور در مراسم تشییع رهبر شهید
🔹
سران، بزرگان، علما و نخبگان طوایف استان سیستان‌وبلوچستان با صدور بیانیه‌ای، از عموم ملت ایران، به‌ویژه مردم مؤمن، غیور و وفادار استان سیستان‌وبلوچستان، دعوت کردند تا با حضوری گسترده، باشکوه و دشمن‌شکن در مراسم تشییع پیکر مطهر رهبر شهید، شرکت کنند.
🔹
در این بیانیه آمده است: حضور پرشور مردم در این مراسم، تجدید میثاق با آرمان‌های اسلام، انقلاب، شهدا و ارزش‌های والای ملی است و بار دیگر نشان خواهد داد که ملت بزرگ ایران در پاسداری از عزت، استقلال، امنیت و وحدت کشور، همواره استوار، یکپارچه و پایدار ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/447010" target="_blank">📅 08:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f213ed4e.mp4?token=VBmeqO_wLnSGpJfgoJqT0lSLrTmOrdwfy9k4O4q0MEjT3PFCiBE6gLF9G0_lAYUaHFZiq2Q0ZeHFBMvvHt3mGeKsAOPKZMXnWb79oDV95ibJ47gM85mHlci524vYg8k7wL-JhhP5uPXjgqwetcSgZContaJ6sqVMmkfVImLx9y1lSSLGa7oAsL59WcZWppNNQZyUn-G1sD-1og70RKLzp_SAdL-_elr7R5L82OlQYuroTTGJS6KGZGVm9j70S6GfWKqCE44RM5hA4zU8lDemwvSSNE2L6hs9SKoBiLbTMg4f3AezOeOWedH8C6gRK-b2BKpyb6P9mfW5nIJUqI-TeVvr0V5_7KS0DT8huHVHZCPojMk2v8la1ToztAZ2RWn94BHvK633v4KY5Z4DAkAnPGXPofsAnq4thmZxi7I2laYDTymtgV774CjpFljN0009Qxw0ZNmxywF0h3INaCRPfQ80vodXF7gLq4l-Yew2mEA9oX_K4D_o0GgpD8H6RJJTiUTZRjMlYcGrlNVzBLxgCOjVnK7AeJqxTMrEpXIwr6Q_OV_Z72dOb7CWF74nt9hD2pzMAs6ksF6GTInEoAuC55dYBYJklQOJj4MCh5gfsv5R8qqJwpKDBCVkvNHIZOquBmuiAsKn92KBuWUaPDUcklrzGmKgSV5WHxquyG4q-Hs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f213ed4e.mp4?token=VBmeqO_wLnSGpJfgoJqT0lSLrTmOrdwfy9k4O4q0MEjT3PFCiBE6gLF9G0_lAYUaHFZiq2Q0ZeHFBMvvHt3mGeKsAOPKZMXnWb79oDV95ibJ47gM85mHlci524vYg8k7wL-JhhP5uPXjgqwetcSgZContaJ6sqVMmkfVImLx9y1lSSLGa7oAsL59WcZWppNNQZyUn-G1sD-1og70RKLzp_SAdL-_elr7R5L82OlQYuroTTGJS6KGZGVm9j70S6GfWKqCE44RM5hA4zU8lDemwvSSNE2L6hs9SKoBiLbTMg4f3AezOeOWedH8C6gRK-b2BKpyb6P9mfW5nIJUqI-TeVvr0V5_7KS0DT8huHVHZCPojMk2v8la1ToztAZ2RWn94BHvK633v4KY5Z4DAkAnPGXPofsAnq4thmZxi7I2laYDTymtgV774CjpFljN0009Qxw0ZNmxywF0h3INaCRPfQ80vodXF7gLq4l-Yew2mEA9oX_K4D_o0GgpD8H6RJJTiUTZRjMlYcGrlNVzBLxgCOjVnK7AeJqxTMrEpXIwr6Q_OV_Z72dOb7CWF74nt9hD2pzMAs6ksF6GTInEoAuC55dYBYJklQOJj4MCh5gfsv5R8qqJwpKDBCVkvNHIZOquBmuiAsKn92KBuWUaPDUcklrzGmKgSV5WHxquyG4q-Hs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای مردم عزادار در مصلای امام خمینی(ره) پس از اقامه نماز بر پیکر مطهر امام مجاهد شهید و شهدای خانواده ایشان.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/447009" target="_blank">📅 08:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12294cf9ee.mp4?token=oLg_ie1IgU0gda4GOsvylPxg0-zZrGKJkpzzdiXkYoLuZVE2e3Fx01TyizkK-ltK7M9aAZk7I_qbvFb70FG0Xwint1Xzjn577a2CZXqAgQXTy0BRnCWZFaOOBxIjzHI5A5duLysphL7pcL2V4pgU5H3aMJPU7y6q0DCTuVMWseDhp0OABJoizJnd3GT_FJGS6irDdbYejkKM-jma84mYQRkD_e5Y-P7QB_9RWWg6U2LfWepn9c5GI3QaFGAibl0a1_YL82ymwBISi4s7kAe71F41ibJzgw8lpI4-O-z7W5-F9YCEjrTdS3FzmGa_FZlctVsANouM6M7VDY9x5-dq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12294cf9ee.mp4?token=oLg_ie1IgU0gda4GOsvylPxg0-zZrGKJkpzzdiXkYoLuZVE2e3Fx01TyizkK-ltK7M9aAZk7I_qbvFb70FG0Xwint1Xzjn577a2CZXqAgQXTy0BRnCWZFaOOBxIjzHI5A5duLysphL7pcL2V4pgU5H3aMJPU7y6q0DCTuVMWseDhp0OABJoizJnd3GT_FJGS6irDdbYejkKM-jma84mYQRkD_e5Y-P7QB_9RWWg6U2LfWepn9c5GI3QaFGAibl0a1_YL82ymwBISi4s7kAe71F41ibJzgw8lpI4-O-z7W5-F9YCEjrTdS3FzmGa_FZlctVsANouM6M7VDY9x5-dq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر شهیده سیده بشری حسینی خامنه‌ای، شهید مصباح‌الهدی باقری و شهید زهرا حدادعادل  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/447007" target="_blank">📅 08:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa93eee7a.mp4?token=VoPTGRmNe90EfPhGkMV7Er-R23htWXM-a4CYlN6mzjLQzojGhANIf30eFZe42Yq_WVxoWsgkPx3pdhkGHXsCVl-nAkV2KWPtGwh1OivEJ4ApjxeE1VO-EQtY4Z5iCgzGn_-JVo-6qSW-3ZAsFWQPfjmKhv4LbHsbi6LRtyUWHETb0o84xQG_bAXc1_giiIxSZmyA2pXhCpraeW-zQWqGZureBGRKCQH-uOy2qdcvGjASrmTix7Mbc4wEY_Yj9ecSpEEAads3vMw-AYGyKLoy32uGLXjBZGgLGvduAtVgEgoboYuz8pKNKhuU_mgMKXPIsbTk09YwN9uDGfiY5WTRWYCRPdxPK1odUMZmULvPHRBuOrmAlpJIWqz3yIg1Pr__A68tUPvS1RsjhYUSAbyNMlqFkiFx5MW2M5nlZczmE0geYZlHgrdJ4jgac8JfDZk3w8m9wEfyY1nB9yMApXhr7jf8GzZxxgUIn1NWi0y5c6Ij4rxHjz7tnRrrabkWsbeUJTEvzONQbAxIOcXjAIsx4xiK0qMETKdPJEnVCasHPokwQPFydh-12qT81-4oE9A1Xte_TlKr4scrw6ZdGfa-oZQbfjYcOEWbKe7OU0jTTRCJ7tw2BWX9Z0bA-iNN76EClYBUwiYguuSQvscpKwFd-IKofBfr8ZjWunJ7M-xTr78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa93eee7a.mp4?token=VoPTGRmNe90EfPhGkMV7Er-R23htWXM-a4CYlN6mzjLQzojGhANIf30eFZe42Yq_WVxoWsgkPx3pdhkGHXsCVl-nAkV2KWPtGwh1OivEJ4ApjxeE1VO-EQtY4Z5iCgzGn_-JVo-6qSW-3ZAsFWQPfjmKhv4LbHsbi6LRtyUWHETb0o84xQG_bAXc1_giiIxSZmyA2pXhCpraeW-zQWqGZureBGRKCQH-uOy2qdcvGjASrmTix7Mbc4wEY_Yj9ecSpEEAads3vMw-AYGyKLoy32uGLXjBZGgLGvduAtVgEgoboYuz8pKNKhuU_mgMKXPIsbTk09YwN9uDGfiY5WTRWYCRPdxPK1odUMZmULvPHRBuOrmAlpJIWqz3yIg1Pr__A68tUPvS1RsjhYUSAbyNMlqFkiFx5MW2M5nlZczmE0geYZlHgrdJ4jgac8JfDZk3w8m9wEfyY1nB9yMApXhr7jf8GzZxxgUIn1NWi0y5c6Ij4rxHjz7tnRrrabkWsbeUJTEvzONQbAxIOcXjAIsx4xiK0qMETKdPJEnVCasHPokwQPFydh-12qT81-4oE9A1Xte_TlKr4scrw6ZdGfa-oZQbfjYcOEWbKe7OU0jTTRCJ7tw2BWX9Z0bA-iNN76EClYBUwiYguuSQvscpKwFd-IKofBfr8ZjWunJ7M-xTr78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر امام مجاهد شهید حضرت آیت‌الله العظمی سیّدعلی خامنه‌ای توسط آیت‌الله سبحانی  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/447006" target="_blank">📅 08:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=boV4g0yvxoOHPgWn7x1oUUPG-zT2qICULO-BrDX0BHeETEFUlMtuYScCUlLPk57wtNT07Q1O5_Tlc-DkMBlKsXmhU4M4iAyr7I-tS9S9CbzGlO7igK3MecK0-7FlpKbiY8eDYnie8WY67hl3FrzqZhyytYR9EdrkmGVonP0TN33a7OG36T3bKKe0chBgsC5Y9eOf8sUqM-o2M4IBG8IF0QuIHxrHKvLLerTbb9hnnXUCtwUNZN3tQZjDEhlZhwAe5x4Xe0HUqd_uFrnlOQVM0ht88krJG664dB07Yk0-3nIQGn12jFEcNUY9G46My_rKzXWvc2Rc8ekgcGHN_HlzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=boV4g0yvxoOHPgWn7x1oUUPG-zT2qICULO-BrDX0BHeETEFUlMtuYScCUlLPk57wtNT07Q1O5_Tlc-DkMBlKsXmhU4M4iAyr7I-tS9S9CbzGlO7igK3MecK0-7FlpKbiY8eDYnie8WY67hl3FrzqZhyytYR9EdrkmGVonP0TN33a7OG36T3bKKe0chBgsC5Y9eOf8sUqM-o2M4IBG8IF0QuIHxrHKvLLerTbb9hnnXUCtwUNZN3tQZjDEhlZhwAe5x4Xe0HUqd_uFrnlOQVM0ht88krJG664dB07Yk0-3nIQGn12jFEcNUY9G46My_rKzXWvc2Rc8ekgcGHN_HlzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در مصلی: یا حجت‌ابن‌الحسن تسلیت تسلیت
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/447005" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca699d47.mp4?token=CBeEi6wdDiF-_yMrN3NzvL4qLLzeIFf34OYbhZgHble3-LBkVzdL5el0OQZRL_8GxH-eDLatnkjHeAHWFBdzzXEm-LAkSBqo0V3Xu_Ly30EGQjRp3Qubj2pHrBHiZ71_ES-QrJY28eDRO6DXXGTBWKuY9tI3b9We9QEr_am8aQsYxeZ9KBitS1FDgI_EnSdrKZNMCrTSpD_pQPvJgvvhvRky_rNGaqOuCvocWirxmbcxJnoRNKTfAcpl5OrRZz6Pmf3drPpMymQogqhE8tXzj6mMKPl8t5Lq7VRX36zv53H6rxAeF5gcBDhwVVNwsa5E_v06Y8JjHCYzKiOTYBTg-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca699d47.mp4?token=CBeEi6wdDiF-_yMrN3NzvL4qLLzeIFf34OYbhZgHble3-LBkVzdL5el0OQZRL_8GxH-eDLatnkjHeAHWFBdzzXEm-LAkSBqo0V3Xu_Ly30EGQjRp3Qubj2pHrBHiZ71_ES-QrJY28eDRO6DXXGTBWKuY9tI3b9We9QEr_am8aQsYxeZ9KBitS1FDgI_EnSdrKZNMCrTSpD_pQPvJgvvhvRky_rNGaqOuCvocWirxmbcxJnoRNKTfAcpl5OrRZz6Pmf3drPpMymQogqhE8tXzj6mMKPl8t5Lq7VRX36zv53H6rxAeF5gcBDhwVVNwsa5E_v06Y8JjHCYzKiOTYBTg-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللهم انا لا نعلم منه الا خیرا...  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/447004" target="_blank">📅 08:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447003">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8976e23934.mp4?token=kfcnRNIZfG42Tlm8sGdyaw-N5cTI-lIGGgKg-zBczCRLrIm5O_yRkUxPXw7lxz4dyWTR9zaxSLgILpU_tfIkNyROlfmMe6yoUYrNQMqIuPYMBsBWprHsEV4hWWv_1OGwMqMRmg6DcIthO3H_0jc7M-CBNqX8NuhnMVw7-OiuP4-3kVTSyQ3MmnjbTGNdbXMIgtqic2Dqc9xyJ6x1BvCluAOI9B7cm0cdyACgeq95NmqWpv95x1hlpxC9sDYTy141TCkXOXGjWv8jEJ7pi0fE4ptm0pLqKvJsQlF0hoA9ckG7OG77VLzSomb2kS7ww5I0AEakjoW0WCfTrqjfaRvMSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8976e23934.mp4?token=kfcnRNIZfG42Tlm8sGdyaw-N5cTI-lIGGgKg-zBczCRLrIm5O_yRkUxPXw7lxz4dyWTR9zaxSLgILpU_tfIkNyROlfmMe6yoUYrNQMqIuPYMBsBWprHsEV4hWWv_1OGwMqMRmg6DcIthO3H_0jc7M-CBNqX8NuhnMVw7-OiuP4-3kVTSyQ3MmnjbTGNdbXMIgtqic2Dqc9xyJ6x1BvCluAOI9B7cm0cdyACgeq95NmqWpv95x1hlpxC9sDYTy141TCkXOXGjWv8jEJ7pi0fE4ptm0pLqKvJsQlF0hoA9ckG7OG77VLzSomb2kS7ww5I0AEakjoW0WCfTrqjfaRvMSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللهم انا لا نعلم منه الا خیرا...
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/447003" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447002">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=lTcmkAeA4xXOgDovhTQDEWt1uUVwcYPraUhFXDFDFYnWMt_hc3VpGeV6vcgMh2TrdgdGVqtWLMA81CdviMtaR9SXbOncDbn_ETmjbUyvealK0orpepE3rhRb9P2FqrIQ7ERHNWHPIjD9InLX--YqC5GL0k4PPqB2cVX4Diaq6iMFtsBJS-a6xcdgBxhAeVNVjctps_1FFa8lJ5mFiwOkeXWqeTaR9zGUS1z9q95MkPldBB7neXyHmJyUHaGNluXhJG3YNxwXsk93sE1WvDMdDIIoZrrDsHisQ8ZBQjSyV8xT25OD8dvNqPi3oFjctFFh5Ou81UHxN4sAoVpRci1DfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=lTcmkAeA4xXOgDovhTQDEWt1uUVwcYPraUhFXDFDFYnWMt_hc3VpGeV6vcgMh2TrdgdGVqtWLMA81CdviMtaR9SXbOncDbn_ETmjbUyvealK0orpepE3rhRb9P2FqrIQ7ERHNWHPIjD9InLX--YqC5GL0k4PPqB2cVX4Diaq6iMFtsBJS-a6xcdgBxhAeVNVjctps_1FFa8lJ5mFiwOkeXWqeTaR9zGUS1z9q95MkPldBB7neXyHmJyUHaGNluXhJG3YNxwXsk93sE1WvDMdDIIoZrrDsHisQ8ZBQjSyV8xT25OD8dvNqPi3oFjctFFh5Ou81UHxN4sAoVpRci1DfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در مصلی جای سوزن‌انداختن نیست
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/447002" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alvYZI984Rbsd-PBsQi44iO3DPyNxPEyy3aiw4Ite5Uvj2NT7SzyHgZu_YVwBMuo_Gf_VbqY9IcLxP364JzUmYkIS3ggv9IoK7Js4CVMG27VOjuF2UeBJxViuS0FVIjl3Yiufqgd_nAa9Hje9_v-Y6AdyqmGcImIRf3EdFFSs6ZQXI0zgxqpgXN6d-eB2Iles_YtXc8u-lsdg0k7fVRR4QywWegfdEDBf0oXtRZHTnL6FOlQZsa78TVX1hiEAQbbIM8-Nd-upWZVaFMSuIAw3fQ9VB3AebRHuzoRrqETGhbCJlkp3MBV81PNFNjpQk5dPcZ89LGdJsDk5fGQwFD6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی از لحظهٔ آغاز اقامهٔ نماز بر پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/447001" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed5ec1b26.mp4?token=lLEek0Ej5zjDJ0cc4RoZ17E4hFXYXygsPBaVxKuv-fN43jPAX1aVU3SQsxc5UV38Tnpa-_BTNwHFPVA8AGM6goE_lqsLVoeRfS0d_If02qM4vRCTAQ6Q7SFMBzSTrH1Dbw9v8QIOUf-sWTYoa5CmJgBhOJz3hlKEVC6vyQgwP-gEhUY9txOGZHmws1qk0BOYQEUuj5DM4IHYXVWVxL8lHj_B_04IPcmiruAnbY-FGx5ULkYuoqHHyNlpc5QIb5CrHhqOZvQIAef80AsH65pPCeNRTMBygR9fMWt5gn0yVfP3M43iYotVZRM_cyQsU4uC_GNYYjakPAmOwiPhJbK_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed5ec1b26.mp4?token=lLEek0Ej5zjDJ0cc4RoZ17E4hFXYXygsPBaVxKuv-fN43jPAX1aVU3SQsxc5UV38Tnpa-_BTNwHFPVA8AGM6goE_lqsLVoeRfS0d_If02qM4vRCTAQ6Q7SFMBzSTrH1Dbw9v8QIOUf-sWTYoa5CmJgBhOJz3hlKEVC6vyQgwP-gEhUY9txOGZHmws1qk0BOYQEUuj5DM4IHYXVWVxL8lHj_B_04IPcmiruAnbY-FGx5ULkYuoqHHyNlpc5QIb5CrHhqOZvQIAef80AsH65pPCeNRTMBygR9fMWt5gn0yVfP3M43iYotVZRM_cyQsU4uC_GNYYjakPAmOwiPhJbK_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های مردم هنگام ورود پیکر رهبر شهید به مصلی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447000" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84f846d42.mp4?token=NkB27sZ8Ze0unL6J0OBk-u_4bgOYz7vGsqa6C8EqSgjTWxLfkV9JWcCRch1mu99JYLrUbJs_BOTUc0l4UxTT0z1ywtrqh5xCc8IwpE1wCftd7Y_J3jtw6bE7Qr1SsmZlwzcI4plrXTsnrz8gvulwhWYGtdMhH--cXmOJFlomEdJZU4yOr4VIW4rIcZiHy3tEPuvGzLk1rX83nuTHVy7bBjLoMgWi2JfFLWK9Z6pxZoC2_mo7Tu43nG9td48jiimbq1XXI8NlsMsAQ064eaX0kyPbR2f_TWXOicEhS8aRsLNMfio-HjwwZNTnh5bol-C44ag1B9O7Ulr_i20Goy7Wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84f846d42.mp4?token=NkB27sZ8Ze0unL6J0OBk-u_4bgOYz7vGsqa6C8EqSgjTWxLfkV9JWcCRch1mu99JYLrUbJs_BOTUc0l4UxTT0z1ywtrqh5xCc8IwpE1wCftd7Y_J3jtw6bE7Qr1SsmZlwzcI4plrXTsnrz8gvulwhWYGtdMhH--cXmOJFlomEdJZU4yOr4VIW4rIcZiHy3tEPuvGzLk1rX83nuTHVy7bBjLoMgWi2JfFLWK9Z6pxZoC2_mo7Tu43nG9td48jiimbq1XXI8NlsMsAQ064eaX0kyPbR2f_TWXOicEhS8aRsLNMfio-HjwwZNTnh5bol-C44ag1B9O7Ulr_i20Goy7Wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کجا میخوای بری، چرا منو نمیبری؟
◾️
لحظاتی از روضه‌خوانی محمود کریمی در مصلای امام خمینی(ره) تهران، دقایقی پیش از اقامه نماز بر پیکر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/446999" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe631818e.mp4?token=ZEl-VbvupAjKMLZ-SC0D1cf-Fz0MlPkvB-y_KxUu6mjzOIAd4p4MUpylmyCyNyK5UXlFlQY12PsJZBnEZE4EPhUOytVj6mUWEhAuffvhq9Gq5rcOv1Whx4GqKK8KXcWnfgi1zdGWaDhGMr9251uAABpiT-roLgnUY5rit7t0PyApgogG0z8I8sG8kw7OvFuNXH79P682QOfURABcE0RmCrRpyZ6cPkt5scR9j5oe_oaKJ8mfpVo1tLpqIfC3ZxxfBFVftDEgn23pshkzv_AKQgSb-cpycQQ_349GHGl0mcXSwfYA0_AElNiY6QvdTLiY6Kfd5EZvw9qj8o95NLG6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe631818e.mp4?token=ZEl-VbvupAjKMLZ-SC0D1cf-Fz0MlPkvB-y_KxUu6mjzOIAd4p4MUpylmyCyNyK5UXlFlQY12PsJZBnEZE4EPhUOytVj6mUWEhAuffvhq9Gq5rcOv1Whx4GqKK8KXcWnfgi1zdGWaDhGMr9251uAABpiT-roLgnUY5rit7t0PyApgogG0z8I8sG8kw7OvFuNXH79P682QOfURABcE0RmCrRpyZ6cPkt5scR9j5oe_oaKJ8mfpVo1tLpqIfC3ZxxfBFVftDEgn23pshkzv_AKQgSb-cpycQQ_349GHGl0mcXSwfYA0_AElNiY6QvdTLiY6Kfd5EZvw9qj8o95NLG6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
◾️
نوحه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/446997" target="_blank">📅 07:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00316b575.mp4?token=ATWgPKrq4z4Dd9z8f19d47TSTMpfawOSAwWu56XmTqnL9fA-1UuP6fBjG2jyDhy2BlFxfZLbLN0HjEJq5EjRw2nR9s0-jqyH4VKIYd7rZH5m1Y8hYdURzCTs2V2hgRt2pOOkAnQhro5flpcDDVh6F-QP85fWOkhIvdYyMerk-fgDhpDgQo80ecEOLasmPukjfkf_mPWDXjpGiN7KlmAf1huhaBJojXO55CK2ORKFonkZuP17BsYpFEW0kf--Cb3lT6AXJ8X7Fj4UtkI1ufjr-2-clLAe90o1WXz_KS30f6gpy9gvyteA8bxCqfaI6Gu7-HofAFM_iR055BYy1wrvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00316b575.mp4?token=ATWgPKrq4z4Dd9z8f19d47TSTMpfawOSAwWu56XmTqnL9fA-1UuP6fBjG2jyDhy2BlFxfZLbLN0HjEJq5EjRw2nR9s0-jqyH4VKIYd7rZH5m1Y8hYdURzCTs2V2hgRt2pOOkAnQhro5flpcDDVh6F-QP85fWOkhIvdYyMerk-fgDhpDgQo80ecEOLasmPukjfkf_mPWDXjpGiN7KlmAf1huhaBJojXO55CK2ORKFonkZuP17BsYpFEW0kf--Cb3lT6AXJ8X7Fj4UtkI1ufjr-2-clLAe90o1WXz_KS30f6gpy9gvyteA8bxCqfaI6Gu7-HofAFM_iR055BYy1wrvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر رهبر شهید انقلاب به مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/446996" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e63f565a.mp4?token=J1TA4kZzwQxATCouFhmlaGO2tA05k3XUgWRtlq-ZvJLJ5iwPUOqrOip8vt-pDzA9w9F6ccnA7ELCBiengSAvZzQa-q0---m8ZqyxOqaGceJrubzTyJc0xHg4Txauu7MUcN71S5utE3p6PsJy6hgPKX-MN4pwWB21Yf6TRUyIySsxKoDMungem9u9BX63sOVFZwdWobNYqhUV1c1leD1I1sNnw1-vhlWDzRwRG5vJWUvoV27I3n2L8-w_LLagJiUJFNdUEhr-9a93_2axyF5Hwdy_SeRYb29zzSHqYG3Jvcv6BLGv6owRXYAkfeGvqVJH3XU-vK3IGycMb3e6csxHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e63f565a.mp4?token=J1TA4kZzwQxATCouFhmlaGO2tA05k3XUgWRtlq-ZvJLJ5iwPUOqrOip8vt-pDzA9w9F6ccnA7ELCBiengSAvZzQa-q0---m8ZqyxOqaGceJrubzTyJc0xHg4Txauu7MUcN71S5utE3p6PsJy6hgPKX-MN4pwWB21Yf6TRUyIySsxKoDMungem9u9BX63sOVFZwdWobNYqhUV1c1leD1I1sNnw1-vhlWDzRwRG5vJWUvoV27I3n2L8-w_LLagJiUJFNdUEhr-9a93_2axyF5Hwdy_SeRYb29zzSHqYG3Jvcv6BLGv6owRXYAkfeGvqVJH3XU-vK3IGycMb3e6csxHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر نوهٔ ۱۴ ماههٔ رهبر شهید انقلاب برای اقامهٔ نماز میت به جایگاه منتقل شد
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/446995" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697da49412.mp4?token=c63jwe5FF0jX-XS1K4svbELTpAb4rteR-MvG4fK2OOE881d6X3VxeNFw3_FOP3s40mnmjKU0DUh9m8lkCQOZVpu7CjHtYJEdaZT_7NRNsmqDTR53vHoTzmi8-zg-Px1_BHYMQ0aJLvcywnCnZIqXJ-jlIXGxVMSvnY63jTRnrOFI3yI0ryAoAMCCKVDGGGIovDvZ76TIbKwOln-ykzTysORHu2Q3uZKIdXU1JwM_W_QXRqPmJBgFc9Bg6TMhGPlL2N2oVjWygv1uT1NmSTIS6j9hL7jAufNZIPA8TY7vIZYd94vbX304Q3ARfi4UEI-1-gr9c-7e7iQsndy5SAZq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697da49412.mp4?token=c63jwe5FF0jX-XS1K4svbELTpAb4rteR-MvG4fK2OOE881d6X3VxeNFw3_FOP3s40mnmjKU0DUh9m8lkCQOZVpu7CjHtYJEdaZT_7NRNsmqDTR53vHoTzmi8-zg-Px1_BHYMQ0aJLvcywnCnZIqXJ-jlIXGxVMSvnY63jTRnrOFI3yI0ryAoAMCCKVDGGGIovDvZ76TIbKwOln-ykzTysORHu2Q3uZKIdXU1JwM_W_QXRqPmJBgFc9Bg6TMhGPlL2N2oVjWygv1uT1NmSTIS6j9hL7jAufNZIPA8TY7vIZYd94vbX304Q3ARfi4UEI-1-gr9c-7e7iQsndy5SAZq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزندان رهبر شهید در مصلی  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446994" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTs_Vim1-0PoLim5cZ60uTJ99WqzFb_Z4GIa7dWb4YMKWHGHiYJhKjJFHVanIYvG688Q1EAzqgyUL-BUm5jM123eQmSb7JlD7gDsK_nw7sa7rHzyS7Eu5RpHO45D9IvY0YnxUyBSTveuzqACMefUdLFreSo7afk5fkJUShfC3oBfJa5fjyZRxhskTe3GD2lbmkzpp255nDhM2EiIfxq5TfOkEFOj8VmdiVFEsVsxUqwo5B4WVnngSSU_ZdOjuyfHRub5uR1EaEtd3BSICIvwVKnHBO4yp0NgG0CmVQvTBwFcsuiiYzKuftM-uLDOL5NkpA6KgK0uYXD-Xh0tSxqC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصلای تهران پر شد؛ حضور نمازگزاران در خیابان اطراف
◾️
مصلای امام خمینی مملو از جمعیت شد و صفوف نمازگزاران در خیابان‌های منتهی به مصلای تهران تشکیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/446993" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517fcd141d.mp4?token=jB51dPCj13yj95z7I2gFYt12K6g8poAm69eO7MNhwjdYGam-dg1vB4Z3UnGsxfkTNanVgwfRJVzHo4qUtooCtiZzVKLBp2zRmvKOlTYdL2kY8X7PZuZ911dGrBCFri-_aF4r4sXufrLyzkcsYzU5i-UmGtPTwiOdS28sL6UXcqqUbdRhLWU8dW718RFo3DSsxaQbKtFbWd_YHJvPIoHY8kPEOSvaHE7pa4laDdcR8xvq9YwAD1otXSU4pamSAebTJTPba1cnhhNTYN-06oNssLuqh1E6SoDEr6u-K6e4JbPBSevoWWMGNEiQUcijiKigbgvZ8H4K1fV_2coGX-nGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517fcd141d.mp4?token=jB51dPCj13yj95z7I2gFYt12K6g8poAm69eO7MNhwjdYGam-dg1vB4Z3UnGsxfkTNanVgwfRJVzHo4qUtooCtiZzVKLBp2zRmvKOlTYdL2kY8X7PZuZ911dGrBCFri-_aF4r4sXufrLyzkcsYzU5i-UmGtPTwiOdS28sL6UXcqqUbdRhLWU8dW718RFo3DSsxaQbKtFbWd_YHJvPIoHY8kPEOSvaHE7pa4laDdcR8xvq9YwAD1otXSU4pamSAebTJTPba1cnhhNTYN-06oNssLuqh1E6SoDEr6u-K6e4JbPBSevoWWMGNEiQUcijiKigbgvZ8H4K1fV_2coGX-nGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور روسای قوا در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/446992" target="_blank">📅 07:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f4055cd9.mp4?token=W1xtAmC-yv7iHQ9nAl01hiHq0MpUocGBzpP6_87j30NLL8AVV594TS-y-9fYCFj5epjWdkbNC0YBXMTTQrwuOdkkOL-7IW8kJTCp6S9fc3yVh1KGxx3PE1U-n1ZkZvZpSZFSz_B9jm9w3uFMVdyGxZjS8YqjYeE10tTesIZsTJ8DILX4z3cRAPg2lQ6AvV9bRCvjUCZWLc0LrTwJgbDV_Daw2dGF2ZRQYKGJwhEsclHabqdbnpxtYUhjOw4D4dIB7OtFK6VW4BUr7SS67IWgMRrOHOzF6UID-LvfYVx-sV0XpM81VWY9Skrl9CVTOyJSupjs0wYnsBvc79iDosimUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f4055cd9.mp4?token=W1xtAmC-yv7iHQ9nAl01hiHq0MpUocGBzpP6_87j30NLL8AVV594TS-y-9fYCFj5epjWdkbNC0YBXMTTQrwuOdkkOL-7IW8kJTCp6S9fc3yVh1KGxx3PE1U-n1ZkZvZpSZFSz_B9jm9w3uFMVdyGxZjS8YqjYeE10tTesIZsTJ8DILX4z3cRAPg2lQ6AvV9bRCvjUCZWLc0LrTwJgbDV_Daw2dGF2ZRQYKGJwhEsclHabqdbnpxtYUhjOw4D4dIB7OtFK6VW4BUr7SS67IWgMRrOHOzF6UID-LvfYVx-sV0XpM81VWY9Skrl9CVTOyJSupjs0wYnsBvc79iDosimUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزندان رهبر شهید در مصلی
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/446991" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8092655245.mp4?token=L9Ac2ZFUfJGpt99MzuX4_CUrhHW-uu6pIUyquwJl6khg8IiN9ThuOAirxSGoGv19nd-0q96RdKOJeZWEDSNuJ15-wkyxtF1bTxR2gMUTSErLqshergVTFPSMTV1FzCInvQBjNMX7gSIC9v0N9itMcgb5du3qv-rZHSPB5gfY7nSqO4yaagGKyKhRH7qb6iLH37ArAKM6Zzve3K8QVFQnaFmQwuMI1dHnUJg9PTzDCAf_ppMDk1IdMkLEm0wk51x_8kpZJ4MjG4ipwTyesGj4-Z7yRlml37LSfq0ybKwi321PKIvMpv5r7zJhfHu6qclqozanmJG5lQ8WVmtQblpjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8092655245.mp4?token=L9Ac2ZFUfJGpt99MzuX4_CUrhHW-uu6pIUyquwJl6khg8IiN9ThuOAirxSGoGv19nd-0q96RdKOJeZWEDSNuJ15-wkyxtF1bTxR2gMUTSErLqshergVTFPSMTV1FzCInvQBjNMX7gSIC9v0N9itMcgb5du3qv-rZHSPB5gfY7nSqO4yaagGKyKhRH7qb6iLH37ArAKM6Zzve3K8QVFQnaFmQwuMI1dHnUJg9PTzDCAf_ppMDk1IdMkLEm0wk51x_8kpZJ4MjG4ipwTyesGj4-Z7yRlml37LSfq0ybKwi321PKIvMpv5r7zJhfHu6qclqozanmJG5lQ8WVmtQblpjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در خیابان شهید بهشتی همچنان به‌سمت مصلی تهران حرکت می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/446990" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb3942fd5.mp4?token=krqf3bEPTCiu54y0PfG-ceAVlYEnuBf6wXHatO6ciadltXMXhbTLYtS9BMBFTZe6MBniuvrIh2H1hnIloAFgWiwuxg7cPa39AYg28NAWesTSw_clfxlrFj3zIYh7RKd47D1oFTWMiceVb0a4YjkrK8l_vUUy6bzdNQizdJNjtr99hnKnBdY9fgRBrLtoDFsJQ0YbYpJ5FfcZ2jvjkekb_95Sbm0TgOt7vDLHmAky67_A0X5XQStaMa4SKZOJ2pZxHG0mr8xwe09ESEHEGWuvknnjYdXVOuSve8lEcWeRTzuCj-qloZGgnJEObzRRSJAfLeXCkNK7D6DSAXrtZCndtB7O3LbIO9HFTtuWXrHR0T03SN9i3eDGyWUJK-60sIZHq2Fg5zkmfJyTx6HGVW0hXFXe34K_SnlNFTkTnhIrPEwczdBwj37TG9THYepF4DspNv-k5De1ii2va7BM-5mc0Seej8T7xeUqjTVB3IDciUgIdNv1JjfW6EkBml_s8bTk6JY2ffisrKe4W6Bcaf6rHkYsUCe3QKamBAXhBPKyItLRh6J3jULtmZsmVjblHLnxtvRHasQRn4wfQlkj3k2NOobzIs9heBAZ7FZiqmu_wV7pzu6qyDLVBStQ0sy3iTz6kvvcnADju7j5AEhAqMV5JpLu3df8W2eVP2imPLYZsTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb3942fd5.mp4?token=krqf3bEPTCiu54y0PfG-ceAVlYEnuBf6wXHatO6ciadltXMXhbTLYtS9BMBFTZe6MBniuvrIh2H1hnIloAFgWiwuxg7cPa39AYg28NAWesTSw_clfxlrFj3zIYh7RKd47D1oFTWMiceVb0a4YjkrK8l_vUUy6bzdNQizdJNjtr99hnKnBdY9fgRBrLtoDFsJQ0YbYpJ5FfcZ2jvjkekb_95Sbm0TgOt7vDLHmAky67_A0X5XQStaMa4SKZOJ2pZxHG0mr8xwe09ESEHEGWuvknnjYdXVOuSve8lEcWeRTzuCj-qloZGgnJEObzRRSJAfLeXCkNK7D6DSAXrtZCndtB7O3LbIO9HFTtuWXrHR0T03SN9i3eDGyWUJK-60sIZHq2Fg5zkmfJyTx6HGVW0hXFXe34K_SnlNFTkTnhIrPEwczdBwj37TG9THYepF4DspNv-k5De1ii2va7BM-5mc0Seej8T7xeUqjTVB3IDciUgIdNv1JjfW6EkBml_s8bTk6JY2ffisrKe4W6Bcaf6rHkYsUCe3QKamBAXhBPKyItLRh6J3jULtmZsmVjblHLnxtvRHasQRn4wfQlkj3k2NOobzIs9heBAZ7FZiqmu_wV7pzu6qyDLVBStQ0sy3iTz6kvvcnADju7j5AEhAqMV5JpLu3df8W2eVP2imPLYZsTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیده و ندیده راهش را ادامه می‌دهند
🔹
مردمی که توفیق دیدار رهبر شهید را هم نداشتند جوری از او حرف می‌زنند انگار همین امروز امام خود را دیده‌ و رجزهایش را تکرار می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/446989" target="_blank">📅 07:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqIo7Hs9bzrLphP0bfEECnNnnGFfR_Hg99hZhetMbAunmTsj0QbgbwT4WRjy8JwWdblIWzXxY7didPhInaUfx8nq2hjsTD8CkTy3HF5wS1vPyaMwvBAfCSTn7mjtR35_FU8ocsIdRi1Y2kW9lQqpsYRYvlht2px_M84yHtLLrRTf3SnogtIEO4yKBpswDZSTk7q-FOf9Xb5_TQMrmWDeTwAdnyR9l7JToLe_y3-zY8Q6TgkD5ZQGCrqWkUxN9-JxpzBf3C5EszVZq5RqXLcHZss29cz5sKBW-SxtVWGSwFxAxwtt7dOZq2xG8QC8v2CHU3aIB55XrdnMJXKiARs9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مصلی دقایقی پیش از آغاز نماز مملو از جمعیت است
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/446987" target="_blank">📅 07:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99751f7c6c.mp4?token=nX0vpuPx4SF74IehTCVdX2BYvHThD7vZkXXaZTs3mXInfqnD0LXOSOQoQ8i_o_p-5HndBK-I2zli8b02T-97tSvyjipO0r3b5d7Nr4W7ITS_LCnI2_ZHaxmTw6E0m-0MEUNtWyoH1WYuTvXjrykECBQbQHfSHTfWFFtFMIrPcMvNEi9r0dV6RdNr0Rtfx7n1gevsCVn02qA7UQC38J4Gp1rLny3yWOXgHiqXNgfa4zvKmCvg6d5tTz4lIjYUH-X3xdLm2q6niMqYhRWlAZW-sRjBTAuAcSrp_wSpy-7mm1FIfBzM14bkQoaY1jOZ1k-0m11J4WXMHF5U8LJmtCWIZ5mTj14sXJiw_XNtemZYBMkmVrOH3a1ZU_oiLPaVVYfzRqBXRZL9Pqz2zyY1ci5KPgBg01E6ZLBXRJV-KmiruAY0rjKz_i6STSe5n8JfaN3uo36Uh_Zr4FFy5cXeJpltJHrB4EQ1SsAjPhPIkrHzJ2pMV6qM5GnSUgqqCYVBKXWDOQdA_mV1Metr1tljLvrNsG4RCts_KSYVFCrbzN8bLztHNg9qVWunqVNgC2n_jtq3wV5pU0u4zwhjmFSS1HQlZaHrib2DI-2KNB1wPCOJ1wwnPg0F_h5Z2onf01OC6tqFnq0-xotgjT3BKr5mM9HwQaCBRO022aCrXSSJ5hrxixE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99751f7c6c.mp4?token=nX0vpuPx4SF74IehTCVdX2BYvHThD7vZkXXaZTs3mXInfqnD0LXOSOQoQ8i_o_p-5HndBK-I2zli8b02T-97tSvyjipO0r3b5d7Nr4W7ITS_LCnI2_ZHaxmTw6E0m-0MEUNtWyoH1WYuTvXjrykECBQbQHfSHTfWFFtFMIrPcMvNEi9r0dV6RdNr0Rtfx7n1gevsCVn02qA7UQC38J4Gp1rLny3yWOXgHiqXNgfa4zvKmCvg6d5tTz4lIjYUH-X3xdLm2q6niMqYhRWlAZW-sRjBTAuAcSrp_wSpy-7mm1FIfBzM14bkQoaY1jOZ1k-0m11J4WXMHF5U8LJmtCWIZ5mTj14sXJiw_XNtemZYBMkmVrOH3a1ZU_oiLPaVVYfzRqBXRZL9Pqz2zyY1ci5KPgBg01E6ZLBXRJV-KmiruAY0rjKz_i6STSe5n8JfaN3uo36Uh_Zr4FFy5cXeJpltJHrB4EQ1SsAjPhPIkrHzJ2pMV6qM5GnSUgqqCYVBKXWDOQdA_mV1Metr1tljLvrNsG4RCts_KSYVFCrbzN8bLztHNg9qVWunqVNgC2n_jtq3wV5pU0u4zwhjmFSS1HQlZaHrib2DI-2KNB1wPCOJ1wwnPg0F_h5Z2onf01OC6tqFnq0-xotgjT3BKr5mM9HwQaCBRO022aCrXSSJ5hrxixE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهدنامۀ مردم با رهبر شهید در مصلی تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446986" target="_blank">📅 07:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17352b0eac.mp4?token=ovSIAzqBnJJJ-a4fbiz1T541AnxBePkK6JVHNNBkNFGcl_L7xDDigUBwJ76zXXPoHShlpTkrEW9u_1oWbVOVtHiWbPtUMmq8p1D4mU4u4WL7Yai-5wlXQqsGYjHoxLtF-JgJY1IszmyBXJvTHyvf3HiZVgfUUBE2Nwh0C9Q3KUW_xDmlX2zmEOTQDYBlm5UbPQUgZ2AwpCn302RzfroZWDNp-eFK-JyhI5oCUJmG4kG9a979TqAfeBO5WNz3V2MXnr9aAHDGfxZwVOu3NL0Y9FQoDM7JFvswRu-0N7L_ZaKUHCIc2C9V0w7WFzZCt3fXw9RJItYb3akC-oc_DsHvTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17352b0eac.mp4?token=ovSIAzqBnJJJ-a4fbiz1T541AnxBePkK6JVHNNBkNFGcl_L7xDDigUBwJ76zXXPoHShlpTkrEW9u_1oWbVOVtHiWbPtUMmq8p1D4mU4u4WL7Yai-5wlXQqsGYjHoxLtF-JgJY1IszmyBXJvTHyvf3HiZVgfUUBE2Nwh0C9Q3KUW_xDmlX2zmEOTQDYBlm5UbPQUgZ2AwpCn302RzfroZWDNp-eFK-JyhI5oCUJmG4kG9a979TqAfeBO5WNz3V2MXnr9aAHDGfxZwVOu3NL0Y9FQoDM7JFvswRu-0N7L_ZaKUHCIc2C9V0w7WFzZCt3fXw9RJItYb3akC-oc_DsHvTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درهای شرقی مصلای امام خمینی(ره) بسته شد
🔹
جهت ورود به مصلی، زوار و نمازگزاران باید به درب‌های شمالی مراجعه کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446985" target="_blank">📅 07:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446984">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269e38a264.mp4?token=JwdcaR2Fyvl5bPwJ26uev_03kd3eIkMPWzaiyGIxbZ208cQqjxFICa2XPa-65QRqaDaI9HsM_dEI3YTFBSiqn-PjBtl79qbsmuQhf_wyLZbad3EKjeQf7NvVF08AlS72oOTXdiPCUsNAvlFYvShgcRNzbI5wsAtEkN1TSdu0WfAPQl73i0vJ-y3p4pYFPIlzmZ_k7tuso5RzJt9lKqeAibxDOUvy2PzRvMgSGYUJ_ZFbCX4tezkSQfN6VBuMiV6Tr4u_cfbubmOUldJTJhwBR9C3rq3Av00XC6vOi8sCfT-AuZTL1LmlIFk8frX-17pPu2B09f1Pvuz4uQQBFVUYCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269e38a264.mp4?token=JwdcaR2Fyvl5bPwJ26uev_03kd3eIkMPWzaiyGIxbZ208cQqjxFICa2XPa-65QRqaDaI9HsM_dEI3YTFBSiqn-PjBtl79qbsmuQhf_wyLZbad3EKjeQf7NvVF08AlS72oOTXdiPCUsNAvlFYvShgcRNzbI5wsAtEkN1TSdu0WfAPQl73i0vJ-y3p4pYFPIlzmZ_k7tuso5RzJt9lKqeAibxDOUvy2PzRvMgSGYUJ_ZFbCX4tezkSQfN6VBuMiV6Tr4u_cfbubmOUldJTJhwBR9C3rq3Av00XC6vOi8sCfT-AuZTL1LmlIFk8frX-17pPu2B09f1Pvuz4uQQBFVUYCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در مصلی با سلام نظامی سرود ملی را خواندند
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446984" target="_blank">📅 07:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446983">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51bb46df23.mp4?token=q06vavksvQNWMOcUctsMv0V80lnA-cTZ4uHxcXgn4boA6XnTgBJUalUxk6w7HSOmaKVKaiYQLEbSW8C-xuFzHcltA74AkVCNbBhvShOzpNlPeLDWQYePX5T5fpHaxZ-IF7VTlAe_VjKtX4B2R9kQcScIHfjrIuECHrezopBOv5DkQ51AW-veC2FdS5qvm_jUrMgaDtO9zaBE3agjuzTGwdMbTYkrg8Zl7bwm8k4hpEFf0gX_vvO1cLUdnZeSz80NiTkMVfTUGtKQUrmcbjAQ1KVdMkZiVkoh1WP0IjwGoDm3gAUjTKaikRXMjKL3nXwGpBG9nRCEPwNKkETtIHJJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51bb46df23.mp4?token=q06vavksvQNWMOcUctsMv0V80lnA-cTZ4uHxcXgn4boA6XnTgBJUalUxk6w7HSOmaKVKaiYQLEbSW8C-xuFzHcltA74AkVCNbBhvShOzpNlPeLDWQYePX5T5fpHaxZ-IF7VTlAe_VjKtX4B2R9kQcScIHfjrIuECHrezopBOv5DkQ51AW-veC2FdS5qvm_jUrMgaDtO9zaBE3agjuzTGwdMbTYkrg8Zl7bwm8k4hpEFf0gX_vvO1cLUdnZeSz80NiTkMVfTUGtKQUrmcbjAQ1KVdMkZiVkoh1WP0IjwGoDm3gAUjTKaikRXMjKL3nXwGpBG9nRCEPwNKkETtIHJJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درهای شرقی مصلای امام خمینی(ره) بسته شد
🔹
جهت ورود به مصلی، زوار و نمازگزاران باید به درب‌های شمالی مراجعه کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/446983" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446982">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اعزام اتوبوس به مصلی در پی ازدحام ایستگاه‌های مترو
🔹
شرکت بهره‌برداری متروی تهران: به دنبال ازدحام جمعیت در ایستگاه‌های تقاطعی امام خمینی(ره) و تئاتر شهر، از شرکت واحد اتوبوسرانی درخواست کردیم اتوبوس اعزام کند و در حال حاضر اتوبوس‌ها مسافران را به مصلی منتقل می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/446982" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe52fb9d48.mp4?token=OwddgZcn7NQBL3UluxahbteXVZ91j4vmGLa5Dqqu_WWzUS9lzkYscUg3lbh0CU41QoTA7BXEMKA2Qij-0JDzvKwy25AEGPncO4zn0fbGUGMQUfJQ8Qwdz_slBEoLq92KW2VTcUpgMezkU6awUdUgwaEXp9JxShChw-XH50B4wFBSF9kvWYnlDaPPxAYl6W7rId0Vo4cw3tZMkuxySTNrwTvy0SxpIoN83ai06TM-uTUM7235S45wJjtFcUnsrHpvX3y1--Kt_7AW8f8--oJx3PWQNtBOJZK6os2uTuWVPC0lw0pil7W7VrARK_09nXTLUJlZm95eOXITRglY7aXhmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe52fb9d48.mp4?token=OwddgZcn7NQBL3UluxahbteXVZ91j4vmGLa5Dqqu_WWzUS9lzkYscUg3lbh0CU41QoTA7BXEMKA2Qij-0JDzvKwy25AEGPncO4zn0fbGUGMQUfJQ8Qwdz_slBEoLq92KW2VTcUpgMezkU6awUdUgwaEXp9JxShChw-XH50B4wFBSF9kvWYnlDaPPxAYl6W7rId0Vo4cw3tZMkuxySTNrwTvy0SxpIoN83ai06TM-uTUM7235S45wJjtFcUnsrHpvX3y1--Kt_7AW8f8--oJx3PWQNtBOJZK6os2uTuWVPC0lw0pil7W7VrARK_09nXTLUJlZm95eOXITRglY7aXhmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
اگر چه در دل ما داغ آتشینت هست
◾️
هزار شکر که امروز جانشینت هست
◾️
چه نایبی که به نام و مرام خامنه‌ایست
◾️
هنوز رهبر ایران امام خامنه‌ایست
لحظاتی از شعرخوانی محمد رسولی در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/446981" target="_blank">📅 07:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e773e0a4e1.mp4?token=QPbSMaAySMoBZeGMHJBpfHooOVf5YVq2izybQ2m4ULnAkc2vubJ3Q3yDl1-yjVrMNz3QjNM5xfs4ksj5ggBiVpQ9MfLKZXuToTi6mGQ4h4CQVY7rZa0rBymvt2MwnI3StMWwH0cZ8sZafndUm5PDfkeObyV0ZkdoeSniUWHqQ5cuvQGVqSk90PEtq0PAf6kegmzr7AFRz97d_oG7_Hybv06FaNMMCt87KpOS06AmWCwNw_Y_SwSb-luu6AIInq4JLnJ-XkiZZC-w9jzrMjDMfMWXm6ZCGpDJMj8D8ZH2W92rOswWzCBpGKK7bYTw_jOZHZEOarur07MoF24hTPoi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e773e0a4e1.mp4?token=QPbSMaAySMoBZeGMHJBpfHooOVf5YVq2izybQ2m4ULnAkc2vubJ3Q3yDl1-yjVrMNz3QjNM5xfs4ksj5ggBiVpQ9MfLKZXuToTi6mGQ4h4CQVY7rZa0rBymvt2MwnI3StMWwH0cZ8sZafndUm5PDfkeObyV0ZkdoeSniUWHqQ5cuvQGVqSk90PEtq0PAf6kegmzr7AFRz97d_oG7_Hybv06FaNMMCt87KpOS06AmWCwNw_Y_SwSb-luu6AIInq4JLnJ-XkiZZC-w9jzrMjDMfMWXm6ZCGpDJMj8D8ZH2W92rOswWzCBpGKK7bYTw_jOZHZEOarur07MoF24hTPoi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «حیدر حیدر» مردم عزادار در مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/446980" target="_blank">📅 07:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWztocI4q2tr4VucmcP632usTaQMze3IujQjBQMSY8GEyW3ZSS2jij82HIOQZiWj0SDiOCy6WBBFluf9p0DgioWSLLEK0rc0iTieaQdKwD13CgvzapqqJnCMLDBzzaDmYovbceKhb86yXwS86TeD6CfrG4YUO7q3zpww5w9cSBqggsqoNTX2AdEjTViUYd8rQ3UXb4IgSSlf4XqSY0nnP1AWpzfm9UR-bm_0sMMBeqnNbdGn6v0LRHuZJgHAb1jpybcuTbMb3k4HPhYEtUsb32DFGCQgENP9lPyQMFJzOlYCYMIoJhE7CrZvu51j1qy7gZUIVKDED6_yvXipgNjlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
آداب و طریقۀ خواندن نماز میت بر پیکر مطهر رهبر شهید و خانوادۀ شهیدشان را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/446979" target="_blank">📅 07:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d31dd0974.mp4?token=HpR_jqAWnacwofJHGsBr9eFNam-4TkfX1Fm1B-d6S6RaG60PMr8kGPWLT1vlqBmkvF2X-2eiehAObliUphf7eSChcbH1vKZjw3nP0YsLXABhQF_o7KLFUHXT4gpCKTiWgH_Fpm4W8jhL-CpLmoI5Dko8iRaum4esZ7b2bKPsVCW-PSJrWoAtC30lRJw67AvQO_7ze7fIJpduZwZsmdtV5qWaUpQzbX0M35xZTDYt7ckNGXdtrhVnj6ZvHVyrYDlOaO3EE7PhmN4jgIxe06-RiAbShF1pxSGhVf2HS6BT07N-Jdg8FuMTl6mjudE59P9Mp1qzA9StrQdCua_Q6myn8kCpBGg69lCJhssc9i8-f8qmRuy0D47d2Ou7Ve4vS9dFdz6PmoWXlowMNVDrj2aOK9FlwIqu2jlhMnWVP6mL76Zw1PkZO8oyd2yCf8ALC07ur5GBZF_IzAln-mIncaeVQbpBHh5nrniWTK5PO-zRLcY1zOFShd8utYeWjV_LUgP0HSqZzs2R-yfk6t1DbW-9cYVJO2T05Np3-vxRnerkPhxA6I83ckJXAU2pFM3syZuB0qcx8Dx0dF3QBAjGmwlqMhgzyNSNVRtI8wOhO11HZA4mAte-4VgpOgVAHJyUCnRje1KZ-dBs6oF5rM3uNOYajj3vAIa8JYHi60DgM_NzsGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d31dd0974.mp4?token=HpR_jqAWnacwofJHGsBr9eFNam-4TkfX1Fm1B-d6S6RaG60PMr8kGPWLT1vlqBmkvF2X-2eiehAObliUphf7eSChcbH1vKZjw3nP0YsLXABhQF_o7KLFUHXT4gpCKTiWgH_Fpm4W8jhL-CpLmoI5Dko8iRaum4esZ7b2bKPsVCW-PSJrWoAtC30lRJw67AvQO_7ze7fIJpduZwZsmdtV5qWaUpQzbX0M35xZTDYt7ckNGXdtrhVnj6ZvHVyrYDlOaO3EE7PhmN4jgIxe06-RiAbShF1pxSGhVf2HS6BT07N-Jdg8FuMTl6mjudE59P9Mp1qzA9StrQdCua_Q6myn8kCpBGg69lCJhssc9i8-f8qmRuy0D47d2Ou7Ve4vS9dFdz6PmoWXlowMNVDrj2aOK9FlwIqu2jlhMnWVP6mL76Zw1PkZO8oyd2yCf8ALC07ur5GBZF_IzAln-mIncaeVQbpBHh5nrniWTK5PO-zRLcY1zOFShd8utYeWjV_LUgP0HSqZzs2R-yfk6t1DbW-9cYVJO2T05Np3-vxRnerkPhxA6I83ckJXAU2pFM3syZuB0qcx8Dx0dF3QBAjGmwlqMhgzyNSNVRtI8wOhO11HZA4mAte-4VgpOgVAHJyUCnRje1KZ-dBs6oF5rM3uNOYajj3vAIa8JYHi60DgM_NzsGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درهای شرقی مصلای امام خمینی(ره) بسته شد
🔹
جهت ورود به مصلی، زوار و نمازگزاران باید به درب‌های شمالی مراجعه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/446978" target="_blank">📅 07:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nezOMCoNEM1YS-gIkK1fbVZ_IItBxBRxekqoJTC6wXfhu8USwQgyf_bL2Ak-DW8csOv0OBXYLTozzcWSczJciMxfLVgy1oosS44jbtnq4itRxN3l7Q4oO0wSSknMdvnHzu55dS8YwLle2hqymKYQMSARzTydsrAwwZK3bnilhZfkUhhvI5gtNR6PyUvO3C_xTiAgx3v5HFFIITeshCZ4nVpkRpCRYKOpP4e60MQyyGWfFZrpnyu5XjhfbvhDXtUuZTshB0RrzfemJocKtV6kF_5BBUyAbjma8KVOxxIDmuVRrdwL5dFcqOnnFQkMXAAC7aoi1_B3ehIT3gpqU7y8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9q6Lxi46omSmcMPtn40VkBrjT802fTEfoKI1xng9w_jC5R_Pfe6MbdL0qi-wcCenVZpc7sE2otzM3u4PDXNkXVHj3KJExj9JZXW0vUSdA3Zkgo9oUxa5z3fssjYPe9g4tJsrASqCIH7MM8mKCA0ZRZvHLLuaUFOEstUDSa6ZGAGLckkC5wQYT47-wsl4vr7SUf2BkSsb6CzFjWNepwosiJFpwUZVm8lRLetAZZoEHXweJkveD6WcZ5DvGxgIMw9UhSRiP95fQ7K6FpczUN9Ye2MqtPtMrC_n0Uqk1DRo0qyA8N_fQBEUk6fQi270KsNLkHJC3vgHJqANCUsIZNong.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واگن‌های مملو از جمعیت در خط سه مترو تهران به‌سمت مصلی
🔹
به‌علت ازدحام جمعیت در اطراف مصلای تهران قطارهای مترو در ایستگاه سهروردی هم توقف ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/446976" target="_blank">📅 07:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/446346dde8.mp4?token=Rb9nZV48Au8DmUqF8f3S9YRCWOW8srZIKM5iHPhy1BYAUoUhD1pE4ALzFUFzoD3t5tjHwssZkAtF6NkguQ1EejK8sg6P4IRqyT1vja0AFYIv-WbqthRKOGc2pIlwk_8H_dpCpqNzqm5-fqqlM5b-uTKaz-BQShvYiBAoDW6ek3DrTbJBYGt2ZfWXh_HoQUh7sXM_IXJoOT0bJIALA5rKYpPB97_ym-iWWkfESVlONCsi8xZxzNvMK4cSCnU6ftI4i_Molj446wra1U8rDKKNNKt0a3FFNkUIVNB1Tl0MF6h2DLRIRwz_ssf97IJz1EGmT8Zlk14YhDqH7VkRN8aEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/446346dde8.mp4?token=Rb9nZV48Au8DmUqF8f3S9YRCWOW8srZIKM5iHPhy1BYAUoUhD1pE4ALzFUFzoD3t5tjHwssZkAtF6NkguQ1EejK8sg6P4IRqyT1vja0AFYIv-WbqthRKOGc2pIlwk_8H_dpCpqNzqm5-fqqlM5b-uTKaz-BQShvYiBAoDW6ek3DrTbJBYGt2ZfWXh_HoQUh7sXM_IXJoOT0bJIALA5rKYpPB97_ym-iWWkfESVlONCsi8xZxzNvMK4cSCnU6ftI4i_Molj446wra1U8rDKKNNKt0a3FFNkUIVNB1Tl0MF6h2DLRIRwz_ssf97IJz1EGmT8Zlk14YhDqH7VkRN8aEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از جمعیت در حال حرکت در خیابان ولیعصر تهران به سمت مصلی
◾️
گزارشات میدانی از ازدحام سنگین جمعیت در خطوط یک و سه مترو در ایستگاه‌های متعدد خبر می‌دهد.
◾️
در فاصله ۱.۵ کیلومتری مصلی نیز ون و اتوبوس از پارکینگ‌های خودروهای شخصی برای جابه‌جایی نمازگزاران مستقر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/446975" target="_blank">📅 07:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcbfe50350.mp4?token=k3AdPD6nu3z4s44o7dnOzgem6oWVdeJiP44NOAs80ng0jEnODcuKEqu8HpYxa300xBSwrQGDiU5UPz0vEarueeJchBhYD9fNduc4DGpkS5l9MY98A7jUw8MLDdCVsRkBDF0SAX-41DLKvK_KjoPOg1ZnnCOASylTEYAsxnNm7gRzpsy3Lm7UXtm8HMXKGL2rsLFa6Zlhf43-axvChQMARFFXz0qZ_XnWY2UkwUlfYlpyL_Yw2STRgy-zo-ond5fRCkQodMQTgV1JMz0n_KTqje3aTvvIbGeLBFV7CLgGRGABfwGb-ObCxN5oz2zAcuPTWAB_nL2uazPYDSJfi59u0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcbfe50350.mp4?token=k3AdPD6nu3z4s44o7dnOzgem6oWVdeJiP44NOAs80ng0jEnODcuKEqu8HpYxa300xBSwrQGDiU5UPz0vEarueeJchBhYD9fNduc4DGpkS5l9MY98A7jUw8MLDdCVsRkBDF0SAX-41DLKvK_KjoPOg1ZnnCOASylTEYAsxnNm7gRzpsy3Lm7UXtm8HMXKGL2rsLFa6Zlhf43-axvChQMARFFXz0qZ_XnWY2UkwUlfYlpyL_Yw2STRgy-zo-ond5fRCkQodMQTgV1JMz0n_KTqje3aTvvIbGeLBFV7CLgGRGABfwGb-ObCxN5oz2zAcuPTWAB_nL2uazPYDSJfi59u0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
کسی که کشت امام مرا چرا نکشیم
◾️
که ننگ ماست اگر قاتل تو را نکشیم
◾️
از این به بعد کفن، جای جامه بر تن ماست
◾️
قسم به خون تو، قتل ترامپ گردن ماست
🎥
شعرخوانی محمد رسولی در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/446974" target="_blank">📅 07:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c282ff92fd.mp4?token=JdQMB1iS7IAkf80MTqMQ4qDOGAEsVmdBBQtBOsGdjVavFIA8nT4ce8uNz2LhxhC7TIQRzpLl0K_kIvvKsd7YfPlMnpnSH0WjRT1Y7pxfN1BFcxoBJ6K07BXdFMmXoPIfqk-slTwAlcsFPxQmnWoiiDbMVUV_POfLvCcA3qA4OE-M40pXBlBlGxYiYkIoNNmT-q-Lbo4EJtLXqi0wGWkLZApby2h-J7hkD4VsfFvihZM7TGevQQP7TAdSG8y_MKEtq19JBV1eNM5ZT_E9EcLMF2ZXQtDgeleEq0aDH1xq1UMLhCzM7e4yOOjIBcszr4MkHvg02Fj-bE5x3DVdVtzYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c282ff92fd.mp4?token=JdQMB1iS7IAkf80MTqMQ4qDOGAEsVmdBBQtBOsGdjVavFIA8nT4ce8uNz2LhxhC7TIQRzpLl0K_kIvvKsd7YfPlMnpnSH0WjRT1Y7pxfN1BFcxoBJ6K07BXdFMmXoPIfqk-slTwAlcsFPxQmnWoiiDbMVUV_POfLvCcA3qA4OE-M40pXBlBlGxYiYkIoNNmT-q-Lbo4EJtLXqi0wGWkLZApby2h-J7hkD4VsfFvihZM7TGevQQP7TAdSG8y_MKEtq19JBV1eNM5ZT_E9EcLMF2ZXQtDgeleEq0aDH1xq1UMLhCzM7e4yOOjIBcszr4MkHvg02Fj-bE5x3DVdVtzYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه یارانش آمده‌اند به استقبال...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/446973" target="_blank">📅 07:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2d5e1cc8.mp4?token=UzU7jbr7o0-u1l9AIv7SXzKkX6VHtL8uwn3-aDHNpbBb8xB58Jbg8FOPYH1NaEepJdrE8h9tYdgfqjiCP0Q_y71ydMkH5qf9IagmydED7vd1QSNlS86UT5eV4H_BCbf8aAkOWb-B1Nb3fNEzXMCE7Z6BwDRxgMXod3No9D9xvE9l-N8BEk4C3XPC3VEqSElYYxJ0vOs4-cfQXtvx8c4AMiv3cZyKQ7uufswp0eux8B4ehF7CyLsGasRcAFXkHWRA4m2dn3fMwGRuCr7Kb8xHu_TA4DR-3yb_cDo_IkoxN__dnssAYuB9dQDDHqHgWxG3mDnAQSwr6_3ooQt4w2MnfEpYq5sh0TGTJZ0p0utYyU11vC-El6Qkm_cdSzt7kJCo0GLLqqy-yeNxlms-eh3BxW41oXEkH5Ry7WXUcREdC2w5yXLkK3F-fBXwynpPFRYrMezNW9yC2brgVQZegYRM4195pGu75if76AhTdduGPvM6lZtM5lW2m2if4FPyAmp0FEPEan4gn-BnB2x6chASnFoOEopf0SBeRU-15mUXPstMXFVBPAxg2_9jaQZGINrdTEGtKLMIQ21jh5-MUb4hJOM7s097KZ33Pjl_FNSm8LFHxSb5YVv5NzAVVaz_qqhu_JCd6pqmzOGUkPFqiXcnSd2NTUQqKQRGLI-NT7bEIO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2d5e1cc8.mp4?token=UzU7jbr7o0-u1l9AIv7SXzKkX6VHtL8uwn3-aDHNpbBb8xB58Jbg8FOPYH1NaEepJdrE8h9tYdgfqjiCP0Q_y71ydMkH5qf9IagmydED7vd1QSNlS86UT5eV4H_BCbf8aAkOWb-B1Nb3fNEzXMCE7Z6BwDRxgMXod3No9D9xvE9l-N8BEk4C3XPC3VEqSElYYxJ0vOs4-cfQXtvx8c4AMiv3cZyKQ7uufswp0eux8B4ehF7CyLsGasRcAFXkHWRA4m2dn3fMwGRuCr7Kb8xHu_TA4DR-3yb_cDo_IkoxN__dnssAYuB9dQDDHqHgWxG3mDnAQSwr6_3ooQt4w2MnfEpYq5sh0TGTJZ0p0utYyU11vC-El6Qkm_cdSzt7kJCo0GLLqqy-yeNxlms-eh3BxW41oXEkH5Ry7WXUcREdC2w5yXLkK3F-fBXwynpPFRYrMezNW9yC2brgVQZegYRM4195pGu75if76AhTdduGPvM6lZtM5lW2m2if4FPyAmp0FEPEan4gn-BnB2x6chASnFoOEopf0SBeRU-15mUXPstMXFVBPAxg2_9jaQZGINrdTEGtKLMIQ21jh5-MUb4hJOM7s097KZ33Pjl_FNSm8LFHxSb5YVv5NzAVVaz_qqhu_JCd6pqmzOGUkPFqiXcnSd2NTUQqKQRGLI-NT7bEIO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یادتان می‌آید او اینجا نشست
◾️
لحظاتی از شعرخوانی محمد رسولی در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/446972" target="_blank">📅 07:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4135293f.mp4?token=BL4dcp9lZP6aKj3eHb5M3BMBdLqse49qk_EBHqf0yNZOPfyySDGY5qoU89Yn64USu0xAzPiOcurjAjLK8li6g_89xURJt7q6Eeysu359TBQLj2t-eOslMCyQwF0Se_OUXAyA2U07EEK_H0hIgDMQwKKuy-vg70sZGUiIBRM_-b_DquiOxuZ4XzCu73Jt08aym66NhEfzjNmcB8dzhkUpwgwdGMT8iyfInhqX-uC4xde0d6EnlVIwCtUjHcqrdrB79qUfz8y3KH3x_Ploa3UfXyfJE7aPyms44lcDZhmbFaVmWlpQQGv8rnPjZ5otkG6_v3MaSpf5YdsiXO9MHlvBQKnMX9PWsvgcI7t2bmunWTmpFTX4LLLZKXMqnAYpeeG1I_rg34LJTFGJIVRvubVScO-qxTBVDkJJWjMVTvKcsBrhfFTeLkOQ3-aT6fXIxHh3eamCidVsi3z9PAfPEEpToQ1T_YSb4xh37VDMmTgzW3sBS2gGq0yXTRu4rWhDzgNJWToCCOdmelsc2iMlS_L2QyM-6jEohAHlGioheN7JG21_Ucel6R4zynxq9Q9IDQIxztkaMTG-ca1vMuvBNg9N_ncK0hnZq0UKVB6G_saPpqmfK2C8Soq_A2UjgwUavdAkKJb8AEPOmJ1UksEQshtpEzoZO2rBodqmjx3LG9RnWW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4135293f.mp4?token=BL4dcp9lZP6aKj3eHb5M3BMBdLqse49qk_EBHqf0yNZOPfyySDGY5qoU89Yn64USu0xAzPiOcurjAjLK8li6g_89xURJt7q6Eeysu359TBQLj2t-eOslMCyQwF0Se_OUXAyA2U07EEK_H0hIgDMQwKKuy-vg70sZGUiIBRM_-b_DquiOxuZ4XzCu73Jt08aym66NhEfzjNmcB8dzhkUpwgwdGMT8iyfInhqX-uC4xde0d6EnlVIwCtUjHcqrdrB79qUfz8y3KH3x_Ploa3UfXyfJE7aPyms44lcDZhmbFaVmWlpQQGv8rnPjZ5otkG6_v3MaSpf5YdsiXO9MHlvBQKnMX9PWsvgcI7t2bmunWTmpFTX4LLLZKXMqnAYpeeG1I_rg34LJTFGJIVRvubVScO-qxTBVDkJJWjMVTvKcsBrhfFTeLkOQ3-aT6fXIxHh3eamCidVsi3z9PAfPEEpToQ1T_YSb4xh37VDMmTgzW3sBS2gGq0yXTRu4rWhDzgNJWToCCOdmelsc2iMlS_L2QyM-6jEohAHlGioheN7JG21_Ucel6R4zynxq9Q9IDQIxztkaMTG-ca1vMuvBNg9N_ncK0hnZq0UKVB6G_saPpqmfK2C8Soq_A2UjgwUavdAkKJb8AEPOmJ1UksEQshtpEzoZO2rBodqmjx3LG9RnWW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین حسین شعار ماست، شهادت افتخار ماست
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/446971" target="_blank">📅 07:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
نکات، احکام و چگونگی اقامۀ نماز میت بر پیکر آقای شهید ایران و خانوادۀ شهیدشان  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/446970" target="_blank">📅 06:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a994e20756.mp4?token=tfGSEvvl9-YnAOsYhBTF_5SUZpbqF-nBHmXqot7O3zDga6ZY-HMqw8BjtcaY-DC03qwSRszoFb-Zzmjy267h9IlMV0b0Klm8Ijnp_9la7AQq24k4gQHXTypBw2wXk27Dd00mw0yLv1AYOErb14u6tim4MGMbHHEKs8_4OWRoPZJS0_CGIMirwQPsAknIUTidri7ehPg4xAuz57EysZ4hcUrrRtlwiwntAkESzjSaznGXRJz7cGmvN3MZAW6N5KW9eqmbbTsTfthfPpwdT_Le0jKlD3bch6X_lcn4Df5logL9KVk-raKT2_Xwfhh8McT-7raM-xdwNxLhdgZn57erj1JhraGzMp83rgnwjAgt9w0ECXVte9eJqKpbH8VcEg-EZ33Txu5BsJqjpP_5iQo992ExBopMJ6PkUYDyNL907JTd_BhtMlfBttditDtBQnscPJHkWLzZrEzN3KJZmPVRjTcF3JzSkt6fMSQbv7VlyuWzEPII6ZUveBBHo8cYvFOiQhak70CMW-dG-7jCmkQN4nXAIqPqxZasAmRSo_B-mhVa8Dq9w4RJIEtfD3Xdgy-_uhVuwznEW8GBf3bFfddxLgaTZt56_3h13vWJIte7z7fwFPcwQmNxvKRKeIu-89NTtP0fVq1S8d_nEiT1BjMXDw9GBGlv3iA4N9OJr3gQY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a994e20756.mp4?token=tfGSEvvl9-YnAOsYhBTF_5SUZpbqF-nBHmXqot7O3zDga6ZY-HMqw8BjtcaY-DC03qwSRszoFb-Zzmjy267h9IlMV0b0Klm8Ijnp_9la7AQq24k4gQHXTypBw2wXk27Dd00mw0yLv1AYOErb14u6tim4MGMbHHEKs8_4OWRoPZJS0_CGIMirwQPsAknIUTidri7ehPg4xAuz57EysZ4hcUrrRtlwiwntAkESzjSaznGXRJz7cGmvN3MZAW6N5KW9eqmbbTsTfthfPpwdT_Le0jKlD3bch6X_lcn4Df5logL9KVk-raKT2_Xwfhh8McT-7raM-xdwNxLhdgZn57erj1JhraGzMp83rgnwjAgt9w0ECXVte9eJqKpbH8VcEg-EZ33Txu5BsJqjpP_5iQo992ExBopMJ6PkUYDyNL907JTd_BhtMlfBttditDtBQnscPJHkWLzZrEzN3KJZmPVRjTcF3JzSkt6fMSQbv7VlyuWzEPII6ZUveBBHo8cYvFOiQhak70CMW-dG-7jCmkQN4nXAIqPqxZasAmRSo_B-mhVa8Dq9w4RJIEtfD3Xdgy-_uhVuwznEW8GBf3bFfddxLgaTZt56_3h13vWJIte7z7fwFPcwQmNxvKRKeIu-89NTtP0fVq1S8d_nEiT1BjMXDw9GBGlv3iA4N9OJr3gQY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نکات، احکام و چگونگی اقامۀ نماز میت بر پیکر آقای شهید ایران و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/446969" target="_blank">📅 06:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446968">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ed4f6f47.mp4?token=Ux3MuItqXQCj3mYlnxeVIqivwuvOZmBUidnhWvmgh7FTLpTiwI5pGgT6q-URTmdGfK0FlBsxVV47j2j3jl8vAq45TbDuAITIt-TueL5FHErQ21-6NXMVDKilEOp81-qYX_yXNDlG_iolbI7e7HTS1zNDOX93RbiXwvPDIdnmSpfnwZhSiG7UiKQ9ezm1ZxSI2-q7azn9ZvGikVRHR3tgI-zeCTGWe1101ndole7aaoJ14stdYhIMoD4iKZKwG4IjxVBC9Q9XMSUkT1Mc69iuUeeXUryUvd1Wx7ZfZ47j6meUvnAZa3h-ZZ5klJRlu7zNbhez8rQ6sSn8rp8Ykd4k6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ed4f6f47.mp4?token=Ux3MuItqXQCj3mYlnxeVIqivwuvOZmBUidnhWvmgh7FTLpTiwI5pGgT6q-URTmdGfK0FlBsxVV47j2j3jl8vAq45TbDuAITIt-TueL5FHErQ21-6NXMVDKilEOp81-qYX_yXNDlG_iolbI7e7HTS1zNDOX93RbiXwvPDIdnmSpfnwZhSiG7UiKQ9ezm1ZxSI2-q7azn9ZvGikVRHR3tgI-zeCTGWe1101ndole7aaoJ14stdYhIMoD4iKZKwG4IjxVBC9Q9XMSUkT1Mc69iuUeeXUryUvd1Wx7ZfZ47j6meUvnAZa3h-ZZ5klJRlu7zNbhez8rQ6sSn8rp8Ykd4k6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر من، طلایه‌دار لاله‌هایی، مسافر کرب‌وبلایی...
◾️
لحظاتی از روضه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/446968" target="_blank">📅 06:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446967">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41336fbbbb.mp4?token=UMK7am15AVN8bs36iPZHAZKJTIWaVkYrGAFMp5usQWBhbOzgs4-YKcdjc9lRbeA6HPQrncr_43ApIslfRdOonL3nwcU1FfWpAD8goNP19lhdZTpugux_DFEv9YtEXzD3BhZ4G4hvWW4FTJ76hqbclm0Qi7CCRRJDxtlvKBWcve7DhsdzkTdK1lU3OpQ6fih8T1H2l-VIfZXdXwQxLjGwixZ4rB1yzvIT1BRmi6JA-O2ZAG9VlWp62xdpJfs3hc6eluwDheZhcAyVhtk5WLvpmmCd49WpKcUbyQrk_dTFCusUxSq4nJSXgsp1kL3I8k6EO5beZVTPQTeXBCiH1n3QNKPG0JkAlsM_l6QewnFUG-m8x5AK1X1K_a0TfybkvzAlm9BDMxBbTtWQTh0zgzuyozDe0BoRSVajx6hhlL8OkDZJQp30NYN6noVa-tUjceYGwR7ThSobiFu5GHlx5gJ25yv2qhOmGx__ai_gjXjKMh7H89vHLXg7A9Oh-gO2BNl_Lu91_btS0RfFnjnxpkP58CSAJDzP3ByjnDMNaJweC0kSmJqr5opj9rLDXeViIts_EcIjK5zRhzbynPshQqEidR0Z0PtjR247aCXtre5khSgTv95Vn9fGrdJ3hTYvZkYZEXMU-5XWvdPMM8l9iAuvkr6WO2ksRb1-nH9_NQV-vcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41336fbbbb.mp4?token=UMK7am15AVN8bs36iPZHAZKJTIWaVkYrGAFMp5usQWBhbOzgs4-YKcdjc9lRbeA6HPQrncr_43ApIslfRdOonL3nwcU1FfWpAD8goNP19lhdZTpugux_DFEv9YtEXzD3BhZ4G4hvWW4FTJ76hqbclm0Qi7CCRRJDxtlvKBWcve7DhsdzkTdK1lU3OpQ6fih8T1H2l-VIfZXdXwQxLjGwixZ4rB1yzvIT1BRmi6JA-O2ZAG9VlWp62xdpJfs3hc6eluwDheZhcAyVhtk5WLvpmmCd49WpKcUbyQrk_dTFCusUxSq4nJSXgsp1kL3I8k6EO5beZVTPQTeXBCiH1n3QNKPG0JkAlsM_l6QewnFUG-m8x5AK1X1K_a0TfybkvzAlm9BDMxBbTtWQTh0zgzuyozDe0BoRSVajx6hhlL8OkDZJQp30NYN6noVa-tUjceYGwR7ThSobiFu5GHlx5gJ25yv2qhOmGx__ai_gjXjKMh7H89vHLXg7A9Oh-gO2BNl_Lu91_btS0RfFnjnxpkP58CSAJDzP3ByjnDMNaJweC0kSmJqr5opj9rLDXeViIts_EcIjK5zRhzbynPshQqEidR0Z0PtjR247aCXtre5khSgTv95Vn9fGrdJ3hTYvZkYZEXMU-5XWvdPMM8l9iAuvkr6WO2ksRb1-nH9_NQV-vcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت مردم با رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی خامنه‌ای
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/446967" target="_blank">📅 06:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/446966" target="_blank">📅 06:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcecb0ea40.mp4?token=SVPbHhf4hKKIMrvjF1FjxjYACh5nmEUmwFaOSJ_hWAq1IAVhRo31fJewYx2enxb0lqQzkKJNurK7-vXPSSZfdteXrkagGmBNLVz_YH8CRnP08gXvvUsdEyLVz5ZssMWxqvaKwNGxIWdS4c-M3rqNKvgw3B6n5f2zBC73bnUnsxkkpaO29670E67ZWU0EVRvQXWa8BiUjj4jZjUkYcqo1TWTb8mwQm7QgORpmr-mja4-PcqUvj4omEPh2mjfiVfJ6FNlW-cl0LIvvyIyMrofF8VReTg8SboRk0YybQpnU69Pj9yL68vYdABdizv1jrfBdiUyJdTCk10s4nMhQz0s-pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcecb0ea40.mp4?token=SVPbHhf4hKKIMrvjF1FjxjYACh5nmEUmwFaOSJ_hWAq1IAVhRo31fJewYx2enxb0lqQzkKJNurK7-vXPSSZfdteXrkagGmBNLVz_YH8CRnP08gXvvUsdEyLVz5ZssMWxqvaKwNGxIWdS4c-M3rqNKvgw3B6n5f2zBC73bnUnsxkkpaO29670E67ZWU0EVRvQXWa8BiUjj4jZjUkYcqo1TWTb8mwQm7QgORpmr-mja4-PcqUvj4omEPh2mjfiVfJ6FNlW-cl0LIvvyIyMrofF8VReTg8SboRk0YybQpnU69Pj9yL68vYdABdizv1jrfBdiUyJdTCk10s4nMhQz0s-pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌های ما از غصه لبریز است آقا
◾️
لحظاتی از نوحه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران  @Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/446965" target="_blank">📅 06:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec39e7d8be.mp4?token=nxODfWLvL7GWoXC9DDZzpvy96-yVfzskkCpsF2PtjnbC77hmlnuKlb5MshFj4QcG7_ms7S4WhcloNnqjkBtc6eN3oybJAkHlSBzPV0a662N6_j_9A-xTrkg4FXZ2UGYMRCO3ScEKHfWsgCIcJ0EFsDglRX7l0Gf9WzPSiG9MCLmVeGHh82gcX7LfUrsMVj_s2zuil2o0J4NCRvJlpKh5u6mYTG6QCz6lGEa7gZ7AOisHbGlpCTuY91-TZ6KEuXe5XyB4VrSNhgsipNxNxatMB9JPi8gdM0okyg1ga8FTQyrbb8ckxATzSLo-ZFw8wk2J8azSF7m519NmmwV2dQyJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec39e7d8be.mp4?token=nxODfWLvL7GWoXC9DDZzpvy96-yVfzskkCpsF2PtjnbC77hmlnuKlb5MshFj4QcG7_ms7S4WhcloNnqjkBtc6eN3oybJAkHlSBzPV0a662N6_j_9A-xTrkg4FXZ2UGYMRCO3ScEKHfWsgCIcJ0EFsDglRX7l0Gf9WzPSiG9MCLmVeGHh82gcX7LfUrsMVj_s2zuil2o0J4NCRvJlpKh5u6mYTG6QCz6lGEa7gZ7AOisHbGlpCTuY91-TZ6KEuXe5XyB4VrSNhgsipNxNxatMB9JPi8gdM0okyg1ga8FTQyrbb8ckxATzSLo-ZFw8wk2J8azSF7m519NmmwV2dQyJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از تراکم جمعیت در خیابان‌های شرقی منتهی به مصلای تهران (تقاطع خیابان‌های شهیدان بهشتی و قنبرزاده)
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/446963" target="_blank">📅 06:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f899e09814.mp4?token=BzZfNFWJFNE8uW5yZ-oMKmTyqd7PDT7KOGxLK--iqJJEEW55PILRfJ_joI-6-5MR14AiFSIzFr6X3yBjKqdVmUpzjUz0gnXnpaNTA5SKqOjksd0gvpWIwIpqp2vgPQ7LXckb48UGdWzoyjxTMiWPzSgkKSS5T9Lb0ZIYWLc3AjWm9bRWlKK2qU1_IJmQzag9U-a1OpjB162xMWwu3YQHmvK40FQ28nE4S0jwXvnExFYfmmm5fb0btmMcI9-P0X8yGaxSbXZba3iURcW2QhALxk03hSsgh3XQdBMIi9T9XrI7B3grbkVwh8M6vEZW9i065YHypCacEvZwHyB9gp2f7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f899e09814.mp4?token=BzZfNFWJFNE8uW5yZ-oMKmTyqd7PDT7KOGxLK--iqJJEEW55PILRfJ_joI-6-5MR14AiFSIzFr6X3yBjKqdVmUpzjUz0gnXnpaNTA5SKqOjksd0gvpWIwIpqp2vgPQ7LXckb48UGdWzoyjxTMiWPzSgkKSS5T9Lb0ZIYWLc3AjWm9bRWlKK2qU1_IJmQzag9U-a1OpjB162xMWwu3YQHmvK40FQ28nE4S0jwXvnExFYfmmm5fb0btmMcI9-P0X8yGaxSbXZba3iURcW2QhALxk03hSsgh3XQdBMIi9T9XrI7B3grbkVwh8M6vEZW9i065YHypCacEvZwHyB9gp2f7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جمعی از مردم هندوستان در مصلای تهران جهت وداع و اقامه نماز بر پیکر رهبر شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/446962" target="_blank">📅 06:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859457ceb0.mp4?token=MU6uELieAPgZa9ShFxsqxaTmV_VCG5gHQO4novfwO2iKwBhMDfvTiqsxyY4NtCpX1jGbFEL6qoBu4CAJCVt5XrxPVpl9ZVWMnbquIP4x1L7XQgLmLLdLc7v6aRLcOzC2ttOs6ILxpPZzbuBc6MPQWBVk5yCLbpcqEgBplry5AfbrddOGejRiL0U155it4_g3ZUiWzzJsgFCNubfGd5JULQxEOnKriu2DUBi2TAVUUs5szKCYMqSEAfgDC5huiqSr5xAMzRgyLnHm1cITkkiM0AN1bI4kfWUK9eVJEPATtVEU6BvYv38VqD0y_Rfn9M9sYdraNjB3IxJ3d8V5zpczmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859457ceb0.mp4?token=MU6uELieAPgZa9ShFxsqxaTmV_VCG5gHQO4novfwO2iKwBhMDfvTiqsxyY4NtCpX1jGbFEL6qoBu4CAJCVt5XrxPVpl9ZVWMnbquIP4x1L7XQgLmLLdLc7v6aRLcOzC2ttOs6ILxpPZzbuBc6MPQWBVk5yCLbpcqEgBplry5AfbrddOGejRiL0U155it4_g3ZUiWzzJsgFCNubfGd5JULQxEOnKriu2DUBi2TAVUUs5szKCYMqSEAfgDC5huiqSr5xAMzRgyLnHm1cITkkiM0AN1bI4kfWUK9eVJEPATtVEU6BvYv38VqD0y_Rfn9M9sYdraNjB3IxJ3d8V5zpczmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
◾️
نوحه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/446961" target="_blank">📅 06:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446959">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a9b8b436.mp4?token=l9Ss112vRfJY4z_IdeYTsmBeiDVYrBKVJGSP9c3fCAWd4KZQKA5h_-nYSU3nf_fA77kqh4Gfkio-6LtZvmgDi0-id5VMh_kwUCOWR9FSkGvKMqyDVhfu1VXUXvl82IN---p2W58tLQnqs3BlAPxq6oGRdzaP4BTHYNwI_1JM6tkLhVJwDZ5xivS1ALXMb-cwJB8VSSGULg8q5LKJkkbJItuQOg6o_OKLQkA28GeGUEVYBJXYnXNXEMXvFIrQPrDB7e6dIRxnNMC1nEaC3b0TVrFwL5L0ocSmRf3ER0bCVQzT65ZdmAiAoRgJyVJYaCPpQGFLTHIb5rKzmfNUYOrlbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a9b8b436.mp4?token=l9Ss112vRfJY4z_IdeYTsmBeiDVYrBKVJGSP9c3fCAWd4KZQKA5h_-nYSU3nf_fA77kqh4Gfkio-6LtZvmgDi0-id5VMh_kwUCOWR9FSkGvKMqyDVhfu1VXUXvl82IN---p2W58tLQnqs3BlAPxq6oGRdzaP4BTHYNwI_1JM6tkLhVJwDZ5xivS1ALXMb-cwJB8VSSGULg8q5LKJkkbJItuQOg6o_OKLQkA28GeGUEVYBJXYnXNXEMXvFIrQPrDB7e6dIRxnNMC1nEaC3b0TVrFwL5L0ocSmRf3ER0bCVQzT65ZdmAiAoRgJyVJYaCPpQGFLTHIb5rKzmfNUYOrlbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌نیابت از ۱۶۸ زائر جامانده
◾️
وقتی موکب شهدای دانش‌آموز میناب به کانونی برای همدلی زوار کودک با این شهدای عزیز بدل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/446959" target="_blank">📅 06:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446958">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de2d049c.mp4?token=dxjJOBpUj6irCIAxZYkQdsLxcVp_YBFJkLDzPiSW8vWPo99HjQyr4gBFs5xt9sv3UjVLiaHp5NEf1Am01FDWnJfiHKkE0eherh4FYLhN2lKTesSsn0o5pUO9sx6zqEx4KAb_7Ekfk9a1bVMieIZyDPgufdEbNqvLd2ZgYiHY-XBMiuAsZYU07V5E0y_y67EZYSWD0ugwwhN7jJ3cIB6rgihnFpbiqMSEbNEKc82ZUBL9Sl-fIl1AuIFI9F2F4-ISPKOySG1OyH-oV0CwqmYQ3Jb4bS5Ell7_uqf3Ex5YAmkT4blUkm77utCBC92mFSpGvRiTHcwyX2GmW4QLwM8ajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de2d049c.mp4?token=dxjJOBpUj6irCIAxZYkQdsLxcVp_YBFJkLDzPiSW8vWPo99HjQyr4gBFs5xt9sv3UjVLiaHp5NEf1Am01FDWnJfiHKkE0eherh4FYLhN2lKTesSsn0o5pUO9sx6zqEx4KAb_7Ekfk9a1bVMieIZyDPgufdEbNqvLd2ZgYiHY-XBMiuAsZYU07V5E0y_y67EZYSWD0ugwwhN7jJ3cIB6rgihnFpbiqMSEbNEKc82ZUBL9Sl-fIl1AuIFI9F2F4-ISPKOySG1OyH-oV0CwqmYQ3Jb4bS5Ell7_uqf3Ex5YAmkT4blUkm77utCBC92mFSpGvRiTHcwyX2GmW4QLwM8ajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این آخرین نماز جماعت است، بازم صف عشق، پشت سر امام امت است
◾️
نوحه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/446958" target="_blank">📅 06:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446957">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee61da0fda.mp4?token=n2VB8oQM6EG4JSGJvIFkUwC-YNpN05-j3KIYs5clMPWDIX9OR5x8We3PQ8fYm3ImoUkQATouEFL0pfna2HmOZCG3dHdGoKkrKZJzS4idd30cFSVo4UgUOyQ-yf-9PfRVQPrgCCTjaMxakV70rd3bobnYTbK-msWMbfcQA-gTxgZMQ7fCeYkFGuLmv-AIXwJhYBF9GzK73H-FCu_T7T-lkXJNeRmdY3letUC-Mmrh_N2xRNtIw6rDVzo0BnqI_VCZ3Mk1R-DeCKPPgV5GdNesdJJTCL2QSUzWMWHC_PMJw-Rllgqe8cHR6CcR8kZsGbCi5eJurgf5-kSKQgxkGT8tyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee61da0fda.mp4?token=n2VB8oQM6EG4JSGJvIFkUwC-YNpN05-j3KIYs5clMPWDIX9OR5x8We3PQ8fYm3ImoUkQATouEFL0pfna2HmOZCG3dHdGoKkrKZJzS4idd30cFSVo4UgUOyQ-yf-9PfRVQPrgCCTjaMxakV70rd3bobnYTbK-msWMbfcQA-gTxgZMQ7fCeYkFGuLmv-AIXwJhYBF9GzK73H-FCu_T7T-lkXJNeRmdY3letUC-Mmrh_N2xRNtIw6rDVzo0BnqI_VCZ3Mk1R-DeCKPPgV5GdNesdJJTCL2QSUzWMWHC_PMJw-Rllgqe8cHR6CcR8kZsGbCi5eJurgf5-kSKQgxkGT8tyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این آخرین نماز جماعت است، بازم صف عشق، پشت سر امام امت است
◾️
نوحه‌خوانی میثم مطیعی در مصلای امام خمینی(ره) تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/446957" target="_blank">📅 06:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446956">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c53b445b6.mp4?token=putQU0-GziV9J3GkzNiW6HIJ1Ueid84WB1rOgk1U0kYyvSYr7aKKdfHUF40j6QzpvT92bMt0yno7grHPbNQv_L38sWc8Dp0n9vg8T-vIjxTE5YBS5qvHspIvwbcQKxSnEZ1Ef-IwhLm6keMwsZUNUQQzCx1HnhVxMBjAZHPCwt1lJqnqhg4ojXQ5wnPCs57zA3JZJO4F6ogiY9yKYAmS8_LcKXrXFquDO1sCFtxEAa71C9DHrjHHrB0mND-3rv01h0evvMyopIuFP8HuyIRTa4Zs6r0WnqyYMgzDpoDZJ2O9xNxIPPlVNt1MKhclta2frlJib4gyl-LeDjS4FdtD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c53b445b6.mp4?token=putQU0-GziV9J3GkzNiW6HIJ1Ueid84WB1rOgk1U0kYyvSYr7aKKdfHUF40j6QzpvT92bMt0yno7grHPbNQv_L38sWc8Dp0n9vg8T-vIjxTE5YBS5qvHspIvwbcQKxSnEZ1Ef-IwhLm6keMwsZUNUQQzCx1HnhVxMBjAZHPCwt1lJqnqhg4ojXQ5wnPCs57zA3JZJO4F6ogiY9yKYAmS8_LcKXrXFquDO1sCFtxEAa71C9DHrjHHrB0mND-3rv01h0evvMyopIuFP8HuyIRTa4Zs6r0WnqyYMgzDpoDZJ2O9xNxIPPlVNt1MKhclta2frlJib4gyl-LeDjS4FdtD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف مردم برای اتوبوس‌ها و ون‌های به مقصد مصلای تهران
🔹
علاوه‌بر مترو، خطوط اتوبوس و ون‌ها از مبادی اصلی برای جابه‌جایی زائران و نمازگزاران رهبر شهید انقلاب فعال هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/446956" target="_blank">📅 06:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446955">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_1pur0YeEi4O1GZS90xjpP9VGGh2RslOZI8QXE8AsYMGRWZ4iUsTYB4QnD9FXEVFTk-85PZrvJppTlCyeIIWwp8NQ9yk7IRzC7ITTg8jYoXQWb0V8ECdGPBud3SXkzQ-2usbI43W_ZO8lkYNajbDNu-DzyorD76YaEyiEjJuKAWTrPvImFclu9xY8IXwXWr3Fv4OAHn7du5ru43mOyQSUQl4_tiUVNDPPhmE8LdDZgClf-z3bsJ_jTY_yREVfnKRQ2EOe6wf9319RFPPPCG64J0SkvRR8VmVMoOl-03VfO03cRax4owcBfddd9PeynRF1WRGmsX7ox1XdzrbltJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آیت‌الله سبحانی بر پیکر مطهر رهبر شهید انقلاب اقامۀ نماز می‌کنند
◾️
مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید و خانواده شهید والامقامشان، به امامت آیت‌الله سبحانی در مصلای تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/446955" target="_blank">📅 06:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446954">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cc33fad.mp4?token=r9P0s2qnq5LlML7SVaQrFYeNDXZmEwNaHRJSTxmoXv2rYM7_4vqJdcXv_npSwkDgP0PiFc8LuSCPw3m3tkQRaPYCaId6pD9c4uA06iCX8sgpDPmdczvAeDSaOBIbKbU-uKnU5Wl36q4lbiOLj6DhmGdERF73BeHrk8U146ubZsMq0EfcwQM3XyjjhuVbq-QDzSFQ2HaoqJqViwgbPyCsty_C8jdXOtNjZIWKmU5wyYIP0u1qzkTLkWcxD1f1Doeq-8MgBAW2voGGpIGYLK9V_dEUVm7AWEDK9QJVMC1_Y4GbX9YWks4VMji3eYzlSOGR0nLhfWgHjOPTi8WRGrkGGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cc33fad.mp4?token=r9P0s2qnq5LlML7SVaQrFYeNDXZmEwNaHRJSTxmoXv2rYM7_4vqJdcXv_npSwkDgP0PiFc8LuSCPw3m3tkQRaPYCaId6pD9c4uA06iCX8sgpDPmdczvAeDSaOBIbKbU-uKnU5Wl36q4lbiOLj6DhmGdERF73BeHrk8U146ubZsMq0EfcwQM3XyjjhuVbq-QDzSFQ2HaoqJqViwgbPyCsty_C8jdXOtNjZIWKmU5wyYIP0u1qzkTLkWcxD1f1Doeq-8MgBAW2voGGpIGYLK9V_dEUVm7AWEDK9QJVMC1_Y4GbX9YWks4VMji3eYzlSOGR0nLhfWgHjOPTi8WRGrkGGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محوطۀ مصلی پیش از آغاز نماز مملو از جمعیت شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/446954" target="_blank">📅 06:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446953">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: صدها نفر مثل علی خامنه‌ای در این راه جان و آبرو خواهند داد
◾️
مسئولیت رهبری حفظ نظام و انقلاب است. رهبری یک عنوان و یک شخصیت و یک حقیقت برگرفته از ایمان و محبت و عشق و عاطفه مردم و یک آبروست. صدها نفر مثل علی خامنه‌ای در راه این حقیقت جان و آبرویشان را می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/446953" target="_blank">📅 06:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446952">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558bf8c37d.mp4?token=ZtRVQySdubxx3bVvZOvgbzw2g8p-HXr2gSennFwThQoN8kg9bI1ZVsymXLeFVuL-7u4vPljDTXYvJZo6UbBRmQINPAzNwaXeFpcqW8qQELqlFejmvem24ofsDZjcILvyWtE2E6TQQxrLzPa3pzuWsSXD0wY0MQyFH2H3MOblcq9lXpVSIpzxu0AKVhf4IWUzDL5aqrf6OQ6_hRVwLjE0Xp2kwShFBOmFb85-Cv60pgudRY1jbt5up6NBI1qnRpFOIH8B_rXKArhIvNgu1kBh9a6bGlDvqueddazGaA5Bcwxm55u1L6HZ8DhzAp3uVaQdVOetu3qgjLFGDaxN9shp7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558bf8c37d.mp4?token=ZtRVQySdubxx3bVvZOvgbzw2g8p-HXr2gSennFwThQoN8kg9bI1ZVsymXLeFVuL-7u4vPljDTXYvJZo6UbBRmQINPAzNwaXeFpcqW8qQELqlFejmvem24ofsDZjcILvyWtE2E6TQQxrLzPa3pzuWsSXD0wY0MQyFH2H3MOblcq9lXpVSIpzxu0AKVhf4IWUzDL5aqrf6OQ6_hRVwLjE0Xp2kwShFBOmFb85-Cv60pgudRY1jbt5up6NBI1qnRpFOIH8B_rXKArhIvNgu1kBh9a6bGlDvqueddazGaA5Bcwxm55u1L6HZ8DhzAp3uVaQdVOetu3qgjLFGDaxN9shp7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلای تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران مملو از جمعیت است  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/446952" target="_blank">📅 05:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wTsywTeffGawrLXaw0G38FNgwJXT7XXJZYoD7mIEEi0nEykauu1QtKcpJ4-8c2mDGrmrcyPcG1UrH__Zf9OXeyS1Y9v8_SgGKQZ9sPGIES2nuja0Io2bOqr9izuXtZQxLchx6jlGPijDRnlQbGTOw7WKMnjoPpMdHfqOy_INLFQrIltCvE5fD-4HQgUPIEf1LiRfSqyWBUAFgOcAYON5FJOjk1zf_dsKeySZpEGdDSOcRvSKmTgkGrNJJ2uvAX4qNcSFxyCdpFP-KbUfG47CBDhuZoYIiKal9D3b3SZRTDb_iw3ZBjC_rfeOdIipWPly1BN_6Wvy0pKkOMDsmVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQ947ir5RIaaG4z7gDmpOC6DBi3D_-bYMYcGzlK0gGwR4QH5YwlxKz1DRixHu7xrTDg50VmoHOR2atFjAeaBRlukv6oZvQErJNbog3xapz5dZWC_BdXVxdsZuvPGSq4QHq1Vt57cbSciwZj-OqXDj72HkXjq2SavWVzWgDtwDJb4NdzIFRgptPk32KOoeFTy0S-x15X-X3aBPi8KfQE5C422JXiX_3C26UrhbKe8ofCNszR66Xl5TSgJg6zWwiOlbpn8BhRmzJQD4CkKu3Ie6HTz9Q6iikuomFctZyp0ht6S_nuS0IOxT2pter6e9lqRrgf3eug90vMXMoh-6KJR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1J2ZMshnuTXIv9roRtzA1D1Z1OJZfW21u-S_sw3k1ntnHuxf-pj3_7Uv3_THLCGmoA8tRUP0Qf5rStiD_jyk8Pkq5Dc-qZNVRKpJIb6Aso-xG9LrfWptxAh3F0LKAqK-7OSRxDlTPHnU7GupZS9vCL6FaPU0YjCP200W0z3F_adEbafy8bhGkElLBZUYggfyFo8WDN1L94TeIKDjVyBd-hpE_vv0hYl8oEZWCF3emLhzhlRpuLw1Nkr9C488LxrTTRctHszHRs3iD_X7H7UT0GlGa0qq8QU8uG2ssikgUn2jKHnOKuwHALCoqjqTJ9A_lhjXJg-1oXeKI45pByfpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
سه قاب از آخرین حضور رهبر شهید انقلاب در مصلای تهران در ۱۱ فروردین ۱۴۰۴ و اقامۀ نماز عید فطر
◾️
و امروز یکشنبه ۱۴ تیرماه ۱۴۰۵ تا ساعتی دیگر مردم عزیز ایران بر پیکر امام شهیدشان اقامۀ نماز خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/446949" target="_blank">📅 05:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8109e070d5.mp4?token=Y2UNQ-KpuggIzx2zLt_7M82iOADfmbvBRsdSTshqv8P8oXntF3_MuU-jKjIxy6qpp6RrgdH3XQMVEBlTPL7szYiNU-TOSUAwf8VjhIrr_PMq868eY179O5-rG1OAn1Yer_CpU1m1ZaIcrofMup6EzmdqL1cMWtkMN8WyKMnxbOCSdz5gSiuBQKzxGZSXXISxb4DwvmIEmyABKdvSuLU0lny1qFT-vcnrz_tS2fRuATo18tbWoCMmBculqNXQ6Eg1zS7vKNxkWpcrEcEtmiBrCRx2AJnqkFnig8Ex9Ks-CLmag9Rcbp34Npk9G-wB61eCreg4tbwAFGZA7ZlPeQ_ioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8109e070d5.mp4?token=Y2UNQ-KpuggIzx2zLt_7M82iOADfmbvBRsdSTshqv8P8oXntF3_MuU-jKjIxy6qpp6RrgdH3XQMVEBlTPL7szYiNU-TOSUAwf8VjhIrr_PMq868eY179O5-rG1OAn1Yer_CpU1m1ZaIcrofMup6EzmdqL1cMWtkMN8WyKMnxbOCSdz5gSiuBQKzxGZSXXISxb4DwvmIEmyABKdvSuLU0lny1qFT-vcnrz_tS2fRuATo18tbWoCMmBculqNXQ6Eg1zS7vKNxkWpcrEcEtmiBrCRx2AJnqkFnig8Ex9Ks-CLmag9Rcbp34Npk9G-wB61eCreg4tbwAFGZA7ZlPeQ_ioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
| کاروان علمای اهل سنت در مسیر مصلی تهران
@rahbari_plus</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/446948" target="_blank">📅 05:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a16d06ab.mp4?token=u92pjUBANqV6c4cOrBZcYm7lwYHyCUUFQqhLTf8IQ81hZ4a8X5h5Nm1QaUp6YpaYvmpm7hCh1AsracJwlvWlq1DSw1-mTRQR4392jt4djDoze6axeOwungZKD8QsRI9CM9XOGsg3yGJLkZVt8jUpk5TFIbQSI7TmYqh-0DJh8cJd5WyRYuEvLLFP5eneOvN5iN-tVFYw9NIG1ZJHY6tzuaB-1qD9vmFKXGYCQdXKKPuB2QwyBV38rDzmQcxiuap278_FtamOk3V2IWDvgc5Emxf6Wk7gBScnSSAaKDViEqjsiE_4jEJg-S7yR8XbF8F6AYm5xdvG6vRxacBQVwbSbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a16d06ab.mp4?token=u92pjUBANqV6c4cOrBZcYm7lwYHyCUUFQqhLTf8IQ81hZ4a8X5h5Nm1QaUp6YpaYvmpm7hCh1AsracJwlvWlq1DSw1-mTRQR4392jt4djDoze6axeOwungZKD8QsRI9CM9XOGsg3yGJLkZVt8jUpk5TFIbQSI7TmYqh-0DJh8cJd5WyRYuEvLLFP5eneOvN5iN-tVFYw9NIG1ZJHY6tzuaB-1qD9vmFKXGYCQdXKKPuB2QwyBV38rDzmQcxiuap278_FtamOk3V2IWDvgc5Emxf6Wk7gBScnSSAaKDViEqjsiE_4jEJg-S7yR8XbF8F6AYm5xdvG6vRxacBQVwbSbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلای تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران مملو از جمعیت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/446947" target="_blank">📅 05:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88437a1c33.mp4?token=nSVgReC934h_JyN7ftp7Vkj_LH47agIy1gsSgXohHVLuKtgPY7_Jw430DMy_WC_bDDX3r_OEaVRdICiKg0eQP_kVewlqhnkyCJ4HBoqiWp26kJUxt1FWZBHFufPeEC5PtVVDwdcFjA5PUVIWIeAid30ckEzb_BIRiimGsvqegwnEU17TIgrVLrruT0z4Sh4tNgUj4dK64kVAhMmQp7ooQPT6K2RnvDpjWqpPJrmmQKjpWog7mivyiEnD7agdyED0A82mOrrS2-lNun7kIfvl9fq_-0J1uu2Xfnvqc2U5-HbSbCmi5dgdodz8fL7DBlATKiZfR21VJ6Lm2kacGDo5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88437a1c33.mp4?token=nSVgReC934h_JyN7ftp7Vkj_LH47agIy1gsSgXohHVLuKtgPY7_Jw430DMy_WC_bDDX3r_OEaVRdICiKg0eQP_kVewlqhnkyCJ4HBoqiWp26kJUxt1FWZBHFufPeEC5PtVVDwdcFjA5PUVIWIeAid30ckEzb_BIRiimGsvqegwnEU17TIgrVLrruT0z4Sh4tNgUj4dK64kVAhMmQp7ooQPT6K2RnvDpjWqpPJrmmQKjpWog7mivyiEnD7agdyED0A82mOrrS2-lNun7kIfvl9fq_-0J1uu2Xfnvqc2U5-HbSbCmi5dgdodz8fL7DBlATKiZfR21VJ6Lm2kacGDo5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد نمازهای عید فطر رهبر شهید در مصلای تهران، ساعاتی پیش از شروع مراسم اقامۀ نماز
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/446946" target="_blank">📅 05:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxjsdvhI0JG_x68FPPr1-PMWlk_oQCkiIRCOwkf7Bx3kO8U1ZyHx2byMBHC8esJ_I-TYegcTw88CyCSEPmKpmD1S18-qeC5Q5V-mnAYD83E4RtAwLCWKSoyf3bsKcWMxF1nnF1DBrZZfFlUshpDvn4juaWd1cllshZRY_D1RFpYDXbDsZ9A-ft_XKtcQRUQmJMMTG-s8LTgGnlqhcPokUeX-jGIYqzTZXSWzo8itOeLvfZbSkudIsUQtCXTL7WYK9IdFLdK3AgHbwyVkWqTDm6tx-vVJBSvt1HjXhChWIpynZBa6SoqvPD24T5yWxrqORSoJr67nwGTHh433fq_YXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایستگاه متروی شهید بهشتی موقت بسته شد
🔹
همزمان با افزایش حضور عزاداران و در ساعات منتهی به اقامۀ نماز بر پیکر مطهر رهبر شهید، ایستگاه متروی شهید بهشتی در مجاورت ورودی شماره ۳ مصلی امام خمینی(ره) تهران به‌طور موقت بسته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/446945" target="_blank">📅 05:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406dedb2b1.mp4?token=K-sJVKXzFNOfkSD5Zr_trg8EkMKJMxwFHybMLCdrYHj4PEsU3NZ-rPkNaDZWj7edqczuCJcb7C0R5NM7UOUC9aMMKPQ9bDxNi6pFsNvxYRAVbyk7cEjtUaz6RlH9ix_ochJ18d6AqNJ7JM6F9uqJtZcAeH5BkicbNOtmiHYBgdVll4gVK-ubLRiBQX5xAT22ERR4oIxEKNlQYqWma2PLEhLgax2DyUWXtOYjtIsM_4cAsukzz-jJ1ZNuFaUOT3iPD4VIU-Lv61JJgsh13B70oybYXUI_fxv_dNO5DEHtfDxitsqiB_6qJUwZq6idzuNit7TXDoKmQ_GKPgvW3TCTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406dedb2b1.mp4?token=K-sJVKXzFNOfkSD5Zr_trg8EkMKJMxwFHybMLCdrYHj4PEsU3NZ-rPkNaDZWj7edqczuCJcb7C0R5NM7UOUC9aMMKPQ9bDxNi6pFsNvxYRAVbyk7cEjtUaz6RlH9ix_ochJ18d6AqNJ7JM6F9uqJtZcAeH5BkicbNOtmiHYBgdVll4gVK-ubLRiBQX5xAT22ERR4oIxEKNlQYqWma2PLEhLgax2DyUWXtOYjtIsM_4cAsukzz-jJ1ZNuFaUOT3iPD4VIU-Lv61JJgsh13B70oybYXUI_fxv_dNO5DEHtfDxitsqiB_6qJUwZq6idzuNit7TXDoKmQ_GKPgvW3TCTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران چطور برای بزرگترین مراسم تشییع آماده شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/446944" target="_blank">📅 05:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d263632c.mp4?token=DaJpDhGon081zNN5oLuSyQO_o7_D813_7SJcgngGO4D7rZiDWgZYzWoI-jjZMIUItdo6NwDpsSrV3xEcOeoLGq_YuHEvOuCCK3N0Ndcn9quy6c6npN53C7nzkjuO0uhGvecpLvhnVUpivEUYUjbc3PIr7K9ne09sEgxRhKbs7wIGxdRq2FUPwaIYb93fLXve3jGWxIQltyYOgCPm5pHB8_8hH1s66Y12FYq1EXp7KeXYvY5Rs726i7Zai7B6e_-pKAq5NGOh430ExFClrr-aS5G_vdsWL1iMOH-eWgZ5kM81PPBkLzOztHiaikzHbXe52Hsf5NaHZT1lDH-EJPr2qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d263632c.mp4?token=DaJpDhGon081zNN5oLuSyQO_o7_D813_7SJcgngGO4D7rZiDWgZYzWoI-jjZMIUItdo6NwDpsSrV3xEcOeoLGq_YuHEvOuCCK3N0Ndcn9quy6c6npN53C7nzkjuO0uhGvecpLvhnVUpivEUYUjbc3PIr7K9ne09sEgxRhKbs7wIGxdRq2FUPwaIYb93fLXve3jGWxIQltyYOgCPm5pHB8_8hH1s66Y12FYq1EXp7KeXYvY5Rs726i7Zai7B6e_-pKAq5NGOh430ExFClrr-aS5G_vdsWL1iMOH-eWgZ5kM81PPBkLzOztHiaikzHbXe52Hsf5NaHZT1lDH-EJPr2qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خادمان مردمی: نیمه‌شب با پخت حلوا، دِین کوچکی به زائران ادا کردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/446943" target="_blank">📅 05:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6618208c.mp4?token=RHMrJAF9Lr-bxzzrJvIDpVbo9VrOlzQKoS21cPebCZtPdYdsg6YMmrgpM9VBb31EiDTBdOKLx_5zsmbEevqyUpAv9VOMFZnrvxamN3ve-IZnRON_EbxlKHmLt3fJWh91ICe81yDTDKehWpUMSVv1dRVaefJOucy6uFmTz454y10X6uz5iugUp8W-xpnFyxJlsiAmRXzqTE5Tr9DSQ_6LrbYaxpn2Dp7tL-sNZwTL4ftRmozrDm4tKmJcuVwV46usTH-JTJEAoGeIJg3ZOiDFhmZhW-ZqE5p6n3i5uOSsGmg_u4aDgaZt-c1Pn5Fz6Fnj61E5F0oW-8Xxjy64MzIysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6618208c.mp4?token=RHMrJAF9Lr-bxzzrJvIDpVbo9VrOlzQKoS21cPebCZtPdYdsg6YMmrgpM9VBb31EiDTBdOKLx_5zsmbEevqyUpAv9VOMFZnrvxamN3ve-IZnRON_EbxlKHmLt3fJWh91ICe81yDTDKehWpUMSVv1dRVaefJOucy6uFmTz454y10X6uz5iugUp8W-xpnFyxJlsiAmRXzqTE5Tr9DSQ_6LrbYaxpn2Dp7tL-sNZwTL4ftRmozrDm4tKmJcuVwV46usTH-JTJEAoGeIJg3ZOiDFhmZhW-ZqE5p6n3i5uOSsGmg_u4aDgaZt-c1Pn5Fz6Fnj61E5F0oW-8Xxjy64MzIysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حشدالشعبی تا موکب‌های مردمی؛ نجف و کربلا در انتظار رهبر شهید
🔹
از نجف و کربلا، عراق در حال آماده‌سازی است. عشایر، موکب‌های حسینی، نیروهای الحشد الشعبی و مقامات دولتی تلاش می‌کنند تا میزبانی شایسته‌ای از پیکر مطهر رهبر شهید انقلاب داشته باشند.
🔹
ده‌ها موکب پذیرایی، کاروان‌های خدماتی سنگین و طرح‌های امنیتی چندلایه، بخشی از تلاش‌های گسترده عراقی‌ها برای این رویداد تاریخی است.
🔗
شرح کامل گزارش را
این‌جا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/446942" target="_blank">📅 05:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1-LSwarpRyB43VTFVEgtBmBQncVlFO55xVymbzSBKRFH-mhHvUBOzujE-U8IGM0kki13ZQPcixeRgh--Lx1ywGQchu_4j8-yP2wx3G1iQ9LI2B1lE8MJByO3NI3rf_Psf22PVJvT56QwTam3r4WW9wvPfiTxG6fAesttHEaJVkr-pvHCsc4fVVDQXIKqBqxRBnCVAAc25rmQeT7Jkn-d7k6hltInA_eRc437UvNqzfvs-eDLT9qkY2UqqoaL8P7EGNWQYaGx3_PSulWtrPhkhszVjpBU3ylmHYQ381OjgnuBBX-trV29f0iqU2d0Lf9_gx96WldNTNqO-wA-dPzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مقامات و شخصیت‌های بین‌المللی شرکت‌کننده در مراسم ادای احترام به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/446941" target="_blank">📅 05:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10b2e9a32.mp4?token=GwFX4N6AOvugClnN63nuf8seaEf6WdA7yRHDXb59PAwt3FeChgIgKOo9pPe8N_HPWN593GnlrRKpw93S6dd2eHCgg0SwhpQZOV2TZCVrkVT0r_7vJjs3MAyLzikrU82qSS0miv6EfNUGkIYwqrosTYcwRhj6s3QPf7Aol0gR51LvFnSHJKWeNDsOsCjHMJ7OnQ0BodDls_TRYVOIBAOmKlSaxxniXFsqBKvT4QB7MnFCP5s7y54l9f20FcVAeujNdbaa6tUWZOxeue-22HRdUS4mjbDpSv_KcDk-wkdbDAzHdsIBteF7Z1Ozfdh2LBaBylCEu5hlm3p01IqT2FaQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10b2e9a32.mp4?token=GwFX4N6AOvugClnN63nuf8seaEf6WdA7yRHDXb59PAwt3FeChgIgKOo9pPe8N_HPWN593GnlrRKpw93S6dd2eHCgg0SwhpQZOV2TZCVrkVT0r_7vJjs3MAyLzikrU82qSS0miv6EfNUGkIYwqrosTYcwRhj6s3QPf7Aol0gR51LvFnSHJKWeNDsOsCjHMJ7OnQ0BodDls_TRYVOIBAOmKlSaxxniXFsqBKvT4QB7MnFCP5s7y54l9f20FcVAeujNdbaa6tUWZOxeue-22HRdUS4mjbDpSv_KcDk-wkdbDAzHdsIBteF7Z1Ozfdh2LBaBylCEu5hlm3p01IqT2FaQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مسیر زائرسراهای اطرف مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/446940" target="_blank">📅 05:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39e8f01bc.mp4?token=ehhf0elKa6A25yafZxMi2-bL0xV6-Zq3F6ejrBdtS3U20_mJ3HigcBzZlods1ETYyE7KSspd7sHoif6FzxcnQ_x5PnQWOrmoW1mIchY30OYKlc_VfarVoGnKmDKwkje26Jdx5PNMouXV0dHUjzQfefoFdBOCuI-bRJuSK0eyQaWd0wUhqqmb5Fb4vnWmbg9EfE6HnKk74rPNGEMr0QonpNYotftUvQRInEGmAJlJ5rXdvJPeGw-R0cmomvwbN80nqsm9HmjxB42D5FbRm0gU21ijJVLoacdaVQnb0aQl35LvPA2jNeg42dJKbN-TOSRDHTT7ewn_f3_d-un3h_29xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39e8f01bc.mp4?token=ehhf0elKa6A25yafZxMi2-bL0xV6-Zq3F6ejrBdtS3U20_mJ3HigcBzZlods1ETYyE7KSspd7sHoif6FzxcnQ_x5PnQWOrmoW1mIchY30OYKlc_VfarVoGnKmDKwkje26Jdx5PNMouXV0dHUjzQfefoFdBOCuI-bRJuSK0eyQaWd0wUhqqmb5Fb4vnWmbg9EfE6HnKk74rPNGEMr0QonpNYotftUvQRInEGmAJlJ5rXdvJPeGw-R0cmomvwbN80nqsm9HmjxB42D5FbRm0gU21ijJVLoacdaVQnb0aQl35LvPA2jNeg42dJKbN-TOSRDHTT7ewn_f3_d-un3h_29xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم حاضر در مصلای تهران، هنگام پخش صدای آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/446939" target="_blank">📅 05:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7e161249.mp4?token=ZUjtk0DMJ6z3y4bw5wehyKnecA0V-Tm_7gIDhehsBuqcn-G_wnadnIhQ5aa9QrFODpVkqbLjaw37M51qM1wmFPGWSCsQSsLBsF6vc1_mCrGtQsjAtdddA3p-V_eJOFZNqS91QH2eF4dN1FxmnuNUERPhGKPc6Ed-Ojfl70cr-PfWAHB7DxYjrois4SwGIqB-MOXQmI19ddQJXSm70m1osyA3pEx7Jkq5zPfjrUXR_XrMZCp3F_idnL8-dQheQ8SCuKB0qFwfDgo5f5WxCse-jOxQ_Z3oQ3SOGexikayKbgSi-Eg0Xpx0dfYmM7BuMJyfyOvoZ_lhkDDimGJOBQM2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7e161249.mp4?token=ZUjtk0DMJ6z3y4bw5wehyKnecA0V-Tm_7gIDhehsBuqcn-G_wnadnIhQ5aa9QrFODpVkqbLjaw37M51qM1wmFPGWSCsQSsLBsF6vc1_mCrGtQsjAtdddA3p-V_eJOFZNqS91QH2eF4dN1FxmnuNUERPhGKPc6Ed-Ojfl70cr-PfWAHB7DxYjrois4SwGIqB-MOXQmI19ddQJXSm70m1osyA3pEx7Jkq5zPfjrUXR_XrMZCp3F_idnL8-dQheQ8SCuKB0qFwfDgo5f5WxCse-jOxQ_Z3oQ3SOGexikayKbgSi-Eg0Xpx0dfYmM7BuMJyfyOvoZ_lhkDDimGJOBQM2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر فقط یک جمله فرصت داشتی، به آقا چی میگفتی؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/446938" target="_blank">📅 05:05 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
