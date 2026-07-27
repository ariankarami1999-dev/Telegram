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
<img src="https://cdn4.telesco.pe/file/QrvxPEjXiB2H_zBMRtR_LJlirnrMhl3U5xR96ve-ivnlP77LXSdtOBsS3DqJTdwQjTSJ6dSehNhGDdtBTLq0v_4hlvw775mlqgSackhzhMQww7rjKhLhRFNF8Kg9-01IxlLWWhcE7r23s3MeQLa3VXZGGTgkoqxpgOEmlX-THh1GSqFA35SPOO6oYSMOEgJfgYcOMRoB_a_SsRTPl7YbUxWCkmRIEaNlJVA1xDZBNrsj01VolEWxDcNsW22fOwI3F4ToC7ioNuJk67YJIQhJ8sGXhthXqMFyOKhsNM8fnipTWz5dLAr7xJ4BHUrf0-Tylk5Wd1sM2Z5VMzNe-2g36w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhNJxy7cNeIWAeEPKA32rQVOaESp1kSWduLeXzNLHoiEDoD5CQqb1VnL-X6_e4c4FnapdIJ7xzW76U4XX0S3g_VR_zqXYqkBfShCClFnNy7VtFhWY6BNvfOt6LNpvuxtQ_DniK-ybAq_Wl0zbPvEqs6sd0gBr1PQE9oWFAHVr15atwLtQPe_7L8DXJEY5fP6xKFUxsOePSEDNjcqa1cTmhhg3NJCdWN2NS9b7fU-9HVBsBIzpRtOc2qYS4baUZ3DrL3kHJSxo3fA5ReZB56W7vVW36n0r4tequjT4mYnKgedfm7L7rNiGA1vLyYewaESXi4lC7e_e_s-Q-HfXxP_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0ZBQZ0T5YPMfVc2fyJp4kbFRQHO_DZAw2Yb3HJLh7Ocn93TEK1oyXkHEr2DfouNaUe8x-um0ibBJgdZFzQlBHt1ocRsyPmWcOjLRTS2YCDA6J3mPwYCHRGaMzjVs-FtdQTqB0EGRKSK99_L46q1G3i5ynMpVGdLbZT3rGvcEqHZmwCf2uwNHWarNZkhhUm8pslgboBK-Vk4VIovXaVi0xCQJikkihm3YIX-WXzkL-OXtcjd6F5Hln12Y3cjmkRuxbF9n4vxjsX6_7GEvnV2J2MnF51eE_s9yxuBbn1MtBiWtA62OD-6zTjrLdpU6Kl6qHfUshoHL4JGvoZu7M0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-mny9qaFlhJ7Jn8ao8wFQ9ifyQzjt7-lnHjOn7WOAG32fb_NzPxwe7t3DGZcep-QV7T2xZve0MKiuSfLo2Vt6s2N9sCbZy6EIIjHmyV5TzWTideKlMU5GaEV1P7N8LIi2Eq2bE1Uu3etq6R0ZaAb7wRyEF5AnX1XLyzKlUw581S3bxNqQzefnmCZr9tn15tZFKncjgdYABOTUx7Co87G19pfQTKwvkwb1vaOSOz_1OC0DwZSIpy4WtlgRKlPBhrWriTpFmBBmCjUiOccizTIFD8XslDKENJvohxUd3Af_QSsuNUu7FEZqTC4oE2AXcV27SUXbA97J0P8uCFKd1NIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p1sCX9o0tHaU37cU8Is6ijgJUtN6Q3PcYmGYIpFUXr0d1E_aqN0P1NE97-xSQ3pnh5txY0Sv5ifuMvm_8pZbX0xs_w1SGpWRCJHt9JxwjRmyD_TZNuboouU0VBQGj8lfbTF7GQ1U7dWdh31n9aBjNmJy1mHXbfNSqr4_buQRiQOllG8i1_HbD8tIBiGJEryIR1Jhrj3Zr8uhmRaEH4etfu01NAcuSmfwM7RtyGqOwdNQ6mV6lPm_Wgg0oqBRwuQn90DmihB4MRijc-R5SevYv1e3UV9IdVTC8Yw_4YHqAtruFrSVPp1Ew35NeeLsP93LXjFXTBMSOWbuQu6WeAtfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5y1a2KLuM15rJ58ws0N-_7TNYsk8hCVtYvu_WTpN4bvuVqVm1exC9lGsq0FVYID1hqr3pT_5kGWC6ZaHulBhKarW2ge-g1sIw8e0Gm3XtL0Hs-jBkCOT_PL2aYoEcHQMb1xdb6p5fJGKI728c4v_pc-dvWYU3fQc7fgMws_4nxP6SzcThO4xL_nymww-yjZoZXpnyGuVwT9sVICG_VmgzEr_Nq4vpRh5BtENJV8cRLnIkhWIc82zj6y2f274w27ovyTNJ8sO67jNjfIQtEr0kGEuH995rTwqI30S5qG92F9CRPF8QGVkLSl3SD-7iHCmXI4RJPxLRBQKyA-8eGyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvCvOioHaohVvdQUwqFVFlrf9mDr8052V9KwPk7siJ1p6Yu42xkKfaBWY2u2yr1mXYqnxTTZN8bDEaWtxpA2UmX__c_AnWVHhS68vJRvl-7oIa8YXIm9A98w6o63JsE4dYknj1zAf-KQAjqO7CG7iM7GNxkSCXFerdG6oiNR0Vk04qWUu8J9uz5_St0aE6PRvfmzHiyWxjJlBUMIkxcAVvT2VlxKI3U-2u-BU5nSoBV2rpJc8VgbCQO7K4r78UG0lxlbJDha9JqQz1QjcE3CgXffTXvO7kPX7iJhZGU0HVz7wX2G0i9AWboE2SJINersqSNqEJmHgDBQiyz5g-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6gYhEugDIX-Tww12P0DzcSg94evEWu6syKjA5r6h_DGl7pC3esHrPn01nDfQOypTn7Wtg5OdZWVt_pF6PIrzA3yGiBA6ED7jEFrxdDYzNaAcOcn_E-kCVvDIZkbwKSCZlObWuwKAhED2R7o4RWFv1kmGd-2ctWHbf8FX04S0o0NdNWQP0Ou0KFWxPvQWLPhTO8OTC5WXQH8U6Cnk_Cu9npGzCCug5qGWsagpr9RVmoq1JyYhh8ktHMJecmCkEI2kNatrNuSyaRPdorr6cRlbCQYOrPPGSkRqwIhhECA2Ddow99s-Wkx1eW8kVIuE0EZlaJALm-XXMcVTwQn5q0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDvMdlkfzDheHcMPeLoYmRVALTMV78kx_rSxpNdhCUapv95RMTJG1dwtRk0nyvQmhMsRJfQuZHLTw_XyuFYGv_U9A9bmZKabtCAH-h3DcyQtYP65gAJK_JHE_SYfoMTMP3RsTHWWHPS570yIGE4MK6BcvueLia5vznIY4qbA8ms1vw8G19DxGEOZL6HZ5uQstHrx3i3OgKp1XrPZHTAz81IC_5qcu-FDgYZ55FFQR_Bp50cVmfLx1UC7q40qYrVkaoqTBjBNGl8M4apyqWgSiOXyHTkVgFPurM3PJD6tWnAjzoHcEkgd5tOwXz72j06k6C-3yoylnFkEPcahxTyu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qk_mK4qzor8fxJLEaisia8lHgXZlkfDvVRcerwiWCwfwj82mpMbzI1mJu5QNHhHuO34kLm0rxguEgHikSTOy1kbcveATi3RYHjnUR7uTs1sF81iQ0Mp6hSotvwyZwLytPSHfRIH4Y9CdPLIw7RcejIxsBu-Ct5bJRCoWAHr8ExMVVCwQ3H8uPKnDJzpMwQCyA-xVdOM8WGNhtoA34wESsVkO8856SW0FbWRaUq1OVWxBTPJiYfHEvrwgWOeS0rwSZSfdzQMQ4SwXPq8Y6UXPFlDuBDYKXDq8GWmETHgV7aCdswTGJAyOWLDPDP7t0_R8011Vfz7mhA6MEIAPkaXbWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWMWlgvAbtND3FeNR56bbRbzSw5qysmjogV-enKZriOe1uyxoWoUcHrdFyZFLyngwDR3yovq5D8er9ch_VU9AIY9-q1ji88-XZYg7M2ClwxbA6i5FhzMf_5x2UyaMFzD2ZEzSGqB67o8TAeRFBG74NkbaLTA5kYScLvK4g7MTkTlEMsjG7qnNZQLXK5xImCDaio1wvB70yovr_cpQc6Cun0onQuJVMgipDkEk38pzZXdHSndg-JePoUSHsKkGay6y6H1J0nDVZbpFB5qZPNAkavtcQz-rTHVPxrVTnlArILoKPawyW9FWgHCUQRLDpAnQWMvsfeYhhFOMjGtZwsQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhVbztuVaHrDiarLc4Vd-K7ti_7k1F73q_83EUNC6AGcRVf1Al3D_Sf8ctRFQrxPwttI4w_r0yJ9q1DyVtxzc1pFf6fcevzkMDpUP_uKReA6jzsDTwXUwsvMUbL2OPwGjPrA7s_Db9MO0cGTKaymyp3meEtHYXQytfFvOX8NvbYHSiB_2fF_LRHt2rCJqMI812knkMGgYt-SGMc0t4lH51rIEVImfxkuG5M1yuY7dXOkhimNmvevE9LbbAGi6YGbdDmv9gb9VdmIBXElqx6lBUT04j9juaf3yBpJISt0O8W4AJc5KUPbHcJcRMoaLBvvjT0ltlS2OzSKkaUZDmGazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnnNTLe-3_Zft_tZDYhNITNsIDju1KGfRCEO_EyxQb0M6jbwMeuICcSiy1eoPBjNquBTajaD7A7lhgHuRfElje7Uy8SXctriJMpiTIOHrRUu9eCfydG7xbPtXmkocrgCTyf003kHddRM3iumBQImdEgVe68Oo1_hKWwz-BcOavlg5481qBHqq3Uk3iFGcGvHeAx_Eg6cvSKJYss6jK9-p0XaaCZk7SPLD79ppKZE0UZ5A9X_giO5ufI5zB3TRjf59rh2WBxwoHl8JfsBCyQkb0DwhU4ulaPk_gj-TssmwbI9LnS389f7PaGoWYPd-RXgkjzNwORvnOg69V-QCw4yOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx0eGbOvUPPuAVj80ZZDq0TEGp6scsBVBZvjqDK5uK5P4UtpzKHU0zp5cgoFyYnccDBr2sMXCnboV6NnurNjPuZP4J3O9YELemuc70jhVyFEdZiulnt22XfsKm-FvL51Nq6CEklaXEOvbjM51cNmjXtlgunQKU9JzQSAFQWFr0ZWkPUdofYUzfFqsE79yx74UAiU0AUutZ2iPLQOlq12zhhsPAwZTAvWKBKt56I_lRby5_1moQaQfkc4CjROUmvcqYP1pPiz_NQRX0L8q2VloK0dDqjddY6RlNmCuAM78IdsH6_q7kfwWj5EyYQJ9Y2KvzF8tAUlwec5sm-31UncXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7oNV3rCVQ4u0STnILGPCM7c6NmzDhFfdMXoIFQBY3ep9x1psQdDEOwnHDHmmMD0pukBPzGI0SYiCEYu3BCHq_CUDqw2_qwDnPLuzD8aX8IfyVMs7SBU6168xp6bwtf4PQz6jghzzXayTMyCnwgEKrRPzbwBKxQXpt3MmfEp3YPCuGc1PoDaZd8ZvnX7hHqXwLheMUzbuaswtdiidWU8FPD8khD8AUpqwkbcA92ikogf4RjtWn2FQoROZ-zpF-Z5Z6buQqO8PDJXOn9Wu_1wmyHcFpYl3Heu1duGEnc9bBmv7tkcZPf0WQiAfDEsxEIqI52EewjTfvc7wsBYFR0Yew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZxm-OyF2ThNp1n0YQ54ISrDYP5JZp5G1M75EQb-kx4yYPl1n2Bfg3c38_EGPNHb0R8z2XgHuITD3Ewe-QmR0dB8bcO7Rq8T--o1mCCvTRJTxwYpAA3p-L5QKzSpUNYOtY4xTyuQR_8uFVSzpXzfjRolatafIwzYH127udzovWtbREQ4148TB7VUBPKDpGQHIGWP1XQwibuC5XcHCMVij4WR34x1s1O20A2wTjMFobmkxfsDzpxXlima2HVTffzjKhcWD0O1a0eLvOhZCgJb63QrcTe14l7TgcM0o2P9KOt2kvU_BYN0sh3fcWeo-kTALS97-c8TZ5DqPbDpAokOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KU4nzOa-0yCYZZWTSLGgW9pDVb1fGHFxvkqVzAyEkXB-dHfzD_gtTURGZIMrXSSV5lg3VVS6thSg1sytbBPX2rsMdBK1acf8w3hPlDVYpjeECOdhebdvis8xo_D6LhGpvTwDhx4s-vOHWV_NMjwooextFAtdx_B_A_xPzwfkFrI3emdfDYsvnuRzLRRTwzeKltpElTat7Ov3eBU50PpW36d6DbGCLRs5fMcPnu0XFC6fzAj4TeYVxIUFJFfI0-wTxDICBAu2Obvre7ohIH2JHyvG0S94WykZXEqYVhVKtZJ-xejec7m35FMlX68dLe3_E0D8wAWukOxgdwuypw-nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzHqloctjOiScp589OYPd2fDJHaW8scg0A7zBJRz3_hF0K8qxddYMcaPulVmjXwwbtWJVFpRjBEM1qw_xEFotk5N07uj6LYf1h93B6vQaJR40DkWfg9ywdI8c1xChiUaQ7CZKpBW6reEMPUbPqUsf_gToA2y-yCwvgorHqCZgU8YJKf1oqE98yc93nEFurWf-O4bhp9ha9f2ElIfavdSYktI_YJERz6ehBFz2JDo-EKbYrh6NUe8bpBjso4hTb7rkqO7ZdsFKHc-pr9WErV-JbN7HiW4tAS5_IM9ZxaAjdCNXaE4JW5XDI6-5B27OH1680UZMCX3crYV5N6hK_QP5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKuhMTS3oGKhbg5mOydJcPMybEl2hVQ_5LgLgmRhF4MCqvBLxN_H7MPv4TJYIJrjlNrV_YZeamu-Yiu7DKp01GC2NZVPYodgpBZNrRTUH-3CqMnW2Fh13AyC2hP79NW6jvfLty1fnqG-sazqGRcGxQs-ee5lRtAmwwebuQMOFjLZBgRYxCcnWT6ZixfC8r94IWyZusv29RyLpN_ntvn3wxENqOlRa1IxHqnwATKsXQ1bFOUL4Te8D6RgR7Tc85h73U6Y9xpvcUnNGmUpOo7DGNjacM-n8gd5z0SUWM0u0dxfyeXlJTXdKzvI2fZNg0zgQdooc3MmwgzFQOZ5D1_JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQtZnFJ2rDUuZ6bDP_iX12w1e2SBJ31P4SqMs0IOMJKELXMDf65JxRQ2xmLVrMbZalfxOeK5WmMV9WJGwTLcuFAsb1CkvibzXIUwnhrhPKutWK7FbeAopC80-mJMGJsqKrspePiVvxwpaL8DVOMI1ZENsoi1UcwXEsziCWB7_cDOr4EnPx4_CSBkbYrqjmCjy56hLNzIlHHMFRuWn_Sb4qSGkCLnc-ZnSOEyT1xEiXrpnRHLcIYKA7xyQmJMKj69OnNBcsqeLXw1jUJxEkF88HdAjc1bUql-i7HRwTIC2m67HwvPRuVZ6THHYXpWAU4OcJVD4CAWkXT54WyWytHAkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlBXjLGChHNXHVWE2n6vSVTLkRWlQfWEwSf3v9eOM4ecuA-aojg0M7RZGBuwB1SiEeXJUbQ8pRO_99VOd8GOWrg38-NkBsmSP56gI7O4aQZfCuUMIdTKBO3HQVfcQcfNR25wfAUXeNsRdVpP4FbXaWxTV3_xZvvg7EEqEGRqMW8f9lxuNYZHGg1C94tvKVYKRxxK2LQCqxjuaLQ6n2WiIS4yDZ4DRTndMYJWsuI3KuiYm08dMMErhmBZVkauEwqWbA9uSb4T7OGO9FXMq6xrk6tanxst_YYD8yab9Y8VDdQ3LTSN92f3Y6QcX5ZDqX_nKIt1hyqFGbpdozDmDjeqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Mtx7DOQxP8xEQrgVsZ5-xSyIqJgiRsBMcq9hXxGKLWY9vmZKnesHCoJlYYu_9uyHL2vdmI6cE-WR27w-DWPLUM8anttuNIzNCkhSibGk69BzJyQcNrCQMrGL8TMqpX1So9o0l1waYMp8gN2JbXEoH1PXlwd8RkHyyPZEjIspuasF7g0l4aIpoTxx9HHv_Td0fSnatD74_lkFgeiCVE-e0N34zFdg-q3GO8THrIbBxTr-hP6_boLtwyw57w-C7o6Y8BPUaO6e-QrGUX2gX8na4C3ZJzelktwgYl0VI85cDnXPrY99SYknyGMY1dXhZM7Ubp-hOnJbZJKVoyXz-V2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oChXQwU2C30WSXuRD98nDIlDp61wWjSLyDXdJmTHIorQjU9UKvlyW4w03hqTPHDI-7EzpXVRMJCYxTWjbersnM9aOjLpIyH1zXlo5KYWaeeAXaozdbKZ1db0YnfvR6udJnxVOfNFAeYLlmmI_6UUGjApKlYCyQA-Eifb8MXSeKtXA8swszb_c3PIA1Fb5FGPw98GVA0i8YIm3f8vmXlSYc3VdIMY1uIWz7ICtrlIgqbKzEjXSg7PADHuoMD8AlGLBNBFJZ7Ma4boaHppR9Krj1CS-uPYk2A60muyPnP7M3_WYc01IAgfbn-LVuGK94KYX3OdwpHvOJlXJ0WUgfny2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=Q_dU3DcLzwKZX3TGr_EQL_CKNcdT_TY06OOAIzIX1SdFQdEY0SPrZG-7rXUM0EWCljbHK6XzkIVJMKWfIWoDfrkZv-fdn9IDDC03DY-MJDvLezpt2YgVaztG8eUrCXWBE9vQRpHmIdEchjHyVWUR_qP1-k2cnPFhNb-wl5LCK3Y4sD-PPHTQJksqItbckmqM_osKI6l8ghoE3yP5XmVTzVVzLAu-xvLudLp_uNKANmCfWdBoVxqiMPy-k-D4hLdl6nyU98KFoJVNxCy7a91rbFL6pKwmKu7ezRUURk21CeqAzV3GfwiEBX558i5JEOHLmiBISHY8ECTgtA2ghnmCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=Q_dU3DcLzwKZX3TGr_EQL_CKNcdT_TY06OOAIzIX1SdFQdEY0SPrZG-7rXUM0EWCljbHK6XzkIVJMKWfIWoDfrkZv-fdn9IDDC03DY-MJDvLezpt2YgVaztG8eUrCXWBE9vQRpHmIdEchjHyVWUR_qP1-k2cnPFhNb-wl5LCK3Y4sD-PPHTQJksqItbckmqM_osKI6l8ghoE3yP5XmVTzVVzLAu-xvLudLp_uNKANmCfWdBoVxqiMPy-k-D4hLdl6nyU98KFoJVNxCy7a91rbFL6pKwmKu7ezRUURk21CeqAzV3GfwiEBX558i5JEOHLmiBISHY8ECTgtA2ghnmCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=kIgtXoPhotwjkTGsSSPREd_IKZFT6IfqqQFTDHZY6LSDSeg56xsT7vAA1YKARbIuv3mjwUKprZnx3WKhCtTvOrNKKnG6Wc91jDdROhM3rynjBZumCrH9rEKgo275qEPvQ5AUf6faTCbesSGSNAKaRopakWhKRIE4v6AxpTvEMDZlu2AcIrdEhXlPAF9VXNQE8rcmKnqsTOEVuYfZ0BHM_idX3tQjYCpTDpdNIpfVYY43l41t9aJ-Cf9T1T3lP0zWl4RtcpDBKspaLBSmKjKGF0w-l_GBrrTM4aWyfwsuf76fC07cNxTHkoQIBzFBG3V28FdPtCAqnV0W5fo-2ODqoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=kIgtXoPhotwjkTGsSSPREd_IKZFT6IfqqQFTDHZY6LSDSeg56xsT7vAA1YKARbIuv3mjwUKprZnx3WKhCtTvOrNKKnG6Wc91jDdROhM3rynjBZumCrH9rEKgo275qEPvQ5AUf6faTCbesSGSNAKaRopakWhKRIE4v6AxpTvEMDZlu2AcIrdEhXlPAF9VXNQE8rcmKnqsTOEVuYfZ0BHM_idX3tQjYCpTDpdNIpfVYY43l41t9aJ-Cf9T1T3lP0zWl4RtcpDBKspaLBSmKjKGF0w-l_GBrrTM4aWyfwsuf76fC07cNxTHkoQIBzFBG3V28FdPtCAqnV0W5fo-2ODqoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln3YPGwgVDZXqZKlXGOAIm3GHhbuIq378TByKNJIWXErroFP7F3CscCEVhgJn4i1318fYq5ocQys2IhWk7ZRrMK4ZZ9upv1UdT59kCYSoPqzdWCVgBaL0jYMXQKLAy0mAVkiZyMfEsF-qTxsaqCKlm9HCqL7HHeb6pxx3LfdLNDBeMDmInzhSrmBE_2VSKSb9ZSgWwIPxAqj44pOO8el6CkMZPoFMT9Tpdmtnhfflngm3_UCUUG_2cY-xc1zmyKOvuiInjiIhP28jRQWIzZw3j1cuXepjOB8uinsT_fbPNfhnoFmTyYcD7AwMRl5HxEYo6dcaxQOLB-Sfm5TyaM6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=dbyaAarmxuJ46usJ2nIM5Ao0YTjNCbNt59R6pfMaOu0CMIQh0Xal6-QXxspn7Mc7UrsNgFHyBbRapOanAnrqxdBi1o1StZbqLeXOy78crWPT4mu5pCjSF1YjDiqr_5XU_wUs0h780UWxMkrAGruuPvIg2iuODDRfsXsy15V-dyrPFt0rX1PFT6vh_QEW4qEreGuoRBiv9s1dSqLOxdFKL4O6XeSKSBDuNZffrLlZXFF5vB9JZ9oHr8CTHmjyhJMiPIgs5x1MdW3al9fthq9GkIW18EBbk-pZdAQ3dMxQTrKVF0PStJMSi6NvzqaNGXbKH5JEgA5A4lqHarToWmvTQXixlqaxxmYurXHWchSIBiqegxY3RntQSfF_93WdsRIGziBI6kDYRwu624hsmb2C87FhTLiT4Wnf_WYrEaY8VopyevrRU9FBayq10zmnJYFUf1W_vYqp5QiLNagaGMbsHlIlnBOJk01YoBQG-QlqVhqPwoA3QfXny1xwOo8NFM2EJwJJDtGqLLTJB5ES3YYoP1mSc4zdv7GUpbKfqd74eVZ7xxs1gSCU8aq2hy2sjzqSuBHXUMvSGfvexUfd9e30D2bQyuKJBZVlZTAnZeYZ3xAzeb_sUoQMpTJM8herhLAjYXexvoLciLYkvYUeb9__pPt7fVI2ZIDWQDv2IYmfYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=dbyaAarmxuJ46usJ2nIM5Ao0YTjNCbNt59R6pfMaOu0CMIQh0Xal6-QXxspn7Mc7UrsNgFHyBbRapOanAnrqxdBi1o1StZbqLeXOy78crWPT4mu5pCjSF1YjDiqr_5XU_wUs0h780UWxMkrAGruuPvIg2iuODDRfsXsy15V-dyrPFt0rX1PFT6vh_QEW4qEreGuoRBiv9s1dSqLOxdFKL4O6XeSKSBDuNZffrLlZXFF5vB9JZ9oHr8CTHmjyhJMiPIgs5x1MdW3al9fthq9GkIW18EBbk-pZdAQ3dMxQTrKVF0PStJMSi6NvzqaNGXbKH5JEgA5A4lqHarToWmvTQXixlqaxxmYurXHWchSIBiqegxY3RntQSfF_93WdsRIGziBI6kDYRwu624hsmb2C87FhTLiT4Wnf_WYrEaY8VopyevrRU9FBayq10zmnJYFUf1W_vYqp5QiLNagaGMbsHlIlnBOJk01YoBQG-QlqVhqPwoA3QfXny1xwOo8NFM2EJwJJDtGqLLTJB5ES3YYoP1mSc4zdv7GUpbKfqd74eVZ7xxs1gSCU8aq2hy2sjzqSuBHXUMvSGfvexUfd9e30D2bQyuKJBZVlZTAnZeYZ3xAzeb_sUoQMpTJM8herhLAjYXexvoLciLYkvYUeb9__pPt7fVI2ZIDWQDv2IYmfYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=kpqey0S5jWUxH1XDCDNiqDzw3CkRLlykaXXzbKleg7IXpCLHji5yglrpKl5wdnUb70E8MFStjq8e33gBdD4gFrm7A2WZx1KaaTgrCMDkQPN4VMSJYfolsYfKoJa6VCTTsRi7sdfiJaVm3QllROs0PRnxV90LpUXHHUlZ2FSyWLIctLGN2ZKSFOL38SIcSjk4_kqFxQEGt-NlKhDZA0oL8KIaOMzL0V-mGn2uFf6GjGVYk1i056rtP71p5jf94IBFDbMzjdxa1NCl6sTh8juB_it-kE_x2FzqYQGfDlaJteLqO5wpaPynhb0Di5egjZRO5RlVHA5CN--FirHft04rSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=kpqey0S5jWUxH1XDCDNiqDzw3CkRLlykaXXzbKleg7IXpCLHji5yglrpKl5wdnUb70E8MFStjq8e33gBdD4gFrm7A2WZx1KaaTgrCMDkQPN4VMSJYfolsYfKoJa6VCTTsRi7sdfiJaVm3QllROs0PRnxV90LpUXHHUlZ2FSyWLIctLGN2ZKSFOL38SIcSjk4_kqFxQEGt-NlKhDZA0oL8KIaOMzL0V-mGn2uFf6GjGVYk1i056rtP71p5jf94IBFDbMzjdxa1NCl6sTh8juB_it-kE_x2FzqYQGfDlaJteLqO5wpaPynhb0Di5egjZRO5RlVHA5CN--FirHft04rSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFUn_oUDHGTp2bpfoASwrUCmhcfH3vqE9xlz--hPpfyRPwhD3CWhu3RkXuG5TXe3HmL4QTQTVxdc5xVXihuntIGK5am3DlF29LfxYBZ_PfFPqMr6aasIFcAVM36gJK_bohyutnD0BN4H9Kt5-bU4U3ySm5n2Fn33R6VvqNtLB9-SaRY-x1Xt7XL_eAU7QUAmOPkVMpwJ8c3UBaS-b8i1ZYkcWSVjTKDKt_OnJ6knR_bn7OudvMy1eyCnkOysBxg41EtjcWAuol6B3irjjuj7vz1GpLmQmculDaXvXqIYaLyJdil4xoyWfbsNMOb4dDEgQgFzBBjdWhsny5Zy-hLnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1khiMrmHUPxBYv9645ECGs07MnqUTJeIeJKbXQD2pYz5Xr9AdnpBdLXiUw8Z5JvzK1VvUcgBie3evcQbHCb7F0-LfH6xjARvtcRRqh69zq0msAbz69QKbkuxl0Ep2g8ZHen7C2NJdB7B2vPx_xjF46i0_MgN8QO7N9B2lXWRlMuZutEOPb-aroEDzWfdZ_TwZLbDYP5Swe-qYXswqW-0rmC3nswWcx79JgJ7yc5VnlDCSiizr0j6qfKdkD_il2Qyr5qGDWwuGbuFeZd-eyI55ehQW5ZW5ip41Ae9U4ufqVKvo_-Pvh2DxD6urrGfFWrh_Zb39RW54hBY3dXp9crhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Iuf3dBk2TRMDPRwts0IPqxvGSoynqPtWwGotcC4CHKf93TE_nQxfZvxuyjr0ecCt0n13Yi7I-CV7FGdSGDXmd_jAg7m5LsIUt3MClnk0XaievpGEgszcbUql0TaaJhf40Jnghi_MNf86VPjuWeDPRWNSiBDShpRMost5FzIdx178F3gIVB44771QgzIgrFnjBrjXNG2XGWipGaDDDalZOsvTTAXtcrPio7RkevAU9tDcEwmG2T_4OwYRNiK2MpBkL8MAxlOs4C0MXv6AdiAoDM2yLSEdQ1s5ig8XSufgWsH4fQ_66k9pJmLRZsKebZ4XGrhmjU2vi0NnvMyAj3rFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Iuf3dBk2TRMDPRwts0IPqxvGSoynqPtWwGotcC4CHKf93TE_nQxfZvxuyjr0ecCt0n13Yi7I-CV7FGdSGDXmd_jAg7m5LsIUt3MClnk0XaievpGEgszcbUql0TaaJhf40Jnghi_MNf86VPjuWeDPRWNSiBDShpRMost5FzIdx178F3gIVB44771QgzIgrFnjBrjXNG2XGWipGaDDDalZOsvTTAXtcrPio7RkevAU9tDcEwmG2T_4OwYRNiK2MpBkL8MAxlOs4C0MXv6AdiAoDM2yLSEdQ1s5ig8XSufgWsH4fQ_66k9pJmLRZsKebZ4XGrhmjU2vi0NnvMyAj3rFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LyEi1H89YZI7LP_6qL0CTbsk92GvcYsZk_LSzMtu0HV1aG6c8Yju_UE89ySN25_JOyOVwPpIeaBIO3d7uUCtl0nDu_pS33aAOfVSbjqO_yM856-Sp0weRKvni183xPlXgdyx78Ej_fEW75nQ9Roa3zSG5KbnSxCqqcuvMX3xjgE_FLRilPT-YpGTabuPEyg80ooK6QRHewyfbG-8QzZdF6Pnw2ut8x8e9J1Js8UVpIjkgc73WNJ4cOPyF0Fbuk44A2x0yjtfCsUd8hpMDHXaGFtZZ0a_N2MyBm8lHdLpSdCILkxXyjOttd3392fvVpQAlNHqhlRdyB7jxDLaxtYPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YutgGoa_sYfiU7lJJOBae8mhuVGxEXugGwdVn-W_pT0ovWcVGfS6BnGMQOmLdVl9zx23SrhRSDtaWWzxEahowHuuIcrGvUGOqa6-cnxzAsujUSNKs6N6zGXXg9-MK9CYrE4DHWV3UVoVkHf0pwGPJfTt5dNU_paghZLhIKcqNMjxmHBPJ5fG-BlzcNw6mQdmIQtBuAkKqYPSMWpmpnyRFLnbhdmaYGTRVrnwqAo0Zv0fcXazHu8zc-1RaFsgSiR0iHPuiMyUEKLRzpOnllOCOzoXcazSZNmtashJfeo1UcQOQjVYtrNqbfTLXMDvZZbzKLwwnQo9YLRemXOe7VRLVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=TfLL8lrbZSRoJcN2-2PJo6OQHDWbFSVibQ372j6qCCaVD60S8zpfBTwPHwIQL59bbftlgyL0R-6zh-277LnTC0SX97Gs_TWcB_70LEjfjxhlWO6NdC6wy6B24by5b11EUH6nlRe5EtatdStqs3NXvL8wEEECGs_7uuNB-i7ngA6XmMXVEjwsn4DoBt9J-DGp68rTL84j1N53k9CLQJqiRhgwZhk1q_zPRDCbGObyj7nC1E-MLrMz3qxJr7yYfhgz-UzqcbUNcFJxw9EVYwOQTTDj4MzKI8xscoffwYYJMCS6IORytnb2BfCLWXcJ0eIbYxzmkCN-WL5bY3VXxC_qKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=TfLL8lrbZSRoJcN2-2PJo6OQHDWbFSVibQ372j6qCCaVD60S8zpfBTwPHwIQL59bbftlgyL0R-6zh-277LnTC0SX97Gs_TWcB_70LEjfjxhlWO6NdC6wy6B24by5b11EUH6nlRe5EtatdStqs3NXvL8wEEECGs_7uuNB-i7ngA6XmMXVEjwsn4DoBt9J-DGp68rTL84j1N53k9CLQJqiRhgwZhk1q_zPRDCbGObyj7nC1E-MLrMz3qxJr7yYfhgz-UzqcbUNcFJxw9EVYwOQTTDj4MzKI8xscoffwYYJMCS6IORytnb2BfCLWXcJ0eIbYxzmkCN-WL5bY3VXxC_qKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=qAcEMjHxyvDHmLKJJCQEF3Q5-Bbpc7bB_MBRPEPt-LY3AP_L84HoZlDW1lHj_ijpa0ZxA_elmfeyzHU5i5st_wTamKaitF70JGLPDlQ0jgYW4DsrItDFGX3drPhwUFwWueMH43dSAM2vIRg5CWoBYVVJn6BX3xaCw25c-G9OigftB2ukR6bXNUyvFiag15AtkxJFTRSo7e8numvsDcIHDHPg5o2SWQaPRnduRU2jwpZ0u6KNjabuNf0mfUvu4JHxnoIqpuyT9BB8NILQ1hmVrpK2qC7QCR_Fo-qil0HszqPpkvYuHadW5p8PCoY1tGtrRCTXooE_j2KqIvakxRMgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=qAcEMjHxyvDHmLKJJCQEF3Q5-Bbpc7bB_MBRPEPt-LY3AP_L84HoZlDW1lHj_ijpa0ZxA_elmfeyzHU5i5st_wTamKaitF70JGLPDlQ0jgYW4DsrItDFGX3drPhwUFwWueMH43dSAM2vIRg5CWoBYVVJn6BX3xaCw25c-G9OigftB2ukR6bXNUyvFiag15AtkxJFTRSo7e8numvsDcIHDHPg5o2SWQaPRnduRU2jwpZ0u6KNjabuNf0mfUvu4JHxnoIqpuyT9BB8NILQ1hmVrpK2qC7QCR_Fo-qil0HszqPpkvYuHadW5p8PCoY1tGtrRCTXooE_j2KqIvakxRMgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=bWdbGp3nw3bRTnIDsby2oHM8Wyy0y0GjKA9mo5YZ8vYd0VUZnQu9jl8hDuBtABi3EHZSQEsSO8ofKwFKXzmmPdzEC7Wxf64zXiaJS9Yjolksb6E-qah9jd4nVds2AlLxH7smOm-OCbk7Lg39lrQYTGJoInvR3x4WHqjtVAHXYRs2mN_K7InsMXELJt4gKMJ3gPYXR73f-X6UDHPzeG3M41F75PtWcL9CpS6ZowWIxzE1q7trGp51FYrRoGvR4qsamh3MiWq6iTwTsqIwekWMi0PbMQKPNksIxAJTTNN9Kz_yOFbjUK-CoNIg43SB80uEdoEg-JHCGUeIsXQP38Tgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=bWdbGp3nw3bRTnIDsby2oHM8Wyy0y0GjKA9mo5YZ8vYd0VUZnQu9jl8hDuBtABi3EHZSQEsSO8ofKwFKXzmmPdzEC7Wxf64zXiaJS9Yjolksb6E-qah9jd4nVds2AlLxH7smOm-OCbk7Lg39lrQYTGJoInvR3x4WHqjtVAHXYRs2mN_K7InsMXELJt4gKMJ3gPYXR73f-X6UDHPzeG3M41F75PtWcL9CpS6ZowWIxzE1q7trGp51FYrRoGvR4qsamh3MiWq6iTwTsqIwekWMi0PbMQKPNksIxAJTTNN9Kz_yOFbjUK-CoNIg43SB80uEdoEg-JHCGUeIsXQP38Tgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUUh7IDlJU6TlUtpw6VoRUttuAsbjaKquRBccbv8-7sxrOG6ymf9YPnDN-2dyNK6Wv9g8SgmbF6LKYb8wynC7sApHUXBQSWwmBS5RKgaOGIdUjebm4PK4e4Rxi2mVkBXPPH5SDUp7vyx_rivqnkOQmrl0v7wDMyQSRSRqOeTu4tS5upPXEYhT9reuGTfg4oFY2LPtvt1V30u-r3cRRTogxptzodyAz2UxFfEHOn7MW2B9O0tZUsUIiy6aJqpd2gMEE9C4L8NtnvrLJARof22QBLoPavgXB1h79qsLockyDR-CtT5UpLh3UmmGao-lww2c1cF_x1XPxYzY9c1NpYrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru5P5KpYn3RfWwLLsrTGigigscEWgsk3PJMvvfvDnLB5Dd0Jzpx_Y48oolNOYd0MQmR3-1qoIB7qfqQH8g_IOnI5qiS30X_wMrZsptOhVEeKA4iqo5wd_UfHO8MJk0Cm2YylmsLpUz-Ez0jmyE6Yuw__Z8XS-nIT0vs17RKe9RGc44WE9ANPnyBJtKy83SAKzSuD2_ybzI22jkdom-X8DiWoK5iaT51E0FoKY6krD8grqsVVhaznpno3QEXu7vw4D1r71w8kSb2ly6ivc_LUbC5d3LyLYBRFAp16U2ItSbJ_h6B3h_WjEgYveenaockvfml2cS3vKc0yiRqdanxoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=mL0hY3TyOkPmrKM8FtHskYYFIb9ajn4EznKnQLg8xOI5M5aTJyfbfumzrY_49TrDAJFGliiG_PmRqUuCEK6fmPVIizN1CGamQW_MNAooxp7Q-wG4M6snO_pytfgGvSE6QW3pnHQMC6dIOkRjlzVMxmHsEeJJDM8kyAOHjzTqxcKGtHqvyXnV9r0kJ7kRIB5nYKWWSNk-E8yYs65fVDoReVR8qlMmFGry1hwpiwwtwscf2q0Zeb03m8UfAecXCaCHjyztCCy2npZ_8Do8HH9GYEu9rExUWLS4lesS67mnYzxD-k2yCM6NrVBRvgYDFG9gFgeCc9dLy2crP7AgPSuzxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=mL0hY3TyOkPmrKM8FtHskYYFIb9ajn4EznKnQLg8xOI5M5aTJyfbfumzrY_49TrDAJFGliiG_PmRqUuCEK6fmPVIizN1CGamQW_MNAooxp7Q-wG4M6snO_pytfgGvSE6QW3pnHQMC6dIOkRjlzVMxmHsEeJJDM8kyAOHjzTqxcKGtHqvyXnV9r0kJ7kRIB5nYKWWSNk-E8yYs65fVDoReVR8qlMmFGry1hwpiwwtwscf2q0Zeb03m8UfAecXCaCHjyztCCy2npZ_8Do8HH9GYEu9rExUWLS4lesS67mnYzxD-k2yCM6NrVBRvgYDFG9gFgeCc9dLy2crP7AgPSuzxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=Szv1po8AjAMAyCeZGKt8Z8KdNIuHFyT0kr5R_muiRrKKQWCv2jNytbUSbuFhUAY_M2uf5wCzKr1QrC_yuegk6bPSOKSORsaOvPZF2pMZT8wBAEG-HGsoZGfo_RNeXxwP_HuiLaRxUo6IxgnHLdw24VmrcxGWVfdcArsbq5E1T5VpH3V35rhkXKV6SJ0x9oUNfWEYtazKH-FzFLqqoreiAhkIXKeoqnS7bCZ_i6k0lJacQ-tTZTWtN4QftkEEd2tf0C0TBXbsqj9M66l78S7PsXgCq_bHMkqM6gMSn1-OaLdaNPLd6owTf7rZGGSSoLxbvk7UmABmzJwrt6pv48ly_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=Szv1po8AjAMAyCeZGKt8Z8KdNIuHFyT0kr5R_muiRrKKQWCv2jNytbUSbuFhUAY_M2uf5wCzKr1QrC_yuegk6bPSOKSORsaOvPZF2pMZT8wBAEG-HGsoZGfo_RNeXxwP_HuiLaRxUo6IxgnHLdw24VmrcxGWVfdcArsbq5E1T5VpH3V35rhkXKV6SJ0x9oUNfWEYtazKH-FzFLqqoreiAhkIXKeoqnS7bCZ_i6k0lJacQ-tTZTWtN4QftkEEd2tf0C0TBXbsqj9M66l78S7PsXgCq_bHMkqM6gMSn1-OaLdaNPLd6owTf7rZGGSSoLxbvk7UmABmzJwrt6pv48ly_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK-JXCcJhNEsXZD6EdwolPh8S0rgdKW-v6Z9KT-ubrlgRfi8Pk_RiqkMr9jT3xjVmRZWsR6-vwzHvJyugFSouFNtFAc7cXtrScZ5YlWBGt_19LaGPPArJX2g5dXYuanf67gHeRxB0WMfXStO0yh2XRiGOQc5e71enRXA-a3B0v9Glv1xheVqAuHYYoCMGGld0rwzxpW1xt7br1vI0DHQQxQhWNrA5MDcwCU8KKnJXtQQr4Uu6Dnjeo6c8OiqZ7Pc31-z0uC9WGeKK8bTIOd_gfBKsNiyRBuOqHJVxesnCT1dw1_9XHPJYfMmUOpcRNrVtvrdqn1dERShjy7rAycvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=aP84k7zPMvEguQnGAWxR10NOiREDnWkImZgBNLK9FjWBaK004gK24s7P53OXnY7s8mL4cKlC8DXE0mhRvn58WoNX6jH5d-N-Ou8UweHkThOPq2dLZ1Ifr_4dqFD8sY19zQJw_Y2YcVvrSHhBJeFKOmucRSMxnsZuuUfvNf7i2TJp7poymeRhN9RMUnTAqBumin3e9dJaTWT_B4bq7jqA621G8T9EfBubY_3R4Isk3M_z6pxcBZqrao34eiMCF0xyE2wRs9xeYgASkHMRjWvJVUrcu0y-A7XbIlxtffyCqHyE0P4aGeLLi5KpkJ9ucpJgNAVIiZ0UxLgzTQSBoRSUpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=aP84k7zPMvEguQnGAWxR10NOiREDnWkImZgBNLK9FjWBaK004gK24s7P53OXnY7s8mL4cKlC8DXE0mhRvn58WoNX6jH5d-N-Ou8UweHkThOPq2dLZ1Ifr_4dqFD8sY19zQJw_Y2YcVvrSHhBJeFKOmucRSMxnsZuuUfvNf7i2TJp7poymeRhN9RMUnTAqBumin3e9dJaTWT_B4bq7jqA621G8T9EfBubY_3R4Isk3M_z6pxcBZqrao34eiMCF0xyE2wRs9xeYgASkHMRjWvJVUrcu0y-A7XbIlxtffyCqHyE0P4aGeLLi5KpkJ9ucpJgNAVIiZ0UxLgzTQSBoRSUpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw3liMXg_4qDUnjGXboBTDVcsGwwGLJPjcC4TAyGsxoOteh81YnW-BTyd4XOoRbCd5YnzE2wHwFr5X18UqzGNWn1QjKqHwSQUxI_AOeiectnlCQ7gg9JxWvQXpHELeaPnRY0quaWZ__1i4TwPjz617liZRhnlmg36ZPeimyM4Ixq7D7w04B_j7yO1hyshqJA47e_k02hEC1caOCjlT9u422A9JKhcoTICw6RhOSzKFbwVs0qr4yQMFvV3_hHFsE-HQ676xEp4RbKdnWPEEB8tnE_l-Jb6fmquYyrf01W7O7WeRH6Yhkv_U71xcK050m5rk1X8WB_pWPEAYFK8ffOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCBTEuxQ6M6V4fJ-em6MGKJSokuMeH5rYFF_wAVZn_tLliCWSL1YRIza4FyqWvtzUBuR45ImzTfm2hvAy3GLbtnh-AojPEG6FYLqVxdoqck3tMi4DTtr1swetX4cQdGV-qWgSH4iTxmY6FKgTTd7lRumZJTBVRJ3BZ0ck6Qbswe5WA_wPy2MdJslofIMMUv7p6xmj4UBgbVHry25x0J-sKlx5-Foo42QdCYOUvZIgH-D4vnUAvdoZRBUl4okURu5D6oSUPMq53R4HsH2HTr126rkEB0kwwAfELEpmYqQB_7D-tlUFs-v04c2X6TrQ-VAefMxovPvczj2fv1gIJBMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJUZeLWY4lBEOOb7ePOoaFsq9KHnxpQnSJX_w03HiQjjrUQp7rplf9Y3oKhjRU5YgfudOl9OUq7A8QRGNdShWgFbVW09R2rZH_WTXDqbSNmx15xtHYOmlMDRrnYwe0g3sI2kQGtWZE-uBG7b7bD2BwldyZwI7FlM4psdHiVxWJt4uM8dUXrAvorMjFbqwG7JposBBfoo8rhplJtdmJfpAkdpvJMLgh2Hfd6SuiWbV6b8PXfUzvfTcvjUerRXyuXJOz6lxsM8TDKK8JmGX9UxNDpcV-HOWt0Yx7LxOCqM7_FNwJ7aDpHMFKd4Doyxkl--_dnX8DgYTPL6MpdsSEImNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=SYMN0cwDS68J6-1YkBRU4rrXmTh4qJZ930NfvvabhbHYpPzKL8r5FqdSIu53p9ihvzpr5VW-Xqg9INPEN7JV_X0lNCLHENVYObGQhMMJt4c8UypQUR94xV6Q6U-qAKd7yShZjU0Q-V52eD51HAEtKuRVO-1lOEsy5G6PuUZIzmIRkFDFhAcmn0j-Yomwr7ervl2jWr_iRk6_RO0vLqPdyxCIulG2LfbnzsHEXlDQgM0RFuGAQxXaNCgH251RnT2Q6uyAD2-5gu9A7hKjBh50exB3KK84GKx69wi0Nhpnyf28opad6eMBhuPkeAw3I4IMEX3PsE7sF-mC1X-wnZiL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=SYMN0cwDS68J6-1YkBRU4rrXmTh4qJZ930NfvvabhbHYpPzKL8r5FqdSIu53p9ihvzpr5VW-Xqg9INPEN7JV_X0lNCLHENVYObGQhMMJt4c8UypQUR94xV6Q6U-qAKd7yShZjU0Q-V52eD51HAEtKuRVO-1lOEsy5G6PuUZIzmIRkFDFhAcmn0j-Yomwr7ervl2jWr_iRk6_RO0vLqPdyxCIulG2LfbnzsHEXlDQgM0RFuGAQxXaNCgH251RnT2Q6uyAD2-5gu9A7hKjBh50exB3KK84GKx69wi0Nhpnyf28opad6eMBhuPkeAw3I4IMEX3PsE7sF-mC1X-wnZiL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYTUxwbuuLdCFa7UDYVWDV8C2I_KAUE5NumQeII5UKhwM_DVlnu27dv9ttZD9opfCtn-kD1d-E80HVnRl0_L4fvVGraNt0BUZ6So8pgOzkmMpg7oy25sPh-WJfX5_18E7mg_gugT6Ultw5EdiKCsFdb61DxVpZCqSrhhWacAgQURiXEWahQM9VcG3lP3x63IWfDRhAtTP8R6mkUHjXSDDcCBsxFRwDki89DPOAxukK-JnA_5jJ8CJQ-fmxFwuk6D9sBLx95LRWq-hHalT2aGLfcgxTAyTcau60OBgcNdsNJMJsmvtFH1sD_mEs177bPcanvjlHqBs_CGCmvNnZq1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=JlZTH1WVL84FZFAmmjZYgUFOeBXIx9F3lATCO7CpnkW2DxOOSv3klV2sJSsh-dhEWA9rMTojEjIXsdCRHbKiOTwejreEk5pBPmTpTQV-1xLe_UQOrMigN7mIV4A3h0tGZnu3k6v4h7Q5vTOBvPa0TbeC9pXJqxAfCVEtqHzZo7Jxf4efkz_jCFmHT1KLnAjBjgJM5QXnC6vchD3eIbfnorNjoShdhX5cXA-yeJA8TANUKbUhTmWZGfmZMyLrYJ17iA-qN_brGJ8BxwgkOs4xVIKGOzB6dZyqS8S7DATwBhOi3audIFJoUlcdV03pFExqK6ej_4JkhVkHf56fEEf8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=JlZTH1WVL84FZFAmmjZYgUFOeBXIx9F3lATCO7CpnkW2DxOOSv3klV2sJSsh-dhEWA9rMTojEjIXsdCRHbKiOTwejreEk5pBPmTpTQV-1xLe_UQOrMigN7mIV4A3h0tGZnu3k6v4h7Q5vTOBvPa0TbeC9pXJqxAfCVEtqHzZo7Jxf4efkz_jCFmHT1KLnAjBjgJM5QXnC6vchD3eIbfnorNjoShdhX5cXA-yeJA8TANUKbUhTmWZGfmZMyLrYJ17iA-qN_brGJ8BxwgkOs4xVIKGOzB6dZyqS8S7DATwBhOi3audIFJoUlcdV03pFExqK6ej_4JkhVkHf56fEEf8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=LwlPEHL1zJv9O3y5xoog2ZkTfqek43wzIcDqVSH28WUevuSqwXiBbCg6u1clov0-OliO5U6qydaYekOcVGDgMaEX7fcwZ9D0cSH-XPuTX8UjOsMRh0qr1iDT3raWRy_qPm3O1c-upR9pTOssLKAOkpPAO_xOu9uCfRvKN1IwfSGcgjYxibcTe0qImR5IkSIqCzLmT2dNYRucn6Fq4agt3oAEbbkiMxfOEJMtXTNZTDtX9gXRaVTT3ivnpGS8A4gaaU471SaLlH6KGn2pDGay1YiuIXbxgFV5iy3rFhVI6DWv3b6vd-0eCmNVIZl694zOYO-rxCBcRmb_wU__k7V90Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=LwlPEHL1zJv9O3y5xoog2ZkTfqek43wzIcDqVSH28WUevuSqwXiBbCg6u1clov0-OliO5U6qydaYekOcVGDgMaEX7fcwZ9D0cSH-XPuTX8UjOsMRh0qr1iDT3raWRy_qPm3O1c-upR9pTOssLKAOkpPAO_xOu9uCfRvKN1IwfSGcgjYxibcTe0qImR5IkSIqCzLmT2dNYRucn6Fq4agt3oAEbbkiMxfOEJMtXTNZTDtX9gXRaVTT3ivnpGS8A4gaaU471SaLlH6KGn2pDGay1YiuIXbxgFV5iy3rFhVI6DWv3b6vd-0eCmNVIZl694zOYO-rxCBcRmb_wU__k7V90Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLpkfIIe-SXpoo-Ng60aZCcy3m5Rm3LCUJJk9mtdeV7dEfSTUKrzg5aEN1ls_6uk6CfSwy0SDViV7h4YWbC2EQUKxN89uXZSxgeLaD-NXSXfU6mCvL4qimfvUhULaNJs-0sSXVSnKzpVefmybv1OI20h_TpZ6Efa1rPKEMw3U3RMzwFYllVjGtrp3ADy5vNBPlSJdunx6HaJxnZVMbgzvXZq7qd5f83-VkG1ryv9hwdxar0gfRAPYy_OA0RIirV6m2BO0m4LaZC7cwkiwn4bxdaBk4WiGAi3Hp2dswCjkfdkAEZ0JtDEJHwXA_Cdj_rZ7FiA0-LHzkrgNSnxJ7Befg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=bH8FCNc5tgJjHAJbCMNdzG1AqEXKldpZt2lZ5o9vLRjb2cLrxm7yremahcUVyj1ajJ4TijQq6kXL9uFU6FnjaD04dpuBlQ7koOWskyGmsMqBcYFKeuGpzyd3ywAmYOgTu5HD3XLvlGwEJsHTxjcKiEnKuhveDnYKY5qHEdBRxtItYr48y3_sDyaQqOF5qMSFA25qtggs6-ou85szbHVMsL3jpVu6DtGzOQvjmUPJ5XEGj3lxdiKCAX-Avv85sinQyYZcGymWowa9SDZv5XwKyb5sl3etl3LWF8uvF7WA-eYwBPlX91YO7RAvGHUkvY_ZASG_LPi_foTCSjL50ubOqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=bH8FCNc5tgJjHAJbCMNdzG1AqEXKldpZt2lZ5o9vLRjb2cLrxm7yremahcUVyj1ajJ4TijQq6kXL9uFU6FnjaD04dpuBlQ7koOWskyGmsMqBcYFKeuGpzyd3ywAmYOgTu5HD3XLvlGwEJsHTxjcKiEnKuhveDnYKY5qHEdBRxtItYr48y3_sDyaQqOF5qMSFA25qtggs6-ou85szbHVMsL3jpVu6DtGzOQvjmUPJ5XEGj3lxdiKCAX-Avv85sinQyYZcGymWowa9SDZv5XwKyb5sl3etl3LWF8uvF7WA-eYwBPlX91YO7RAvGHUkvY_ZASG_LPi_foTCSjL50ubOqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X0YxgR09vrvYmn_35YK4TKwTY5X7xCc-pHO9MbsDLNeIdLX7FHY9tbxkydzpPy0O9jPdmA309OiakSyuSdcBFmemDrzqjuAp09dM8VQ9fD9lgLv6RPuBXLymcxSCSaHIgmywnubVyIJ1ZRRiVvnb4I1_CGdMrOFFNy6iGUS1_gg65D-qA68yDq5IWenaSPnWJK0-hjpD_8x0inO8X1m9-4JQQvU-_pEKPJU8eRB_ZnHDs_LK-xmhUy6PII8tBvugoPLWRTHnL9ifSVyhzQc22WhH60r7q5CM9-aaUanml2rgnx14-uM00UG-DYc8uFS82QwP9BWjDemh3gvBZH7kxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X0YxgR09vrvYmn_35YK4TKwTY5X7xCc-pHO9MbsDLNeIdLX7FHY9tbxkydzpPy0O9jPdmA309OiakSyuSdcBFmemDrzqjuAp09dM8VQ9fD9lgLv6RPuBXLymcxSCSaHIgmywnubVyIJ1ZRRiVvnb4I1_CGdMrOFFNy6iGUS1_gg65D-qA68yDq5IWenaSPnWJK0-hjpD_8x0inO8X1m9-4JQQvU-_pEKPJU8eRB_ZnHDs_LK-xmhUy6PII8tBvugoPLWRTHnL9ifSVyhzQc22WhH60r7q5CM9-aaUanml2rgnx14-uM00UG-DYc8uFS82QwP9BWjDemh3gvBZH7kxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=TAWboIKV9ocvWhAvxLegfzue4xsveu7BXDEt3E-p8Mp2jsyQLe8Q7PVzMUeeIc66lWi6Cud76zUtPFDv882gNSjZ-oORBs0RCZLwOjT51DfE7Z1CsfveBA7W-MUHeCMlPBh55QNj98Sa7EFDIaTGFVu1MX-ahQF8kpNQB_8wp4vFE3hVOYXcKMNPYIDctUzKNpM9Bktx88jHZ4nNezvIoa-zdwtxGrwGEwPURQ1SlbcCM0amjG6_r7J-uVt8d7zXpb64BxszSXXuDv6txz9ZrORjZHAvbQcaKqgXIjwIdV5m7153Gp-QkHMjK3jsHoC2XMHpdVtL5sH9tZ1qrP7jUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=TAWboIKV9ocvWhAvxLegfzue4xsveu7BXDEt3E-p8Mp2jsyQLe8Q7PVzMUeeIc66lWi6Cud76zUtPFDv882gNSjZ-oORBs0RCZLwOjT51DfE7Z1CsfveBA7W-MUHeCMlPBh55QNj98Sa7EFDIaTGFVu1MX-ahQF8kpNQB_8wp4vFE3hVOYXcKMNPYIDctUzKNpM9Bktx88jHZ4nNezvIoa-zdwtxGrwGEwPURQ1SlbcCM0amjG6_r7J-uVt8d7zXpb64BxszSXXuDv6txz9ZrORjZHAvbQcaKqgXIjwIdV5m7153Gp-QkHMjK3jsHoC2XMHpdVtL5sH9tZ1qrP7jUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=Z4PWtTOLSGMjOyprvk_8uqQzrNt8Mwu-ls9Hymwh84svg2cL-zPbtM2Du0iuevy79brg9jZ5aeDu1MAzpJRMq4wpgbkdnb__SzQk9XIKWPH1QF_eML2vaQG8XQz1hs5pPH25H0nL4jupdE0yRWhZbBgKFt_Roy1c8jB8tMauc25gwVqGiYrLxk915b6r3-eUVo91gdin_Eh3-LPNX1vUQRiZlJImIdBZ-Xau8MFSW18WpXVSvUPsBW6I_3mwzWAIEaqiDNtZkFgfh0rPyjsRBkB30o41rcudCgRq7rYzCzykL5t_CvJsiPUiW6LGGRZeGCIcioNa8DooMcHsF3_6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=Z4PWtTOLSGMjOyprvk_8uqQzrNt8Mwu-ls9Hymwh84svg2cL-zPbtM2Du0iuevy79brg9jZ5aeDu1MAzpJRMq4wpgbkdnb__SzQk9XIKWPH1QF_eML2vaQG8XQz1hs5pPH25H0nL4jupdE0yRWhZbBgKFt_Roy1c8jB8tMauc25gwVqGiYrLxk915b6r3-eUVo91gdin_Eh3-LPNX1vUQRiZlJImIdBZ-Xau8MFSW18WpXVSvUPsBW6I_3mwzWAIEaqiDNtZkFgfh0rPyjsRBkB30o41rcudCgRq7rYzCzykL5t_CvJsiPUiW6LGGRZeGCIcioNa8DooMcHsF3_6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=nkqpuQdBf3zgQ6jWwNce4ajV1VAKHNjYkgalKq08B-8i20efPNKKHelhdB9omFXA_uaOe-vRQvWKt-7Msb3u4lLS0ccsLR_UFXPtP0i1B3bQCRFTu-Poj8h8lxcU-SxKPuNtbI8ZW5AGbcLRU98bC3i0WMb3z2bbAkbrCnaT0UgWD514kc26TkSIscibmZcXQbQXhOPs-CKjgYbdDzsPFdZY0FRzlN1UeRzHs2IxyAe53rIInGAPp_5EBNP2JGwC2xUnSyroyYFnq7J88ksknKZ5ypbvYQiVOjKSRboToHsTBIZXDx9jIo9hWi69dvo1-i1zcfLuvUpAaEj-SycsfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=nkqpuQdBf3zgQ6jWwNce4ajV1VAKHNjYkgalKq08B-8i20efPNKKHelhdB9omFXA_uaOe-vRQvWKt-7Msb3u4lLS0ccsLR_UFXPtP0i1B3bQCRFTu-Poj8h8lxcU-SxKPuNtbI8ZW5AGbcLRU98bC3i0WMb3z2bbAkbrCnaT0UgWD514kc26TkSIscibmZcXQbQXhOPs-CKjgYbdDzsPFdZY0FRzlN1UeRzHs2IxyAe53rIInGAPp_5EBNP2JGwC2xUnSyroyYFnq7J88ksknKZ5ypbvYQiVOjKSRboToHsTBIZXDx9jIo9hWi69dvo1-i1zcfLuvUpAaEj-SycsfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Byt361lA54OiMpbkC5hefAJbo9GahtN3xVYOGyA_DhxPp5BXv8ylTe-4lpsoVorvkMOtDhy3HOOzNh_xEsk4Bw9nxlwsDBMgGZ2dwoHIBe8wNstI8TsdZZtPasq0uR4MuzQkhv0sHnBLmBIeT44WAiVT3chFLh8IeMP1OWwCpEiN4OXmvKV9mxPkBOXgn9ivoCUqTSMa1YyXi4n6GumFUx7KPJ2TGpWwc8Rq5g9KfJ0TFhwjKStK63gcMLqjnUuuqd63pBVem8mR3pEI91oLGpEpcYKMrO0BHZwYUpirxe-pWxRNm2TJXy6phD_QBuhHqY3ml2455yiYGvU0e6FpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=fLX4kpsRHTp4HSnqln8T2prauv0RiLIFII5HziOY6sA-ED0jpVEmhylOHhyoImAjHHsfwfnHrVSkUbXedh0dWk03Jne0vNYZA2eJS-47I7wJfaZXW30Kg15whvIBYx3IHnEkf89WWBuwsC6BPto6CEK7Sp21r_fM3z-3rS1hcZdeji67ak1htyMXB-7zXGLm9ULzq3qlOWzmesMiO8eQEM3GZvypXci4eoGrbCO2dwcRy9ZzXpzODKlLt5M8qQjltRabP3JFQRjdB8EvLp8kNeuAISl2egxCQVEkEo5LXn1YJefp-hoUkWQ_N5LJkhP4N5YsmfR05xiSH0nhSmj3bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=fLX4kpsRHTp4HSnqln8T2prauv0RiLIFII5HziOY6sA-ED0jpVEmhylOHhyoImAjHHsfwfnHrVSkUbXedh0dWk03Jne0vNYZA2eJS-47I7wJfaZXW30Kg15whvIBYx3IHnEkf89WWBuwsC6BPto6CEK7Sp21r_fM3z-3rS1hcZdeji67ak1htyMXB-7zXGLm9ULzq3qlOWzmesMiO8eQEM3GZvypXci4eoGrbCO2dwcRy9ZzXpzODKlLt5M8qQjltRabP3JFQRjdB8EvLp8kNeuAISl2egxCQVEkEo5LXn1YJefp-hoUkWQ_N5LJkhP4N5YsmfR05xiSH0nhSmj3bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQMu8wUVrXA6vVztd5Y3gTWdza7i_np4ilyNJPsfnIxG8sydECX1Lj0o6LHk9z7CIaz28F8X2uHHcnqa3nYym5dY_zqM8EsylBh0Zkon3PM8LSOYQPrMKnKlxI8wzn2urA8NoPRLu3ggtZQT5gR5K_by4rkMwHhQkmFjYGdv2EtiiId-BoizQ3TOI9WcoJAUOnMziNoNY4ah8YVFKGVgRB8sEiBVkAh7Qev6NLK216ZxosJDkojKa5UHp8BQgW3pFeNF8wFwhOEW86ZL6xj2YLv6vj5YNhg1n3MsJSY4fh92cOSS4dhIjBbYrV7_zOYpgwZ1jjx_9pa3tucPRNU07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=JJiLBEcpWyBtl9dXUlyV8MPGv3PbII8z9fUgwNG1NCtkGxZZYHc_CP5Zc8aTn7-CKALjAm4ZoD3TptAwY04J-09cuy8WCMxXGbSflXBN9TCQqlkWCCsqqad-tiPvBQuhWCxzkjy4aP170AAOIxiYtODZaYtHD3VkdoAg416Oj2aXGoAX4_8NPGChxMegRjZ3ZUmS1ZzASBDjgc_L_67QKtW26s-aE1BLRYo5ZCb1sw3QoPDhq4wSB3ad5HSXOxjs095UJDZI4JaaLVdQ4SiTEOQ5pu0x3-DNGWYJN8D2Oxs8o4QJcOW6xvXYGIcqOySyN1mMopJJ8gORG0jAwJoafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=JJiLBEcpWyBtl9dXUlyV8MPGv3PbII8z9fUgwNG1NCtkGxZZYHc_CP5Zc8aTn7-CKALjAm4ZoD3TptAwY04J-09cuy8WCMxXGbSflXBN9TCQqlkWCCsqqad-tiPvBQuhWCxzkjy4aP170AAOIxiYtODZaYtHD3VkdoAg416Oj2aXGoAX4_8NPGChxMegRjZ3ZUmS1ZzASBDjgc_L_67QKtW26s-aE1BLRYo5ZCb1sw3QoPDhq4wSB3ad5HSXOxjs095UJDZI4JaaLVdQ4SiTEOQ5pu0x3-DNGWYJN8D2Oxs8o4QJcOW6xvXYGIcqOySyN1mMopJJ8gORG0jAwJoafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=Z7ny9SeZ8HHpj98y95EO84O4-Y_AYOpnGnWSfEc-UhfSyPFDVYo3FZjwTqEqQ31t1GBD_NvLhJ6-TY6H4oe8vVRsmeTg7YjUaeoWOvkAtPuvuaoXodFZXBIPacCbNcAQr5NJSFCqmn5alJZGghb4M6N0b9oVjYrKAKiNGbjP-qJiOBHlWX34ghj3hnkZsZG33G7yReSoU2fQBg_RT9vYlMjidQw6XaPJ4YaGl5L_C3VklO3EnNNr8szWU_iGre5X0e5lbdG3eF8fMiYTv6mXvl9XzmgSAcwPXZVc2nYLa-GJJ3Zwm_PfxBYNlY4sY-UXU3SEdGLzmMWrq8EGn44rqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=Z7ny9SeZ8HHpj98y95EO84O4-Y_AYOpnGnWSfEc-UhfSyPFDVYo3FZjwTqEqQ31t1GBD_NvLhJ6-TY6H4oe8vVRsmeTg7YjUaeoWOvkAtPuvuaoXodFZXBIPacCbNcAQr5NJSFCqmn5alJZGghb4M6N0b9oVjYrKAKiNGbjP-qJiOBHlWX34ghj3hnkZsZG33G7yReSoU2fQBg_RT9vYlMjidQw6XaPJ4YaGl5L_C3VklO3EnNNr8szWU_iGre5X0e5lbdG3eF8fMiYTv6mXvl9XzmgSAcwPXZVc2nYLa-GJJ3Zwm_PfxBYNlY4sY-UXU3SEdGLzmMWrq8EGn44rqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=Ko--432nD17BtNgZRkJQSJL-5rxRxf8z3xZg1BR7rrKHq2byQ-C8tfGwFp2VLV3DNPitvEdzOK270KXF9YLgJ3gT8lZ7Ce5_qZW_G2Mn06N2k3NqdYAMgZ15W8kOTvxljG9PpSzYqrQx0xkzBd9GL_IHgcmq5mAPZmz1XQaB2H22q5NnsDVCbuH5PZuu_vGdwo6PyifWaSXnvRBtXLESvVtUjTFqKh8P_mLg47YX3gHxdMK0wg6pNUzZopXmvgWm0X4OC6G2AcIsx8k5BUns9S0VTjBg_p3OttBL9ZSWfZYY28XneMoQaEoHOXNRzuxymXldyYvSgwpzeBmETdoTYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=Ko--432nD17BtNgZRkJQSJL-5rxRxf8z3xZg1BR7rrKHq2byQ-C8tfGwFp2VLV3DNPitvEdzOK270KXF9YLgJ3gT8lZ7Ce5_qZW_G2Mn06N2k3NqdYAMgZ15W8kOTvxljG9PpSzYqrQx0xkzBd9GL_IHgcmq5mAPZmz1XQaB2H22q5NnsDVCbuH5PZuu_vGdwo6PyifWaSXnvRBtXLESvVtUjTFqKh8P_mLg47YX3gHxdMK0wg6pNUzZopXmvgWm0X4OC6G2AcIsx8k5BUns9S0VTjBg_p3OttBL9ZSWfZYY28XneMoQaEoHOXNRzuxymXldyYvSgwpzeBmETdoTYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=G1FkniiMnRVQh4kUQhMcx0vkwZZcMHXCrNcIEnlwR4zgc7gyxqtKIoLKEXrml421ZtGbIg5_pxWaAPXgro1p7OzXY7q_DSKXW0ZvNgL51U1wJKGN3Ht-GgOoRpokmsTbYb0i47wU64-XfLERluRNDZaox9zjSP53Rbe5_BWkVmR5_HP0ztKjGWE4MD3IagKjEaYyAGqYSZlZRqfVJXthrX0aZSs993xd9zf9YLcuzF44V0h6ywLDcHnHtTzDuCE-rSYsuChlyclxhfhvWNAVPLfPqQoVRL8Q9rxoZ4SUcXWo09xHt9wwj0ziSrw3O2AH50_X2QfxY1SxKHZWA-g5uEGzLFn4L-3NOiFwB-k4OskPQQ3Zt83W-JIr8xRC0pyvTqbattAAd1gv8ZC58LC9zL8r_y9-S4rkOQq9CfgTDET8Ay7-Bi28PS4HeYEpCumfjuMa6GSy4KG8X9ZRwCKWlM3Sy4jh4-_QIWq8i8FcqTowqg3yXfpg2SvT9nnTYftP-g-70vCG-rdwx4qJM3hBCLlpv5P9UgyFw12FlrBv_E2vO1tUu3J6jefWu14oDYNg-2KkdZnLBEH3GOC9yByCIHJgH0NIo7xS_FrN4kuzoOXsfW5jsR48DEjd2y_3kGCBgxRlPzq1HtDBa4f-fcDCNv0MHqvAr3xW8murMXYafQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=G1FkniiMnRVQh4kUQhMcx0vkwZZcMHXCrNcIEnlwR4zgc7gyxqtKIoLKEXrml421ZtGbIg5_pxWaAPXgro1p7OzXY7q_DSKXW0ZvNgL51U1wJKGN3Ht-GgOoRpokmsTbYb0i47wU64-XfLERluRNDZaox9zjSP53Rbe5_BWkVmR5_HP0ztKjGWE4MD3IagKjEaYyAGqYSZlZRqfVJXthrX0aZSs993xd9zf9YLcuzF44V0h6ywLDcHnHtTzDuCE-rSYsuChlyclxhfhvWNAVPLfPqQoVRL8Q9rxoZ4SUcXWo09xHt9wwj0ziSrw3O2AH50_X2QfxY1SxKHZWA-g5uEGzLFn4L-3NOiFwB-k4OskPQQ3Zt83W-JIr8xRC0pyvTqbattAAd1gv8ZC58LC9zL8r_y9-S4rkOQq9CfgTDET8Ay7-Bi28PS4HeYEpCumfjuMa6GSy4KG8X9ZRwCKWlM3Sy4jh4-_QIWq8i8FcqTowqg3yXfpg2SvT9nnTYftP-g-70vCG-rdwx4qJM3hBCLlpv5P9UgyFw12FlrBv_E2vO1tUu3J6jefWu14oDYNg-2KkdZnLBEH3GOC9yByCIHJgH0NIo7xS_FrN4kuzoOXsfW5jsR48DEjd2y_3kGCBgxRlPzq1HtDBa4f-fcDCNv0MHqvAr3xW8murMXYafQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-8oa3MNuV0WjjCn2lmv8DuiZ4l1jCYNEv5zM0I9DjFDeqznzgtR74UtDNo26Evy9qeOwMP2e7bl5AxeZBkfahx3rk_Ps3ISpQh_ZIHeZBrq-G7ZIbIrXAB3M2dYihXv1t5xEOAve_tL7hsGHFwLNeWH0_9YbVOIsTMmJ2WQYNNEMpaDTn_n8l5jlSSF_JGjhIFfadMGpwRHFuoHDU79AdU-1RZXt2MdDazISWkMuwKrS9D79X49Wb2xRqz0cTEPo68bWMdOpaSkXezxlISOjAlAthE2GL3C3k3uNMFx7Axcm-GPVrHnWLFWEW8Yaa9ZeLzEIb03sWRi44uhzdEEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Ft43jYqwQQg4Egf32ar6KlxmsJFt35f_EwGwGj2m8cv7CR9ypFSZMF6oD3uN3yZ0aw23gWjT3mPYX_mSRr872ICHsmR1t3ieW0Ig0DbxeU1VpbM5aU5nC-Gfyudj_jvkI653Vf7-B0PH9rNvw0hpCRT8RyUDWl4YEXPUFVvzexQl-IXMTFcVwcPOdn4kowSPmUYCSC4qMKFfz2Csm08wyQMAX2KzhW9i4TmXPOM5gVAMrf4pgGaRtOkrSsdyOrv9vQMbpE8fN2_L9vQb7luRRn9YrpME-LUek1apMrXEcJTYiWFrDMuPMAFiGqJihFw6bcintYI37aOkZDEKlsiRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Ft43jYqwQQg4Egf32ar6KlxmsJFt35f_EwGwGj2m8cv7CR9ypFSZMF6oD3uN3yZ0aw23gWjT3mPYX_mSRr872ICHsmR1t3ieW0Ig0DbxeU1VpbM5aU5nC-Gfyudj_jvkI653Vf7-B0PH9rNvw0hpCRT8RyUDWl4YEXPUFVvzexQl-IXMTFcVwcPOdn4kowSPmUYCSC4qMKFfz2Csm08wyQMAX2KzhW9i4TmXPOM5gVAMrf4pgGaRtOkrSsdyOrv9vQMbpE8fN2_L9vQb7luRRn9YrpME-LUek1apMrXEcJTYiWFrDMuPMAFiGqJihFw6bcintYI37aOkZDEKlsiRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So4JSD1O8wRnBdK65H0aJltXg_kKl1PrNjX8AQ644Qi_HMRNzfXXlR95HKL8TJmq_EiMf3HduncM2g-DsOiLoOSx45mpaWdJ31Q7jenSe-yqNW4BDHD3j1ddobPIwMiAVy5QOVPQ_ACJU9mUzPziHqZYkO6WcMzluknPnYJn-o9_1NGS0Iw61er5ejl35RPLDAtIq-GHq7W-QsAbzxp_QMq6Loxj8HvOOqA5C1Au4RgX7o-qT_8IAv4xX2UKpbHcjELbAZzoQ3RgTx_rvIyd6Ay3RaohOwFOS5OXqlrUk5SqNyiQPAJWV8Re3LPOao8iQLGM4zZmsLrJsRWQjW_o3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnU_yGHLvZocRkyW7OYAmqbqFIQMZlfghzGfouyAg5ikoYJ13r-s4d76HwERsel1z4ReHrNbVL6lfU5mivcvrWQc2iK9kgb-P-grryWrQVL-tu35smv2IukF8W32I6OkscoMdL0CfBZG_uTm8a_IZQuU6Okdp3gpPqFWT2dqjh7q3wYKjJu-pBKp_Ge0MvAu_Q-bK9alIDyzc9OHmDmfTQyGiLV5OqVfmFLZ_RhbH9ByVJ7AHd4rIdB4GpZ8ZugBeUBfVLCxpxNk7OM66YML8OoQrJQfApGxCzc3Mza_dTR0iB9QypVkU9zV10Sk5LuV9NUxD_XVrShsJOeZOQosxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTMacQl2dMALn_PDFy1BnsSyWSvwk-ltiX7Fd_XfNtqoXd3Wed5hJtTWxnDvbW37m9n6d_TvH38P-V0aW4f0RwknZY28Mmf_VU4zetkrsXMSRb1IC7H-bjYr1NLqKVx8YVLOn7iFo0XbUZ_tKSmXOjAx-wraWSrl0418BnhhV__IOOs72X31an3ae-HrB_tuOmnZP_WBhil0wxvTo-Lx-d1idMfkl3KC8o2xsF1-yGvwV_1YoWKtVyNSGyPNSrJ6yNCGNrw2BgwtTcy3mWwnJSLLfzS76FklhmO9ISIRInRikao0SO6bGiwDbAo37cSo6bzUZU4XgVq8wcbhSay0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qddjfAtBHlVJAL_d5LPVHniXvCWr-TB9_fKUvdM8tucExNdHaXsaYks-6DEtSS66uzBFAdKI88FOR3gdHmbgbDVw3yfJaMNMIhjEy3FUaokeEIzOqVqm4odghhL-hZbenJajSpgqHSNZYyUhhEI9YJBaSKjkOZ0gAkYIVCgqqkmy5c5zmQ3rLgoeY6yzx_aJBIATljVwmZ4OC1NmB8ZrAld-Fidxs1HI7v4lJDTHlDPf0Uzf2xB7cXgKPQJgWGjELDvWMVLtgaKSxhR11fPx1xsCwx6ci8lUcoVm0K9P41P_SVcTdQCQV_QalxqII1V7oyzlz4og7uv1f1_Igf5xBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHlkSkdocVHiD3FAuwcSGpSJtLQ9cfTgoDbpV8ITyRL84jQjouJtzmJz9rCuCtZyNlH7JIGNUnBt9KnKUT54s4zwA9-oRdmZpjZB0dr9jKirHibE2P78u_kbONoOOCMkTR4E2PTFZu7qwbFfOmUuhtWeR4AGnFm69QmZdbQHfsLngYPg0zZnm6aVGvW4vArdMcsN2RQX-GjhIkY0Nb64yqtj4kkYf7QhONusG3JsfRIlpJcsgrn6uD4VhoqnA_QxImFWIZDtrWWDy6oKZOBkpVX6H9bhQvmJ2CFxKqCwehtPbeks9GG57_EdVmC9jysuREQDNnhcfn5a0n2ICMT6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ch8liX3LqK8VxEuODczSXCOd5sglqpK9J2CMvl3elE_7CdO642YyJlnG9srVnB-j0IF3By0P93iqNdkALS2BP6CKaueqMncewKyaIfNdNykcEa-dBMsexP5t0CrEu9IM_z1VaJrI3N9Ou4LTe5H8pARH5excAnw79P2kKMuLSnDeJcJCeM0HHUadY47G41G_tvKhpvr8DQEXoqpP1Z2sZaNOxQI0jcrJ16T6YaYXlgNillYcGOufqm2Fxgajp1JdZz8UZK5MOOrVeHk4A96eO5ksSnq_1htN-yciXZNcmisg5MC6TGHGEvR3jje1ptdJ7W-DvicYABZhvlLF30GFvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=vzc44vpzj5bQwBe1UySvq2qWTrMCS_EqwOhNaP4QsIoKyHm7GpBylchuGrIXwd4AscChW9JN5UZJ5OTgDvQvuf4z_mBC4RtvRjS3vjew33WdHuvdR87Ue6xZkX9SwM6RqE269uu_uzEfQaPdSik60pj6KxZjswsJS-uCkcSSQfabZ2JsQUxkFtR8FaYVZSbHt7q7WCprHyRuvqASgB8_9RP1GSkfR8h4-ECWG6pbN9aPmBWlilamN87aV80bwgd8R3zyNxOvyJ-ZKQKWGR3VNLogQP6HtMmI0wcsuIZSLfKYwzDEDqkM6VDFqOHC1UFX61FTiaL2P4QMfq0H3cbxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=vzc44vpzj5bQwBe1UySvq2qWTrMCS_EqwOhNaP4QsIoKyHm7GpBylchuGrIXwd4AscChW9JN5UZJ5OTgDvQvuf4z_mBC4RtvRjS3vjew33WdHuvdR87Ue6xZkX9SwM6RqE269uu_uzEfQaPdSik60pj6KxZjswsJS-uCkcSSQfabZ2JsQUxkFtR8FaYVZSbHt7q7WCprHyRuvqASgB8_9RP1GSkfR8h4-ECWG6pbN9aPmBWlilamN87aV80bwgd8R3zyNxOvyJ-ZKQKWGR3VNLogQP6HtMmI0wcsuIZSLfKYwzDEDqkM6VDFqOHC1UFX61FTiaL2P4QMfq0H3cbxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=kX6kgM407k_BSnHMfzzJntUUljjmd4EC0BW-mxun90Th2nH5xv4N1-eKWmeNdaG7vuNgiNfa3-MA6d-MzAF08S4mRT-i44_hSoSjMFFtufJoxUoapJg5Gq0vO1pJeqYsx29oQyBM6EwHYXgyyp66hm1zsSfQxtTpXrdOF7OoJRvDDI9pQ3aowNGwufJuZKWYvCsZbCmRfzpMBlRoK2kni8U6aRK2t6plqyPuZmd6CIG-b8W6q0Qe4apgWnMuGAejyeL__GXIquW4Rdu03SHqsLkTpDrLCteGD-nZYfUBkavqj99HsdA20OPoz_DhcKX0BaPpaVqkuL8TGrcOtSlB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=kX6kgM407k_BSnHMfzzJntUUljjmd4EC0BW-mxun90Th2nH5xv4N1-eKWmeNdaG7vuNgiNfa3-MA6d-MzAF08S4mRT-i44_hSoSjMFFtufJoxUoapJg5Gq0vO1pJeqYsx29oQyBM6EwHYXgyyp66hm1zsSfQxtTpXrdOF7OoJRvDDI9pQ3aowNGwufJuZKWYvCsZbCmRfzpMBlRoK2kni8U6aRK2t6plqyPuZmd6CIG-b8W6q0Qe4apgWnMuGAejyeL__GXIquW4Rdu03SHqsLkTpDrLCteGD-nZYfUBkavqj99HsdA20OPoz_DhcKX0BaPpaVqkuL8TGrcOtSlB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Klou2l-Ny0ERR2oIys_2mPjaJSZrTHXhhsfRsbGWFi8eKuCATE5ObzoOHmDEYzuKpFalwZNZSakOjOQEjFnWqqAamlB7c95L5uIPKehjeBzNRtdihqzrjENjrNB__ZC80vzeEle2dzAw1uGFIQ4S1cQ-DIBWFq-IHRNWmsv4z1UGyfEI5u6O6OVnAK45fuLNse7QrPgPPp_t81BfGcv9uCelSkPBLbvNPoyiST80B7dc00NLF8vLaq52X1fHqVsbRMoSZdSyoIWKrHjji-b2sf6zYiMZqCTKDPo6lx5aqQzNPInTxo2XX8WkINfRxU8Eae8DJP452hDNTcVX8ib3zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Klou2l-Ny0ERR2oIys_2mPjaJSZrTHXhhsfRsbGWFi8eKuCATE5ObzoOHmDEYzuKpFalwZNZSakOjOQEjFnWqqAamlB7c95L5uIPKehjeBzNRtdihqzrjENjrNB__ZC80vzeEle2dzAw1uGFIQ4S1cQ-DIBWFq-IHRNWmsv4z1UGyfEI5u6O6OVnAK45fuLNse7QrPgPPp_t81BfGcv9uCelSkPBLbvNPoyiST80B7dc00NLF8vLaq52X1fHqVsbRMoSZdSyoIWKrHjji-b2sf6zYiMZqCTKDPo6lx5aqQzNPInTxo2XX8WkINfRxU8Eae8DJP452hDNTcVX8ib3zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=C0FExDWZ3IbpEofwHsk3psiiL2VAEVRMCmnByPeO_NSxeSe4tHaXukCvRgL7Ci2TzzJhF1dNAtyHqtofksmdGTcMOeuZPyJH7K2uj8RN_eQ5QW-nkCrtB3WACRdQFzUCoS_Hhywh_PSLG1Qn4t72c39rdVrv2CielxfseaddApl1kFqNNo8h1cr_JsVQ-484RMs2BJWmWID79TQhc-O6g-05vg8lxTEAZ2dgLK95kdhcy6rR7XIgX5fjsjFRga-S0dCCDmztQwPsMwynKi1W0y1lC-8TARz05awXEQ72DNterK0yBrjZfQ8CO4YMPneSnwUKhmenvz3_uF17acyM2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=C0FExDWZ3IbpEofwHsk3psiiL2VAEVRMCmnByPeO_NSxeSe4tHaXukCvRgL7Ci2TzzJhF1dNAtyHqtofksmdGTcMOeuZPyJH7K2uj8RN_eQ5QW-nkCrtB3WACRdQFzUCoS_Hhywh_PSLG1Qn4t72c39rdVrv2CielxfseaddApl1kFqNNo8h1cr_JsVQ-484RMs2BJWmWID79TQhc-O6g-05vg8lxTEAZ2dgLK95kdhcy6rR7XIgX5fjsjFRga-S0dCCDmztQwPsMwynKi1W0y1lC-8TARz05awXEQ72DNterK0yBrjZfQ8CO4YMPneSnwUKhmenvz3_uF17acyM2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=uC_hs3K9Hk41WCsNPo7FchKX1H_krY2_L6V9REQBFY6WnPF_8HctX_QctMbQju8IZ9qRpnPLMlODhJcAKnmRHz_ev-VEAkmjnjMidT12VHbMPvYKtOtiJiNuJBoKhwTPXPv52eLQXsGUo9TxxOSsJgPun7l1w1Vdj85pNn7dNcFESegWs6AmdaCafmtKiZfh36ILs5sD59-h4ZXSmP4ae_OOiRVuSTvIpq47qBcjz33frNJfSpwgRzQgpW9Yjzpc-ePo8UUn0I14zltrHzlDRXYwIexbzvN9HvweDe1bGXNdqO9iaqmZS9Un-xinaKuMyNpwmzpVG3Cmt3H2grSC4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=uC_hs3K9Hk41WCsNPo7FchKX1H_krY2_L6V9REQBFY6WnPF_8HctX_QctMbQju8IZ9qRpnPLMlODhJcAKnmRHz_ev-VEAkmjnjMidT12VHbMPvYKtOtiJiNuJBoKhwTPXPv52eLQXsGUo9TxxOSsJgPun7l1w1Vdj85pNn7dNcFESegWs6AmdaCafmtKiZfh36ILs5sD59-h4ZXSmP4ae_OOiRVuSTvIpq47qBcjz33frNJfSpwgRzQgpW9Yjzpc-ePo8UUn0I14zltrHzlDRXYwIexbzvN9HvweDe1bGXNdqO9iaqmZS9Un-xinaKuMyNpwmzpVG3Cmt3H2grSC4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=CnK2luYzCmVw3SlP5T0IKy02lXcwJJSBI1fYPts6lvziN87onxaPE5hC15U532yRfoCxQjMi8-WUVIwVe_790b_8eXYSmorXd5-DanEUVNOr_0XdMiYJnUlQURMTCQICF1JwRZYGP3cqDnd7W2y_O3VGyCh5q2ee28PhocLQ61Ft_pTFy0SyCXUJqdEgV0VoFyqeYh6ydP-x6Q0aZ00yENHOKKGJz2s-9HWVg6jvJ1kPwZ45VmlQzPqXaEHuxjVG8XsIUbEt-_0JQ7_qSWkHm_N6xceuupmw2fURFm6pE4_MSD1r1IrsEABhLPQ1SYPGAXmlsZzyfCvBmVO6KiPlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=CnK2luYzCmVw3SlP5T0IKy02lXcwJJSBI1fYPts6lvziN87onxaPE5hC15U532yRfoCxQjMi8-WUVIwVe_790b_8eXYSmorXd5-DanEUVNOr_0XdMiYJnUlQURMTCQICF1JwRZYGP3cqDnd7W2y_O3VGyCh5q2ee28PhocLQ61Ft_pTFy0SyCXUJqdEgV0VoFyqeYh6ydP-x6Q0aZ00yENHOKKGJz2s-9HWVg6jvJ1kPwZ45VmlQzPqXaEHuxjVG8XsIUbEt-_0JQ7_qSWkHm_N6xceuupmw2fURFm6pE4_MSD1r1IrsEABhLPQ1SYPGAXmlsZzyfCvBmVO6KiPlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrxCL6oK3-noUsIE2eAwm0FER_5GvBG_vEm_wND7_eIs9s77vi8StteebRJoryGrAz3pkGe0Vo1LrgwcTHIFLO7p_i2t4udUa5LjMaAd8FwrEuNlxkXwdL5uQUIdfhdAb_Bdh4RDgWyjSvPKRf-TcHdWgnsOLLWU6km2myGpRUEeU24i5NrCYvV4OVO_cUPWLZZR86FYjCqzuB3xTjEx_p0XBHpuf4bT3VWZFvcxerhek_zhzQsqWstDtSlhzq2MbTKl6kvfRK1W2N74pLkD-dk4kN85_0rnu0xQ27JHvzWuDGyzAFxt4bIvJUTkcfYwIEU30slwG9jVCzobFC_HKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvpacarMet51Fu6bqSvaFvV4Fnrqb2zJ-t0xyucOSOC9vTA6FD9BRX5WNRbOb_pnLekt5TEObwKQWYIFoqW5Y_yitLbECORjUC9L6zA0eREVr-MgdmXL_iPfrpm62c_8_5ilcqPeazLakn5z9HXvflnufsmP42A-R5Wx6P2qxF9lNouTj2nNaA-AP6nwgGa6PvmySCgz3bfPqTswY1yBuydntrT7IZRmd2gyu9zfyTRMN7SlD4wthsUPVL8otgtTZtpWol8G-GUbrtdqMb39xmF9MlEGGrAHvTzPGzd4f9is9rw4qKXMXGE8-sNlHsO5Q7iIK0lEwN7HRwTmvrwYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-AMWPYBhwHALgd7KBX_Rb34yLfGV4owCDpxrvZtrjTEQfyd116CJK_ahUO726LfPM1s_qjpH3_-8gddy0i4BFo0STnnWYWMrU9ei-I8FR-PTahnbLEtAK0CzkrNnvnm67-nH7G8EvMtHoVWpvNPYhxBWHOEScpPajVkVSOqPLd8ZqYy-betW8QDlSPOSqlpt7bhtXaJKEiI4cgwvMcSPh-DKT8sK3kR2y_1A9VbHYZqQMBqFS5t1P1OrXI2LxK4mdsekQl7t1bPvQV8K9ITRBgcX42LAKQjOkHwxl9qRh7LvXO_cgYks7tE9fYHvDtxOw9em925EP1ldzuWrfAc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=dMivWc2ic0sDaZ0icmhOTPwZm8VP3Z5wmqE5mDCUy5SDbF2VdOeaafL0ZXtNOneK44CuqRMhlx3L5xRHGNF3llelHmxy2w4CFSZAHagCjuHSwY7S2eQ74VkSOaW4KPsUnBQG50JIdv31egflYEbDEr8-pzzgT1tC_HwCdM5ERrZ-2tsRats0ka-RTYu5_JMjBOjGyilghn93PjqUvIPcwBQzEjwxFFdLvleXem_V-ADlYyZoAgt-DB8zuniQMsfxqdoYB59I0lNNwxs27kcnlwAEOq21xiF1NTxnDYRrXsjJi3KE5gUw7niCcMpwbESP-AjJ6pM2eRk2K8AVo_VMSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=dMivWc2ic0sDaZ0icmhOTPwZm8VP3Z5wmqE5mDCUy5SDbF2VdOeaafL0ZXtNOneK44CuqRMhlx3L5xRHGNF3llelHmxy2w4CFSZAHagCjuHSwY7S2eQ74VkSOaW4KPsUnBQG50JIdv31egflYEbDEr8-pzzgT1tC_HwCdM5ERrZ-2tsRats0ka-RTYu5_JMjBOjGyilghn93PjqUvIPcwBQzEjwxFFdLvleXem_V-ADlYyZoAgt-DB8zuniQMsfxqdoYB59I0lNNwxs27kcnlwAEOq21xiF1NTxnDYRrXsjJi3KE5gUw7niCcMpwbESP-AjJ6pM2eRk2K8AVo_VMSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fguk3Apj1FB2FdmBIFQKQkpv_uPz2XtBlMGHKkuBx68YaOXSGtYl6C1LOdE1RFGKSlrUgXRvkMgaLIA61mtXhgg5BuSpEare5tP34izWG4yFi7dgflYHSsItLrfs_Mvry3LGOnU23AG0KHBfmwAtXojpJHbrXcmy8goJ2bXta9tFIcSgQkHNy7o0lEg91YJx7_7EQkm5Ekzuy21fKHr6bMP0mX8lcuQiTove8JlEDn84h7nruMi0C6KCPvHQR6Byzt-mIYKs-eoJXY60ZBuzYSOgll1htU2ragQzVgSHKTk50isIo9vhKT4Y-IF1J2nmKoDzE7pygCp432yrHTDfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unqQm7-mlqf3ePV37yng-2yTNnb_MHSxZd45ORLYIPf_PMQnn0EeFd-ipLtA32NY6ocAC0PW_1wR-S6Qh843Hq47q39m0MCOPgg8QAUvCf_e2P9-kL59QdfDMsRxApSiqO66HOS5QaIQHo2QFpCQfs7K9l1UwXyW_KoAM1pIrVAMeyWx_OTuNtpZ9rDoGOqk64qluas6Ott8S9DwnX3uXdeK0bmNFgNCqMb_sIxsbz1F-4WAlj0BxAez_j_Tde10T8c0-hMXNytcPyzhDKY86N7yoo-dlJOQEkUriUszSGGzTzKaiUDY8scKkpSYGZhsDMb90kh5BdvWD9lohsVfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=s74XtvAIR4t3PluYL86P_-Hc9tL0mcUCYHprC12QkEaYJc0psIu0yuwJbpkekwoK-tArdhjNbIU6A5uRKVHmd6WpVKGWcxlYCQk8tdETniiA2H9s6qT5fJ4GFlHDYSlSVIP1ElPTklhY5H8lqO71hTonOYeclP7TV-dakKjkaE0xBpw4apxAKhSKeB4bBBiNmMhKnr8bCYDc5bcOnk7ew8LMTx5sPTE90qGvpT5QxpAwcswKq6t94UGU9js8vUy4vJLArZPVQSmWAkJ4CKxxH53eF6jVYCd7kOoLEfTUymb9chcvpv-Vja6JulMs_eX2OFpkYFhmtJqrizSVunIv5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=s74XtvAIR4t3PluYL86P_-Hc9tL0mcUCYHprC12QkEaYJc0psIu0yuwJbpkekwoK-tArdhjNbIU6A5uRKVHmd6WpVKGWcxlYCQk8tdETniiA2H9s6qT5fJ4GFlHDYSlSVIP1ElPTklhY5H8lqO71hTonOYeclP7TV-dakKjkaE0xBpw4apxAKhSKeB4bBBiNmMhKnr8bCYDc5bcOnk7ew8LMTx5sPTE90qGvpT5QxpAwcswKq6t94UGU9js8vUy4vJLArZPVQSmWAkJ4CKxxH53eF6jVYCd7kOoLEfTUymb9chcvpv-Vja6JulMs_eX2OFpkYFhmtJqrizSVunIv5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzZzS3UtF6hX1Aqy_0iaewJBg413zsK_wUsO8_24hOZAdqpNqQygO6BUurwtZqK_iCxOKHayALEjw_A5JKQEfUhO6-OWVU1p5Usq-pZyRyUI4Jk2DUXentOommqaZuiQpQC99ZEnZikWKp3oJ53yjSq2oP9fTAAc65-CRD2UbmFVZBa3uEEMIVpydiydfu6CF_10DD1NnWqJVKLiVnMsgaS3TnMdgV_yhlJKEOMAFGUdDR9gFoOTNVZu_RgcLoXRAXhUFXWZY9idQOxa6EZtrlsJzZ5jM46rRBW5glWATVUuw0-BQfRj0Cx8I_QyDVJlVtM7M00Vh8hNhabeGq8ZTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGOf5WHAL3zoC2DohfKe-_9S2kqFuGeb5vod-0seBAaR-QuEIsW75DQc9Gc6tSdTItg1CKeq8B4DqBusyG_nr1pUD0Eg0ka81Mkmwm-wNYO_BFoU2slZYbgU6tMyXKcMEfwBOP3uVWbd6lUq13f9HYrYJAVGArqK2O2lZY4pLXCfbWhaNAb2_FSJv4hhVjfB1U1i_tlo2JjpVBfR52DJcGRiFnB5TylwjBqmY_BIdg7JGMoIiuiLWra-afdhKW-p7CMpVrofWNmfTrmoJcJwVEhw0BuqpOoRV8XMdFbely9290pTJIBHXJX6zsdk2wDBfT-8lx0N5W2PcQurVIhwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCtEV6m5FLASbt2ykDSgydEzxfQ2_DSBpDtO6kSTXohpcm9yslEb7QG-aI5rToO5Cpqy20rnG1Hj6G2IqhukQGpYc0thmd3ezjY8-vk-ojukvV2zd4SUeNXrYLgSFTYGwiLuDxOHNJz8RczriVU_XEvACzqOLsor0VzxFigVc-ZC1x-RAyCLsCw1HGh4bXQd8bAeNvYsIJTSyAs60YSeicBv9oJxNjVCI8irHzVw39sfdV5POqh2lR3NMP5032SEpcqYBpyB7UmP2zTkgcLd1pqaKOEc_Sh7xAUcg0D0lTGh3SBwGPKuEnWbhVve58NbD6HUaUnKsJUsMPzlBhiQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS775MURVelGlUF5AvReAQ1wtiyKAEuANROVRqhFI40y7o0tU7FcHENbsPKdocHuFq1obZU4kR_iq_9_zwSQ1cOGRNqodhjeOEdsLn-zp_onERHy1YSJj8_a7EdyqC7noPbgNVE9kaE687Loej0EzOeIO2OuhuvzGbIgO-HDQ_4Hf4MjWZtHA-0KAoTt_lWfLD4wp1bCEUREbvqGF0e6_-3g1MUf_4G9HGCXn7ASMVs54SKnQUS8Y8GwMxH8G8r_1NhRGIV4RP-MbTxXUB4UClUtgbH8Gp6FYe_eXUKAJ8ep8kQeMTOJ7pSMM_pwp1K8-tAQzcfIhpOiILZYZ0c0fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=PnTsVxiS_0GKsqCgQ3M88EII3VXLBuqegPwIEQWuuzxMmue6xlSfquoR1aT3YoQ2hhxD49y01OxiGrf4KJVA9XUXsI9SoWOYJKsoraC3lJXm2pa1Pq58vBNButEa_Mb-rtT9BKY92HjzWmmyriAHMLnlLhalDG1tozaCBaw2cd5Ychf6Axhwta-RC42QY4GRv46RX9rpevNt619i21QYwBNnsGPHAIqilIRHFVfOlgKyRfMw13ZiaVZhtTNoRVYcCzpHoNNz3G-yHz0C6cY4Dvxsr-3vQb2UgFrjbZUtDXvhfS4ZCQpvTjkoh2YVsFRpTY-mk4IaBKcyy1LQWVMDcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=PnTsVxiS_0GKsqCgQ3M88EII3VXLBuqegPwIEQWuuzxMmue6xlSfquoR1aT3YoQ2hhxD49y01OxiGrf4KJVA9XUXsI9SoWOYJKsoraC3lJXm2pa1Pq58vBNButEa_Mb-rtT9BKY92HjzWmmyriAHMLnlLhalDG1tozaCBaw2cd5Ychf6Axhwta-RC42QY4GRv46RX9rpevNt619i21QYwBNnsGPHAIqilIRHFVfOlgKyRfMw13ZiaVZhtTNoRVYcCzpHoNNz3G-yHz0C6cY4Dvxsr-3vQb2UgFrjbZUtDXvhfS4ZCQpvTjkoh2YVsFRpTY-mk4IaBKcyy1LQWVMDcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=FOcKdK_VCOHU5w-1JlCqhQpadpGuTKjV0m-HEfyPPkix8JzunYF5K3kGh0TApOWNLs5mpbU5rqE_GI_IFSw2CZYJbkRYTvjfoVn6uPMUJu5KtJzhD64ktBGKiTRj66yFA4MX4dqhvvGDZwXs-sR9JiHxWc_sgBGpe6TEfVY6jObLt7eqAXqiWTP5RunewvJoGR2Rfe6YxnM9F4pygxKjO12XVG_3IjwB9mf1wPKGPhtmbX-TtlBObmdPyuLMGPa80d6YKRYGS20sOzmjLqQhWf_uMyV-jJ1nB-9VVQZNmUNmHJOdjRCoZeSJpkNcEVdQ5nlVgyR_1NfviWhn4UeN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=FOcKdK_VCOHU5w-1JlCqhQpadpGuTKjV0m-HEfyPPkix8JzunYF5K3kGh0TApOWNLs5mpbU5rqE_GI_IFSw2CZYJbkRYTvjfoVn6uPMUJu5KtJzhD64ktBGKiTRj66yFA4MX4dqhvvGDZwXs-sR9JiHxWc_sgBGpe6TEfVY6jObLt7eqAXqiWTP5RunewvJoGR2Rfe6YxnM9F4pygxKjO12XVG_3IjwB9mf1wPKGPhtmbX-TtlBObmdPyuLMGPa80d6YKRYGS20sOzmjLqQhWf_uMyV-jJ1nB-9VVQZNmUNmHJOdjRCoZeSJpkNcEVdQ5nlVgyR_1NfviWhn4UeN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV6GcU7xiu_ontQ8JL2maFR0U8ON02-ZVlIIZyzWvBg0-k5w5Lm2-lQy-aWK5QaWpfeJ7KOTUkmnYVqm2Ke6bw_578skHVrWBAa6CZqWat0FgavAIOHvRrEW2Cw6K3_9i1aGdtfSkz-ICiABS0hp296Anzk001o_At02up5vKr7w9U7LXcqTcvLt19AD8IiHSCzdDTf_-6s_vFnaEZeBh1BHi7srzEjSj2JCGC2xoctpgHjUXfqEPNcrqbgwuf29uWIs449UjmkI19LnCREPgYh2SXgj-SXXJaOdqIVUisuy-QnqBhYvDg6lQEgwDoGyZ9OCCRZUjhuEptMxtxEUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=Wnpqz5BXN30ihx_YcDuUityTTNAaycoQ5xqaTu2sHIraKboFIb0dyXKPGItJHwr-zQAayYp8v3XOSSRR_8IE0ip2E_ccjbNHTutOzkuBqlRpyPSi8ExLomcgz67RQqrJDA4-xM3v0p8rXXSqWqZCDEX6CKzIvEDd2eR3Vx8GSVIAaFaQO9T8PETApP-7rDJ_3JKAobRHvpU-7Kk0jJIvNicXcTejLbK1aoO_VW604pGnDn4NnO2WyhkrI42AXe3Yme8MEDVOZ_wPxnqkoJasER-Xhm40xQ_91QMo4am6atV8eZ44x45WHiHYux5gCYxLh1-8RhLlTuxiOlOpE8BcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=Wnpqz5BXN30ihx_YcDuUityTTNAaycoQ5xqaTu2sHIraKboFIb0dyXKPGItJHwr-zQAayYp8v3XOSSRR_8IE0ip2E_ccjbNHTutOzkuBqlRpyPSi8ExLomcgz67RQqrJDA4-xM3v0p8rXXSqWqZCDEX6CKzIvEDd2eR3Vx8GSVIAaFaQO9T8PETApP-7rDJ_3JKAobRHvpU-7Kk0jJIvNicXcTejLbK1aoO_VW604pGnDn4NnO2WyhkrI42AXe3Yme8MEDVOZ_wPxnqkoJasER-Xhm40xQ_91QMo4am6atV8eZ44x45WHiHYux5gCYxLh1-8RhLlTuxiOlOpE8BcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=LLl0mGPQhJAsbgU1B3v4TqnmWaeGM5WdpnJJPmi929iYUAlphT6-HfSCFO1AlLcmKotg9RcuBfHydEd36w5hJKL4aTk2Cz3rbTE237ugmAMchePDVjKSv4rhivegl4rUi9sd_JNe8AtzUpyK-YPQMkwyiDMb-m-7mTu73Bb48310yjh5LDeRSypYIF3T6nGf89a7Cs1tSvACdcyXU33r7RTnI09n-37yCk1mkReyyP76DB1AM7BOHmrbdxXwIfrnHYxTjnCFFiI8GjwQNB_hTu_J1orTU1e81W7itBR-JSf9vUPOat5RtcvmXEbOCVAmTi3Dz0u9uFoh46mEc6jLUQG5D5ENkQUkd90fFk7eCuW86rHFZ3acHke1T8GnW8TLqgNw5OsOynRbdiMHvvTU-cuzLORNoTOEFwPZ3eiv6dSnI48ckxzL6P6uXucMdb3I8Ox-MEHBFrHuRwSMS1WzAD6yPJNmsI3eXqgEPE83L9pV0G5yH8VOWeJHjiesmAQ5_-PKecYbFVi8PmjZOUBiTJNQ8yy2zUnpJ44Yj3a7yb3I6ykAZ3hB5agc3CVhNM7juNvSU2S0YCra7ql--B6k6XKgSdKoZR356QEXEM5t520x_iQRXX4B3lGFLdAEp1Na5hbzKuqb8KWEDRJcazAvYYZoS_yoeTbkRREYSALENjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=LLl0mGPQhJAsbgU1B3v4TqnmWaeGM5WdpnJJPmi929iYUAlphT6-HfSCFO1AlLcmKotg9RcuBfHydEd36w5hJKL4aTk2Cz3rbTE237ugmAMchePDVjKSv4rhivegl4rUi9sd_JNe8AtzUpyK-YPQMkwyiDMb-m-7mTu73Bb48310yjh5LDeRSypYIF3T6nGf89a7Cs1tSvACdcyXU33r7RTnI09n-37yCk1mkReyyP76DB1AM7BOHmrbdxXwIfrnHYxTjnCFFiI8GjwQNB_hTu_J1orTU1e81W7itBR-JSf9vUPOat5RtcvmXEbOCVAmTi3Dz0u9uFoh46mEc6jLUQG5D5ENkQUkd90fFk7eCuW86rHFZ3acHke1T8GnW8TLqgNw5OsOynRbdiMHvvTU-cuzLORNoTOEFwPZ3eiv6dSnI48ckxzL6P6uXucMdb3I8Ox-MEHBFrHuRwSMS1WzAD6yPJNmsI3eXqgEPE83L9pV0G5yH8VOWeJHjiesmAQ5_-PKecYbFVi8PmjZOUBiTJNQ8yy2zUnpJ44Yj3a7yb3I6ykAZ3hB5agc3CVhNM7juNvSU2S0YCra7ql--B6k6XKgSdKoZR356QEXEM5t520x_iQRXX4B3lGFLdAEp1Na5hbzKuqb8KWEDRJcazAvYYZoS_yoeTbkRREYSALENjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJgR1l3Z5p9aJm0YeRFLtmxFtH1-vOZDi7zPgdj7IpXkkbjG6h-2iS0pMdFrI1OEwzZ5hG2fJZcq1BVMl8F3SWYMX1smy6sIATrIvBBf6oe31DuSWYvxbTiPsA-4v9CQFUzzMpl8_l4CHaDAC_tFQPqOVGXj_K4NRanZnHwq0Gp--VWO3hWlEjMF9acabIUViRZ1airjIrqGsfiJwCio577WTeWkyufIKkiyowIlwh5CZplexacAQtmLcHXDrTxb5Mel6x9mqm4kzu8UgR9zMd_ZI6JposoEf3rcIJFhW6ZIFvnMnIFxHb86L22xvFoLaQwb6Hf8nxAvQyIES6tj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
