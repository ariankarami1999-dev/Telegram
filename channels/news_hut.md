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
<p>@news_hut • 👥 143K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7bhz2u6bn17WVsRkXKQIX5wh3hh6Wd_-PgDePYxLlmA9vvmwFfgy0kFA8OKZGAalAkEVcSfSHHvzr78ZfKQDLem7dlS-ejM_JQc0Surzjcq5PibnRF8yBVRV59o1a27lVaPc61OhG7ihVcon48vVW1toHcKtRr6H9YzAfEl4drHg_ZNPIMhbruAzcvB5alol22SwCWL7N1G7wiPONlZb6KcLQvca39DGdut73PVd6M6OdT1qh1ZuxXYxGfk06JQvlBMrUbZAwcer067LF2MH-JZfknGCvg5Nc4HU_GYQEaEcxMOMZrJNcL_bJiBl43_mgjdQuGbQPDHAvl3KIRe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcJRossjPrWCF_2utB-vq8DPX---v9i4samIEGNEWxIeIAn-zXh2XL3l6PLdO8WiFx69-BFkq2WBjUmzwePLgwCBbciH3IXmbpjIovUMl6urt8xChM4oWfgJ5Obm8291G_4lnBqR_auR_oVaobJkOcSsDGErJhqJ89igdfpLCMXr-mu1e2xpK59s2ZO5WSWIkClnBAJhXkYZjxQ9ryrgfzn5FNYbU_vxQVtDR3dYskQ1YVPA2w78x8q70hZdp82eYZanLeKdHBU3WNj0pYZShJ_p6fk_zxyAQ2gFIQUcjoV16J44aPiTrxR1Hcn3qeQ-7aMxXkpXSicSjs6t-WsA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3VJf2AHOds4t5Y6OqXwn8igGQQjXeC5ulU6ftmOAR7t6pi-tyUEYTf_DqzsjpHhOfVa61WxPM_p_g9-rguNjNqrhlDniKpNL-VA4baS3NUkPuD01P6xKwZ2YoR2yvxrGahVwHmRjvSU9yyZe4KHVljKxkleKR60vRz0Ov3b4TDHV160jq-tfZph4lV7CDTzYxEJ5yQShj6_NGv2RXuPXnbe-qfsi-OH3eUGykmbpVRodx27RKal97SBe-DhgXnEge6iDu1QamrVWy3luXVyPTY8T60_qtN-BkB482o5Ic-nKYaPKleb4BAnvHP4ieVBK88jf6DIBzOCBMs92rQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1NRc_RjsXBMseCDrrznSjALBWXozTYvD9dsKPHMQUgAQqK8tLvE2l9nqijdKnHWajGHuSZDAmxLFvu0MUYO46UfMzPMqfwtnX-OF-BbP48ud5qCGpC5v8nnxNV1PY6zwnNcyxch8Nx-ao93ICKONA_iX9tYa6VINHc1SM5LVJSu5DY4gyLa1Om39tfkSHRNJq2MjwKTBly06kahkTOs5CltQwnvNAOc-LiplDsjwG9u6vh5hrMdzMJPt_pdRMpY9FtP-4Zo8AZTbSqWUXs69461c9I5-6pWIyAZf8-q1gmZwxgBwvCmhs3x0DnQrAsjJ0iULsgvOiN2EKmIBoHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFoNV80J59si8gH975sWja7wnBr6HdwRB62NoyPe7BHd41oVW-QgUhdAqxhZj-wMkGO7ipw0nLFDjZSLwmIUZgXX19D4euO7LhQm4f89lA61h_lp7gOZXLgSGDrRyV7vv4l8JwEK0mchC0Wnau9M0yH_aMbB0QR1v-cNyHyl541udJVt-vrLgGGW-HckQ-5d94jloK_QUyzimvC8JmkcItXEzi7ABnMuwe4cgkgqCfKJH-5doeGZ0Y0GzrftCJDEnDQSALmbQu8sgRNbyrp8__KHMhHHgPyhouP3WqGlY_KrrugvlwvvNVIbtlewNOfIXPHoHHRtTEgwzrMbKMAnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_vpNPdi1bar7Cp9v29IZsx5RAV5K9_3LO7hijc7PXuqaftRfccDZCS2ZTZiJhOJGrM1A9nRpbJ3fIrSMHzagXu8dt1JHnUb9FhGm-i-pN037xsRnUvA5T6kkRCbqBrXV5WAkGiN8N32P7JL86SOCdJZg8Sz_Ai59nYjzLcG1yUg2ZxsP_a-rpJ9eOwk_Nwe-86R_yZN9CS_tkih51jZ94QgOk9qaLvhGfU0eUnV2QZKPP1ykx3OSQY-q9-nNZ8NpsVAl8s2JPmmMUwVrJyliIkjFScpdn9vrcTnhHF1yxMp6GVzeGpIoVy8jbHpYR1yXL_U6j7wqa7_sXQ5nFNoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5CNlrwVWJWkb-7uhQcbASBHQ3TLpJVpKThZKxyEgm0C5o1arqBT6vA0BwG0MSvbz3mlDU8nIWvKgRPO1u44De7Rvp5nCJc6NPP5yuejFtiDDTezPW8klrzXhOGsrfborG4iFHOqOs_Lu5fCQw1vfd1j8P8wzGCEMIY_YWBiajzYt-93NelY6YiMNBKL6bWRkvTZLpFrPVDuTr2kD0qWBAAlAajxQC3WEYTZXEY4Q9VSih55aBTfEVQuFknsRx2IXQH2BTXT5g11ry8uxKShgI1d6LOcy8IBIiqLq0pSd9R5Ppk_ydcCzpRSh2uX6gkySdxccazQCNVjSXgk37r9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXAkiY75luyi5wJMK5BHo2Kjwt2EtZRsvBmQtKWwSONFV07v1kXA-l_cF7XKjxHtdve_8rALHV53u0YVqzFV1m1ErggGEJYpuKPKXI2zwyUTL_XhGpIRpvFgtSjNCQoSWjZaMmdRhHsRSP9Ivt4e7NOuHNyN4jv6qTxpSGfcvybyOGkbIVg0LyuKiypNkbSFHAI1zgPB6UAGDaJTV_ltEXBbT2zp1Fqp93283y5aEWwWB8nrhp1X29MvQ8yziXimdYlekxOnnZtqRMBOKbP180Sh3PWu_HcV_lyAi5kRUDuWZEgbFBQmKrXEo45LR6S-1_8OOdT413OYKK_3UtU2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG5IqvMM2cHc4AVjR5ot2hfbSteYgrHZsOE80pMshCKiqcpxz2587sN6TSkswhQ2e0jGhTITgaNxymd2BuGVzyhLgxqLWHlY2JhWSsCFAnK2gdoyR4RyoIs1jD-3H4pArntdO-_0-ck89DXKjUFk90E6KbwMy9d8C0qwroeIWp8ONawPWe0mgYZ_Soe4AJ88KAf2BhvNqkSWQgZomjXS_Ky4Gvjidus_2C6RSW0VSILrC2BA934jW34Z9UCqxFPnuefbWxl1TepCJ6IykDwPoSS0E-dC6hOKHRe7h89gbhZwb0H_vAFMcJFA_5n-sBnk7CERAN3FnKqhHf2-KI3iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NokYCFgi3cZfUO9EJ-vUh6XiSurSBIVnmvCqjTUInouHcQXswzwMp3THw35X0NlcDXhOlXt48genrQxWoWcTrBNAogX_Y4whI6IQB3xTox8OBZUishnVf84T6ZcWdDI5Xf2btXqZmoPOcoGKswpVHrEVC0-WMMhj_1CjcK16wTRDTWpcey4W7SExv3TYrFVptpjEJigo2icYtuxJndTZ0z0VRB_pAOFsB_mHcEela5GhM0wmKJwDJrBkY3ws1nSjY4Gm6EUGJSzHdV5XsrzkeVKWfw46WbzRE4mqqyOlIQO2MbHvuS4jCY6IPn9K9DkmSusyLPqWzoFXP8szBa8ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGAECeL2tBt-oLCGYrrvaTKpWfPdb2gn1pYVSzbhFKXWhk9p2blQ8keDDGNwTAHNqFLz1PUyj5FpEYL2lFLj-ru1L69wMJbxWx-xY7bXUmwIoSHUHGMBr2_cTusPEXYuO1gZBBbsP2x8rseDP-OyUGfFFCzIHMANgfRpHNL2CQO0qGGyJtabfL-8IletdLyS0TbLBbRYB37oOIiAJ0bzs22rj2og77VZI0IXTZNlWEFQ51DvnHJcnW8_fZBNrRUlezxaK6hyb5zqkhXGTA2vPlBFhR-96VCciSFoO5DKpY51EW-95OalcORFL2vS6BFJBKELawgJ9SST6HjTVmhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phX78U6n2bxjwRoDbD6iqE2mgLc-ZCvaVfvraJFCdjcgwZ1T8obkcDqLq9N4Bxkre9FgPPjYaXSA3paFXoU-6OPu0CzbIsG2WqI4YZkQvwupz5EZ_jZ-WmDfAbdeGex0cpmhqW0HueBTEfhKj8OYOWk-lbfZP3VXN58s_k7whhWKCcIeg3k9mTKirUm0oppr2w64SRVHbXXbmHXkODQzE5c8tuG3JPJCOmaOjEqbNYcJNtmfyS71mWXgZLcnR0HtYmdqJTHlOh_cY_Y2lijbiitCos6vfkfS9WxCc-VAgpM-ki4dvEGQhlR64Zhymc1hMUYZSZ4k-44HrcN52hzoiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_lmp0HDP3X7lmOuMIKxNuQRGuvjzMyYe12Np6Qu6HmJROxNPhP-kG2uHrhyBN6oEkPiIAH4rfTE3X9XRZFmCPRASsUncKybG1MeteEm60XZzJ-qds4TcEXPxOcc9ab5miGLklAtan6wm2_tC1pL6VrfgKK1zwhOt16GVMAPd-crQWClHc_Zc2wHtMWMUHinAgsU16AEhLh08pN7SllYXck9n-vzGDyVAyp4GrWlMXOU_0BBZ3C1WoTCEESxn_C7TlZS2h9BWwKm9SKW4a2PivBacaAa_UNQzjdcqb_Iv8XbdBpzdY4rDPXlZMxLrERJVmJBXw6v2wBxxN6SSJOkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e42QB_shB_-LWoQqHcnaJOj3BDt_swirSX1dqtpnLdavAe69nIAmXeihDuuZZXtH7pnz2VUDUgAyfM8022UtGjg9HvqUbcN7ZF50eWYNzxqcmvYRJp_S9J6WSgDd-ex29ypp6e_eyKZWQJno9e3zHDb7mF4vMvugLs9bBqWmTJrxiA_ksdaJH0ob25X1F6X7taR2QDEIcx6WIadFEfrZcPOBFxn8-OBZzL3675aGMUdvcMD8VtdOkAeSAWtfAalZzMeigXwAslcGXB1SOlH-9sWVAl5Q-5-ZO92zLZ452EZsfi9jNrh8ECyiCnj2ZkphiFAqmucK528gaxYEKdufEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=G6kJchGQLLymU3oydRRbywBUasz6k1sp8BcXMw3P7S2O2tGE5cRvUYoe8OH5huKffGVFI0HZb-7MHn-7y_JpJAEW5hsprrSOy1E7X8vkWX5h7iODCOqibAKQCRn8HvX1lQs7YUvZR7P5QBNscyXwWa_aXO6elIw3Hd0Qq1QyKYUGuAXqKE5OraZhyi6JoiEAA-idZCMK7PHkSy7CPiFhuIAk11K7iVc08BePHGpApCi51rSbWVbaw64Xwqu24pj0c3e3g2pYR-iWyHGn_RdTlK_IkgcO3xcUfyEzf_mzYNTZkV7HTdFjHJi1eOi8PlXuxOL8cPWZrKNo6_X5TATnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=G6kJchGQLLymU3oydRRbywBUasz6k1sp8BcXMw3P7S2O2tGE5cRvUYoe8OH5huKffGVFI0HZb-7MHn-7y_JpJAEW5hsprrSOy1E7X8vkWX5h7iODCOqibAKQCRn8HvX1lQs7YUvZR7P5QBNscyXwWa_aXO6elIw3Hd0Qq1QyKYUGuAXqKE5OraZhyi6JoiEAA-idZCMK7PHkSy7CPiFhuIAk11K7iVc08BePHGpApCi51rSbWVbaw64Xwqu24pj0c3e3g2pYR-iWyHGn_RdTlK_IkgcO3xcUfyEzf_mzYNTZkV7HTdFjHJi1eOi8PlXuxOL8cPWZrKNo6_X5TATnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP5TU5bKWfej-pn08orWdChtYArDrZWGNL0gYOZpVIoEmn4tGJdMtxaxBZeDJS9lix_d7DFwEu7zuNNiU4nW5R_29_gdPd0DFzzPNE42e7ZKFCiBU8FMJcABmEdhgrMi3lIJW7N2rkjAvMhflYaOfDRVbojb2MX0xK6DnGuaU_SpfEJME66uY2CDBR5uzGvu3t4VyNrZeTFA8Tmb5YfQfCVsslyLg0dwlyPY7qmLKKE85YI0NQI9M5yLeXbadCvvqbIE1LV1blkNta3d149u13tt54y7-n9qSfVARfhOYIhdkfaCBRrER06fVw_MvdpXXiT6Q0ZZG5DggMnQImg07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2LJ8gRU7eN-HBxowpaRj5oNuEN_mpJrj6S33x88WoXFTCm8pWb5Ziqi39bvbUQDyv5IvtgE4nqVIyN3bw6rKreiOPDo_ErcO_PZLsOVKnWPLl0HWQ1fB28KY93uuwg4F4h34vWgP5fGfaNXM0I17IwPPP7xIsxbsKoOf8CKJr4Ptu9QHJWljZnaAFMj7G-4FqpNiwhuFnvJGzoVleU-B_8p_fmNfu2h1j0lu5vq6RoX9uWtdCACYrcF1ZsUChSAv0AOJV98zb7m47MpIaVVfIU1H7XTXeqy2zIddmO0oWlDozBRcSG4wet5ELvxHZujdqRjNocobNNgMjqNbnEQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI1b1wQl3UKNjlFIIGai6wefuKMBc5o1ZIXmWHuUU3AwyD8jvHG2_ZYOzYzWFiLgf2c5rqc3hj2VifvBD9M5t26Fej0mk9fO_ojUOIAzF4oEr-1yVdiLtg-dbMhQCptMAXhMuEBasDw08Z7UwAUwdImEPeYX5duRsYbGJ756WSgC1CkTED4v3DG_YATxP0uHI9m8MN_o3d4JX-i0u4V8RxYEIoKy3zPYyYQyPjd6LelkRh4oMwuzgxe9v-LhtCA8PKUP9dL7NYV8GLgGft0VLpLKCMbyQSzkX0cALo7Yn-li1ODyKVLv6kVziVqF553ackyx92JVx4foMSkvdXJO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ZpzFaMG-z8-aWWaI8O56NdRUR7mh88z47V_IF--_DZMi9d6QtYXtpkdHLxDVLPKjV0i3LuTWBttK8W4QEJVWRkMrZAVYig4NmUXL6fgB_U5WUqW3qtRTnh3cApk8_3r43FHjj-JJZGGCeizXbJcXTrMsEIuABfA3MJeiq48427EycwkNkbV1te0IVsfX9rwdWE2cgZGPPetvBGJZiS36MH8e5aNgdPtnYl73z73vBuGBo-uE3sZynnqpAinCUGiu0ueNNWz1ex_0TtJK0jnrvS6MyO7o2fyPshsHqly7QPVB3OI2vXCKLFhoRvGiOksB4qed3KCYdGn2hH4XgtbnUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ZpzFaMG-z8-aWWaI8O56NdRUR7mh88z47V_IF--_DZMi9d6QtYXtpkdHLxDVLPKjV0i3LuTWBttK8W4QEJVWRkMrZAVYig4NmUXL6fgB_U5WUqW3qtRTnh3cApk8_3r43FHjj-JJZGGCeizXbJcXTrMsEIuABfA3MJeiq48427EycwkNkbV1te0IVsfX9rwdWE2cgZGPPetvBGJZiS36MH8e5aNgdPtnYl73z73vBuGBo-uE3sZynnqpAinCUGiu0ueNNWz1ex_0TtJK0jnrvS6MyO7o2fyPshsHqly7QPVB3OI2vXCKLFhoRvGiOksB4qed3KCYdGn2hH4XgtbnUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=PnRzgn57mukGHhqmGj5ckPfo0PQQxKpY_mfgeCGi8wH1kkI_xUf6GU99HMCUOzkzE0QxcOuWjVaFGdh7F78GVxm4fG9n58CUxrPWHKVMtKOwibbyxzXr2u35hqH__MxHluSpAKc3qUcZi66ck_LGqikbAnwsiw6SuyBBuSGYOIyrJSlLzt9ToaoWLCIrlctGgrRDIB2MrBFdQI5pQcFmCqsw-Bn2Fs85mhzJPOaIs8v6iNfhrsL20RFYn89YlNCcpKQ019oiSmAae6dvuvsHdSlhB_h0vtmX8e2ST2kiRz_daZghxSvhLTemToFlBfS_XiiUEf-OroQTPy4xdEYJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=PnRzgn57mukGHhqmGj5ckPfo0PQQxKpY_mfgeCGi8wH1kkI_xUf6GU99HMCUOzkzE0QxcOuWjVaFGdh7F78GVxm4fG9n58CUxrPWHKVMtKOwibbyxzXr2u35hqH__MxHluSpAKc3qUcZi66ck_LGqikbAnwsiw6SuyBBuSGYOIyrJSlLzt9ToaoWLCIrlctGgrRDIB2MrBFdQI5pQcFmCqsw-Bn2Fs85mhzJPOaIs8v6iNfhrsL20RFYn89YlNCcpKQ019oiSmAae6dvuvsHdSlhB_h0vtmX8e2ST2kiRz_daZghxSvhLTemToFlBfS_XiiUEf-OroQTPy4xdEYJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ5z-lngWzIf9T4cr7041QR9XHhO2Kes3j9tHMNK0lxNp-HE7Tm0gB9je2_sP7ZdEjJ0BSTei7-1wnqCcHbynfFtYscIzSII4hQxAFXS_F6W8yMJ_gVhy1C4O2HGo_lnqV9aP4ZFwzTyg_Q2UYwMS2S7N41orUi1rXRogXYQss14o5_k0uYqMto9C6RlFzgfemGV8kCFEzQTKqa1WaMAZRUrd8RoTXe2VMyxmWS7UHZmMwnqjrxlzQdPEt01_20wDWXmLHjGZpjFvqQZJ96GCJW6FB85aknXYPcEpGKzXJj_osFDyaHPediscS_BM9_EOPeVqCSPg6Mxo7zovCn78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1jx1Q9hMEJiPsTqw5HVz4110Keb9jvkvjAfiaI54HeyRM925Z6iEWiUvWdsa0yld-BuvgvgxTVuwLfDMLLsvnGKZsKae-Gr57rGsYEgKas0yEfdhFuD62JYIHYjJ0TcEankHSktIGdIPa82fFFXxU8zI0VrpgXFIj9Rqk6swtN395Tg0HMteCmZgbnunUfFIuvx0ZpiDF8MihyzVwRj72-pgT--xWz2COxIir0X_EqB5CS2ojKNlP64HeCze3Ane6IFWktPF160p8xtjloweZVE2KoZ8cBQs6Us87LWCZ-oQAZzv5iaLlLwODaD2Z38seXcUCl1Wc7MeWiShhXvxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=F4uVCGYx-DnnMaC6G64EmGLjsWpQUtNEvu8XxZkbfVf3KZLkRlvpeBEjF4SVTLwQvsgIkexxUxDCjYrkEkgXiFFqdFGhG9rSGVrldDN-nlfdVI7EQkodI7WpDBGYs4nIAXiEzTN5yVkfWcQ7qsthzPAGW_2MJGUpRDV9xrH9MDMYXm2ndHU7OdHU6_Mxbe24ZlSOVoGe0ZSxQFWwd7sceCj-YlziC7khC9zQA_nmfjRmF-RdkhebbE_lgE22BVQ4qVVV57_54tvzUmdr2kF7A_tz1X0o3jQeqKH356_i40As7h2M13H7Zbmg3MY7r_UUK6mmx_LBG8Z_94zFhGeZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=F4uVCGYx-DnnMaC6G64EmGLjsWpQUtNEvu8XxZkbfVf3KZLkRlvpeBEjF4SVTLwQvsgIkexxUxDCjYrkEkgXiFFqdFGhG9rSGVrldDN-nlfdVI7EQkodI7WpDBGYs4nIAXiEzTN5yVkfWcQ7qsthzPAGW_2MJGUpRDV9xrH9MDMYXm2ndHU7OdHU6_Mxbe24ZlSOVoGe0ZSxQFWwd7sceCj-YlziC7khC9zQA_nmfjRmF-RdkhebbE_lgE22BVQ4qVVV57_54tvzUmdr2kF7A_tz1X0o3jQeqKH356_i40As7h2M13H7Zbmg3MY7r_UUK6mmx_LBG8Z_94zFhGeZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=FW2aRCqh7e6goUtDUsMGv9wdZQJDUTPKC9hRpOSGazWqyFKnTzZppit4aL255wfzmk1aWSWERDALi4BQXR7DwhA2sTiM-9vKjEVpFczPoOE-5D83A2U3voA-9upDgj6gg3KSLAOnCdNlYceHLd7oYK7Q5Q5oR6P2nVdlcPdkQs4ld0TYbrr2QIJmgm5Uabyw48H87d3ozburb1kF10eMkYZxm2DaM1DXCTHcdCdLa2_AxCjwmpZfFMS12jhXKFZBeMObbwC-YV5q_uY30xDUKB9bgyqYuYzsueFMnji52qraKvTaMJOWq3GPVgcBlWJY8hA8yQtlmNRJVSFtncIikrzI9smh-p6rOizF3kFdFwCfgPeXkJtYae1awKUrzDgjlsetLnBZ7gtakOS6XYhmOvgPg3Z9xhFbeZV9LTAIhUUJiqelC-l7e0yqroXaqW3Gn2O6RLIqBp9vDoh8yrO1MpKSoILC0uJRzqgkcoAtZqlqVf0JaJe0ydIOF3JlH1xaNYcvcMz8rzNrYiVrjLwrLisYJh9WlymbolL1ipcq5Fe2L09GvWjrE3qmDbiJPBpFZMmKoITQEOU-n3CPa2rlY5sRK9vpZbazJUl1Khj4EcvtJxWAKHG4Ymze8crqxkf91fzbxxI_aCYhDElpb1OTvsWcUmiFr56XZi6ziZju3eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=FW2aRCqh7e6goUtDUsMGv9wdZQJDUTPKC9hRpOSGazWqyFKnTzZppit4aL255wfzmk1aWSWERDALi4BQXR7DwhA2sTiM-9vKjEVpFczPoOE-5D83A2U3voA-9upDgj6gg3KSLAOnCdNlYceHLd7oYK7Q5Q5oR6P2nVdlcPdkQs4ld0TYbrr2QIJmgm5Uabyw48H87d3ozburb1kF10eMkYZxm2DaM1DXCTHcdCdLa2_AxCjwmpZfFMS12jhXKFZBeMObbwC-YV5q_uY30xDUKB9bgyqYuYzsueFMnji52qraKvTaMJOWq3GPVgcBlWJY8hA8yQtlmNRJVSFtncIikrzI9smh-p6rOizF3kFdFwCfgPeXkJtYae1awKUrzDgjlsetLnBZ7gtakOS6XYhmOvgPg3Z9xhFbeZV9LTAIhUUJiqelC-l7e0yqroXaqW3Gn2O6RLIqBp9vDoh8yrO1MpKSoILC0uJRzqgkcoAtZqlqVf0JaJe0ydIOF3JlH1xaNYcvcMz8rzNrYiVrjLwrLisYJh9WlymbolL1ipcq5Fe2L09GvWjrE3qmDbiJPBpFZMmKoITQEOU-n3CPa2rlY5sRK9vpZbazJUl1Khj4EcvtJxWAKHG4Ymze8crqxkf91fzbxxI_aCYhDElpb1OTvsWcUmiFr56XZi6ziZju3eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=l0if9WngsBcz5ExDm7bqB1cYexeJcDKiEoNJZdePdWzA0hs67dHSf_cU74ZhiJqE3soCtXjPuhGr7t0byH6vYXXJUlcYg4YA7pDyfkcZdAPRKMadinpU9jxvtn3fYVzN2Wxj4ON1XkIn8GNXxTkNENshfDHV-wWzMLfeadUcHiJHj3eIDAH_opYeroLdv0hF3UT6VXvSjPzJqUHdmIvhmQYp3M4OFBsiOiA4e2R5vR8NMzGkjtcwIMrL6tREDmVorVMC3dWjOylQ60X28El2OFmjOAK8G8fI7h7fpVM6WRl0WjVRahT6T6Sm19u-wT7slpRbL6bnRUdNb-eOhd5Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=l0if9WngsBcz5ExDm7bqB1cYexeJcDKiEoNJZdePdWzA0hs67dHSf_cU74ZhiJqE3soCtXjPuhGr7t0byH6vYXXJUlcYg4YA7pDyfkcZdAPRKMadinpU9jxvtn3fYVzN2Wxj4ON1XkIn8GNXxTkNENshfDHV-wWzMLfeadUcHiJHj3eIDAH_opYeroLdv0hF3UT6VXvSjPzJqUHdmIvhmQYp3M4OFBsiOiA4e2R5vR8NMzGkjtcwIMrL6tREDmVorVMC3dWjOylQ60X28El2OFmjOAK8G8fI7h7fpVM6WRl0WjVRahT6T6Sm19u-wT7slpRbL6bnRUdNb-eOhd5Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP6Q7eaqLFVQ3Scm5eQsAxnfx384fx5JedrPTfV2-ruyJLXSl6tJs_S-_viZizPRQrUl5GWUYs_F8VernoviP2vF887lyXu1-3WuTckBRkqJ2A0huX5OhWlCViQi3kc4NyZK75qzRplrhAX2rA7-mZvSyeC_tdrApWth90yPvu3JYdxX6VpKoipYj9rgGiCxK0eA5Lv2iX5sW9EYI128ULWTgh4zalXnRDBOSpdv7l0Qhn1-kVFmEgPjuYBQ-11DEsS0fzTPbV94DBb8la6jJdLl_xRumAvglqrVpHscyTtATLx98Fzh9qiOLS0JR4uhVil0tYi0R0s4ZoAh9f1Scw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_GnMPERDjaJxI6od_X8WPqISi7Z9M2QHAz9uRrMw2KO10C0Qj71BQA2J9bvTveNevx3z0p5tSsj9UIRyLKlB_XcpB0f6T8IZgioheQH2XjqEKnhiFJTHIlTUQAiA167qjANoW3zQ7RT-okNNBCMqwwYLNgvdgpfwmNXfweg_8DWwup6yPlYf2mnPVb7unu_VJkRXs--VOsGZmD7UdfICQwrRZ-4HtOdX5SKVu4QMylT2VOi_r1VXr9VPY2luzdQtG_gcjT2kFhPHCnxDwLiFT6uci9A9lka5QF5tFKj27OTeRcLv0_sbZVLTBr_GTXuAqteNcKULLl-P4o6YTDllQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=uYLRt8Un0puxNPTPPlTrx0rXIM_NzM7qDmqVTJtK9eL8GVi7i0II_RaX0W5MaJan5s8E94UpYpFxa07AHTQ9bFbkC-gB54wJdIkQWW1qlB-mUrfN8iNA68JJa7D-LYk9s3PesBDT7d8xN8HR40H7SqByi7VBQcX1oT2ZuAtWz_VXZGKVttL_UiW1GhDA8_grMz4mGG5Y19Pq-D2QUsTcROUWYkvxvytq3TnAOgHnyTthz2LkZhLgPETg9icP9LdtNCSMl2qXdRlTLc-6azYOx7EMRYlzdJWArIcBj9wqZ_vhzZqZ48dEWoxAO-WjDaEP9zSbOCs4s9eT7Ig14RyZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=uYLRt8Un0puxNPTPPlTrx0rXIM_NzM7qDmqVTJtK9eL8GVi7i0II_RaX0W5MaJan5s8E94UpYpFxa07AHTQ9bFbkC-gB54wJdIkQWW1qlB-mUrfN8iNA68JJa7D-LYk9s3PesBDT7d8xN8HR40H7SqByi7VBQcX1oT2ZuAtWz_VXZGKVttL_UiW1GhDA8_grMz4mGG5Y19Pq-D2QUsTcROUWYkvxvytq3TnAOgHnyTthz2LkZhLgPETg9icP9LdtNCSMl2qXdRlTLc-6azYOx7EMRYlzdJWArIcBj9wqZ_vhzZqZ48dEWoxAO-WjDaEP9zSbOCs4s9eT7Ig14RyZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=cdDeQZgHY_wqy-X95mv6aDf_urNix6yElHjusADCkkfT7XExvOdMg0smJWEZIe4aVt1VSm3lXTnU55xPzsAA-lSU1V70MlSVRGKsIKYHxYRkCmcCS7orf2vcskpawBbbyN3OROtguQWK6QgXDqTOcpqij-ICSAnjvi2COUQTqQvNCKITyoZIeOBtq6CtAc20u6DWm67_XT3ko818rYXfvtuWUZe6vjHXlqVWXGSUzBbJsHxyFXP2sGP_ExKzXi0yDtzajhsCozNLq7qsqqA3AF-sonPW55WbJvjdY_KXqJUSPyJ91I89cL36lEIJBkOHNHuiy2hdClqJWevh9A1N3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=cdDeQZgHY_wqy-X95mv6aDf_urNix6yElHjusADCkkfT7XExvOdMg0smJWEZIe4aVt1VSm3lXTnU55xPzsAA-lSU1V70MlSVRGKsIKYHxYRkCmcCS7orf2vcskpawBbbyN3OROtguQWK6QgXDqTOcpqij-ICSAnjvi2COUQTqQvNCKITyoZIeOBtq6CtAc20u6DWm67_XT3ko818rYXfvtuWUZe6vjHXlqVWXGSUzBbJsHxyFXP2sGP_ExKzXi0yDtzajhsCozNLq7qsqqA3AF-sonPW55WbJvjdY_KXqJUSPyJ91I89cL36lEIJBkOHNHuiy2hdClqJWevh9A1N3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMoWyf_orcsCMjByrZg958jhskcQkSoC0WLROundxlhbMvypXrAL-AhCb8YMj9Bp8_W7Z9tBASefCvjsOvhu7jS0_J7FXc-s-yKUC1llhnbCf0oqdDk0ftvWZmxZ4FoN2teYdvM3uH2ru9xK8M98PPXjGqsuRemv4Hr9KBGRhSspb8uH85vGTub2-W5WaX35QDk-qPpLMLuq69nkGFZPrfx01zYGSzL3bGTONvWOKuKrFndgCyAqYXh5V8o9qOC9SidGBeBoW5N6HiCHL5soSiwQcQpaLkku2LgOYd5taj40mtb2EpBLr1mHCAlLfDW4mApSNp5iGzRJVhJ1ZGlfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfIel5mwaBm42kLLtUkGLxBHe0tKJRrryLQ6pnLr1zlVCYkTLT3rptNqRu_oCNx80-Uo0a5WIcA_m2wIZcerKft-e2YEh16_bSrwW3fvwyNQOm_DhchgFNculHc4T1OqwTBymsjVfHIP4RNcCnxanv6HqX6pJoYFO9Dk3j7PjIXYNhpI5lX5YRr6Liq5soqLY5dlovjK3iqMbSR2uO8CruW9gUCJcr09YHL_BHUtk9V3eTWAfrpAtG1kiV7S2vS_aCO25BmWD8WpA_WDVpJCAiSCaTVcm1N2ySqVIec9-e7CU1ilDekzAs2C6460cwpzm54CZZL2Gt5rjHf26yBG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mThvHmqT1yes2bBVdi1x5nQzQ0VxWzLPtItWVhfkLDNEuqEM71nWtgB355e7F-MPx5OLgq3wepS4SNKDVjRaTEUnp85X-psJGz7p3ypbkLOfbMRKQpKs8yLClowA0pQUeVcs3hImXAAQyqZaaidQQfFyZ8oaPn0aEIXuaRki4hPsFfx20r6OX1x66sy6exsLsg1bwptc2K-cEd6MHuPvDFwYEY1gtG2QZn6ofMQmyowXEoGTrKjqXGoSPpIw_8SNj5zZFzSiRezOpsNpCJGSR04tO6Usv93Zf9SmXttbyY3oK2EDAU-m126ev6AyKmAs0MknQ7EbV3NF_Kok5oTWyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=OtR0sECqpWmas0QLAjYa5qMreKz_0hWQ2A6A7nnDCtGNuJzCP5cLCEp_OAz4sBjFZ-EYeZDoneRd6vrGrKOZFYAkKNnzhqDhw30hS4r69MXmy-YKTxaU0SEQvAgsioA6KdLvYa5wv1E6x3FfloOeWZL92FHACroGU5bDUG7XGhzvzd35cIYcPFXdUmrLTTtlQkVEs9bvOrDD6HEpOcN2iMI9flD8Sm0tV05x8NAGXQgrG77ZnRSlSFbJgZjNPfZFC0zUEKGRNQRXMb_n9_tvsyoeXUQQ8QbL2OEKH5-faN6n5PxKuJoyuDneaUy24FBwfT6FzqL1PTT1S7MIrd8XOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=OtR0sECqpWmas0QLAjYa5qMreKz_0hWQ2A6A7nnDCtGNuJzCP5cLCEp_OAz4sBjFZ-EYeZDoneRd6vrGrKOZFYAkKNnzhqDhw30hS4r69MXmy-YKTxaU0SEQvAgsioA6KdLvYa5wv1E6x3FfloOeWZL92FHACroGU5bDUG7XGhzvzd35cIYcPFXdUmrLTTtlQkVEs9bvOrDD6HEpOcN2iMI9flD8Sm0tV05x8NAGXQgrG77ZnRSlSFbJgZjNPfZFC0zUEKGRNQRXMb_n9_tvsyoeXUQQ8QbL2OEKH5-faN6n5PxKuJoyuDneaUy24FBwfT6FzqL1PTT1S7MIrd8XOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=NTVUe10Lr2qHZaOdpdy_V_38v8W45ShPgwmihTtBYbQsHAQnvGjLgybfJfT5ostjBBoSHykKSczMqWoZNu0Tcn-SUFA1rVAiYJgQ-MCO4zfL_5_PdWcwsnYljmnWDtVaIo8e6qKRR-eTJeNDbgJRQL697JOnBrqmXQlodnk8gHfnNw8Ck70Xj_XOe0YiVHkTzaoxfUIE9435i6ct9oJBo764E0ZpLH2LXZRad1ZBr3V5yeL3wQteIeRwRvEnijg66uJ3ATfIBYjLDiCqucwVwxvbK63Pwky_LlSNB29adO_IwhhBhtZ7D_ITfo1mtlyeH6errdHYtdKeb14w6umEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=NTVUe10Lr2qHZaOdpdy_V_38v8W45ShPgwmihTtBYbQsHAQnvGjLgybfJfT5ostjBBoSHykKSczMqWoZNu0Tcn-SUFA1rVAiYJgQ-MCO4zfL_5_PdWcwsnYljmnWDtVaIo8e6qKRR-eTJeNDbgJRQL697JOnBrqmXQlodnk8gHfnNw8Ck70Xj_XOe0YiVHkTzaoxfUIE9435i6ct9oJBo764E0ZpLH2LXZRad1ZBr3V5yeL3wQteIeRwRvEnijg66uJ3ATfIBYjLDiCqucwVwxvbK63Pwky_LlSNB29adO_IwhhBhtZ7D_ITfo1mtlyeH6errdHYtdKeb14w6umEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=AtbcQG2XLKmd5D5MqPTFFMVevLJyZ5p9rtYhartoChinXtI6weqaUQ17CCC2uuHPneBJs8nit-ajlFSIZXv-ZPByLp3ACs-SBFb1dWaslek_uTArBIBYMTB-P5NfsMdWqme_vm-sgyfzxjLMOGHvwXDA1VaXT7yUyPEakeDfznjj7S1fm-x_u86wauwHsBQr8VHsWBBScjuStTse21AcZkMgwTsKh1L3TyZ-2qMdlMoR8Q06lsP2utilXSLCsmMCSlf9iUcQ5bq1g1WiRohBa6fhVz3Tu3EPeVLkdT99D6W4ThQtZXM89QjI6VkX3rzR-tWyYEtcy2aKZGIvtApgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=AtbcQG2XLKmd5D5MqPTFFMVevLJyZ5p9rtYhartoChinXtI6weqaUQ17CCC2uuHPneBJs8nit-ajlFSIZXv-ZPByLp3ACs-SBFb1dWaslek_uTArBIBYMTB-P5NfsMdWqme_vm-sgyfzxjLMOGHvwXDA1VaXT7yUyPEakeDfznjj7S1fm-x_u86wauwHsBQr8VHsWBBScjuStTse21AcZkMgwTsKh1L3TyZ-2qMdlMoR8Q06lsP2utilXSLCsmMCSlf9iUcQ5bq1g1WiRohBa6fhVz3Tu3EPeVLkdT99D6W4ThQtZXM89QjI6VkX3rzR-tWyYEtcy2aKZGIvtApgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-0iJy7IbuYhogtoj9CHdM-iWg5HOG0ZZwaP0Pg4h1Vvc8klu7x0_h2y_GMLrxf74m4IMB8IFe8vLYqn3zFutuV_S-l04oGZNy7d9Ki-3yOKJgTotBEMvFopCPHzBDvSrcd5kTe0Ho1sQBa0CswrhhjoTQBD3pYlj0iGRYKItPTbPleYBx_aQLht2nzrtQx5pF5EcioK-XQ7ft2cxkx-2qeYi0yUKc8ZAeQWwzyZ3WWh5n3Z0u-60FkduGhJQMftOUm3DazRtFJnON2UNCsRAZplfJBSO7Z-HlkeMjg7J8z7I1OpBiW_1JraRyZhfhuHZ_quhHUz35HyoVDbqS9TSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9LnMVG1eHnHwsqGc7kU6JbYXfuZNYyz2ndfppszBdtpmGlSWLYT0oI9LukX1OeRKP1zyiwfzpyIW46gQy8QubyK_AYzTWu6IWTBPENHLWl76-7JabV-mKp9xU9lOWRy-1hiH0cCb8WJQ7ZunV6VaRZg8bexBM7-bAD1bXBeROmAg5z0y5UI4jcdvhlcsh1z4QIDbWh7D5RIpOTWR0qaUuGkY93GWoE2JX5qaVBn6XbUi4PPtFwqGkuNrAB_5oe30QePhZU93Jkp5ee2f_E6qaS_49UhQmG3786n4VCPiFdVW7sf0W2QhObg2HI0Wemt8r8jUjSNb3NJJ6OT_psoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhwNvw4UfDd5ww9VJojGrWrUCYx8J4IiN_QRLFIHFek_NPWDifq0MkozfGgwFNkqA_-bcADXb0SLehOU6n9J6FjrU3RzntpNOJ8Dh-3BaP1oSUHvoDA1qwQzkHuzo8XMkEIcKC36h0mAferyK5Op7bZhCPg5qAdww6fWMR1ORVufMRhC2hG0E0-7WDLI21eHAOz4fQIBnc35_Loo6z_eJ4zkk5v7qqV1VAoZ1r5TFFRmq61OBhqj271ofAS7B6I-fqLNubgopUBjlBpARWNzzq4N1FGhIgCpTqv28Z8chvVWhw_dMosS-mDz7HKeNzFDtMz6tijBqoGS0qEt8vM9Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=qruWFvQija9ZHmLIvaaUoaETuSudzBAEbSYgUqd59vaAjqN2sX9kP85CuqzalmJ2L2fv0EecPvfPCJOAwCEyZQOzx0hnl9rPrtuF0BPPgiWdIgw6BeQ6jPhDiZ0eXaZ89_PrmSW1VRHZiKHm-JPc1hXH987uA2AgEvvHZYNvOXIUZKv0Y8pRKCO8isyR1QRDwTTZ_CGm44O9R3Hs71HYr-hEeENsWL3aThnDeWjN1ZGTNxEhHxJphO9C3ve_p1c8RiyAt-d9M69rxZBkU-RgkyeZUFSRElZkACXXe828EPYBKedLYzhoKIJBWngAZZ9rtm1yYMV2BXUB2TIoTej00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=qruWFvQija9ZHmLIvaaUoaETuSudzBAEbSYgUqd59vaAjqN2sX9kP85CuqzalmJ2L2fv0EecPvfPCJOAwCEyZQOzx0hnl9rPrtuF0BPPgiWdIgw6BeQ6jPhDiZ0eXaZ89_PrmSW1VRHZiKHm-JPc1hXH987uA2AgEvvHZYNvOXIUZKv0Y8pRKCO8isyR1QRDwTTZ_CGm44O9R3Hs71HYr-hEeENsWL3aThnDeWjN1ZGTNxEhHxJphO9C3ve_p1c8RiyAt-d9M69rxZBkU-RgkyeZUFSRElZkACXXe828EPYBKedLYzhoKIJBWngAZZ9rtm1yYMV2BXUB2TIoTej00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcmid3634gEId2-hXKi40KrCj6NaNW1FqoIVp3ZLSsQl9uP6kg6xPpgtA80HhvShbjwP7U9UKZTA-Dj_Wxqmdj6_37Of1CvULAzbcZXeOV671lm7lFgeuLpfY2anK5s3M_eVtqwmPVj0elm3x311HFYC9e61AVndWKqMn7S_9rCw4S-41vCb_oL4woh5q3GNFYPE15qoIRYHH0oOnhaf6Iiu47oqW9wFTCRIYlXZ21_-SuobqL3gZ_6GheicFUZnFWsZYIDSS02Mo3JEHTVZncbqVrf293XgGfo2qbJa1bFulxxez5xFaidldmr-LQmN_4fj-MDGM1LTuSJ5jp4DBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=paq-Fo1q9OjMyjb-5UztmObWkkQSgZyWx3fts6_BW2OqOrlMK4fYexkYkQEJ88imAjcp42q1iCERWbmPA0Jk9IRfTCZJ5BzuFfTJVP-cQBhdE1YPq5G4dPtxmQLSbPaJ_r9cUHjzMPGQFR7L1VekJ63Mfbd2NdxjykFUr9vqSeJTigM7gMqkmWg4FOES3_quL7thQLy3PTm5Pp_PnjrYxwQ2dS6_LRA1JAq8GKsYamkMUTuoessWmIY3FTutgym80qOXn8LXF-0K6cu3n_VjVKNu370YXHKtopAXV9FMgxYqLP_rwH_CeVY2OncOCbYdzXZiFN8XQtD128ZL_d20zzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=paq-Fo1q9OjMyjb-5UztmObWkkQSgZyWx3fts6_BW2OqOrlMK4fYexkYkQEJ88imAjcp42q1iCERWbmPA0Jk9IRfTCZJ5BzuFfTJVP-cQBhdE1YPq5G4dPtxmQLSbPaJ_r9cUHjzMPGQFR7L1VekJ63Mfbd2NdxjykFUr9vqSeJTigM7gMqkmWg4FOES3_quL7thQLy3PTm5Pp_PnjrYxwQ2dS6_LRA1JAq8GKsYamkMUTuoessWmIY3FTutgym80qOXn8LXF-0K6cu3n_VjVKNu370YXHKtopAXV9FMgxYqLP_rwH_CeVY2OncOCbYdzXZiFN8XQtD128ZL_d20zzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBBhTTsQWRDxWg1oWTn0bmJstxDGr97Ka8MrTGgWo7U28UPjqNBDIfvYQ4sEM1r_9He9SBrf0fsxs-tcxcbaZzDsUJeElH71tDjv8hF_2zDGJRklKAHSz-xyMIabuUwCv-P1hxsg_UrbvIIFwo4rtWAiptcOLMaOpQXQXn19NkIW4jJXw_9uZaOW-h3qTl_3TYDTcqJ6Q13zxt501Ahj1p3wb729-suQMKTO1WN9H3u3zTKh7FyZO5xQFojOqwfD256mtvsIOIy-xkjVTRsL5pmdC_RLaXyM-3P5gifsUPTpcl9xxpmpSiEX1O5XxAqp51denN98A8uuAI4O1HheqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=Ggk2ksMK8w-4jeEEpi6OfEYBV2-Ckk-Qqa4lwya9Gp483tELKxLOzv6XeyEv3q9r5cPSv4Biw2Y8yI9HOtUYghsuKI5D7dbPOqCR-iLzz3gCkRVn6DxpYOzMfxc5f5yCToAn9qDzHIa7oOkRYeSbQZPJXCZOtXluF5qrX8sNUdBtbqMr7vfRJg7TQVQQnJdiyiwNY4Uaro_gAddeCX0kWYIMq2kPvNYJXIqn_XmeqR3cUUlLvP2hE6cM6D7bB18ygjjT1wLLLWp2tIFuk1oUec72W_r1I9ocNZauhMo_DzwB8t9KxX6dbD_6WWEFoaeON_4tN8rGPAF66-LvfhfVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=Ggk2ksMK8w-4jeEEpi6OfEYBV2-Ckk-Qqa4lwya9Gp483tELKxLOzv6XeyEv3q9r5cPSv4Biw2Y8yI9HOtUYghsuKI5D7dbPOqCR-iLzz3gCkRVn6DxpYOzMfxc5f5yCToAn9qDzHIa7oOkRYeSbQZPJXCZOtXluF5qrX8sNUdBtbqMr7vfRJg7TQVQQnJdiyiwNY4Uaro_gAddeCX0kWYIMq2kPvNYJXIqn_XmeqR3cUUlLvP2hE6cM6D7bB18ygjjT1wLLLWp2tIFuk1oUec72W_r1I9ocNZauhMo_DzwB8t9KxX6dbD_6WWEFoaeON_4tN8rGPAF66-LvfhfVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_bvR1NAVC0Gb7UXSbuakCIIk5KEv8vi0yITLLEUcnlOXHHN62RExv3Awadmy7QJiTi9mkEuN9Vt04SEUZVfX72okvI2kFLkHWX0f0gdIQvzfL-7q5Gf12K-XvpIp2aDioOeHxRPY1VO0RXoYWCipSm6FP52fUy04QaUUix10Aqo9fu3iNBJx7IA14_fTTXBay3I2LkqsYvZZfe7jozA32ad6akREGFUohEOooSG-YEBDPP9VT6mubRyhotvev-I5sTNJdM6Q-lUvHBO-aXB6osJIluxBhBlcUbico-eY1sFQvvRuUOpXmD9moJbpaJDZN8xMeknVVAvqbscLtDob2tM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_bvR1NAVC0Gb7UXSbuakCIIk5KEv8vi0yITLLEUcnlOXHHN62RExv3Awadmy7QJiTi9mkEuN9Vt04SEUZVfX72okvI2kFLkHWX0f0gdIQvzfL-7q5Gf12K-XvpIp2aDioOeHxRPY1VO0RXoYWCipSm6FP52fUy04QaUUix10Aqo9fu3iNBJx7IA14_fTTXBay3I2LkqsYvZZfe7jozA32ad6akREGFUohEOooSG-YEBDPP9VT6mubRyhotvev-I5sTNJdM6Q-lUvHBO-aXB6osJIluxBhBlcUbico-eY1sFQvvRuUOpXmD9moJbpaJDZN8xMeknVVAvqbscLtDob2tM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=pLABO3Z9HxEq10zdz9mWIpdDX7hnkhzzw3FRl25VSC6afo9dAAjlVGrEP9ndI0Z1Irpd-XPXSBJtE6hd97fx-6RwK5iT5ajuY3Dg8vSTnrfaZNvJ6BhUolT2sfyuZlH7adRoQ6QV4CGjV6q9C1I0oDBkUd7bRQLYRQ8qQaqK6keXFAwXgEZBHKK5Lmue9wW6gAI7XsJifEq2iAp9JWMrx6KGTmwYmC2LQC1o-4WUlrLeTavykIUWZ6qwZEC_7T2YkmhnQji2MIEAZZE6pSYlZmPrkIbxsJ2YQ-KJysbftO4-0I8R8Avks0KkjVGBBscJUPXiC_lP8Xd4PQ6yTJMjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=pLABO3Z9HxEq10zdz9mWIpdDX7hnkhzzw3FRl25VSC6afo9dAAjlVGrEP9ndI0Z1Irpd-XPXSBJtE6hd97fx-6RwK5iT5ajuY3Dg8vSTnrfaZNvJ6BhUolT2sfyuZlH7adRoQ6QV4CGjV6q9C1I0oDBkUd7bRQLYRQ8qQaqK6keXFAwXgEZBHKK5Lmue9wW6gAI7XsJifEq2iAp9JWMrx6KGTmwYmC2LQC1o-4WUlrLeTavykIUWZ6qwZEC_7T2YkmhnQji2MIEAZZE6pSYlZmPrkIbxsJ2YQ-KJysbftO4-0I8R8Avks0KkjVGBBscJUPXiC_lP8Xd4PQ6yTJMjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=T2sR4xr465sxwj5CadGE_ARgMb-XWtC8G3LdvRjkSZWDV9-7S3BGCXlzQ1wnhmKccUkDppYOGCi3ZX9rfnr9JA_WCBNiY43K58VWeDHVdYQbWlLU_MQ4bdVsEIvKtx1PSBiEO-ffff8T51mbUxZinHYX3yYq17FyDuznvwi50FRXlZ7oL8wKjCQ38Y9zwR9Nw7V2spaTnNWCEyTsAprWZmljcdCV14Ji5Avip9JDLaFjqNG2ALKMJYTN_LcIrUWXudVKSCceyVTrPA45L3oVm4h-6uMzEzvuNi0vF8Ir2YaXHiepbRoPyQp2PlzXZqr6JaAv6WB4H1w7PQljnV3stA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=T2sR4xr465sxwj5CadGE_ARgMb-XWtC8G3LdvRjkSZWDV9-7S3BGCXlzQ1wnhmKccUkDppYOGCi3ZX9rfnr9JA_WCBNiY43K58VWeDHVdYQbWlLU_MQ4bdVsEIvKtx1PSBiEO-ffff8T51mbUxZinHYX3yYq17FyDuznvwi50FRXlZ7oL8wKjCQ38Y9zwR9Nw7V2spaTnNWCEyTsAprWZmljcdCV14Ji5Avip9JDLaFjqNG2ALKMJYTN_LcIrUWXudVKSCceyVTrPA45L3oVm4h-6uMzEzvuNi0vF8Ir2YaXHiepbRoPyQp2PlzXZqr6JaAv6WB4H1w7PQljnV3stA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRVvma4bF5B-6eaWlcJxXMII7HngN6F19Oc_hJftSNI7EHTTLEjA4ZTpYVymEbrrpJLGOsTPByiThfC0gow012kl2lxOTofZ_lpK3S76ZTY_E3HmNGU7rfbgGz3ShL5OflONuRUrhsvRvefnyflwpvY0ZHsz4uGCREN1aV30KjD7cKiWIXo_fID2njdSFNRcmgRqqNoO7IXmPfcZKg9t4nIYDriSdYwHyvZUHq6B9DfFqq3b2FmWvptlaIVz-YFECbnCRBqye3hRb3hoUHZJY9Poe8y75Ua9lDQOoc7KpFBed-K1QlWPjji42ndhfr4GT-PmMwEYStcakRVjkkNePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=AX4e2e8ilXrXH7gLufTq9pmL7BOM0jHI2vkW8-5_wu1g9k5q9Ee7F4SoZr-4yLyRBz7kAS7uAG7xpXZoaJYfrcZGPaBuuaFtyt5BL_W-PwwsXAlg7Nb8fmmFixqxoBuJBVyIrw0na2YqrpIg3xKx0FfXiukKQp8rs--KOT-wwAz3vYiVVzOsIjPr9gwWOfv4OFoBdS45kCA7mUoLxqgP7VB74T70NjUV45lcmdxm5IHM3V19ZDBpaNe-69tJzNlCQH2c76Y02jN7m5U2g7Iw6HojsEXKCZXSUHV5qlhtch-u94VkXhLkRZYtMEPeg1Mu4C2cQSAcFKqxdXp5HbQVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=AX4e2e8ilXrXH7gLufTq9pmL7BOM0jHI2vkW8-5_wu1g9k5q9Ee7F4SoZr-4yLyRBz7kAS7uAG7xpXZoaJYfrcZGPaBuuaFtyt5BL_W-PwwsXAlg7Nb8fmmFixqxoBuJBVyIrw0na2YqrpIg3xKx0FfXiukKQp8rs--KOT-wwAz3vYiVVzOsIjPr9gwWOfv4OFoBdS45kCA7mUoLxqgP7VB74T70NjUV45lcmdxm5IHM3V19ZDBpaNe-69tJzNlCQH2c76Y02jN7m5U2g7Iw6HojsEXKCZXSUHV5qlhtch-u94VkXhLkRZYtMEPeg1Mu4C2cQSAcFKqxdXp5HbQVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=rS_NvAAF5vmXxwrSKXN5P4ATESJ3tb8HPafmwWwDroyTDhDchjo17o47oe2_9n90V14nbYJn9sncNgvv5YCKxQ2VOeQMZC3-xtRVlpJUtTvR-TzyrQIRB4JRPjDDcMjse7Tpwg_FN6qUrnQBIVUwaVWlE4HKowLg3qlcFJDEcD2v2KGQSfsGStYyaFDNsqx-bNJ9NGtEhxbBlRNBTpj0_0Vx6jx-GFLOp6cSGNvdDu4gXcROHT7v4wQuD9gXgfUiSOKqpfbHA1potDMBiy1WN7UmBuaQcEPBfoTRzXPtFDHfy5Iz4g5PLW-eC8MhnCZjmhdyEBrj7Pp83eXb7rJgkLCvF7sd0Cm73wi3Vr8oaG64kSxSE2be0PItuGACH6hIsbjOsUAht6THEf9spzBTpAcVDFqkhZ3IkfjcgjkFie_osFRlce4yJkp4ZYi5_B77vJOM_AHNvGkJ9W153LhlZ23lRqr7T8SyRRrCb656CiuK98AGJhpGep3diSBgmrg8glMahDqTCSpg0r2T-RaG4vi2G64622cBz9jm4v2ImJmChfyJwDb-9TErcuBDJG36o6T_FuTQbZKJP7rryEfDwDSj_HX6yOCaBVDF1wXbO_HJGPLKbbhmoxJHzKPul8z2Jx75hVvZi4Gk-iJBf9E5sLJUyc5Cx_K_yzxDrqnaJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=rS_NvAAF5vmXxwrSKXN5P4ATESJ3tb8HPafmwWwDroyTDhDchjo17o47oe2_9n90V14nbYJn9sncNgvv5YCKxQ2VOeQMZC3-xtRVlpJUtTvR-TzyrQIRB4JRPjDDcMjse7Tpwg_FN6qUrnQBIVUwaVWlE4HKowLg3qlcFJDEcD2v2KGQSfsGStYyaFDNsqx-bNJ9NGtEhxbBlRNBTpj0_0Vx6jx-GFLOp6cSGNvdDu4gXcROHT7v4wQuD9gXgfUiSOKqpfbHA1potDMBiy1WN7UmBuaQcEPBfoTRzXPtFDHfy5Iz4g5PLW-eC8MhnCZjmhdyEBrj7Pp83eXb7rJgkLCvF7sd0Cm73wi3Vr8oaG64kSxSE2be0PItuGACH6hIsbjOsUAht6THEf9spzBTpAcVDFqkhZ3IkfjcgjkFie_osFRlce4yJkp4ZYi5_B77vJOM_AHNvGkJ9W153LhlZ23lRqr7T8SyRRrCb656CiuK98AGJhpGep3diSBgmrg8glMahDqTCSpg0r2T-RaG4vi2G64622cBz9jm4v2ImJmChfyJwDb-9TErcuBDJG36o6T_FuTQbZKJP7rryEfDwDSj_HX6yOCaBVDF1wXbO_HJGPLKbbhmoxJHzKPul8z2Jx75hVvZi4Gk-iJBf9E5sLJUyc5Cx_K_yzxDrqnaJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=Es2tMK0DSyoUjmpbeETbMabaIN2zxsapRMnSqe_5NBLCCFlYUbS5fhG_dN-1kl9fno9OysTyFoYD79bCAw_rjUg_oQuNOLWtsYRa80YCAnim2dXnndTKtUaMqXRrhcvGhxrxXmS4k9t-Yjk_a38yDmDy6lDtBirR1EEUD7K2OuV-lwpujsqMH9kzLpITxigs84icYcaqSjeKOWPJzmMHoedd2ScEd3an3RXG3EPdYgqesDJGd9n2KB3kuG11y0jjth3o-Dbnsr_m7PKKiPStOUq77c_NDBzQGDU_NrTd_LQSg60ZTXLJLWPWs-q8P00V504GnGJgCHUrPzpH5dRv3bi9VmBxyECQC9BcEFo6MQyj91CpWpBisZT-GS5IfcAUSLe21F_i1I12qgaN1AVUkaxYuCX-l-NSbaHatr4TWmqYr4VqYjVl7hwGF7vqXY4XoDJzSLEk7elF8rdcEgTO1z8_SPXN3KBfoHDUl1JJzW7XR6P6KnIwfa_yInETNshjvmIYqIT6RqIh_pTEUMjEt-TXmjkDFkHK0W9_GkIf14YHtQX5nJXhlYo9p2xNx62Z00BCTTPwZZ_46ANoO46fwaU2s_nBjzyklTzfF6yi8xj-Eav_jfuGZiOAyXxEtD85c3h16aUdiX4a27tSHo5WedgHD2Fr5tIGZT6sVSJLlrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=Es2tMK0DSyoUjmpbeETbMabaIN2zxsapRMnSqe_5NBLCCFlYUbS5fhG_dN-1kl9fno9OysTyFoYD79bCAw_rjUg_oQuNOLWtsYRa80YCAnim2dXnndTKtUaMqXRrhcvGhxrxXmS4k9t-Yjk_a38yDmDy6lDtBirR1EEUD7K2OuV-lwpujsqMH9kzLpITxigs84icYcaqSjeKOWPJzmMHoedd2ScEd3an3RXG3EPdYgqesDJGd9n2KB3kuG11y0jjth3o-Dbnsr_m7PKKiPStOUq77c_NDBzQGDU_NrTd_LQSg60ZTXLJLWPWs-q8P00V504GnGJgCHUrPzpH5dRv3bi9VmBxyECQC9BcEFo6MQyj91CpWpBisZT-GS5IfcAUSLe21F_i1I12qgaN1AVUkaxYuCX-l-NSbaHatr4TWmqYr4VqYjVl7hwGF7vqXY4XoDJzSLEk7elF8rdcEgTO1z8_SPXN3KBfoHDUl1JJzW7XR6P6KnIwfa_yInETNshjvmIYqIT6RqIh_pTEUMjEt-TXmjkDFkHK0W9_GkIf14YHtQX5nJXhlYo9p2xNx62Z00BCTTPwZZ_46ANoO46fwaU2s_nBjzyklTzfF6yi8xj-Eav_jfuGZiOAyXxEtD85c3h16aUdiX4a27tSHo5WedgHD2Fr5tIGZT6sVSJLlrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA09jUYY046Dj8YLfB3nLQST0bXakdIUKqngTTsHh3SK5UqrcBu9MXY1RguZ-IxlOGcJG30jEEMx_1-JAgCeAB5UGsyMQXRlHISVvF33J8ifGCaCnY0WqXpfJ-B-oHb4uZS21lRH0zDuI5w0Z1jM-4zFwIgRRAQJJFzHWREBj_Vf8mjmKkCxbbzpIgxeqFTZzoXvWdLU1C-XHJiG5ZmUgdcEapSQQcZP7Iivk0u518pA6XxAfpeHUzrTGzLe9CG8pSN89cUd9E4lAoGq6G4wNnIUUzAgxU4o-rMS_coFVUlMt2Yx4iJuycVkTCWTDvHhR9rbwqWVzOi-cePSw1rpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujHKJL6ZA4EH_rHoOOD1G9vEwTYA22rYWMh0hKizY4H63VeOFAqGkxKWtDmcRQ4hme_l2NLYsu0RXoZVZZMw-0dvDe-xnjmWXD50IWH0OZRZBY_2YCPZ3xyRt5ndWFnnOvyWApoxXZ4GLXTyqYErvcQkK4GCbQznv13JatSZTZXC0kFfhPZeJ37iNJqQT6Y5u4OENsxD5iNy4bHPIDyaG5No_KSePEzoSFH8bksScUrTBV1Mh_f04VW7fr7olhQcv_Opho5_IxnwECpQe8Ltl7deNmxzpTF-i7PFbMHYvRhE4iYZ_JhB1Aqr-frEg_AxmIyX_VOC7eVsnVweiiJ0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP2aj-gLWFMMRV3wK6hlcv3dfZcxaOL8VHsC8NF1E2Z5lQJIlwA8rks8IAc8QVTCRZoawVSVT2zK--0Aq2oEyvEywjZUHuWLl-oNxPHrr4CfPU0iQ7sImXxTQSBWBOl3mik-bB8e0RD-HH-Rqgz9rs5MmGdA7VNbwGGh1vH0EhB5d-Qne1vuNNoSVxk1I2jqwaRVRMof-9WFrN1NA6BgPxb3qAdvPWJpWVaozaujxlYWyjkAotfubpdUdXSEI581VnlUwt_Pam9GEpIzYMW9HtcFFicaOaeodBDnq7ysFIpWtChc-OQRrKeeYKSZzIGlELYGxYBfrP3HA2AMWLQquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=hqxZKpTuMIkxysBdqpg7NE41AHIJ0GYCF5F93Yq4OiMJx4KDnuKPaSZbsGtG2jutLS6dLHGRrm9-G_cTy7oqSRjorXm_zE2Pv2wt_PLaoNjqUi8YfEel5ZKXr1qCwsQZBw0NyfjVD5vIPh3N78PTaxMHdbWjgbYudojvnM2KHmS2UAK1FoiTLm98KCO7pcwDy5HzigFnbRa6f1k8AGIevbz3O5tNWAgQhQxckG1Gv3ktNNF_kEaXzU53eFGxjTJ1Q-ZAeEqN8GleN_gHHH-Q35D9mHFOGRXPxYU1IyZ1vU5KCavtKvpQrbw9z_EaBmoWEXEEK4O-pUvWAB8GPahKMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=hqxZKpTuMIkxysBdqpg7NE41AHIJ0GYCF5F93Yq4OiMJx4KDnuKPaSZbsGtG2jutLS6dLHGRrm9-G_cTy7oqSRjorXm_zE2Pv2wt_PLaoNjqUi8YfEel5ZKXr1qCwsQZBw0NyfjVD5vIPh3N78PTaxMHdbWjgbYudojvnM2KHmS2UAK1FoiTLm98KCO7pcwDy5HzigFnbRa6f1k8AGIevbz3O5tNWAgQhQxckG1Gv3ktNNF_kEaXzU53eFGxjTJ1Q-ZAeEqN8GleN_gHHH-Q35D9mHFOGRXPxYU1IyZ1vU5KCavtKvpQrbw9z_EaBmoWEXEEK4O-pUvWAB8GPahKMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ufjs2bjKNj2GFCOP-PyZqRKCJvo6OPepRvhQRAUV8mOUcGoXZJFFSn245FicghIz07KJGdmhqNGKCbXX4f-CaDBPtHRsGiC71t5wfqT8NrKT_Wfq6PR_0d2mLQmCopXLlmvkO5lDS4JBM82geBWQP2fv7RcqQ3ZPronqCrs2Qvvck6fUFeU6GAvJxwLYH6egWmj-hJmQp3fltb-BXzUNt5O-jUgxQI80DzLPqBXo6_ON2zz1mVMttgdHgFZBTZNfGdVrkmYWR_CEc3GNAi9sCf75nR8dugPNnlb3E7OFtuibJry18KcAv33U-O3KYU0p3aKtk84PPd05eFDVWoukzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ufjs2bjKNj2GFCOP-PyZqRKCJvo6OPepRvhQRAUV8mOUcGoXZJFFSn245FicghIz07KJGdmhqNGKCbXX4f-CaDBPtHRsGiC71t5wfqT8NrKT_Wfq6PR_0d2mLQmCopXLlmvkO5lDS4JBM82geBWQP2fv7RcqQ3ZPronqCrs2Qvvck6fUFeU6GAvJxwLYH6egWmj-hJmQp3fltb-BXzUNt5O-jUgxQI80DzLPqBXo6_ON2zz1mVMttgdHgFZBTZNfGdVrkmYWR_CEc3GNAi9sCf75nR8dugPNnlb3E7OFtuibJry18KcAv33U-O3KYU0p3aKtk84PPd05eFDVWoukzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnLhr3ZnzamHxaDo6YxrZGl7jBbf0EJGMALiw8ukNZyNlXMQ5gcKuX9zmbzMknDb_wTn4p0kA_NIe093IuqqcvY5JFURykYPY5tAUGuhBZKq9nxlcRSDTzpERBKHmej2KOOOfNk58Ql3H8ASIwUMSn3ANlxKFjr6RI32JwzdwONJCWW0VTxMGczxEKfVpeUkyDT8TQnrB-c0I1wsWuBgaaTfu7hWbIzJ9eQNqHvMk4G5W6cGn7-rSfl9oMxllN1Iiu50RIkR2QCIxEPUTmU_LUmSsbpM_fe3p4YDm8vVzpeL2ZuplfQRtm_VuXaxn46AJDzspHHFCiivvD86DxyM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSkh3w--UgoeRxIBQQJIZjRdKFHTqSF6U3wt3hfBftozG7C94JCfegs5M8UVGpeXNuw24GewFZtdKdCcSxjgfERHY9DbkLcsFYzVq_irREr5_Dmqr3xwFNiTfpvZwFWMG-OyNMxgI6CL99BHm-n184AE9Ole-9R2KDJ7pxyLh7GCJHBg0lebXIysnNU31mxVvSxzw8wTz1HgovuHTRLCXZOu7bXAuYRu3ldPOVIFywuDC7eJ-mssV6MfpXRfjccKmbpejycHnXGtpDG4NvpL_plDWLYROmUk0ssoSSWDd1is3_pYa8NdK1aXNA6TXKJpVdMFvLaxOpUT2vPQ1kdigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9cHlV7uq56tSz_Wgd9uV8bKXPVAO2jcu36Hz6AgehtxG-oqJuBHtKd-ny8Ss--dTPv7cQQOVkO4iOxLEBOGG_yqnMbUAzKkyvJFVMtIClK-_vPk1sHLuj_GSw_nD82mb2ijAGkcQ1mnACN2IBQOtZHKjcA8WUt-ffsiYYnHfMRmy_03mbWlz0UC5QWfXuv8qeiTwhKiQv3_KnKsVjhgASXFG3Yr4Ixz-AQtlC6AY073RxTj6hSqy0ifd6qy2BhRPqVoBDnq7sqtImtFkpL7yCkVv1dMx_mmwvVt_O9AIGmkutqC__LSnRvN964m90OmCJi_9pPQOD1b1HrV-Q-mIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=geKyoNDtUyi8ZxeW19pbq3EDOZbKi0wSf3S6_u9WyW_ysSgT2WtQSiANyaioTn90qy7paiE71_ysqVJPtFDc2L2DjAoAQmLSIV5CzSPTsqAMfV6J1pTMlmpZ5WbdSgnfVc9LH-EvoTd3udYXGaJAXV-octk86ZNgqN7DhUZZRPWdQLAVSaZYKIYFU2XkCgkW_gk4SlhrJrBxkEX2fzLm-vOSrjd2IYEreharAmecqxjxKokD77DiPQM01xewpNfk1248UmKmGMyKqBUHx_oa4KwL2H6SRb0qNfFj9WfImiWCQwmq178SgFEmD_-2wlKb_xFq-FwjLKeLLjGlUcWuHlyVUnR1wF90-g7hgZZOUUwKFwvFaAY-OnD1vIDJ7mOe-Yp5tIiBQhRr57S9vtInJVfuqFcyoZCHFjfmTt5SF9sRxVfvWWbhWmrL0whpptOLLmgFaYQn0rZAuPPqil58sfWLemF6zJTuRj46K9WxK0WQfh23hieQs8YWE5pDiesZ2Pnh6hX88-eq7xnh3ajkg7pzk7dVfRI82pKvM68oP3utnO2mhQPeK-IiT8vaul1D8RAjOdxIpe1BPjM_uI2mBVCj086CgSXTwXuZpER5S0PPIyWFJvbaEIalMN2xQia-4VKHIP2QJ40mKdjEx5Eg27Tptz3V8jkJUtlEtgj7PbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=geKyoNDtUyi8ZxeW19pbq3EDOZbKi0wSf3S6_u9WyW_ysSgT2WtQSiANyaioTn90qy7paiE71_ysqVJPtFDc2L2DjAoAQmLSIV5CzSPTsqAMfV6J1pTMlmpZ5WbdSgnfVc9LH-EvoTd3udYXGaJAXV-octk86ZNgqN7DhUZZRPWdQLAVSaZYKIYFU2XkCgkW_gk4SlhrJrBxkEX2fzLm-vOSrjd2IYEreharAmecqxjxKokD77DiPQM01xewpNfk1248UmKmGMyKqBUHx_oa4KwL2H6SRb0qNfFj9WfImiWCQwmq178SgFEmD_-2wlKb_xFq-FwjLKeLLjGlUcWuHlyVUnR1wF90-g7hgZZOUUwKFwvFaAY-OnD1vIDJ7mOe-Yp5tIiBQhRr57S9vtInJVfuqFcyoZCHFjfmTt5SF9sRxVfvWWbhWmrL0whpptOLLmgFaYQn0rZAuPPqil58sfWLemF6zJTuRj46K9WxK0WQfh23hieQs8YWE5pDiesZ2Pnh6hX88-eq7xnh3ajkg7pzk7dVfRI82pKvM68oP3utnO2mhQPeK-IiT8vaul1D8RAjOdxIpe1BPjM_uI2mBVCj086CgSXTwXuZpER5S0PPIyWFJvbaEIalMN2xQia-4VKHIP2QJ40mKdjEx5Eg27Tptz3V8jkJUtlEtgj7PbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhtdsyaSUA2LZtRydTPIad8jdy22-qbRr4i1l9Rv7UQvD76EjBvjB5aryqfd0InvoYNNao1vP8JnQW09Dscn-1lS2sxUQAozr4L_JfqZX4GuQC59l5igcynAycTLJ2kj24Wq-aG7FR8Xif5ocnf_5JWL1BFERyg8Hej8AVO5EYvBqn6ZOcCCCYPv2Euc0fgsl4_Yjs3Vxt-2-qNRFhjZQWtSHEqXYHm7DuVnUQQgG-pazIVzjfxvGapoHjP9TIDLdIth2YyvGmCo9v9D9I7LGwK6d9n9ua6XMCr3OIiB5m3HUBgFwyE9IFUYPd-zV-ymRaa6dDizvkBGgZwdZvfhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=bWHZK6yeDQCbf-EMLqmRzoz4PnCcLwXlPaFmfyEcoxK7wYQyBSsEV-3St-cWlGsnUuSL4J1ELQlN2i9ptnMD-lmstpx32fhFzpXyJ2JmRMlKx5XBJ8CcIANlX5Xit7uBsRiJ6bIPYVnyZW_6XiLurPs8pp2p0a7Ig4zqQcEVs38jLaWRXVCeSaGVNPLHOoIFa17n2Axa24mYz9fFyTWSFgyXUUwchHkpevBd23fR0ZaXNH1AoGKE3c3wI66zm2FaE8eHxp7zYqQDVQE28o0P_GitHdxYdiNWtPrIMGpwxwb0-872dkeUm5ST-zUN4GJptx9uSdKIs0_K82UxK44z1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=bWHZK6yeDQCbf-EMLqmRzoz4PnCcLwXlPaFmfyEcoxK7wYQyBSsEV-3St-cWlGsnUuSL4J1ELQlN2i9ptnMD-lmstpx32fhFzpXyJ2JmRMlKx5XBJ8CcIANlX5Xit7uBsRiJ6bIPYVnyZW_6XiLurPs8pp2p0a7Ig4zqQcEVs38jLaWRXVCeSaGVNPLHOoIFa17n2Axa24mYz9fFyTWSFgyXUUwchHkpevBd23fR0ZaXNH1AoGKE3c3wI66zm2FaE8eHxp7zYqQDVQE28o0P_GitHdxYdiNWtPrIMGpwxwb0-872dkeUm5ST-zUN4GJptx9uSdKIs0_K82UxK44z1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlkIPtcp5fPLVHvfWmUczmrllXQNrkehRYr2lX2a69xvfdnBjKeFCPKGKbqh1gp0XF4agbzkkLLdAkJog5_AxlgnMJA99EAl0GU5Dufases-kjMaZ2dwoLKH5qIjLtW2gKN1OARpz8SvMjBRId9XrFt-FPM4qvvuYqcP26LyCqULaGW_Asi1sRvlfe4tM1mtaPW7VOxLDnyNG041aoffOEnHUHtenmFxB2e81LRyfjiUOiIVeod02xEms0QYc8LbHtOILpewJHgvnnE6WqRvS8N1vGNTwY6IpFTHvBsXknEJCMEfB7QVQ6rS6JjMvhJvtp5oR0pUVbcypCfK88YsSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lobGsXxAV7QrVypMGE0cxi0IsIstTIfJVC0YBoPKqPWrm9A2v-wX3FFL3XdAAPPSsouCVUwcPzoCB1xQbRWm_prCLIj2t-zcmmALXE2GUrndi0vK7ypBs-oEBaruEz__uCB8HlI7--6LI39aufIJI00CQMDZ2-lUQ3gC7eG9Co3O30etJeMtemqxHjKHb0a19wHvLn_epJzWfxlYDEClCRGRHnnzDpHYDYZhmU2DWqO1m-ezNV4kqsdvby_TITH6ujhvQdMZKwXz4C8ov1I5iV2tMPEK27YWGxBmuS5tgtdhPiiqF7A0l2pZpz9pTzgetqgevpKrU6DHFkSSCIAM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VWCJl6yYLNFvNrsaypIXqJS_vjgWtOG5dakILENCbzn09-n_0JJGI6yLgCXTU9FCygHoqfMuegDppF1EDwGItO0OhxMacsQQgZQOdTOiOcndO5L_G5DoNHcAO8if3-MrwWZmKA5oko8jLyvmY8a4jJyOUur3Yx6wwteyE_h-jmKDYD6y2TJz6IHlJPpPtg9LReGW-USkkJjW1TCJITEEM-5NrjURQy4shH2na_B6hBtjBKSwIuXUeNUw4D3rFG1Q3TS_jIws7PbwX8nFZoAn5S-7DZSHuuwtHaFJsSHEVlKctUhBbIgcFaxXQ7_2UIcRiKzhwUB1Q70U5p_L2aQpng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=TM_ZSxnI_pc9L6iBfI974dYYbJrzV_f2gHVPIkG-5tY8yHsQ7TcjXj93HHKDNzluKpuDSsxa6dix3PC8t9EVBFOQMVl5P5lT7aX37B4nxDP0awA_o6SBZxGSA3ErehBi7Aa6sYMX1OBVBtTZRjnpQtuYHlDvSR6gB1hHrLJh_LWaLa6Hggoqp-aGOqF9bfEBFAq_PyjHqciXIzXWWFem8NgW_5J5BK4NeUf8jtxjZO6qsDJmiUNrLXnn5M2j-HLVx8zEc2d7Uwyo0ASDEYrXcyHGek8D6jb7VUqyDNwA7p4RXvUk05eLwPX2Z6cHfFK78GP1FjsS22lXYyviO6QagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=TM_ZSxnI_pc9L6iBfI974dYYbJrzV_f2gHVPIkG-5tY8yHsQ7TcjXj93HHKDNzluKpuDSsxa6dix3PC8t9EVBFOQMVl5P5lT7aX37B4nxDP0awA_o6SBZxGSA3ErehBi7Aa6sYMX1OBVBtTZRjnpQtuYHlDvSR6gB1hHrLJh_LWaLa6Hggoqp-aGOqF9bfEBFAq_PyjHqciXIzXWWFem8NgW_5J5BK4NeUf8jtxjZO6qsDJmiUNrLXnn5M2j-HLVx8zEc2d7Uwyo0ASDEYrXcyHGek8D6jb7VUqyDNwA7p4RXvUk05eLwPX2Z6cHfFK78GP1FjsS22lXYyviO6QagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyZ3S_Nd_BtSw4eWqjrHyet6G-5h57uby3sK9zYcZ18I5rOxl6jHy2c1w68El0dtG_SPjzXuKOHG-Jwm5--JSS9EHYLqCSrAxH4QBO4kJmANy9qJzLn3nvOst7JjGPF5KvWI0qkh-iMJasmxNm5tr5wcs-jp4u0q7nsDTWXAi2K0qRUXWKe3OnWZn3UlYbNJWnTigKoizh2v914r4ZR4VXxhLa4ogLrqTjOmySpyiRC29yLw-5gPgjw9Ox9iidFEI_ynwxPlkPKL-pDygxs7xcPvhSKjKL7r8mTh--TwGyw2GYdhNkyPgxTUOVpyHzwRqqq5QC4A3IH96gDl_zgBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBG9FvtOKZcuBOr-BsognSDivQeOjZf6LGih1cdWEX50nCjNAO_CYCxEIkGfOFBdSw1D3_UMmR6PdnsX64XRshYzTFCo5AB0tgv3XweHWqbMzwa9N9tBp3VFKBstAon6RxG5QN6i8PQNmcQEIz4K73zFt2InP221XD4bP8gXvOSGoQZHIg10FLf0EE8kxkU3DMKhFS-iBT6RGAtznZ0XJ6k9M0UJqVtb_AHIxUeKnE5m4oVnVTkqS9ixY-lskoZnVOE97Ml4a0bJre496u3HzBUvwLdi5nETlQn1Rxf9aXEkqdUNmPMRwOhPKu196E0Uw-Xx3uzYMjMaPe3t_5S8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_QvvydyKW8zCiLHySsMrPvvo9gEFlkyMWxXr1kc0e9wdFJNUn5ht9UTt850gItqJZ8YWSclupiMDES2ujsKSpMrJe7fovk-vDHWvXAcYB3PT9jYKZlMUKYq-K_6gzMMHJdBwNN5gsT5zDlggUENNcrmmQjnT593k-HjtPkQ8N4i5XmB8ge4n27RNT0uyriF9KF3QTLNco3DEPPvv79CBxF5pWhHQflpCdnQKU3NZZojTOD1d28gmGKaVHJ9EgK14_nTj2OBXnR6hnAE2LTj3szg-_dxYFFTfm3SbO_H619JKSR7cU9fMG0XqAQ_7a3HkCRA0lszgbb9RBQ0OQbLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ap4L8GKqZ3F6t1vQATGb_xtJlv5st2Ebr7EixCGs5lR6eCtEy4Ay9FwiyvhpaePx4a1f7ym432fyxbomdo1Xx3x0gMR6AqECZdXbpj3ybMdSNEbpp1swhp_j35lEYsVElI5N7F5tPa8PW0aUi8O146bhjsleFAjgpOlkSBkk4mA2p_OisZ7erGjECnbPzsx4MjH7Ncq4WPu9kXtcbvCuoVzoGKR6RFMoekRES0MImUbwMrYjl-bwGHr2Ui7L7avHRklzepFhkjYl62qsnyEISx1g6rcZUQZNegN7d32wRiywkkZW8p6bJGm-eH6vyQi-wFBOXsXjVtjS2froLQtTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4cU4cJzAwB9uPUY2kfV8Nmon0JZ0B0r50u6yCnRNHZ6CuNXZzSIfGZkcIVdyVSo0Uc94lFw4Gbwa9qmMGhxbPCTwp8EhaOsU_SLVHURDck1iVOqzMV0Fv4978rfv652kLxT8mWyWCbSIfSlZ7dBSvsc3DzYd1qfIhfd_jDXptXFts04g2lgVxUxSWf9QozuVLv2RkzjCcd4I3o7gibhtKYxg-2tc5H1ztiJnZnoTg1cQz1aMF2_HTpfKj9ygHOrNsYqT81NcHy43KaWc_qSwRK3YOVkn_2Q2fnVP7q-6GVGdzFEfOytUmGmApWmpXylZxjz6QTd_kLV2XouGaO0aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7EOYSkOeguSXDSOAsElodkJr82uNOTuQEsYNJtEWWYnxZxywAecqa7RQlCevG0w8A6pE_Ljq_b7DB1Tlyz0A3acDd-_NSzKSNZnrNrbA97CQjbB6YlTS1HceGfPpZtMjqaJYL4GVl3OuhMzQyZjFfa9V3RdhZp816PyMRKhWPyCYFk5_YwMjF0KuRI2CYqwJfgBWut_wszZEzcin5E8Zm2wEpylCMSDN6tsDNHg2cO2C9VX1u9vfXNHTSy5jSMifweBmRzjdL6HO_lqwFaAQjzZli9OX4t1st7AUge888KKDWCF54E_Dx0w_wAF98H7IRc0Fb4eC5k6wH_9msQtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Odsk9wwmbJqMaSBTkyUygsss-0NocAxTgApjudaMJHNnlNHFyFOArtg-j8MMcp5-oBKkjm4idmcT6b-uGMs9F-L3uRD73DqE5YEFuZadtmUTer5LEK5aEUpyAyMTAoPfWMF2aVreKFSZ0k7XgkMBtQS8yOa8JXlzEF1se_mYyE-fxyZ993WJYHGK4jv1qWIxnh4ylPTV0VScZaGiwTLXZt1usnrdsq4afCDF3vgkU_9bmP33TVLiXSHwLaqeOBsMREL5RDCAHtO_kC3CJFAhnyZe3gatITiPKihFQp8RUiltC9nPKXBC5K2uG-gzdWpou9KdwpO9fheQHIQORDcHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFamIejtixS0N1uRoaHwT1yBZXuQoEtb3z69lwB1InEj3QPqv66Oej53gKu7SQa1RIoEzFXfwMqy_Mq-0UNBKbxpDBAPh6XVHMxEOPd3cwr9-6TJvSzlcU6yqy_97bMieSOLJ4p1n94rrLwvA13-08hVjnYqqdX7tZ3rQPnYLmbgIadll3YAuD7wH-HeI10Mq3AJ7x0cQLp19fJKQWGh6eGoGShiQ3weXI0v3zBs1JUFYO9WHlP5XGhV86AXjonIZRP1VXdljyOy_yTsnpt5sPwwXKdBKWgVyDBvxw4txwf6kenzxfvwwQEP7PtVOBnYnicxYfpnfAkJIcwgifirWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gxog8UCWfXR80HmJQdMU6Nib4J-6TdPdbP2ROp1p6DlODBqwSBJvleOveJwfaHYR2AauP6u6E_1S3Ppmze5k1ipaucXuhBiwSZzPf_0ZjrHhMenAO8pEC9yAkRMTd3p565KQhL2nYpb6PqnWQGqt-Pu21ZB99K6-x0KSJWp5UFbsDt_Vn5PphvZkpOZAHXLfVekXYGw6MK9DR_9VsDZWFdv-wJYZhfjzCtWJsKifCX3rzqFvAD9aga7MommcpM2Fbi3SzB9Wf8hb6iUiPpvHMA9L37sxW8fJxxRPw4gVfsGdqrh-xUU-7viEDTU0nLbiWVLs3qCwfUGCVL5zomYxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPqcZ5sZBd3wrFnziqHFWVJ7D6w4f3nP017w3u0AVNaGAymfwJ3I5bMyGCgJNKG9Q0ejR_ToZW_KxaCWmTYk2nPLHpaC37vzgc_T_PJC6FhEKmdb7lSa5njMb_s0HqQ8leC5ZhAT16IVRQknmxMKcHOYh6moX2MUYUVyZUMzlluNXZ1vBJWTrbFGp1ux_Bwov08-o93_0ZyC2jWBX14B4hfeeItELfZmfIS3uP3yskimjvb6rDj802NPOmd81UTEcruE1gyYuXonledxw4EldocxPJ2dzr3E-MQsB0bSCIbVVK8SV_tXGy12GSkzoDoZlmlSivOHjsBzCliL-TprsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v06XpSgB5t23CNtKQDg0ou4B4zML7wkhLKviXbUxBsPlGIDOsScI1t_MHrffeo_7KygHeW2U31qys-NtMKdPydKWLj3yprsAedupCOMXFD83bXCqc3kcrbkDbKkqOrlzKfN9pbDDcSinvd4Z3AEtTc44Fj3fA4S74SdExxXqEBqcJeqAcHJYgRG-vx-f-ZZDAXt7etgda2gtmnaYtNH0CG_FTbCC-_t6wJSpVonaiTFEasMugLqReL9J4IpwLH0qkT2sUb1NbGQjZGxs74H7GRgBpAHaGhwX2sxlKur6dk8DPItQZ9PQgdlg0hkEVV7htr4KOqtNVF9VwlPhXkZrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoPMdAny-THbcBeV5ohoFj5O2lR8aDs_eCLQeakJ2MMAVQnu4x0KO7HTJRPvxYN9-vgKkpkV5isr9MdIofrGgwufXndxbLIIqkZe12QfRRgow69Shxtt1b4e0BV4eNj3Ex_WWqShwK4NrkQKgtYzTq6j7m7GEsv-W2PkCe3HoIrm93BAK6P3H2Fv4r20pjAp0xh06bVGhuZRHxJO5648tw4mQ3OvfDYEZOQWFLPyFMMzDoa4Ce7ek440tsm_VK4g97JN1D20LLrfT_qWRj5FxPYMWdLQRqrDMm8ekV9DtExd-gWzNcgoj09VEOp0PSy4wAJXI0VjvyCnWcUkjdiYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdU24C7gfT3Wc_QFLLOcfuNKsl3Z2imYbIruIiahIsLfpJ-NCwdb2x7fHNlWCl2w0sN_vxR1YB3_6Srp9hRmODLcgAAXbySOCslImEpyuZPi-8Z8u7AFN1mA0B3XzI2otPtsejEWGc0mMRhFNPswhZfK5EWGMDoyPnzTfwx2l2m-AsmTdhkUxaEEiyFKQ_NXKetWu-n-wViZvGitZOOAplbOdsHP5ItA1BXDruoTNGJfGOrZ5hcGKkL0XLU-RfLr6shxPspfDPCc3e15SHQu4kkWStvjzQp4A0xyhPucUY_7MvAmeJyWHv5r9dW_8YzOMpOzB6-sKalu_mHLafgkIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX2GawpiuU150-lrf-mrBb6d6QV1lZ4XGFOphmIEiEwKcgZIzPPMlfIOTM8oI2pHq4OlR1YO5gSKM_U5jM8GFRfZ_K34OyqSOIJNh_R89-LvD9AvbH3Tjsz8D8P6_cIGJE-BfQI0T4ovqGCHgKkmEo4URus18vJfMrseEqau3EWOZ70_pM_O0D1uDor8QX_Fzonry2PgjL6-bir2rF2tErLIxRqA5XMPct72FvmEi5Nj6ex_XmsALeGIFGd8_e9HevOXIIEFqUKkXdRsDDWX3q4-oMlWBvh9CqHeTLWZuW0VGmqsEnpmCFuQGevlyAXCnnjmGp2K53su-P7cvcAseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=avsVjRz8lqloQOTp_Vhl-APuh9t7SS420WzTL2KoWMgi6R1E7Lw50cM0lyFnTZu8is5gK4XO5FXjgyQxY-bPteyS2gP2JOD2DPMDgEQkVb9rC0NHWUK-Bg8tJtq1fc7P3Q1g6oqRdOnIjvdpHhjZxOrVwdBvFRWS2zoIPd97IfWJ4J-INbmeGewuuTGKuPZDe2iApT9q3QqfS0qr8zD08qTptGTIuwKZwYh8NwzOID9AOwK9t0MMvswc7tEc-vCbPP8Q2UrZLW-rjn_nMIsCKSGr0xftrxKGbjpyVgF3JjefUj9U4S1LvLRz4sWO64-7DWRyWS-oF8shfaz2op68ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=avsVjRz8lqloQOTp_Vhl-APuh9t7SS420WzTL2KoWMgi6R1E7Lw50cM0lyFnTZu8is5gK4XO5FXjgyQxY-bPteyS2gP2JOD2DPMDgEQkVb9rC0NHWUK-Bg8tJtq1fc7P3Q1g6oqRdOnIjvdpHhjZxOrVwdBvFRWS2zoIPd97IfWJ4J-INbmeGewuuTGKuPZDe2iApT9q3QqfS0qr8zD08qTptGTIuwKZwYh8NwzOID9AOwK9t0MMvswc7tEc-vCbPP8Q2UrZLW-rjn_nMIsCKSGr0xftrxKGbjpyVgF3JjefUj9U4S1LvLRz4sWO64-7DWRyWS-oF8shfaz2op68ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMdp7uWmMMqZUp13Y_lwNmb3YBId1k-jt1H_szNTZaGQrFwxiYljbkBtJ3IBoXN2AFgKa8B5qM02HkI1ofpA0mzhy9sPz8nCE-Zhz6uY_hUm-x-xcchVQcC2ra8viR4L6zhJTy7Gk9u_v0vHV_zrgs9nTHBD8hvEJCT9t6ZIV-3BX6iGSVMspbFoEUh3dy7WLTkte8yYZkaKzxcx6G9U9pRmySq9Wre7-GriExgN_eI_5Z8wLMANecPTOb48dtIi455K6u70M1KAH1PMUC5mISwSj334xfzxHcNToC5NGd2kFQk7Lakv4TNkEbSnAIgaWgix9tfey6llXnk9RYRlgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
