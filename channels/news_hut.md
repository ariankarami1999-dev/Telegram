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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEZ82PqCAF4RNKh18RXaVEZeGKnZ2U4ccFZX_K-79RwlZ5yKolNZJef3zpqbcS_m1af6TLmAJ8qbkDUYIRcqtBw3Ft50LFGl9YDO7V2TrxrtjaEIKrnknWep3CGEKMyyBRk-Ln3xlxBi0lcyw19_6lf1DWA1v_4Zv-yOEyBPsSHxLvs8LfyaEaBtFQWZOFCvdMXnE63MWeZ2pd2_TGAmhFnoeE7vIozFoZChRywdh1sA0Jr2PPu_S2MiNdxC-WRitQtfnW5VP8A3h9R4gh8kdf6FZrNJ-32JVGHoh3adj4nrdkT-rJCrxD-t_LK4M43IqrBdrEDDJk4kea4xM7d8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1iLxnnGDs6ZsKIbz_j_9RNFnuCt4XLZpfguYvHGiZ248i6qZU_0BonnNqQbMeUiBJYsqpgO5bIzZvTVCnBwlMxXPn_56ogkq2-b8HEvbc0kpOhNsxFtKNohShV5NnRbjVShJASEWE2CnlhldfWBQN26M4AF64mHVaj3dXdz1mXsBkeHwS8bh1GrFMAwiGeFROGSnEarMW_IWTkwcD7Jtkz3gUzSjXiCeVkF-btcXVHZyHgP3DTly7N6lsebQdQcZzLCSm1MCyfkRSBfrN6uiHDrDhXD_GESD2meq8ewDYwBpBHuRmvXprakjsOZVuqQORGLFCrbqlbzAtm9Ldkmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjdeN14fwjDb6eEGr81w6EGWot7j23Gv_YQmyPczkZxBIH_qfUfYMvUcsx9tjNFvBBAyi49zsenmSeB7kbuwXK7ZdgRT0WRHxuayFCZq5au0cUN9mS8MiWB7VCovVjZO0Jxmh-dMy1KJt6SIrrkyVEpPoeXMKSifprY5oGcW8FF9wX_uOpM5VhoVMp-Th1YRNG3TyXrDVLJm09FNM0_sEvA_EBqVVQQFrPpl8DlpIKH6KtB3uww1jD4udFzld7k1xBY1h0YPpbAwoskVSO3qxQSaRKdm2CUGPCXl53pAd6-jois6ANMU0Xnl62Vhq3e59CqlUqF79bfHsaKF_ZA4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc8g60cNstDi266vpwQIs-zpvycOHkJnuqfraTy5GD3L_tcta87rdZ-E4m9lC4RdIM8JjMa4RDhTKAl8rzkW0PpWB9sJPvwdCdLzEk8UW1vw0KMcFhzD8IeBhPsIBHn9CSLD86Haue081hCB5td-C8IcPiwP3RLHA2VcLHqAv7zqyxKgaV2-FhlGXbrk6d55FmJpYrbDUL00UPcQeUkDp400JDb_pGA_nMPUmgfdqFAiR2sV1O95Q_XfqFhQekeVFMXeD4ueBUKolNEGYuBX7bfvmN2mqwMYWY1NT0vSbTWKEjAkk9A0SfQcmFdGYTabnlDDjvkI527e65JxAgyrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=fJOb26RoBhktuLu3Bj1g5dcl2ECWMLI96jdid47-9SJP9lkIwxY0np1q8YT2KSO1rzeOiEJEE17bFdJJOYyJS-kcUWIUUID8zZpvtXyliEo4nQfP8XOvbvpY2wyYd4uoroq7ChKRAFehCPw6qSI8jqIIdlJsy2opsbE9QxfgMHPguNMDhOX7cbusBXtNWoxOwO4k-MwL3X7_xWvIxo8pwD2UTRlqJ1Wl7V_pTbOjEiBOGbK2sG9rrB5RFo_p_bxjqO2ElSIYCeb45jtSuR9Ot64C-79wbPjNA7vnsJunV6VX4kzt8wht6FcqgR_NyAO0t4BIX9IWMeiiuLIJygD0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=fJOb26RoBhktuLu3Bj1g5dcl2ECWMLI96jdid47-9SJP9lkIwxY0np1q8YT2KSO1rzeOiEJEE17bFdJJOYyJS-kcUWIUUID8zZpvtXyliEo4nQfP8XOvbvpY2wyYd4uoroq7ChKRAFehCPw6qSI8jqIIdlJsy2opsbE9QxfgMHPguNMDhOX7cbusBXtNWoxOwO4k-MwL3X7_xWvIxo8pwD2UTRlqJ1Wl7V_pTbOjEiBOGbK2sG9rrB5RFo_p_bxjqO2ElSIYCeb45jtSuR9Ot64C-79wbPjNA7vnsJunV6VX4kzt8wht6FcqgR_NyAO0t4BIX9IWMeiiuLIJygD0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Pb_FbDInPK2NMiOIu4-g8XiPHl6dQTrnZMCzvMXTVl4db9260D8Yj6HKvO19m7Cb9x6R-_mVnQCuj5obbg5SWp6b5mX8a4h1AG5HmHfc3qu00XPItLBBkLLXtiMUpyYUHgZeOrJUjKUB1iFGzCYoPN9QDc4M-IUFipY4wenFlYVsmGlSz8sDNYsuIc8egtp_C-n6-lC3gO4xrWoPipc4Wf8IzMfz7gvf6EornDFGidWaIooc1qkjTkffrPobYsSZrEi21aCI_120kQKQd5hykqAnhWLglai9l7T2rLQ9B7BSdt6Er9Vp7qH3_2UpuKsc8GDf8ADJcf1yE50S8HDPPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Pb_FbDInPK2NMiOIu4-g8XiPHl6dQTrnZMCzvMXTVl4db9260D8Yj6HKvO19m7Cb9x6R-_mVnQCuj5obbg5SWp6b5mX8a4h1AG5HmHfc3qu00XPItLBBkLLXtiMUpyYUHgZeOrJUjKUB1iFGzCYoPN9QDc4M-IUFipY4wenFlYVsmGlSz8sDNYsuIc8egtp_C-n6-lC3gO4xrWoPipc4Wf8IzMfz7gvf6EornDFGidWaIooc1qkjTkffrPobYsSZrEi21aCI_120kQKQd5hykqAnhWLglai9l7T2rLQ9B7BSdt6Er9Vp7qH3_2UpuKsc8GDf8ADJcf1yE50S8HDPPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk96nmqqUQmfkW_suNk9XCAwaL0NR75UIjeAUr0JqI_fa04QMg9SgSrx3au0p0t3zdfrPWA3qlQwzfPv6CPSL6ilepEgJm322ZNauLiwyOTB5rpZkfClx5U4Eo3M5m0SC2oJt2kt9A-IhI1tl9AyIZZRP1fTx3Qn0RIomPkS_nL3gHdUqyGRU-0q6wCD_bZfbzKg-YrFuYF_xi7KChPvlo69VboHOc2rjzrOtupiBF8eBqp4O3tzcrmlVMV14ZofK0TXDabeIPhmLxJXWRIRYSZ7o3Ss9ckvAL9zwJqIPhHCjb4Z5bpa-5cERYNlxjtf-Gv_j5DFHOl5rSk8EXdDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=mbAVqpiR1eJczRCNtWp0UtMFDASQK1OUoTEaoy3kTKmAGFYu7Po-E-zSHSYNBuvdVSsd6kkHmx-em8R-sbAfrZe5yLkYDo8dlnJjYijQK-k8m-_1e9yYqVsS51RztRxvemHxNDCs8niD4LxZHXPqAWIfjq2s_rNrWatWRk3QWwVegfs32UutJ-U54N29lF0VFAyw52XB-nLZtFvzrxsL_7VTZsEqkDWjPBmxLUQWssde9ckKY4UqrT6stjJ6Z-aWQYnZx54tOQSN2hVtN78Og4_s1XedqTvPzB_K5eEhqs-qQc9sKu5o_XQeLeFAnmp8PT-rS0tgGPKUZNRejUJ4jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=mbAVqpiR1eJczRCNtWp0UtMFDASQK1OUoTEaoy3kTKmAGFYu7Po-E-zSHSYNBuvdVSsd6kkHmx-em8R-sbAfrZe5yLkYDo8dlnJjYijQK-k8m-_1e9yYqVsS51RztRxvemHxNDCs8niD4LxZHXPqAWIfjq2s_rNrWatWRk3QWwVegfs32UutJ-U54N29lF0VFAyw52XB-nLZtFvzrxsL_7VTZsEqkDWjPBmxLUQWssde9ckKY4UqrT6stjJ6Z-aWQYnZx54tOQSN2hVtN78Og4_s1XedqTvPzB_K5eEhqs-qQc9sKu5o_XQeLeFAnmp8PT-rS0tgGPKUZNRejUJ4jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaiIYQijD5R1Ic2YiTuR6ID98p_2hecvEh7eun6mFWJxcsoIuLy9tilRPvzfpnjKuVqvhJYWgjRSIYMifcOxqqvQxBGYswEVsH1L6oE0lo5zfS8RHv8jmHXFLM_HQN3tMTZaZPEGmkNkMTEccEMpyDVS95wnqajNF_TQtpT4NNs04yg3qT-kqyKKWTgo10VVOB1oGm7ul6nvlD4ku_OT8AJu3adoDnSUSP2-brrGO5H4Q-bMxvRqivFn3KNH7NcYC1_Xtjd3S5fnkTiGQUWT8VYJUqNNER2aau8RyLnl9PDsg-pqTl7OWUlVzAvy7kf0gXknUZjYJEFsv1f7T0-BbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=ini9kg4UuoepSgom8QU-p5sbxVq4Nbew84CHnOcU5oEyKVPVgGFcsFN1EcOXd_v_4TCfpsvDBrwexYNQYhJtIUDRHhySBodIxtNRwoTmIUnk-NRsXB57FnpeWwOCR5-L2sG3JOkR5JYkGLEP7mzmtXIs6ejxhf3EH9PNpuJE4NbpXYLCtrw7HbH3Lf44HWShagxbqjKd-Xo9bHrdr05a3Ww9HZlcefgtacUjGn7uBc6idro-Sv15bAVBiOGyThb3U777wateDmkKa9CMDQkmIZBJHtfh4CIuFeRLIGu5vPOjPbOk-qotY_ldsqvh6Rw3AzAm2rVWpYIZ6LWj-UJ8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=ini9kg4UuoepSgom8QU-p5sbxVq4Nbew84CHnOcU5oEyKVPVgGFcsFN1EcOXd_v_4TCfpsvDBrwexYNQYhJtIUDRHhySBodIxtNRwoTmIUnk-NRsXB57FnpeWwOCR5-L2sG3JOkR5JYkGLEP7mzmtXIs6ejxhf3EH9PNpuJE4NbpXYLCtrw7HbH3Lf44HWShagxbqjKd-Xo9bHrdr05a3Ww9HZlcefgtacUjGn7uBc6idro-Sv15bAVBiOGyThb3U777wateDmkKa9CMDQkmIZBJHtfh4CIuFeRLIGu5vPOjPbOk-qotY_ldsqvh6Rw3AzAm2rVWpYIZ6LWj-UJ8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO6eW8txIRnadEw5sLat4uHiBBzB9PUfRdRJ4Fon3GR-G99FPrivoww-T9XH-6O8Nzrrdb4AE0C6nYFxjEs7kx08BWV_9EbD0U9h-FlcU0ig1jSuqaOUhGz-dznOS0YqdLJvp1ir-AqEPsPmkePeyAjaP4wYVq3x27fSN2ENX8KcZ-dctR6hmWAKNxAOO9F5Ac6PW_DB3mSOhNwaSRaX2vIWtZks5spBKoPcLeykFWPEqyO72FA8yD7_WuobDuEaCD92UNcy_Hto7dyCmO_IpJj0zbKqsqY1Qnu0ORbTbH2HKCI2Asvgxz06O6KQOQ6Ze8NgWQeT2LmcIfMs3J-BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=n4l-p831OLYYOhoNg7UONXd7kVTDlz2TAwQ_fo_Rrld0EnhIR4MUpvGoxjd91uYs2Rsm8ybAk5hKWgPRsEieOfLDDQbtMFQsfhgwbd7Z3OnMhUAy0ruq_kKezMzKTPyKDa8x16iQhVQTaPVqA77ajSzS27bpJxhFcyN-GVNazbCuqRGvFgPrqHzL-7lSsoKKrQMe0olU4s7MjUgJQh_2mHDUfwck_-G8tuhov5xcfEf-wEmMFHx-Tj7jkvnx_juKqwhTWhAgSVXykJHjpwBj5ZJaZs7m6PR3Clr7fr_gY9zBYU811k5WcqhOoP01CYNWJlZerC4rrLKheBZzgST_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=n4l-p831OLYYOhoNg7UONXd7kVTDlz2TAwQ_fo_Rrld0EnhIR4MUpvGoxjd91uYs2Rsm8ybAk5hKWgPRsEieOfLDDQbtMFQsfhgwbd7Z3OnMhUAy0ruq_kKezMzKTPyKDa8x16iQhVQTaPVqA77ajSzS27bpJxhFcyN-GVNazbCuqRGvFgPrqHzL-7lSsoKKrQMe0olU4s7MjUgJQh_2mHDUfwck_-G8tuhov5xcfEf-wEmMFHx-Tj7jkvnx_juKqwhTWhAgSVXykJHjpwBj5ZJaZs7m6PR3Clr7fr_gY9zBYU811k5WcqhOoP01CYNWJlZerC4rrLKheBZzgST_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=EcBbo7oTftevatSsr1_pUIPAZN9kq98Cx6kG_nMaR1ApDpVCj8M6IiFdaC38j9XSzV0b501RSvoX1PTFjnPppV1-gqMiPY4TA11RrfzyP5Icxp_ijePi3okobgUtsjLJ9xRd29Kh1U2g0Fg5j8BzsDc7itqksekCLxI31Cl3LlrNl5_yCfM2z9qbcdngPJLt9vvHSE0kAaIinwyM6pOMYW6AXI41D9f6j94RplaMjua59nW_ihDYBDPoPoLSCxRbsmiM2wPAQg2gMyrTjJ68fh7m91K40QoPjl46gc3yypYKaM_G07TMLdoBxyfpEFxWFH8SBTh9zXzqDUubff2TcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=EcBbo7oTftevatSsr1_pUIPAZN9kq98Cx6kG_nMaR1ApDpVCj8M6IiFdaC38j9XSzV0b501RSvoX1PTFjnPppV1-gqMiPY4TA11RrfzyP5Icxp_ijePi3okobgUtsjLJ9xRd29Kh1U2g0Fg5j8BzsDc7itqksekCLxI31Cl3LlrNl5_yCfM2z9qbcdngPJLt9vvHSE0kAaIinwyM6pOMYW6AXI41D9f6j94RplaMjua59nW_ihDYBDPoPoLSCxRbsmiM2wPAQg2gMyrTjJ68fh7m91K40QoPjl46gc3yypYKaM_G07TMLdoBxyfpEFxWFH8SBTh9zXzqDUubff2TcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__Im-v6AWykWtRGEnFOjU7I2MlYvlbgFh1ECWlFhEQ7mFOnC33V8E-P3CTX5e0AjJ4gv6kDMdc5mkIy_H4o1GhLDhfpMogSPWNVfIuw9f5iACrhojYDm0c4GkXo7fWNv11X7jv9XKlCUntLoU-nr8WlcRf7h74v38mfWV7ItFzUwNSd-mtLO9T5tWEblBLmCLyYYg1uSKWp7zzDP_voexIGmcM-0xi8qnXp7hvkQtWFJjYWZxSLun9_3mosxti8LcW4nz6JwLFNnGyYIspWp6MdRlY6WvkXB_HkaloqSf7jAUBvkUKAE9LxhUoC8Js91q9IYcXRv2cj2-RU3dM7tSsME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__Im-v6AWykWtRGEnFOjU7I2MlYvlbgFh1ECWlFhEQ7mFOnC33V8E-P3CTX5e0AjJ4gv6kDMdc5mkIy_H4o1GhLDhfpMogSPWNVfIuw9f5iACrhojYDm0c4GkXo7fWNv11X7jv9XKlCUntLoU-nr8WlcRf7h74v38mfWV7ItFzUwNSd-mtLO9T5tWEblBLmCLyYYg1uSKWp7zzDP_voexIGmcM-0xi8qnXp7hvkQtWFJjYWZxSLun9_3mosxti8LcW4nz6JwLFNnGyYIspWp6MdRlY6WvkXB_HkaloqSf7jAUBvkUKAE9LxhUoC8Js91q9IYcXRv2cj2-RU3dM7tSsME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx6cTciypAjpT8P_gfLoO9fMjwLe0vjhKi7ILFY8_VdYFwrqYec4dfeY2Elv3AIb-68t_epwEBinPj2LFhw5XIqlYW2qt8sc5vY8P2fBKHk8tFe2YPhl0-hyGdsTNcC9Hz5clZEGigOAig57UjcvSnd88800GdXdaX8A_13nx-w-8emMSX77CZ2yFsIeys533CQgnqffwKI4csisebNDOU_P5-fnPTGnY-CKce43dUabLEUEPvRajdxd7_UlCmSRuHoRcuNiCc3zALle1kwRGz7AY07fkqc9Qe_HmaRy1o_XQPEx8x6t9MITYn4JLJzD8_DPIhQ1pZ3sOsa9OrnJpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4dNJHfUmp9EAMfnBh1KdB06GWonu5T34Ul-1kqGJe7MgzpmaNmJZgzas9dewE7keR4Y5ncNfsx97kit99DKZCfaGCvwQLuOm9NK_ru47vUIB1H_xBL8Inm2C1M0-gEPU3Oj1wmjDSvqh3Fy1fUyb2HTHtB5ZCpdbOJrxTl6EgzoYkpDarFYd0vZlWxH565br0mg_nyLPwtiKa1XyAU8Sb2eCvX30WdR_h5p4fEkOuUJGgXULT0FafyN0wAIV8YVrUkBGHDAz-JmFOuuzL6R-CxDMtYXcFT872FrFBAE_x3J0XPmYseNvk0PLjladd_6sAH-5lXIuaQi40yNqaJX2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=URFy2IKvI7JWc5e6_DyRBmSz7vHrsnA2NzU5rvxgcQunJa1W38XWWvYrJXJX-escWOcLrxXirhxzIgey0bDQqK9oV-OqbaI0wQuLVAGUu3jLqnm3mWlo028j71_1yY4vDiqYkiMPiiKyoqb2p3c1eebjD5F6kvhmSyDKQw5eWrKsQ6cLai-pSDaE6lN9ddWotB5to_KE0v6cc5y140v4aguZAvmVTBQybS2c3kZ-Abh-LgTUsBqIO4H-s4aWU9siq7WSCr2WGBIecbonx3y1C4mjHFl5783y6329Z9qujv3OSLoPSxuc7Zgt8k-TDKhupzuE8Brv0-9a946ykqD6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=URFy2IKvI7JWc5e6_DyRBmSz7vHrsnA2NzU5rvxgcQunJa1W38XWWvYrJXJX-escWOcLrxXirhxzIgey0bDQqK9oV-OqbaI0wQuLVAGUu3jLqnm3mWlo028j71_1yY4vDiqYkiMPiiKyoqb2p3c1eebjD5F6kvhmSyDKQw5eWrKsQ6cLai-pSDaE6lN9ddWotB5to_KE0v6cc5y140v4aguZAvmVTBQybS2c3kZ-Abh-LgTUsBqIO4H-s4aWU9siq7WSCr2WGBIecbonx3y1C4mjHFl5783y6329Z9qujv3OSLoPSxuc7Zgt8k-TDKhupzuE8Brv0-9a946ykqD6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxUGuluNYwLzklV7IyTFQRsd_5xZzlQC7Wr69yKcePseEQPczTl9lJRBeSwrm_feOhMGJXT4Q6Y0vqucX6w-ZUHtUXupSs2nX_bvmEZtQnNWJcvr2dR56vvhY0xH8UVcmnzV2_rvc4e9tOQoC2dr_ymF8VCdl34dDTt6_94m2SkP5DogwkfT5Y7Wh-YXJ55GwKONRWv6ihLJI5aGxA1rH4O-a2BY_716bHyYHcD9lI47za7eQkLoCFvdL6vXWkf5zmckDKP_NWY45do4630uFwaiGn8CEXlya7buScYiLtx1JXoMG1bvrA02T97C7zshKaJO_G0ABH7xoWVJlmnw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3RnvurabCeKBC8KduTC20a_YUZwcLb7cP3rQJ95hMSpLzRmIhSd0Lyj3l-9wHtE73JGMRDuUn1qlM8UrpfA8EbcYABS8HIxslZ7T8oKEDTJ63ePTJbsaVZ9rcmq9cowV_pA6yJF9ndV9eYew627MDcm6xMso_gUqhUBq4CNtPBwfSAdEjk1TgkeBUnHrA6xRoT54RgDIl-Ua4ryleToX7xUbly3PoYCJvkxXtKOotzVb42ORXlVs6FHDpu8K56LNw7esB2f2T0OTPl3wQs1I2c4JJx-ZoIVMjsByPOfbX_7Oj6uSL5piKLQEaO6kwNOLuQmU05Af4ATDMzXJWiSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=LWtWWbDepS1Lpw3KnKJqIv2z9lztH0TO4CH8iiBYpfNPsW549mT6UsKnFDbexP5wMXCeodJvpQhcZsLqQPg1u5MtdtqBCzXKnuvjkxDBSykfFvnRcKaam5Uke0-mRa6PttA_UhNPcR1M2WCh9qJZXMZKRrUbAJIhZKcY0xA7xgNVtuMvU2Tq4LdFL0hT1ExMNDWLREEX8_KNY8rO1WWeKva4TQX1dbqH26P_vS4HqfmjLLjTGQnvmAq9ZSnhtlDYoUYDvTq_1jBbmNOIu3FBrVa5Q74s2a8IxdcaVBN2EDfl3RBQkyzBw_hxqle4BuNsY7CEoImLr5TaH3Fd1un9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=LWtWWbDepS1Lpw3KnKJqIv2z9lztH0TO4CH8iiBYpfNPsW549mT6UsKnFDbexP5wMXCeodJvpQhcZsLqQPg1u5MtdtqBCzXKnuvjkxDBSykfFvnRcKaam5Uke0-mRa6PttA_UhNPcR1M2WCh9qJZXMZKRrUbAJIhZKcY0xA7xgNVtuMvU2Tq4LdFL0hT1ExMNDWLREEX8_KNY8rO1WWeKva4TQX1dbqH26P_vS4HqfmjLLjTGQnvmAq9ZSnhtlDYoUYDvTq_1jBbmNOIu3FBrVa5Q74s2a8IxdcaVBN2EDfl3RBQkyzBw_hxqle4BuNsY7CEoImLr5TaH3Fd1un9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Z_ki3L3XB0gtmgMfgHQcPHICzCFYXYQyDDbM_KT4lRK2i_aCMF5DwH0Qe0Most7e3yU3zYvIWH5YprZHyx3wF4WSMkYG5ddn1ClHFwZkCWLAkdJuI8MweCXu3Myef0cQAqPDitz2OYuoO_RMfe2a_UdIm9ALNZjA_AH6hAxmZ0X5DQw3RJ1c_fRW_TV9Kak02owFVl5c_ApLK6rrKuu-GQaKopYugCqbV2LxbHIN0qE4I-bzGbnENNXLytXhQjiU1mgT-IbWArhbS2SPT7UI6PyBbCGL2mhT7i5PvVPSpcI0oAjPztqlAdIcGWTaga_eks0AEZx2D0Ga8S1CBjyCww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Z_ki3L3XB0gtmgMfgHQcPHICzCFYXYQyDDbM_KT4lRK2i_aCMF5DwH0Qe0Most7e3yU3zYvIWH5YprZHyx3wF4WSMkYG5ddn1ClHFwZkCWLAkdJuI8MweCXu3Myef0cQAqPDitz2OYuoO_RMfe2a_UdIm9ALNZjA_AH6hAxmZ0X5DQw3RJ1c_fRW_TV9Kak02owFVl5c_ApLK6rrKuu-GQaKopYugCqbV2LxbHIN0qE4I-bzGbnENNXLytXhQjiU1mgT-IbWArhbS2SPT7UI6PyBbCGL2mhT7i5PvVPSpcI0oAjPztqlAdIcGWTaga_eks0AEZx2D0Ga8S1CBjyCww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyQCyBmv1-QPPZjZMnS4_sKzD_H9hRWCAY1vHmPCBuhJ8IlZvG8FN_87LCKBQF800hF0eKszHQ7h6aggVNb7f1_cSxCM2j7I5bOJuk0Bya9DN9O2tFgo12pd4yjMP3Coj3yXCBzq86uFRLE0HYjUnZzV-svRnJnX7FSDbdRWM8xMMTQ0ja2kx9JLW385vBG3VoDrPqij3Y7rB1R34LgwtCEtWohVKkLd1g88lP5GyZ2k_aMNk01HvIO4SQvCurwqLEVSESXzCZkuZsfq2Ativ9Rw3IG2--elvemycaRk-WDklJ2GSGfU5p50xhYWAxqpSvVAIP4SovpTvPrGFwa5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsUvxNn4Itb7XeqMs4CowE_zzgKPMRII6BSg9Eeft0mEKPZo2sxGSgJVWgTJqvSCAOZ7VkRSlMZD3KRT6UrKNt_fQpXFIqMtCBmksra2B5iKfds9N_B56glEumU7dcWOSycnIJJAgXsGd1uqL80UbufjZP6QNkPofNJ785os8ox85dUC3MhITwWx0t-3VKPmllnS36qjYzBcvi34xLxbBGRK0z39nzNYl0lopqM39HTTDfxJujtbZ3GLxf77sOQAEL6cuBFZYfqvy_8sZ-j_PlyV8dBo7EUrVv-Yd9BbmcaNu-250ENZ6ZXWmZAMzE36Kp3pHo7YAJg4541e8ww5Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=j4QzlkuMoMuBD65AFiiMIqvZqOjY_G6D0ikOkg_1fCCqQegBv1-JGzzaZLGoqO2wv0DhY7WnC5MbJpUwWGCiIJErvvFzb2fjHDdw3CWIa9vxFpGUkQ70KBNx9rlLSwOOLrLbrVtKDZDXN5Yi9vJSXRCcrewxf8cIdf44nXnP2xPP29kMFZriTRzgvxSTfrge_w8eifhkRjLv1XEthzHOFBAwkZ-KDiTbqYIAgj9NS8C9qAkeetmXlbZZY6awcE5NL-eQikhoDVjEFyQxcFDEbbKslzrWOTXJipN_XUGZi9T77h8pfYD0XHUV1hsD5HmQgH1Vsiqd4_Fh7ss8o5Cfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=j4QzlkuMoMuBD65AFiiMIqvZqOjY_G6D0ikOkg_1fCCqQegBv1-JGzzaZLGoqO2wv0DhY7WnC5MbJpUwWGCiIJErvvFzb2fjHDdw3CWIa9vxFpGUkQ70KBNx9rlLSwOOLrLbrVtKDZDXN5Yi9vJSXRCcrewxf8cIdf44nXnP2xPP29kMFZriTRzgvxSTfrge_w8eifhkRjLv1XEthzHOFBAwkZ-KDiTbqYIAgj9NS8C9qAkeetmXlbZZY6awcE5NL-eQikhoDVjEFyQxcFDEbbKslzrWOTXJipN_XUGZi9T77h8pfYD0XHUV1hsD5HmQgH1Vsiqd4_Fh7ss8o5Cfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxTrJhxM5tTODRPgwCrO7ERIiJ3XH42ZHcjUsYnOt-yiB-NhXb7d1Wrg1DhVDaIWQ1G21o4MJ_tET1BZP1tG6h8pqWme8Yx-29Rij5Uosgj_PXGKh8xtbt-CsbGH7kMqR9LWd8G4voLVHwVFTAGTxReKcZweBdz66ePWU5Zf-s_hhnAOTYnUjkDvSXqM4GTAsVcJMSE4aJhLJo2R84NJH-9BDAtFjbTQp8oaX-i_zkSNhfyc-RSjMnHf_EOW1GR8FKa9IT4D00CniKJHyXwpPhyqvvwt2OTx15uDzh6AdgH6xPakWNYV1hUmxONp4C4ZZvmPAhItLL8sALsUxoeNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlN0jDuT4kUV0bV839HzCk6Uqy_NGkXiqYLy4AQmc98bbwZsxzJfScZspRB2mTSv77cuUJS-TSACNCoVsC16VAb1yIZ3Lm1jrlTGBQPs-STcDirWEMaQD5uf20x3T-4bJSwxAPNe-Q6KzAtP1p3EVJiNeqRcoqJ9dTdB7SRpCB8M-MGAPkfmiuiqBRPQRhuzm4fXpSfGT1aaqFSiplEw7WpkuDKRs3Gj4__cKiw3dK3wmtHTF-Sdm3pc9IaVUcKdj0nViJP01EtGnEmmYixtLZYk4M9P06Y-WMyqUDK-yAI9KBANvUoLwr7KrGcnYsSV-Xtk9k7nVF_nIpQjlLLofg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHomYSfv_nBOIo4HgAMxMyb5DsHOKhQDhmrVpIZjTmm50F1HapVjT5XMYNN_k-vcmFEp0bnjH44CpMvGGAEnF7wD9K6iBt_QlIeD2Mmw91Vt5834KjtSqFnKMU1bPBT3AfrhXiuXZI11sfEpmnyKTRbjwmqG6cNyXw-1kJBhn8DXyryI-GLmCa1sJPnKjeplQqxX-5xUE7xAtfS4KlIu1u2geUX7Bsq5OEGmm28J1HjNJXP2K_9JGQm3NBBREVZ7R3qaOc7u6mosGCq9wkwSy8xsImqOBIi__wCcCf4DHF7UES9fZLw6BKZFqDDhdkfuZqa5-V02fRov2jgIfcigUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=uE2y8MD2NvS_ZrC66bkx3Ds8pkr40eZSgwFkFH3IQkCZXFLZACmSXUsCVWey3wbOLGIKXnM4AoKZWL22q_dIkCrXqpWsJM2t3ebbsUkYfILm8TSahtBIsPF7Nfz4UgI4wVcXquKxlHptWkcal6gXM9JhfASxvhlR1GkkAVk6sskrUe7Z4Gaw7swZZO1gkbg2N49PxtupJKQ1AnJeGSHbQK4WAeUhgpoedTD6KTrWvs74UlNRPh14nNAt9ZaPgmqk8kHtGgOME7F4v8KcrfaULn9J_zAdFOgN40RP51m1Tg9lCuuQib70qNy2LkCZkxzAHgPzI5rx0Zrj8KpN85ckZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=uE2y8MD2NvS_ZrC66bkx3Ds8pkr40eZSgwFkFH3IQkCZXFLZACmSXUsCVWey3wbOLGIKXnM4AoKZWL22q_dIkCrXqpWsJM2t3ebbsUkYfILm8TSahtBIsPF7Nfz4UgI4wVcXquKxlHptWkcal6gXM9JhfASxvhlR1GkkAVk6sskrUe7Z4Gaw7swZZO1gkbg2N49PxtupJKQ1AnJeGSHbQK4WAeUhgpoedTD6KTrWvs74UlNRPh14nNAt9ZaPgmqk8kHtGgOME7F4v8KcrfaULn9J_zAdFOgN40RP51m1Tg9lCuuQib70qNy2LkCZkxzAHgPzI5rx0Zrj8KpN85ckZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlPf2k0xiTL6AuQbzhZFy13rTD1mXJ7Jw-JB6qdOD1AHe2QMhimB9TasB_Ryam50_vrMZUwXpSB9TUjGprbpalEqH-XG9KEGkvQqLXTh6U4wuBSgB3p6r3D62ZPMh1jdllMh0IUgIPErDcq_6_5Rg1v4C7UUv-2l4SMfHpplWDy9iHg6UuVGqkSawAjSLatth66K2FApcwECybE-IRLHUCEGzvivqO9N81vheiUbgk1Uv9HZY3c9ITqOLofwOPs-W2ZHH7M0CR-q3zTKwZRVQ90Lcz5nZFuFeoVWP6m7IqSyntdoL8UoNOgjJwb-_abxhPsSyx5gJTV79CqtTKq5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HIB_JLCs1MYenfEP82zfQJ8xgIw3VK6IUKIdfE0YKQx1V5dKI2ZeImvCaqEGy-StjTy2od6jrKc7tuJLiIFBoIYWtd8GjZgznTt_N335tBT2YZ-sV29ay9_O8W2BHQxZitYN6AaoYPIeZB7bkC0-QOzuVuSjtIgjgoHggZ0H--TDbs1b7bqaqvyQN7A3l6D7lRJNpI0FHtOW5rebBf9k1Ri_BWvTYQqDDwewCs5zCbHUm-bjmzSwL1lcijA6zrkyzzPWPI4b13SuqeZRfx9WFkNmeNsyq2mXfr7o2SkU3mZGwo76LC3K0GSQ78XQmvYWYERXUH1VmK6Ly2fDZle9NHPP7NEso2ekPD1cWyh9pzM2spGXtOhH5Gv_SJuT4OjkwxYJVrN5c1J4-7cSZMbjwu2HpQrPjYSLuWa4__ELnBlPQn9R4MryWKpc8KIGzTpsdPXQGxHWBgLP3edKt5qSM_eTn_9nwDmhhw7AldSI1G4oQ5mdcuiX1JTV4Pr0gzEx6ia5YJG3_ROPr4csc0KvtRvxu2WYEDhkB2bgznNahmtnp-tqEOTy_oN4bo-q7ZLqTuIM9zjBqtU0lwGbcUcDNpT2pPBdGKi_-ravemARQn4XAVgsl4BosEswGXUDB74oEPugrWUVXMdERF_tfdXpaIGnc3EPGyqxD5xk1QRKWLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HIB_JLCs1MYenfEP82zfQJ8xgIw3VK6IUKIdfE0YKQx1V5dKI2ZeImvCaqEGy-StjTy2od6jrKc7tuJLiIFBoIYWtd8GjZgznTt_N335tBT2YZ-sV29ay9_O8W2BHQxZitYN6AaoYPIeZB7bkC0-QOzuVuSjtIgjgoHggZ0H--TDbs1b7bqaqvyQN7A3l6D7lRJNpI0FHtOW5rebBf9k1Ri_BWvTYQqDDwewCs5zCbHUm-bjmzSwL1lcijA6zrkyzzPWPI4b13SuqeZRfx9WFkNmeNsyq2mXfr7o2SkU3mZGwo76LC3K0GSQ78XQmvYWYERXUH1VmK6Ly2fDZle9NHPP7NEso2ekPD1cWyh9pzM2spGXtOhH5Gv_SJuT4OjkwxYJVrN5c1J4-7cSZMbjwu2HpQrPjYSLuWa4__ELnBlPQn9R4MryWKpc8KIGzTpsdPXQGxHWBgLP3edKt5qSM_eTn_9nwDmhhw7AldSI1G4oQ5mdcuiX1JTV4Pr0gzEx6ia5YJG3_ROPr4csc0KvtRvxu2WYEDhkB2bgznNahmtnp-tqEOTy_oN4bo-q7ZLqTuIM9zjBqtU0lwGbcUcDNpT2pPBdGKi_-ravemARQn4XAVgsl4BosEswGXUDB74oEPugrWUVXMdERF_tfdXpaIGnc3EPGyqxD5xk1QRKWLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmQAnf8BJSEojRvUPp-woLyzFwgLneA20soHwkWF1H8g-GdbB31M3xfOgzf07WHrfKOQ_fR-z_CZ9gbyB4MKmt3p1vcqzHDNbFn03xkYdMvuwrGtRyJqVKNVKu_D8tRzD_NOimg0WeThSfFciXHgBUG3Ehm1epfDJEQg9vPAjR1GTH-dffHrWMYTMQStXf5ir_RZJwBMbjLa8NlHafkLBt6BY4Ra4gMZJP587EXa2zk3lIMKUhNNVKXqoG57DKV8iWA362-B1V6mwdJXDoKOUxmzmvo_8aIba1Fd1nmiCQVtOJeuMJ7ZM7WSjHT_8L1EYzRRX1yFfqGk3g0oIpmtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=EHFfHNoOdkixWaaV0RaR8QOu-HbKhmwJEKAPm5XMH1YMMS7OC3zEuFB11bQ2eklAnPZyBnD2_4Rbcc4ZqA8SCMYr6Qp29Ady2lcbpDOTJX7OwQados95_TPmxHqdLjjPJLHOZUmJBkejJfBH4euGvcEtfK0_IhquH3LlebHuAXF9KN9n2lrORWKE5HPthzkI24T0ATkdP8aTIGeCEeEpKIqx1Tbgc5jYUOc8beOWJ8aDr_STjvjCNuYn2j9GbQxar3iFUZLHzCC3eLvIS9LJjcI4TCfOwg1h2iVU486CQQ6WdGndzGxerhjWWvMV8Vn74ADxtLSkpOxNBy3FvWAeiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=EHFfHNoOdkixWaaV0RaR8QOu-HbKhmwJEKAPm5XMH1YMMS7OC3zEuFB11bQ2eklAnPZyBnD2_4Rbcc4ZqA8SCMYr6Qp29Ady2lcbpDOTJX7OwQados95_TPmxHqdLjjPJLHOZUmJBkejJfBH4euGvcEtfK0_IhquH3LlebHuAXF9KN9n2lrORWKE5HPthzkI24T0ATkdP8aTIGeCEeEpKIqx1Tbgc5jYUOc8beOWJ8aDr_STjvjCNuYn2j9GbQxar3iFUZLHzCC3eLvIS9LJjcI4TCfOwg1h2iVU486CQQ6WdGndzGxerhjWWvMV8Vn74ADxtLSkpOxNBy3FvWAeiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZN5JO7mBdzqcmqTnVLKXJ-laHpfOW9ptwfv5F1LtXAzBvdFB2fiauRNamsUovrwmxnEBnxd6TlsfKzbR15IA7f2nleh3akWvrOGp77t3UneuTKE3RKPECXW9SlQTOsKY1zctHI3DFJoq95Jdimqng-gr_wMV-s_JXAUBsnzBp3zVsWVjCq7M-nYaAvqqX941t0wY52zHMsMct_7Su0V08MA9nAaB74-u184nBxo0m3stbcoPx307v5aAg-HTGVeIh1Q218_W-ow809LgUSShdWtLkLW7LpubGon33nfH8Td58c311J--KZixecYmvtkTXENlj0erHQcBwYhrTbsXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=j0aP3nImUfEBBBRuhsRnsTtjEl807r-kMzloXWGF744TFPQ__zFhrg48SIvUToxY9JsU6oWHoLIb-_s8kxW_0JseS0y719eK9dPR0iEQUkv3Jw9WwGssz37k2_qeL10H-0LzJi48-k_L1EPcuPN5aF_cyOi8kvji0TXHch3Fh7k9ZALQwi2jZK8d949E08-7yNFDXcaxEZqKi9EW_V_MLAkPEi91tFzF7YeTe54ekhTLd3jqSlo3646e3Ge2EwWEZux8T8wZz3KLzC6w4PxmCOvSNfVE9F3OYE3EN59KQEKAmW4GkkAMy1XoOva0o69ahmt0zMo3SfmC59ScgFTmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=j0aP3nImUfEBBBRuhsRnsTtjEl807r-kMzloXWGF744TFPQ__zFhrg48SIvUToxY9JsU6oWHoLIb-_s8kxW_0JseS0y719eK9dPR0iEQUkv3Jw9WwGssz37k2_qeL10H-0LzJi48-k_L1EPcuPN5aF_cyOi8kvji0TXHch3Fh7k9ZALQwi2jZK8d949E08-7yNFDXcaxEZqKi9EW_V_MLAkPEi91tFzF7YeTe54ekhTLd3jqSlo3646e3Ge2EwWEZux8T8wZz3KLzC6w4PxmCOvSNfVE9F3OYE3EN59KQEKAmW4GkkAMy1XoOva0o69ahmt0zMo3SfmC59ScgFTmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7XvB1Dnd9gpe2fAdURlGbuLtDQmvZG65GLPGysZ8GWYN5dTayG9hJSKLYIkFGP6AOGHsynbjjfJ8ledu9NzEjaLY4I3k7Hab4FBhf7Rq8LGHOpVsLYLVjvR40fHxSV-TAyGRsIyJ-VhPOyE7mXv2SswCVPWL6Ov-uCg9QllXhGA305J2wFHm8r5uvaJr-TPjO8J5AMeT388Nsunc9dxtB1nrcVHmHG9sWFSRFVxa7vc5beqx7euCcTOZ0_fdR4GBRiDWBa39rhzhdPDeC1Hwvbo4gcwBryw0aUDk5B2oJeQ81A2pl_1MnFZyxqijrHM51gyrIi_HyKMQaO7QtKyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=I8R8oyoeEptxo10x2Pa5um1C6el5W_yBCz1E3jH7XOtW6DSfHUGT1bzDVxs5u11QwVceAkMZ6Ue-GuhJS26OQ0HQ2jlxQsos_8K0fOZwZ0JjNtKlBZNSezWUS5JKE4RJsRGaTVTWfDTg62ryq7G81XncABeA2SPxxRt3RrfsgYOZ5JFGr4hNHeb5OgHyM8zeu92jq6YI_bEh4Nrxz_nxGPfZJXKcQiCdRqomzxQa24h7vAj0MNSqChZTyc3GUdZZDIUUCxRTGtE9ZobSYqa3rktGV52tpxUkekFT8WzmjE0zcoUFIjZEPU4Na00I3aKJtB_JGg_yBsyITzU2uGVbiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=I8R8oyoeEptxo10x2Pa5um1C6el5W_yBCz1E3jH7XOtW6DSfHUGT1bzDVxs5u11QwVceAkMZ6Ue-GuhJS26OQ0HQ2jlxQsos_8K0fOZwZ0JjNtKlBZNSezWUS5JKE4RJsRGaTVTWfDTg62ryq7G81XncABeA2SPxxRt3RrfsgYOZ5JFGr4hNHeb5OgHyM8zeu92jq6YI_bEh4Nrxz_nxGPfZJXKcQiCdRqomzxQa24h7vAj0MNSqChZTyc3GUdZZDIUUCxRTGtE9ZobSYqa3rktGV52tpxUkekFT8WzmjE0zcoUFIjZEPU4Na00I3aKJtB_JGg_yBsyITzU2uGVbiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=pZj9pGsUqXpvjxhRjo3KSgNWL2cy6PEBlgnczUA0pOWvCUo2IzyaljID6gODNzvt-BLYDggpr_NiPIDCxA_Q_EVeqZxfv6gXjcRgMDhaTpHqvWCvNzm9rRgxTzUS7t62GlYTBMl0t-LsmGcGJXhG83oEEMU7XPaQSOV1uKlUsA6hQxtBACxFfGCrAvgSrVgWG0V5SlewWO5bULaG5IJaXctooI7ADj4DJAVp4YCjRTLsGlpP-QdqDZEicquzO64YvH9TsegvAkouw8hX3Njbg635rMNK3_FvLP6KysnTlFkBL-STU4A0j5cL8K8i_iDoNTaLGPsVexYKzy-8F2VsXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=pZj9pGsUqXpvjxhRjo3KSgNWL2cy6PEBlgnczUA0pOWvCUo2IzyaljID6gODNzvt-BLYDggpr_NiPIDCxA_Q_EVeqZxfv6gXjcRgMDhaTpHqvWCvNzm9rRgxTzUS7t62GlYTBMl0t-LsmGcGJXhG83oEEMU7XPaQSOV1uKlUsA6hQxtBACxFfGCrAvgSrVgWG0V5SlewWO5bULaG5IJaXctooI7ADj4DJAVp4YCjRTLsGlpP-QdqDZEicquzO64YvH9TsegvAkouw8hX3Njbg635rMNK3_FvLP6KysnTlFkBL-STU4A0j5cL8K8i_iDoNTaLGPsVexYKzy-8F2VsXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=O3YWCcjQBIkvsrSInhuEFUqJGw7LMAiEdVqbPT_Q6S8_6DIV2pxYafjImRi3RpsY8dIuyLT26yCVE79sMpo5vG57nCxwUbccuK_hKNuZfmtGUtYect5UBGC4WaUEC1iaF-5J9bvuWMJprg9Pxo5kEOfXDpFtqn9tFFzUF1vVmDddRw5Gskasqhi4k6cr4n8MYUrUt8uKM1BPk1LdhYbUaXMAnUSvLxwvfxj6MRp7wUlvpJh-SFxHPwP1DrjgRJjI32p8dtIuv5xgJ3QnFSbOGD4bv4V_S_jl2pEYr69RWEK_baXPzcUKUBqzQn4LJvMqNOVAtOJyqgiJ-NJI3dXcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=O3YWCcjQBIkvsrSInhuEFUqJGw7LMAiEdVqbPT_Q6S8_6DIV2pxYafjImRi3RpsY8dIuyLT26yCVE79sMpo5vG57nCxwUbccuK_hKNuZfmtGUtYect5UBGC4WaUEC1iaF-5J9bvuWMJprg9Pxo5kEOfXDpFtqn9tFFzUF1vVmDddRw5Gskasqhi4k6cr4n8MYUrUt8uKM1BPk1LdhYbUaXMAnUSvLxwvfxj6MRp7wUlvpJh-SFxHPwP1DrjgRJjI32p8dtIuv5xgJ3QnFSbOGD4bv4V_S_jl2pEYr69RWEK_baXPzcUKUBqzQn4LJvMqNOVAtOJyqgiJ-NJI3dXcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7NwzffI3QVorvzCeuyfRCLWTaCUmu7gLp2l-Z0_tJEoExDi8x0JKSINoWmYR-oiV9jijZ9uYbSQYoWhdnpxhAcREsigFaalyV59FQAPm3KpX2qRTCVYvryw4Kj3JBde9r8J5xUa9FK4K50YsDOUVE1CVY_FuaRJOAa_GEP3dfi0PqybYd1_0fNAFXA7pVAY_2BuUVHALcNNcEKLUwmFfTgHxFkwkmOBdFy0cndgwXt4nu4yfYrTqTblp2MSQ6QoIvIoNO3TWTbYvl2AYHV-ipi5OwY9eK4XWhSZ3QdSDv6UvT1U45v0fKXdlvsMmdAgk7TwSW7joH12hn2qknuRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=SKQM8EajOpLR0cJ5tx6v0rkcFRHlSB2UXALNeQlUfJtRrIlXduRG9M-QmWg2KGUJijAULoehQKcfN9ZW2eConsQwOa96u8e9i_iRMclTfaiuL8_nmx1-PeJJlWAUng-zrIGUz4gdcPu7U5FmgL6iMvInMgSzNCeoIpiELM2V5yJQXYmB7xwS-M3-SDLm77jUv0RFBpCS7DAXQxuZ4I-RJa64AjSIFvEvTfJHBYeh1jMBoi7VW-yptpSpVCkn8uPIy4bJqM0fIL43zf7Ux4oAZcFEdXF2D_GVUoBMq1QdtfM5-_6CDL89GcpqrrKDUTaxbQwTn2Pp7nHhfulLm4t6xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=SKQM8EajOpLR0cJ5tx6v0rkcFRHlSB2UXALNeQlUfJtRrIlXduRG9M-QmWg2KGUJijAULoehQKcfN9ZW2eConsQwOa96u8e9i_iRMclTfaiuL8_nmx1-PeJJlWAUng-zrIGUz4gdcPu7U5FmgL6iMvInMgSzNCeoIpiELM2V5yJQXYmB7xwS-M3-SDLm77jUv0RFBpCS7DAXQxuZ4I-RJa64AjSIFvEvTfJHBYeh1jMBoi7VW-yptpSpVCkn8uPIy4bJqM0fIL43zf7Ux4oAZcFEdXF2D_GVUoBMq1QdtfM5-_6CDL89GcpqrrKDUTaxbQwTn2Pp7nHhfulLm4t6xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv3jgcFXN9_IJR4vMwzwN44KDZl7Qy6-scJQbnnKbyt47pfJt9mmsaowHMxwLSe__xmB9jHO9-LcpXJpHD3Eo00U5cnure_EtNL3cXR-2rCsCun421-y3dA7E2c6TbxJTAb3YCOgj7g1FVhGHdeHAh6mj9XQQfQjdufSkcfbfISv6I0kCWqBSKELId9Tdlxl1XcOiQ5cLdK5Fb87Y411-bUfjrqJd7-OofGvlX5PoZbIKbVdzrh03DnA_cULn3p6WZTgU8cd0JhSPXfr-UPJ099sIiYUEAZB75GYYJNp-38QqmjST3ZZ5H68wZbUXb0eZkX0oVud3VAf8h_lVd-zPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6jKTk4MXFTJubL__XkYIJpkbMyIsAsZ9oD6_tMJDaMhpAAZDfALpQ5Zr4BxNxpo_x7d0kiNKHThptOuXVI3xL0BLnbZbN3b9JCJoWhv5-e7LOWqYjvmchY4tcQg_TwamlhG6GV3kC8oRdwXlvyjgv6QzxrHn1XCYeOVJROexbKHyMeHPhoOGHPH8wWQdqMg_52XzKJYaS9vr_Qtku86SMTwlZO2myHzpTm9vNVKap2gHjgR6ti6cM9UJK6WJHEikuv_dO1CXWA_FO-C8R20DuDbAcqMKbxhjUZr_ywhNeh2C2NEex_weToC5d2fWTXKNn-sm40XggNygS7NtR20Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnq-_OuCFIX7q1tKGioTEkggFPiK-b2EkZddUMR_2GTq2Si_ZAv8ZL_jZtELrejioE_WfKBe18LREUzIWZvRsN-TQBRx4q38KZ1osLh7_jaozmC6z9sS3XJtR0XpeM_D_Yqul9lMwrWK-jFET2oBSREYRCNW4Msguc07WuaDT0buwWSCGLyfLLswG1uVs4cftcfgC9SPP0AfLGqAdH_0XoWEnYFwc3e6CSGB4GlIrgfJrLyxLBhpjTDSe5zg9t4fB_xgrAc1lWjtpG9-PFymcZig1AJ6eUagbUL_wyEWCVTuTJvZoj7Tra3AmGpYITr2r4Rgbz0sEt3gBEEW6PEvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
