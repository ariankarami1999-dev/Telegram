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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 990 · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1iLxnnGDs6ZsKIbz_j_9RNFnuCt4XLZpfguYvHGiZ248i6qZU_0BonnNqQbMeUiBJYsqpgO5bIzZvTVCnBwlMxXPn_56ogkq2-b8HEvbc0kpOhNsxFtKNohShV5NnRbjVShJASEWE2CnlhldfWBQN26M4AF64mHVaj3dXdz1mXsBkeHwS8bh1GrFMAwiGeFROGSnEarMW_IWTkwcD7Jtkz3gUzSjXiCeVkF-btcXVHZyHgP3DTly7N6lsebQdQcZzLCSm1MCyfkRSBfrN6uiHDrDhXD_GESD2meq8ewDYwBpBHuRmvXprakjsOZVuqQORGLFCrbqlbzAtm9Ldkmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7CjlSYwTdkwTxOJR4OYQO3tYfU6Zz-eHjrKVbokmsgrvmWcoVNbsUDN-LLWV08NCiAEXDOncszhB6bhcs2FpOBMUNud87f2wW3NHk6AjPNeAsPj5XhMxAI-3zXJ_MDjE8bupXO7tYh5_JB8tH0rwLdCgVqWkSar_SR2jGPCtBX-Bg-hR8EJ_lHbcK8V07Wpz9a3a1K83ENjIzt-9b1fxzTb1bnUFjf6D9jWjKyepPnsW5dJtXVmlOtueJFuPfGpQP02IYJwKca48FT-1zVOemOm3IjCEgxltyJByAHnF0lvYx-jcfKS8yP24V0pRthPm10_D9LRk6jxxfkywUPjTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=G9Tw62SPV4LTLl1knDzJ0-A8-z8gm4kwrF3MgVekdn93u_znyuVEviComsYWpthdEvQAPu8iMuczx2WvTj21faxbVT5P9gJ-UyyBwly7234voyH2YBxgMiDla0eCVPuLAp4dIEcs4ZxThcJbpp5Rpsbh-XKSjW4Wo2jfsNywh0cIR-y8XbfQZKrbm8Zn9_yVWCDFguMuRAj9qt8B5Cwpp2QHpi3Acej-oB0QK1KitzXRHuI6qtWrJhPMSmGwjzcurOcJDuiAFAMgxJueB3M6uvGnpoVcREwD2Owdbkr7PfXMBFUvRgYpA1unA-9CJfm3M7P-21nX-6syrP3RB_xd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=G9Tw62SPV4LTLl1knDzJ0-A8-z8gm4kwrF3MgVekdn93u_znyuVEviComsYWpthdEvQAPu8iMuczx2WvTj21faxbVT5P9gJ-UyyBwly7234voyH2YBxgMiDla0eCVPuLAp4dIEcs4ZxThcJbpp5Rpsbh-XKSjW4Wo2jfsNywh0cIR-y8XbfQZKrbm8Zn9_yVWCDFguMuRAj9qt8B5Cwpp2QHpi3Acej-oB0QK1KitzXRHuI6qtWrJhPMSmGwjzcurOcJDuiAFAMgxJueB3M6uvGnpoVcREwD2Owdbkr7PfXMBFUvRgYpA1unA-9CJfm3M7P-21nX-6syrP3RB_xd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UG3_TBFpk5zhi-cUWinDQseVrmJIO1jEzU0__rJL0A47cxi2hO1nZxU2tO0bUJliq4xTnGVJShLqHtwZ_23l9cmNmSpx6ud88I2XKlMUC1Np4wMsFE45ln5stCkj-9o4VC6IsYEDgWtxEDAWKZSzZVYHdN3LdzQ5pGVTIenrTofLdhRt4evz_jY-D-I3Zs4aJTAwbzSs6fSqEM5aeZLJL5AKaKOMZXOuDs6YksN6ZXYBwi2VS7ELk4tqxlePzr505xuSqUOiSbkPW-96As7APOE9tNknPTklFuVlNRv28c8KakMl7xK_PRNVEwfmbStHGxRh4H7cyy4jP8UinOAVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UG3_TBFpk5zhi-cUWinDQseVrmJIO1jEzU0__rJL0A47cxi2hO1nZxU2tO0bUJliq4xTnGVJShLqHtwZ_23l9cmNmSpx6ud88I2XKlMUC1Np4wMsFE45ln5stCkj-9o4VC6IsYEDgWtxEDAWKZSzZVYHdN3LdzQ5pGVTIenrTofLdhRt4evz_jY-D-I3Zs4aJTAwbzSs6fSqEM5aeZLJL5AKaKOMZXOuDs6YksN6ZXYBwi2VS7ELk4tqxlePzr505xuSqUOiSbkPW-96As7APOE9tNknPTklFuVlNRv28c8KakMl7xK_PRNVEwfmbStHGxRh4H7cyy4jP8UinOAVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZR0VCvnEz-2-ZbL5eeiND8SI1BpsLDoRmrnM5hFsHdMD_dtm_c_pLoR3pcCYQTI5Yld1PURdM5TfSbhRbVvwS2UoE9zWA3xT_FiDDo1RhysLdVVMBe3I1Uo4PMsAWOWmp_cBKHhHU_BvwCkZ-FEIssygILBuZKS9nlTnLdfDLFqiWW7-UF6_8yj1ee1w40DwPCdRDrEPYO8ZC_-293V3uLHPfKy3bk0tf_tX-9KvzCf7WS46Sq4vbGwOvSFe15ZfA06KYSy99uvLQPVDHjZ_Gy-abqBrdekfaNfiC-T4SSQjUqvClWZqeSriZA39IaCTvDymV7AYEMQqVuf0Si6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=a3prY700Ub9KtdQTO5X8lDZ9YBMVDsTIhD6-G9UZRRhHf3O1fl2wk5lseLUhlqYMBetlHqBQR2u-NqkDXdHr0TEXcZdxhfPOMBZ7F_bRH1jIauvgAY25f4WauhTXnvvpLaVhMHzggar6kWJBAkr9PiHqAgpocqGPlaYVIsi_HyKrNO50fOiuanT5Hxb5KDpm6IfJ4UN8YE0hzGqehHJcRQAY6q4RYKT2mmaheJ0xmCQT9q-bUgkqviwwC32vo-xoCzpLk14dOFLYMvafAXwETQy2OBCIopkVR6OTDvgfV1ewPnNlVWERCh1LgiwCkA0WKCQk5otb2z0mUFPlAqPy2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=a3prY700Ub9KtdQTO5X8lDZ9YBMVDsTIhD6-G9UZRRhHf3O1fl2wk5lseLUhlqYMBetlHqBQR2u-NqkDXdHr0TEXcZdxhfPOMBZ7F_bRH1jIauvgAY25f4WauhTXnvvpLaVhMHzggar6kWJBAkr9PiHqAgpocqGPlaYVIsi_HyKrNO50fOiuanT5Hxb5KDpm6IfJ4UN8YE0hzGqehHJcRQAY6q4RYKT2mmaheJ0xmCQT9q-bUgkqviwwC32vo-xoCzpLk14dOFLYMvafAXwETQy2OBCIopkVR6OTDvgfV1ewPnNlVWERCh1LgiwCkA0WKCQk5otb2z0mUFPlAqPy2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RluRRdrMsgs1xGOEkx_OnCZisPkucOWm034iYC83MxNs1YWskuDXMnEvnwK0GuiQLeGDwkFqzCwLHI_v6Nmk12sAs7RErv5ZDEWIEIOWIV4Jrh3_wXerWwGycyDCYr6eQex2o9UWQXEGWr2mcZ2Pi-dW82Jtjyf2sjB2O3L0kkYidV7rVHGpchLxRgCskwgmg6tYS2LR6zK1cf-BgnLP2Q0dYfa7OYeoylPDqxCdbtv6g7jXdm_FYu156n3rmYy1ePCTiTalBCY-kOvzcYxQQ2N92eNxmn1MaKQzw5H4KT_JzPpgGVAP4lvK_a1f_ZZlSgH6eSDDrizAr1_epUxaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=VTyWHRolXhS9ryXICJVp_sEyMX_Fu6oo7Ma3tNg3Mv8q4AR2axMISVbmhOqZnrll5Qrl06dUfwXB5i-iOfQaQX6maT-_0hRn9ynjFyN9XffDudXyPLgzQynDIUbGoEttu-_TJ-oub47063p0ZS9bZ2--ot9sUl1MDdjh_NL99K67W49UdKknF-GJs8tFTBverMnhFCByBDm0r3VXMIRIL8mLv6NUMvg33N-kGDXj5OZZ1Wgwa6jIxldFmDOoq0vUEnONflDcD8CS9pKxtiub-ogtFZLKXL9sXM9AQ_nAgACMOsga-3UOFnttuVfg4fEWEJISxAzLsbaARwlGTAHKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=VTyWHRolXhS9ryXICJVp_sEyMX_Fu6oo7Ma3tNg3Mv8q4AR2axMISVbmhOqZnrll5Qrl06dUfwXB5i-iOfQaQX6maT-_0hRn9ynjFyN9XffDudXyPLgzQynDIUbGoEttu-_TJ-oub47063p0ZS9bZ2--ot9sUl1MDdjh_NL99K67W49UdKknF-GJs8tFTBverMnhFCByBDm0r3VXMIRIL8mLv6NUMvg33N-kGDXj5OZZ1Wgwa6jIxldFmDOoq0vUEnONflDcD8CS9pKxtiub-ogtFZLKXL9sXM9AQ_nAgACMOsga-3UOFnttuVfg4fEWEJISxAzLsbaARwlGTAHKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Qw2Q1J2RlbEV-wJTodXoiGxe17jZdFE5I_GsLAq4ljQ-B6Xb5mLw_k5RKf7CCXMZZCvk5Er3GN6y5fGLu8V4KraNInvzw_iJxt7fTxIPuxopVLZo38l0SIKabh1a19Eq3wOHu2JXSL34rbx2yeqvcDxiVVIIUGKnim5r8tnxa9VPfQoS3FHtsN489GMoxK5yYK1CUgA1Cw5HQyoESihTA37wi6PX2H4321Bb5IbbZbWQq13zTVriItAcirJRp-_0xAjvMXp-Yz28eMRvwbdbeyAaGJrP1yNXYz8E8qb3yDONZsdFib1XtIOixfvPSTt9m5imFYfqtkBl18Ip6iZRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Qw2Q1J2RlbEV-wJTodXoiGxe17jZdFE5I_GsLAq4ljQ-B6Xb5mLw_k5RKf7CCXMZZCvk5Er3GN6y5fGLu8V4KraNInvzw_iJxt7fTxIPuxopVLZo38l0SIKabh1a19Eq3wOHu2JXSL34rbx2yeqvcDxiVVIIUGKnim5r8tnxa9VPfQoS3FHtsN489GMoxK5yYK1CUgA1Cw5HQyoESihTA37wi6PX2H4321Bb5IbbZbWQq13zTVriItAcirJRp-_0xAjvMXp-Yz28eMRvwbdbeyAaGJrP1yNXYz8E8qb3yDONZsdFib1XtIOixfvPSTt9m5imFYfqtkBl18Ip6iZRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im5QaLQ4yf_kibN7sDdJVy2brQswdEH3YMPi3XsILJTZHV3sGLfkO5zjl5_oIksWpGzlr2_gcMn_36PksCpQjU50GAAWdzOyWoJ_4jFuhWwiAz0y8R91VZbxO7bhye-XIk_s8wqK6R4XGWLDS5a4GbqeCpblMRhOBreBeEmP-_yDy8t8D8H1rXUop2RNzvMjEj5JF443n3clMmhFL6EGeehLSPKFYjM7Q5kqASR7jEpK_hNKdAOnFuOIF4KryD5j_FZId_KyBVTz9RcpXZsbueDAGhs-xw_Tu7G9xWiYteBtdKZxau4e71WPbuHN57ifOiAfxls5WdPCx7rfyGB58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=jhWoj6j1iNB7adORV29ZFGJJjMiGiyo_--8HyiHBXNngq-wfiehvo8f219AkrAJxX_0osndU756ON0jJIK0GPX9evBWxPNatIKPhdfzkT6mnF_-dvH5WaUSRyVTY-lwhyTo2x0z01oRIEql9L0ORuswysEp2K-t_SMo4Na_96F0tHQ4aPUqwSDcN1JVzTlGUb2fZvfUp6JSeJ51Dxr1f6cl3auoRPcPZ4SU-wMtg7YTbEpZPBw9NHzbx82zkMj_TI57icAlVu2DoSSHe_cFBR3otH6Hb5yo6VKygHiVM0bdlTLrGV9k-i7JlOgWnkIp0z6DWyP_niRIt2apa41RnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=jhWoj6j1iNB7adORV29ZFGJJjMiGiyo_--8HyiHBXNngq-wfiehvo8f219AkrAJxX_0osndU756ON0jJIK0GPX9evBWxPNatIKPhdfzkT6mnF_-dvH5WaUSRyVTY-lwhyTo2x0z01oRIEql9L0ORuswysEp2K-t_SMo4Na_96F0tHQ4aPUqwSDcN1JVzTlGUb2fZvfUp6JSeJ51Dxr1f6cl3auoRPcPZ4SU-wMtg7YTbEpZPBw9NHzbx82zkMj_TI57icAlVu2DoSSHe_cFBR3otH6Hb5yo6VKygHiVM0bdlTLrGV9k-i7JlOgWnkIp0z6DWyP_niRIt2apa41RnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=H9paVXJDwRzdz-_ahZ-YeA9JlDBvaKGZuqdVmyxyL4hoLo5_mz_hEFGRwc8Hzg1GJTi8c6Z9ZfpXCWXpWAeu6t84n9repwX9Qhu0dbbkER-7O1y9lmipybSA1S0_bxNI2D4MvUUuVp5mgCbEJQrwNRTM3GEVHJoXQqLZ_8z7mbmydmPCRWYSwgFWm2mrohGyxG7AIvVTXnjvSy4r6qsXZLJsDKkZtcyGWNfbds3xbgqCnBprnXReSU3iV1XyLNC5152RonYBGJ2wZDQg-vRI4UI7gvruPCNK0E6jyzCv8hgL0oPT2CuMf6wVC4877uK9PiOjsxwrrZD4ufPvy_wEAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=H9paVXJDwRzdz-_ahZ-YeA9JlDBvaKGZuqdVmyxyL4hoLo5_mz_hEFGRwc8Hzg1GJTi8c6Z9ZfpXCWXpWAeu6t84n9repwX9Qhu0dbbkER-7O1y9lmipybSA1S0_bxNI2D4MvUUuVp5mgCbEJQrwNRTM3GEVHJoXQqLZ_8z7mbmydmPCRWYSwgFWm2mrohGyxG7AIvVTXnjvSy4r6qsXZLJsDKkZtcyGWNfbds3xbgqCnBprnXReSU3iV1XyLNC5152RonYBGJ2wZDQg-vRI4UI7gvruPCNK0E6jyzCv8hgL0oPT2CuMf6wVC4877uK9PiOjsxwrrZD4ufPvy_wEAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4rrMwK5FO6UzOSyxIO-u5B7CL81pitDEvI0Gb7OHTJBcBciCt9zUElgctMIQviEbECuy__hZ52KHZmKAYoHkE5c7V643xiRvu3DbbGUSej9brH6dGM1FyIf0sxSGVFH7PgURQa0YvdDvtauB_Y4_hQUvvtbwTgYchClEh2DW-5nPsFN5VHfXG1E_BkPN7F9F3NQGkbftWCv6ZrCrGRGfUodBEzF_zPYZ2FsliC6grVv8ph_dU5-Sl66pOJKhaJ_01a7sZ-yGJIQDNtEZ6KX2eXkyKVO5amVciQN2b2ekIiPnH5oHCOf-Zs_GE5Ri5YZ9vl-_iYY71wkR-xnrmaO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwsFrRbtHN-e1yKKDPSFIoGDhdmtQNZ7aRVdkKxLCtufn6OIDy70KyR0SGay2lbcpi_7ZGoZEMu7y9ctsGNiyGFl1oyaen5AkGPRfMohejzAnNNOqXZhWd1B1tyc1v4SZabq2P92x70P9SD7AVQN4gkCiUpplPUt4HElTE3EpSvUYZ3mNqjBDBP8ejwvjaF8lOApTmp_jIbNR3WNoVpkRHG8c66QST1XPEZOwp1CxYv7zBhW0jNyPqAt3T3fHDGunDv4xw88xSakGMybDKRztFAZrYHx3bkcFIkptnX4JYBscmJjswofOpO0Xkv25AhaoZtzvgFSv6EpDU8dA4S_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRWiqleJZ9iYXlokUO3N624evVNIPlFppJqRg2l7vroOJXgHlZT-oEhvdCltUHVPiA3-DD-HNgjAwWmPb8zNT50SW7DeAfrSxibq2AK5AjxYDsBBcpaumOJLPjzUWdukxbMTzHomcpWBwbCRFI5SkCB_QNwmP6HTzMMSAQWGmRMZX0iaEE3rtLsrb3IcFnjitWtMnAiV5-91D_q4x9VTvJeUDusIo_rsIxdgfHB5sjIBJnAirpOFKD_qP0XL1STnOHTgu1F5ptmEwxyCq0poTwwkfB6Tci6atla3Syf0tiANzhxwFqQOzjUQ68mn0OGW4D5K70N0UHXxoTolIjY4VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dOBhsVMa7ovdmspBHH5ThBc0fIsQN82FuPNpunou1eobILR4fO8lIZnIdU5sPOUMuI8U9QEh6hmmLDGBi1aJkdd6TPHzVBNP9hT_y8OU4r43XiP8g82u6MTsrhjbPlhqiuXDbjBD5N2YdqHO8vwUiYhMjjfTOnGT5VaBFOcs2-jDHZIRyJkIevsExrDHill7DwMpLLXnKjp_MSwGY7web79Sgj_LNJ3-lEK7EK6ab6dFOnsjkfwRxnRm02hmMoirba9hQa4fkM5wtFl6BRTJbPgC8efVM6Ky9A04Uo9ZLFLwGu-JTQJzWB0zG7UXfMcutrJdKWUddY0ntOri8MOseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dOBhsVMa7ovdmspBHH5ThBc0fIsQN82FuPNpunou1eobILR4fO8lIZnIdU5sPOUMuI8U9QEh6hmmLDGBi1aJkdd6TPHzVBNP9hT_y8OU4r43XiP8g82u6MTsrhjbPlhqiuXDbjBD5N2YdqHO8vwUiYhMjjfTOnGT5VaBFOcs2-jDHZIRyJkIevsExrDHill7DwMpLLXnKjp_MSwGY7web79Sgj_LNJ3-lEK7EK6ab6dFOnsjkfwRxnRm02hmMoirba9hQa4fkM5wtFl6BRTJbPgC8efVM6Ky9A04Uo9ZLFLwGu-JTQJzWB0zG7UXfMcutrJdKWUddY0ntOri8MOseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=MlxH5U1uP1wQTJ_aHirplFy9itugZIF4rn7k8jRyceowbQDtDpD1oHR93x47IgziDFcd293soqroPk8wOzhSKSCkfD19MXUxz63uEuA3S0nz08NTJMCf5pvMw6X2tTs7Xb_GiAdukXQjnsvy_yZun_kQNBjYVz2O4fJdWexPBF-IB4YKE50QGmx82jNZHfhOg1DQUEvRRA3-2k7Y_NXh0y_5TajroSkC54cWe7dQpRtkJGlVGH_O-S7WeUGHqKNHHW0bj61Z-8ib-aeIw5UHfw2o8FuS7hPMhgb-j4wKkf-1fn-H2yV6GdkVQ54gw4HxKMQK78eZlq95xrUNZ37Lvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=MlxH5U1uP1wQTJ_aHirplFy9itugZIF4rn7k8jRyceowbQDtDpD1oHR93x47IgziDFcd293soqroPk8wOzhSKSCkfD19MXUxz63uEuA3S0nz08NTJMCf5pvMw6X2tTs7Xb_GiAdukXQjnsvy_yZun_kQNBjYVz2O4fJdWexPBF-IB4YKE50QGmx82jNZHfhOg1DQUEvRRA3-2k7Y_NXh0y_5TajroSkC54cWe7dQpRtkJGlVGH_O-S7WeUGHqKNHHW0bj61Z-8ib-aeIw5UHfw2o8FuS7hPMhgb-j4wKkf-1fn-H2yV6GdkVQ54gw4HxKMQK78eZlq95xrUNZ37Lvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6RReQs1C2dT_zwqZBbnVYJgPDGkqnkBHCix-wRAxEbIvckp6okwq7jeo7lzKKxkmVH_X4racQS6prjV6Ng-u0eKP-8tvh2sJxKNs8dx6sOPWQN5DTxbH_hTA20v7FQbe8f6lK6_c-zKlRRHPJAcrhM5tAYRclNUI2obE6m9tIwtqXnKAyx8POShTqNRqqiWV751zdUGz86SZOHCvcGc3L1sMXPHLrKiJVp9RgDXMiBVEy4kDL18_ot782iEWGQri510Bx_VhlsF7Dz_4Os9PElPRVYWWLKoG-OGEcSHDBoqoEKIACZMbB6-zzD5yvCxs5kKJAZmF7gRTpW8KY9fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=TpqRNdJODhKxW056i7iMJjS1zVAWBKBRKQNOsOhyWF1l7-u851HJioWpCGuU46LvImJJiSrX9SfgVX7IT2-l8ZxWTGMZabxMx0ilUkfxUKu0AcyvIhZzMCOxtRE7yPGAlt4szs9fdwXVxpuwfqFsGV-R-_B6Lb9DqlWaM6P5Rd7F2s374_Vh6NFbtMI4QUQds3EQhU7VMzVvF5WgrOz16Ae-va1_TZ2NnnXbmn066sLzkBngAsAHFYiWFi8mHFOgLw2QCvfST8IVwcVCicnhEHL4ia-VUrJsPMPDwg91H8RNK336yeaaGKIPUFeRcJWSgbT6MQE1IPst48PzPzf-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=TpqRNdJODhKxW056i7iMJjS1zVAWBKBRKQNOsOhyWF1l7-u851HJioWpCGuU46LvImJJiSrX9SfgVX7IT2-l8ZxWTGMZabxMx0ilUkfxUKu0AcyvIhZzMCOxtRE7yPGAlt4szs9fdwXVxpuwfqFsGV-R-_B6Lb9DqlWaM6P5Rd7F2s374_Vh6NFbtMI4QUQds3EQhU7VMzVvF5WgrOz16Ae-va1_TZ2NnnXbmn066sLzkBngAsAHFYiWFi8mHFOgLw2QCvfST8IVwcVCicnhEHL4ia-VUrJsPMPDwg91H8RNK336yeaaGKIPUFeRcJWSgbT6MQE1IPst48PzPzf-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=tCqjAOJVHeczCCD5-O3TnJeyRTBlelscB7ePXK-sQPollubjHY4ENn-zuV8banoLkvgasYqR57Qd0RbQFkdFc8osLB-0v6mwzZhtrq3KgtwFRo5KgB7U9GeOQMB_iFmPfjdxejRV1kVPE55X7cM4HieyWbZiPbwdnAt6S9gXS-0KoYPP9rlhgH4z_3EAcTZBc6_6aKFAY6OlYaAwas20GJaCP9aV84yXAVJNB7nBQ2r9Z1lOpV66y6XT3EK6WK3X8S2HN7CBXVP_DLm5xTv1jMjJB6csBt2A7TJkjKBNhHXVnvklUA9qvscP5nj_IEzqjLsEoMywhIUxhDQcuudBtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=tCqjAOJVHeczCCD5-O3TnJeyRTBlelscB7ePXK-sQPollubjHY4ENn-zuV8banoLkvgasYqR57Qd0RbQFkdFc8osLB-0v6mwzZhtrq3KgtwFRo5KgB7U9GeOQMB_iFmPfjdxejRV1kVPE55X7cM4HieyWbZiPbwdnAt6S9gXS-0KoYPP9rlhgH4z_3EAcTZBc6_6aKFAY6OlYaAwas20GJaCP9aV84yXAVJNB7nBQ2r9Z1lOpV66y6XT3EK6WK3X8S2HN7CBXVP_DLm5xTv1jMjJB6csBt2A7TJkjKBNhHXVnvklUA9qvscP5nj_IEzqjLsEoMywhIUxhDQcuudBtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=eu9da9m7jIXaCVAQEL0lxS7H4OT6I9gydmdQ_0wyhHo_jZfHgLNKQUJNK8iwhZ-V2Z_vWwvfM2NKQ5XKUbuIJKBWDRyN_Asp0FC-1onj3XIUCGJGUAvNRWDrDsvO4eHyG7sX-QwQsvPjvJ5OpR3J1EXuSN4uyor1L_TV4LOCb2KZ_avcCDzO75dtaUJz_q-wtPgKvwSyIScPAL3tm0EdRvXB4S9_JWxmcktdIJr4HbA8DOXpGJ9sD-reaSWNKLYOlv9tBH_O-wdWUf_ntYB07H_BWNVEpatavX7-bQ3TbdpLlKOPoK5bcmiR7-o8DLCx7AKVXXkySiK87mXgvcW8IlhllbUEwAGAUYQ1M-QJAdoNTgS1l5sBxeN-5ruD6PMbz4dnktfOY8d8Of2Plfzxf1DsPrVRLvatbDW0h8UJZCgzUxM338pZxV8v3aBgFP7ZYJvzyZas3GJLtHYrJk4_-JZb94yZwwWdQ8d8i5FwcSPjmoU7uPd0RiYKUnwbxwfo1_xXsUujOWP7SO0mt5NoIKa9wlTJS45979fVDa6PCsEOaBosIxBht7NVfSa1wN8dfPhPm3T06EinZYHbTMK5BpQG-PYhWxFVQqNBdL_f07iA9OAaTDTKoPoPYkE2aBCuG5iCdl3j2rIhz99bykXHPciK5S3M8TAUotItjpIwPP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=eu9da9m7jIXaCVAQEL0lxS7H4OT6I9gydmdQ_0wyhHo_jZfHgLNKQUJNK8iwhZ-V2Z_vWwvfM2NKQ5XKUbuIJKBWDRyN_Asp0FC-1onj3XIUCGJGUAvNRWDrDsvO4eHyG7sX-QwQsvPjvJ5OpR3J1EXuSN4uyor1L_TV4LOCb2KZ_avcCDzO75dtaUJz_q-wtPgKvwSyIScPAL3tm0EdRvXB4S9_JWxmcktdIJr4HbA8DOXpGJ9sD-reaSWNKLYOlv9tBH_O-wdWUf_ntYB07H_BWNVEpatavX7-bQ3TbdpLlKOPoK5bcmiR7-o8DLCx7AKVXXkySiK87mXgvcW8IlhllbUEwAGAUYQ1M-QJAdoNTgS1l5sBxeN-5ruD6PMbz4dnktfOY8d8Of2Plfzxf1DsPrVRLvatbDW0h8UJZCgzUxM338pZxV8v3aBgFP7ZYJvzyZas3GJLtHYrJk4_-JZb94yZwwWdQ8d8i5FwcSPjmoU7uPd0RiYKUnwbxwfo1_xXsUujOWP7SO0mt5NoIKa9wlTJS45979fVDa6PCsEOaBosIxBht7NVfSa1wN8dfPhPm3T06EinZYHbTMK5BpQG-PYhWxFVQqNBdL_f07iA9OAaTDTKoPoPYkE2aBCuG5iCdl3j2rIhz99bykXHPciK5S3M8TAUotItjpIwPP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdo1EEUYDLy_zZduCbmQF8uempwzt7PO8CCNzRT9WN2Iw-j9zAkpUzGC_qD8TCkeIZg4Z1Lc3lnbU2NQPh2r2hP1EF3dRanomKv1rXCHtgIt-Ml3GgLT8VETWQBvgIZub2pd0IETdfQQh8Sdg7vE87O1meULrc3h47vGrkeHCJD3m3FcNUEXhRWwRpDEZctyWz5kIawjk4i2BRLLSNyUwFzKrymbBzo5SPcrVWeIlBNx2s8sCcXLMFp7_mSB8Wok7-XyDnijAmDNUrHdWm2OmQU-4Km89MrYpWiE7WTq2sNIuk8dXrTl9KrzglTLzmh8t9hkQzqwty8-Urpe5loTbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jJnUyxBh_K3V7yTmhP-68pETBDQEDU_L60a8FK0cmrDz9jdx9cuaOV2C5vDr79rtokaXCM1MmhuA8iVJq6bQvXUhaGi1tDRRJ_wlfKsLQTDttewuDwR9AfiH7Z9l1rS3HxeAvL75aHlCvjduDGYCahkMCMv5SDyvTXSr7fnVSaqkRRb0dB2I20uTrmOkh0fLjp6YoNAj44FgjRMREeODBMF4G-mnDHAMEBpIuuclOKTkIebmrKo_QkfqE6XL9Y3ad7f9gHP0bAjOIGGLCnYkpYPkWGnO4TbCgU4D8tuJbeiDzwHPoUVhVHQF_CHlTrkEPJJeIb16TRadl5L9lf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=AYoBi8XNUi6P-ibDd_zh2Efu1h1XrsonfwTUNBknsyYYXRJhnNWKtXTw8BYgvfht-oASwL0DkDtpp6oBaGpuxIoqVQmOHQEG6vyIqBMnp7HHKlj0g7PfynD_n_1TRKR7zwYqJMv9etAS7VIa-G8J2-2OtypqFJSvYjORQPQEeGQ5S2ggLljyBkRlVQJkngInYiUvvjQI7KdOEZLC4y_nJw1v_FAGhOFMdymXMDRJHen5Hagc-9m6Pgs5Z3YdYzpMr-SjQgTVdD1CGbWKNMWg510Z4Mt8_WPmrQOoYZ6JwXeO0NjXIVgOVMDmFsQiPI8GoCjUEZt2ZnN1LEor19IJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=AYoBi8XNUi6P-ibDd_zh2Efu1h1XrsonfwTUNBknsyYYXRJhnNWKtXTw8BYgvfht-oASwL0DkDtpp6oBaGpuxIoqVQmOHQEG6vyIqBMnp7HHKlj0g7PfynD_n_1TRKR7zwYqJMv9etAS7VIa-G8J2-2OtypqFJSvYjORQPQEeGQ5S2ggLljyBkRlVQJkngInYiUvvjQI7KdOEZLC4y_nJw1v_FAGhOFMdymXMDRJHen5Hagc-9m6Pgs5Z3YdYzpMr-SjQgTVdD1CGbWKNMWg510Z4Mt8_WPmrQOoYZ6JwXeO0NjXIVgOVMDmFsQiPI8GoCjUEZt2ZnN1LEor19IJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxDgzRDfPmtnNiCtEbnha_QTuDjSYa0tq3Qx-dMleehrtMCSRIrQIjMjys_1xbhQgnuH6HLShaZZBS3iaLkIwZ9dfN0n4FWbwodjofHehsZOsJ7QuiDU54Yl9j6kUpU3_qt6E3-Z_fMUhW-ycBKWXe6Up2Lq2AKzyptDxsgC8-CqOrKNhfu5yC7ZWLjPXaKisTKJK7N6bgQEWR3EXAxiCq9JpFEAzwCdVJOc5DDbMU6G8mpMWy_VK8C4A-q3d5PIYjXKmy-pLyw1Sa37IgVmxL63CuzeTaLqlMrQEUBsHGe5NKsyRt8XNidVff2INqhu2mhQ7Z6NEkHPhATFfYEDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT5GCovzrOhFdEyK6MUjb1-7bIQEsIjLI_HWFc0T1cKlTJ92nBMX7VhlZLVmzfrZE_hZ2a0S9AP9ZGYw8u-c4ibHHOw0whmXKouoUpqH5py6_5LBJbTUlx0enzLnmO3SKzYYVHnb3cTAYx9smxlzQNzbO0gE8DREBx7kHQ1ZIxz410gAHouey2deex3Tw_rh_OC4kiXWyjLFt5zQJIxul0XKuXF-3sqw09jdHQKt_NI_Xce-Khk1iDbUyfFFaR7bTCBwpFrTM9qC9V1WkTSr-bFxeqdo8tB6Thgou99mzrtoWsfWwMavPOM83m6DpjCrZJiss4HNVyeZLpOsyplywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=dsjasIIgYEltG1ucKHQVv5rD6XrMB8V4FaaFViyTxujpYDePgQiQXBLnrrClMXdnsDqe9dfCi9_R186mRU0DfYS3d_Mn-ufyJ-lnr2tsQiHUSBkkMAqjEUWoVpjrXWNzZe59RPJfgwM_MD7hV1UYfgrObiPA1NFzqFw8TWAk1l8PVhtV5D2XI31FmM3M8sKpGqngTVhUEopOstitk6Xx9OrQR2z-Z01nrLZdS1aFcNrJ6rOMWIqxM9hR69YwaKJ2g28qhlvY5nl4rCknwDL9RFfyvbCyXJnrPf4AJG84mTLcz2Jta3jSckKa_8T8nO-mNsUvVs9Eh_43olJJGCDedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=dsjasIIgYEltG1ucKHQVv5rD6XrMB8V4FaaFViyTxujpYDePgQiQXBLnrrClMXdnsDqe9dfCi9_R186mRU0DfYS3d_Mn-ufyJ-lnr2tsQiHUSBkkMAqjEUWoVpjrXWNzZe59RPJfgwM_MD7hV1UYfgrObiPA1NFzqFw8TWAk1l8PVhtV5D2XI31FmM3M8sKpGqngTVhUEopOstitk6Xx9OrQR2z-Z01nrLZdS1aFcNrJ6rOMWIqxM9hR69YwaKJ2g28qhlvY5nl4rCknwDL9RFfyvbCyXJnrPf4AJG84mTLcz2Jta3jSckKa_8T8nO-mNsUvVs9Eh_43olJJGCDedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Z6z4yxMDDFf4nzzZMAMRVAnfNZVg2hK0ERojx0ysdcYzhnvgode6byoWIA_BjW7iJPYxVNBZds1vBKhcsKFJYZVAmWVhPBC1kFEXcU_czfHuqn0lZlbbFs-Zjnqdz1J3FZorrnMNuwuJb0ua9M7jTt-HLrO2JYdbEEauKxLKgp6wIZ9GyzPXKpu6R6_gB9RaKo8_3L_gobkG7_ecWJVi4ITdMkQfo7k0MIIEyd8mcPBrFGwC2lqBRljPcfA4uyGWsiVpiF_5xZLNxL-gd6jZHmZ_ZNahOKxEOemBCF4wIwD9Xa7Rt7qULyc90Td3OHdalVIXldf2ZO27PwTMkPcvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Z6z4yxMDDFf4nzzZMAMRVAnfNZVg2hK0ERojx0ysdcYzhnvgode6byoWIA_BjW7iJPYxVNBZds1vBKhcsKFJYZVAmWVhPBC1kFEXcU_czfHuqn0lZlbbFs-Zjnqdz1J3FZorrnMNuwuJb0ua9M7jTt-HLrO2JYdbEEauKxLKgp6wIZ9GyzPXKpu6R6_gB9RaKo8_3L_gobkG7_ecWJVi4ITdMkQfo7k0MIIEyd8mcPBrFGwC2lqBRljPcfA4uyGWsiVpiF_5xZLNxL-gd6jZHmZ_ZNahOKxEOemBCF4wIwD9Xa7Rt7qULyc90Td3OHdalVIXldf2ZO27PwTMkPcvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1AMlEj_e8s6hmzLFgAJOy4COgz6bf1Tb6MEHUaKoqtzrtVh-x2zXwfcgUF0o82AvFoVwqAVIVYCjWtNozVUPwVSUwNvD2cCHnnxBAMuHtr5lz35bifecGMPc5myelm4w00pKuekHBp4nD9vesKjSXRJGDxT-q4ezEqkMBA4RKJqGGRUzSV6AvZ4jmTELUlv-MpsV-wd-nwdGYqU13R9_asWH9kroEiR0AjIXSS6QP5jvE1pi5ZjCaLpimb0faJ3D90gMBkzNSyAHyPBdsh-b2jazKchPNxoo7qicC3UilweR218m6gg12pJq9K8LxUCxSQh2NjRxHzpdy_gaDizGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csX5kOaHyvDoUmmpG7tqRPI5Hn1MZQjAjNN0ZUVOIYWY7D_CI5iepjUnuDic2OCZ_FF6B6cmArEEEOsui_rvmG8zZbcq3eJnAdJu6acNke6qV9M8H-UXCFCxz9GIPDESaBPi5yFtBQFeia1Bfa3zL49HHWWV7Ew2g29vDRXuPODfbuC9elDFw3VNYdLcz3ifAXeBsxhrAm76hz9aVCQyj2pfWQ1g6oun3L0_kYzbk8xGQS5MyO-H_LghclxU9zfuiuCYI106_QCHL7gbB1NhFIBSVKpKjVWkaEGjkoFbKdQYFTwe2EPd4zt7psENrr9syglxxTKGULNGULMSB401Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=OlWwCjQNRnw62Pytjs2D9yp3AZ6CvdHLte8a9mU2INuijh2ySAj4KpE-YYfplRVJSBARPognmmaPSR2EG_aF5HGEwdJZifkbWsmjpm1pdRAUqFz4iJlYXUOnbTnOYFpKZNihF41aK1-mvf4QH4Kwz4GOzWhr4XtxnbUION4LgIQ2DpJo4moqgrpANdV8LQblTUxQRJjWyNG-KyUqCQLdS9H2nImdMmIoBIV3rB7ieRZ70gf0hJ5jPEta1WUUjPuDX7CcoxHBmIPl_fhPYsCT70rvHUpFFoZu44mj9tSv9U4uIoVyJpV9NWT2Dg9XSpItDoxZJdDeNqQeGoCTERpNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=OlWwCjQNRnw62Pytjs2D9yp3AZ6CvdHLte8a9mU2INuijh2ySAj4KpE-YYfplRVJSBARPognmmaPSR2EG_aF5HGEwdJZifkbWsmjpm1pdRAUqFz4iJlYXUOnbTnOYFpKZNihF41aK1-mvf4QH4Kwz4GOzWhr4XtxnbUION4LgIQ2DpJo4moqgrpANdV8LQblTUxQRJjWyNG-KyUqCQLdS9H2nImdMmIoBIV3rB7ieRZ70gf0hJ5jPEta1WUUjPuDX7CcoxHBmIPl_fhPYsCT70rvHUpFFoZu44mj9tSv9U4uIoVyJpV9NWT2Dg9XSpItDoxZJdDeNqQeGoCTERpNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJP9Wu5ZLRaMNrqbmJ5SYP_L8-2Xjf9-cqtrCQiiYcRsNkqcAAf-q6-gqNF5jjHBrcSxUtezHlpHkMv3jFXPJwXjW9RSnOvM6xI7K6v89uPSGcG2UfZ5oD0mzodaHr9riFUBwbTu9XXLzMlrZgCLUYZRopIL8ZgLQw3deJTFJ78nBXL9w68moPrp3Ugbjmeqz4zppLYOkWvgxjY349mJzIy5g88rv5puDh-o-7dAX9zwEIXSpSDnHfGxz-ahw1Gwu-eQKqYQkC9lOZYtnFHIv5IwjRTNVqLReMfgNhQS1ZdE6rgyTw4GzHbbM-dFE0lUxBounKBwQ5T51OSHLdt2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCpCKO6VKgz4CDcIg6OXyUdhBTn0TE9W-Jzo02L-0bfSo5Gg3QSlTZ3Pq_MgYkeBgAU_BJTF7LFOmErNbmYqcv8Ff5v3oKo9v-3iCtHm8Ww5QcxvSl5562wHOQmlDMxC0t_fALBGpQVBD8Y-LOXDiBFBI4-9Xs-iKA8oocBnRcLZOoUf7X608jyxtjjncDkFLbre8xrKNXlxWnDBFDEn0yGE4q_EdzzPphOvSgyl3jITrCg3pSUwBSCSIscCzkwvpBIX07C6keWLdgniXQn3j6LIeXL7FbB8qQwhq20PQqK1hj_MUEq7qBiELHRBHJ3gilw7FQwFh3lekZ-s5Mq_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix4Yi2Md7dwGQbHdkNtrhMHTyOb8xaRux_r2jGKBQJzwsYqfQSHIijnKi-HNV761Ejupj0oBlsAclr0SRR4r4b5FQbyYUeqyxaBAhy3nDM0dLn_vL4L7MOXNtF-wMvu9Ib-r_EoGG35rAAqalTzuFrZ6emsDaFSKJcIpufs2EerDCiTe5XBMGfCuXy7XJIAY6umbeh_n6GqVmLkiAtGjDIkZz7grvWIEDQVCnpOOuubfoX6b3GjNE5q6k8nZYDayqoH0w-CqVvwDnQ96qjOtXO1LqXKxWhgS5zkXXwJqpItZ647odtq9ROv2ve8pR7lHesoNeR-90KviVdv75xSRgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=AWvn-YDiJD70yHVmnMzvLCz_cv91xDXlSR7AslpbcqriVx8dLjrkSVaiMXAqMtkhqduINGfVBFR0vZIqNoBCzFjzEVbUoPz6gkzveN2ts06vXnHhCio_izX2imNNFOZ1pVVp8l111agPM6txo7Rz_PK43dv0uygqSF71lgL3SxZq-gwINhGbpScabKI18QpHD3k_1Jrty4XyPV-a1do50BHUTVpp9GWY5P8TAUIXsSBnnU9HkDTVwuP0AR9_Se-vnOcE2ElnBw-SoJuqHuWWYDtdbm6IsvjszqIM1K_v4I2d-CqjhIZZ8PqdZAlIdX_uamQW8KzyHIxVCxAtUfvT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=AWvn-YDiJD70yHVmnMzvLCz_cv91xDXlSR7AslpbcqriVx8dLjrkSVaiMXAqMtkhqduINGfVBFR0vZIqNoBCzFjzEVbUoPz6gkzveN2ts06vXnHhCio_izX2imNNFOZ1pVVp8l111agPM6txo7Rz_PK43dv0uygqSF71lgL3SxZq-gwINhGbpScabKI18QpHD3k_1Jrty4XyPV-a1do50BHUTVpp9GWY5P8TAUIXsSBnnU9HkDTVwuP0AR9_Se-vnOcE2ElnBw-SoJuqHuWWYDtdbm6IsvjszqIM1K_v4I2d-CqjhIZZ8PqdZAlIdX_uamQW8KzyHIxVCxAtUfvT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0NZ3LmdPr09FxvAyvRwJV_B1JyF2eOmUyimT-OAR45CIoBb2AAiEfIyBltwt_MOd9dzFRIq42E9Y6hK-jO_rAWKAIV4-RiwJsAavDgL629o0FtsKpSf2y0FxZDOfctp8BfQQgQPBXAhHGjMwMjNhcTfio7jP8QbLpNQX1RIn5ILo95CIuD9K67IyYdLioY4RfFz82nYEEZppbDNkvIuG3nVCcyYV95un8-Q0C-tERHwpCUE0qF0DWGq70G81FC1hjlFQsC7qyn0nbftt0-cxabDMacsWRMu_L1nDgiRrn5DfB_zdL6DqaflKfFDjc3caeKIP-1-eOVQPBugrJmrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=ntJaKqrS-ZTmAxK7bhrf6M2lPucm_OLQizfN3SH9vQGhRSqgxjXTfVUGd0XmDeYYFP6o9lughqN3mCt0E-XqbzZpdwTWSw6E-4mHQTMVwyVeKOItCJAx4dnzGb1ty42Y3p1r3ukVtCbL-Q5tcwIcw7SpdsXNSXmGDEEUNeLlenHqDrM81q_uKj9l7F-9xz-j8LQ5eRgizM5lKT3zGQgAjD9oRS_9c2ZMAk7vqdUNxXXCA2g6co1rPi52sARY7bd88lTKCPh06qgbDyWrqUugHtWWcZqjJUw89cEvj8c3JMZ1gqZCnn_WeVCpi0hKbSUnAYx60jCVwDkiNUzCZ9XM1Ucy0-W7yykGNjjEFoLUofcVGVRP7xfffJcv9JY5-zMnnXPQcWwFsxuxqliSrsZtPeiUr5syiUoUUmSVYKwxv2T942GxYMeE05aFxLHmNt1AefUM07mXKYrVwbI2dEL76uOVUMoSvQ6YoRQgHYf3EBVShoyxWAbKnDRBKcT9TfHRHGU6z4K3iydBp3l7isaTvQl5yp2o83u9bwl0YuhCY9IXWGlSYOrDkNVJ66-LbSpcV0wGP0nmwF0dTK0IlJ2_gpoF5jviMjfrADECMMhBZh6ZqXr7ZO6BV9lvruCG6XNlvGLFiDeV8qX597YT2dwepAxBlcAPIJNSxyUs3ekfONo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=ntJaKqrS-ZTmAxK7bhrf6M2lPucm_OLQizfN3SH9vQGhRSqgxjXTfVUGd0XmDeYYFP6o9lughqN3mCt0E-XqbzZpdwTWSw6E-4mHQTMVwyVeKOItCJAx4dnzGb1ty42Y3p1r3ukVtCbL-Q5tcwIcw7SpdsXNSXmGDEEUNeLlenHqDrM81q_uKj9l7F-9xz-j8LQ5eRgizM5lKT3zGQgAjD9oRS_9c2ZMAk7vqdUNxXXCA2g6co1rPi52sARY7bd88lTKCPh06qgbDyWrqUugHtWWcZqjJUw89cEvj8c3JMZ1gqZCnn_WeVCpi0hKbSUnAYx60jCVwDkiNUzCZ9XM1Ucy0-W7yykGNjjEFoLUofcVGVRP7xfffJcv9JY5-zMnnXPQcWwFsxuxqliSrsZtPeiUr5syiUoUUmSVYKwxv2T942GxYMeE05aFxLHmNt1AefUM07mXKYrVwbI2dEL76uOVUMoSvQ6YoRQgHYf3EBVShoyxWAbKnDRBKcT9TfHRHGU6z4K3iydBp3l7isaTvQl5yp2o83u9bwl0YuhCY9IXWGlSYOrDkNVJ66-LbSpcV0wGP0nmwF0dTK0IlJ2_gpoF5jviMjfrADECMMhBZh6ZqXr7ZO6BV9lvruCG6XNlvGLFiDeV8qX597YT2dwepAxBlcAPIJNSxyUs3ekfONo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhOrre54y8bZzCxrbNl84Y-OZeLdZjdxJqx2vHLEzap2WTuSUWCQ08ySndlhoGWtKg1oIY6FIAlnZod87-y-UfK0d61OLKnBOE_8_S9eYPO-JMmeqUrdrNkEFuKWH_xchh38nukxNyuhvDmmYpQ78IYGVtaNt8PvLRCt1SlRS5BD2_W9dcHUtDkD8dTrfF4k02ZabXuIxGWJK7IKulhWk0cMKy1j9_bHUxuR_HDBQYB_dmpE_KkmK7Y-wdkaGWlFEVD1k3D6KhZ94_xcg3U91B50wr0H7Jn4LYEvInpY2p5pJljeH0fmB4e_wAro6Te5HhbyRrRy_hWwfybKaRUlUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=UTC3Mvu94kY2QOH7ykOfVxrLhljWMT2qkBEJB86_NUwmZHmDTnwHoK4JL0k_zBJ94m0KI0Koe9eXXHGpzBx3M6yBICUsixX1uZz2w1574RdF6GFifhmxu81nXJ7Mr1CwMg5UXSalt1Xninxt6I64iDVgO7M4P-gY2iDNzuKBe_DJWWaTGDCGHOzgt_CG8goKo3g84SK_a-utBbNxl8AKmRXqj2xgEjwTY7DdpDWNhxmW_zsvjuGtyLtGV2D0U0AHCht6KysJTWt5mXCXZhv7bTDy1P_Kbvpsimu6tgGirUej4LfAShfddDiolieeaN57Xx8Ba3MjFpQNMS6Yl17cIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=UTC3Mvu94kY2QOH7ykOfVxrLhljWMT2qkBEJB86_NUwmZHmDTnwHoK4JL0k_zBJ94m0KI0Koe9eXXHGpzBx3M6yBICUsixX1uZz2w1574RdF6GFifhmxu81nXJ7Mr1CwMg5UXSalt1Xninxt6I64iDVgO7M4P-gY2iDNzuKBe_DJWWaTGDCGHOzgt_CG8goKo3g84SK_a-utBbNxl8AKmRXqj2xgEjwTY7DdpDWNhxmW_zsvjuGtyLtGV2D0U0AHCht6KysJTWt5mXCXZhv7bTDy1P_Kbvpsimu6tgGirUej4LfAShfddDiolieeaN57Xx8Ba3MjFpQNMS6Yl17cIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRFAOtRYPwI1TCgRxj3KLqYyjxpZMR_DZEDefWXltAZsczXGxNG4R4h9_2N187I3dji9KekPw0-KMfcPhEu5o9c3J0FIx3V4yQwMPt6z0HiK69we7kaMdwvZnTvgyHsQq2dmxgLZHVfFuWvQwrsg1dt2A3T19B8Xa9dGnVBpaDKi5Li78GlgDLk5IVAhBhjDSe-vXHC5o5a7yEWfNpinNAQXfHAL8BQ8wDcspTEliFveuH1B4Pw89EPVcJLGta_YkSR-0dBKbjiCRspA6VfC6_DWl_EXdGCLDMmI5eRTIlqy8p56JovIwoqccpn5ICHGJOspktitc917NtctqkvoKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=Qr2OULvQz0vGHF8y_j8iNykACf80-TlpTGxqW2BTA9fNwm7VRZW3I6qNcca8Z8oAl1DAPiVL5K0nibWmAFskB4Ds6X463BUyaYbLJTrisx-MXwfQyVYzTxtGcKmH580EV_-dQnBsCgYgJPjs3Sx4R0RbJSj43RrnA9fMq5F8NIKAPDMm4_uamvjZborJJqyJck7g6Ao9cAJTvedWsRiIE-9c0eo0wcPjVOM7BkhRAvBKPVMB60IHxdo7U_sWhoK6hRhl_8Nwdv8OSCFtNbUrjMsDcbw-BwoUSRCM7EFPinM4fPJXXHsyAR0mO4zjmXArIzaGgODB7xsQAj4FUwv8Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=Qr2OULvQz0vGHF8y_j8iNykACf80-TlpTGxqW2BTA9fNwm7VRZW3I6qNcca8Z8oAl1DAPiVL5K0nibWmAFskB4Ds6X463BUyaYbLJTrisx-MXwfQyVYzTxtGcKmH580EV_-dQnBsCgYgJPjs3Sx4R0RbJSj43RrnA9fMq5F8NIKAPDMm4_uamvjZborJJqyJck7g6Ao9cAJTvedWsRiIE-9c0eo0wcPjVOM7BkhRAvBKPVMB60IHxdo7U_sWhoK6hRhl_8Nwdv8OSCFtNbUrjMsDcbw-BwoUSRCM7EFPinM4fPJXXHsyAR0mO4zjmXArIzaGgODB7xsQAj4FUwv8Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFhiK00gzfbTADOWL5Ifm3dTN6y1n81ZMRIKSnsBNiFG4D3TzRzvGU_mOhsI6SWvN9U2udDJDDlgw_uXcNkwZSj8emp28_HcYZ9xStpqW_-N-1X0OKUFw6IQnQ_fHzjYf0nOCFyjgPSpo39-tWQ1-UaqYHWkrJeUsnJ25fhtdOF88dGcUByQKAzJJ51EujFO1gb8yu7fKktBBGKfyV9McrwRsb6t_6vsTzbpV-mckN1XebBLO-Y0wAYkD67Bvy_AGhRsURFaucqFoChWUDpA7LIlWxBBt5RR4lPlGl7s_3Vd-Fj2aFt6ootVKvosi3JKsBhHnBOTxlLttlcbZXkVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=JDPePDT0THxoz1gwyjLCwC8DHTxLIN-vk2UPrsP3H56QwMcLmofCNJWRjhdCmAPG44HgzTHkZaKWSMFX17rKbJXEdpBJdLspUSZGd9QoflbnRcyAZrx_rbmcZ8kfKj3wbeS64JM9Jf-3aapkpYHIdL-Xm9aTf-v8Aq_uDlmemv88dSFFZ2psLmEFvwFJPJE_iejLk9WpdPuhwztNjqnR4bl29kRVIputPeQW1W4H09RqfYZliFDZW1M5k9jes8-XQohRuPw_LnylBsIg--snyXkO5p-bfI43SICQDUV4eysJ4OzyzwTI6J0tcFSg9OuYktrenRsuj2ACiGoWY0NZsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=JDPePDT0THxoz1gwyjLCwC8DHTxLIN-vk2UPrsP3H56QwMcLmofCNJWRjhdCmAPG44HgzTHkZaKWSMFX17rKbJXEdpBJdLspUSZGd9QoflbnRcyAZrx_rbmcZ8kfKj3wbeS64JM9Jf-3aapkpYHIdL-Xm9aTf-v8Aq_uDlmemv88dSFFZ2psLmEFvwFJPJE_iejLk9WpdPuhwztNjqnR4bl29kRVIputPeQW1W4H09RqfYZliFDZW1M5k9jes8-XQohRuPw_LnylBsIg--snyXkO5p-bfI43SICQDUV4eysJ4OzyzwTI6J0tcFSg9OuYktrenRsuj2ACiGoWY0NZsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=eV8LEbDRD1fkUf8clpuPRiTC18ExjbIH_UWlywU_F-NK98v5dXRLEL7RQW4pDkjW5ieznhVrwCWsBcGNxnru1bZD8_Gg7U_TMX9OuOdEx_3ydVZ3Qfm16dXOAlECH6uxUG5GMKa4ZWTDaCy92_kY3GNTxIRk3jli0o0XVWm2eCRjdDzc56tOL-vrAuaUciTz6fR-6zmkv0VBqEaX-z-8glz9A_Bsmb5xi9hQppqbc2y58Uq1cvzbFcSXKYSHtOybJH8oCxu6LAWky9jpcmu3cTBeuH73EosM8XK-i_x3rdJZjWqzfGBCii_72X_CRGOcyiS9gZUvMdhfQiNyp8PT14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=eV8LEbDRD1fkUf8clpuPRiTC18ExjbIH_UWlywU_F-NK98v5dXRLEL7RQW4pDkjW5ieznhVrwCWsBcGNxnru1bZD8_Gg7U_TMX9OuOdEx_3ydVZ3Qfm16dXOAlECH6uxUG5GMKa4ZWTDaCy92_kY3GNTxIRk3jli0o0XVWm2eCRjdDzc56tOL-vrAuaUciTz6fR-6zmkv0VBqEaX-z-8glz9A_Bsmb5xi9hQppqbc2y58Uq1cvzbFcSXKYSHtOybJH8oCxu6LAWky9jpcmu3cTBeuH73EosM8XK-i_x3rdJZjWqzfGBCii_72X_CRGOcyiS9gZUvMdhfQiNyp8PT14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=tmw2JHyz48q6vM3LT0Xsaj4MVTYLKUnOdTiyS5QyJeW_wafePdHsaeGPcXbDcME-T7xqUNtwfcX5NIKUhD3kUt-lbWJ4g8zFdhrv2GYACKNZ-rK5K0oH0IbovEtZufQiF3q4ksbSMBIH48qOKszu-uJtK99la5z1pnUIoiay7aUJRnc2yEXeFlSquY90uif-Xm57bnnbVF4G89tc8_iOKIj7e1mgl9FxOdYLRZA6FWpynMqCnnU8fKoH1xi4j2YIQfp8L4BPSaPRY9LjsfJ8xcFI3c7wRs38Ig_T93odFMve9QWOek5_1-D-1fHBM_abBbD24JpDuHWz7hmDrlOh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=tmw2JHyz48q6vM3LT0Xsaj4MVTYLKUnOdTiyS5QyJeW_wafePdHsaeGPcXbDcME-T7xqUNtwfcX5NIKUhD3kUt-lbWJ4g8zFdhrv2GYACKNZ-rK5K0oH0IbovEtZufQiF3q4ksbSMBIH48qOKszu-uJtK99la5z1pnUIoiay7aUJRnc2yEXeFlSquY90uif-Xm57bnnbVF4G89tc8_iOKIj7e1mgl9FxOdYLRZA6FWpynMqCnnU8fKoH1xi4j2YIQfp8L4BPSaPRY9LjsfJ8xcFI3c7wRs38Ig_T93odFMve9QWOek5_1-D-1fHBM_abBbD24JpDuHWz7hmDrlOh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bt9zGbHgZA5P4r2WIWJRtO0pX-aMavqOGvtDAFrqBjBlgO7DnznSfMObVAZcUMVMhP9AN5TjLIARkDQ_Br3_EecMB6O1o3QkgJTdANxQFE9QiTq-ZhX2LkaTNlZ5iKViPDuFZspSflnbKcjHWldraTzq_K7pwzpSgVyFbswn7HLOoJuYufo0PMtxBReUjr3ETdLkODMN2X9DF-VevM2CBEZYW3OLmThgsQ-ig9i2NBE-DTtUPHdccw1EZXEezC0m3uZNezWQoI8dsQWYtWuZPKqe6oQ3VPhpiIpvljWh2lJU3S8fV4bvRg2KHofimcbVYxyN9_yipTxxJfhpSwvYFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU-djmBxkBAWYuST5DRg5B2WsHEbcYMcemRPZv_gH4AvnmZTlKSfBsMObGbUETnc-sfeMEiiE_iHylBzNrMYkUmSDSQ2tMhq4xvqahaNi4dBQrVAYcSh1vfRungXsj-aFCAhZLCZXOjXLjkIuneYpTeWd5obq2nG3nf-VHi2nKoXw4kPK8Hx78NBZnSegNWn1V8AliIOIpBCNZjK1q1Gu_DhhIUMSPg24JDaXTIT-gUBElNWl6GiAm7EAAECicK5hO_CKsEiVwmEHxvAI64mozbaVOgaNw6lM04_No3XP14iRzT-B3YOoNy204mUclnQPrGWrwkw687rUpK4cdEWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=RWkKols9E5-2LYlfESb00kgzNPqZUjQLdicU7ax6CYYzIqXuVnrTd9F36glXk_ORScmozphQ_ZOV_J_AFSNlC6jHlWiLlG6EgYZjI76GDCvTi_CeKpeBB6rmorTSRS3SV6hd-k-D9_NtXAV2gtbug42NTf5_wtzbD1Joh73Vj0Iikg1Eso8jNSp5ngONJfGXSuN9e1jxTLiqtGSHv6qJNzORDQOijIMqeKzxr2DBj33vlmlTblsX1EFbZIso-54Fq_FfnNYYdl_GLlfnCdq_f4SXy-f_Hy6RRbCOrYzphtdXn_Ef_rKiA8tbglmrXaApItJQPEo5oOA-p3WeIKeGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=RWkKols9E5-2LYlfESb00kgzNPqZUjQLdicU7ax6CYYzIqXuVnrTd9F36glXk_ORScmozphQ_ZOV_J_AFSNlC6jHlWiLlG6EgYZjI76GDCvTi_CeKpeBB6rmorTSRS3SV6hd-k-D9_NtXAV2gtbug42NTf5_wtzbD1Joh73Vj0Iikg1Eso8jNSp5ngONJfGXSuN9e1jxTLiqtGSHv6qJNzORDQOijIMqeKzxr2DBj33vlmlTblsX1EFbZIso-54Fq_FfnNYYdl_GLlfnCdq_f4SXy-f_Hy6RRbCOrYzphtdXn_Ef_rKiA8tbglmrXaApItJQPEo5oOA-p3WeIKeGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR_MUc7f-k2gNs9F0qok_IigJujZPbnbLHFtW_oaCcMc14OltrJ-sxjuWKGd32hZgP_L1atNLDtHRLO1XiLowpguMPLzyT2IWdEmQzXz5iTEq-y6pNbn0kBxtEyQEs9xtsLZDBUhSn3vzmECviSiCJTbMJdLn25kEThYkkLIgefSALaVoLd3FgdWJpxxb7cne0Q3kTrum3TL7ctjPwpXbqNL8NZQ2upCJoNhxpWYPLrLEhvOqcWVQqLDBNdlxGyNMqOAsWTZdTw1DLO0cxKH4OdDfjzoDoOXtF4EekfDVAmPjiTlWf6ub2pn5QpyOrzbXUHfgGp-0BOwCuck0K_Pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSbBF8ftRQO_ck1faIK2jviDztsN7pZ_99ViFhDEy-EeG1--tHsYX5Xs8tuqHLf06MLUSRtsousadkya0x9R7lhjT9lJ_f96Up1YY9psxGI2tCZecevg3wF6MkNR7TjsoeTO6xkzRIxKQ4o3OHoxg5xWXXCenSLTPQ0O9JcpPw1RMme_L0BUfawMvyXMZ2YO_ljlgmp4XoaZouUawDrbD7YklxghMatbIMGecbi_0iH7e7FxItB2oU2pYRVXAcN2rhMVWhTxJAEL7PV08PHxg3yTUevMSU5FCkV4kq0QoNxScz224SCfwcM_3sdPPyGasx0nQJ25O78DfCx0I0HiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0pYn5fCDwYt3pubpfymxh6ulVsP8RmqUKCCXqPmLImvtaOpXd1t3jv1OYEyFN7z6tp96Oh_ESSCXDAE7FWpiAUzhJbRA1H0KKdzg3j5BDSX6cfDSSovwPkET1MCa0suNOimpFJVw-rtPj2ibSJ86dSCGE53kydg2BZ-g636591XhbNe8NpzaJUO5NnvXWYtouqrKgltkA0f68lS9FM3d2C557vCrYFXZ--Qnv0ditlI-IfSA-T_ztAC2pUFu4aOZtBNiyWVpdrEwP4eJAaDfjNyFqmu5RoU7heu3aCfnBwqx1LEcaUzYIhsBOh26b5cF6z7DuxCIfvy7NVRP6cwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=Rxdqbra8mkmG458VHBL50P2Q0p_iqr2FuO8t348p2EFvD61SDIpiu4wVPl-Eu6I66gyPMrW4FWOa1UK6g26mgWdNP-7cHndI3AC3IsmjEJhVERJAWhahAF_O5rkDSGpKnL6r5qA6zoGpBclEYCPRY94Cjw5b2scN5KIZD0CIONdRewvzYJEBp6CSEXiEh53VWTAvoK7DdOl-oD1noCuHaOZ3_SHRW4Ej7XGtiXBGehYdJxwHECeNaSHAZob4PowaIVd7auAQsxDDdQz4cbVy1ktyl2fcxeNvixoV-8hbAhL8E3E_y5MYh62TmVuDV9J6ICh88rfCo5CagSd1Nxw55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=Rxdqbra8mkmG458VHBL50P2Q0p_iqr2FuO8t348p2EFvD61SDIpiu4wVPl-Eu6I66gyPMrW4FWOa1UK6g26mgWdNP-7cHndI3AC3IsmjEJhVERJAWhahAF_O5rkDSGpKnL6r5qA6zoGpBclEYCPRY94Cjw5b2scN5KIZD0CIONdRewvzYJEBp6CSEXiEh53VWTAvoK7DdOl-oD1noCuHaOZ3_SHRW4Ej7XGtiXBGehYdJxwHECeNaSHAZob4PowaIVd7auAQsxDDdQz4cbVy1ktyl2fcxeNvixoV-8hbAhL8E3E_y5MYh62TmVuDV9J6ICh88rfCo5CagSd1Nxw55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
