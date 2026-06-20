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
<img src="https://cdn4.telesco.pe/file/b5e2NMAAzUJVUtfdA3rsccfySBU5mbTmCf0pj4cCH6VBBoCZFIJCOrZI_sCnnWh1id2EjRv6uW7DnrL1ek9Ebk50ToL-mVmnUcz6bVLVsRoWUfEVhnuuJiTdOWjQUhxHtw7yysy9WpGS8HVU_l6vBr4rUOprjfFipIZ15CPe3PfFeSU2o6XIrcxnaQnNe5zwsHonYPtNLksQM1ssP2eSXT6oEB3HGVQwb9_plpGiREzmGJj71E21rZlbsjMFYoxQbv16Z44Q6CMv73Hr8WHTDgKZF-wIcM1rUUZn701syNf3KPitVWCBeFahX6YvJOONabmyDZyQ0HiHraVBY_cUmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-443515">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e035502f.mp4?token=Rxmt8QgDDQlkS2mH2vjD84SaCBhLeIbctcKi3jCHcOsGMcqTcsyQAAD3XkmtibE5vhBhqmFAHI5okQph68WoGMYcy9uHOBx2n_i5Izl2H3jwb9ROTRyFhd5C9pX7fV-J0paI4nagc5OMwZA7ijo2R9ND_SSLRL3QvGRLHvC0E27tHHfc-irBMQ3IiYDWxvKHzB-YFa39aG9ygFuOt9seKNztt9h68EoBoudVpIA1hfbN3-ucnpzXAOZdwaq4SbErjc_qb2F66HMK8b5P0aXFjfGds9l8s5ZGofMCmlED_OnaxYCLThMpuGRogGjOczQrTmo9NXX7wV9LULK60484tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e035502f.mp4?token=Rxmt8QgDDQlkS2mH2vjD84SaCBhLeIbctcKi3jCHcOsGMcqTcsyQAAD3XkmtibE5vhBhqmFAHI5okQph68WoGMYcy9uHOBx2n_i5Izl2H3jwb9ROTRyFhd5C9pX7fV-J0paI4nagc5OMwZA7ijo2R9ND_SSLRL3QvGRLHvC0E27tHHfc-irBMQ3IiYDWxvKHzB-YFa39aG9ygFuOt9seKNztt9h68EoBoudVpIA1hfbN3-ucnpzXAOZdwaq4SbErjc_qb2F66HMK8b5P0aXFjfGds9l8s5ZGofMCmlED_OnaxYCLThMpuGRogGjOczQrTmo9NXX7wV9LULK60484tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: امروز مرغ‌داران ما نه‌تنها سود نمی‌کنند بلکه دارند ضرر هم می‌کنند
🔹
قیمت تعادلی مرغ که ۳۷۰-۳۸۰ هزار تومان است امروز به ۳۳۰ هزار تومان رسیده و تخم‌مرغ هم همین‌طور کاهشی شده است. @Farsna</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/farsna/443515" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d61d37ad.mp4?token=nvLh1yxzG0Aj4u_LoaWESEKG_g3S2K_U59EvQGwvexJGtCK6xeB6XSedzgcMx7UL1d4f-cgc-E4VWPz24N8rrngxYogk4fjVp4UV9Lbk86yXY-HE_JS8Cu6_uDRGhQJnZ2jWtG3ULImqeyH9X7XJd4TB0M4gvg47hBAHScwtAypIIyDU9CBD60rB8Nzhh1bIN9EUqTFxP9MknX9F1KTgdSR5Ogokxn9f5mAZ1sayg6-ZdgKvg0De8Q-FApksoujPFF7XEFTWXtf6cxATaeO3cILKr8G-WSv1UY8t06agGq-XfxZpfCIRkWGSWmQLP0peaGzTpFVUJF74HIi2rYEibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d61d37ad.mp4?token=nvLh1yxzG0Aj4u_LoaWESEKG_g3S2K_U59EvQGwvexJGtCK6xeB6XSedzgcMx7UL1d4f-cgc-E4VWPz24N8rrngxYogk4fjVp4UV9Lbk86yXY-HE_JS8Cu6_uDRGhQJnZ2jWtG3ULImqeyH9X7XJd4TB0M4gvg47hBAHScwtAypIIyDU9CBD60rB8Nzhh1bIN9EUqTFxP9MknX9F1KTgdSR5Ogokxn9f5mAZ1sayg6-ZdgKvg0De8Q-FApksoujPFF7XEFTWXtf6cxATaeO3cILKr8G-WSv1UY8t06agGq-XfxZpfCIRkWGSWmQLP0peaGzTpFVUJF74HIi2rYEibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: در حوزهٔ کالاهای اساسی و محصولات غذایی گران‌فروشی فاحش نداریم.  @Farsna</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/farsna/443514" target="_blank">📅 22:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6f4a0454.mp4?token=T7IM3GWvB5VHpRWojMucUp7ZR7vUZBhUVWFXkAI2CG34XhptY0J4TcxvUaVxNMOqpCYAD5QEAXp1EAtleNX8HHuBEEnfg82jd-WrRvV_uemGgIAO1ErMEYkEs7O_HJYzhLuZCIRPpIoM7uylTHxJv1lZ6-9U92Tof3wS_pEO41Ygo90u4Fjguo4FY5irDZMGtlDjSJexPcj5-6acIv0zc10LwPUwT1ibWJHRhm5SOWuX35_tYW1XE0IK8KyAeNw7e2s84efwEPe17Mn9rZwyORV0Uatp98alx4l65VG7RUv_Vv1Z8eNMh-67mhWPHpEBeg0YwTdM_8C5UobIfFihmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6f4a0454.mp4?token=T7IM3GWvB5VHpRWojMucUp7ZR7vUZBhUVWFXkAI2CG34XhptY0J4TcxvUaVxNMOqpCYAD5QEAXp1EAtleNX8HHuBEEnfg82jd-WrRvV_uemGgIAO1ErMEYkEs7O_HJYzhLuZCIRPpIoM7uylTHxJv1lZ6-9U92Tof3wS_pEO41Ygo90u4Fjguo4FY5irDZMGtlDjSJexPcj5-6acIv0zc10LwPUwT1ibWJHRhm5SOWuX35_tYW1XE0IK8KyAeNw7e2s84efwEPe17Mn9rZwyORV0Uatp98alx4l65VG7RUv_Vv1Z8eNMh-67mhWPHpEBeg0YwTdM_8C5UobIfFihmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: وقتی حقوق کارگران ‌۶۰ درصد افزایش پیداکند، این موضوع روی قیمت کالا تاثیر می‌گذارد.  @Farsna</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/443513" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506cd7cf18.mp4?token=vZbm-cUzbwrCIos00ooyE8gD-YFvkl17M5ajCTnlBItFNZEsYWJXqSCD3OZiJvtafiff2iLoqfhnzslZ1mL8NQw__5rNc4xxd1y-S810nzWQlz9Etoq2CEYgAw1pmjxbINlU4m-6X2YsQ62MpKYfEqVZhnWkPWPIaGYP9PA01Qa_KcPOI40Wh99Ou5znSxiMDfkH-kQaohoaJjOTPQ6SiJjOqGnoUxWXNbyFMoxUv77mBqt1DSRoCKwhzohg3gOS7H9kROHiP_B9V7aie2KEEwdVH-foT4IHySispGnPIeawHaYTH0bz1qc0RFxWqkSZVmFLzxmAs0P5kRuxCs_Y7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506cd7cf18.mp4?token=vZbm-cUzbwrCIos00ooyE8gD-YFvkl17M5ajCTnlBItFNZEsYWJXqSCD3OZiJvtafiff2iLoqfhnzslZ1mL8NQw__5rNc4xxd1y-S810nzWQlz9Etoq2CEYgAw1pmjxbINlU4m-6X2YsQ62MpKYfEqVZhnWkPWPIaGYP9PA01Qa_KcPOI40Wh99Ou5znSxiMDfkH-kQaohoaJjOTPQ6SiJjOqGnoUxWXNbyFMoxUv77mBqt1DSRoCKwhzohg3gOS7H9kROHiP_B9V7aie2KEEwdVH-foT4IHySispGnPIeawHaYTH0bz1qc0RFxWqkSZVmFLzxmAs0P5kRuxCs_Y7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما هم مثل پدرانمان عاشق حسینیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/443512" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eb62dba8.mp4?token=lJBAkXOg-xO69sHTsPU5e7SVPIwhXdKbHq6wVsTaUp3ulL6_hj66b8wlTwJ2LDWS4wcDRKTxVWrc5tgwvG4PHX-vqswdVhO2BSIPaSNe6ZPFJ1McmzhdoFBa51UdZWVT1fFKLQYmqZ7FjwgUL8u6fVUjl0gO-VRwkXtoaDs1jCyo-p3l6c0FNfRUeMZU7WyGWR2K2J5cT6QLqjFwmxnJRR4x-ObFyVo8V0NpZJ0rrxZZan56YDggl1WuSOK5zxWfvnWNZs6akmByGZAmR3PUL2vP2uDcLvmpKUaj9L8cp8sbg7iyAC5tJktBDLQjlZds-UN9mvwP2DTuve7O6D0Slg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eb62dba8.mp4?token=lJBAkXOg-xO69sHTsPU5e7SVPIwhXdKbHq6wVsTaUp3ulL6_hj66b8wlTwJ2LDWS4wcDRKTxVWrc5tgwvG4PHX-vqswdVhO2BSIPaSNe6ZPFJ1McmzhdoFBa51UdZWVT1fFKLQYmqZ7FjwgUL8u6fVUjl0gO-VRwkXtoaDs1jCyo-p3l6c0FNfRUeMZU7WyGWR2K2J5cT6QLqjFwmxnJRR4x-ObFyVo8V0NpZJ0rrxZZan56YDggl1WuSOK5zxWfvnWNZs6akmByGZAmR3PUL2vP2uDcLvmpKUaj9L8cp8sbg7iyAC5tJktBDLQjlZds-UN9mvwP2DTuve7O6D0Slg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: وقتی حقوق کارگران ‌۶۰ درصد افزایش پیداکند، این موضوع روی قیمت کالا تاثیر می‌گذارد.
@Farsna</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/443511" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6kXYIRSsVWz9CXMJhq_jEm5B8cmfVvKi3CE3hSlUJvZSr6EPWKHhArn2xns2a9DijalvFinrLsd7W7nwUs8eBl7cjEaF7TphX05JK2dSe-BRaJdIPDNzwaxCpbdpqLF7MdsT6EdSZKPvtUc6p6GbMmYQ_cgCZ3Oa0BrOFM5_a1zvp24unMrHR7L2hLEEM_AI7J7NsXiXP4hLELtx5fHEqt21A7azl2znisnwtC0RDdgyz939GXOrTpPYXzK2-nVt-kq50z-UdSV5BThUNbNXv9eamLwKa5kr8qCjM6_F-75It8y4z-HP-tMfiqBPWGK-mx7LbDCtWXma7S6m4pY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو غایب بزرگ مقابل ایران
👀
‼️
به نقل از DAZN، جرمی دوکو به دلیل عفونت دستگاه تنفسی بازی مقابل ایران را از دست خواهد داد.
@Sportfars</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/443510" target="_blank">📅 22:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4577c5198.mp4?token=M4-hSptMdS9eHDRphUz5MfrrLsZqm1_RoT-xk1oSujwFvZo4fP0uugVuyK5wfIm-9SszOLkHsS3qyYGmDWGBb6SXo7eQi9qVX5fbXIAa7LmeL_BiBYrV7Q1rsmxvRfuHCK7jOJ5umL9WfBsmDAmTC64-wwAFKgxqnMJNXSvqrnP3BtPxwkrhrRwG0XbCxsY_Q1rX1iS8UYxn9YAoiZcGIBUxekXfS1ov0eL14AngFG2Y2WO5_Bin3zbG40sv3b2QUfx5euaKsg_o6nnRSOXcYTmvPvrGgl9nfLbV2UwQSCtoUw40M-UbfDFFn3jukHNJvMGGXQBGwsHKgWe5pXLOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4577c5198.mp4?token=M4-hSptMdS9eHDRphUz5MfrrLsZqm1_RoT-xk1oSujwFvZo4fP0uugVuyK5wfIm-9SszOLkHsS3qyYGmDWGBb6SXo7eQi9qVX5fbXIAa7LmeL_BiBYrV7Q1rsmxvRfuHCK7jOJ5umL9WfBsmDAmTC64-wwAFKgxqnMJNXSvqrnP3BtPxwkrhrRwG0XbCxsY_Q1rX1iS8UYxn9YAoiZcGIBUxekXfS1ov0eL14AngFG2Y2WO5_Bin3zbG40sv3b2QUfx5euaKsg_o6nnRSOXcYTmvPvrGgl9nfLbV2UwQSCtoUw40M-UbfDFFn3jukHNJvMGGXQBGwsHKgWe5pXLOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصادف مرگبار ۲ قطار در آلمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/443509" target="_blank">📅 22:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
سلام، چرا هیچ نظارتی در بازار نیست؟ زمانی که دلار بالا می‌رفت قیمت‌ها با توجه به دلار بالا می‌رفت، ولی موقع ارزونی دلار اجناس ارزان‌تر نمی‌شه؟
🔸
قبض آب این دوره ساختمان بیش از ۳ برابر آمد و بعد از مراجعه و اعتراض به اداره آب اصفهان دلیلش را پرسیدیم، گفتند چون نسبت به دوره قبل (در زمان جنگ و عید که ساکنان مسافرت بوده‌اند) مصرف بیشتر شده، آب‌بها چند برابر شده! این موضوع خیلی غیرمنطقی است.
🔹
در ایام ثبت‌نام دانش‌آموزان هستیم. برای ثبت‌نام پسرم به مدرسه رفتم و برای ثبت‌نام چند میلیون می‌خواهند، اگر اجباری هست آموزش‌وپرورش اعلام کند تا مردم تکلیف خودشان را بدانند.
🔸
چرا کسی پیگیر مشکلات ۴ بانک نیست؟ الان ۳ روز هست که توی کارتخوان کارت کشیدند اما تسویه‌حساب نشده.
🔹
ما الان ۳ هفته هستش منتظر پول وام ودیعه مسکن هستیم. دقیقاً ۱۷ خرداد پول واریز شده ولی گفتند مسدوده و یک هفته دیگه می‌تونید برداشت کنید. بعد از یک هفته به اختلال بانکی خوردیم. الانم همچنان مسدوده. چرا کسی نمیاد توضیح بده کی این اختلال حل میشه؟
🔸
با توجه به فرجه نامعقول و نامناسب در نظر گرفته‌شده میان امتحانات نهایی، شرایط ناپایدار کشور و فشارهای روحی و روانی ناشی از این وضعیت، از مسئولان محترم درخواست می‌شود در برنامه‌ریزی و زمان‌بندی آزمون‌ها تجدیدنظر کنند.
🔹
سلام من یه متقاضی مسکن مهر ثبت‌نامی سال ۹۰ هستم. بعد از گذشت ۱۵ سال هنوز واحد ما رو توی مسکن مهر پردیس فاز ۹ جدید تحویل ندادند و هیچ جواب درستی نمی‌دهند. به داد ما برسید...فاز ۹ جدید پروژه نارنجستان.
🔸
خواهش می‌کنم برنامه قطعی آب فاز ۳ پردیس را نگاه کنید. از جنگ رمضان تا الان وصل بوده، دوباره از امشب شروع کردند؛ تا همین الان سه چهار ساعت آب قطع است. گردن هم نمی‌گیرند، می‌گویند قطع نکردیم افت فشار داریم، در صورتی که نتیجه‌اش برای ما ۱۲ تا ۱۷ ساعت قطعی آب است.
🔹
کاش در ماه‌های اخیر خبری هم به موضوع پرداخت ناقص حقوق اعضای هیئت علمی دانشگاه‌های کشور اختصاص می‌دادید.
🙍‍♂️
شناساسهٔ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/443508" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efab1522b4.mp4?token=Hrg_6J6E1Qg8Z3n2WimQUlEVjyo1Eh3vI4EYI6EbXkgfG0DWPvF9I-OnF2zbz6kvg73mVneI4O6GEwglAGhfM1kbqBxvSBHstYv1QP70TqkTYQSVfyIS_O3EjuZ2prx0DKAu-K2p1EaLV1vNuJGcRI6TIK1gkuD9ly-Hb1DdD0KDS2vwngohOTS3Ub0dmrJK79uLQwCel8yoTtN1sQOBIH-h_0qGx7RCpMtMH3RS3Mmy-a_yepHxEtK3JaTBxs0k5XtwXREU_WQahIYLx6OsUmy2HP3dAVla1EjApUjaLKa5FVIqvAmzvBPwbpjsF90EUAQufK418q-Av07-Rp3dxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efab1522b4.mp4?token=Hrg_6J6E1Qg8Z3n2WimQUlEVjyo1Eh3vI4EYI6EbXkgfG0DWPvF9I-OnF2zbz6kvg73mVneI4O6GEwglAGhfM1kbqBxvSBHstYv1QP70TqkTYQSVfyIS_O3EjuZ2prx0DKAu-K2p1EaLV1vNuJGcRI6TIK1gkuD9ly-Hb1DdD0KDS2vwngohOTS3Ub0dmrJK79uLQwCel8yoTtN1sQOBIH-h_0qGx7RCpMtMH3RS3Mmy-a_yepHxEtK3JaTBxs0k5XtwXREU_WQahIYLx6OsUmy2HP3dAVla1EjApUjaLKa5FVIqvAmzvBPwbpjsF90EUAQufK418q-Av07-Rp3dxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در خونخواهی امام شهید کفن‌پوش به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/443507" target="_blank">📅 22:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667f87f7f0.mp4?token=d165AXho-F4UKj-syFRviy-y4297vT6nzL_owYIbjSawzhRN5BgGDivo4zibL2Oj_hUdfyAMGPfMthwEMnAL7J5dPFRUsaKF_mnaZrJ3a9IHlzwPOdrdwbY11kgX3RuMpqe_ofQnrtFCaqeo1FuBG1c5LyL_ryblIJUsg3udCz6wTetMkZcL89GCnO1XfzhIFDQEfUkSu7muoBs5Xvay2a7MSiEX0g90qr4Q9GrWZ-b7zShY7bH_mSa8wE3zxEvRVtPfOCFaXFQ5CVVw2Vn48WJRz5Ei20SScjZyomDA7aMa4B44Nz8W3SQG5LEOCobaIjQ68g6jRZ0H4ZqACqsZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667f87f7f0.mp4?token=d165AXho-F4UKj-syFRviy-y4297vT6nzL_owYIbjSawzhRN5BgGDivo4zibL2Oj_hUdfyAMGPfMthwEMnAL7J5dPFRUsaKF_mnaZrJ3a9IHlzwPOdrdwbY11kgX3RuMpqe_ofQnrtFCaqeo1FuBG1c5LyL_ryblIJUsg3udCz6wTetMkZcL89GCnO1XfzhIFDQEfUkSu7muoBs5Xvay2a7MSiEX0g90qr4Q9GrWZ-b7zShY7bH_mSa8wE3zxEvRVtPfOCFaXFQ5CVVw2Vn48WJRz5Ei20SScjZyomDA7aMa4B44Nz8W3SQG5LEOCobaIjQ68g6jRZ0H4ZqACqsZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است
🔹
اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند. @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/443506" target="_blank">📅 22:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udQT1Et4y-3hA6tGpzdv2EY5sofOWwHoTikLQaGANUK7DJTAohdhNIey9Xun-EImEXbbrfsJmeYSaVa_T90uTSdwP34FkWgoc_pfzPiuRZbV1zMQRzYn02kfG_0WfxiM1SRTESSLLSujgjy2NmufNVOZ3kP6F8SViQozQfyy5oc_rLGYQoIum-2lzmewyaWmakey1pbRFNpiOd3q6yqGcQQcfGQ9VQRn8b63A7e8R4oy6DkNmClu_DVFVHp2aX5RKxviwIyR_5RnfIM6kkUEtD8ojEJw0Oabkj1QLhp_fmAy0C13noK5_Snyc5BW59uVveV3ZpnP_T1M3DUMd4ZuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1CIwuqcFhu1YQ1LdQBM8sl6lcZSMa22vb-XUVQkxNvIQIAjETc-I90LMVj_HadHYsCJxHvy4VbKGNt5M5U7W_Kou0v5p3D0NTcM4ZjYMNfEtI3BQvKp4GHQj1s30cc_q_N9_EcHFPdSQ9zQaUNeZrAQBGvI7uDxDQs091octisBT3In4laIobHrvtMJYqh4e7gMT0gx6uRyuS4DUIJNbf3KdHSQPK2X3xdvx5b3g8nxbuhsELdxFnNHxsbgQKBA6JAggGoUGo_1TAgCvMSAhoEaBviOu-_zhBnhXHg25k-JYW3ClXOMZMGNprHx_0Pr9PFy46zMhr-3lYcNVQFJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rngL78Du-sRsmxcDRdm874aKDKvMmLER454pfpHf4ca334lWi1RSmbTSJyH1zbKZJpQ_CIJiXGQKFEi4u5xQiVI-j-1whRBJ_xDxt3br6lPaEl0I0Wr0Zn9tT3fqKcwiOjZokaSXfAka5XEdCc1dLRMlhq3sWnzmrS5jvMJMPGVM4I38GT0M3vwIMxadKPPuErPdPpHBF8MFVfAYXDqCSCGwomHZDfd79i-2_w8L3q03DnK6aidXydZuH5f-SGE07K6BgBiFvkZ6_VwAk0DbERnR6Y01vAR_dWVYzp4SSJjJFZ0YkpPIPIXNoSgaZQ79ZTbOgN-qfqaXM6K17cboqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g56UCUYn28b29-fn3pYEN5iCPGPLjoLLhTV0xXnla1jz1etmsGv0ugmagKXg7O7jkL9_MCNsLh_91aRsYrQ5M77RmhUW2yLQz7dr_2ucqP-6LQb1rPFU7w7qJ3qcTGE91z9M8Y2FQzVildcwp21MmWLvN1YInLclx7Os3oqIMLfgkGTMOudOVZx8NBL5rz8uAGIDk65ab1UXEiUlAcb_Sy7RKtE0W_JtNFt097GEo7mw4L0KfUcxx2VOf9gG6uUb70QiapFpp3-a4RFzsbw_EsfElk-SuTTLPq5wxHuSLcY1tbsZb_M30TVhnH6Kx2sXFxLa4RuDmqQSt8xSqdmEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnckZx1dGvOrygULlSHvQ2-wHGGS8gslwZxrIYvpGKkB2nTRxJ79_ORVJi34G5EYSRVjv5afNKwPfOdYqvxW5opWd2313q--gblDk9C_R5bFqWhKC8ruFLLg9r60buuh2wRHpim9sHB7AckC0kKfnis8lpW9N5VhnVitcxAhWaDLGcDjPlUUnkmgbjOaNutZKidEHJ1yeRmY9phVkh5f-tTyDs8P9nta7KnV7yBA0NHeHHpjWVt267s0aufGQT7HEM-WW1llWG2cbUs46H0ES_0B8HuwPJDGbhrvijAq47rJ_EKMy5EcfUVbTnhI3igahqQuZiBwHItT2HX7_7gjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4dIme0RgFNU1yAXq2-KAEpv7HufkdMkUvjyfZcUvTiyscyGp1X4C_MBMh32_-g0b_nMdmTnibkQShZTzUwKOevUizFJWFmwqVJz-X3D7zCH2gcicpItV_FeWayqj0YZpslUmr7dJsGiXh4ooWg1rFA8QgqJx-pILGLZ1kSf17H6XmZqbbgHp_dBTBrI3TY18KYjbj11_OwHicE9wqO95HofIZLljHnWg3mtbtVrkZ_vBPAzqZ1y71QORfPN180GzEqPGFGMwZ0ah1z-2GLS2jSEAgWZ3UCPNlDo0YjpLZp-lJxcPwAkbHCwlKFUtD9uhC4jU4Vh115BQWkoeW-6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oik34l4NwHFFtKySMmjZii30qrsuTL1IoMu-mJZjtppakGWNNfkwbmvQOf39ShBi0PeMjNHUVR-TibUR9pc34685TpToqQ2KZw_MaL0LNURDMjlssD3supgcLMFHOAp5gmVAXaeuhpph2amW2EVhN3j_CW25RejdrbcYAYc7eeAGvo2db3ssCIzgCelM_sL91tSt8QzIUccG6srUims0S0qrkin-w0952g2SLbnAd8vJeaUCjUJ5LvzKPQchag1bQ59H6xHmIHfjhjQJGzTt-wXp3PQAIvqqMZmfPp9laTSA6XzvhBGrB5w54P8fpNcSA4uWcAyA2eYry_7ob3DBWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی هیئات استان یزد در حرم مطهر رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/443499" target="_blank">📅 21:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a45268f8.mp4?token=qunZhlF8wUzX_6Vt_yxGifLvMlz4rtDRgHs7TqSekX6pZaHy6TKnpp65XHr7UTk9_mH1kKfJfh6eoRGm_a0kZlw3dL2pNYanqN4E6wUz6VeU-C03XVOeeQ0KixdxAsSH10VIGG19l2KxhS9eycWn5CwJdHjlu6NnBb_WZ71Fy1A6jWwbqM90aQOcSbE5nR-0x5Zwp3vAxfI7Mgf0TgvVa78VurDpwjMv4EwhXcvLmQpffVZ_rDE84iQZ1oR635LAJppSvlXAY64FrSOEeSZtOWewdHatcD7oD8m0_MKxFhjpJ-1nDXRJFXATsPBMXIGzelsFZ-1bOjQj4VtTwzHofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a45268f8.mp4?token=qunZhlF8wUzX_6Vt_yxGifLvMlz4rtDRgHs7TqSekX6pZaHy6TKnpp65XHr7UTk9_mH1kKfJfh6eoRGm_a0kZlw3dL2pNYanqN4E6wUz6VeU-C03XVOeeQ0KixdxAsSH10VIGG19l2KxhS9eycWn5CwJdHjlu6NnBb_WZ71Fy1A6jWwbqM90aQOcSbE5nR-0x5Zwp3vAxfI7Mgf0TgvVa78VurDpwjMv4EwhXcvLmQpffVZ_rDE84iQZ1oR635LAJppSvlXAY64FrSOEeSZtOWewdHatcD7oD8m0_MKxFhjpJ-1nDXRJFXATsPBMXIGzelsFZ-1bOjQj4VtTwzHofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است
🔹
اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/443498" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔸
ارتش اسرائیل خبر داد در درگیری های روز گذشته در جنوب لبنان یک نظامی اسرائیلی کشته شد و ۱۲ نفر دیگر به همراه یک افسر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/443497" target="_blank">📅 21:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1488d2de71.mp4?token=tVI-mOFvyOiQFZzvCigNAGs-esgjsjni2WBSLR_5CDx19tfh4laKVHgsEr5qPL4PGx8i0Hb7OI38mdkKQNaUS1s4Q8p6e1rxL24yCbuQ4cJHjwf9Dr54sTgZufliZvKiW4Yb2NTJJNJC_YBhFPbaAzb2YUBxXgI4WxUZg0S0bd9IdT5Js1DwMocbHY6ze42sbBkwd7g7pyZosuh2kqT8x2ioQqfWAl47Piflz5X2yt8MWTHR-yqI7YgnRkGbt5HzvNiO8akMysr7ByiLYELBtMZ3ZQ4V08rDF6r73ZsuF3rcqjrpJp4dS2pGxi8ME1e2XnY-52IYTC728h0sHnP6_6CNTiJA3aqi7CBEl1D_LA1DlsMvYbW_jt-m7eCDNb2jg8hp0oixJETXQAC5guB8Q24e20A6YW5e0sLODPU07rtHU3R-SUDkM33Tx9bvDipG6Rpeb19oeeZ02oEAsYMCo2Jl3MnOT4TlKr0IwCAInWWhfJkBQyQJMMNzoJWCW9_SCtd5nxHaE40qvCxj4Cgh9QimDzTfJHTNQMYTB1mGLAYBah9JC68rS04SgL7L_ZonwLE7QpwAVZp3bG1-IC7kM7dV8QiUjgHdp_OmmbBGP1gv61qGwG6QfbYQtneaR-C_2cfjGz7My0j5dBO_BtWUG4kYP2dTfUqcwNxvd5Khpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1488d2de71.mp4?token=tVI-mOFvyOiQFZzvCigNAGs-esgjsjni2WBSLR_5CDx19tfh4laKVHgsEr5qPL4PGx8i0Hb7OI38mdkKQNaUS1s4Q8p6e1rxL24yCbuQ4cJHjwf9Dr54sTgZufliZvKiW4Yb2NTJJNJC_YBhFPbaAzb2YUBxXgI4WxUZg0S0bd9IdT5Js1DwMocbHY6ze42sbBkwd7g7pyZosuh2kqT8x2ioQqfWAl47Piflz5X2yt8MWTHR-yqI7YgnRkGbt5HzvNiO8akMysr7ByiLYELBtMZ3ZQ4V08rDF6r73ZsuF3rcqjrpJp4dS2pGxi8ME1e2XnY-52IYTC728h0sHnP6_6CNTiJA3aqi7CBEl1D_LA1DlsMvYbW_jt-m7eCDNb2jg8hp0oixJETXQAC5guB8Q24e20A6YW5e0sLODPU07rtHU3R-SUDkM33Tx9bvDipG6Rpeb19oeeZ02oEAsYMCo2Jl3MnOT4TlKr0IwCAInWWhfJkBQyQJMMNzoJWCW9_SCtd5nxHaE40qvCxj4Cgh9QimDzTfJHTNQMYTB1mGLAYBah9JC68rS04SgL7L_ZonwLE7QpwAVZp3bG1-IC7kM7dV8QiUjgHdp_OmmbBGP1gv61qGwG6QfbYQtneaR-C_2cfjGz7My0j5dBO_BtWUG4kYP2dTfUqcwNxvd5Khpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های شهرکرد آینه وصیت رهبر شهید و فرمان امام سید مجتبی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/443496" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/443490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب ششم محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/443490" target="_blank">📅 21:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/443489" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627580024b.mp4?token=SDJpgq3hV3-KzSskBQCm5_SVxq5yrQnZA_UWNN9O6s5Jay5qoNyDi6jrT6eZmwff54eXsbTX3WpO1lVP4rFBex2Z2P84Swu9ccqYuXT2xnuLmzJpc3awtR8SUSPqqjx17ObMb89CVzzPNdgQDKWeeKca6cbuyS-TnWKOEFBMldd1b8EkK8d3Wzes4pYHJV8ODYm7Do5NwbnSMbz6sbXEQ6_Rt3550kZZnXuPrOdh9CeqyJwdx2DaiKZiQLKHgzqVFQVGf2fn9siZx3A6YAm4xrH3UfUW6T_DX_c9xAoa7ueBJdwKtSZpi-jggXnxTQ524u-l9rXdmpQV29C7IkhLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627580024b.mp4?token=SDJpgq3hV3-KzSskBQCm5_SVxq5yrQnZA_UWNN9O6s5Jay5qoNyDi6jrT6eZmwff54eXsbTX3WpO1lVP4rFBex2Z2P84Swu9ccqYuXT2xnuLmzJpc3awtR8SUSPqqjx17ObMb89CVzzPNdgQDKWeeKca6cbuyS-TnWKOEFBMldd1b8EkK8d3Wzes4pYHJV8ODYm7Do5NwbnSMbz6sbXEQ6_Rt3550kZZnXuPrOdh9CeqyJwdx2DaiKZiQLKHgzqVFQVGf2fn9siZx3A6YAm4xrH3UfUW6T_DX_c9xAoa7ueBJdwKtSZpi-jggXnxTQ524u-l9rXdmpQV29C7IkhLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیهات‌ مناالذله، پیام شب ۶ محرمِ مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/443488" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443487">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1856500ba5.mp4?token=HZgo2HJ25pqeNg1Ytx0Mw244kYGAeAfMCbx8-V6SNAoZYjPIoCWP15-vF9ekqAPP5Xj8Th73l-Ruiq_467tm2cKb7IM7NoKiHmXYvoK4NtflS6UPXo6IQVDUL5pZvXUMLXvxdQUj_RnpXDgPRwTB5DCqzN3D96cYmgibz-ahwuihrB1VS24AHegHd_1LJNkk5nN1tTxl9Kq26re5a__Wvx67JEIkV7BwI0WnlBp_yCegkMI70FEtIWvB-fdoQqmYkesKeb7YJvOvuWVhQZFFFryOiZN-XTCr7PUtzwjtoKlyIulRCG9kHfQACetsbYN_mFB04vEAwAd3Mtfpz1zQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1856500ba5.mp4?token=HZgo2HJ25pqeNg1Ytx0Mw244kYGAeAfMCbx8-V6SNAoZYjPIoCWP15-vF9ekqAPP5Xj8Th73l-Ruiq_467tm2cKb7IM7NoKiHmXYvoK4NtflS6UPXo6IQVDUL5pZvXUMLXvxdQUj_RnpXDgPRwTB5DCqzN3D96cYmgibz-ahwuihrB1VS24AHegHd_1LJNkk5nN1tTxl9Kq26re5a__Wvx67JEIkV7BwI0WnlBp_yCegkMI70FEtIWvB-fdoQqmYkesKeb7YJvOvuWVhQZFFFryOiZN-XTCr7PUtzwjtoKlyIulRCG9kHfQACetsbYN_mFB04vEAwAd3Mtfpz1zQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند نکته از پیام صریح رهبر انقلاب دربارۀ تفاهم نامه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/443487" target="_blank">📅 21:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f7449320.mp4?token=NQypc-LYVir1DbahNRCTDEuOy5xFbDg2bxhgwCnpS75SIdqTJslKDOvGOEwoKBRuVXrw7mJ6PQoWSW-ZBBq2zuxurf1zaintd4yfBOM49aD4wiwVXpWcmXrWfkpiq0NcN8tQXfRLRytp5nC83IhGHskQ7XUbicA12N8BOn0ClrMp5hWkKjmAhUQ577_akn5kIT4cW2LS-b5BVpg128owkrgvgIFzCIUd6sZmVdzm24C18VodT1F6yidPzjeEeq_s7-KkbV6Go_lg0s6PaCw1Q0dL_TMS4RhKm5V0Y9iZ4sS0ZjMC54GUzVv8BcVweE5k8jnbEWFx9vNrSwzD2av8UXOrKrR-6uG5keQLFJMrj1kfX2Ub-p01EQm-7ky9t1q3qEhBvtq-44OqHFtZZc_NHUSevjeIWGeoPBtSnhtEmSO1TKK5eKftkbPF_leHJMzwydekYwKij8wuKyguzYkOf9nZ2bNZ_UJz79c9ocqDX5oFnJ1z6qs5clFP9hbtau9BXRY8vtNr0uNA1lq5oDz678gNNB2MAmAr0WxdSd4EGAnPAZwSfy9EW1e_6pE-S1yyowJNMsxPfaID7zku_g4gimmXNlC0SYskSSgSNGjhPSWOxYjX7P1uZa3hyqEbbHZMDBt-xL0bNT0sM1BuomT2sVa4-eXZWBwhRFGgOJvEopc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f7449320.mp4?token=NQypc-LYVir1DbahNRCTDEuOy5xFbDg2bxhgwCnpS75SIdqTJslKDOvGOEwoKBRuVXrw7mJ6PQoWSW-ZBBq2zuxurf1zaintd4yfBOM49aD4wiwVXpWcmXrWfkpiq0NcN8tQXfRLRytp5nC83IhGHskQ7XUbicA12N8BOn0ClrMp5hWkKjmAhUQ577_akn5kIT4cW2LS-b5BVpg128owkrgvgIFzCIUd6sZmVdzm24C18VodT1F6yidPzjeEeq_s7-KkbV6Go_lg0s6PaCw1Q0dL_TMS4RhKm5V0Y9iZ4sS0ZjMC54GUzVv8BcVweE5k8jnbEWFx9vNrSwzD2av8UXOrKrR-6uG5keQLFJMrj1kfX2Ub-p01EQm-7ky9t1q3qEhBvtq-44OqHFtZZc_NHUSevjeIWGeoPBtSnhtEmSO1TKK5eKftkbPF_leHJMzwydekYwKij8wuKyguzYkOf9nZ2bNZ_UJz79c9ocqDX5oFnJ1z6qs5clFP9hbtau9BXRY8vtNr0uNA1lq5oDz678gNNB2MAmAr0WxdSd4EGAnPAZwSfy9EW1e_6pE-S1yyowJNMsxPfaID7zku_g4gimmXNlC0SYskSSgSNGjhPSWOxYjX7P1uZa3hyqEbbHZMDBt-xL0bNT0sM1BuomT2sVa4-eXZWBwhRFGgOJvEopc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای قیمت‌های فضایی در بازار موتورسیکلت
🔹
سازمان حمایت: با گران‌فروشان بازار موتورسیکلت برخورد می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/443486" target="_blank">📅 21:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f7d6b0e3.mp4?token=LcVYQJnw5k6UFYUpQs3QLxdDfzgBpCCOIoiCIqUNriCwWhwN6ThaHt-sWUUM2Pf7dzyjgDAtstoFY2H7VnUBd5sB7yPVIMV_fRaEE2EVifJOFTCHKPFiztLWJTwdvX0TBo1ZcKRhy7w6bOYUIBn8CVNKMvJvR7cj-s1RV3ZcolDzbaKH-5_89SsHf_tT7GKjMMhTOLZHndhNHW0WtCYjui-3QpNkLCFUsZYOg4eIkRb_ESqGLOln4_pqSOTDjZsLYr1fpbPUJIvXfjH61GpLVfDCN54Q-XJ1Hi_uXK-2Fayz1KgwZg7ZuxJkM19KUcjqz2JdZF7riIArch_vYrKMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f7d6b0e3.mp4?token=LcVYQJnw5k6UFYUpQs3QLxdDfzgBpCCOIoiCIqUNriCwWhwN6ThaHt-sWUUM2Pf7dzyjgDAtstoFY2H7VnUBd5sB7yPVIMV_fRaEE2EVifJOFTCHKPFiztLWJTwdvX0TBo1ZcKRhy7w6bOYUIBn8CVNKMvJvR7cj-s1RV3ZcolDzbaKH-5_89SsHf_tT7GKjMMhTOLZHndhNHW0WtCYjui-3QpNkLCFUsZYOg4eIkRb_ESqGLOln4_pqSOTDjZsLYr1fpbPUJIvXfjH61GpLVfDCN54Q-XJ1Hi_uXK-2Fayz1KgwZg7ZuxJkM19KUcjqz2JdZF7riIArch_vYrKMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تمجید کاپیتان بلژیک از طارمی و رضائیان تا مصاحبۀ جنجالی دستیار قلعه‌نویی
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/443485" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443484">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34dfd69ee.mp4?token=pKJ10Y1QgWqEgCs7dO7LUtzLfwLHC3mBpOFD51XxoXkFWeVSW9w4ZzG4Y2uWRWXiR9qwbXgvj6KwMfwINg_yG4z8Nq5sgl7eFbrPBOx-2SsQglg8hEk_UXIrmr76m9qBlxIY4dGlNtNznW21QbzplXHpIDPhxFgB2Ms4xrl24KaGj24nVsQKwtCOLzJePsJ3peFssYm0unzLfmxPWsJlznccHwLCWIq8O8FgcrLmt7UPfnZpWr0CiCQWgINQXkdVrNTplwIUJpBIGdyUKetOJxBHFh-QumWeObiVKsPUEUNKut6y6RF4yhbtwlRIfKAY16IJcMi2GHyGsIcjFLGJcqrNVVr93eiRzrglp6PqfU_dPcv-Ih6tZlaup7P5FyBYjZJkCeRTyCsWxTPxeAU8eSVnclyfmTlFVZjp9pWb4Gmfii8s9xj66QlRElv9vMSWKStXWgKHKgmvMT6kNqhsss2Tk6HLcFssNoghKMkmxmKdRh8LrFnDhswoin3yjw3p50-_dI3pQSNTnBTpHeRFOdk2rk6QTe0d4zu1G_phe5VJ2sNXk8PuJZdjmpyvUGwM9GP4WVJTX-AWd8iIht2Cv3CGntoVh5meqg98dANNinsSnNlsIXGbFOu2zdwigrUe2GDRvBfYdajvAo9w7PV2sNOTtpwhDgQ7ErOmYl0ffQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34dfd69ee.mp4?token=pKJ10Y1QgWqEgCs7dO7LUtzLfwLHC3mBpOFD51XxoXkFWeVSW9w4ZzG4Y2uWRWXiR9qwbXgvj6KwMfwINg_yG4z8Nq5sgl7eFbrPBOx-2SsQglg8hEk_UXIrmr76m9qBlxIY4dGlNtNznW21QbzplXHpIDPhxFgB2Ms4xrl24KaGj24nVsQKwtCOLzJePsJ3peFssYm0unzLfmxPWsJlznccHwLCWIq8O8FgcrLmt7UPfnZpWr0CiCQWgINQXkdVrNTplwIUJpBIGdyUKetOJxBHFh-QumWeObiVKsPUEUNKut6y6RF4yhbtwlRIfKAY16IJcMi2GHyGsIcjFLGJcqrNVVr93eiRzrglp6PqfU_dPcv-Ih6tZlaup7P5FyBYjZJkCeRTyCsWxTPxeAU8eSVnclyfmTlFVZjp9pWb4Gmfii8s9xj66QlRElv9vMSWKStXWgKHKgmvMT6kNqhsss2Tk6HLcFssNoghKMkmxmKdRh8LrFnDhswoin3yjw3p50-_dI3pQSNTnBTpHeRFOdk2rk6QTe0d4zu1G_phe5VJ2sNXk8PuJZdjmpyvUGwM9GP4WVJTX-AWd8iIht2Cv3CGntoVh5meqg98dANNinsSnNlsIXGbFOu2zdwigrUe2GDRvBfYdajvAo9w7PV2sNOTtpwhDgQ7ErOmYl0ffQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گذشت رهبر انقلاب از نظر خود دربارۀ تفاهم‌‌نامه با آمریکا را نشانۀ چه می‌دانند؟
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/443484" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57be3295c2.mp4?token=oCHl9ATpAgKBdnjE_qCK6Q3TzA7RhkaQEwO4lrvOFNHacKSJ1m_CoPE2lFiBKnhYNsR599r651IEU5duQ8d07QosMHQvUH68nGJSy-o-v0hTt7TYSIWZvXIzN8yzTTMywpqdGL_6SMaiDHBG66EyNU6g89mMDrQT1nHQatjSsHyy20mefExyPDWdqeAubrHBKg0ofcAsBTWg4cCCQN9w-_fFFG7-dsOU0FJstKs0bxF0pHe0kUB2WNTqzo65kUGUw3h0GIRBuQ7h6wmPBG1-sALK42x03NpwtFobgL-mwKRrtgQA_O1X4ZXMA01yrTYUNkkeH370fS6eW6a2r_KErKbL69BO5TGhFGbEgxxXDnb60icOWe6d5g_T3Vzcm2x8wsL2yphckTDNV2nMxArMFNScv7BfGkMUOabpKrz0QVFyi-Rb6MgdgwQTisOuE-KiMNUcD_qk9TYOWdkMgnCqSuH4J2rpMuOl3dqWZpkGr3tXEI7_S4Q93Fag7uiXHqJETZLMMjvOio0Gk3IaYHzIDixEXCrbCK84xahzTEhcuvn7RlqlAotZoXs_j1Ks3KUtcB62c4M1QVDQH_pvMmGsmcoJ3ZqwNbUE10Tt3DoIZfz6-07xdO_qtDNGD4HvFOqJl9b49fV_BB7Z3HvOWOztNHzfmyL5d8UUZpEfknOUloM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57be3295c2.mp4?token=oCHl9ATpAgKBdnjE_qCK6Q3TzA7RhkaQEwO4lrvOFNHacKSJ1m_CoPE2lFiBKnhYNsR599r651IEU5duQ8d07QosMHQvUH68nGJSy-o-v0hTt7TYSIWZvXIzN8yzTTMywpqdGL_6SMaiDHBG66EyNU6g89mMDrQT1nHQatjSsHyy20mefExyPDWdqeAubrHBKg0ofcAsBTWg4cCCQN9w-_fFFG7-dsOU0FJstKs0bxF0pHe0kUB2WNTqzo65kUGUw3h0GIRBuQ7h6wmPBG1-sALK42x03NpwtFobgL-mwKRrtgQA_O1X4ZXMA01yrTYUNkkeH370fS6eW6a2r_KErKbL69BO5TGhFGbEgxxXDnb60icOWe6d5g_T3Vzcm2x8wsL2yphckTDNV2nMxArMFNScv7BfGkMUOabpKrz0QVFyi-Rb6MgdgwQTisOuE-KiMNUcD_qk9TYOWdkMgnCqSuH4J2rpMuOl3dqWZpkGr3tXEI7_S4Q93Fag7uiXHqJETZLMMjvOio0Gk3IaYHzIDixEXCrbCK84xahzTEhcuvn7RlqlAotZoXs_j1Ks3KUtcB62c4M1QVDQH_pvMmGsmcoJ3ZqwNbUE10Tt3DoIZfz6-07xdO_qtDNGD4HvFOqJl9b49fV_BB7Z3HvOWOztNHzfmyL5d8UUZpEfknOUloM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بس‌هایی که نقض آن توسط اسرائیل تکراری شده
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/443483" target="_blank">📅 20:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اطلاعیهٔ صداوسیما دربارهٔ اظهارات یک نماینده مجلس در شبکهٔ خبر
🔹
صداوسیما: «اظهارات یکی از نمایندگان مجلس که در برنامهٔ زندهٔ امروز شبکه خبر مطرح شده و در آن به‌صورت ناقص و مخدوش به برخی اسناد طبقه‌بندی‌شده و مکاتبات مسئولان عالی کشور اشاره شده است، مصداق تخلف قانونی است و پیگرد قضایی خواهد داشت.
🔹
صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار داده است.
🔹
همچنین شبکه خبر با ابراز تأسف از بی‌توجهی این مهمان به موازین اخلاقی و الزامات آنتن زنده، اعلام کرد مدیریت شبکه ضمن پذیرش استعفای مدیرکل مربوطه، به‌دلیل سهل‌انگاری و بی‌توجهی به ضوابط حرفه‌ای برنامه‌های زنده، برخوردهای انضباطی لازم را اعمال خواهد کرد.»
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/443482" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: قدرت، تنها تضمین واقعی در برابر دشمن است
🔹
اکبرزاده: دشمن زمانی عقب‌نشینی می‌کند که قدرت شما را ببیند، نه اینکه دلش برای شما بسوزد.
🔹
ملت ایران با ایمان و اراده توانست دشمنی را که تا دندان مسلح بود شکست دهد و امروز نیز جمهوری اسلامی به قدرت برتر منطقه تبدیل شده است.
🔹
اگر دشمن تعهدات خود را رعایت نکند، جمهوری اسلامی هرگز عقب‌نشینی نخواهد کرد و ما برای گرفتن حق خود، نه برای امتیاز دادن، مذاکره می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/443481" target="_blank">📅 20:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">الجزیره: نخست‌وزیر و فرمانده ارتش پاکستان به سوئیس می‌روند
🔹
شبکه خبری به نقل از یک منبع دولتی پاکستان گزارش داد نخست‌وزیر و فرمانده ارتش این کشور، فردا یکشنبه به سوئیس خواهند رفت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/443479" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a78498d54.mp4?token=a9ubCPg4YpeUYoEzDw2q9lMCrDgIql3uTc0bK54VTqfUzOdmdF7eQUemvkZzROTQP1eenKTOWAzNnFskVDZ10KgfL8rkME6oUHLOOM8ifh-V_6YwI9yyEwjEJw9H4L1L7atJEDUwkfU53K3Fc4nRlLNDw3-ijLQ6sXTVpcQ-Jj8HGKN74ibxYubHt974Lyrs9cEe1y0dejwPczlWTdYBrw4Gcevg5MLBbXJhq7LQ96p5R2UJFZ6waCCcs6vKwPpAWfdhp0jygG4mNL32ALu7BZLJGjdLWb-lwpPVOnUG7YvzfC3vvwMrP8aKAfSlDvfK9BtdDlidy2ZjaBv5cWZ4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a78498d54.mp4?token=a9ubCPg4YpeUYoEzDw2q9lMCrDgIql3uTc0bK54VTqfUzOdmdF7eQUemvkZzROTQP1eenKTOWAzNnFskVDZ10KgfL8rkME6oUHLOOM8ifh-V_6YwI9yyEwjEJw9H4L1L7atJEDUwkfU53K3Fc4nRlLNDw3-ijLQ6sXTVpcQ-Jj8HGKN74ibxYubHt974Lyrs9cEe1y0dejwPczlWTdYBrw4Gcevg5MLBbXJhq7LQ96p5R2UJFZ6waCCcs6vKwPpAWfdhp0jygG4mNL32ALu7BZLJGjdLWb-lwpPVOnUG7YvzfC3vvwMrP8aKAfSlDvfK9BtdDlidy2ZjaBv5cWZ4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مورد عجیب وینیسیوس جونیور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/443478" target="_blank">📅 20:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS2trs4-y-W0hsw9nA-XmjHubXv5DsSaDSv811bFS-a4hPbwzgHI-lO2TmdXc6pBZRCOSDBVIiE2KgUmvK3uwjWziIeUHRY2Ved1kNUXCA6eY0WP8CNYDMBVgZtcYE5INNpXzX3fxFMsD-Fdk6_Us5pAZj4Ew0UvO4fX0L6Md5i6R2uxpL3Npc0cpQUTfjuBYxIXJOjLajm14COnlItj-108R3zlFNlWcqBe9cnypTT4ZR8EK4agI064-VLq9_uFDFatNk1j_l5xkHfSWbhNA60TfB7QpbJq0JBKbvDUar6TI3LM0vVg1nHER4vvJBuaLbwoKt4JSM13-yphtYMVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستارۀ جوان والیبال ایران به بهترین تیم جهان پیوست
🔹
متین حسینی، پدیدۀ والیبال ایران، پس از درخشش در رقابت‌های قهرمانی جوانان جهان، رسماً به تیم پروجای ایتالیا پیوست؛ باشگاهی که از قدرت‌های اصلی والیبال جهان و اروپا به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/443477" target="_blank">📅 20:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM4SqAzzu4qxSeZ9s2xUa9Ga_1VwLZkv8G9cZLQl5ssR_tb6kSppnPN3vqS8PzUWvxso__ASA6lXMdocP2imn3apIfSiUysRYp3SBGhaUQl7GNQsAAFzmSqHmR_5r4FkHsH8E6C50u--gHIhfVgSlpC0422ndVAks6CjABb0uO0TwWKRL8301KPT3gkU5KIbFcpKjgrO7ClCvq0HtA83uxD2Yj05Id-CHoXyueyrP3zTzC0B90c98COpDEDMPEN3p12HKYuZGqx8bX8KzBRJd1XZ5IcQJNdzJZdQazVwSEFTdZM3EAoCSIG_e2AfkD22Xaw8aiuQd_gBI8uPRuJ6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ساترا مخالفان پرشماری دارد؟
🔹
در روزهای گذشته بخش‌هایی از سریال «بدنام» با عنوان نسخه سانسورشده یک صحنه اروتیک منتشر شد. اما اگر از حواشی مربوط به بن‌مایه داستان آن بگذریم، این تنها نمونه نیست.
🔹
بخشی از انتقادها به ساترا از سوی فعالان اقتصادی مطرح می‌شود که طبیعتاً خواهان آزادی عمل بیشتر هستند.
🔹
این مطالبه تا حدی قابل درک است؛ اما از سوی دیگر، نمی‌توان فراموش کرد که رسانه صرفاً یک کسب‌وکار نیست.
🔹
بخش دیگری از مخالفان، اساساً با اصل مداخله حاکمیت در حوزه رسانه مخالف‌اند.
🔹
هرچند این دیدگاه در محافل دانشگاهی طرفدارانی دارد، اما تجربه جهانی نشان داده است که حتی پیشرفته‌ترین کشورهای دنیا نیز از تنظیم‌گری رسانه‌ای صرف‌نظر نکرده‌اند.
🔹
اما شاید مهم‌ترین نکته این باشد که تضعیف هر نهاد تنظیم‌گر، پیش از آنکه به نفع مردم باشد، به نفع بازیگرانی است که از نبود قواعد شفاف سود می‌برند.
🔹
بحث اصلی بر سر «چگونگی تنظیم‌گری» است، نه «اصل تنظیم‌گری». هرچه نقش یک نهاد در تنظیم قواعد بازی جدی‌تر باشد، مخالفت‌ها با آن نیز بیشتر خواهد شد. این واقعیتی است که ساترا نیز از آن مستثنا نیست.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/443476" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501eaf8008.mp4?token=oCPyacZjEDH8eUySck5vm_8a0FzW1Siu4kBQ0toVW9Gcq6NMzbiUmf_J7z8MTA4FUZrsMLWHIBfow-Axt45FJMJrGsC3zC4piOSnEwDVW_s4gWmGATm6XWrjDKP5rW-rYhtsirSFVBcTEQ9QOkQ9_IJlRCzJSd14v_i-cvRbbe0dVikQpqH6fcDWrsb6cFaUpe4FcttA1N4R5c9s7Vo-KqOOX5uR6iP771L6K2B3IZ6ZS_HZJCbJoGxGZQ6sOgr9znYpZ1FR3EYzJKvzojAtW58ngMZcodcvJFs9BuJg5LctD_fBssB3w0YNJ8TzG7pteTMwFThUIa_ipmV0EgAu3BGrn1Wj96VHGB-t0nELpAeHChUQ8JYY8PV7LCLp8QaZJs2pRf8Q6QUAqBxiG_YH6Dl_Ovxx-YuDYI2xTd22h0_lJCCD_c0rwSKjMERQgHdWyWuOI6vXqdzCK4sf8yhVlDVlChRcAbfUhEpbmg4W8k0SlT0RF-D0t1Pv3Ac9mWkJYweugZuOdP7_zi5bQjQ_JjcpcYqKloaICK2R-hd6x8YeFBrm89qkWfGn4o6EgyvDEy_T8FgCuLG4q_7-U5PIQXPJbVbKbm4QZaBYDCW2Z4iLel71koFDUYBURllfiQUAgJ1scCSoaogFvMfrB_SqPpEUsvh3RKjHvGksxrNn7xI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501eaf8008.mp4?token=oCPyacZjEDH8eUySck5vm_8a0FzW1Siu4kBQ0toVW9Gcq6NMzbiUmf_J7z8MTA4FUZrsMLWHIBfow-Axt45FJMJrGsC3zC4piOSnEwDVW_s4gWmGATm6XWrjDKP5rW-rYhtsirSFVBcTEQ9QOkQ9_IJlRCzJSd14v_i-cvRbbe0dVikQpqH6fcDWrsb6cFaUpe4FcttA1N4R5c9s7Vo-KqOOX5uR6iP771L6K2B3IZ6ZS_HZJCbJoGxGZQ6sOgr9znYpZ1FR3EYzJKvzojAtW58ngMZcodcvJFs9BuJg5LctD_fBssB3w0YNJ8TzG7pteTMwFThUIa_ipmV0EgAu3BGrn1Wj96VHGB-t0nELpAeHChUQ8JYY8PV7LCLp8QaZJs2pRf8Q6QUAqBxiG_YH6Dl_Ovxx-YuDYI2xTd22h0_lJCCD_c0rwSKjMERQgHdWyWuOI6vXqdzCK4sf8yhVlDVlChRcAbfUhEpbmg4W8k0SlT0RF-D0t1Pv3Ac9mWkJYweugZuOdP7_zi5bQjQ_JjcpcYqKloaICK2R-hd6x8YeFBrm89qkWfGn4o6EgyvDEy_T8FgCuLG4q_7-U5PIQXPJbVbKbm4QZaBYDCW2Z4iLel71koFDUYBURllfiQUAgJ1scCSoaogFvMfrB_SqPpEUsvh3RKjHvGksxrNn7xI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازرس کل وزارت صمت: فولاد مبارکه در جنگ اقتصادی سربلند شد
محمود صلبی، بازرس قضایی و بازرس کل امور صنعت، معدن و تجارت، در بازدید از فولاد مبارکه با تقدیر از عملکرد مدیران و کارکنان این مجموعه، راه‌اندازی مجدد خطوط تولید در مدت ۴۵ روز پس از تخریب کامل و عرضه به‌موقع محصولات فولادی را اقدامی مؤثر در تنظیم بازار و جلوگیری از کمبود کالا در کشور دانست. وی تأکید کرد فولاد مبارکه در شرایط جنگ اقتصادی در خط مقدم تولید قرار داشت و با تلاش شبانه‌روزی مدیران و کارکنان، ضمن حفظ چرخه تأمین فولاد، نقش مهمی در مدیریت بازار و پشتیبانی از صنایع مختلف ایفا کرد.
@farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/443475" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNBkLbV21j2zAyRfVnOUpnFN0zciaN0WYo9vg7y97rsrZzAxOv7dLQpCWlG_mhhjWn5yjXvTAota5d5EyxF_Bocr3o1k46_hjS6oycUGGtNx4GrQEFqOVo8tgQSU_049619oUhMMyC57AXtph_g5Ylu--CXBr_VLwI7cw11Z5LHbcLDKldvXlm9MB7uwW5qiSBycBH9Ye0tzlFKeos_oxdITyUAjeOceS2MO3stAFCWf3EW0zH8VjoE7__a1WA4W85mpfTJZVZOSXbas2je6AEsyDkgNLdNKourGrC0TUocoY9M5WfHmZ5Cru0-IYSOtpOd9lNu1PmTEKJ5t03cxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سقای شهر»؛ پیوند خدمات بانکی با خدمت‌رسانی به زائران اربعین
🟢
بانک شهر همزمان با آغاز ماه محرم از اجرای طرحی با عنوان «سقای شهر» خبر داد؛ طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا می‌شود.
🟢
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه خواهد داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می‌کنند. این امتیازها در نهایت به بطری‌های آب آشامیدنی تبدیل شده و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع خواهد شد.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/443474" target="_blank">📅 20:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/443473" target="_blank">📅 20:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d88bd8e6.mp4?token=I2Rj1aufIBcCSmXekx8OYB4wcg01lKKivBpPRvpyiiEbv8_Ud20ASl2idA5fprWHV6t6RM2ayMz_2udZp1W1v1VntTfhQwo77muvB6_BXFDmLk7Lnf0hitnsWWA1q2YBsDQm2COTDd_-V3ZeuP8CbqMId76ZnqKfUkb6G4HSVZ-yXIrlV-nyttyUTyYaJwdVUnbD9sep-w4Y6gw-wPmeham7wZoZKftd-oWPUpbDyLIiD0WrSLevRVJ_hWZPS9adUnbrmEoX3Vqid_SDX6JyIPxJC-1YrsPookzrOuSj0EmkG1Dc9cAhVPBFzPny8_poCFMqUu2fYymG8xvNIVU27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d88bd8e6.mp4?token=I2Rj1aufIBcCSmXekx8OYB4wcg01lKKivBpPRvpyiiEbv8_Ud20ASl2idA5fprWHV6t6RM2ayMz_2udZp1W1v1VntTfhQwo77muvB6_BXFDmLk7Lnf0hitnsWWA1q2YBsDQm2COTDd_-V3ZeuP8CbqMId76ZnqKfUkb6G4HSVZ-yXIrlV-nyttyUTyYaJwdVUnbD9sep-w4Y6gw-wPmeham7wZoZKftd-oWPUpbDyLIiD0WrSLevRVJ_hWZPS9adUnbrmEoX3Vqid_SDX6JyIPxJC-1YrsPookzrOuSj0EmkG1Dc9cAhVPBFzPny8_poCFMqUu2fYymG8xvNIVU27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای زیبای حسین طاهری در وصف قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/443472" target="_blank">📅 19:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da9c41bdd2.mp4?token=RCvVU2aja8-tQjm89CpRRILYZ7Pcuj5X9FFFM1xC5SJCP4vfu8d7Vjirm1lI_QwxFnaXrjKvSWDoPIWaqo2Yp0m_hXzsD4ZV6OrIQCV3Oef5PiqlNO74AMM-LQDXFyjWXbtyaAXl3ugGjfFeTvuVhQ0zsVCw2kfK0pRLquraq13H0RwzPr2nNlq4U-ahMbBkrW3Ygk3UEhOMs1kVLsQXxrso3G_27h2kdcyTHnTcu1gQ75VqR7B44GFA131WR9Pv8yRiPaB1GGqRv_yopaBYMkGSAV3ZTEjy4jRbJKqklQTWgcnG1ofr8iLISvbfzYAJBas04fHY_3M9mxKsOgHMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da9c41bdd2.mp4?token=RCvVU2aja8-tQjm89CpRRILYZ7Pcuj5X9FFFM1xC5SJCP4vfu8d7Vjirm1lI_QwxFnaXrjKvSWDoPIWaqo2Yp0m_hXzsD4ZV6OrIQCV3Oef5PiqlNO74AMM-LQDXFyjWXbtyaAXl3ugGjfFeTvuVhQ0zsVCw2kfK0pRLquraq13H0RwzPr2nNlq4U-ahMbBkrW3Ygk3UEhOMs1kVLsQXxrso3G_27h2kdcyTHnTcu1gQ75VqR7B44GFA131WR9Pv8yRiPaB1GGqRv_yopaBYMkGSAV3ZTEjy4jRbJKqklQTWgcnG1ofr8iLISvbfzYAJBas04fHY_3M9mxKsOgHMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقاشی جدید سیدعلی میرفتاح برای مریم، کودک شهید میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/443471" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK5HZaDPXlyUiKQCh3hx76Yw5ghySnQNBnftApT9jP21Eqtx7yeOuXKOkeWc3eR-M08eAzK_e7cPmYDMAXnhrl-7t6gZH36HHMpsJXrk0x6xqEUpHcPD8QliEJDVjRDZSDLbfWP7FcEnaeTV2F3cvK3rKZfT53fTOSnd2WNidvTfq6B6Ymoyf2ZTkKSizgIJTKcFLsmS7JXZm2jsAiL8LdDe7oKN0mVI_IOoDgbPKVZyihxPZ4kyfUKgCF1NI5q9jHFNj1UFI0vv8xib_5AcuPziOXDL0uaPUPYy51M9lQ1baPG0MLNCo4L1AjeoVaE5hLy6Nki8NTYdIsGbC77IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس فرانسه ۲۰ نفر از طرفداران منافقین را در پاریس دستگیر کرد
🔹
صدها نفر از طرفداران منافقین، روز شنبه با وجود ممنوعیت اعلام‌شده از سوی پلیس فرانسه، در میدان ووبان پاریس تجمع کردند و نیروهای پلیس پس از متفرق کردن این تجمع، به گفته برگزارکنندگان، ۲۰ نفر را بازداشت کرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/443469" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pawTBLLQHxbV58vCCW1u_Ty7J9e_H5PvSyCQjZaYMq9ZrBQ8wt7Rr5-D0Y8vDHeYmcTfQC9CYdtAVEDsjCgkC3TXlwl5a0DkBU1p_hRtDISqX4JIlU07quvWgMhi2Skk8lXF90ZMc4fwklqZoazxsbMlXYx27FYfa-I-PPYFJA8ccsX8FxZPVHPqNDc1r-XKOz_SPqftnDIcIJUuyNEAYTk_5lNuc0Rr_Z_AFnPOnvFeBYJaPtLge0t9bL-5EuSJYxmEEJ2eTwIFuB2G8AeJ6tutBE9Al5admGZHXzDrox1dtm65ICuX64kj4uZjaG5S30eG0qhebpsmvSnBmw9tFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند
🔹
آمریکایی‌ها زبان اقتصاد و هزینه-فایده را بهتر می‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/443468" target="_blank">📅 19:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a831fe169.mp4?token=X4cpQsboY71zEELTRctDEBOyzqGE2U1wLLEnVF4fCvPvcR8XwmkDhMhTRtlSsCJtDYAKp5Z-MLu9LhvljcLTMKwZiqVf0OfsmFIW7ooH7DitrbItw9_-rglnq0MU5RxjMdHxT9ALAUAH7ttNBrcJtNE2GU4wPOjDOu-GMQ1qGi4nSz27SvS0p8ONIj21X1g9EASQESnnQb6suvPn2khSClCbUh-cqeIukgaRwUzDfEihXle57_hqhveIKqrEmid0aGKeFfJ2cHGSRiBvIpWa903aj8xohBPaeRlMs9dA3Wco3QbhE0p8TX1-PxdoDV_k30_HsgcapUvSLE2a4vxhyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a831fe169.mp4?token=X4cpQsboY71zEELTRctDEBOyzqGE2U1wLLEnVF4fCvPvcR8XwmkDhMhTRtlSsCJtDYAKp5Z-MLu9LhvljcLTMKwZiqVf0OfsmFIW7ooH7DitrbItw9_-rglnq0MU5RxjMdHxT9ALAUAH7ttNBrcJtNE2GU4wPOjDOu-GMQ1qGi4nSz27SvS0p8ONIj21X1g9EASQESnnQb6suvPn2khSClCbUh-cqeIukgaRwUzDfEihXle57_hqhveIKqrEmid0aGKeFfJ2cHGSRiBvIpWa903aj8xohBPaeRlMs9dA3Wco3QbhE0p8TX1-PxdoDV_k30_HsgcapUvSLE2a4vxhyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نیروی دریایی سپاه: شناورها به تنگۀ هرمز نزدیک نشوند
🔹
با توجه به جنایات رژیم صهیونیستی در لبنان و نقض تعهدات امریکا در  برقراری آتش بس، تنگه هرمز بر روی همه شناورها بسته می باشد.
🔹
تاکید می‌گردد تنگۀ هرمز بسته است و شناورها به تنگه هرمز نزدیک نشوند؛ درغیراین‌صورت…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/443467" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e18ad3888.mp4?token=qDdq5vTxGJ4i2YpsfpzX3nv8J7wLZAvGTnyZXrRf2_MOjdshjLbkXRYIPWvJDaUwzwEbdvdk5B6RahxzXUWZVgVp2R5BcovCAb5QMQQosBXsi-hliMrYQ2VK06Fdy3I1wXId97Tk7LR-A-kACegE692KRLGruF45IspaOAc51k3oHQHqEsjAKWlh1q1jZ5qZFnDouU0xWd5lxJfaWq8_GI2qzWKlzDXTqUleotaviyEJgd0L96uDNOVMxWn5XuX-_BtwZreyQCwKT-vfdQPCXE80cJ739gXC41UBJcvIMUHcQhsxhvz09QitJDDzuOvIgA6csQqux0yw5Tg6KvzpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e18ad3888.mp4?token=qDdq5vTxGJ4i2YpsfpzX3nv8J7wLZAvGTnyZXrRf2_MOjdshjLbkXRYIPWvJDaUwzwEbdvdk5B6RahxzXUWZVgVp2R5BcovCAb5QMQQosBXsi-hliMrYQ2VK06Fdy3I1wXId97Tk7LR-A-kACegE692KRLGruF45IspaOAc51k3oHQHqEsjAKWlh1q1jZ5qZFnDouU0xWd5lxJfaWq8_GI2qzWKlzDXTqUleotaviyEJgd0L96uDNOVMxWn5XuX-_BtwZreyQCwKT-vfdQPCXE80cJ739gXC41UBJcvIMUHcQhsxhvz09QitJDDzuOvIgA6csQqux0yw5Tg6KvzpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت المیرا شریفی مقدم از زمان حمله به ساختمان صداو‌سیما
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/443466" target="_blank">📅 19:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh5Nv6uGMnYIRNFYMCf4_ZeojCKZQJ_Vz3XR7cdNjNZMGOU1Ahea7y1wQpXCZMJlfBBKAK-Uvku81VurfwV8Ymt7K4ndPPL7hdSWci1kJwF3iITfTVZL-QWU9N8w8unMyXGN55avCM0v3HJY_Modr_9-teFW0DhLGqOiTtGwrCNvzlHMMvnUYDXvHOksPcs6dn4edgNdGAfRa3wlk7bjOKQI3JXVyXhkh1QT4DLj1nmQNgUmpduzi9PjqNd4L1wGk7tDtHv5fDGPGHp9x5v9Yhg5Tu2SLCuxquP5hfWztewiwga8AtTUkBYevNLkdNNxazLO8owGEYXH_AosXyWD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران‌خودرو محصولاتش را کمی کمتر گران کرد!
🔹
ایران‌خودرو افزایش قیمت تعدادی از محصولات خود را اصلاح کرد. این کاهش در شرایطی رقم خورد که این شرکت در یک سال گذشته چندین بار قیمت خودروهایش را افزایش داده.
🔹
در این اصلاحیه تارا توربو حدود ۲۰ میلیون، دنا پلاس ۶…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443465" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نشست سران قوا برگزار شد
🔹
نشست سران ۳ قوه به میزبانی رئیس‌جمهور برگزار شد. در این نشست، آخرین تحولات کشور، روند مذاکرات پیش‌رو و راهکارهای جبران خسارات و بازسازی پس از جنگ اخیر، همچنین تقویت هماهنگی میان دستگاه‌ها و صیانت از منافع ملی بررسی شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443464" target="_blank">📅 18:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۲.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/farsna/443463" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443463" target="_blank">📅 18:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دستور نتانیاهو برای توقف عملیات در لبنان
🔹
شبکۀ ۱۲ رژیم صهیونیستی اعلام کرد که نخست‌وزیر و وزیر جنگ رژیم صهیونیستی به ارتش دستور داده‌اند بدون عقب‌نشینی از مواضع خود، تمامی عملیات‌ها در جنوب لبنان را متوقف کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443461" target="_blank">📅 18:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443460" target="_blank">📅 18:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsMInYdPOaW-8lyhA0Jbx9750pvYzyH2cjTRBCeb4J650qsWpmB5c3fP3nIXmiNOt7pfw23VA5EBbeUS5mf1dkjQOgG3xwlS-p3wbT6nQp3ruoiggyjFt6sM7I7P7Q0m31kBpQUrIHVifoLy0htecO2W161hRw1W_MpNaBx6KoQt_YvwsPUYfyO7GE7Wrm7fpoynBDwnx2luOC9sYgrL3n543j3KuhBOWQwI0u090zr1wwqDkVmuLZZ_o1UWc7e-APFg8IpzTCdkGrxDb7ys0SwPZRPhGXtnf8IIomK28Ww-AMVvM0Y9A4Uz4FLTl5sUgdgTd1ir2yqpHatBRPJKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enybS85QkmSER_xLAdY6d1qC8pkZiYVSCWx3EcO3NccipCoFz1HyClwzqmz9AjdrANKH3e7_rjzPkmH07Ptr7rTocWbTW7IgjDCVOGpy3VyVzxtWyboXZHngw5rINqYp0aDZRPp_HywxHGMNSESnAQHjIouamgUz2beX_pUXoLrzu8dfeFP7k2gihA0DKyCmCqfes3LZ_1kK71EprwNmdk7i0pw-Q75Vk-HggZnb-grrlN88fmJHY3dZdVBfSBoeFYOacvlD99hF_sRKbfHt51EpnVSAIjMGylfSw2Q88hNnKa95zvzuet5lljpBMGJc2NpJndTee93qBm-XUWWDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9tDXyRGR40QLvM528aSBmBaBMNr7vUIlXE55AzlANatNN6lvsiHnUKewQ79XNvCrvnwNVBqW89wYTcSSyJG66S0CmkrSbeJdHVde02-lPXlWBWErCj7046qGj4II8lQPo5DARhGVuH6wuK0wsNkySS25XExcIznAYMu8tIn4o1TP8MQ62qhIB1u82Ka9ZUlOQf3gNk6NJIJyWKMmGNYYOmFf__TuWO5dK-_YQ9EVBYTh4nw8s2xYSBkjPK2IhRWsXdsXuaFrpmh-S0XiCy6d4nyjv4k3_dRhc-O4sjuQHMdVDo1LxdwC5KwnKcp9Jjprjp3yo3MFIg4rzfwHT_w3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0xvhF6YW0RqPlmqbLpnrtCvQLAmDVmNmxLwh0o2wYrSCPTi56LEw1Qc91Q-me2N2UWTE75GvZleZNV5gIwflqS95vEWQjEXgha-qrf32wEsfrqcBTzkCO6xBgcF57sW0gLPSR3nE0ZqedqeQTVYft0ym8_t_tCRGU0K1K-BzX7wCnJ-ghCPGVPiwDkBk3Lb_cLzMzTPPPI7ZQjHI8731qfWTaWrX0Uwb5NYFvI8sLcmPH-989BYFKDnx1IbLawej76e4kdlfFXiyzCawttMSGdH7UzPi9GpxE-ivM3BDGb63c7H4LTi0Ik3D6DrOSaOA3eYIYqpggM5Oc4W-wZ7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVpWBpo43IiLqRzuKR1rWOkJWawMDOefbGLZJ1OvPOYyeQ9QNVEDVEMfUx--mFBMGd9EKxgiLqsL69ZmOHTlCoxkAh-AlsFBbA_GOPablUEtvVsYn1Y4FqOjrEALLObkypGZniyB4e6AIQNooWIaUkZhOz9zjTOy7FOoGK6z8qXYIEEVUuzw0vBReRlMt6MUCojDBCrC2DV9-cbNhvqh6Jv81Vf_W3myEmi8yDpHpmuADeN5BLYyiOc9KNm5Y9RqZxblijGScUuUw0vNirRpY0_POajJ422cJALIa-zvfYicp1Mld3ZjZvVcMpI-BRXofbLIbEi5k6xSWQojIYTpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tsqn-R76U-XSt1uRRyrSiYRiBzjHR1cXtzH28Xf_O04sf1QldgBVo9XR7F00e4VisCm_sI4X2GY781DpzcbkuSmIbG64_xHWrja5yZY_qBaPnqr4vEpyzaC5SSPd-gX63PUPjzEO6OK38cAbMm1YQC-yWa2g2mm1NpOVmbhn3o0PRfrjp2DgOvBIBiEq7fhayAsA08bqIHHjrxTj6iTnxa03J7HpCkn4dovYnp6-Z_xdla8K0CgjtAzf1yzS9BLDxue7RunOspmWMuAj981rcQ7qs-Iw49giaolIlUkvr-0_GYALPpVOxSwVzZxDEmn3-mR9QQNUTeVjfNi-Z4rKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMhsENxRhVVJlZ1qe6Kt2RbvL9LmPOJsOqh6qO74QgXtmD92d0PMvxRG-ANGu8z1dJbuTKwPNotAvt0zF07I-PB04eQewS5uoX0dRNab1Pb0lRlE5AbRO2tk_ODJhKt5kNkBuhg_toAjVZrv12EwfbQAaaQsXgEiwD_yTh5Wacv-NzVgm7S2qelTXafkSY5LvTQS-vwwycjwpgfwLs3e7TbzzRBeRK21JamflzrHgk4pl8RGcKBozOMHeW7qmWjaMh8Ma31h0SsP2V6WjPgbI6e9-Mje1YF2So9Uvcwe5xM8pnQkPPnu1WwNUjokCq2_2K13lL8ddWWKgOjE6AkmRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هرمز، ساحل سرخ ایستادگی
عکس:
حسن قائدی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443452" target="_blank">📅 18:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خروج یک هواپیما از باند فرودگاه مهرآباد
🔹
سازمان هواپیمایی: پرواز شماره ۴۱۶۹ مسیر شیراز به تهران، صبح امروز هنگام فرود در فرودگاه مهرآباد پس از آسیب‌دیدگی یکی از چرخ‌های فرود و کاهش سرعت، از باند خارج و در حاشیۀ آن متوقف شد. تمامی مسافران و خدمۀ پرواز در سلامت کامل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443451" target="_blank">📅 18:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c507c128c8.mp4?token=Prd2shcjz7bVONeRKU6KJJpApCoXz0pYMYIqV8B4w949lKfKFbAvbOJog8fI9SdeCuRZy3aTl_OMd4hjcmRoQUpw87TIj63bs2y7vCAp1AQjuuhvUp6GVwJHPmepjfoO6BONdr7RjWBk8o39q84dvGO0ErjxudzqgJha84FoPai01249tHD_rp1FacitmnYAhplh4LRAQpQgi7L7xJNmasTvDB--q36IGT2B9I99pKsmG6_NWLoOnbsJT4EikbEMGI-b4FfUtZuXwp4eupRWabLVcn9gF5M6XX9hMRlBZyaFKjs6UkbqWO0LC1w2aPb6xwtfJVLyON7Ldb10esnRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c507c128c8.mp4?token=Prd2shcjz7bVONeRKU6KJJpApCoXz0pYMYIqV8B4w949lKfKFbAvbOJog8fI9SdeCuRZy3aTl_OMd4hjcmRoQUpw87TIj63bs2y7vCAp1AQjuuhvUp6GVwJHPmepjfoO6BONdr7RjWBk8o39q84dvGO0ErjxudzqgJha84FoPai01249tHD_rp1FacitmnYAhplh4LRAQpQgi7L7xJNmasTvDB--q36IGT2B9I99pKsmG6_NWLoOnbsJT4EikbEMGI-b4FfUtZuXwp4eupRWabLVcn9gF5M6XX9hMRlBZyaFKjs6UkbqWO0LC1w2aPb6xwtfJVLyON7Ldb10esnRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، عضو کمیسیون اقتصادی مجلس: مقامات ایرانی، چین را کمتر از غرب تحویل می‌گیرند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443450" target="_blank">📅 17:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTujQLQHs6ResGqVVeueJaPgYWgBDGoq7zaQCczAZDxU_TU9bGLq62s6R_Lbg1yEJsEZE4I5_5jQI46yoYZk4lmHvHeKHbscvPFZ8ZNVfQnDQNOfgk1il0bpi7Qy5-sb11bNCp1vh0EXCBeZ2qu4bDJlwPkDiKXhcV9Jpw2WhVh5OFxOT8iFXRNSPrLhRpdzIk_b17GNLs2MfkdMTw8CJwzrCwzOcZiopAp8oQlroi6nfJjjY4FT6r2TyyAECcbNYjEy4P59kFg1UzC-jP9LkeBxnNjnKrRN5pFCHLYCQfTQ7b-3-wmbQzrFyDlQqD2wXu86fM-6X4pC8GET8fVHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwyn-TEPW2MdDTYJdkadfLgI6avXPWycpklRwxI_XnUPVD0nWWqVwm3TOy8Gmik8Co3Zf8sEwZNzvli4Cvt1uHbFJYrJyTRoGTHFeW09CweMKO9YfdKydoGpVbKLzv5xQ13oYpwPE3YudfX32vCaB6IokGESnLSRCOkCp7T1bErZcsK-pRKccqTxB0D9-dm9-gXuOIvBeDJB-l_IWNhM4pEI0zhowDJMADced_fef28X2ZiguFSwjs0o--PmcipWq3cruxmuVnr8pxP99QRNkBtIz5yXI-2rRDlEnWXHYpf6LJUUSoAseSeXvJQLcO9miQFC4Vmv7z0s6ZTEo8uZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zrs4wrSaImfY770QCemYV1yYaBuEtYiWcFI1-wy82Y3sfp1RIv8IsM3306sq5w9wmm_Vfwfi2qoBO5YmvTc9vtYMCDvrpqtcE2EJ7yqIk7XpP54vh131CUBbWdPlDu_iqj-m92DVggOQTJ6R_Dn1Q85yAi68FjBz366zE4xqIoA4Q5xU4FGqx9Gfxy2mT5BIBynQ7vkT9kI9OOzELSeSW9NMu3UXHWZfxx3JWrCBbtvcq1xFExaKUYacpwl7Dd_mzhbPVOW6PNMZf-TYfgr_HqUMpiCLHYpvODd_iQt4JIt4ObEEcYgZHsQC1kn2HZzu4rHqWirkFdpuMGsuH6E3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK8pMZCQTmeQpDN-FdjRExK0uSCragbmxuR8ed4ysNfo4hpYRs4wyYh5N6ezQaFqJhNso0GVb6fgMjlmKYNpScHT26W-7N9y7aTR2IITvHnhRw9Thu97XnCZoC1k9nX7SRYhx18YPoPsX9fQRinCUavdlt720E0G3RJzdzyxHivtSFQoB6HDl2aBrTLpbLxLqh_h4U9_pMIod9xdsga7O2_RheL2T2dHOsAved1Lmt12OZvnuuxNrFDzqq2z7JbflhMjm3X4zis4_pV9_Qc-Jk4_bee50XV6-TLwv_h4w-UX7oZ-tlPJ3AjrqKStYST14Vyteh24-hhDmVCJf87KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh4WqgIsVJlz8emZKF2Sbm8drVOPX61_2NuhCvey7MT9SogfdWG1PGK2YaIhyI7swIQzUXWJipPXtNE7Id4eoV_874pTo_X136YMRAgbkkVApi8TVmqQ8-R2ngR-_0k0d8BYfILB7tm7taWQ_qdTq5KTRiEjHmufsyU__dEStJNkdQpRjyc1bUy9dy0gH0__bDlmi6TblIxOsu3o0udS9CbnURm1WXyFpGyKHXPJyiS0WA4TpTpWgmsb339KzlWkjbKZxUDrg3VeObCNAVL8mfU0wKQM2ZLQDx9Fov05LvkidLctqb-cpdhtL9AWrpUS4gcgkBNfxHmbTjZycbaAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzPzOLEqMywrz-9n4TAx2pvZ1e62j6DJh3QCLqzHWET3N24iPRYqXf0uOZ-KLmG28TvGD5qludZVv0PVL6n0Cb_VYTchQLPImlpCqvohbPEzBik0odsRMPL-Q1SGD7dXhZEC8_59rZkAEfcaK0NiHxk0USSnufRXUuKRL08YFI7xMO5ZcM9BXysGIJTzhiBvLA5hwgSNYeu2H1aAd9YVRDOqCPEFDcSDeBAfC33BYzj08-qhyVYey4WXqG_XyvFHk_cMD2LvFS78Kgs6FdwdUHdOpG5T1tSeEHgHtMG6iMPadALo5yfYnh7fTg6JAH7ygBbgwYlFJ91MnTYTxgvLDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
دیدار وزیر کشور پاکستان با سید عباس عراقچی
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443444" target="_blank">📅 17:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtp3caGJtQf7Yvw-7DcEQdOLkkhi9a-rri8AjcGDpnsK4LSenGNPqNWrgLP_QDk-_gFvV_DiQp4PDBiEVdiPltb8UBYp1CP9IWY66ZGimvW8VE3Yb1i6e71IYc1lqCvzQYQaaA4hHkMlg3OJsVlFCea_K-Uftll21RigSdP8BG8PAXgcHfR0W6wF8_zG40Je0StyflcuxjSFP7USwB7_bNL7-JwEa3kQ_3Stmag3csVLFJzk7WgD0GAJuwmMMBekNllzV5vjDovAdIfrfMPnIarDbVYkKi2kKV7KZL1FZ-qtOqZ72Z4TPDCSHeBGUmz4fkj8YJ3D-niaK9hZt4E6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارلینک پس از پذیرش قوانین عراق، مجوز فعالیت گرفت
🔹
دولت عراق پس از ماه‌ها کشمکش، مجوز رسمی فعالیت اینترنت ماهواره‌ای استارلینک را صادر کرد و راه ورود این سرویس به بازار این کشور را هموار ساخت.
🔹
شرکت اسپیس ایکس برای کسب این مجوز، تن به قوانین و مقررات عراق داده و پذیرفته است که فعالیت خود را در چارچوب حاکمیت اطلاعاتی و تکنولوژیک این کشور پیش ببرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443443" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhWj4_h8v6FS5Y9VqOngJq2ln_jBObhz5hvUc5d6ovi0EAYEjp5tDg7Mp1J-wsl3mfgfUjmfBOgvVO6xBVX64J81RvpfrvVyaqKVHhasUap3H8ZfHuS6PotWL6UCi525zsbceaXl-0u_osRdMX7MFoAV86l7FUrhSLY8EvqLaceo4DOcuGhTBWdYUYKBJiYgPJ5oEtFfviIwojw0157XCgv6PAIo85xcQGudww8p-lMeGS1XkUU_LIKS8jSxjApka6EmPxi22DIMkwgcvKnZWalRHu4mK1zR05H1c9RYdyIFmRoFc7gYe4MQhnKpoEGM7ZhtUFabQpEiB3CHspJRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای لبنان از ۴۰۰۰ نفر عبور کرد
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات رژیم صهیونیستی تا به امروز، ۴ هزار و ۵۷ نفر شهید و ۱۲ هزار و ۱۲۱ نفر هم زخمی شدند.
🔸
این نهاد لبنانی می‌گوید در حملات روز گذشته اسرائیل به جنوب این کشور، ۸۳ نفر شهید و ۱۴۱ نفر نیز زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443442" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
یک منبع نظامی در نیروی دریایی سپاه: تنگۀ هرمز از دقایقی قبل به‌طور کامل بسته شد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443441" target="_blank">📅 17:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443440" target="_blank">📅 17:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اگر بخشی از تعهدات طرف مقابل اجرا نشود کلیت تفاهم دچار مشکل می‌شود
🔹
طرف مقابل باید هرچه سریع‌تر تدابیر لازم را به کار بگیرد وگرنه کلیت تفاهم دچار مشکل خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/443438" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه:  آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
🔹
ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443437" target="_blank">📅 17:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/443436" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/443435" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/443434" target="_blank">📅 16:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌کنیم که تنگۀ هرمز به روی تردد شناورها بسته خواهد شد.
🔹
اين گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبندکردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/443433" target="_blank">📅 16:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751d1e0b88.mp4?token=A030S116dKDyRIrYBYbA1QXPfHyt3PORz4CeIU2ZMP4L7qoYTrc7Me_FPi-buQ-FxC7uBQXi6DA8By4SVCtivCWrx3J7uhOBeUi4B1V8GNO16sRGwY90uOl5KILUqyg1cbimnEKFO5ZySZwqOuO68G3qBlVSBb3BEyIVmLh1o-7gLCvZi2K2G_5B1JPwRv-nKtXFu24QGK9P5xS3-iDxG25C4K8UUQ5MU4Oxsox37utU98Itss7O8-pgNz7qhZmZBUYtBMj16NjfTGaywS25y1Ao-3X5TdYReiI8Sjfo2ZfrRGSIqqy95VR3mdN7lSr9YTvsfqJHXvPRYSr36_r5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751d1e0b88.mp4?token=A030S116dKDyRIrYBYbA1QXPfHyt3PORz4CeIU2ZMP4L7qoYTrc7Me_FPi-buQ-FxC7uBQXi6DA8By4SVCtivCWrx3J7uhOBeUi4B1V8GNO16sRGwY90uOl5KILUqyg1cbimnEKFO5ZySZwqOuO68G3qBlVSBb3BEyIVmLh1o-7gLCvZi2K2G_5B1JPwRv-nKtXFu24QGK9P5xS3-iDxG25C4K8UUQ5MU4Oxsox37utU98Itss7O8-pgNz7qhZmZBUYtBMj16NjfTGaywS25y1Ao-3X5TdYReiI8Sjfo2ZfrRGSIqqy95VR3mdN7lSr9YTvsfqJHXvPRYSr36_r5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدام زیبای نوجوانان تهرانی‌ برای کودکان میناب
🔹
پیراهن تیم ملی، یک پیام جهانی:
🔸
«کودکان هدف نیستند.»
@Farsnart</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443432" target="_blank">📅 16:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu4Yz1HY7CbiwFK2pZMYrGLGfd4rY4aHo9bLgdojkydTQl7Bs33C_cAEiZCkvHiW-Arfsim017P2ERR7OTpmnw8N6sZxC1PRiHjiW2gVIT0uMhN9o_Y00F0XqR6I-7Awh0-3MhIfEBte5QHFrdcyCh3rvq6ZG52qsF76glfQMSAuylyUsA-yhToadY3I8raspPsaZ7XksNDgGAvdD9nWZJ69qHW0muH-2xHhHW4tFU4LyvO28wp9735By4s8nCGWsIrBCcnwrOkvoVUI7LjYVN2Q6Xh_jS81fWKLxAmOOjsEV9mwUcH9cRoxvuNo3Y7nzpAS5lnCwUfGB3MoAv7n1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان وارد مشهد شد
🔹
وزیر کشور پاکستان که به‌منظور دیدار با مقامات ایران به کشورمان سفر کرده است، دقایقی پیش در مشهد به زمین نشست؛ تشرف به حرم مطهر رضوی از برنامه‌های نقوی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443431" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80b7c7a4e.mp4?token=gS9OVyWzhUC2ASza9QRNbUNn6Jnb9jbixBPRQPdqwiL0EhGBW_mC9WCJgUZ9jVVx5yaEIuFEdx_KLRH9SUYhxBeujWjMsCTMG5KnC7_oBt9yq_FzorvTHLfRZHSXc2hNuY5nXmlyBNG1UOSlYXrFc4Nf8Z1ZUVIqFO3oj76P_sLjMPnEUkBIlCxXToPMVpPB6gMVVrSmKs5YQEFKkr97D8Ft2Sadp2BK9dB30xCCo8OVeVQDqyppnw-KRtcfTdLe60uaUZnH-O6YwTCCsmEgr_iDUZloxhDa6QB7sCq6BSEAid9yjS6PY0NcxjEBdolatRUjUB7pMerKr2b_Z6BNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80b7c7a4e.mp4?token=gS9OVyWzhUC2ASza9QRNbUNn6Jnb9jbixBPRQPdqwiL0EhGBW_mC9WCJgUZ9jVVx5yaEIuFEdx_KLRH9SUYhxBeujWjMsCTMG5KnC7_oBt9yq_FzorvTHLfRZHSXc2hNuY5nXmlyBNG1UOSlYXrFc4Nf8Z1ZUVIqFO3oj76P_sLjMPnEUkBIlCxXToPMVpPB6gMVVrSmKs5YQEFKkr97D8Ft2Sadp2BK9dB30xCCo8OVeVQDqyppnw-KRtcfTdLe60uaUZnH-O6YwTCCsmEgr_iDUZloxhDa6QB7sCq6BSEAid9yjS6PY0NcxjEBdolatRUjUB7pMerKr2b_Z6BNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی عکاس ایرانی موفق شد در رقابتی بین‌المللی و در میان صدها اثر از عکاسان سراسر جهان، مقام نخست بخش «عکاسی خبری» مسابقه Golden Shot Photography Awards 2026 را از آن خود کند؛ آن هم با عکسی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443430" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98ac79ff6.mp4?token=psVPG2iN_FCKVH6LEWZTz55BkMx3r-BxyoVxDhrWaNqsj9kGxbFegTvHHliDefW2mpW_fUWZaigm0phtlzxh4N09iv7dWyRVsr3S9_TQnwUs02P1rAcqOzetFNtC10Tl7ps8vKtdou-DZdI3S71vTTF4Er4jLnq-Dw7Hp9uBen4rH3jK0YeVO8iB9HIU3EOP9nzIevGRE7RNU5ZHrFOnHQgoP5fGSsiZtacTT0w7BFlYVxCfUK3CWf-nM-2jRdeaArogXEBhw9sZdIqfXYucKOH_cSccRiT5KWUGQ-IvP_OCJeuM8pfOS_JXD3d6czPIHuFojvg3f6a7KDwBNmxyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98ac79ff6.mp4?token=psVPG2iN_FCKVH6LEWZTz55BkMx3r-BxyoVxDhrWaNqsj9kGxbFegTvHHliDefW2mpW_fUWZaigm0phtlzxh4N09iv7dWyRVsr3S9_TQnwUs02P1rAcqOzetFNtC10Tl7ps8vKtdou-DZdI3S71vTTF4Er4jLnq-Dw7Hp9uBen4rH3jK0YeVO8iB9HIU3EOP9nzIevGRE7RNU5ZHrFOnHQgoP5fGSsiZtacTT0w7BFlYVxCfUK3CWf-nM-2jRdeaArogXEBhw9sZdIqfXYucKOH_cSccRiT5KWUGQ-IvP_OCJeuM8pfOS_JXD3d6czPIHuFojvg3f6a7KDwBNmxyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عزاداری مردم یزد در حسینیهٔ معلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443429" target="_blank">📅 16:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9757274c43.mp4?token=RRbpd5ZX08VILRiGr6nMWkkFatWCEu_aaquqdJHnqj9AxW5Z402skJQ6i6_YC108olKYIPQazQgUm2xkqiMja_SGgas6b4YqvAjnOv_FiXVqy2Odu2qxm778ZYZLg730ROC1la_qtRQDNcRJGK8X6KYjlo0yC8W5_Qxac-PSYV78tT9O6WJoqQJyCO020tDEU_coibTnAOIH0px3hljcy8WZEKNB90vXrksDQ2uhpSrkD0_-WHSm1JePpL6kEkusvJkzbGrBQEd-Sr6JZ2Hh7KXc5ISyusnlxPgb8RaYWX9XeECezupcZIhwHkrggu2JWxmbMmSzD3bOWD43ADbP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9757274c43.mp4?token=RRbpd5ZX08VILRiGr6nMWkkFatWCEu_aaquqdJHnqj9AxW5Z402skJQ6i6_YC108olKYIPQazQgUm2xkqiMja_SGgas6b4YqvAjnOv_FiXVqy2Odu2qxm778ZYZLg730ROC1la_qtRQDNcRJGK8X6KYjlo0yC8W5_Qxac-PSYV78tT9O6WJoqQJyCO020tDEU_coibTnAOIH0px3hljcy8WZEKNB90vXrksDQ2uhpSrkD0_-WHSm1JePpL6kEkusvJkzbGrBQEd-Sr6JZ2Hh7KXc5ISyusnlxPgb8RaYWX9XeECezupcZIhwHkrggu2JWxmbMmSzD3bOWD43ADbP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست نیروهای شرکت برق از مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/443428" target="_blank">📅 16:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189907ab09.mp4?token=jfFIBtGaG96OD6doZP2yX7os4EjeK6fB6o8Lhwn2nsE_r_gA6DeanXH__HoKZVuZKJOZtbKHIOdXinR5si6sfO_Lo0dm4PDpIIiUzKcgLCfm8gMSMgF-VgPfsTxOGbXEb11nnQzVwlxI9JdESHZoO0ssVDUMdI282xNc-he_ncc-9xQT_VHmjqQzzoyUJ91s14rw-RCuYrBFqyGZbsZJK5b_tuSaYiB-v3Fgr8FMb5r5gENCuIsqwXtuoE4_tLrgQZxZ4Xahqbdk2nmso8mFHYTrLB7WlE0mSkiOADLPdiP9Db_Cnq7gH1NyIXs1yKOzj9c_jTcuPTNzdy7STmuqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189907ab09.mp4?token=jfFIBtGaG96OD6doZP2yX7os4EjeK6fB6o8Lhwn2nsE_r_gA6DeanXH__HoKZVuZKJOZtbKHIOdXinR5si6sfO_Lo0dm4PDpIIiUzKcgLCfm8gMSMgF-VgPfsTxOGbXEb11nnQzVwlxI9JdESHZoO0ssVDUMdI282xNc-he_ncc-9xQT_VHmjqQzzoyUJ91s14rw-RCuYrBFqyGZbsZJK5b_tuSaYiB-v3Fgr8FMb5r5gENCuIsqwXtuoE4_tLrgQZxZ4Xahqbdk2nmso8mFHYTrLB7WlE0mSkiOADLPdiP9Db_Cnq7gH1NyIXs1yKOzj9c_jTcuPTNzdy7STmuqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوکویاما: توافق با ایران چیزی جز عقب‌نشینی کامل آمریکا نیست
🔹
دانشمند برجسته علوم سیاسی فرانسیس فوکویاما، توافق با ایران را «عقب‌نشینی کامل» آمریکا توصیف و تاکید کرده که اسرائیل و آمریکا با امضای تفاهم‌نامه با ایران، مشکلی را حل کردند که خودشان آن مشکل را با شروع جنگ ایجاد کرده بودند.
🔹
فوکویاما معتقد است که دونالد ترامپ تمام اهدافی که دولت ترامپ طی سه ماه برای توجیه این جنگ مطرح کرده بود، به مذاکرات آتی موکول کرده است و هیچ یک از اهداف دیگر آمریکا برای جنگ علیه ایران از جمله «تغییر رژیم» یا «تسلیم بی‌قیدوشرط» محقق نشده است.
🔹
این کارشناس تاکید کرده که بسیار بعید است که ایران طی دو ماه آینده در موضوعات مورد مذاکره انعطاف نشان دهد؛ زیرا «دقیقاً همین مسائل با هویت بنیادین و بقای نظام سیاسی آن گره خورده‌اند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/443427" target="_blank">📅 15:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f13d2ca8.mp4?token=ZNKwRIdI1XaADT37Em7lC_MVHGbzFtPXm2A6OwKzBGSVq3uwvXf3AgZSZQTnMmpZBte5OamJuThf71K-_jI0gBAxBOrvz_0SZ-cudVtJX6stWyP5WytT9OBeEzpxNAqDa5f4te5uVAU_Nt4wqZPX29oxtkxDIrEgx4RF_nshEsBPfqxfKiO7_NCnyHqNn8m0NOdqqE_YhOZU-t8_OfxByRncua9O-TJUH-8e7FhI16TPWMxH_ga6g1zegEwP8H3GzKA18Pu28eaR_Lv0NhzNsm1ipzS0ha9HuvUlJQY4v44Umz2Pp3QGzO4qZ8YmDMINrHEaAviioj6A0loYjOB-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f13d2ca8.mp4?token=ZNKwRIdI1XaADT37Em7lC_MVHGbzFtPXm2A6OwKzBGSVq3uwvXf3AgZSZQTnMmpZBte5OamJuThf71K-_jI0gBAxBOrvz_0SZ-cudVtJX6stWyP5WytT9OBeEzpxNAqDa5f4te5uVAU_Nt4wqZPX29oxtkxDIrEgx4RF_nshEsBPfqxfKiO7_NCnyHqNn8m0NOdqqE_YhOZU-t8_OfxByRncua9O-TJUH-8e7FhI16TPWMxH_ga6g1zegEwP8H3GzKA18Pu28eaR_Lv0NhzNsm1ipzS0ha9HuvUlJQY4v44Umz2Pp3QGzO4qZ8YmDMINrHEaAviioj6A0loYjOB-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: اسرائیل یک عملیات نظامی بزرگ را برای تصرف شهر نبطیه آغاز کرده است
🔹
اسرائیل با تفاهم اشغال‌گری را رها نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/443426" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlCguniBhQi_AI6Fal3mTyuBmvLs9xNeInXzO3STvhxItFoWMC2AHj2oYSe-JdYp36BMxH750ISXktxLYSb0NMqQ9CnAHZyW3FRwhzh7mwqudHKaSYgc-IiXFEI8oA17yfdcymBHDfSUPDm8cqxrLkx_VON3rpbiMVAjAjO-2wQAIG83LsP97-SVtb6M4EQyYY5byEzTOf1d530p3xpR9h8xIIf8o2rRN0lO0TFv2O8sMQADTh4E6wEu9MH30byhAQqfFE1i5oaH7XtwAQie23FMKVrRc50s9aXoOZlb9utGMxmbNjMZuvisxa0D3KYXDu_COtRzfW66L-_SJTMDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/443425" target="_blank">📅 15:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwIzZjLtloXDT4yXCDL13RFVPOf81IhMYeo60qXLI6h8mjtKZKCeCBg5p8uhe0JKaRrOgG64Ljzwl1_rx5dd-8I6qpPERqG0H6hxa-x__plqM6YYteg9dQQ5skQrZsI6DCA6jTiFA27Foa_MSx5S8HFEaIPnFj8KRiQdlPidxfzlJxLsWuq1fc-yK0wYYk7JfbsPPVPvmnM4SPm-Own3OpXAXWzrBuvwXC6lzYufwxeSiUCGZNHkPFhA8u4VPZcl_q4Q8cJsgmkorEYUOcgkZFs_14ESa5W74g6ogC7PU7Xt4ZF_VU1Edohn8DmGBJjqtE2qDsMZSeesjAlPjXR9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری شبکه سه در تجربه تماشای فوتبال در ایران
🔸
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۴۴٪، سهم بله حدود ۳۱٪ و تلگرام ۲۵٪ بوده است.
🔸
بیش از ۷۱٪ شرکت‌کنندگان مسابقات جام جهانی را از طریق شبکه سه صداوسیما پیگیری می‌کنند.
🔸
شبکه سه صداوسیما همچنان نقش غالب در پخش و جذب مخاطب برای رویدادهای بزرگ ورزشی دارد و جایگاه پررنگی را در تجربه جمعی تماشای جام جهانی حفظ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/443424" target="_blank">📅 15:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXqzOmpzABtQ-geN0p2Z0XQa9x6a1sU7ZaGCCmCdCVxfgxfTkvQN4Q2IavfrTcqGFNpMlDUgxbWem0ujOu0UKyqS_KjL0TfaXcRdW0D2C_iDsdvCscX53XXPe02WRhyshpEkIR1-1CSXFVRAtsE0OkDRkKpdR2QX7tWHQKoPu0M99sFc3q4JCJtrWiSjHtivM9W-2tfu-1yR8j_G79jgrbay4EPKQChjJbsLeCUFSFKZSBEK74L3jUqpqw6a_0xd6D5qHrvafWf5RT016p6K6ulDsshhIbXnZWP1USErRyk-8mI-ikv-Qea0DZY0bK4hjyprmv2B3JqzqAiA3Z8frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#اینفوگرافی
🙏
خدمات کلیدی بانک تجارت فعال شد
✅
تداوم خدمت‌رسانی بانک تجارت؛ بازگشت تدریجی خدمات کلیدی بانکی
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/443423" target="_blank">📅 15:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/443422" target="_blank">📅 15:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd3o8_Or0nGZ3y8MidiSvaiwMYt80pKoZ_plXx8PVqM7dQGPSS67d5P914TESfxC59ZduKYfhazMbvs0CxH_S6sU84Nq-buDZ194NT3i8YJiPQ1HdzXzDM22TV5svXklW7BHCOriahAWLqOBh9p8q723n-OcJzYYfQgOnOhkPizy6nlDNgDzuJQddQq4UxomBL9g-YJ-I2xVMRWnp97N3VosKMTAL-4BkYEvLgN0fgtmMd7Xx596P0QCmwNtJcbyd339rq-YAPDEJYtO4W1Z_sXbiKoBrI4kdpvQ3Bhxkg7ID7Eu7PQwWX4CTdQZOP0bqXnmLshOZTqzmHOlcVCOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترخیص فوری مواد اولیهٔ داروی دیابت و ۵۰ هزار قوطی شیرخشک
🔹
دادستان تهران: یک محمولهٔ ۲۶ تنی مواد اولیهٔ تولید داروی بیماران دیابتی به‌ارزش ۷۳۷ هزار یورو ترخیص فوری شد؛ دستور رفع موانع ترخیص ۵۰ هزار قوطی شیرخشک وارداتی نیز صادر شده است.
عکس: مهدی قربانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/443421" target="_blank">📅 15:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa76fba735.mp4?token=XUJ0T032Ad-LagCszufTh9jjp0rVxdzTAtXk83rPeeiph5xRjPPKWmg35g0hpVBQjPbfZXRDe90_NtbBk_ZM5uT8PYKZn6JeQQEWCQX4inSWvC61Y8S88-P8a7i9iHs0z-kvmhRu5JcieIMybPery_xo5DbSkCbn4EwXoa755vV8BMUPeFcOq2HJZiC5qn0WaUpz7QL6QYI2wtGhQjRkUZDW7MOF4dVmNI_ZSlJEVyiEcFugeMGECUzLcd-LQ4OWcTmz31XainYAEGqJUhOOL7MFtDYC8rhb8XBKipenMTprKbkx5BW5tfotIRamzO1f4wmhd9Tb-nXCs2D7xpwBm4A9wiBSDXWJ6P_DCHBNoKmYZTQu_vMVXGvIKLSmdWoMciQB82QNk2StNprOuLou5ypsOnBF1P5XZEuEFAHZdxpRnrl9hbfAVLn1xi6StrsfHM_X6N0kLW5SYIXkMyVC1GjBC8RfTcN06PYc7IyIS5i4UAezU6KQhP5vUG5fRhGdcAVJHfOl_jZ9er0JFjOqLKyMg6M0IriTie8x9DKBfVWDUWQw4HndNusBr-b9-RgvHqzv2-QT1tYult_fl-kY-J3Pd0KSE57sEBY4mTMg0TNXKVows_4k3FVgg0PqsWh8bY4iB6Lc7mHYXxOUAMINLxG_THrUxXWvg4o0g-9PofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa76fba735.mp4?token=XUJ0T032Ad-LagCszufTh9jjp0rVxdzTAtXk83rPeeiph5xRjPPKWmg35g0hpVBQjPbfZXRDe90_NtbBk_ZM5uT8PYKZn6JeQQEWCQX4inSWvC61Y8S88-P8a7i9iHs0z-kvmhRu5JcieIMybPery_xo5DbSkCbn4EwXoa755vV8BMUPeFcOq2HJZiC5qn0WaUpz7QL6QYI2wtGhQjRkUZDW7MOF4dVmNI_ZSlJEVyiEcFugeMGECUzLcd-LQ4OWcTmz31XainYAEGqJUhOOL7MFtDYC8rhb8XBKipenMTprKbkx5BW5tfotIRamzO1f4wmhd9Tb-nXCs2D7xpwBm4A9wiBSDXWJ6P_DCHBNoKmYZTQu_vMVXGvIKLSmdWoMciQB82QNk2StNprOuLou5ypsOnBF1P5XZEuEFAHZdxpRnrl9hbfAVLn1xi6StrsfHM_X6N0kLW5SYIXkMyVC1GjBC8RfTcN06PYc7IyIS5i4UAezU6KQhP5vUG5fRhGdcAVJHfOl_jZ9er0JFjOqLKyMg6M0IriTie8x9DKBfVWDUWQw4HndNusBr-b9-RgvHqzv2-QT1tYult_fl-kY-J3Pd0KSE57sEBY4mTMg0TNXKVows_4k3FVgg0PqsWh8bY4iB6Lc7mHYXxOUAMINLxG_THrUxXWvg4o0g-9PofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای خیابان‌های کربلا در هفتۀ گذشته
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/443420" target="_blank">📅 15:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📷
آماده‌سازی محل تدفین شهدای دانش‌آموز جنایت ترامپ در میناب  @Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/443419" target="_blank">📅 15:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443413">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KT59DKqweMlhOrZ-8CGkxqyPU7L1BjX9Kkr7NST4C3q7EY_N9h8ag-EdlhRWfgaEUyXZR0jfh6aBkez-gdFFHu1w4_hpWC0850XlrwnTY2dyZMk1URL-koP_w7v_L4h6fhH7IwY2WoPK4mVx_goKElF7yZoJhG1rtu3AVXEx937POSJAAjsEOj-7HMb7VgwTRTSq7kuOrG6WyqfCgA0soMf8FZ6I39GCWzIgrtwiWMawZfEvhZBZGK7qwiCVCEovCMQhlStOguUDgcC9pxGfZnDITWivHC2tWW_NsCXcgNTHc3PWHuhJIVJTHg0FN1puhVEN4D1dGHd621Xjly7PpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pY0ftORaq2nrA_pWYiVxkGmhKIeuWjmGa-zFfwh9sRhNyRaUz_pFqtKRIG5RYtqmnikd64Qjps0uj966J5jtUe2ob9l2OwGmeP-epBjYwv1uxNnVLctoPyq-76pD9ia5fO7V_1GdnvNjol7UNyvqjs-kr4mDEqqptq_-vnr1HxqSaVLZef8q3a3XwdVhwFoF1mAeYGdlxdhwQMGcKWs2ITAv1OJYAKU2BBS4D-_1nL11VgiIRic9SsoTPvs7ju6XG2CDgU4ZFN88wDqI7ci3FNGRQ_nr1bsskURA6o6yQDVFvRckLEm5kviWu8kbC8AXs4Ko1KwMeMGWDGyTBNnaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1ksBy5dRbYBiiZESUBWhb3NoNJw1a93yZ72Zx8Nse-ob8A5t2MMGrYGN8ofxlov1Vf5KMCn37qNEd9VzEDHueUAwu8MTlwSdOroGq-qVa3_sSbb7fdnv-IESjE6xD28dt0-6cUiASUAWejPqVV1MKr6z7qV2mL4r-9T9TV0UpOOxTE6DROL5aL9t9I-U0bNE4pLiHwBxr0pG6c-pOdw8AkC3s2NmOp1Dx12Kf1xiJ7VmbnjcQW6kSxcPyA4wgydSa0Og3D8OF69qUMSu2jAkAoI_0dqo3NRLx6fwh8zHd-SFhes_M1pFxyrhGLxnDjrRq4lFZEtHH-Q9fFtoaNhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoXMgXqrcam_3w4RNl6ZoYxMnMBaRl_o8OmIgojxVYl5TVHiyMBfnJ7WW6fcysobXRllP-H4wVeCYFb4ZxbTXBn5B5m1f2RpUd7JfrQ1xGxy0EuenhtNvHTm4yMO9OIwtD23E7ZNDlykSgmOIJQfRuvyrnIujEP3iJoY8gwIzNBL9_BmiaVvqcM-PWB6CKBtOf0MzxzJvr8mHOina7atwYuNlmwY1RMcTQWP71GztemoLFvXMDSWgFIJFfFpn3mqKNqTwZwkT2WcN_EzdeFk2a0UoM724JTjEw4MWZVVRI9Zfp6RIoEIQyAE-9kq8yQpB94ckEtrrgQowwGUUgs4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eq8e9y1XJAVunEpq29NQghD2V2QOL50zylEBR6DFC8QcNLEkRX_Rsd7fkg3CVar3LCBa0cyUoOKPl0qmR6KtFnUj_HWxkRjBEg6dbqRmmxIYkRuDxs0exDHVCibytmmLT4tAm5acfYSWrKxEbf57r2DcIAp-ri03rRHqgVDNScfz3NXB-C_UJUl3Fiu_e79HY57S-Kt8VrivizAQwIn9eyhm9TsUfHFztqQCC2JeUyVmEfqCb6KJeo1r1lxy1Ck7VZNovsp591g0XhrAaW9SDXqFQc6wwlKVjUR5NDyPAwO2pVEbEPhybHFp_RAiYPLWUxVvODANFDQVwKAJ2HTM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgPJEVkR4_3-EgSSS6OwqM9u27byG6I096oCwtssN5ReVa97MLMZnWY-HuHzBxei_iqqBLbRApKntrWaRTwPscESDtFSaojqBBoDUwIUJKDrEki24k8VIeQOYbCHpqGB6x5EjsXNLi3TtN6ippyOs-d28bN7e0yhO9JHccE5j7zAp5As5rUB6nfEfTgboZfFQD2MLGbkMtwUltZW-Gc9DS6WBMtfCJSyc3fiRtbEJv72QRoQHz2XIaS3mNqi-SHsTrMUQKVrV-3H00kbF2TmqVe0mrbf-Kh5cyLhdhUn0BVgn1qYhdSgYCkUHrXSDtzAhJeT8-j-Kc9fim7uXfBF9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنب‌وجوش فلامینگوهای مهاجر در دریاچهٔ مهارلو
عکس: عرفان سامان‌فر
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/443413" target="_blank">📅 15:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzKbplZMVKjvm6E39-79T9Wfs2C226SDACLYOuocJb3h5wPXGbPtXPPcW_2iv2JwMU89n8X61cgEbEdqaNujL9v7eMi4A1EhEHzC3XhEOGoT964mWTE8Uv2CQEaHmX_A57HMpBXYpoiD4-Mgk6l5qIY1j8QOZWquyB4wU--lVd7aWNjrx6o23uqrx9Zs_RGzIEk0AM6qruKKD0wT2k3GOGigx7RZfgfzGbsqxLZVz_aNmvjLWsulEh0cX0_Ly0VC9bkpUdOe9ahdcMbDPWUgJrgmSsl0TCgxCa0NT13xTDRQq2dmcMoekUtocHAVWh2d5ZYNexZPQsZviMVN3xDgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه اتاق عملیات مقاومت اسلامی درباره تحولات اخیر و نقض آتش‌بس
🔹
اتاق عملیات مقاومت اسلامی حزب‌الله در اطلاعیه‌ای گفت: دشمن اسرائیلی بار دیگر با تکیه بر ادعاهای دروغین تلاش می‌کند نقض آتش‌بس را که خود هرگز به آن پایبند نبوده توجیه کند؛ در حالیکه از شب گذشته تاکنون حملات علیه لبنان ادامه دارد.
🔹
مقاومت اسلامی تأکید کرد که از شامگاه جمعه به آتش‌بس پایبند بوده، حتی پس از آنکه دشمن از همان لحظات نخست آن را نقض کرد، اما با توجه به سابقه همیشگی دشمن در پیمان‌شکنی و حیله و فریب، دست خود را بر ماشه نگه داشته است.
🔹
به گفته حزب‌الله، ارتش اسرائیل در شب گذشته اقدام به تلاش برای نفوذ به سمت ارتفاع «علی الطاهر» کرد؛ منطقه‌ای که با وجود تلاش‌های مکرر همجنان از اشغال آن ناتوان مانده است.
🔹
طبق این اطلاعیه، امروز هنگامی که نظامیان تیپ کماندویی ارتش اسرائیل به کمین رزمندگان مقاومت رسیدند،  با انواع سلاح‌های سبک و سنگین مورد هدف قرار گرفتند؛ به طوریکه مقاومت توانست تلفات گسترده‌ای را روی دست دشمن بگذارد.
🔹
حزب‌الله تأکید کرد: مقاومت اسلامی اعلام می‌کند که همزمان با پایبندی به آتش‌بس، در برابر هرگونه تلاش دشمن برای توسعه اشغالگری در خاک لبنان، هیچ‌گونه تسامحی نخواهد داشت و رزمندگان مقاومت در کمین‌های خود در آمادگی کامل به سر می‌برند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/443412" target="_blank">📅 14:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG4EymdEQrumHbKRLd18-J7w5bUSPyAWuFIM6krI5wi0R8eEi-PVmlnJz6ZG5jHOIa4GVbU2BhEH_HuLoNJbt4CET6hLJswutlW7SDASt4xj4wNHpjmq-TG3HoVBZ5tshiRJL0ADIEHDXmD17MEORbeeabwqdmP7HMM3SvMlwgGMEqzyJB5dYWhuOIjAtd0tyBliLSYSBiEFkzSobevi6QgbFCQg-FgwxeiPil_VIqDUw4r-jR7Z8Ll9pK9bo-l-NuFfsecUdHWpVsoEJsHHBIHMWX-5L4Jg_jdUWzjGF8DtonlW_6jw1YXOVPVV7NdgLaWuieYYUWwfHZOx52cTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارز زیارتی اربعین برای هر زائر ۲۰۰ هزار دینار اعلام شد
🔹
براساس دستورالعمل ابلاغی بانک مرکزی در رابطه با تأمین و فروش ارز زیارتی اربعین حسینی‌(ع) در سال ۱۴۰۵، برای هر متقاضی بالای ۵ سال ۲۰۰ هزار دینار عراق در نظر گرفته شده است.
🔹
فروش ارز اربعین توسط تمام بانک‌ها و موسسات اعتباری و صرافی‌های دارای مجوز معتبر انجام عملیات ارزی از تاریخ ۲۰ تیر تا ۱۲ مرداد انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/443411" target="_blank">📅 14:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoqApBTUosN18_hWk2jGLrHrb_7NoSh4Qd9lBnsMk9fJWDOtDTtzPI2rHQpcsLjJPUfTXaDyGqH8XFllP4wW93ks3PfUua-84UwwP37tyMjE6unW8b1EnSBoguz6Kzz_9uQl4QvFfXWqG6CYp5XR_cQeqAXsbwEYZVL1wePBHEmFUZy20jGF3phDk0Zex_UHpyzJbV9OXeWIj1oAsUaC__8xQkA4wJW_Vt2Vj7hC-qj8Io2ojf8mhgtRwgCNHuOxsATUxI2yklhA6p_2qNMHymGv5_CmbbS1MzxvyeAApG9U8ghGT6B6zKG4q9GrjSNrv-0HMFJDZccsXS_1MXvRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvvAYsjN9Ps_rAXjnN4n2gHimc6BlY1AWthb6KPTUjZCyUYtvmakCuFwHkj0k6GUlX2WNJnRT2LRmu_YoIVzB0EvGXr1wDNun-EJhRUlEayV65Z_ub96R9iXjnf8LlEFjDEowXoW7mB8Q3wphO9WQha6CBIFr6VQlI8urW--mGna7f-GglDGe4DQ40M3LjjpyZ4cXW0rTEgxuuaeQiy8gMDp34lGv5F-JpjSMAl8lTTjv_LDxWir_OqIy93iEj0Ah5foxtp3X2HBnPSygleGZ0t28_K3e37eWYiwS8LV71m9C9af15ToWpilpn1hZ7ELJRz0zTJUDaVD4mbj-iAXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsOLH7k4rP8qDaSJBZ7RWyDROUZDF5JhFWIeeuwxyvYLIebw5JiSw2Nr534gYmNj8q_dSAhSYjv0SOWdmw5VRfYasVy2HDLrl71Rm_engg5wAIA_4aAwasC6Is4EnzfNlyW7dPMITTxsHZe0EnQS6DItP3gzZNcCEqwArnqlxOptGQ_66WZfaqkiZW5l1YUiibCZb0yoWFDS5k0kpbja7Sm80AlNuaASLTbzZEfwUGiK5kaUeZqiTGi1Od8cMmEs9GA1urIts-bHY7fBogqaTdIFIvUpw0DE9eEszjzqqYhAdjg1nWO9kuXe0im6Feqx-N7h3Tzy-DasbZbmyGKt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIzw84ghd9VKIrCeUVq2mVlsUDNDSGZazsWU1WHyivu43xfOaKEpMrZzG8HzDr5RvzFRoWh8OTbftY6niFm1WgurhP3Tht7FrXs-0ZljyZRqsjY2vpU03iqjAC6oWHxJR1pHcKQunKZ2Lhvz4oTLUHeK6LGWpa8p6oesw1cWDRCFJz18REWgkPzbtUqIsF0Ozq65VB7E7cCqfXIx6pVP4C87XTRkaYvwMbpiKejYRbv0ouJFucbveKNzTE5WG3AUx1gxO-ILJkN525w09483FC4YCUIlzb1TgqOTRHojtT-DUN7toDqqdpzDDsasRkEi3wXDJW30pDttTEdarxGlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npm1A-NNHZO0jzzXc_jTHcDKLrR8J3w8yKC_TtU0P0fDcmZqguaTl5I6fXQiNCDWci9NQsAWM5CBrNrH889x9NQT7Ry7uG2he_R3jz3R7D-PyCWViUnRy7rg5_sCP78ggSFSRRdzMyX1YZ2JenJlVsuAHWUUClttC43WX6iUji9AN7b-1Mzcu1-P81QqhtWijydCnD2HdERPUYYp0VSMLkTa8jFP_H5DASfmtSDNLb2N3Or7sscDB5-Qnq_lWzNfYS0d23aRKr-rTYSkqiE9S4AIri4FKizTfJl14qU9I3b3d_F0auvSE2ODGPmlgMDnlJAy91p7dTEdURNLR6RU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjHDpsi_rTZ4x9k0e2LFA2kU6hUIFRKKPbRASU4nLwytVuLEwZt9j5DIZCLnVOArnjCfU-R0-agoatWk851UwMh8c_pHnc9Ta3RwMLmVCF4sGqEB3MpUOGoqVr8ARB-RecsCdKtAnx02i0tUOXXLmLlFZvWMgxZDhhQuWepI2hhas5sJk8q3GRCYOdITvTm691Ah2vv3XcHajYkb4AL49KZd7PKCUepA63RxeGEhJ7d-awAaCe7ie3PUoa1LrXZizqUq1MEXuZnB9cyRCZPe51gW8EeOpO4ALH519CIg1zqulQcQ1EvvkNW-h_sIk2xm7nMBLIIgvKkdiO7mNe49cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور عوامل برنامهٔ تلویزیونی کاپیتان در خبرگزاری فارس
عکس:
‌محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443405" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86958ea936.mp4?token=mbrLzJl8A4t2xwQ5emmQk_3FkVoi7yoE_J5k39Kn0GYtBDeCWjqgq9vHvgvDvR28DuRY26w-cQyq9hRUuloQysZ2_vMBDuPyQSiFhkOczJ-VfxlyTsVZXXwezOKb-b4lvj3b3NIGsKyk-fN1y6u512TxF6uTqNjhXX5aMRn2rCnjtt3yL98adIsO0DLv3NwI2WDAqOXSljT9ZxBn-xxG3trqkUje3DzEIS38ABrhThw76WvdikvY6wFEBzh_38Byb2hpN0-ey_ykf67BV9iWT2ZzhBpKtKnsNG_sSwm-91s1Wh--d40tnVqaxIsxFtyXJ3EqfCl1EWEESPlLm1ot9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86958ea936.mp4?token=mbrLzJl8A4t2xwQ5emmQk_3FkVoi7yoE_J5k39Kn0GYtBDeCWjqgq9vHvgvDvR28DuRY26w-cQyq9hRUuloQysZ2_vMBDuPyQSiFhkOczJ-VfxlyTsVZXXwezOKb-b4lvj3b3NIGsKyk-fN1y6u512TxF6uTqNjhXX5aMRn2rCnjtt3yL98adIsO0DLv3NwI2WDAqOXSljT9ZxBn-xxG3trqkUje3DzEIS38ABrhThw76WvdikvY6wFEBzh_38Byb2hpN0-ey_ykf67BV9iWT2ZzhBpKtKnsNG_sSwm-91s1Wh--d40tnVqaxIsxFtyXJ3EqfCl1EWEESPlLm1ot9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی با صورت‌حساب کاغذی
🔹
وزیر اقتصاد: با توجه به آمادگی زیرساخت‌ها، همۀ فعالان اقتصادی باید از اول تیر صورت‌حساب الکترونیکی صادر کنند و دیگر صورتح‌ساب کاغذی اعتباری ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/443404" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee46777c.mp4?token=eDjPvAQfRM2Iv-2Kf7qaFtBA4Cf28h8N0zQLvNnABm4MfX-LHkMNl4gs9oKpyzmjj6InEm8ZdpcRlQf4xJE8o-__BHmOZE4kM8jDNvj-x_lFeRft2JSVd6Oaor7iw8fNiX6LzpD7OpnoZ6jNAsxFcOxKaPGDBBhAkPHl76HbgVNQ4OoXTgfrxn8JegrjH9NRTq482jhzHnH_kgK_CLIHDMib16ud203Q75pdch1CGdtgjuVMScMR8eqf3VPY6L24RcKW0cl6tcfXZb7m1TIZswyjjt9lEvOM7sl1QwYhmslr_0ovq4Qrcju75jv-iff0iB_NzRPElwIEIOWl_1Ah8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee46777c.mp4?token=eDjPvAQfRM2Iv-2Kf7qaFtBA4Cf28h8N0zQLvNnABm4MfX-LHkMNl4gs9oKpyzmjj6InEm8ZdpcRlQf4xJE8o-__BHmOZE4kM8jDNvj-x_lFeRft2JSVd6Oaor7iw8fNiX6LzpD7OpnoZ6jNAsxFcOxKaPGDBBhAkPHl76HbgVNQ4OoXTgfrxn8JegrjH9NRTq482jhzHnH_kgK_CLIHDMib16ud203Q75pdch1CGdtgjuVMScMR8eqf3VPY6L24RcKW0cl6tcfXZb7m1TIZswyjjt9lEvOM7sl1QwYhmslr_0ovq4Qrcju75jv-iff0iB_NzRPElwIEIOWl_1Ah8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنایت در شهرک قناریت در جنوب لبنان
🔹
منابع لبنانی از حملات شدید و پیوسته به شهرک قناریت در جنوب این کشور خبر دادند که تا این لحظه به شهادت دست‌کم ۷ نفر و مجروح‌شدن ۱۷ تن دیگر منجر شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443403" target="_blank">📅 14:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d49524548.mp4?token=Wq9MkHAXePYGN2YcA98Z2FwFehgKpWmsHgbhr5XiF0POXOXsJU2nAOy99L_vl1BccNkgqlJtcl5xnBCm7dyboULgcAosn0UzejCUlYnBgllYehSYBR72rXjoub_Uy-l9RWhTap0alx302asjwIzDpKvDdI7ZFzc7VPsVe6awBFoRNY0S8YPNEW6GE4VXLkCcJNzqSjmuuaZB0gADDeXCzbyAz_s5d-cbpe9oaVTneTQEEEdYo3vVAJeF-qbX-Hvag_INhI9LHiuEoT-NvS651pfNnB5l8K33d0eqGhtshNMP427zvwHI4oNAVCEYm5wuQR_8lRA3HYeO5-N7c1JsdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d49524548.mp4?token=Wq9MkHAXePYGN2YcA98Z2FwFehgKpWmsHgbhr5XiF0POXOXsJU2nAOy99L_vl1BccNkgqlJtcl5xnBCm7dyboULgcAosn0UzejCUlYnBgllYehSYBR72rXjoub_Uy-l9RWhTap0alx302asjwIzDpKvDdI7ZFzc7VPsVe6awBFoRNY0S8YPNEW6GE4VXLkCcJNzqSjmuuaZB0gADDeXCzbyAz_s5d-cbpe9oaVTneTQEEEdYo3vVAJeF-qbX-Hvag_INhI9LHiuEoT-NvS651pfNnB5l8K33d0eqGhtshNMP427zvwHI4oNAVCEYm5wuQR_8lRA3HYeO5-N7c1JsdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروی دریایی سپاه: اگر شناورها مسیر دریایی جنوب جزیرۀ لارک را رعایت نکنند، مسئولیت هر اتفاقی با خودشان است
🔹
از برخورد احتمالی با مین تا تصادف‌های دریایی و حتی هدف قرار گرفتن.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443402" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d70cf233.mp4?token=d3qIMktKJA7mZOjpzGplh48nGxoIzA-WVDx82FQzccmubgtNp_Ti5MlP0TQRt2742Tin-wHcVw__iWr4RomrO11HLmrjULltdrAllGvBaF-Irfh7cz4NfDp_i7Sbae3ZV1LysucqU4zOSTuIcQqaSy5qtqS0fsD6V0ugCJ9x_TOzdl-8_hT3KdvExOip8zb7WPdLDU5zOKHrZ7Bmkoq8ThprobnL8B6HwSXnm5wkPqhj1AuJjvITGlulDg8LuLoVPrZ6bNj2f3ViF_7QlINvs_FRypFZHd14RZREdcLt77r3nY4VFGmepb0-N9gepkktOBwY7LAgI7HXIZW2dcqBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d70cf233.mp4?token=d3qIMktKJA7mZOjpzGplh48nGxoIzA-WVDx82FQzccmubgtNp_Ti5MlP0TQRt2742Tin-wHcVw__iWr4RomrO11HLmrjULltdrAllGvBaF-Irfh7cz4NfDp_i7Sbae3ZV1LysucqU4zOSTuIcQqaSy5qtqS0fsD6V0ugCJ9x_TOzdl-8_hT3KdvExOip8zb7WPdLDU5zOKHrZ7Bmkoq8ThprobnL8B6HwSXnm5wkPqhj1AuJjvITGlulDg8LuLoVPrZ6bNj2f3ViF_7QlINvs_FRypFZHd14RZREdcLt77r3nY4VFGmepb0-N9gepkktOBwY7LAgI7HXIZW2dcqBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب‌هایی از بمباران‌های وحشیانه در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443399" target="_blank">📅 14:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUxS7Wr1Am4FbtfuGlqHwLkU0Vxq8cR1hZZtqBi3h4S6lKgibk6-JmMRGfqvMO8Wk6f7twjZChEo4Tz6CEaRj-dn8vjkNDpjeivHs-csN0dzYAkanh2Y8c05H4xOOGU_oqO7cydyN92PWvz6mtwq8JWdX1ez47kxNZymXWKGBaTaovagtyonaPIDHQIsAov5B4LGU9L9BSJsSG7qs7D9ezIptvcHXbW88x2WHDcRTiUFE90-e-whZ70wesber4Rgf9kkw9MGU8VCRskKNeb9lvrW_vLNTRLdo64zBmuKDOB9jg_XWQpOJgRczkajDpJAzJxbiHjLauNky_vAocWh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWHKwVs3W6blTtIOrphvTyWzlyvk9iqctjtx6MqwHRFVTCz5QYs9QTuQ-JjdrxFIQsOTsy_5b98NzgFJiIsquvIK9wqj0jhINdvHBYpMRH0D8VjirR-QUhszDJNrwFdFNgPYt3mEkkHB3smtffABb5XmK2mR4iwXsFP9NbUpoLq2z-6Z5lPyipjvuVi7MN6Ya_ifIy2nLBDMbRr8oLcU-v8S6nkuT9p6-U7mA2XxM46_aC99MtIxB7cRkreurRNoWRLpdxHcLburLleogAS-Ek7uttJ_3RMANyK1ArPEEbqODaciI9jKsEsi7q9vXkzPICcAllgbry1XOB6y1iK-1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بلوار علوم و فنون به نام سردار شهید امیرعلی حاجی‌زاده</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/443396" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKs1Krbp50502Bzaoh5dqJzfROHda0G0ht2r11sqBbgSzqcA-iqzC_vixscroZemSvzSVSHnFffJxj6fQVvD_HWDkYae4XaifR_p4eA8oK-EWurSkUcGIfsOgpy1bWYNvhPIzYVQbsP5f0pvQR2hdaVEruYXCQVGAL4vVrkpGvMREv6YMk5qKgM_gCG1bKlzi7sjvzCegm1GOGgR52v3Ua6UvgFnmZ5fSA3zXYaQta3RFqIklJc-UYcuBp68S1THwwCTJ60w-qd9BJfKqPYX0VruAWKyFt4z_pmsGbC21bw1-Edf_0PCyfQyj39k7oNDOeI8XMF3dEjTK16M3i6Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سگ هار آمریکا
🔹
کاریکاتور کمال شرف، کاریکاتوریست یمنی، در واکنش به حملات رژیم صهیونیستی به لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443395" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4h3F521GeScM19G-bguUVQbLRvUYYGZRsiwA5qkLLCW9ojhYzjhQbpZHNgnsTQ6RjN6oBbNpNv9t7TNWrIFIpAcjFzMq8TYxma7gK3YF5SdDqMYYQbyc0Ny48u4IdMoBg9w9JMw22jB8QpwfrWQpFy0MrEqIel-IAzKZlNlhsRMfZpjLugRNXcwM1tEVNCA_2h64Q3_TJOZEhb9k5_1nqlfM_FBuMTsPa-2ICHqsWQXJdOtS3b9KhyB-iJo9gouLcl-sdoRwczVQmoo8jEAzCoZ7znZ-ZJp-Le8VC7A87RomUaQJdhEMpoRMQEauZ4prMZbcJJgZKOn1BeQEgQeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
همزمان با پرداخت یارانه اقشار کم‌درآمد انجام شد
✅
واریز پیش از موعد حقوق بازنشستگان کشوری توسط بانک صادرات ایران
🔹
بانک صادرات ایران همزمان با رفع حداکثری محدودیت‌ها در استفاده از برخی سامانه‌های بانکی، رفع نگرانی‌های مالی اقشار مختلف جامعه را در اولویت قرار داد و در گام نخست، نسبت به واریز بدون تاخیر حقوق بازنشستگان و پرداخت یارانه خانوارهای کم‌درآمد اقدام کرد.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، طی روزهای اخیر و همزمان با بروز برخی اختلال‌ها در شبکه بانکی، اقدامات تخصصی جهت بازگشت فوری خدمات به وضعیت عادی انجام شد و عمده سامانه‌ها در کوتاه‌ترین زمان ممکن در دسترس عموم قرار گرفت.
🔹
از جمله مهم‌ترین اولویت‌های بانک صادرات ایران همزمان با برطرف‌کردن محدودیت‌ها، رفع نگرانی‌‌های مالی اقشار بازنشسته و همچنین دهک‌های کم‌درآمد جامعه بود به نحوی که با وجود اختلال فنی، حقوق بازنشستگان کشوری بدون تاخیر و‌ پیش از موعد پرداخت و یارانه خانوار‌های واجد شرایط نیز واریز شد.
🔹
قربان اسکندری، سرپرست بانک صادرات ایران پیش از این در مراسم امضای تفاهم‌نامه با صندوق بازنشستگی کشوری، بازنشستگان محترم را ارزشمندترین نعمت برای جامعه توصیف و بر رفع دغدغه‌های معیشتی آنها با هدف ارتقای رفاه اجتماعی تاکید کرده بود.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/443394" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPJoasMIt_UyXwlxtMiJ0y428ESxYPIah9l7MYxZamny5DNU5ZGW88PpsC_EH4LrQ_k5mGNlrrZXwAzqgoADzuYZtM4kLrsRpMktc7dVF3oGvo29z8EN6_4dQiNBwAGjCTEkl22Su5kAYeNZLX8qu-S2H8XFPFjkzCA1KOCGIdmIt_jUg686SVx3izBj15RId1TMp5uhWquPFoAk9UP0dtTIJYK9uAn8YtWJIcOQwjRSF_84DmPrySOa0sAUeHUoSEEbFJZWGQU0MT_PkcNdmEeAzvg32DyHsasG34JW_47mt1ja9fgwxWGLqEKj_a3_fe53UbV_L0pWbnQ-QZ0OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/443393" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/443392" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAVnYVfAp9tdOS_WNzrCKhfgW8JqxpwsPLKbzpcm2_y0lDhG7bG2np_07EkBTipSukbck5RP8LAO-s2wuH2QTUGajIqRa-rNGzwgnPUZDFy9PSvYJYVtIoKbMOPj5Rn4MT-BiW1QMjWIDkmF1iMZ3fGQ0G0t1cLoatPT4HZRSx9gMM07QOl87I6odlxHdVh9EBVDCEeweQDzIFwyMPyrsodtsQVU1Z7u_Af5amNNS8jKtzsRKcVuZpXXJYPKBXwQLaVZVWLPGj8CoTKD9oRk6q7ySDT4pEa9aRuCd8WGoH2gg19veokxnuu2YT2jTFhmnpRTCxIFUeeiBPFj0wlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم آب دریاچهٔ ارومیه ۱۸ برابر شد
🔹
مدیرکل حفاظت محیط‌زیست آذربایجان‌غربی: در آبان سال گذشته، ۲۴۰ میلیون مترمکعب حجم دریاچه و وسعت آن ۴۵۶ کیلومتر مربع بود که مقایسهٔ این آمار با شرایط فعلی، بیانگر افزایش ۱۸ برابری حجم آب و بهبود محسوس وضعیت دریاچه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/443391" target="_blank">📅 13:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت ۳ لیدر میدانی و ۱۴ مزدور شبکهٔ خرابکاری دشمن در ایلام
🔹
وزارت اطلاعات: ۳ لیدر به نام‌های «مراد-ع»، «مهدی-ک» و «رضا-ف» از اراذل و اوباش سابقه‌دار شهرهای ایلام، ملکشاهی و سرابله که در کودتای دی‌ماه ۱۴۰۴ با تخریب و آتش‌زدن اموال و اماکن عمومی و تیراندازی، تصویربرداری و نمادسازی امنیت را از مردم گرفته بودند توسط سربازان گمنام امام زمان(عج) بازداشت شدند.
🔹
از لیدرهای بازداشت‌شده ۳ قالب TNT، یک کلاشنیکف و شمار زیادی سلاح سرد کشف و ضبط شد‌.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443390" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ توله یوز هلیا پس از مدتی ناپدیدبودن امروز رخ‌نمایی کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443389" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWL15VcPl-8p-MsQFy5heSwbkni_4yH2j1u1q3kCTJtNd3ilTkBZuYRFy7b9hyhNpMRPfqXnYP62WKC8NzK6iJPmr-ancuRkxDWusCNJnkBHUA3Dqu64C_2wPFzUy9tH4ITYR6HG3UwUyra-Ng7jXZqr8TZsRyTmIxF--zULh-vJgaQE8j3pa5xMCTVHsde3_Yo0PqBShKAx8niAWQ6fY2V5gafrIa9FX-02PkohEqFnJszQMLQyHh4ia0Pu9FZID-L5cpVnrTS_U95yrL-OVr4j1_QaVnsB1A4eiVEwOvvcD1uuhJ9BpNEcHwaIPlHa8L_xCxFtDGkjqkNJs4fPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل جدید دریاچۀ ارومیه آغاز شد
🔹
دریاچۀ ارومیه که امسال با افزایش ورودی آب پس از ماه‌ها خشکی، بستر از دست‌رفته خود را پس گرفته بود، اکنون فصل تبخیر آن آغاز شده است.
🔹
عیسی‌پور، مدیر دفتر برنامه‌ریزی و تلفیق ستاد ملی احیای دریاچۀ ارومیه، به فارس گفت که آخرین…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443388" target="_blank">📅 12:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم سوم این مسابقات نیز از طریق دیدار پلی‌آف برای کسب سهمیه صعود تلاش خواهد کرد.
🔹
طبق این مصوبه قعرنشین فعلی لیگ برتر یعنی مس رفسنجان باید در بازی پلی‌آف بقا به مصاف تیم سوم لیگ یک برود.
🔹
نقل‌وانتقالات تابستانی لیگ از ۳۱ خرداد آغاز می شود و تا ۴ شهریور ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443387" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRs4UqFYOw1tsdeIAhF8aHXFqYl352jNPOmJ0Rc0y_nxzzp-tSN7oXN3_YUcYIXarSlyvVrhiliGAirsnRsy-z9076keRTmTNc1HbNjzwwvV1dvcOteuPeH96HDBsAlZoxyKFX0toAL7mIHIQxz-AZYZ3bUWNUKI68W62PJ08lTUp0Fmxc1NvAuU-VIkH21ZaPQv3pYht_7LKlgnv9HeO1Pm8fvfgdrE_HQB_d9ANHTVVYyOxyVFOhsiD_4v1H-dTHbVZG0487R1BgnpFpszwYixYbg_igG0RYq2NGyA1siDUtmu_Vkk56qgIjH0kyMW8F2USih-ZW1DcOp8En1Auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۹ هزار واحدی به ۵ میلیون و ۱۶۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/443386" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyAIdypnnRXXdCRnLv-VdBN69s_tm-yKhyWF5POYBXbDZiw4Qlw6JA1LLFhZRhAZrDeBCdhGySGE3oWmaUIEZzGHD0MmN3Y-GynBelXvkZIYGVTWHTRhDVGE_AOCvhtf8XP-YVyMgLP31EuJfEF5tBMA7D0_wvnI1oPuw4w5r2CQZyYNGfCsQiS6qYxcfemYSd8NDL2J5w90PQ9Qb7Xb4X7oGvG003l_ZV-c3hit79dOmPzstabpR3QkzP6k6IxURzJGmGZPj_SP_vdgWbw_hcgTkfJMdYl4Yb6xBEIwdEFmzPbccALqEROokMB2-hBM3I5tJM3DtGlirnFBo0BnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای گفت‌وگو در مورد مذاکرات ایران و آمریکا برای چندمین بار در هفته‌های گذشته راهی تهران شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443385" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4PsPE8HBUheRqdkSKMOl0QnbT_zq-MygUsil5Zvdh0vA96rdxu8vA1ynm6hfA8Tmkun0yKmIpI7dTwkgERpjwT1uLaWL2f3mk5jMYEjKnE4M83bqKk-U4H3-wGUzfb_FYLoryfK_-8O1iDG-vkopgR4fWmwcVYSC3PuH5bYxSeN82T4_1jXeh3plLatQwtzHIFZvtRwMJcuP-VS8ytrUzkbjaiJDn8vF8jB09CRU4PsFPUTBLC3iLc8OJZzd2PBsJDbv4gmDsR9TxFCWDhecWPbT4yf8UaHpA0uniypii-ZTW_-8EhI6RYN3LQYyRfPezM4bpYLuQeMXEszzDteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443384" target="_blank">📅 12:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443382">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kynJdSzi6CI8Kv3BWgAlVAb4rR-0cc92CXx0bDy19Rpuykpzrqh5FmzZMZuAxBkdX9il60IBa-BIYieYOMASVCoz6_sDtV4JztgPJhKvAEvT8V-I1BGUbMcN0E4J_npDjGqgyhFxCciLjPcUBn-JFMTVLXPbDl-YZAAavTuQbtsBkVTZ-n7uMLeLKlCCO5R2fAq8zxFPf0xikQUFcn-6lHKxJNnFJNXRkaBIy1zKv84vaqpX4h_zpnn9rVBE9-Q8VnlUZKS9Vb-J3PTlAKxskQVUerqX0nG38wrx6ypmBPO_xS_z1MsoWMh6cjDC-MoL9sshrr9-aRFixPxqgtJ7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anq_0joBi53N231kH_ukqTKal6qJBs2MEhyOJ3z3vFZsxo2aE4HpoOKBGzWS_KAJjxaC3D5VTzNTZcBb2ZDTHvFgBT2Dwv9M0wtBUxaYHx2KNERCo1y9OUhxLJl8yEK_-_-mE-Upn-akcAHqoSHz1a5NLI_cB4bqYkdEBbx6_MtIYY579MaaIp3pVHkIBWIGxUeY1DSifHvnCk25noaC_VV_vblmKi_wAUQA_AKJuHk6IxWsScVbA2ymlacp5BaHulXRDvrR2dWaSOLwu9XeFaPnOD3aA6_eL80y4SDFmNCam1mc8ZuMumTfKE9fmWbcWDogv7Mnt3eyZaTUehnKCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی:‌ تنگه هرمز همچنان برگ‌ برنده ایران است
🔹
رئیس جمهور ایالات متحده،‌ دونالد ترامپ ادعا می کند که جنگ، ایران را تضعیف کرده است؛ موضوعی که بسیاری از کاربران در ایکس با آن مخالفت کردند.
🔹
کاربران شبکه های اجتماعی بر قدرت مردمی ایران و تسلط این کشور بر تنگه هرمز به عنوان دو عنصر مهم در پیروزی ایران در برابر آمریکا تاکید می کنند.
🔹
برخی از کاربران آمریکایی با اشاره بر مقاومت مردمی و نظامی ایرانی ها در جنگ با آمریکا تاکید کردند جنگ ترامپ نتوانست کنترل ایرانی ها بر تنگه هرمز را به چالش بکشد و بندهای تفاهم نامه نشان دهنده شکست بزرگ آمریکا در برابر ایران است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/443382" target="_blank">📅 12:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWecX2YqgN5YGLaGckJXvD-VauEi9KDM9JO3RJnCjlF9RESjR4yLQqUPCZY0MkKIcFB6mIdC3-EYuvcm44DfFtFcMKpuezRaqBOPBgR5CO0KV8mqHrRydvvn9Jdqc_FLjyL5cf8g0AiMxPcUmF48a3jKOvQEzJmwCefD37l6haIUSqg8J42Ebn8sa63lprLHR7B_fdtk4DVvDtSmD74n227RzUr7jk0RTNJTLCrG_FDCZLWw_gPShVATNMHix2nb0f2iGzWB04jMgqoCcpVU6SYsG8X0-9o3-HZDkYe8ezLoTQaWrspLE1RosJxb0tySbohphiKahgzRkKpNEii5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در نشست همکاری پایدار اقتصادی ایران و چین مطرح شد
🔰
سه پیشنهاد مدیرعامل مس ایران برای توسعه همکاری‌های راهبردی با چین
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست هم‌اندیشی فعالان اقتصادی با رئیس مجلس، با تأکید بر ضرورت ارتقای همکاری‌های ایران و چین از سطح تجارت به سرمایه‌گذاری مشترک و انتقال فناوری، سه پیشنهاد راهبردی برای توسعه همکاری‌های دو کشور در صنعت مس ارائه کرد.
🔹
نشست «همکاری پایدار اقتصادی ایران و چین» امروز چهارشنبه ۲۷خردادماه با حضور دکتر محمدباقر قالیباف، رئیس مجلس شورای اسلامی و نماینده ویژه در امور چین، سیدمحمد اتابک، وزیر صنعت، معدن و تجارت و جمعی از فعالان اقتصادی برگزار شد.
🔹
در این نشست، دکتر مصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با اشاره به جایگاه چین به‌عنوان بزرگ‌ترین مصرف‌کننده مس جهان و نقش این کشور در توسعه صنایع پیشرفته، بر ظرفیت‌های گسترده همکاری میان دو کشور در زنجیره ارزش مس تأکید کرد.
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6R9
@mespress_ir</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/443380" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKEOzfXW0ah6URqX_dXLRV0SMQTaeRSIi9kzaPK3Ziaj5uCFsYE95oNlbr9Q-81-rU_WRcLKawOjGCqZAGE5PPtQKtr93ulNkQH9NEQ3hxYQeW1E3bBswogwfs9JUTuzbXPcTvnofr4ahaQCBJrnqOfr4OqN7SMTZCWC7fcyZUenePuq80XMv_gyLbd4jPWl2I6OZC-7grEUH4OpETX7XkGxjjBONZ1K7ecL5jSXNlVafGmlON41SgumFsw2El3UcByMsfoR2pHvq_GdKtJ4VMrc0EBeD7UtkmfMS4I8g7gyuCPyBHtcqiaogjEd1ZUrS5DtmK2t8knwor11hqjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
نمایشگاه پوشاک ایرانی-اسلامی در مشهد
◾️
به مناسبت ماه محرم سدن پوش با همکاری بانوان آلا برگزار می‌کند
📆
تاریخ ۱۹ خرداد تا ۹ تیر
(در روزهای چهارشنبه و پنجشنبه ۳ و ۴ تیرماه به دلیل ایام تاسوعا و عاشورا نمایشگاه تعطیل می‌باشد)
🕙
ساعت:
۱۰ صبح الی ۲۰ شب
📍
آدرس
: مشهد کوهسنگی ۲۸ پلاک ۲۲
◾️
پوشاک زنانه مناسب ماه محرم و اربعین
◾️
پوشاک کودک و نوجوان
◾️
پوشاک مردانه
◾️
محصولات سبک زندگی سالم
📣
تمام سود حاصل از فروش صرف امور فرهنگی و مهدوی می‌شود.
✅
ایران‌تن | رویدادهای پوشاک سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/443379" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/443378" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انهدام کنترل‌شدهٔ مهمات در بندرعباس
🔹
نفیسی، معاون استاندار هرمزگان: در راستای پاک‌سازی و ایمن‌سازی مناطق شهری از پرتابه‌های عمل‌نکردهٔ دشمن، عملیات انفجار کنترل‌شده امروز در مناطقی از بندرعباس انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/443377" target="_blank">📅 11:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصوبۀ دولت، رقابت برای ساختمان بهشت را داغ‌تر کرد
🔹
درحالی‌که زمان برگزاری انتخابات شوراها ۲ ماه پس از پایان قطعی جنگ تعیین شده، دولت با اصلاح آیین‌نامۀ انتخاب شهرداران، دایرۀ گزینه‌های شهرداری تهران را افزایش داد.
🔹
با ابلاغ معاون اول رئیس‌جمهور، در اصلاحیۀ جدید، مدیران ارشد دارای مدرک تحصیلی در رشته‌های مهندسی برق، مهندسی مکانیک و پزشکی هم می‌توانند شهردار شوند.
🔸
در مصوبۀ قبلی و با توجه به غیبت این ۳ رشته تحصیلی، افرادی همچون مسعود پزشکیان (رئیس جمهور)، محمدرضا عارف (معاون اول رئیس‌جمهور) و علیرضا زاکانی (شهرداری فعلی تهران) نمی‌توانستند به‌عنوان شهردار تهران فعالیت کنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/443376" target="_blank">📅 11:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg4T0wbBen20x7HRqnUzvi9-wilAnngL68JA5gIdB_FaOL9XSMO4IYpzWoYCCj19M_16kNH9SbLsiuTdjgBsBYsHYjbCHWeanp2CpJhemURFghcgXFfOiv0dR-XdUs2Zge8JggLlSjBOjNzT9bFCabg91A5eTUx7NtaQrlMa7slgB1KyBA8Gb9DqMsyeLDCXe0LoAxJvaJWKrsg0Gt_Nz3jii5-8XenjBAGjBG8VNVtI6ArFhm-IU9A_6K2oU-3qu87IIflpqInGrTKLwX9txF6aFZNKJRAO27nzsuBUN0SfO5Yuhp92GY8EAJN9gjcZhWB59fmbam7gg165-OaNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcrmJyHDNZ14-sE_9TIES6bwIsGcpB1axo95XM3fk02sAiRy18FY9fBSl7pyjkLE2TYXyVvZ2QdjKVhYrftu94JMiEbp2HblUPFqOeDHaZPyV_SBsfCvu9odoWnVfgQ-AQchCKX-zBIyWTb9BfYsMqjCLUmf52b4O-GRNWTPZIvdTkPF3QTxrircTmROGCloSPpNtlblDVmVsgbn1Rzmepw-IF4Mc79LXmJL7GYIYZm18LtVl9Zj1x3QUFkxSKxYlSkLUz4NS9V8_VucUqOV1BXR7Y29nYHWJnQeSPuenZJB4B1xDFEQ-fPh2bYZjjnimH7VZZpg0sI1lo2Qd8EWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dngral8lRnURsP35IsgHkinSqPYGMUxteVjQtimSIAGZ8ny8RLD8nDy-YOX4eAl77olyG3OBj-b8lnrzqws0Xs-BkUrhjbgcNkewbqXujJzvT8ef_Ul3fVH2XrtWIoijreqsoQixOUAXYeoHzgZnSoQiF9zWHPsDBbYxYRJUlKInlN_lB7caUSlpZyK2xDLqxK9ZZE8w-nkUleoezZqGBOk54XLQFuqZeyAEPNGES5k5ZaAUs3CjMdwcQCIhiAymL82wvynvcQyxkdiHRV_EHC4tyDSrOIwhp9C5YTlQ61X5V9bdQp7Q4rbjGKH5FTYnOLOZWcDsXflYMJtcmvwKWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا: شهید پاکپور مرد میدان، معمار تحولات عملیاتی و الگوی مدیریت جهادی بود
🔹
سرلشکر خلبان علی عبداللهی در دیدار با خانواده شهید پاکپور، فرمانده فقید کل سپاه: این شهید در بنیان‌گذاری یگان‌های زرهی سپاه، تحول‌آفرینی در نیروی زمینی سپاه، ایجاد امنیت پایدار در شمال‌غرب و جنوب‌شرق نقش بی‌نظیری داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/443373" target="_blank">📅 11:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OioQASMh_M1KKCbjupngSkR2IUFNLcPsOJxXfJ3CVaPd7GHCLAhV6dgtqVsJ2t7I7XcgnUnOMkGTknBoDpeqGmnWcplWPrEHETncHSkiSz34FJyzQpPMry3-9jSxWrO6wXqm7I_RZJ_h56Sp9ZPaTjfVOvdXV8YUi6XEhMQKaKxtVIse9_y42lzvV5H3Ik51y4p0ISayBMragO7RH00ygM4xw1DOv28GASM4gn4kO2vVQP4b69VD4MGD1Tmg2Bze84MsK9fpTLrXW1QnllH3aZmDUeMQwQtx6-7OSpmrjT0JR-VMmWLRab2BbGYolakTQ6wx8hvlrrF4omh0qATd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۲ مدیر اختلاسگر در سیستان‌وبلوچستان
🔹
دادستان عمومی زاهدان: ۲ مدیر متخلف به‌اتهام اختلاس و رشوه دستگیر شده و از یکی از متهمان ۵۰۰ میلیارد تومان طلا و وجه نقد توقیف شده است؛ به‌محض قطعیت دادنامه، رای صادرشده منتشر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/443372" target="_blank">📅 11:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443371" target="_blank">📅 11:32 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
