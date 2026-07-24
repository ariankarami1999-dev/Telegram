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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 20:31:06</div>
<hr>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2RPDkiriB_WUbRPPJcZQGtUvOsBM0WylXl_BYW8NMCdxgSDZYVfAyhVhSSkrYKAlkJOi9xOGkcOJZtngKaEAGMZqlemrkte6sJeeN518U32hkbNBibc4ipjIZyefjtVztVnET-KpKcbE7H-bcTaTWB5YepXK2jcyYLlkvLDqEGEwpwmD2WI_vZ9BDCCFOWrGBCDt9BvXukF0yON_Yc0qsFZ8MXzVDs2m7TX-ZrR168TciGGDfdA2Oac5EKAl3q9ZhjcxVZSB9aGd5vM38jaJTxj1Tcpiz85K8sIvhZRxucHJdlvdYuqRY91iBoCt369UT80nEilyAPqSgl1PFtEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iINLIwQJOe-e-sTck44oowJ0GlZRX0H_oiga6eqDVqp1wBEh4RtHwdE-_hVODyZxzhOqu2091IRMmIVOGFS8-OBkLHMasdMVo-7enIhbwOJOqw5NGBsm-zFyTIuwz8pmXN6srgbXGTZ770eW4A5NOGDXRMOI7u8lwl8ZoiD-amnjhvTMUZno-k43QS4-JU_5TVhO0Ir9xwV7lF7d1_54g65wdKEYgFYaInSK2eWL2Tg54pe3f3wxYeDe3RpRohpVnSnUlIn33QQY7dg7QlmeiT21EmBllfg5CHke7WMCVWA71yCCju80pYU6-caOF8PZm2IvhaJfweFA7hfHLk7ZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYXKLhzNkBrgoZZCKmio6fvj-Y8l70W8Cy5mBW4hujzD7hopl1RyQ8zq_N9Qf28Bwem49Dsj_ZzSxZh2LbzeGad7OahnkoA-oM1IkcDu5Mq6NpS-RRjx-9GeozkUY6RzMqtG_2Gd7X5MSAHPLtT5OrKeIEwY5uJclwv7iMdNnyC8I1exK9glZ4OASidvipoZkRq4U9wqmUqwrYPiCq3LRAnz_hMJoOIybbommhh2A2-3-J6-qI_Uq4-Iu_L0MJoNwz5K4FJ0wYDs2BCIR1q9hzyP0kD78yJ38ujSbZCyTDW1w5hySZsDA3NeP6LmPv_G41H4XCobj7auC334uFnVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-e7s_oqzMpRSJx0yNYDL_KOGbYRHJl47Ayu5o135dtT0Ejf1Bl2Hu445h11tKqNR2QaD2N5_Wq4OQTguYnYpszvvxasj0CVCOIylp4U3bN-9-n6PyNREYyL2SOrZywSwFT3pH5Y8tU7OqYIVlsQXeKvteJhG4tmPnIBBzLg6qiadz477Vlm3IqZJEnvHc4qjeDJOIXY8hyoGTjYeBOk-Gtfc-X23ns-cSQhghGIUZtBiI9GasDUgqOTHNDZie_Z7NXC52T-wAgib6MT_Gtn43QMdW0drD69Sv_qmgt-pjn4xM3htVJn_KRbITklBA3WuuH3_px0Hz9YYV2WxLx4lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEZ82PqCAF4RNKh18RXaVEZeGKnZ2U4ccFZX_K-79RwlZ5yKolNZJef3zpqbcS_m1af6TLmAJ8qbkDUYIRcqtBw3Ft50LFGl9YDO7V2TrxrtjaEIKrnknWep3CGEKMyyBRk-Ln3xlxBi0lcyw19_6lf1DWA1v_4Zv-yOEyBPsSHxLvs8LfyaEaBtFQWZOFCvdMXnE63MWeZ2pd2_TGAmhFnoeE7vIozFoZChRywdh1sA0Jr2PPu_S2MiNdxC-WRitQtfnW5VP8A3h9R4gh8kdf6FZrNJ-32JVGHoh3adj4nrdkT-rJCrxD-t_LK4M43IqrBdrEDDJk4kea4xM7d8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1iLxnnGDs6ZsKIbz_j_9RNFnuCt4XLZpfguYvHGiZ248i6qZU_0BonnNqQbMeUiBJYsqpgO5bIzZvTVCnBwlMxXPn_56ogkq2-b8HEvbc0kpOhNsxFtKNohShV5NnRbjVShJASEWE2CnlhldfWBQN26M4AF64mHVaj3dXdz1mXsBkeHwS8bh1GrFMAwiGeFROGSnEarMW_IWTkwcD7Jtkz3gUzSjXiCeVkF-btcXVHZyHgP3DTly7N6lsebQdQcZzLCSm1MCyfkRSBfrN6uiHDrDhXD_GESD2meq8ewDYwBpBHuRmvXprakjsOZVuqQORGLFCrbqlbzAtm9Ldkmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=c7eBmwzvpDuuvFDzT3GZZ6T9hhmc6aMaBKM_vRQzSpf6GY1fpS50B10v1nieLL1RFPNY7kKxR0fBnB-9A6LqBtK-f3NWzrFlcGXEvn_ZKgLHJ2yEfR_qe5OWRZOrLLFqKI_hfJzgl_Wvcfkl-YQ8_RzyEIno2U-0ZlbezQIG-IlA9gqGy1tJ888r5RXi2p_FOMfBfsXADEBmsJ2xn_GSFdMYDkBxRJbeNU1NBU1gRXD8FlnhD7JM9Aqt3qeNoiiJoL7QmoPOAn6ZFPLydBU76Ouu7Cx_nO0c5VoNJdmID_UmctvdoIo4elUOsRthY9XyvdsCjxKxx96aDGymIW2Mhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=c7eBmwzvpDuuvFDzT3GZZ6T9hhmc6aMaBKM_vRQzSpf6GY1fpS50B10v1nieLL1RFPNY7kKxR0fBnB-9A6LqBtK-f3NWzrFlcGXEvn_ZKgLHJ2yEfR_qe5OWRZOrLLFqKI_hfJzgl_Wvcfkl-YQ8_RzyEIno2U-0ZlbezQIG-IlA9gqGy1tJ888r5RXi2p_FOMfBfsXADEBmsJ2xn_GSFdMYDkBxRJbeNU1NBU1gRXD8FlnhD7JM9Aqt3qeNoiiJoL7QmoPOAn6ZFPLydBU76Ouu7Cx_nO0c5VoNJdmID_UmctvdoIo4elUOsRthY9XyvdsCjxKxx96aDGymIW2Mhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Tep3cdORHfOmIemKo27RtHosPdO2z_QAlNQpE6yUZZI1day7xfTitXmtp6U-PNm4k9C8eOJuv_WzhCO6LNutE_lHRZZAKNvGSu_0xxDuJ64b4DCiLf-MkzWhpch-T3oN_iusw6wSqlMcS83_BUcRWEN2NazPQ7M_BWsqZWCwO45XBLRtTRAbmLhZW2sc3y63TsfxBf9Qp99kjm0_e45XrV3z7axcZvHiaPU93IPuzQnPPxI0Xr7g8e3cgnZxWu-Ez1b6SUvwHnJUM6lI49rzMdNq544Tsi4yWA5MoJ8y2gipr1l_RoziHqYr4f1AEqMxZJ099FCshSrNYZdKBqljIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Tep3cdORHfOmIemKo27RtHosPdO2z_QAlNQpE6yUZZI1day7xfTitXmtp6U-PNm4k9C8eOJuv_WzhCO6LNutE_lHRZZAKNvGSu_0xxDuJ64b4DCiLf-MkzWhpch-T3oN_iusw6wSqlMcS83_BUcRWEN2NazPQ7M_BWsqZWCwO45XBLRtTRAbmLhZW2sc3y63TsfxBf9Qp99kjm0_e45XrV3z7axcZvHiaPU93IPuzQnPPxI0Xr7g8e3cgnZxWu-Ez1b6SUvwHnJUM6lI49rzMdNq544Tsi4yWA5MoJ8y2gipr1l_RoziHqYr4f1AEqMxZJ099FCshSrNYZdKBqljIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKHiwW9xeZCOxnAZwlsPDjPWjNpQ2owyTPbesA9iZFzCR2nymI9Yi53ZTWo5kHJpzJHAzGOP7DB7GI7PVvZHHm9lrYxGItaVUwV3t0TOKDEbjBaU4IKD1BbzzGM8esZKDD4VAvraR0i-ZK_6pAijMh54QvGvQfxMMLhPx-3FlLZlmDJ5inzsUA_4V3OklPPcoTCY-AxLBoP6ezDPAv7zg5FYJfsW3LFiyv1vC5N4Ho0Cix2vAXMMR4PPFH_qwSSPpH-s8m8ZT-SD1UqupKPGS6vp6ZiSC6pDLO6b_Laq-FZY0Ax4FFML2JQfzLzwknnxcj8vanRgb5UctjbUZiQ6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=KB663OVx-OS5TFXI_6lRxTYV_OolzPov5pvfrgI7oMfjntktrNAU7APXa9s5n_Pm6VmTPSovSifJWskxMtrIz70WcMHJC2XPhbyewQQok70jG6jgd_I_1IwF-PtZP-xKcjDl6ooyrMsqxmYGBUPCLVIrzgA3I9MvKf8PiTn2uw-Ttu6-PoItGgLCUslFo3T450OK8kMN_IPBOedwj8N7QHkUP_kWXXgOZ5dDczOWlkwNL4L4MSsyFq2AEkjrgJ5PQs3pHJ9J3_Kcg3Vzj9THA8UT7HNCfZoM6PyH6xjp6ZI5sremnDJAz4XV4fbrMrce9K15BTEO7NzfcxfifivyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=KB663OVx-OS5TFXI_6lRxTYV_OolzPov5pvfrgI7oMfjntktrNAU7APXa9s5n_Pm6VmTPSovSifJWskxMtrIz70WcMHJC2XPhbyewQQok70jG6jgd_I_1IwF-PtZP-xKcjDl6ooyrMsqxmYGBUPCLVIrzgA3I9MvKf8PiTn2uw-Ttu6-PoItGgLCUslFo3T450OK8kMN_IPBOedwj8N7QHkUP_kWXXgOZ5dDczOWlkwNL4L4MSsyFq2AEkjrgJ5PQs3pHJ9J3_Kcg3Vzj9THA8UT7HNCfZoM6PyH6xjp6ZI5sremnDJAz4XV4fbrMrce9K15BTEO7NzfcxfifivyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=SzI2bylMDEAPwtDZZrbbfYm9cIcAM7Zzy_z4p2AzchKFdsCd2NgzrO3WWYTvrLCDxOefREjbMQLXS-8cW90v4r6A4aNRU_TBxfjwFdxok5Ii0W0VIiFON2VWJimbdrX4-3O5EoW9Nc-SfjlAWZkcwifONOMrgIubicCGAFm0xkoHzw6wr96V7knKfE_JZ-Mnyw_nmRdL8URH4kKHMOUrEA_dGEg6zLDoU7AueKdToY6k2Gku7_g5TEmJaMMR56H_6h-QMLJEy1tf6_Ky7UJDvCqdIMa7rRq8QZA1frhIAe8dm8CbDkvzZLqvf5nzqEyDW2QlbFrwQ1XCD5WmZcoCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=SzI2bylMDEAPwtDZZrbbfYm9cIcAM7Zzy_z4p2AzchKFdsCd2NgzrO3WWYTvrLCDxOefREjbMQLXS-8cW90v4r6A4aNRU_TBxfjwFdxok5Ii0W0VIiFON2VWJimbdrX4-3O5EoW9Nc-SfjlAWZkcwifONOMrgIubicCGAFm0xkoHzw6wr96V7knKfE_JZ-Mnyw_nmRdL8URH4kKHMOUrEA_dGEg6zLDoU7AueKdToY6k2Gku7_g5TEmJaMMR56H_6h-QMLJEy1tf6_Ky7UJDvCqdIMa7rRq8QZA1frhIAe8dm8CbDkvzZLqvf5nzqEyDW2QlbFrwQ1XCD5WmZcoCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjdeN14fwjDb6eEGr81w6EGWot7j23Gv_YQmyPczkZxBIH_qfUfYMvUcsx9tjNFvBBAyi49zsenmSeB7kbuwXK7ZdgRT0WRHxuayFCZq5au0cUN9mS8MiWB7VCovVjZO0Jxmh-dMy1KJt6SIrrkyVEpPoeXMKSifprY5oGcW8FF9wX_uOpM5VhoVMp-Th1YRNG3TyXrDVLJm09FNM0_sEvA_EBqVVQQFrPpl8DlpIKH6KtB3uww1jD4udFzld7k1xBY1h0YPpbAwoskVSO3qxQSaRKdm2CUGPCXl53pAd6-jois6ANMU0Xnl62Vhq3e59CqlUqF79bfHsaKF_ZA4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=NWvX34RSaOcB8wJJV4Gnyl6t1zJnZFMfRtIrIF0wF8_ShJ6a3zLbWkj76S_0MctqP9sS9kPNJ9vzCxaaOANTtVeJQzWzMudZUNfMIHifGdJzxJfVt5Y1XxUkArt0doTzvgWAVNb5TigI6tiLYBc09Pyu8n4ZjWkO9CeJD-_6dcS24VtdeMba2nNk4gmH3QYnQdkDvhUIDy4JMl7FnUEKhZSb6jwUBd3DKMEoXpJ0kdwMPd8QFzxTdxMqTEgzko2VJf70XGdz-IEgtL8xXz46TChPiYP2gz_f_j6RqQxMY4gWBk0weNzr9WLyjhQPZgfXBs5bU7uCqo0nSO679flR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=NWvX34RSaOcB8wJJV4Gnyl6t1zJnZFMfRtIrIF0wF8_ShJ6a3zLbWkj76S_0MctqP9sS9kPNJ9vzCxaaOANTtVeJQzWzMudZUNfMIHifGdJzxJfVt5Y1XxUkArt0doTzvgWAVNb5TigI6tiLYBc09Pyu8n4ZjWkO9CeJD-_6dcS24VtdeMba2nNk4gmH3QYnQdkDvhUIDy4JMl7FnUEKhZSb6jwUBd3DKMEoXpJ0kdwMPd8QFzxTdxMqTEgzko2VJf70XGdz-IEgtL8xXz46TChPiYP2gz_f_j6RqQxMY4gWBk0weNzr9WLyjhQPZgfXBs5bU7uCqo0nSO679flR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0saKQcfgx3UbOFyHWuDhgH0z_NuIJK7w7zbm3-MSgVamSEAdCXoZ_hecpg-ValrJvfEKp1d9KeZgpD0bYS_6QkoL-fz7Vm_tpUvOmk2v5O4xIG7cYD2E1UJX5TyMVXNUkgFyJK_BVtLsQUAXOypyEPhjHa5cYaU_oGkA48_21yyNJif4IvYwhnc70pp4eJaH9sRaCowQlZX0r_RLrpB5PE_diEdYOR7Bx8jqNAQ17gnKMcOyhaUjS1jyMtoDYV0CrZpAnqjxMhmEhVWUYcw8MbD6bEf_5fSgTQwzROYgUpFagm4lxw7GGANTkPff_08E5ZcV4ooyReqGaacYNhKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=AwuAXD5X8NbB6uHWMULl2MYLxL6z3KunJadseBeLaqyaub7XUxl_wAaz-YufHWYO7xaQFI4DI8TmVF20ACWInWdT07OrziJ_5J3HdS-VhHQDL37ZpN7xR25BPBQ9Kvix5ZoKRMz3wBj5kwoFEeBcqh_1vtw_crM6ElMEoBgl6aAbyhWEKrZbmzVsKCDl2q8fG8JU1osBbG_T0yG0MitiaxL_J_k18TYPvfYoWEwE1s7sOWon0XkZKsJA3RkxOjHJIhJNVEJQ39Wj85l-oMkRyGf4UD5QOoVqhgUyF7nw6NvwTmA1IdGOOyRjQ9gE3Ta7XcV5_rcHLiEOieBkB69VSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=AwuAXD5X8NbB6uHWMULl2MYLxL6z3KunJadseBeLaqyaub7XUxl_wAaz-YufHWYO7xaQFI4DI8TmVF20ACWInWdT07OrziJ_5J3HdS-VhHQDL37ZpN7xR25BPBQ9Kvix5ZoKRMz3wBj5kwoFEeBcqh_1vtw_crM6ElMEoBgl6aAbyhWEKrZbmzVsKCDl2q8fG8JU1osBbG_T0yG0MitiaxL_J_k18TYPvfYoWEwE1s7sOWon0XkZKsJA3RkxOjHJIhJNVEJQ39Wj85l-oMkRyGf4UD5QOoVqhgUyF7nw6NvwTmA1IdGOOyRjQ9gE3Ta7XcV5_rcHLiEOieBkB69VSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=P_EDBXjqd89EQwEOqSTTPKpBBloIa_zow-rzDAOP-USgTaueJu6-hdGwFuBASi8Ehc1jbL9bUxlSJ2tnqJNNtiq6ZxoNMCMbd6xlAZ3Ioe0hgi_EoNCOzZZYmImHYAOlBZshi8Hpy-JbnLqdTRfKEe9AkMap6H2JFRNP30K1r2pn9eaPCB43frVTU48PzJ258jbrB37ktKJ7uixiDFAiAuK_UNS484nfr1YG4kGHpEf6O9Qlm6VCR6WfxWF_UEAua_SewUH4zSyzMfAMeD-80ELvGGmB0-5bcRL6mnTQHZdgmNtBzg_LxfLHdjgbsE7ZIrDi3lQi_tO2hM974TRpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=P_EDBXjqd89EQwEOqSTTPKpBBloIa_zow-rzDAOP-USgTaueJu6-hdGwFuBASi8Ehc1jbL9bUxlSJ2tnqJNNtiq6ZxoNMCMbd6xlAZ3Ioe0hgi_EoNCOzZZYmImHYAOlBZshi8Hpy-JbnLqdTRfKEe9AkMap6H2JFRNP30K1r2pn9eaPCB43frVTU48PzJ258jbrB37ktKJ7uixiDFAiAuK_UNS484nfr1YG4kGHpEf6O9Qlm6VCR6WfxWF_UEAua_SewUH4zSyzMfAMeD-80ELvGGmB0-5bcRL6mnTQHZdgmNtBzg_LxfLHdjgbsE7ZIrDi3lQi_tO2hM974TRpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk96nmqqUQmfkW_suNk9XCAwaL0NR75UIjeAUr0JqI_fa04QMg9SgSrx3au0p0t3zdfrPWA3qlQwzfPv6CPSL6ilepEgJm322ZNauLiwyOTB5rpZkfClx5U4Eo3M5m0SC2oJt2kt9A-IhI1tl9AyIZZRP1fTx3Qn0RIomPkS_nL3gHdUqyGRU-0q6wCD_bZfbzKg-YrFuYF_xi7KChPvlo69VboHOc2rjzrOtupiBF8eBqp4O3tzcrmlVMV14ZofK0TXDabeIPhmLxJXWRIRYSZ7o3Ss9ckvAL9zwJqIPhHCjb4Z5bpa-5cERYNlxjtf-Gv_j5DFHOl5rSk8EXdDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IXJ2Dkc7YFxH7Bt2mt9aVNcxlGq3V14brZszr3QLb0Wicm8p9IV63U74_AlE76cqvp7CF7bGHTRKDO7fM3JENswEoDlqm2qDzq_VXTgBNDM6VGz43tmqC8JVlLhMSUA4o3DT58_0d6bsNMHxsh0bI2SNzfRROE5RX-5w0DXX1mGYqnq4hNrahMvAbsAMRZ3z9T2s0AiZOEIeMtXIjj-7WhUYDGqxzFUl3jr2mZ478bt7hk-Da6o_UIusq4F62R_kChBqtfYiktquQjDhyqd2Fgmu_GFtr-wJjC35YZfY22FJTxIXSq7ItMz-UolyjhnYZFscW_A7C8amEY5ATyfFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IXJ2Dkc7YFxH7Bt2mt9aVNcxlGq3V14brZszr3QLb0Wicm8p9IV63U74_AlE76cqvp7CF7bGHTRKDO7fM3JENswEoDlqm2qDzq_VXTgBNDM6VGz43tmqC8JVlLhMSUA4o3DT58_0d6bsNMHxsh0bI2SNzfRROE5RX-5w0DXX1mGYqnq4hNrahMvAbsAMRZ3z9T2s0AiZOEIeMtXIjj-7WhUYDGqxzFUl3jr2mZ478bt7hk-Da6o_UIusq4F62R_kChBqtfYiktquQjDhyqd2Fgmu_GFtr-wJjC35YZfY22FJTxIXSq7ItMz-UolyjhnYZFscW_A7C8amEY5ATyfFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=Iowh-pU6km_1iCzaeqs8fetfEzmdnyinZvQoxuRSDPQLg7eLPQvAU6guTC2DyzPyyPfF4aaM7gs-GieaidHrUz4lKQD9XooqcI9f_4opFr5KH1kdTlYNrgHtPMYB1m4M_qaFUTimwmbKvN8QMoQeDg6cMo25bqm-T3avYxqw4gtvWMRB3PCZ0o3d8GMc7VWJQHIIu-puhdNSpU1h53L9sqFoybErVzIoYKcKxqpJp6OlCrbWIOx926xSCgr5tZlXansWQ-WSxDUiTblq1QoUhS1Dw2Qn14X5PcRapunCux5Ctq66m7MULHBXM5foUDJnGktMVtKXoQLEGZbhz-mPZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=Iowh-pU6km_1iCzaeqs8fetfEzmdnyinZvQoxuRSDPQLg7eLPQvAU6guTC2DyzPyyPfF4aaM7gs-GieaidHrUz4lKQD9XooqcI9f_4opFr5KH1kdTlYNrgHtPMYB1m4M_qaFUTimwmbKvN8QMoQeDg6cMo25bqm-T3avYxqw4gtvWMRB3PCZ0o3d8GMc7VWJQHIIu-puhdNSpU1h53L9sqFoybErVzIoYKcKxqpJp6OlCrbWIOx926xSCgr5tZlXansWQ-WSxDUiTblq1QoUhS1Dw2Qn14X5PcRapunCux5Ctq66m7MULHBXM5foUDJnGktMVtKXoQLEGZbhz-mPZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG6E2KTNANwP2pi7OhrBJeb5j8Ux38-w3FesOkIrkb4xP6rFyE69Fv58r2JxAFiai0tAmuuzsnwy1P-1bfH6QkxlYSvwramf8mVOzEFwPTCghp0t8UccZodEDdkx2mq5pE-Vyaap3-GyXSrDAQSnK2cktgHOS6f9z0g5etaZXCvj6IyWzZv6VJkLRW_Ikyv3tOPOPVMGhPC0eqUS8-vtInACCWJz6yxy_Ca3L7a7Z2LYxDSsCulah1CTy1LZA143dqa3nmOGLZ54ElHE6UuiGrU85yAzyPTxPDn9XBYJCPueoTG1_rm4ZUn0fG5tjliTFFnCs1Slw_Eny5wiA84c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvVFwMYaFlKbhPft33AErCNiGj_nIY45TW5Vq9LUcmmC4tOcaH2hwJ9sGPkYAXCqIxV3u3kbI18rTuM8iRkLFk11Xl3kjRG5tHJkzHftjcSeR14Y77omHMEVPVAMpwi3eGVhmXltePpVrakYMRBzFE1IOU2m_e_WxSeij_yzqbJRCndoC2cmXTMSRH0aRl8j9hCaRaDKZSeXVvpbOTJCiaelLCApNe7AtU4fR1rCZZaZZHQqdinJNkgc1Nuee5v4RUjh0XFIiVTGAIY-BFZiBN53D8dgsTGHfuMN32zSyAQcKpAmeKfBXcUpxN0NSCdaH4Y0QYiJNyV3-zbAJhyaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRWiqleJZ9iYXlokUO3N624evVNIPlFppJqRg2l7vroOJXgHlZT-oEhvdCltUHVPiA3-DD-HNgjAwWmPb8zNT50SW7DeAfrSxibq2AK5AjxYDsBBcpaumOJLPjzUWdukxbMTzHomcpWBwbCRFI5SkCB_QNwmP6HTzMMSAQWGmRMZX0iaEE3rtLsrb3IcFnjitWtMnAiV5-91D_q4x9VTvJeUDusIo_rsIxdgfHB5sjIBJnAirpOFKD_qP0XL1STnOHTgu1F5ptmEwxyCq0poTwwkfB6Tci6atla3Syf0tiANzhxwFqQOzjUQ68mn0OGW4D5K70N0UHXxoTolIjY4VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=tz8dk154Ms-izqilr5uCyYALD9qYHGkT2uq_nz614937GZ-hPWk4f2v-XaN-s_ul3ffcA0ak4khDH4ldvtVTj7h5lhtIZGH_c_LLDi8sxFjCIAh5LXsiGDvTZ3-LtV7iUIkz-H1H_NbfA8RzbMQ0fr4NWDmShqOvnJwHF1S7mzrYIHsxICdgppYoUU2xUqoI3nVwlEdRsLKwLyWos7nYLs32iHIpVAeXqX0YZnFblMqTRyczQ1sf0EnE0h-K66CuqC9orkHIghUvV7H1us5z19aEDHnK1O_97x4GhoAsZ_WciJI9U4cfZNcBw9zCdT0sosPdSMzovJ1REjl4B3NhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=tz8dk154Ms-izqilr5uCyYALD9qYHGkT2uq_nz614937GZ-hPWk4f2v-XaN-s_ul3ffcA0ak4khDH4ldvtVTj7h5lhtIZGH_c_LLDi8sxFjCIAh5LXsiGDvTZ3-LtV7iUIkz-H1H_NbfA8RzbMQ0fr4NWDmShqOvnJwHF1S7mzrYIHsxICdgppYoUU2xUqoI3nVwlEdRsLKwLyWos7nYLs32iHIpVAeXqX0YZnFblMqTRyczQ1sf0EnE0h-K66CuqC9orkHIghUvV7H1us5z19aEDHnK1O_97x4GhoAsZ_WciJI9U4cfZNcBw9zCdT0sosPdSMzovJ1REjl4B3NhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=XEZ0KvGcIl388FOsmejLLZspEJUh1juF34ebRof-o40tqVUgCI2OOmmYDBuIXk-J66pZGc5av-BPlZOAuV3zLxVPyvYvwPDQ64q-DFDPdHOT1wvbB0PKpBwiGJ2WCmX7x40BT3YJPFnBAtwfaJ4uJAdYQgXPhe_12jG7W5tTOgBPJgBEums1Yxks5bQOdRCYGToniYpiS2fro57P7k1NjRrnx8_6VnTkzD-wcIGdL3JjhUeL00TDflX2YKlkASpgCT29sU7hqS9FtVtRqzA0aVuR82-ZnBpAJaqEoo-YELPXib3QSWjAXKUXNNyXAVbi7eMepPIUJM4wpANSyRy8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=XEZ0KvGcIl388FOsmejLLZspEJUh1juF34ebRof-o40tqVUgCI2OOmmYDBuIXk-J66pZGc5av-BPlZOAuV3zLxVPyvYvwPDQ64q-DFDPdHOT1wvbB0PKpBwiGJ2WCmX7x40BT3YJPFnBAtwfaJ4uJAdYQgXPhe_12jG7W5tTOgBPJgBEums1Yxks5bQOdRCYGToniYpiS2fro57P7k1NjRrnx8_6VnTkzD-wcIGdL3JjhUeL00TDflX2YKlkASpgCT29sU7hqS9FtVtRqzA0aVuR82-ZnBpAJaqEoo-YELPXib3QSWjAXKUXNNyXAVbi7eMepPIUJM4wpANSyRy8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/papDr0U58z5J8e55kWU9WeEKguXYcK7y_uys4meAk2YROofjODyuxJ2fcSizxQzia9xbhoQwj2s7NwkC3gE5EqmcEMyi2MuqGorjlcR4yNjqHmRf20w546NmjYwPtFmokTPdggK9OlH31lSPuPeb-eOklp2XtaTFw_uu7PIeOCovhcqkJE1wImNEwX-F5E4z40XjRsAiqu5OOZGHSHfocEdDbJLv1LUrG0sB_kqyjWNV1lWYHbDhPr4XPccWIHG6uFlANAcPawasMZntF2HhhxY6f08pWg15Bi_EgYFDs_wOlF2JgoJVjEQQJw0l-cvsTmkfAbsD8BoTpY0pllqlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=Gp5s7MU_tQ_sMhg9la3ADsxgnz_t9od1yt5hSXPH8SbQoQ_N_98LlUlFH8Azt4PIq4-gp8usHu3ocTR_pyRTQnAJGfeV17xhKTCILLse9L7A4qaSNh_AA2vw3D28E8skPQCfE2pt2CJ91MkoFJN4EilTTL2o54d_3FwQ7L4redxUXcvyMlqg7AyDXtEHVGq8y1_kI4_8vmUeh9CEeAjLyfTj69jiyE_tgv3s7eRyLDq4DO8ZWHBUSCFbOfkYkGuMvyQghVIeJdfzHOhlkN3Bd3ZCgCDFcUkta_k04kaS_I5eOojuMRwb3IvnZaH0zQ_shbbu3hWMCscyZ_Tf6kHyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=Gp5s7MU_tQ_sMhg9la3ADsxgnz_t9od1yt5hSXPH8SbQoQ_N_98LlUlFH8Azt4PIq4-gp8usHu3ocTR_pyRTQnAJGfeV17xhKTCILLse9L7A4qaSNh_AA2vw3D28E8skPQCfE2pt2CJ91MkoFJN4EilTTL2o54d_3FwQ7L4redxUXcvyMlqg7AyDXtEHVGq8y1_kI4_8vmUeh9CEeAjLyfTj69jiyE_tgv3s7eRyLDq4DO8ZWHBUSCFbOfkYkGuMvyQghVIeJdfzHOhlkN3Bd3ZCgCDFcUkta_k04kaS_I5eOojuMRwb3IvnZaH0zQ_shbbu3hWMCscyZ_Tf6kHyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=kPvz6lUm_qzS5eswg76MIpevlZbFVfoLkDhiwHY6HqRvyKxpN79MxABZYtymlFUgH6AkNkR9BLICHqerEagTTVHIbZeF1nWXqxmtwYAVT7jgitvAJIJUf3tCyCHgJ_pHIKQFyVERBL2SFVAJYphkjxRD0VDmdkAA7MMwoSRnMM3oNHDQMI8SABBzr5QjUOXb836bLtVHl0uIKmUYc7kBnSZDPUs_Il_qUirRY52eHpeVD44Sd2EmUt2IL-oq9O4eUylGuU4voK_nBVN_9IVr2Aktbx4RLQWDnM62p-ODWszkkEJoS7FFLCZkJyl1RPZDH2Z8O0B_uBc8vzaHbOQRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=kPvz6lUm_qzS5eswg76MIpevlZbFVfoLkDhiwHY6HqRvyKxpN79MxABZYtymlFUgH6AkNkR9BLICHqerEagTTVHIbZeF1nWXqxmtwYAVT7jgitvAJIJUf3tCyCHgJ_pHIKQFyVERBL2SFVAJYphkjxRD0VDmdkAA7MMwoSRnMM3oNHDQMI8SABBzr5QjUOXb836bLtVHl0uIKmUYc7kBnSZDPUs_Il_qUirRY52eHpeVD44Sd2EmUt2IL-oq9O4eUylGuU4voK_nBVN_9IVr2Aktbx4RLQWDnM62p-ODWszkkEJoS7FFLCZkJyl1RPZDH2Z8O0B_uBc8vzaHbOQRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__HszlBPtApf1Lz3N8qNgzwTTS8KmQ-bmKScrAUBq5u_io1eC2TWtWWJELHIBlpk3RO3Qf9Co5tFK0JGH76g6c1TO4vUpslwHy3AHmEV0uHnfboctXyVvI0tmkSU32n_rXCHQjv7-SnwgxiCz6iy_jgvxcRh9PQBJN9YM6k3sAGAzibgK4FHFttIEkz_dPrJbKu6jUU-aC_IL7cPWW7052A94kpZnLQwsL6Nzh-MhZXpWHnnMQZ8je_uS7LwEFEKFwQqKbOBeZIAthc1fwqUjDhr9HAx1yax5FWcC_OFpnpd_0oPyhaRCd7CL2U5mzeE6Zl2nxOqnUnuxN-qrvU3lrr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__HszlBPtApf1Lz3N8qNgzwTTS8KmQ-bmKScrAUBq5u_io1eC2TWtWWJELHIBlpk3RO3Qf9Co5tFK0JGH76g6c1TO4vUpslwHy3AHmEV0uHnfboctXyVvI0tmkSU32n_rXCHQjv7-SnwgxiCz6iy_jgvxcRh9PQBJN9YM6k3sAGAzibgK4FHFttIEkz_dPrJbKu6jUU-aC_IL7cPWW7052A94kpZnLQwsL6Nzh-MhZXpWHnnMQZ8je_uS7LwEFEKFwQqKbOBeZIAthc1fwqUjDhr9HAx1yax5FWcC_OFpnpd_0oPyhaRCd7CL2U5mzeE6Zl2nxOqnUnuxN-qrvU3lrr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPnvjpUpRHlhYz0bewNjor92E3I613uxHSLTe_QLvDmL4ugbB3qx7BlcYr0NjWDKin60cg4n04uBTQxwz1t5tRCVd2FVxQbBvcGcEdqiNjjE71DGqy7S7VdDwbnJF-7qDj8lIHcxDYCnLC3KtzGM_DbkJj5qiUpDF7DbxTTuLxHUhVEWyXdbqyyT96lG1T1cw-XTabhRzXe2OvHNnTO7JNdPlHF8pi8HVAYi36LWqHXp0TbO0Qi1vpH6PK_XkjKBmlrbg3ue2LLPwI-D7jrkL5VM1rM8GPuZ9p1J5etd_EINyyeUHcOvl7zDlpsNuWorRrPEhtAUbgu8vRk1YDNTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eulv_f5758bXOVA7blICOuoI3iU_61dcMKA6pS-4qSskl5wln5_6h0BM74xpDuyaaAjx5FdInG1GIDO_iQcScUbWfpYVJ4SVkteMt-lJgCv9hH0VDf27UMecaP5n26c5EloBXjPfcOCDgHz7hubqEU23PvEbBXPAQ_PKOznw9bEdA3jApaz4kzBtSHhTaSRkO6O-_-rqqOiazNYkpIM16_H5wOOVPLIifBOJvrqZXwckFNRMcsUMq8kAc7KHhEOGVnfO3EnWrrbpDb9rlrRQ83_5kjKBdVUhfaYFWO7YMi5Gcnb_L14XVThqkhVNw2W4rVZQB_lK5Nwt9FhfICBpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=S350C9tvFlu5lW4vI06aLxsWyS26YvFUMUf8YHCtq2q5gediX_3pjLfq3FiBrQlvVSvbJUXFOS63bDH5g4fIu1ZimQSsqXuq8spAHqQyJFYN6wK1eoyqOCsJcDdmC6pxThukfQOqYQLecyGtPuq2Z2a6Aiyg19ugKhCYZAX7jSPcc6Z10rZfomrrzU5bti4sSBBvG6HYvR5a-c6354ijD_COKShYhWgiQGNEUFNVCr1klgOEJ-8AKL7zDTdPuNdJEDQV6WcSR2a0EU03xbWhLxjxtzisLR-gd56rJhYAmef555HqJcoxGrVloEahJHXh1ED5SE6Nn5jtgLH72MYUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=S350C9tvFlu5lW4vI06aLxsWyS26YvFUMUf8YHCtq2q5gediX_3pjLfq3FiBrQlvVSvbJUXFOS63bDH5g4fIu1ZimQSsqXuq8spAHqQyJFYN6wK1eoyqOCsJcDdmC6pxThukfQOqYQLecyGtPuq2Z2a6Aiyg19ugKhCYZAX7jSPcc6Z10rZfomrrzU5bti4sSBBvG6HYvR5a-c6354ijD_COKShYhWgiQGNEUFNVCr1klgOEJ-8AKL7zDTdPuNdJEDQV6WcSR2a0EU03xbWhLxjxtzisLR-gd56rJhYAmef555HqJcoxGrVloEahJHXh1ED5SE6Nn5jtgLH72MYUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_WtZz4w3lr_mAQhwpudlVQmDRrTBOVI4TBs6jtT2qWFxXHx8TmbPbqHrlVd8cqyAbr-LlLtTlUL0CbaewANrOElwbV3QsT5RBPJZ9o4-RTT_3DkVa6NZ_RPuZ-GGRP8hrshEm3yjBdOYMjENwfpLxMk_Xw--9WtyOcbslkGWuleS-F77TeR-mUxN8iIIfwmBxJaror9q68Kk_5esiQpwVNS53x_DbK_U7icBrwxVUHdyOfUmZCeuAydo_a4OYsUkupBO80gGMUw864ywGK3fLPxB5LUnyos9YU6rP614XF1UW8yhk4NK5chB0xxf_L0Hw1GZ_AJ5UQkjJSYfYQQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGsM9Cz9k-blfz2NNQjhNMVbI76VJONC0hqHjiapqlfTJk-BGkPtXOSSj5cVekxGZ9-1w5A-sMaF4ihbTrT16HgbgzKoXORPMDX5bxnxxg8eofakDzNspZRa0abDWooES8E6k3T5L-jvBsDjw4dqVUiwAP6dbxy3iRQLAqdS7CpMFkz-vzwHwvX_K8iGqvEBWoUWd2FmmqFh2OH37VsqfHbowrqUU8vWmw7Wl_UvFAWkNZ63Xjsq_bChPxYt_O2XodpugEl-KSck4p9wvOE93X4ucYjs7uxmIEr1_URjvJl1cW1TYwTWm0zw0p3NX1Zh6WhEn3FwMcGvLZjsMZurCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=HgzmHTZekc9tXw2jlcvJQpftpxD0RSTAR42crZ2Og-WpZHjxEv-pjLsNlDGCqZut6uSgn2PRWDj4TIRlckSNVC8hVTYqBmSRm_twD3l86auNo35I5eTiTCa0QETA_VBTZtVuQhQh_ZXQRv3rNghuCBWeQ3CpPil_G9hXYez15saanOyDjHXaPy_GfFQeS463CWvg0Y-i5c6Yeu2tra696klrDev2ZiIWLn6PPlRc2y4WnhQFs_Xd91OgqWwuQxfUzGF17hrsAuk1xBMhYALqRUQslwcyuzsXo95kFwpd579K8v_gKQ6a9tSSribxYZ6llUkVYyxQqRJfBapcekCHwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=HgzmHTZekc9tXw2jlcvJQpftpxD0RSTAR42crZ2Og-WpZHjxEv-pjLsNlDGCqZut6uSgn2PRWDj4TIRlckSNVC8hVTYqBmSRm_twD3l86auNo35I5eTiTCa0QETA_VBTZtVuQhQh_ZXQRv3rNghuCBWeQ3CpPil_G9hXYez15saanOyDjHXaPy_GfFQeS463CWvg0Y-i5c6Yeu2tra696klrDev2ZiIWLn6PPlRc2y4WnhQFs_Xd91OgqWwuQxfUzGF17hrsAuk1xBMhYALqRUQslwcyuzsXo95kFwpd579K8v_gKQ6a9tSSribxYZ6llUkVYyxQqRJfBapcekCHwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Zz53PCjch_0rtt2ot1G-ByFjhFMg8jChZ_FtUWSpjnzk58X0I6wCgLHskWpiH450fyxApxRSQjRH9jAhoCtQkqyVQGRu-NkcFbDUNQHUBH75Mc0AP3oOplIab_Tl1y-UdgiMThoZ6nx_DDGEec4VG2thRtNns2dnCZ94lWWneduygmtYbye9hxFxg9IJcXG14F2VRL5AgmMMZJKLef6Qk-x54Yy-jdWNKu4q1NXwjBQgWq7WOmV27wE4n2C-JBmvutVw8x5log4pyosDM2Kl6caGllTozp9RFANs7IRmXHT3FsVVgPC9c9LIYoPpPrckBMALnZ-NYgoSesEGGMjX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Zz53PCjch_0rtt2ot1G-ByFjhFMg8jChZ_FtUWSpjnzk58X0I6wCgLHskWpiH450fyxApxRSQjRH9jAhoCtQkqyVQGRu-NkcFbDUNQHUBH75Mc0AP3oOplIab_Tl1y-UdgiMThoZ6nx_DDGEec4VG2thRtNns2dnCZ94lWWneduygmtYbye9hxFxg9IJcXG14F2VRL5AgmMMZJKLef6Qk-x54Yy-jdWNKu4q1NXwjBQgWq7WOmV27wE4n2C-JBmvutVw8x5log4pyosDM2Kl6caGllTozp9RFANs7IRmXHT3FsVVgPC9c9LIYoPpPrckBMALnZ-NYgoSesEGGMjX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEHiXSQ6OXeEX_g_49zdJn6D_4CkPB9RTzEKX0QqgTEsMKdUJmvhmSgzltDKLxo6acc13iVYhrT08iX2aXh1Jg77uXaoZLDvMexVSwbUXncj5qDKsH-kUu5fCHC7odWWNQ062Gfv8DpwWBB8ShEwvqzppg5ZY1YXkiKvmlisu1T3iyLRV8zeGzFMsT_2sRvoVc91QRCNlAAqn3ZbrfZn3thfeH_mj2C52JIu6YPFn3O8J0JpEzvcXAsFIl8JmKtd6iDfzZpJCuwOizl5qU_jkP6CS2eztgBmEfIdg9hvlyOK-WJPfcMRMLfFnNU6oIQdlsmiS2ALym332GeYJzjreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKjryz2hOr-lsZ4pyWe7OF-EQyZdlqnABfVdGS0K7PrmKZPn9P9TQ4wLqJItPo6FHOGJJ2PQas7K_vX4MzbV7VyqQkaSuSNUJ0ADpbhtttUmQdjNETVuw9Q-A-BDn4qS0XQP5ScuHDwYQCxBpDdQCtuNIMuyTIvFrB1QPTKbV2QNrY-E3X0U-rvb6WT4YAjXWCjKtf3E9CC11oVQaJJcJnzE6H96S0N_0_9NuMJX4QB4S322ot-GoB8IISKDKyQWTqpmfbWmWnQLAY5LADCc_l4oxDYnOEFmRZRxK9_6jYj5JRI5Dv_-jpKgr5nNUAzTpfDK14GN0UoSAc5NEhCoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=S3iFbnsGmUg5zAMkCoftCaqH68pA1-_yJ6kVlOK8CVTB07LHCpK819gXrPVhFsOGbFDCwiZkeJ81eJn9sBl3Z0mNpEiOOUv71HEA2hw4e8vlvxUC5iEvPJ_sjY2-Hm_0xb3HRbdptpgz6-XT3Qbr6NDxOSb4QalDUVynFumsxuxCj_cjBori6L4xLlU41n1cS-2etpbiZv4XQwdEr_GH1GkFXzhsYqucyfScSjca9OVn4ViyZWuMVhCz1ny4IbVDAxInARDaQjyMibQgYgw-qx0cD9M7W1unAnoNOMqDzHJcEeE20YMh3r2A0hr1Q8ZedzO2495PeeZmpYV320-88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=S3iFbnsGmUg5zAMkCoftCaqH68pA1-_yJ6kVlOK8CVTB07LHCpK819gXrPVhFsOGbFDCwiZkeJ81eJn9sBl3Z0mNpEiOOUv71HEA2hw4e8vlvxUC5iEvPJ_sjY2-Hm_0xb3HRbdptpgz6-XT3Qbr6NDxOSb4QalDUVynFumsxuxCj_cjBori6L4xLlU41n1cS-2etpbiZv4XQwdEr_GH1GkFXzhsYqucyfScSjca9OVn4ViyZWuMVhCz1ny4IbVDAxInARDaQjyMibQgYgw-qx0cD9M7W1unAnoNOMqDzHJcEeE20YMh3r2A0hr1Q8ZedzO2495PeeZmpYV320-88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv9GwjK-udWiX6h4iLS2XuL5RvEzmp8gM2ZZydRQBjpyO-pLn55Z6jL2YfpN1vLk9XlC6uHbjrMAzqEN5lhzIi3WJ8cDGt1QduMyFh7pyGHRIw0J0UmpDPEL-Iy2z3vv5t6PX1QWnvwvbOeIiqXPu29Hunqlbvl4S4WwuIduD8L6CYcI6uokkp8L0j7Rs253LksKoVWSnPGrMt7tATOqYQ12fjsZsl1U7I3cQsqFvRRXq7s3a6KIKnfqtf6i9EWLRNbgYVi8JrdVcZv698JP9uGvUCoiKJDkGDmASuIz-5AOXrxZDSRVVknpzztvz1GEiIHi3GChK7SsrWVH90cfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snFlePLrRC2HznVZo8k4Ui5Q9JsdVElXKEQ6wkc-6rkip83fkXqxEJCZQiS3PRZZbFTDqNoU46yhtor3I1rWJioU2qya2rJ_bRxtphGWL-3G3lsqseb2fqlOZiHKR-d58ZGN9JJSvLl6glueH4PsHz1LzqIP86G2Utt30Pv8btBNObbti1xYSJVHclBtKPGmJ5h-7lhdvj6goUAPIAw8qlpPNywONtNudVpZPIl7OyI4h-miWsnnKDzqq_kMo2TUseq4mPu3_wnFj5mUsZH_aZytHwzWC8RGKwvhCbEnm7x2YN9zSv5WoAAcyI4Ba9s-gXrl9yMwJk3EB0Z7RB40MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB2UbNis70uwQbucxOsYxaV7PEsjvQM3A4di65x0QmtptkJW1y7kIjdmK3zrRbWiHKlVx4j3u3sDFiJBvNI6E3dI3OLM3uqZuQCnKL1qu8MA9Qtimbw-adTDj58hEiED4OPO-p7ZnL8kC171cLXss6I_j9XSA_XGY3RxOLorKZvHuKTUgNx61Ptu59AmyOI3RpOxoJjkWxKV-vlliVnip3ZpxinYv_sPIHLjhnlIeNQyUVTH2qpVz2x6HOkYQO3rJHeAY_xLa0aYizleDPT9AfhSGz5o-Sun-EpqFrOH1eRaH-ZuY5eB0pn5UlZdpKHr5G2gUToKNUNr0TAQbx5Hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=dIRGRwOFEZuR7WSKWA79YH2ldGczAMi7gu539rsNYsRys07D_4LZN1mLuzk8VnF4CckkzVRPhdrqmWSTWp7do7z6TISWEj3F93GsA-MZueq315XTL_NYpBu75WDLFa8fQwOUY8oO74oH21qLqyHW91QV1XNoO-xpYp6fzHPFH8ieH8bajn8oyvmgjpPzmzbUGiBEdBCUuP67VVykCrDhLDoSr0r8dGol8B6o6Y7wLdD7DNf4Rpe_aPT5jzlXB_TEAglSx0rD6LX4URuPvxSN_oLh8QjqudLAFsCE-r317Cnitn3-K4vcjeeemsiqWTyyoi5IzRL8aiQhv_RkOYWEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=dIRGRwOFEZuR7WSKWA79YH2ldGczAMi7gu539rsNYsRys07D_4LZN1mLuzk8VnF4CckkzVRPhdrqmWSTWp7do7z6TISWEj3F93GsA-MZueq315XTL_NYpBu75WDLFa8fQwOUY8oO74oH21qLqyHW91QV1XNoO-xpYp6fzHPFH8ieH8bajn8oyvmgjpPzmzbUGiBEdBCUuP67VVykCrDhLDoSr0r8dGol8B6o6Y7wLdD7DNf4Rpe_aPT5jzlXB_TEAglSx0rD6LX4URuPvxSN_oLh8QjqudLAFsCE-r317Cnitn3-K4vcjeeemsiqWTyyoi5IzRL8aiQhv_RkOYWEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOC-IucKOE6ce-HsT1DkqSbyn24JXV4qG1QIBZ0tq5BJIozFM-SLFia6bznrhNvYeh6XoUN5lwSe6TKQPHLlVIqApXSHlhzirH9sxsW6Jg3xzUu2idL-PbDAK1tzYUxnR79CbVizqJ8k117gnz1ouEctogRCr7Lio_aYqpFAI_uYyvCwRED78kpAJIGC8DolBpw3vVJw27eXhCYaXsfrjQrvVIZjf1WP1HzS2iq-LT8vMeYF4D1AKZgObOdaXlWW3zAGdKUYBbkW3S40374AMXZZKAL-1x8wzt3LDywW3sc8jkCYRIWVq1FqwZhgKP38ZZ7BGNt7IcdOUnBsws0WfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=uob6z0uZaG-KDwPYIBxYiP8hdwpk0tMC5Ag22aEn88Scz3w_w5Ax9UigbmvJW7QHUXDnlKY4n6429uw9lVIiDaxXWMYV6AVmzJ8Xl_QgTR9hDbWr_mRe7hxDujdz1D12FB91GixjND2Ho9m_ElmuHbIIEBRDDgF0MxMUhwYur9wL5nqgVV9K_Q4pl1KPZORVBKj6zu4pJfr6Oscy3bnrQWNBRWI5jX6bcFEYn70OtSKkxRFu5hMy2HuM0_9BikZIL7NjOVw86dAV-4oWZukgZ8Auv4GLT9E23vALwPsCwOaFdnV-XdTfmQkFQgMcg1j1cJ9B9xULmhe4MH4IPnlStYX99Sllx16lJ_HOG2PR7cH2gU9UDRJ1EDFAOcXoC4lur9Zp09VAvlEj58ryh55HcmCoMkXzn1HWu_xCVPxpR3WChrOo1cj82BKR6jxFsTeVuVrIRIGRYCKNZNNkfiY9u8pB6SMuSlSB5YPc3_lr_fnLZNvv1c0A26gByzV-NpR3IwpdJPIxll6vZ6p3hukkOkHTwlKK7UvQ1ELsgs1MVywyyEtKk0CKFsUOUdoUjdw3oe7KyzNo0XBiXiDYEiuJ4q0qEGkvWwJ5CBu42UPewyvJvuZxov13TQyCsK6zHfxCqkjBZORnnpKfzZwR9xwQwPmeNUJYmOXdmElNBdxNo3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=uob6z0uZaG-KDwPYIBxYiP8hdwpk0tMC5Ag22aEn88Scz3w_w5Ax9UigbmvJW7QHUXDnlKY4n6429uw9lVIiDaxXWMYV6AVmzJ8Xl_QgTR9hDbWr_mRe7hxDujdz1D12FB91GixjND2Ho9m_ElmuHbIIEBRDDgF0MxMUhwYur9wL5nqgVV9K_Q4pl1KPZORVBKj6zu4pJfr6Oscy3bnrQWNBRWI5jX6bcFEYn70OtSKkxRFu5hMy2HuM0_9BikZIL7NjOVw86dAV-4oWZukgZ8Auv4GLT9E23vALwPsCwOaFdnV-XdTfmQkFQgMcg1j1cJ9B9xULmhe4MH4IPnlStYX99Sllx16lJ_HOG2PR7cH2gU9UDRJ1EDFAOcXoC4lur9Zp09VAvlEj58ryh55HcmCoMkXzn1HWu_xCVPxpR3WChrOo1cj82BKR6jxFsTeVuVrIRIGRYCKNZNNkfiY9u8pB6SMuSlSB5YPc3_lr_fnLZNvv1c0A26gByzV-NpR3IwpdJPIxll6vZ6p3hukkOkHTwlKK7UvQ1ELsgs1MVywyyEtKk0CKFsUOUdoUjdw3oe7KyzNo0XBiXiDYEiuJ4q0qEGkvWwJ5CBu42UPewyvJvuZxov13TQyCsK6zHfxCqkjBZORnnpKfzZwR9xwQwPmeNUJYmOXdmElNBdxNo3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYhFYfo4wejkknSf2ME7LjEkpICAtvY8abwaay5Nwvg-yqjMKg-RCdhkow6hsgP6KLg9cQDsRv3riOdyEWjnk3oWrCSfLKx_4bjHxzvznINNbQUFrZ5yhFeFF42C1JxGtq8-UfPzDc_OWfqo_Lj6JrViJmVczUk4sp-_hQG9sHcttGsObcYmcMeVpXVU9cpIyMwvNfmXC16tHnAoQwu8swpYvgM7WOXH5QdbbpoHkItZFk6y1WtICoUrY4T_OtzsROJu7AkLzZKTP7XP_K_dYn0yX5moX5TH-JSfDPZgoiBKPgEQePGoOpTGgVrBxwqtERXtImafJoMXSkMUtM9GWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=CZUfZlXoTnOm571YhyAJCwEPCqzmO9PR0Y26gh-Smcbt5i83qsBXnmzr7SucR02jl_ea74Y2XbwuUGH9bKO9NowsnWmE9eXVj0zkqEPeVlUF7p5S1ulL2Tehcxo_JnYua_QIrLBqCYFvN7c0-N835f-Nq3hEIsx4B8ujQpiPQzXVY5ayWzLveLYI0IZpk3vW8EaJYY2z6_v7RQdO2HS9rYfo-Nb7XElfkQ0TuDospvh45oCFjkDTkRbDvM7I_IrRLX6JqZoOe-9p6NMfqHui0WJ5J0aGGL-U9IhbM4eGMWvhSFEKV3wrURf8mWlFfgt9JGUw117zx2O9tn5b5GG5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=CZUfZlXoTnOm571YhyAJCwEPCqzmO9PR0Y26gh-Smcbt5i83qsBXnmzr7SucR02jl_ea74Y2XbwuUGH9bKO9NowsnWmE9eXVj0zkqEPeVlUF7p5S1ulL2Tehcxo_JnYua_QIrLBqCYFvN7c0-N835f-Nq3hEIsx4B8ujQpiPQzXVY5ayWzLveLYI0IZpk3vW8EaJYY2z6_v7RQdO2HS9rYfo-Nb7XElfkQ0TuDospvh45oCFjkDTkRbDvM7I_IrRLX6JqZoOe-9p6NMfqHui0WJ5J0aGGL-U9IhbM4eGMWvhSFEKV3wrURf8mWlFfgt9JGUw117zx2O9tn5b5GG5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avJTVoXpCAIMs27PEfjgYu6bUFY7YAQvf3ydGoIoNAJOl7HJmu7UWsKz8nBSolZ1zVVKItSLr_aH11iv-0bTaXOpTQD23If5lz5g2AoaA7olXIBMuvQinBnleRa_dQDJYQhbi6nI951ShUwU7CmkeJVxVg0R1IfXYDM0YuUBDaXZ6m8rvJD3lIb6bK3bCkRqiO0pTJfz-Eki8oXah91JtpMYmj1S8KYc_JhZFtrq-fRfJxDl-D00aQ7C1LAicD-fy-MJuplKWV3dcG_XLdrdn4f6DMbrr28wz451fQy-M9ppur-a69zZOzfDUE2ylJi4fnIVYgD6vPsvPjMUJN5RsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=BJfPYOtN4BWATHKUuA1I34j1ZHEpf-FKu3kePMNSMbXqY7G9Z8cHhBg3s9wcyxR4VR6dS8747pBRL4Xix73xpbzU5qQYh5sfNsUTjydV3ZJCMDMHh-ELYEAnT6tFnD8rQoURcT5gzW_j5ilj4bnnezwYwWLYGxs-tjEQMufxEvaj6xtWnksTDEXeFvAO4UwTwkfQGPuQvHhLZ7V3psBBxZJZ_r6EdOsnnEaRRAbfn8gGjOuApmgxv2FI6IN9fOczhF7OQBVpepWUVxZtE059owRMX-lOGy-q3wVrncDt03MXpezB1TilKm8wP34Ukzu1WdLdWueh5L7AtvOKkpP0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=BJfPYOtN4BWATHKUuA1I34j1ZHEpf-FKu3kePMNSMbXqY7G9Z8cHhBg3s9wcyxR4VR6dS8747pBRL4Xix73xpbzU5qQYh5sfNsUTjydV3ZJCMDMHh-ELYEAnT6tFnD8rQoURcT5gzW_j5ilj4bnnezwYwWLYGxs-tjEQMufxEvaj6xtWnksTDEXeFvAO4UwTwkfQGPuQvHhLZ7V3psBBxZJZ_r6EdOsnnEaRRAbfn8gGjOuApmgxv2FI6IN9fOczhF7OQBVpepWUVxZtE059owRMX-lOGy-q3wVrncDt03MXpezB1TilKm8wP34Ukzu1WdLdWueh5L7AtvOKkpP0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2s2yJDGbm9WdI0VgtA8Acg48-nztui_wzTLsSq-t6QwGwcjXfxhU0TfSV__FmMukI_bbVTIG9agIz8z4Bj0aCxE1Ywv_INXbnumYZr_EhHNrthgE3BnWieRhQ5TeW3FagmtJFVRja6cGFj9GK7hEUFcwOJwQbxaMCdTMDlZuHackdPUZfos6bUMEj76MisLKrf2zJMFgFl-VfTYqa-wWYRUs2XHlOMzVDmwgqPoSPhzdw7QkgMGOC3WrtG6J-7LTz25zyJ8cmF9h0HgJHHnSXrgPjDOhTsi7ZYAwXpg7pJyFUwDJtJ_2rSmuo105ZZEcD9sC-BlMOuoHJBQDlQNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=Muh6wdKaqv8SUgAM4wm_NmH5nEFZMuTqeskfHgjW6aYt2_BI6_QpMLA-KqrR8f2F1hlBUy4marbJ4pI1yScwWF5YMOELf_HZjM5GU28vnjBc4m3Ixo2lj88vdtvH1_XbmarVyYcRf5EVeDpuJ-ODvRCDxO89k8jALvKmnYlL-x5B2qNtTAJrQOGDijRbYRGpNwyjzMcKpjI_2ljlA9bEcjwf53EzA7-LHOS7hj7aUhZcPvZau_gBXWhif2_bopzP4nGR3YAvu0pCfPJH0SPY3I0ONCV41JupQeNygi_c0h1OZgZ319qX-SQ9prL0IA-XbMiGNvF7U76XTRx5RGygZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=Muh6wdKaqv8SUgAM4wm_NmH5nEFZMuTqeskfHgjW6aYt2_BI6_QpMLA-KqrR8f2F1hlBUy4marbJ4pI1yScwWF5YMOELf_HZjM5GU28vnjBc4m3Ixo2lj88vdtvH1_XbmarVyYcRf5EVeDpuJ-ODvRCDxO89k8jALvKmnYlL-x5B2qNtTAJrQOGDijRbYRGpNwyjzMcKpjI_2ljlA9bEcjwf53EzA7-LHOS7hj7aUhZcPvZau_gBXWhif2_bopzP4nGR3YAvu0pCfPJH0SPY3I0ONCV41JupQeNygi_c0h1OZgZ319qX-SQ9prL0IA-XbMiGNvF7U76XTRx5RGygZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=P9sNnvhQKwWJfPUlaBi8rZHZmHm06bff7EhkA-y_UiUBdxvfIs4f0NIQKcdCeypxfFYbaPJ4QylYyMLS4jNFJ7ykj9bSDiGHt5w_o6ItggUidaRUcaKTWGAxNwNMPoG--pzPDK6AgPc-MWZxVZccAsIM66jWeAJkYO7y_a9UYxikqv_JUKtmrlYo47YUpogdwjpclPDb4eQvXrKV1zyu_wdOHWvzAHcrNriVD1BI3paJlI3dIPBJTtBlTMJwqfwF5ZiZXdtn8So3eE_tMuPXB0uuIxESuVHfvm1twKX3ejW25ckuctQuWN-LgC1X8hzfFgk_8_lqgfTRPbNv9wQBW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=P9sNnvhQKwWJfPUlaBi8rZHZmHm06bff7EhkA-y_UiUBdxvfIs4f0NIQKcdCeypxfFYbaPJ4QylYyMLS4jNFJ7ykj9bSDiGHt5w_o6ItggUidaRUcaKTWGAxNwNMPoG--pzPDK6AgPc-MWZxVZccAsIM66jWeAJkYO7y_a9UYxikqv_JUKtmrlYo47YUpogdwjpclPDb4eQvXrKV1zyu_wdOHWvzAHcrNriVD1BI3paJlI3dIPBJTtBlTMJwqfwF5ZiZXdtn8So3eE_tMuPXB0uuIxESuVHfvm1twKX3ejW25ckuctQuWN-LgC1X8hzfFgk_8_lqgfTRPbNv9wQBW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=PdnbptXOFv_NL4lvANPwAkhYxasfw1M-GyqrOxQqyM52ZNjpbPdGt3vdOgoDu9iXerTRJkxG9VAPhXpC_dSHXS5tqkqnlkn4JXuVKl1xrUCJyfB42RUVbxKbradV_qlPorfRU2h3jZl0n9u20KUSVt9SnWrGeeUTTI2dmF_XPxOgu--5TFoySekmnMq__k_U7-Z5yzo0twyCb6xQvw3dMiqctsZbeIyqvKT_0_QA1ZoxOtHt4j0YvwBcQv3YZmPHoauIMIRS9d20fBs_d6NYiFurc4S_8XF2mMBZKbjlDyRlErZhCGglY705YYsd7fNrveJ2Y_TguWXLQ0QykU6AcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=PdnbptXOFv_NL4lvANPwAkhYxasfw1M-GyqrOxQqyM52ZNjpbPdGt3vdOgoDu9iXerTRJkxG9VAPhXpC_dSHXS5tqkqnlkn4JXuVKl1xrUCJyfB42RUVbxKbradV_qlPorfRU2h3jZl0n9u20KUSVt9SnWrGeeUTTI2dmF_XPxOgu--5TFoySekmnMq__k_U7-Z5yzo0twyCb6xQvw3dMiqctsZbeIyqvKT_0_QA1ZoxOtHt4j0YvwBcQv3YZmPHoauIMIRS9d20fBs_d6NYiFurc4S_8XF2mMBZKbjlDyRlErZhCGglY705YYsd7fNrveJ2Y_TguWXLQ0QykU6AcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrNa3tccNPokhh3z6094badG6wf1mHRJcrjdrF8_AROEh9ugcXtuYw4oC9ev92oOapQ6-HyfdH9RgJBpYUtw0el-1geC38RcXlwiP41_GjtMkJ3bNDuo4mUXCUVOKP5m098PCD7SCqEwstqLt65gObcZcSm6-RJIo2la4CNW34ha5a_CeIYAp9IpnIrxnumH5OsREmrEjZWttYeI02IVbpY0xFtNWRSK3p93QfxZgHBohQbSE9F625RJfWxr-VGAUZBnYpsQbR9B96rARN88S0dsDyTM9ca0u-NRnm26CxAEfXMw9auL0yFfln8q0r1x9h9Ced2xWCFxEht3CuD8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU-djmBxkBAWYuST5DRg5B2WsHEbcYMcemRPZv_gH4AvnmZTlKSfBsMObGbUETnc-sfeMEiiE_iHylBzNrMYkUmSDSQ2tMhq4xvqahaNi4dBQrVAYcSh1vfRungXsj-aFCAhZLCZXOjXLjkIuneYpTeWd5obq2nG3nf-VHi2nKoXw4kPK8Hx78NBZnSegNWn1V8AliIOIpBCNZjK1q1Gu_DhhIUMSPg24JDaXTIT-gUBElNWl6GiAm7EAAECicK5hO_CKsEiVwmEHxvAI64mozbaVOgaNw6lM04_No3XP14iRzT-B3YOoNy204mUclnQPrGWrwkw687rUpK4cdEWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=ny0RilhNBQdb4wl4xEn53i4j9ne70_eOd2mSD82NOKhBV9MknBNvNsfxjQ_GNjKIpgAtrnwRfgsF5iERxmdpYJqwSpjv4GpsGK493Xiolek9kxXZCza2g2UtLp_HC1IYMpuLDOHmYgmpEIbLSCfhGlTRWHEiO5JtbZmuVg-qfe_ekPaRn_noL7DsXkqXYqqjLYpfb3XC8Ik7H-Ot20z-olcrD0fpkRZSO0vrSk_gZTNFKp5uZLgZ7zx68n8UVjyp7fcStCOFa4P0KGBm25IXLvvt6ppMD2sqD1qvhZ-ZfQglsd2HmZgievxG0Ld5IN-Xa8yMIDO16u0N0_WT6LubBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=ny0RilhNBQdb4wl4xEn53i4j9ne70_eOd2mSD82NOKhBV9MknBNvNsfxjQ_GNjKIpgAtrnwRfgsF5iERxmdpYJqwSpjv4GpsGK493Xiolek9kxXZCza2g2UtLp_HC1IYMpuLDOHmYgmpEIbLSCfhGlTRWHEiO5JtbZmuVg-qfe_ekPaRn_noL7DsXkqXYqqjLYpfb3XC8Ik7H-Ot20z-olcrD0fpkRZSO0vrSk_gZTNFKp5uZLgZ7zx68n8UVjyp7fcStCOFa4P0KGBm25IXLvvt6ppMD2sqD1qvhZ-ZfQglsd2HmZgievxG0Ld5IN-Xa8yMIDO16u0N0_WT6LubBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhp9L5UP4bMGh2iN6-fKpKuv_0GT1R0mEKuADU5MgXN1AH3_Lz8srvodZvZR7QIQJkiyb9UvCuEhbBGbkX2wGsHR95827K_Op52iZVgSbXk2PVyXhZLZS3lK7t59GV9qLN2gNNvD0HiJngBBF2C_kpfcmADw02iSSdyKIlOvCv5r2fztzuf2xEoWC6dnkORyjVfLvwyY8s9Clt2raaat3SKX5h5xEcGmU5uaSYib5PG2h1xAGW7zYvkkpaKL-46cf7Zy48t5fDS1BqE3sZuha7ZZpyecrz0fh1yvU4OkhZB5AGIBPuSQ99RH1wuGBCA_EcZmsiNn1jSF54DYgu9fog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
